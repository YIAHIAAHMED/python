class Hall:
    def __init__(self, hall_no, row, col):
        self.row = row
        self.col = col
        self.hall_no = hall_no
        self.seats = {} # puro structure lagbe , tahole list dorkar
        self.show_list = [] # ki ki show cholbe

    # show add kora
    def enter_show(self, show_id, movie_name, time):
        self.tuple = (show_id, movie_name, time)
        self.show_list.append(self.tuple)
        self.seat_list = []
        for i in range(self.row):
            row = []
            for j in range(self.col):
                row.append('free')
            self.seat_list.append(row)
        self.seats[show_id] = self.seat_list

    def view_show_list(self):
        for x in self.show_list: # x holo tuple r x[0], [1], [2] holo tuple er index
            print('show id: ', x[0], '\t movie: ', x[1], '\t Time: ', x[2])
    def view_available_seats(self, id):
        if id not in self.seats:
            print('wrong show id')
        else:
            print('\n-------------------------------\n')
            for i in self.show_list: #ekhane i holo tuple
                if i[0] == id:
                    print('\n movie: ',i[1], '\t Time: Today ', i[2], end='\n')
            for x in range(self.row):
                for y in range(self.col):
                    if (self.seats[id][x][y] == 'free'):
                        print(f'{chr(x+65)}{y+1}', end='\t' )
                    else:
                        print('X', end='\t')
                print('\n')


    def book_tickets(self, id, name, phone, booking_seats):
        for x in booking_seats:
            r = ord(x[0])-65 # A er ASSCII value 65
            c = ord(x[1])-49 # 1 er ASSCII value 49
            # print(r,c)
            if r >= self.row or c >=self.col or r < 0 or c < 0:
                print('seat doesnt exists.')
            elif self.seats[id][r][c]!= 'free':
                print(x, 'is already booked')
            
            else:
                self.seats[id][r][c] = 'x'




# hall er object
my_hall = Hall(2, 6, 8 )
my_hall.enter_show(147, 'Domm', '10:00 AM')
my_hall.enter_show(205, 'bonolota', '01:00 PM')
my_hall.enter_show(241, 'Rakkhosh', '04:00 PM')
my_hall.enter_show(334, 'Pressure Cooker', '09:00 PM')
        

while True:
    print('\n-------------------------------\n')
    print('1. view all show today.')
    print('2. view available seats.')
    print('3. Book tickets.')
    option = int(input('Enter your option: '))
    if option == 1:
        print('\n-------------------------------\n')
        my_hall.view_show_list()

    elif option == 2:
        id = int(input('Enter show id: '))
        my_hall.view_available_seats(id)

    elif option == 3:
        id = int(input('Enter show id: '))
        name = input('Enter your name: ')
        phone = input('Enter your phone no: ')
        tickets = int(input('Enter number of tickets: '))
        booking_seats =[]
        for i in range(tickets):
            booking_seats.append(input('enter your seat no: '))

        my_hall.book_tickets(id, name, phone, booking_seats)


    else:
        print('wrong option. choose again\n')  