
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


def create_intermediate_list(sourelist) : 
    mdtlist = [] 
    for x in sourelist : 
        mdtlist.append(['' , tuple(x)])
    return mdtlist

def check_if_has_comment(line) : 
    for i in range(len(line)) : 
        if '.' in line[i] :
            return i+1  
    return False 

def check_if_has_symbol(line) : 
    if not check_if_has_comment(line) :
        if len(line) > 2 :
            return True 
    elif check_if_has_comment(line) > 3 : 
        return False 
    else : 
        return True 

def flatten_list(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item, list):
            # If the item is a list, recursively flatten it and extend the flattened result
            flattened_list.extend(flatten_list(item))
        else:
            # If the item is not a list, add it directly to the flattened list
            flattened_list.append(item)
    return flattened_list

def list_to_file(file_path, my_list):
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write each element to a new line in the file
        
        for element in my_list:
            strelement = '' 
            for x in element : 
                strelement += str(x).ljust(10 , ' ')

            file.write(strelement + '\n')
    file.close() 

def dict_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for key, value in dictionary.items():
            file.write(f"{key}: {value}\n")

def comment_statement(statement) : 
    if statement[0] == '.' :
        return True 
    else : 
        return False




