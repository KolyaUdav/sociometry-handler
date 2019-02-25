class Person:
    name = ''
    others = []
    selections = 0

    def __init__(self, name, person1, person2, person3):
        self.name = name
        self.others = [
            person1,
            person2,
            person3
        ]
