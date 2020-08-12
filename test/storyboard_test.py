from storyboard import *

def test_VoiceClassExists():
   assert Voice

def test_BubbleClassExists():
   assert Bubble

def test_VoiceMadeWithName():
   voice = Voice("Bob")
   assert voice.name == "Bob"

def test_BubbleMadeWithVoiceAndContents():
   voice = Voice("Bob")
   bubble = Bubble(voice, "Hello World!!")
   bubble.voice is voice
   bubble.contents == "Hello World!!"
