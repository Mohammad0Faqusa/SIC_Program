import functions
import exceptions 
# Example usage:
sic_directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "NOBASE",
                   "EQU", "LTORG", "ORG", "EXTDEF", "EXTREF", "CSECT", "USING"]

intermediateList_path = "intermediate.json"
symbols_path = "symbols.json" 

opcodes = functions.file_to_dict("opcodeTable.txt")

intermediateList = functions.read_json_file(intermediateList_path)
symbols_dict = functions.read_json_file(symbols_path)

first_line = intermediateList[0]
last_line = intermediateList[-1]

first_location_counter = first_line['LOCCTR']
last_location_counter = last_line['LOCCTR']

program_length = functions.program_length_hexa(first_location_counter , last_location_counter) 
if len(str(program_length)[2:]) > 6 : 
    raise exceptions.Overflow("The number of digits that are reserved for Program length {} is out of range"
                              .format(str(program_length)[2:]))

program_name = first_line['label']

listingLines = [] 
objectLines = [] 

header = '' 
firstLine = dict(intermediateList[0])
opcode = firstLine['opcode']
object_code = '' 

if opcode == 'START' : 
    firstLine.update({'opjectCode' : object_code})
    listingLines.append(firstLine)
    
header = "H^{0}^{1}^{2}".format(program_name, str(first_location_counter)[2:] , str(program_length)[2:])
objectLines.append(header) 

text_record = '' 
text_record_lines = [] 
text_record_max_length = 60 
object_sum = '' 
text_record_start_location = '' 

for line in intermediateList[1:] : 
    
    linCount = line['line']
    symbol = line['label']
    opcode = line['opcode']
    operand = line['operand']
    locCounter = line['LOCCTR']
    operandValue = ''
    object_code = ''  

    if text_record == "" : 
        text_record_start_location = str(locCounter)[2:]
    if operand != '' and not operand.isdigit() and opcode not in sic_directives  : 
        # if operand in symbols_dict : 
        if operand in symbols_dict : 
            operandValue = symbols_dict[operand]
            operandValue = str(operandValue)[2:]

        elif  operand.endswith(',X') :
            operandValue = symbols_dict[operand[:-2]]
            operandValue = str(operandValue)[2:]
        
        else: 
            operandValue = 0 
            raise exceptions.UndefinedSymbol("undefine symbol operand  \"{}\" {} in line ({}) ".format(operand ,operandValue,  linCount))
    else : 
        operandValue = 0 

    if opcode in sic_directives : 
        if opcode == 'WORD'  : 
            operandValue = str(hex(int(operand , 16)))[2:]
            object_code = operandValue.zfill(6)
        elif opcode == 'BYTE' : 
            if operand.startswith('C\'') : 
                operandValue = operand[2:-1]
                operandValue = functions.string_to_hex_string(operandValue) 
                object_code = operandValue.zfill(6)
            elif operand.startswith('X\'') : 
                operandValue = operand[2:-1]
                operandValue = str(operandValue)[2:] 
                object_code = operandValue.zfill(6)
        else : 
            operandValue = '' 
    else : 
        object_code = (opcodes[opcode] + str(operandValue)).zfill(6)

    listingline = dict(line)
    listingline.update({'operand_value' : operandValue , 'object_code' : object_code})
    listingLines.append(listingline) 
    
    object_sum += object_code 
    
    if (object_code == '') : 
        if object_sum == '' : 
            continue 
        text_record = 'T^'+text_record_start_location.zfill(6)+text_record
        text_record_lines.append(text_record)
        text_record = ''  
        object_sum = '' 

    if (len(object_sum + object_code) <= text_record_max_length ) : 
        text_record += '^'
        text_record += object_code 
    else : 
        text_record = 'T^'+text_record_start_location.zfill(6)+text_record
        text_record_lines.append(text_record)
        text_record = '' 
        object_sum = '' 

for x in text_record_lines : 
    print(x) 
