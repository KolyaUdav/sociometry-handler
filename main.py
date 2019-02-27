from get_data import get_data_from_txt
from generate_data import generate_random_data
from data_controller import PersonController as pc


name, person1, person2, person3 = generate_random_data()
person_list = pc.add_person_to_list(name, person1, person2, person3)
person_list = pc.count_selections(person_list)

for person in person_list:
    print(person.name + ': ' + str(person.selections))
