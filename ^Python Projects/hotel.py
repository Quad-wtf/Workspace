from time import sleep

class Hotel:
    def __init__(self):
        self.rooms = {
            100: {'type': 'Single', 'price': 50, 'booked': False, 'guest': None},
            101: {'type': 'Single', 'price': 50, 'booked': False, 'guest': None},
            202: {'type': 'Double', 'price': 80, 'booked': False, 'guest': None},
            203: {'type': 'Double', 'price': 80, 'booked': False, 'guest': None},
            301: {'type': 'Suite', 'price': 150, 'booked': False, 'guest': None}
        }

    def get_available_rooms(self):
        return {room_no: details for room_no, details in self.rooms.items() if not details['booked']}

    def view_available_rooms(self):
        available_rooms = self.get_available_rooms()
        if available_rooms:
            print("\nAvailable Rooms:")
            for room_no, details in available_rooms.items():
                print(f"Room {room_no}: {details['type']} - ${details['price']} per night")
        else:
            print("\nNo available rooms at the moment.")

    def book_room(self):
        available_rooms = self.get_available_rooms()
        if not available_rooms:
            print("\nNo rooms available to book.")
            return

        self.view_available_rooms()

        try:
            room_no = int(input("\nEnter the room number you want to book: "))
            if room_no in self.rooms and not self.rooms[room_no]['booked']:
                guest_name = input("Enter your name: ")
                self.rooms[room_no]['booked'] = True
                self.rooms[room_no]['guest'] = guest_name
                print(f"\nRoom {room_no} successfully booked for {guest_name}.")
            else:
                print("\nRoom is either not available or already booked.")
        except ValueError:
            print("\nInvalid room number. Please enter a valid room number.")

    def find_booking(self, guest_name):
        return {room_no: details for room_no, details in self.rooms.items() if details['booked'] and details['guest'] == guest_name}

    def check_booking(self):
        guest_name = input("\nEnter guest name to check for bookings: ")
        bookings = self.find_booking(guest_name)

        if bookings:
            for room_no, details in bookings.items():
                print(f"{guest_name} has booked Room {room_no}: {details['type']} - ${details['price']} per night.")
        else:
            print(f"\nNo bookings found for {guest_name}.")

    def check_out(self):
        guest_name = input("\nEnter guest name to check out: ")
        bookings = self.find_booking(guest_name)

        if bookings:
            for room_no in bookings:
                self.rooms[room_no]['booked'] = False
                self.rooms[room_no]['guest'] = None
                print(f"\n{guest_name} has successfully checked out of Room {room_no}.")
        else:
            print(f"\nNo bookings found for {guest_name}.")

    def run(self):
        while True:
            print("\n--- Hotel Booking System ---")
            print("1. View Available Rooms")
            print("2. Book a Room")
            print("3. Check Booking")
            print("4. Check Out")
            print("5. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.view_available_rooms()
                elif choice == 2:
                    self.book_room()
                elif choice == 3:
                    self.check_booking()
                elif choice == 4:
                    self.check_out()
                elif choice == 5:
                    print("\nExiting the Hotel Booking System...")
                    sleep(0.8)
                    break
                else:
                    print("\nInvalid choice. Please enter a valid option.")
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    hotel = Hotel()
    hotel.run()
