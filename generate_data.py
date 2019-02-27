import pandas as pd
import random


def generate_random_data():
    data = pd.read_csv('names.txt')
    data_name = data['NAME']

    random_person_list = []

    random_person_list = generate_other_person_list(names=data_name)

    return (data_name, random_person_list[0],
        random_person_list[1],
        random_person_list[2])


def generate_other_person_list(names):
    list = []
    sublist1 = []
    sublist2 = []
    sublist3 = []

    name_list_length = len(names)
    index = 0

    while index < name_list_length:
        sublist1.append(generate_name(name_list=names, index=index))
        sublist2.append(generate_name(name_list=names, index=index,
            name1=sublist1[index]))
        sublist3.append(generate_name(name_list=names, index=index,
            name2=sublist2[index]))

        index += 1

    list.append(sublist1)
    list.append(sublist2)
    list.append(sublist3)

    return list


def generate_name(name_list, index, **kwargs):
    while True:
        name = name_list[random.randint(0, len(name_list) - 1)]

        if name is not name_list[index]:
            name1 = kwargs.get('name1', 0)
            name2 = kwargs.get('name2', 0)

            if name1 is not 0 and name is not name1:
                return name

            if name2 is not 0 and name is not name2:
                return name

            if name1 is 0 and name2 is 0:
                return name
