import openpyxl


horizontal_cells = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                    'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                    'Y', 'Z']


def write_to_exel(person_list):
    wb = openpyxl.Workbook()
    sheet = wb.get_sheet_by_name('Sheet')
    write_names(sheet=sheet, list=person_list)
    write_other_person_ids(sheet=sheet, list=person_list)
    write_selected_person(sheet=sheet, list=person_list)
    write_mutuals(sheet=sheet, list=person_list)
    wb.save('sociometry_result.xlsx')


def write_names(sheet, list):
    letter_for_number = horizontal_cells[0]
    letter = horizontal_cells[1]
    cell_number = 2
    person_number = 1
    for person in list:
        index_for_number = letter_for_number + str(cell_number)
        index = letter + str(cell_number)
        sheet[index_for_number] = str(person_number)
        sheet[index] = person.name
        cell_number += 1
        person_number += 1


def write_other_person_ids(sheet, list):
    hc_index = 2
    person_index = 1

    for person in list:
        index = horizontal_cells[hc_index] + '1'
        sheet[index] = str(person_index)
        hc_index += 1
        person_index += 1


def write_selected_person(sheet, list):
    for person in list:
        for other_person in list:
            if other_person.name in person.others:
                selected_index = get_cell(person, other_person)
                sheet[selected_index] = '+'


def write_mutuals(sheet, list):
    for person in list:
        person_name = person.name
        for other_name in person.others:
            for other_person in list:
                if other_person.name is other_name and person_name in other_person.others:
                    sheet[get_cell(person, other_person)] = '+**'


def get_cell(person, other_person):
    letter_bias = 2
    num_bias = 2
    return horizontal_cells[other_person.id + letter_bias] + str(person.id + num_bias)
