class Person:
  def __init__(self, name, strength, const, skill):
    self.name = name
    self.strength = strength
    self.const = const
    self.skill = skill
    
    self.hp     = self.strength * self.const
    self.max_hp = self.strength * self.const
    self.mp     = self.skill * self.const
    self.max_mp = self.skill * self.const
    self.df     = self.const
    self.atk    = self.strength * self.skill