#21. Create a class FileManager with methods to read from and write to a file
#class FileManager:
    #def read(self):
        #with open("text.txt","r") as f:
            #print(f.readlines())

    #def write(self):
        #with open("text.txt","a") as f:
            #print(f.write(" new file"))

#a = FileManager()
#a.write()
#a.read()
#__________________________________________________________________________________________

#22. Create a class Log with methods to write error messages to a log file.
#class Log:
    #def log_error(self):
        #with open("log file.txt","r") as f:
            #print(f.readlines())


#ali = Log()
#ali.log_error()

#_______________________________________________________________
#23. Create a class Config that reads configuration settings from a file and provides methods to access
#these settings.

#class Config:
    #def read(self):
        #with open("configuration setings.txt","r") as f:
            #print(f.__dir__())

    #def access_dir(self):
        #with open("configuration setings.txt","r+") as f:
            #print(f.__dir__())

#label=Config()
#label.access_dir()
#___________________________________________________________________________________________________________
#24. Create a class Database that connects to a database and provides methods to execute queries.
#Handle exceptions if the connection fails.
#list = ["ali","abbas","sara","aziz"]
#class Database:
    #global list

    #def queries(self,name):
        #try:
            #for i in list:
                #if i == n:
                    #print(f"your name is{name}")

        #except:
            #print("connection fails")

#jawad = Database()
#jawad.queries("jawad")
#_____________________________________________________________________________________________________________
#25. Create a class Report that generates a report from data in a file. Provide methods to handle
#exceptions if the file does not exist or cannot be read

#class Report:
    #try:
        #def generate_data(self):
            #with open("dat.txt","r") as f:
                #print(f.readlines())


    #except FileNotFoundError :
         #print("file does not exist or can not read")

#new=Report()
#new.generate_data()
#_______________________________________________________________________________________________________
#26. Create a class Ticket for a movie theater with attributes movie_name, seat_number, and price.
#Provide methods to display ticket details and apply discounts
#class Ticket:
    #def __init__(self,movie_name,seat_number,price):
        #self.movie_name =movie_name
        #self.seat_number=seat_number
        #self.price=price

    #def __repr__(self):
        #return f"{self.movie_name} {self.seat_number} {self.price}"
    #def discount(self,d):
        #print(f" real price{self.price} discounnt {(self.price)//d * 300//d}")

#killer = Ticket("Killer",34,200)
#print(killer.discount(20))
#______________________________________________________________________________________
#27. Create a class ShoppingCart with methods to add, remove, and display items. Each item should
#be an object of a class Item with attributes name and price.
#dir_car = ["a",3000,"b",2000]
#class ShoppingCar:
    #def __init__(self,name,price):
        #self.name = name
        #self.price = price

    #global dir_car
    #def __repr__(self):
        #return f"{self.name} {self.price}"

    #def add(self,name):
        #dir_car.append()
        #print(dir_car)

    #def remove(self,name):
       # for i in dir_car:
                #if i == name:
                    #dir_car.remove(i)
                    #print(dir_car)


#a = ShoppingCar("A",200000)
#print(a.remove("b"))
#__________________________________________________________________________________________________

#28. Create a class Restaurant with attributes name and menu (a list of Item objects). Provide
#methods to add and remove items from the menu.

#list_menu= ["rice","bean"]
#class Restaurant:
    ##self.name=name
        #self.menu=menu
        #global list_menu
    #def add(self,name):
        #list_menu.append(name)

    #def remove(self,name):
        #for i in list_menu:
            #if i == name:
                #list_menu.remove(i)

#mail = Restaurant("mail","menu1")
#mail.remove("bean")
#print(list_menu)
#________________________________________________________________________________
#29. Create a class Flight with attributes flight_number, destination, and passengers (a list of Person
#objects). Provide methods to add and remove passengers.
#list_passenger=["ali","sara"]
#class Flight:
    #def __init__(self,flight_number, destination,passengers):
        #self.passengers =passengers
        #self.destination =destination
        #self.flight_number=flight_number

    #def add(self,passengers):
        #list_passenger.append(passengers)


    #def remove(self,passengers):
        #for i in list_passenger:
            #if i == passengers:
                #list_passenger.remove(i)


#a = Flight(21,"KABUL","ali")
#a.add("aziz")
#a.remove("ali")
#print(list_passenger)
#________________________________________________________________________________________________

#30. Create a class Hotel with attributes name and rooms (a list of Room objects). Each Room
#should have attributes room_number and is_occupied. Provide methods to book and check_out rooms.

#list_rooms=["room1","room2","room3"]
#book_list =[]
#class Hotel:
    #def __init__(self,name):
        #self.name = name


#class Rooms:
    #def __init__(self, name,room_number,is_occupied):
        #Hotel.__init__(self,name)
        #self.is_occupied=is_occupied
        #self.room_number=room_number

    #def book(self,room):
        ##print(book_list)

    #def check_out(self,name):
        #print(f"{name} check_out")

#room1 = Rooms("room1",23,"seized")
#room1.book("room1")







