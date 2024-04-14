
# def file_to_list(f_sourcedir) : 
#     f_source = open(f_sourcedir)
#     sourcelist = [] 
#     source = f_source.readlines() 
#     for x in source : 
#         words = [word.strip() for word in x.split()]
#         sourcelist.append(words)
#     unique_list = [sublist for sublist in sourcelist if sublist]
#     f_source.close() 
#     return unique_list
from exceptions import * 
import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns a list of dictionaries containing its content.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: A list of dictionaries containing the JSON data.
    """
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print("File not found:", file_path)
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from file:", file_path)
        return []

def write_json_file(data , file_path) : 
    # Write JSON data to file
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)
    print("JSON data has been written to", file_path)

def file_to_list(f_sourcedir) : 
    f_source = open(f_sourcedir)
    source = f_source.readlines() 
    f_source.close() 
    return source

def remove_element_from_list(element, my_list):
    while element in my_list:
        my_list.remove(element)
    return my_list

def fix_list(list) : 
    for x in range(len(list)) : 
        if list[x].find('\\n') : 
            list[x] = list[x][:-1]
        list[x] = list[x].strip() 
    list = remove_element_from_list('' , list) 
    return list 

def file_to_fixed_list(sourceFile) : 
    list = file_to_list(sourceFile)
    list = fix_list(list) 
    return list 

def string_to_list(str) : 
    str = str.split(' ')
    str = remove_element_from_list('' , str)
    return str 


def file_to_dict(sourceFile) : 
    opcodelist = file_to_fixed_list(sourceFile) 
    result_dict = {} 
    for i in range(len(opcodelist)) : 
        opcodelist[i] = string_to_list(opcodelist[i])
        result_dict.update({opcodelist[i][0] : opcodelist[i][1]})

    return result_dict

def is_just_comment(str) : 
    if str[0] == '.' or str[0] == '/' : 
        return True 
    else :
        return False 


def program_length_hexa(first_hexa_locaiton , last_hexa_location) : 
    return hex(int(last_hexa_location , 16) - int(first_hexa_locaiton , 16))

def ascii_to_hex(char):
    hex_representation = hex(ord(char))
    return hex_representation

def string_to_hex_string(string):
    hex_string = '' 
    for x in string : 
        hex_string += ascii_to_hex(x)[2:]
    return hex_string


def write_list_of_dicts_to_file(list_of_dicts, filename):
    if not list_of_dicts:
        print("List of dictionaries is empty. Nothing to write.")
        return

    # Extract column names from the keys of the first dictionary
    column_names = list(list_of_dicts[0].keys())

    with open(filename, 'w') as csvfile:
        # Write the column names (keys of the dictionaries) as the first row
        csvfile.write(' '.join([column.ljust(12) for column in column_names]) + '\n')
        
        # Write the values of each dictionary as rows in the file
        for record in list_of_dicts:
            row_values = [str(record[column]).ljust(12) for column in column_names]
            csvfile.write(' '.join(row_values) + '\n')


def write_list_to_file(list_of_strings, filename):
    with open(filename, 'w') as file:
        for string in list_of_strings:
            file.write(string + '\n')






