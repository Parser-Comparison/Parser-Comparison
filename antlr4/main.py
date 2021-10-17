import sys
import time
from antlr4 import *
from antlr4.tree.Trees import Trees
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor

  
class MyVisitor(MyGrammerVisitor):
    def visitLetterExpr(self, ctx):
        value = ctx.getText()
        return value == 'a'

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        return l and r

if __name__ == "__main__":
    while 1:
        data =  InputStream(input(">>> "))
        start = time.time()
        # lexer
        lexer = MyGrammerLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = MyGrammerParser(stream)
        tree = parser.expr()
        # evaluator
        visitor = MyVisitor()
        output = visitor.visit(tree)
        print(output)
        print(Trees.toStringTree(tree, None, parser))
        end = time.time()
        print(f"Runtime was {end - start}")