from mycroft import MycroftSkill, intent_file_handler


class Helloyoutube(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('helloyoutube.intent')
    def handle_helloyoutube(self, message):
        self.speak_dialog('helloyoutube')


def create_skill():
    return Helloyoutube()

