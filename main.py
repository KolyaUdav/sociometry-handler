from get_data import get_data_from_txt
from data_controller import PersonController as pc


name, person1, person2, person3 = get_data_from_txt()
person_list = pc.add_person_to_list(name, person1, person2, person3)
person_list = pc.count_selections(person_list)

for person in person_list:
    print(person.name + ': ' + str(person.selections))
