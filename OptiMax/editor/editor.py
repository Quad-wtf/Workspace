import argparse
import curses
import sys


class Buffer:
    def __init__(self, lines):
        self.lines = lines

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, index):
        return self.lines[index]

    @property
    def bottom(self):
        return len(self) - 1

    def insert(self, cursor, string):
        row, col = cursor.row, cursor.col
        try:
            current = self.lines.pop(row)
        except IndexError:
            current = ''
        new = current[:col] + string + current[col:]
        self.lines.insert(row, new)

    def split(self, cursor):
        row, col = cursor.row, cursor.col
        current = self.lines.pop(row)
        self.lines.insert(row, current[:col])
        self.lines.insert(row + 1, current[col:])

    def delete(self, cursor):
        row, col = cursor.row, cursor.col
        if (row, col) < (self.bottom, len(self[row])):
            current = self.lines.pop(row)
            if col < len(current):
                new = current[:col] + current[col + 1:]
                self.lines.insert(row, new)
            else:
                if row + 1 <= self.bottom:
                    next_line = self.lines.pop(row + 1)
                    new = current + next_line
                    self.lines.insert(row, new)

    def save(self, filename):
        """Save the current buffer content to the file."""
        with open(filename, 'w') as f:
            for line in self.lines:
                f.write(line + '\n')


class Cursor:
    def __init__(self, row=0, col=0, col_hint=None):
        self.row = row
        self._col = col
        self._col_hint = col if col_hint is None else col_hint

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, col):
        self._col = col
        self._col_hint = col

    def _clamp_col(self, buffer):
        self._col = min(self._col_hint, len(buffer[self.row]))

    def up(self, buffer):
        if self.row > 0:
            self.row -= 1
            self._clamp_col(buffer)

    def down(self, buffer):
        if self.row < len(buffer) - 1:
            self.row += 1
            self._clamp_col(buffer)

    def left(self, buffer):
        if self.col > 0:
            self.col -= 1
        elif self.row > 0:
            self.row -= 1
            self.col = len(buffer[self.row])

    def right(self, buffer):
        if self.col < len(buffer[self.row]):
            self.col += 1
        elif self.row < len(buffer) - 1:
            self.row += 1
            self.col = 0


class Window:
    def __init__(self, n_rows, n_cols, row=0, col=0):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.row = row
        self.col = col

    @property
    def bottom(self):
        return self.row + self.n_rows - 1

    def up(self, cursor):
        if cursor.row == self.row - 1 and self.row > 0:
            self.row -= 1

    def down(self, buffer, cursor):
        if cursor.row == self.bottom + 1 and self.bottom < len(buffer) - 1:
            self.row += 1

    def horizontal_scroll(self, cursor, left_margin=5, right_margin=2):
        page_n_cols = self.n_cols - left_margin - right_margin
        n_pages = max((cursor.col - left_margin) // page_n_cols, 0)
        self.col = n_pages * page_n_cols

    def translate(self, cursor):
        return cursor.row - self.row, cursor.col - self.col


def left(window, buffer, cursor):
    cursor.left(buffer)
    window.up(cursor)
    window.horizontal_scroll(cursor)


def right(window, buffer, cursor):
    cursor.right(buffer)
    window.down(buffer, cursor)
    window.horizontal_scroll(cursor)


def editor(stdscr, filename):

    try:
        with open(filename) as f:
            buffer = Buffer(f.read().splitlines())

        window = Window(curses.LINES - 1, curses.COLS - 1)
        cursor = Cursor()

        while True:
            stdscr.erase()

            # Render the text in the window
            for row, line in enumerate(buffer[window.row:window.row + window.n_rows]):
                if row == cursor.row - window.row and window.col > 0:
                    line = "«" + line[window.col + 1:]
                if len(line) > window.n_cols:
                    line = line[:window.n_cols - 1] + "»"
                stdscr.addstr(row, 0, line)

            stdscr.move(*window.translate(cursor))

            # Handle key input
            k = stdscr.getkey()

            if k == "q":
                sys.exit(0)

            elif k == "KEY_LEFT":
                left(window, buffer, cursor)

            elif k == "KEY_DOWN":
                cursor.down(buffer)
                window.down(buffer, cursor)
                window.horizontal_scroll(cursor)

            elif k == "KEY_UP":
                cursor.up(buffer)
                window.up(cursor)
                window.horizontal_scroll(cursor)

            elif k == "KEY_RIGHT":
                right(window, buffer, cursor)

            elif k == "\n":  # Newline behavior
                buffer.split(cursor)
                right(window, buffer, cursor)

            # Handle Backspace key
            elif k == chr(8):
                if cursor.col == 0:
                    buffer.delete(cursor)
                    left(window, buffer, cursor)
                else:
                    buffer.delete(cursor)
                    left(window, buffer, cursor)
                

            elif k == "KEY_DELETE":
                buffer.delete(cursor)
                right(window, buffer, cursor)

            # Handle ^S for saving (Ctrl+S).
            elif k == chr(19):  # ASCII for Ctrl+S
                buffer.save(filename)
                stdscr.addstr(0, 0, "File saved successfully!")
                stdscr.refresh()

            else:
                buffer.insert(cursor, k)
                for _ in k:
                    right(window, buffer, cursor)

    except Exception as e:
        stdscr.addstr(0, 0, f"Error: {e}")
        stdscr.refresh()
        stdscr.getkey()
        return  # Returning to the shell if there is an error


if __name__ == "__main__":
    curses.wrapper(editor)
