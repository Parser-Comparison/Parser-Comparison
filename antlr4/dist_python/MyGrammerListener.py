# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#LetterExpr.
    def enterLetterExpr(self, ctx:MyGrammerParser.LetterExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#LetterExpr.
    def exitLetterExpr(self, ctx:MyGrammerParser.LetterExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#InfixExpr.
    def enterInfixExpr(self, ctx:MyGrammerParser.InfixExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#InfixExpr.
    def exitInfixExpr(self, ctx:MyGrammerParser.InfixExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#LineExpr.
    def enterLineExpr(self, ctx:MyGrammerParser.LineExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#LineExpr.
    def exitLineExpr(self, ctx:MyGrammerParser.LineExprContext):
        pass



del MyGrammerParser