from functions import * 
from exceptions import * 


source = file_to_fixed_list("sicProgram.txt")

opcodes = file_to_dict("opcodeTable.txt")

sic_directives = ["START", "END", "BYTE", "WORD", "RESB", "RESW", "BASE", "NOBASE",
                   "EQU", "LTORG", "ORG", "EXTDEF", "EXTREF", "CSECT", "USING"]
solo_opcodes  = ['RSUB'  , 'LTORG']

opcodes_and_directives = list(opcodes.keys())
opcodes_and_directives.extend(sic_directives) 


symb_dict = dict()  
intermediateList = [] 
programName = '' 
startAddress = '' 
locCounter = 0 
errorFlag = 0  
lineCounter = 1 
programLength = 0 


lineCounter = 1 

for line in source :


    if is_just_comment(line) : 
        lineCounter += 1 
        continue 

    line = string_to_list(line)  

    label = '' 
    opcode = '' 
    operand = '' 

    if len(line) == 1 : 
        word1 = line[0]
        if not is_just_comment(word1) : 
            op_index = opcode_index(line , opcodes_and_directives) 
            if word1 not in opcodes_and_directives : 
                raise OpcodeError("the opcode is missed in line {}".format(lineCounter))
            else : 
                opcode = word1
                if opcode not in solo_opcodes : 
                    raise OperandError("the operand is missed in line {}".format(lineCounter))
                
    elif len(line) == 2 : 
        word1 = line[0] 
        word2 = line[1] 
        # op_index = opcode_index(line , opcodes_and_directives)

        if is_just_comment(word2) : 
            if word1 not in opcodes_and_directives : #if word 1 is not opcode 
                raise OpcodeError("opcode is missed in line {}".format(lineCounter))
            else : 
                opcode = word1 
                if opcode not in solo_opcodes : 
                    raise OperandError("operand is missed in line {}".format(lineCounter))
        else  : # word 2 is not comment 
            if word1 in opcodes_and_directives : 
                opcode = word1
                if opcode in solo_opcodes :
                    raise OperandError("Operand is written error, or you forgot to insert \".\" befor the comment in line {}"
                                       .format(lineCounter))
                else : 
                    operand = word2
                    if operand in opcodes_and_directives : 
                        raise DuplicatedOpcode("Error Opcode is written on operand field in line {}".format(lineCounter))
            else : #word 1 is label 
                if word2 not in opcodes_and_directives : 
                    raise OperandError("Operand is missed in line {}".format(lineCounter))
                else : 
                    label = word1 
                    opcode = word2 

    elif len(line) == 3 : 
        word1 = line[0] 
        word2 = line[1] 
        word3 = line[2] 

        if word1 in opcodes_and_directives :
            opcode = word1 
            if is_just_comment(word2) : 
                if opcode not in solo_opcodes :
                    raise OperandError("Operand is missed in line {}".format(lineCounter))
            else : 
                if opcode in solo_opcodes : 
                    raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                       .format(lineCounter))
                else : 
                    if is_just_comment(word3) : 
                        operand = word2 
                    else : 
                        raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                       .format(lineCounter))
        else : #word 1 is label 
            if is_just_comment(word2) : 
                raise OperandError("opcode is missed in line {}".format(lineCounter))
            else : #word 2 not comment 
                if word2 not in opcodes_and_directives : 
                    raise OpcodeError("Opcode is missed in line {}".format(lineCounter))
                else : 
                    label = word1 
                    opcode = word2 
                    if opcode in solo_opcodes : 
                        if not is_just_comment(word3) : 
                            raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                       .format(lineCounter))
                    else : 
                        if is_just_comment(word3) : 
                            raise OperandError("Operand is missed in line {}".format(lineCounter))
                        else : 
                            operand = word3 
    else : #line length > 3 
        word1 = line[0] 
        word2 = line[1] 
        word3 = line[2] 
        word4 = line[3]
        if word1 in opcodes_and_directives : 
            opcode = word1 
            if is_just_comment(word2) : 
                if operand not in solo_opcodes : 
                    raise OperandError("Operand is missed in line {}".format(lineCounter))
            else : #if word 2 is operand 
                operand = word2 
                if  operand not in opcodes_and_directives : 
                    if operand in solo_opcodes : 
                        raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                       .format(lineCounter))
                    else : 
                        if is_just_comment(word3) : 
                            operand = word2
                        else : 
                            raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                       .format(lineCounter))
        
                            
                else : # error duplicated opcodes 
                    raise DuplicatedOpcode("Duplicated opcode in line {}".format(lineCounter))
                
        else : #word1 is label 
            label = word1 
            if is_just_comment(word2) : 
                raise OpcodeError("the opcode is missed in line {}".format(lineCounter))
            else : 
                if word2 not in opcodes_and_directives : 
                    raise OperandError("Opcode is missed in line {}".format(lineCounter))
                else  :
                    opcode = word2 
                    if opcode in solo_opcodes : 
                        if not is_just_comment(word3) : 
                            raise OperandError("Operand is missed in line {}".format(lineCounter))
                    else : #not solo opcode 
                        if is_just_comment(word3) : 
                            raise OperandError("Operand is missed in line {}".format(lineCounter)) 
                        else : 
                            operand = word3 
                            if not is_just_comment(word4) : 
                                raise OperandError("Operand is written wrong, or you forgut to insert \".\" before the comment in line {}"
                                       .format(lineCounter))


    seperatedLine = dict() 
    seperatedLine.update({'line' : lineCounter , 'label' : label , 'opcode' : opcode , 'operand' : operand}) 
    intermediateList.append(seperatedLine) 
    lineCounter += 1 


# Now processing in Pass1 through intermediate list : 

firstOpcode = intermediateList[0]['opcode']
locCounter = 0 
if firstOpcode == "START" : 
    firstOperand = intermediateList[0]['operand']
    locCounter = int(firstOperand , 16) 
    intermediateList[0].update({'LOCCTR' : str(hex(locCounter))[2:]})
else : 
    intermediateList[0].update({'LOCCTR' : str(hex(locCounter))[2:]})

firstAddress = locCounter 

for i in range(len(intermediateList[1:])) : 
    line = intermediateList[i] 
    linCount = intermediateList[i]['line']
    symbol = intermediateList[i]['label']
    opcode = intermediateList[i]['opcode']
    operand = intermediateList[i]['operand']

    if opcode != 'END' : 
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
            locCounter += len(operand) 
    
        intermediateList[i].update({'LOCCTR' : str(hex(locCounter))[2:]})
    else :
        intermediateList[i].update({'LOCCTR' : str(hex(locCounter))[2:]})
        programLength = locCounter - firstAddress 

print(intermediateList) 





            