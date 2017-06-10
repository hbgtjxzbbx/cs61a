test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla', 'Model S')
          >>> johns_car.model
          'Model S'
          >>> johns_car.gas = 10
          >>> johns_car.drive()
          'Tesla Model S goes vroom!'
          >>> johns_car.drive()
          'Tesla Model S cannot drive!'
          >>> johns_car.fill_gas()
          Your car is full.
          >>> johns_car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          2
          >>> johns_car.headlights
          2
          >>> Car.headlights = 3
          >>> johns_car.headlights
          3
          >>> johns_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla', 'Model S')
          >>> johns_car.wheels = 2
          >>> johns_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> johns_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(johns_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          >>> MonsterTruck.drive(johns_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> colins_car = MonsterTruck('Monster', 'Batmobile')
          >>> colins_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          238e48b17a8085331a1d671045b7a572
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> Car.drive(colins_car) # Type Error if an error occurs and Nothing if nothing is displayed
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> MonsterTruck.drive(colins_car) # Type Error if an error occurs and Nothing if nothing is displayed
          238e48b17a8085331a1d671045b7a572
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> Car.rev(colins_car) # Type Error if an error occurs and Nothing if nothing is displayed
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class FoodTruck(MonsterTruck):
          ...    delicious = 'meh'
          ...    def serve(self):
          ...        if FoodTruck.size == 'delicious':
          ...            print('Yum!')
          ...        if self.food != 'Tacos':
          ...            return 'But no tacos...'
          ...        else:
          ...            return 'Mmm!'
          >>> taco_truck = FoodTruck('Tacos', 'Truck')
          >>> taco_truck.food = 'Guacamole'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          b0ffc1b07af4eb85e09c4128f5bf5207
          # locked
          >>> taco_truck.food = taco_truck.make
          >>> FoodTruck.size = taco_truck.delicious
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          084d4fea107bee8c8124cf8d541ff942
          # locked
          >>> taco_truck.size = 'delicious'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          084d4fea107bee8c8124cf8d541ff942
          # locked
          >>> FoodTruck.pop_tire() # Type Error if an error occurs and Nothing if nothing is displayed
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> FoodTruck.pop_tire(taco_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          75e7eb45dffa5d30654f02570401dfe8
          # locked
          >>> taco_truck.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          238e48b17a8085331a1d671045b7a572
          179a547aff949801cac7a48bc120aa4d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
