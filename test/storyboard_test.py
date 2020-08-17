from storyboard import *

def test_VoiceClassExists():
   assert Voice

def test_BubbleClassExists():
   assert Bubble

def test_SceneClassExists():
   assert Scene

def test_PanelClassExists():
   assert Panel

def test_VoiceMadeWithName():
   voice = Voice("Bob")
   assert voice.name == "Bob"

def test_BubbleMadeWithVoiceAndContents():
   voice = Voice("Bob")
   bubble = Bubble(voice, "Hello World!!")
   assert bubble.voice is voice
   bubble.contents == "Hello World!!"

def test_PanelMadeWithDescriptionAndBubbles():
   voice = Voice("Bob")
   bubble = Bubble(voice, "Hello World!!")
   bubble2 = Bubble(voice, "Cats and dogs!!")
   panel = Panel("Test", [bubble, bubble2])

   assert panel.description == "Test"
   assert panel.bubbles[0] is bubble
 
def test_SceneSerialization():
   voice = Voice("Bob")
   bubble = Bubble(voice, "Hello World!!")
   panel = Panel("Panel description", [bubble])
   scene = Scene("Scene description", [panel])

   json = scene.toJson()

   assert json == '{"description": "Scene description", "panels": [{"description": "Panel description", "bubbles": [{"voice": {"name": "Bob"}, "contents": "Hello World!!"}]}]}'
