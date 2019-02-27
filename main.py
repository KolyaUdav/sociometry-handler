from get_data import get_data_from_txt
from generate_data import generate_random_data
from data_controller import run_controller


name, person1, person2, person3 = generate_random_data()
person_list = run_controller(name, person1, person2, person3)

for person in person_list:
    print(person.name + ': ' + str(person.selections) + ', ' + str(person.status))
