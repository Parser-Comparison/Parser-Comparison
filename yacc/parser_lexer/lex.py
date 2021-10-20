import ply.lex as lex
import sys

# Only one element in the list of token names
tokens = ['LETTER']

def t_LETTER(t):
  r'[a-zA-Z]'
  return t

t_ignore = ' \t'

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

lexer.input(open(sys.argv[1], 'r').read())
sys.stdout = open(sys.argv[1] + '_lex_tokens' + '.out', 'w')

while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)