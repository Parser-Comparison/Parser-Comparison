# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete listener for a parse tree produced by MyGrammerParser.
class MyGrammerListener(ParseTreeListener):

    # Enter a parse tree produced by MyGrammerParser#NumberExpr.
    def enterNumberExpr(self, ctx:MyGrammerParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#NumberExpr.
    def exitNumberExpr(self, ctx:MyGrammerParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#ByeExpr.
    def enterByeExpr(self, ctx:MyGrammerParser.ByeExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#ByeExpr.
    def exitByeExpr(self, ctx:MyGrammerParser.ByeExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#HelloExpr.
    def enterHelloExpr(self, ctx:MyGrammerParser.HelloExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#HelloExpr.
    def exitHelloExpr(self, ctx:MyGrammerParser.HelloExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#ParenExpr.
    def enterParenExpr(self, ctx:MyGrammerParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#ParenExpr.
    def exitParenExpr(self, ctx:MyGrammerParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MyGrammerParser#InfixExpr.
    def enterInfixExpr(self, ctx:MyGrammerParser.InfixExprContext):
        pass

    # Exit a parse tree produced by MyGrammerParser#InfixExpr.
    def exitInfixExpr(self, ctx:MyGrammerParser.InfixExprContext):
        pass



del MyGrammerParser