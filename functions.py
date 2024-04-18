
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

def swap(x , y) : 
    temp = x 
    x = y 
    y = temp 

def write_list_of_dicts_to_file(list_of_dicts, filename):
    if not list_of_dicts:
        print("List of dictionaries is empty. Nothing to write.")
        return

    # Extract column names from the keys of the first dictionary
    column_names = list(list_of_dicts[0].keys())
    comment = column_names.pop(4) 
    column_names.append(comment) 

    with open(filename, 'w') as csvfile:
        # Write the column names (keys of the dictionaries) as the first row
        csvfile.write(' '.join([column.ljust(12) for column in column_names]) + '\n')
        
        # Write the values of each dictionary as rows in the file
        for record in list_of_dicts:
            row_values = [str(record[column]).ljust(12) for column in column_names]
            csvfile.write(' '.join(row_values) + '\n')
    print("the file {} has already been written".format(filename))

def write_list_to_file(list_of_strings, filename):
    with open(filename, 'w') as file:
        for string in list_of_strings:
            file.write(string + '\n')
    print("the file {} has already been written".format(filename))

def merge_string_list(list) : 
    strlist = '' 
    for x in list :
        strlist += ' ' + x 
    return strlist



def filter_string_line(string_line ,lineCounter,  opcodes_and_directives , solo_opcodes) : 
    comment = '' 
    label = '' 
    opcode = '' 
    operand = '' 
    line = string_to_list(string_line)  

    if is_just_comment(line[0]) : 
        comment = merge_string_list(line)   

    else : 
        if len(line) == 1 : 
            word1 = line[0]
            
            if word1 not in opcodes_and_directives : 
                raise OpcodeError("the opcode is missed in line {}".format(lineCounter))
            else : 
                opcode = word1
                if opcode not in solo_opcodes : 
                    raise OperandError("the operand is missed in line {}".format(lineCounter))
                 
        elif len(line) == 2 : 
            word1 = line[0] 
            word2 = line[1] 
            # op_index = opcode_index(line , opcodes_and_directives)

            if is_just_comment(word2) :

                comment = word2 

                if word1 not in opcodes_and_directives : #if word 1 is not opcode 
                    raise OpcodeError("opcode is missed in line {}".format(lineCounter))
                else : 
                    opcode = word1 
                    if opcode not in solo_opcodes : 
                        raise OperandError("operand is missed in line {}".format(lineCounter))
            else  : # word 2 is not comment 
                if word1 in opcodes_and_directives : 
                    opcode = word1
                    if opcode in solo_opcodes and opcode != "END" :
                        raise OperandError("Operand is written error, or you forgot to insert \".\" befor the comment in line {}"
                                        .format(lineCounter))
                    else : 
                        operand = word2
                        if operand in opcodes_and_directives : 
                            raise DuplicatedOpcode("Error Opcode is written on operand field in line {}".format(lineCounter))
                else : #word 1 is label 
                    if word2 not in opcodes_and_directives : 
                        raise OperandError("Operand is missed in line {}".format(lineCounter))
                    else : 
                        label = word1 
                        opcode = word2 

        elif len(line) == 3 : 
            word1 = line[0] 
            word2 = line[1] 
            word3 = line[2] 

            if word1 in opcodes_and_directives :
                opcode = word1 
                if is_just_comment(word2) : 
                    comment = merge_string_list(line[1:])
                    if opcode not in solo_opcodes :
                        raise OperandError("Operand is missed in line {}".format(lineCounter))
                else : 
                    if opcode in solo_opcodes : 
                        raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                        .format(lineCounter))
                    else : 
                        if is_just_comment(word3) : 
                            comment = merge_string_list(line[2:])
                            operand = word2 
                        else : 
                            raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                        .format(lineCounter))
            else : #word 1 is label 
                if is_just_comment(word2) : 
                    comment = merge_string_list[1:]
                    raise OperandError("opcode is missed in line {}".format(lineCounter))
                else : #word 2 not comment 
                    if word2 not in opcodes_and_directives : 
                        raise OpcodeError("Opcode is missed in line {}".format(lineCounter))
                    else : 
                        label = word1 
                        opcode = word2 
                        if opcode in solo_opcodes : 
                            if not is_just_comment(word3) : 
                                raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                        .format(lineCounter))
                            else : 
                                comment = word3 
                        else : 
                            if is_just_comment(word3) : 
                                raise OperandError("Operand is missed in line {}".format(lineCounter))
                            else : 
                                operand = word3 
        else : #line length > 3 
            word1 = line[0] 
            word2 = line[1] 
            word3 = line[2] 
            word4 = line[3]
            if word1 in opcodes_and_directives : 
                opcode = word1 
                if is_just_comment(word2) : 
                    comment = merge_string_list[1:]
                    if operand not in solo_opcodes : 
                        raise OperandError("Operand is missed in line {}".format(lineCounter))
                else : #if word 2 is operand 
                    operand = word2 
                    if  operand not in opcodes_and_directives : 
                        if operand in solo_opcodes : 
                            raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                        .format(lineCounter))
                        else : 
                            if is_just_comment(word3) : 
                                comment = merge_string_list[2:]
                                operand = word2
                            else : 
                                raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                        .format(lineCounter))
            
                                
                    else : # error duplicated opcodes 
                        raise DuplicatedOpcode("Duplicated opcode in line {}".format(lineCounter))
                    
            else : #word1 is label 
                label = word1 
                if is_just_comment(word2) : 
                    raise OpcodeError("the opcode is missed in line {}".format(lineCounter))
                else : 
                    if word2 not in opcodes_and_directives : 
                        raise OperandError("Opcode is missed in line {}".format(lineCounter))
                    else  :
                        opcode = word2 
                        if opcode in solo_opcodes : 
                            if not is_just_comment(word3) : 
                                raise OperandError("Operand is missed in line {}".format(lineCounter))
                            else : 
                                comment = merge_string_list(line[2:])
                        else : #not solo opcode 
                            if is_just_comment(word3) : 
                                raise OperandError("Operand is missed in line {}".format(lineCounter)) 
                            else : 
                                operand = word3 
                                if not is_just_comment(word4) : 
                                    raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                        .format(lineCounter))


    seperatedLine = dict() 
    seperatedLine.update({'line' : lineCounter , 'label' : label , 'opcode' : opcode , 'operand' : operand , 'comment' : comment}) 

    for x , y in seperatedLine.items() : 
        if type(y) == str : 
            if len(y) > 6 and not x == 'comment': 
                if not (x == 'operand' and y.endswith(',X')) : 
                    raise Overflow("The the number of digits that are reserved for {} : {} is out of range in line {} ".format(x , y , lineCounter ))
    
    return seperatedLine