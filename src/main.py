import sys
import os
import enum
import pickle


class Token(enum.Enum):
    KEYWORD = enum.auto()
    module = enum.auto()

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

    BIT_OR = enum.auto()
    BIT_XOR = enum.auto()
    BIT_AND = enum.auto()
    BIT_SHIFT_L = enum.auto()
    BIT_SHIFT_R = enum.auto()
    BIT_NOT = enum.auto()

    LOOP_DECLAR = enum.auto()
    LOOP_CONTINUE = enum.auto()
    LOOP_BREAK = enum.auto()
    GOTO = enum.auto()

    FUNC_DECLAR = enum.auto()
    FUNC_DEF = enum.auto()
    FUNC_CALL = enum.auto()
    FUNC_RET = enum.auto()
    IF = enum.auto()
    TRY = enum.auto()
    CATCH = enum.auto()
    CLASS = enum.auto()
    SWITCH = enum.auto()

    IMPORT_AS = enum.auto()
    IMPORT_USE = enum.auto()

    TYPE_DEF = enum.auto()
    TYPE_INT = enum.auto()
    TYPE_FLOAT = enum.auto()
    TYPE_STR = enum.auto()
    TYPE_PTR = enum.auto()

    ERROR_DEF = enum.auto()
    ERROR_THROW = enum.auto()
    ERROR_CATCH = enum.auto()

    MACROS_C = enum.auto()
    MACROS_RUST = enum.auto()

def search_word(KEEP_VAR,WORD):
    ret = []
    for lang in KEEP_VAR["UNIVERSE"]:           # python
        for file in KEEP_VAR["UNIVERSE"][lang]: # ERROR_DEF
            if WORD in KEEP_VAR["UNIVERSE"][lang][file]:
                ret.append((lang,file)) 
    return (ret,WORD)

def DEBUG_PRINT(ret, WORD, TOK_STATE, KEEP_VAR, s):
    print("DEBUG PRINT ret", ret, "WORD", WORD, "TOK_STATE",
          TOK_STATE, "KEEP_VAR", KEEP_VAR, "s", s)
    return ret, WORD, TOK_STATE, KEEP_VAR


def NEXT_PASS(ret, WORD, TOK_STATE, KEEP_VAR, s):
    return ret, WORD, TOK_STATE, KEEP_VAR


def NEXT_TOKEN(ret, WORD, TOK_STATE, KEEP_VAR, s):
    return ret, WORD + s, TOK_STATE, KEEP_VAR


def handy_follow_ptr(lis, i):
    for _ in range(i):
        lis = lis[-1]
    return lis


def ADD_TOKEN_SATE(ret, WORD, TOK_STATE, KEEP_VAR, s):
    handy_follow_ptr(TOK_STATE[0], TOK_STATE[1]).append([])
    TOK_STATE[1] += 1
    return ret, WORD, TOK_STATE, KEEP_VAR


def CLOSE_TOKEN_STATE(ret, WORD, TOK_STATE, KEEP_VAR, s):
    TOK_STATE[1] -= 1
    if TOK_STATE[1] < 0:
        raise
    return ret, WORD, TOK_STATE, KEEP_VAR


def APPEND_TOKEN(ret, WORD, TOK_STATE, KEEP_VAR, s):
    handy_follow_ptr(TOK_STATE[0], TOK_STATE[1]).append(search_word(KEEP_VAR,WORD))
    WORD = ""
    return ret, WORD, TOK_STATE, KEEP_VAR


def LOOP(args):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        for action in args:
            ret, WORD, TOK_STATE, KEEP_VAR = action(
                ret, WORD, TOK_STATE, KEEP_VAR, s)
        return ret, WORD, TOK_STATE, KEEP_VAR
    return inner


def LOGIC_AND(*cond, func):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        if all(*cond):
            func(ret, WORD, TOK_STATE, KEEP_VAR, s)
        return False
    return inner


def LOGIC_ISWORD(cond):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        if WORD is cond:
            return True
        return False
    return inner


def LOGIC_INWORD(cond):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        if WORD in cond:
            return True
        return False
    return inner


