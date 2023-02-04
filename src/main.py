import sys , os
import enum
import dataclasses
import typing

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

@dataclasses.dataclass
class Token:
    data : typing.Any
    loc : int

abst = []
stack = []
types = []
args = []
backword = []
word = ""
indent = 0
i = 0

def main(file):
    global abst,stack,types,args,backword,word,indent,i
    if not os.path.exists(file):
        raise RuntimeError("file do not exist")
    if not os.path.isfile(file):
        raise RuntimeError("not a file")
    
    txt = ""
    with open(file,'r') as f:
        txt = f.read(-1)
    
    def goi(lis,ind):
        if ind != 2:
            return lis
        x= lis
        for _ in range(ind):
            lis = lis[-1]
        return lis

    def debug():
        global abst,stack,types,args,backword,word,indent,i
        print(
        "abst : ",abst,
        "\nstack : ",stack,
        "\ntypes : ",types,
        "\nargs : ",args,
        "\nbackword : ",backword,
        "\nword : ",word,
        "\nindent : ",indent,
        "\ni : ",i)
        print()
    
    local_indent = 0
    while i < len(txt):
        lestk = len(stack)
        char = txt[i]
        debug()
        if char == "\n":
            goi(backword,lestk).append(word)
            word = ""
        elif char == "\t" or txt[i] + txt[i+1] + txt[i+2] + txt[i+3] == "    ":
            local_indent += 1
        elif char == " ":
            print(word)
            backword.append(word)
            print(backword)
            print(goi(backword,lestk))
            goi(backword,lestk).append(word)
            word = ""
        elif char == "":
            pass
        elif char == "(":
            stack.append(")")
            goi(backword,lestk).append(word)
            goi(backword,lestk).append([])
            word = ""
        elif char == ")":
            if not stack.pop() == ")":
                raise
            lestk = len(stack)
            debug()
            goi(args,lestk).append(goi(backword,lestk).pop())
        elif char == "[":
            raise
        elif char == "]":
            raise
        elif char == "{":
            raise
        elif char == "}":
            raise
        else:
            word += char
        i += 1
    
if __name__ == "__main__":
    main("./main.py")