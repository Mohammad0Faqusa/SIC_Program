from functions import * 
from exceptions import * 


source = file_to_fixed_list("sicProgram.txt")

opcodes = file_to_dict("opcodeTable.txt")

sic_directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "NOBASE",
                   "EQU", "LTORG", "ORG", "EXTDEF", "EXTREF", "CSECT", "USING"]
opcodes_with_no_operands = ['RSUB' , 'END' , 'LTORG']

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

    #check if valid opcode , and detect the opcode index 
    opcode_indx = opcode_index(line , opcodes_and_directives)
    if opcode_indx == -1 or opcode_indx > 1 or is_just_comment(line[opcode_indx]) : 
        raise OpcodeError("Opcode is not found , or is written in wrong place in line {0}".format(lineCounter))
    
    opcode = line[opcode_indx]
    if opcode == 'END' : 
        break 

    statent_length = 1 
    # File length : 
	# • Case 1 
	# 	○ If not comment : (solved)
	# 		§ If not opcode : 
	# 			□ Raise error (opcode is missed)
	# 		§ Else : 
	# 			□ If not solo opcode  : 
	# 				® Rase Error (operand is missed) 
	# 			□ Else : 
	# 				® Statement_length = 1 
	# • Case 2 
	# 	○ If word2 is comment : 
	# 		§ If word1 not opcode : 
	# 			□ Raise error (opcode is missed)
	# 		§ Else : 
	# 			□ If word1 not solo opcode  : 
	# 				® Rase Error (operand is missed) 
	# 			□ Else : 
	# 				® Statement_length = 1 
	# 	○ If word 2 is not comment : 
	# 		§ If word1 is opcode : 
	# 			□ If word 1 is solo opcode 
	# 				® Reise error : (operand is written error, or you forgot to indicate it as comment
	# 			□ Else : 
	# 				® Statement_length = 2 {opcode , operand} 
	# 		§ Else -word1 is label- : 
	# 			□ Word2 is not solo opcode : 
	# 				® Rase error (operand is missed) 
	# 			□ Else : 
	# 				® Statement_length = 2 {label , opcode}  
	# • Case > 2 
	# 	○ Case 3 
	# 		§ If word1 is opcode : 
	# 			□ If word2 is comment : 
	# 				® If not solo operand 
	# 					◊ Rase error (operand is missed) 
	# 			□ Else : 
	# 				® If word 2 is operand : 
	# 					◊ If opcode is solo : 
	# 						} Rase error (operand is written wrong, or you forgut to insert "." if comment
	# 					◊ Else 
	# 						} If word3 is comment : 
	# 							– Statement_length = 2 {opcode , operand} 
	# 						} Else : 
	# 							– Rase error (operand is written wrong, or you forgut to insert "." if comment
	# 		§ Else (word1 is label) 
	# 			□ If word 2 is comment 
	# 				® Raise error (opcode is missed) 
	# 			□ Else [word 2 not comment] : 
	# 				® If not opcode : 
	# 					◊ Rease error (opcode is missed) 
	# 				® Else : 
	# 					◊ If solo opcode 
	# 						} Word 3 is not comment 
	# 							– Raise error (operand is written wrong, or you forgut to insert "." 
	# 						} Else 
	# 							– Statement_length = 2 {label , solo_opcode} 
	# 					◊ Else [not solo opcode] : 
	# 						} If word 3 is comment : 
	# 							– Error : operand is missed 
	# 						} Else  :
	# 							– Stement length = 3 {label, opcode, operand} 
	# 	○ Case > 3 
	# 		§ If word1 is opcode : 
	# 			□ If word2 is comment : 
	# 				® If not solo operand 
	# 					◊ Rase error (operand is missed) 
	# 			□ Else : 
	# 				® If word 2 is operand : 
	# 					◊ If opcode is solo : 
	# 						} Rase error (operand is written wrong, or you forgut to insert "." if comment
	# 					◊ Else 
	# 						} If word3 is comment : 
	# 							– Statement_length = 2 {opcode , operand} 
	# 						} Else : 
	# 							– Rase error (operand is written wrong, or you forgut to insert "." if comment
	# 		§ Else (word1 is label) 
	# 			□ If word 2 is comment 
	# 				® Raise error (opcode is missed) 
	# 			□ Else [word 2 not comment] : 
	# 				® If not opcode : 
	# 					◊ Rease error (opcode is missed) 
	# 				® Else : 
	# 					◊ If solo opcode 
	# 						} Word 3 is not comment 
	# 							– Raise error (operand is written wrong, or you forgut to insert "." 
	# 						} Else 
	# 							– Statement_length = 2 {label , solo_opcode} 
	# 					◊ Else [not solo opcode] : 
	# 						} If word 3 is comment : 
	# 							– Error : operand is missed 
	# 						} Else  :
	# 							– If word 4 is not comment : 
	# 								w Raise error (wrong comment) 
	# 							– Else 
	# 								w Stement length = 3 {label, opcode, operand} 
			

    
    #write the line into knwon columns locations 
    seperatedLine = dict() 
    if statent_length == 1 : 
        seperatedLine.update({'line' : lineCounter , 'OPCODE': opcode })
    else : 
        seperatedLine.update({'line' : lineCounter , 'OPCODE': opcode , 'OPERAND' : operand })
    
    print(seperatedLine) 

            
    
    
  
    lineCounter += 1 



