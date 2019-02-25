import pandas as pd


def get_data_from_txt():
    data = pd.read_csv('sociometry_data.txt')
    data_name = data['NAME']
    data_person1 = data['PERSON1']
    data_person2 = data['PERSON2']
    data_person3 = data['PERSON3']

    return (data_name, data_person1, data_person2, data_person3)
