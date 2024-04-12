from functions import * 

source = file_to_fixed_list("sicProgram.txt")
opcodes = file_to_dict("opcodeTable.txt")

intermediate_list = [] 

symb_dict = dict()  

programName = '' 
startAddress = '' 
locCounter = 0 
errorFlag = 0  

#check the first line , if START
firstline = source[0] 
counterLine = 0 