def IFELSE(lambd, funcif, funcelse):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        if lambd(ret, WORD, TOK_STATE, KEEP_VAR, s):
            return funcif(ret, WORD, TOK_STATE, KEEP_VAR, s)
        else:
            return funcelse(ret, WORD, TOK_STATE, KEEP_VAR, s)
    return inner


def INWORD(cond, func):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        if WORD in cond:
            func(ret, WORD, TOK_STATE, KEEP_VAR, s)
    return inner


def ISWORD(cond, func):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        if WORD is cond:
            func(ret, WORD, TOK_STATE, KEEP_VAR, s)
    return inner


def RAISE(error):
    def inner(ret, WORD, TOK_STATE, KEEP_VAR, s):
        raise RuntimeError(error)
    return inner



# def run_sim(model: list, inp: str):
# ret = []
# mod = model[0]
# WORD = ""
# TOK_STATE = [[],0]
# KEEP_VAR = {}
# for s in inp:
# acts = [DEBUG_PRINT, IFELSE(LOGIC_INWORD(default_lookup),DEBUG_PRINT ,NEXT_TOKEN)]
# for act in acts:
# ret, WORD, TOK_STATE ,KEEP_VAR = act( ret, WORD, TOK_STATE ,KEEP_VAR, s)

def import_training():
    UNIVERSE = {}
    ret = []
    for lang in os.listdir("./training/"):
        UNIVERSE[lang] = {}
        for file in os.listdir("./training/" + lang):
            UNIVERSE[lang][os.path.splitext(os.path.basename(file))[0]] = []
            print("training", lang+" " +
                  os.path.splitext(os.path.basename(file))[0])
            local_type = Token[os.path.splitext(os.path.basename(file))[0]]
            with open("./training/" + lang + "/" + file, "r") as f:
                UNIVERSE[lang][os.path.splitext(os.path.basename(file))[0]] = f.read().splitlines()
            print("done")
    # with all of thoses words we need a default model
    # that ignore these
    print("training done")
    return UNIVERSE


def main(path: str):
    UNIVERSE = import_training()
    exemples: list = import_training()  # list[tuple[input,out]]
    with open(path, "r") as f:
        inp = f.read()
    # NOW begin the L* algorithm
    """
    1 . Initialization: Start with an empty model (or start with universal one) 
        and a set of equivalence classes, which are sets of words that are indistinguishable 
        from each other with the current FSM. -> garbage in garbage out 
        The set of equivalence classes initially contains all the positive and negative examples.
        -> mainly the exemple

    2 . Refinement: At each step, 
        choose an equivalence class that is consistent with the current FSM. 
        An equivalence class is consistent if the FSM assigns the same output (accept or reject) 
        to all words in the class.

    3 .Splitting: If a consistent class is found, 
        split the class into two: positive and negative examples. 
        Add a new state to the FSM and the necessary 
        transitions to separate the positive and negative examples.

    4 . Updating: Update the equivalence classes with the new information from the split. 
        The updated equivalence classes are obtained by removing all classes 
        that intersect with the consistent class and adding the two new classes obtained from the split.

    5 . Termination: If no consistent class is found, 
        the FSM is complete. The algorithm terminates and the resulting FSM is returned.

    6 . Testing: After the FSM is complete, 
        test it on all positive and negative examples to make sure it correctly classifies all examples.
    """
    # default sim
    ret = []
    WORD = ""
    TOK_STATE = [[], 0]
    KEEP_VAR = {"UNIVERSE":UNIVERSE}
    for s in inp:
        acts = [IFELSE(
            lambda ret, WORD, TOK_STATE, KEEP_VAR, s: s == "\n", LOOP([ADD_TOKEN_SATE,APPEND_TOKEN,CLOSE_TOKEN_STATE, NEXT_PASS]), NEXT_TOKEN)]
        for i, act in enumerate(acts):
            # print(
                # f"DEBUG act {i} ( {ret}, {WORD}, {TOK_STATE} ,{KEEP_VAR}, {s})")
            ret, WORD, TOK_STATE, KEEP_VAR = act(
                ret, WORD, TOK_STATE, KEEP_VAR, s)
        # input()
    print(ret, WORD, TOK_STATE, KEEP_VAR)


if __name__ == "__main__":
    print("launch by arg", sys.argv)
    print(main(sys.argv[1]))
