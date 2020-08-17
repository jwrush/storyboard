import attr
import json

@attr.s(frozen=True) #frozen means immutable
class Voice(object):
   name = attr.ib()

@attr.s(frozen=True)
class Scene(object):
   description = attr.ib()
   panels = attr.ib()

   def toJson(self):
      dict = attr.asdict(self)
      return json.dumps(dict)

@attr.s(frozen=True)
class Panel(object):
   description = attr.ib()
   bubbles = attr.ib()

@attr.s(frozen=True)
class Bubble(object):
   voice = attr.ib()
   contents = attr.ib()
