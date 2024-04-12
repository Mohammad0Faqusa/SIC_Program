from functions import * 

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

#check the first line , if START
start_index = index_first_line(source) 
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
    print("location counter is " , locCounter)
    #write the line to intermediate file 
    intermediateList.append(first_line[0:first_opcode_index+2])
    #read next input line 
else : 
    locCounter = 0  






