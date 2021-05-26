from constructor import house

class house_gf_2bhk(house):
    def __init__(self):
        super().__init__(rooms=2)

class house_ff_2bhk(house):
    def __init__(self):
        super().__init__(rooms=2, floors=2, balcony=1)


if __name__ == '__main__':
    gf_house = house_gf_2bhk()
    print("Single floor house")
    gf_house.house_size()
    gf_house.number_of_floors()
    gf_house.number_of_rooms()
    gf_house.number_of_windows()
    gf_house.number_of_balcony()

    print("\nFirst floor house")
    ff_house = house_ff_2bhk()
    ff_house.house_size()
    ff_house.number_of_floors()
    ff_house.number_of_rooms()
    ff_house.number_of_windows()
    ff_house.number_of_balcony()