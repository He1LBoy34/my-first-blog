class Machine:

    def __init__(self, machine_type=None, engine_condition=None, engine_power=None, brand=None, color=None, model=None,
                 weight=None):
        self.machine_type = machine_type
        self.engine_condition = engine_condition
        self.engine_power = engine_power
        self.brand = brand
        self.color = color
        self.model = model
        self.weight = weight

    def start_engine(self):
        print('Engine is running now!')

    def stop_engine(self):
        print("Engine stopped!")


class Car(Machine):

    def __init__(self, number_of_passengers=4, number_of_doors=4, engine_location='front'):
        super().__init__()
        self.machine_type = 'car'
        self.number_of_passengers = number_of_passengers
        self.number_of_doors = number_of_doors
        self.engine_location = engine_location



    def show_car_specifications(self):
        specifications = {'Type of machine': self.machine_type,
                          'Brand': self.brand,
                          'Model': self.model,
                          'Weight': self.weight,
                          'Engine condition': self.engine_condition,
                          'Engine power': self.engine_power,
                          'Color': self.color,
                          'Number of passengers': self.number_of_passengers,
                          'Number of doors': self.number_of_doors,
                          'Engine location': self.engine_location}
        for specification_key in specifications:
            print(specification_key, ':', specifications[specification_key])

class Human:

    def __init__(self, age=20, sex=male, drivers_license=True):
        self.age = age
        self.sex = sex
        self.drivers_license = drivers_license

class Driver(Human):

    def __init__(self, driving_experience='2 years', favorite_car=None):
        super().__init__()
        self.driving_experience = driving_experience
        self.favorite_car = favorite_car



porsche_cayenne = Car()
porsche_cayenne.brand = 'porsche'
porsche_cayenne.model = 'cayenne S'
porsche_cayenne.weight = '2020 kg'
porsche_cayenne.engine_condition = 'new'
porsche_cayenne.engine_power = '440 h/p'
porsche_cayenne.color = 'black'
porsche_cayenne.number_of_passengers = '5'
porsche_cayenne.number_of_doors = '5'
porsche_cayenne.show_car_specifications()
porsche_cayenne.start_engine()

ivan = Driver

ivan.favorite_car = porsche_cayenne
ivan.favorite_car()
