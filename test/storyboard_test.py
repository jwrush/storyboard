from storyboard import *

def test_VoiceClassExists():
   assert Voice

def test_BubbleClassExists():
   assert Bubble

def test_VoiceMadeWithName():
   voice = Voice("Bob");
   assert voice.name == "Bob"
