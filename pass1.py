from functions import * 
from exceptions import * 


source = file_to_fixed_list("sicProgram.txt")

opcodes = file_to_dict("opcodeTable.txt")

sic_directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "NOBASE",
                   "EQU", "LTORG", "ORG", "EXTDEF", "EXTREF", "CSECT", "USING"]

opcodes_and_directives = list(opcodes.keys())
opcodes_and_directives.extend(sic_directives) 


symb_dict = dict()  
intermediateList = [] 
programName = '' 
startAddress = '' 
locCounter = 0 
errorFlag = 0  
lineCounter = 1 

#check the first line , if START
start_index = index_first_line(source) 
lineCounter = start_index + 1
first_line = source[start_index] 

counterLine = start_index 

first_line = string_to_list(first_line) 
first_opcode_index = opcode_index(first_line , opcodes_and_directives)
startOpcode = first_line[first_opcode_index] 

if startOpcode == 'START' : 
    #save the operand as starting address 
    startAddress = first_line[first_opcode_index + 1] 
    #initialize the location counter to starting address 
    locCounter = int(startAddress)
    #write the line to intermediate file 
    intermediateList.append(first_line[0:first_opcode_index+2])
    #read next input line 
    lineCounter += 1 
else : 
    locCounter = 0  
    lineCounter += 1 

for line in source[start_index+1:] :


    if is_just_comment(line) : 
        lineCounter += 1 
        continue 

    line = string_to_list(line)  
    opcode_indx = opcode_index(line , opcodes_and_directives)
    if opcode_indx == -1 or opcode_indx > 1 : 
        raise OpcodeError("Opcode is not found , or is written in wrong place in line {0}".format(lineCounter))
    opcode = line[opcode_indx]
    
    if opcode == 'END' : 
        break 

  
    lineCounter += 1 



