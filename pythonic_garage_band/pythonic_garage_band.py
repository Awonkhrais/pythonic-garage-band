# from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod

class Band :
    
    bands=[]


    def __init__(self,name,members):
        self.name=name
        self.members=members
    

    # def play_solos(self):
    #     solos = []
    #     for member in self.members:





class Musician:
  def __init__(self, name, instrument, type):
      
    self.name = name
    self.instrument = instrument
    self.type = type

  def get_instrument(self):

    return self.instrument

  def __str__(self):

    return f'My name is {self.name} and I play {self.instrument}'

  def __repr__(self):

    return f'{self.type} instance. Name = {self.name}'




class Guitarist(Musician):
    def __init__(self, name):
      super().__init__(name, 'guitar', 'Guitarist')
    
    def play_solo(self):
      return 'face melting guitar solo'



class Bassist(Musician):
    def __init__(self, name):
      super().__init__(name, 'bass', 'Bassist')

    def play_solo(self):
      return 'bom bom buh bom'


class Drummer(Musician):
    def __init__(self, name):
      super().__init__(name, 'drums', 'Drummer')

    def play_solo(self):
      return 'rattle boom crash'