class OpcodeError(Exception):
    pass

class DuplicateSymbol(Exception) : 
    pass 

class OperandError(Exception) : 
    pass 

class DuplicatedOpcode(Exception) : 
    pass 

class DuplicatedSymbol(Exception) : 
    pass 

class Overflow(Exception) : 
    pass 

class UndefinedSymbol(Exception) : 
    pass 