# This code is trash. You know it, and i know it.
# Every dev that tries to "optimize" this code, please change the value below.
#
# total_hours_wasted_here = 1
from lexing.lexer import Lexer
from lexing.lexer import LexerError
from lexing.source_line import SourceLine
from parsing.parser import Parser
from util.error import LanguageError

VERSION = 1.0
def main():
    print(f"Welcome to Quaden! To exit, type 'exit()'\nVersion: {VERSION}")
    lexer = Lexer()
    parser = Parser()

    while True:
        line = input("=> ")
        if line == "exit()": break
        if line == "": continue
        try:
            if line == "</>": print("Hello, world!")
        except LexerError:
            pass

        try:
            line = SourceLine(line)
            tokens = lexer.make_tokens(line)
            tree = parser.make_tree(tokens)
            print(tree.interpret())
        except LanguageError as error:
            print(error)

if __name__ == "__main__":
    main()
