from functions import read_json_file
# Example usage:
file_path = "data.json"
intermediateList = read_json_file(file_path)

for i in range(len(intermediateList)) : 

    line = intermediateList[i] 
    linCount = line['line']
    symbol = line['label']
    opcode = line['opcode']
    operand = line['operand']
    locCount = int(line['LOCCTR'] , 16)

    