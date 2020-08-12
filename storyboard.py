import attr

@attr.s(frozen=True)
class Voice(object):
   name = attr.ib();

class Bubble:
   def __init__(self, voice: Voice, contents: str):
      self.contents = contents
      self.voice = voice
   def __str__(self):
      return f"{str.upper(self.voice.name)}:\r\n{self.contents}\r\n"
