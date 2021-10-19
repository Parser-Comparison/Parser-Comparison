import ply.yacc as yacc
from lex import tokens
import sys
import time

def p_grammar(p):
    '''Expr : Expr Expr Expr 
            | Expr Expr
            | Letter'''
    if (len(p) == 2):               
        p[0] = p[1]
    elif (len(p) == 3):
        p[0] = p[1] and p[2]
    else:
        p[0] = p[1] and p[2] and p[3]

def p_letter(p):
    '''Letter : LETTER'''

    #print('current letter: ' + p[1])
    if (p[1] == 'a'):
        p[0] = True
    else:    
        p[0] = False              

def p_error(p):
  print("Syntax error\n")          

parser = yacc.yacc()

sys.stdin = open(sys.argv[1], 'r')
sys.stdout = open(sys.argv[1] + '_parser' +'.out', 'w')

# обработка входных данных файла
while True:  
  try:
    s = input()
  except EOFError:
    break
  if not s:
    continue
  try:
    start_time = time.time() 
    is_in_language = parser.parse(s)
    print("> Word: '%s' --> %s seconds \n" % (s, time.time() - start_time))

    if (is_in_language):
        print("Correct, word belongs to language\n")
    else:
        print("Incorrect, word doesn't belong to language\n")    
  except Exception as err:
    print("Error: " + str(err))