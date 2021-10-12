# Generated from MyGrammer.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammerParser.

class MyGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammerParser#NumberExpr.
    def visitNumberExpr(self, ctx:MyGrammerParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ByeExpr.
    def visitByeExpr(self, ctx:MyGrammerParser.ByeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#HelloExpr.
    def visitHelloExpr(self, ctx:MyGrammerParser.HelloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ParenExpr.
    def visitParenExpr(self, ctx:MyGrammerParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#InfixExpr.
    def visitInfixExpr(self, ctx:MyGrammerParser.InfixExprContext):
        return self.visitChildren(ctx)



del MyGrammerParser