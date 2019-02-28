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

    @staticmethod
    def count_mutuals(person_list):
        for person in person_list:
            person_name = person.name
            for other_name in person.others:
                for other_person in person_list:
                    if other_person.name is other_name and person_name in other_person.others:
                        person.mutuals += 1

        return person_list

    @staticmethod
    def group_distribution(person_list):
        avg_selection = (len(person_list) * 3 / len(person_list))
        for person in person_list:
            if (avg_selection * 2) <= person.selections:
                person.group_number = 1
            elif (avg_selection * 1.5) <= person.selections:
                person.group_number = 2
            elif avg_selection <= person.selections:
                person.group_number = 3
            elif (avg_selection / 1.5) <= person.selections:
                person.group_number = 4
            elif (avg_selection / 2) < person.selections or person.selections is 0:
                person.group_number = 5

        return person_list



def run_controller(name, person1, person2, person3):
    person_list = PersonController.add_person_to_list(name, person1, person2, person3)
    person_list = PersonController.count_selections(person_list)
    person_list = PersonController.calculate_status(person_list)
    person_list = PersonController.count_mutuals(person_list)
    person_list = PersonController.group_distribution(person_list)

    return person_list
