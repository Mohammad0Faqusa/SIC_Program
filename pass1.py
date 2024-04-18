import functions 
from exceptions import * 


"""
Name : Mohammad Faquse
ID : 201014 
GitHub : https://github.com/Mohammad0Faqusa/SIC_Program.git 

"""
source_file = 'source_file.asm'

source = functions.file_to_fixed_list(source_file)

opcodes = functions.file_to_dict("opcodeTable.txt")

sic_directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "NOBASE",
                   "EQU", "LTORG", "ORG", "EXTDEF", "EXTREF", "CSECT", "USING"]
solo_opcodes  = ['RSUB'  ,'END' ,  'LTORG']

opcodes_and_directives = list(opcodes.keys())
opcodes_and_directives.extend(sic_directives) 


symb_dict = dict()  
intermediateList = [] 
programName = '' 
startAddress = 0
locCounter = 0 
errorFlag = 0  
lineCounter = 1 
programLength = 0 


lineCounter = 1 

for line in source : #to check line words, and filter these words to their columns

    filtered_line = functions.filter_string_line(line, lineCounter , opcodes_and_directives , solo_opcodes )
                
    intermediateList.append(filtered_line) 
    
    lineCounter += 1 


# Now processing in Pass1 through intermediate list : 

firstOpcode = intermediateList[0]['opcode']
locCounter = 0 
if firstOpcode == "START" : 
    firstOperand = intermediateList[0]['operand']
    locCounter = int(firstOperand , 16) 
    startAddress = locCounter
    intermediateList[0].update({'LOCCTR' : hex(locCounter)})
else : 
    intermediateList[0].update({'LOCCTR' : hex(locCounter)})

firstAddress = locCounter 


for i in range(len(intermediateList[1:]) + 1) : 
    line = intermediateList[i] 
    linCount = line['line']
    symbol = line['label']
    opcode = line['opcode']
    operand = line['operand']

    if opcode != 'END' : 
        line.update({'LOCCTR' : str(hex(locCounter))})

        if symbol != '' : 
            if symbol in symb_dict : 
                raise DuplicateSymbol("A duplicated symbol in symbol table while adding the symbol {0} in line {1}"
                                      .format(symbol , linCount ))
            else : 
                symb_dict.update({symbol : hex(locCounter)})

        if opcode in opcodes  : 
            locCounter += 3 
        elif opcode == 'WORD' :
            locCounter += 3 
        elif opcode == 'RESW' : 
            locCounter += 3 * int(operand) 
        elif opcode == 'RESB' : 
            locCounter += int(operand) 
        elif opcode == 'BYTE' : 
            locCounter += len(opcode[2:])
    else : 
        line.update({'LOCCTR' : str(hex(locCounter))})
        programLength = int(locCounter) - int(startAddress)



# File path to write JSON data
intermediateList_path = "intermediate.json"
symbol_dict_path = "symbols.json"

functions.write_json_file(symb_dict , symbol_dict_path) 
functions.write_json_file(intermediateList , intermediateList_path) 

