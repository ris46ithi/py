class house:
    def __init__(self, size = 1200, floors = 1, rooms = 1, windows = 1, balcony = 2):
        print("Enter init")
        self.size = size
        self.floors = floors
        self.rooms = rooms
        self.windows = windows
        self.balcony = balcony
        print("Exit init")

    def house_size(self):
        print("House size is : ", self.size)

    def number_of_floors(self):
        print("Number of floors : ",self.floors)

    def number_of_rooms(self):
        print("Number of rooms : ", self.rooms)

    def number_of_windows(self):
        print("Number of windows : ", self.windows)

    def number_of_balcony(self):
        if self.balcony == 0:
            print("No Balcony present")
        else:
            print("No of Balcony : ", self.balcony)

if __name__ == '__main__':
    my_house = house()
    my_house.house_size()
    my_house.number_of_floors()
    my_house.number_of_rooms()
    my_house.number_of_windows()
    my_house.number_of_balcony()