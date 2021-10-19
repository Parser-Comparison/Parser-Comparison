import sys
import time
from lark import Lark, Transformer, v_args, tree


try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass


ambiguity_grammar = """
    expr: expr expr expr
            | expr expr
            | LETTER    
    LETTER: /[a-zA-z]/ 
    %ignore (" "| /\t/)   
"""
ambiguity_grammar2 = """
    expr: expr expr expr
            | expr expr
            | LETTER    
    LETTER: /[a]/ 
    %ignore (" "| /\t/)   
"""

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    
    def __init__(self):
        self.string_= ""
    
    def append_(self, letter):
        self.string_.append(letter) 
    #def whatisit(letter):
        #if letter!='a':
            #ambiguity_parser2.is_all_a = False
parser_name = "earley"
ambiguity_parser = Lark(ambiguity_grammar, start="expr", parser =parser_name)
ambiguity_parser2 =  Lark(ambiguity_grammar, start="expr", parser =parser_name)
ambiguity = ambiguity_parser.parse
ambiguity2 = ambiguity_parser2.parse
def make_png(filename, s):
    tree.pydot__tree_to_png(ambiguity(s), filename)
def make_dot(filename, s):
    tree.pydot__tree_to_dot( ambiguity(s), filename)
def main():
    if (len(sys.argv)<3):
                print("not enough arguments!")
                exit(0)
    f = open(sys.argv[2], 'w')
    f.write(parser_name+" parser\n")
    i = 10
    while True:
        start_time=0
        try:
            s = input('> ')
        except EOFError:
            break
        try:
            start_time = time.time() 
            ambiguity(s)   
            f.write("%s \n  --> %s seconds \n" % (s, time.time() - start_time)) 
            make_png(sys.argv[1], s)  
            #make_dot(sys.argv[2], s)
        except Exception as e:
            f.write("it is impossible to build tree: some symbols are not correct, read grammar requirements!\n")    
        try:
            ambiguity2(s)
            f.write("input word belongs to the language\n")
        except Exception as e:
            f.write("input word does not belong to the language\n")  
         


def test():
    print(ambiguity("aaaa"))
    print(ambiguity("aaaabaa"))


if __name__ == '__main__':
    #test()
    main()
