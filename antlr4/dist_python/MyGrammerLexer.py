# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\20\b\1\4\2\t\2\4\3\t\3\3\2\3\2\3\3\6\3\13\n\3\r\3\16")
        buf.write("\3\f\3\3\3\3\2\2\4\3\3\5\4\3\2\4\4\2C\\c|\5\2\13\f\17")
        buf.write("\17\"\"\2\20\2\3\3\2\2\2\2\5\3\2\2\2\3\7\3\2\2\2\5\n\3")
        buf.write("\2\2\2\7\b\t\2\2\2\b\4\3\2\2\2\t\13\t\3\2\2\n\t\3\2\2")
        buf.write("\2\13\f\3\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\16\3\2\2\2\16")
        buf.write("\17\b\3\2\2\17\6\3\2\2\2\4\2\f\3\b\2\2")
        return buf.getvalue()


class MyGrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LETTER = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "LETTER", "WS" ]

    ruleNames = [ "LETTER", "WS" ]

    grammarFileName = "MyGrammer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


