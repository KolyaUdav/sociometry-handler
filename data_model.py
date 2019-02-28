class Person:
    id = 0
    name = ''
    others = []
    selections = 0
    status = 0
    mutuals = 0
    group_number = 0

    def __init__(self, id, name, person1, person2, person3):
        self.id = id
        self.name = name
        self.others = [
            person1,
            person2,
            person3
        ]
