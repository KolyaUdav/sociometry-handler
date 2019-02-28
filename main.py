from get_data import get_data_from_txt
from generate_data import generate_random_data
from data_controller import run_controller
from load_exel import write_to_exel


name, person1, person2, person3 = generate_random_data()
person_list = run_controller(name, person1, person2, person3)

for person in person_list:
    print(person.name + ': selections: ' + str(person.selections) +
    ', group number: ' + str(person.group_number), ', mutuals: ' + str(person.mutuals))

write_to_exel(person_list)
