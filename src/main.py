import sys
import os
import enum
import pickle


class Token(enum.Enum):
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

    MACROS_C = enum.auto()
    MACROS_RUST = enum.auto()


def DEBUG_PRINT(ret, WORD, KEEP_VAR, s):
    print(ret, WORD, KEEP_VAR, s)
    return ret, WORD, KEEP_VAR


def NEXT_TOKEN(ret, WORD, KEEP_VAR, s):
    return ret, WORD + s, KEEP_VAR


def ADD_TOKEN_SATE(ret, WORD, KEEP_VAR, s):
    raise


def CLOSE_TOKEN_STATE(ret, WORD, KEEP_VAR, s):
    raise


def APPEND_TOKEN(ret, WORD, KEEP_VAR, s):
    raise


def run_sim(model: list, inp: str):
    ret = []
    mod = model[0]
    WORD = ""
    KEEP_VAR = {}
    for s in inp:
        acts = mod.get(s, [DEBUG_PRINT, NEXT_TOKEN])
        for act in acts:
            ret, WORD, KEEP_VAR = act(ret, WORD, KEEP_VAR, s)

def import_default_model():
    try:
        with open("./models/m.bin","rb") as f:
            model = pickle.load(f)
        print("model imported")
        return model
    except Exception as ex:
        print(ex)
        print("no model")
        return [{}]

def import_training():
    return []

def save_model(model):
    with open("./models/m.bin","wb") as f:
        pickle.dump(model, f)
    print("saved")

def main(path : str):
    model: list = import_default_model() ### get the model list[dict]
    exemples :list = import_training() ### list[tuple[input,out]]
    with open(path,"r") as f:
        inp = f.read()
    #### NOW begin the L* algorithm
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
    ### default sim
    ret = []
    mod = model[0]
    WORD = ""
    KEEP_VAR = {}
    for s in inp:
        acts = mod.get(s, [DEBUG_PRINT, NEXT_TOKEN])
        for act in acts:
            ret, WORD, KEEP_VAR = act(ret, WORD, KEEP_VAR, s)


if __name__ == "__main__":
    print(main(sys.argv))
