class Voice:
   def __init__(self, name: str):
      self.name = name
   def __repr__(self):
      return f"<storyboard.Voice: {self.name}>";
   def __str__(self):
      return f"{self.name}";
   def __eq__(self, other):
      if isinstance(other, Voice):
         return self.name == other.name
      else:
         return False
   def __ne__(self, other):
      return not self.__eq__(other)

class Bubble:
   def __init__(self, contents: str):
      self.contents = contents
   def __str__(self):
      return f"{self.contents}"
