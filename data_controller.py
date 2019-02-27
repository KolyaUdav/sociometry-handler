from data_model import Person


class PersonController:
    @staticmethod
    def add_person_to_list(name, person1, person2, person3):
        person_list = []
        for name, person1, person2, person3 in zip(name, person1, person2, person3):
            person_list.append(Person(name=name, person1=person1, person2=person2, person3=person3))

        return person_list

    @staticmethod
    def count_selections(person_list):
        for person in person_list:
            for other_person in person_list:
                if person.name in other_person.others:
                    person.selections += 1

        return person_list

    @staticmethod
    def calculate_status(person_list):
        for person in person_list:
            person.status = person.selections / (len(person_list) - 1)

        return person_list


def run_controller(name, person1, person2, person3):
    person_list = PersonController.add_person_to_list(name, person1, person2, person3)
    person_list = PersonController.count_selections(person_list)
    person_list = PersonController.calculate_status(person_list)

    return person_list
