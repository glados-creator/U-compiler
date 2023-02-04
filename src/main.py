import sys , os
import enum

class action(enum.Enum):
    VAR_ASS = enum.auto()
    VAR_DECLAR = enum.auto()
    VAR_USE = enum.auto()

    LOGIC_AND = enum.auto()   
    LOGIC_OR = enum.auto()    
    LOGIC_NOT = enum.auto()   
    LOGIC_SUP = enum.auto()   
    LOGIC_INF = enum.auto()   
    LOGIC_EQ = enum.auto()    
    LOGIC_MOD = enum.auto()   
    LOGIC_PLUS = enum.auto()  
    LOGIC_MINUS = enum.auto() 
    LOGIC_MUL = enum.auto()   
    LOGIC_EXP = enum.auto()   
    LOGIC_DIV = enum.auto()   
    LOGIC_FLOOR = enum.auto() 
    LOGIC_CEIL = enum.auto()

    LOOP_DECLAR = enum.auto()
    LOOP_CONTINUE = enum.auto()
    LOOP_BREAK = enum.auto()

    GOTO = enum.auto()

    FUNC_DECLAR = enum.auto()
    FUNC_CALL = enum.auto()
    FUNC_RET = enum.auto()  
    IF = enum.auto()
    TRY = enum.auto()
    EXCEPT = enum.auto()
    CLASS = enum.auto()
    SWITCH = enum.auto()

    IMPORT_AS = enum.auto()
    IMPORT_USE = enum.auto()

    TYPE_DEF = enum.auto()
    TYPE_INT = enum.auto()
    TYPE_FLOAT = enum.auto()
    TYPE_STR = enum.auto()
    TYPE_PTR = enum.auto()

def main(file):
    if not os.path.exists(file):
        raise RuntimeError("file do not exist")
    if not os.path.isfile(file):
        raise RuntimeError("not a file")
    
    txt = ""
    with open(file,'r') as f:
        txt = f.read(-1)
    
    stack = []
    types = []
    args = []
    word = ""
    indent = 0
    i = 0
    while i < len(txt):
        char = txt[i]
        if char == "(":
            pass
        elif char == ")":
            pass
        elif char == "[":
            pass
        elif char == "]":
            pass
        elif char == "{":
            pass
        elif char == "}":
            pass
        i += 1
    
if __name__ == "__main__":
    main("./main.py")