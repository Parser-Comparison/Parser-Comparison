import os
import re
import time
from parglare import GLRParser, Grammar

this_folder = os.path.dirname(__file__)
grammar = Grammar.from_file(os.path.join(this_folder, 'grammar.pg'),
                          re_flags=re.MULTILINE | re.VERBOSE)
glr_parser = GLRParser(grammar, debug=False)

start = time.time()
forest = glr_parser.parse_file(os.path.join(this_folder, 'input'))

print(f"Forest solutions: {forest.solutions}")
print(f"Forest ambiguities: {forest.ambiguities}")

end = time.time()
print(f"Runtime was {end - start}")

# -- Debugging/tracing output with detailed info about grammar, productions,
# -- terminals and nonterminals, DFA states, parsing progress,
# -- and at the end of the output: