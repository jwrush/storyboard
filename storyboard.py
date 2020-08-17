import attr

@attr.s(frozen=True) #frozen means immutable
class Voice(object):
   name = attr.ib()

@attr.s(frozen=True)
class Scene(object):
   description = attr.ib()
   panels = attr.ib()

@attr.s(frozen=True)
class Panel(object):
   description = attr.ib()
   bubbles = attr.ib()

class Bubble:
   def __init__(self, voice: Voice, contents: str):
      self.contents = contents
      self.voice = voice
   def __str__(self):
      return f"{str.upper(self.voice.name)}:\r\n{self.contents}\r\n"
