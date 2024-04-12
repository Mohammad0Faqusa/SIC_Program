from functions import read_json_file
# Example usage:
file_path = "data.json"
intermediateList = read_json_file(file_path)

listingLines = [] 


firstLine = intermediateList[0] 
opcode = firstLine['opcode']
object_code = '' 
listingLines.append(firstLine.update({}))
if opcode == 'START' : 



for i in range(len(intermediateList)) : 

    line = intermediateList[i] 
    linCount = line['line']
    symbol = line['label']
    opcode = line['opcode']
    operand = line['operand']
    locCount = int(line['LOCCTR'] , 16)

    if opcode == "START" : 

