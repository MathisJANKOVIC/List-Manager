class ListElement:
    def __init__(self, name, content=[]):
        self.name = name
        self.content = content

    def add(self, element):
        self.content.append(element)

    def remove(self, element):
        self.content.remove(element)

    def empty(self):
        self.content.clear()