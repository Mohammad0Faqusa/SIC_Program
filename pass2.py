from functions import read_json_file
# Example usage:
intermediateList_path = "intermediate.json"
symbols_path = "symbols.json" 

intermediateList = read_json_file(intermediateList_path)
symbols_dict = read_json_file(symbols_path)

for x in intermediateList : 
    print(x) 
for key , value in symbols_dict.items(): 
    print(key , ":" , value ) 

listingLines = [] 


# firstLine = intermediateList[0] 
# opcode = firstLine['opcode']
# object_code = '' 
# listingLines.append(firstLine.update({}))
# if opcode == 'START' : 



# for i in range(len(intermediateList)) : 

#     line = intermediateList[i] 
#     linCount = line['line']
#     symbol = line['label']
#     opcode = line['opcode']
#     operand = line['operand']
#     locCount = int(line['LOCCTR'] , 16)

#     if opcode == "START" : 

