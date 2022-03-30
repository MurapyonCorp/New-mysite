class Car(object):
  def __init__(self, model = None):
    self.model = model
  def run(self):
    print('run')

class ToyotaCar(Car):
  pass

class TeslaCar(Car):
  def __init__(self, model = 'Model S', enable_auto_run = False):
    super().__init__(model)
    self.enable_auto_run = enable_auto_run
  def auto_run(self):
    print('auto run')

car = Car()
car.run()

print('------------------')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()
print('------------------')
tesla_car = TeslaCar('Model S')
tesla_car.run()
tesla_car.auto_run()