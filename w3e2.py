import os
import csv


class BaseCar:

    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(BaseCar):

    def __init__(self, brand, photo_file_name, carrying,
                 passanger_seats_count):
        super().__init__('car', brand, photo_file_name, carrying)
        self.passanger_seats_count = passanger_seats_count


class Truck(BaseCar):

    def __init__(self, brand, photo_file_name, carrying,
                 body_length, body_width, body_height):
        super().__init__('truck', brand, photo_file_name, carrying)
        self.body_height = body_height
        self.body_width = body_width
        self.body_length = body_length

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width


class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__('spec_machine', brand, photo_file_name, carrying)
        self.extra = extra


def parse_whl(whl):
    return [float(x) for x in whl.split('x')]


def get_car_list(csv_filepath):
    car_list = []
    with open(csv_filepath) as csv_f:
        reader = csv.reader(csv_f, delimiter=';')
        next(reader)
        for row in reader:
            try:
                brand = row[1]
                photo_file_name = row[3]
                carrying = float(row[5])
                if row[0] == 'car':
                    passanger_seats_count = int(row[2])
                    car_list.append(Car(brand, photo_file_name, carrying,
                                        passanger_seats_count))
                elif row[0] == 'truck':
                    whl = parse_whl(row[4])
                    car_list.append(Truck(brand, photo_file_name, carrying,
                                          *whl))
                elif row[0] == 'spec_machine':
                    extra = row[6]
                    if extra:
                        car_list.append(SpecMachine(brand, photo_file_name,
                                                    carrying, extra))
                else:
                    raise ValueError("incorrect car_type")
            except Exception as err:
                print(err)
                continue
    return car_list
