import os 

os.chdir('EnergyBotApp')

from EnergyBotApp import TalkyChatbot




def test_talky_init():
    talky = TalkyChatbot()
    assert talky is not None
    assert talky.current_step == "greetings"
    assert talky.is_finished is False

def test_talky_greetings():
    talky = TalkyChatbot()
    assert talky.greetings() == [talky.script["greetings"]["question"]]




