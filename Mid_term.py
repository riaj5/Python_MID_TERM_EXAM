class Star_Cinema:
    __hall_list = []
    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)
    
    

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)

        seat_allocate = []
        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append('free')
            
            seat_allocate.append(row)

        self.__seats[id] = seat_allocate

    def book_seats(self, id, seat_list):
        if id not in self.__seats:
            print(f"The show of ID: {id} is not found!")
            return

        seat_allocation = self.__seats[id]

        for row, col in seat_list:
            if row >= self.__rows or col >= self.__cols or row < 0 or col < 0:
                print(f"Error: Please enter valid row and column number.")
            elif seat_allocation[row][col] == "free":
                seat_allocation[row][col] = "booked"
                print(f"Seat ({row}, {col}) booked successfully.")
            else:
                print(f"Seat ({row}, {col}) is already booked.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows are currently running.")
        else:
            for show in self.__show_list:
                id, movie_name, time = show
                print(f"ID: {id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, id):
        if id not in self.__seats:
            print(f"The show with ID: {id} is not found.")
            return

        seat_allocation = self.__seats[id]
        for row in range(self.__rows):
            for col in range(self.__cols):
                if seat_allocation[row][col] == 'free':
                    print(f"Seat ({row}, {col}) is available.")

    



Hall_1 = Hall(5, 5, 1)
Hall_1.entry_show(505, "Inception", "7:00 PM")
Hall_1.entry_show(102, "Interstellar", "9:00 PM")


while True:
    print("\n---> Cinema Ticket Booking System --->\n")
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")

    ch = int(input("Enter a valid option: "))
    if ch == 1:
        Hall_1.view_show_list()
    elif ch == 2:
        show_id = int(input("Enter the show ID: "))
        Hall_1.view_available_seats(show_id)
    elif ch == 3:
        show_id = int(input("Enter the show ID: "))
        No_of_tickets = int(input("Enter the number of seats you want: "))
        seat_list = []
        
        for i in range(No_of_tickets):
            row = int(input(f"Enter seat row: "))
            col = int(input(f"Enter seat column: "))
            seat_list.append((row, col))
        Hall_1.book_seats(show_id, seat_list)
    
    elif ch == 4:
        print("Thanks, Our Valuable Customer.")
        break
    else:
        print("Invalid option entered. Please select the right option.")
