# Generated from MyGrammer.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\32\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\r\n\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\7\2\25\n\2\f\2\16\2\30\13\2\3")
        buf.write("\2\2\3\2\3\2\2\4\3\2\3\4\3\2\5\6\2\35\2\f\3\2\2\2\4\5")
        buf.write("\b\2\1\2\5\r\7\13\2\2\6\7\7\7\2\2\7\b\5\2\2\2\b\t\7\b")
        buf.write("\2\2\t\r\3\2\2\2\n\r\7\t\2\2\13\r\7\n\2\2\f\4\3\2\2\2")
        buf.write("\f\6\3\2\2\2\f\n\3\2\2\2\f\13\3\2\2\2\r\26\3\2\2\2\16")
        buf.write("\17\f\b\2\2\17\20\t\2\2\2\20\25\5\2\2\t\21\22\f\7\2\2")
        buf.write("\22\23\t\3\2\2\23\25\5\2\2\b\24\16\3\2\2\2\24\21\3\2\2")
        buf.write("\2\25\30\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\3\3\2")
        buf.write("\2\2\30\26\3\2\2\2\5\f\24\26")
        return buf.getvalue()


class MyGrammerParser ( Parser ):

    grammarFileName = "MyGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "HELLO", "BYE", 
                      "INT", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    HELLO=7
    BYE=8
    INT=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MyGrammerParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ByeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def BYE(self):
            return self.getToken(MyGrammerParser.BYE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterByeExpr" ):
                listener.enterByeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitByeExpr" ):
                listener.exitByeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByeExpr" ):
                return visitor.visitByeExpr(self)
            else:
                return visitor.visitChildren(self)


    class HelloExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def HELLO(self):
            return self.getToken(MyGrammerParser.HELLO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelloExpr" ):
                listener.enterHelloExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelloExpr" ):
                listener.exitHelloExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelloExpr" ):
                return visitor.visitHelloExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyGrammerParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MyGrammerParser.INT]:
                localctx = MyGrammerParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                localctx.atom = self.match(MyGrammerParser.INT)
                pass
            elif token in [MyGrammerParser.T__4]:
                localctx = MyGrammerParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 4
                self.match(MyGrammerParser.T__4)
                self.state = 5
                self.expr(0)
                self.state = 6
                self.match(MyGrammerParser.T__5)
                pass
            elif token in [MyGrammerParser.HELLO]:
                localctx = MyGrammerParser.HelloExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                localctx.atom = self.match(MyGrammerParser.HELLO)
                pass
            elif token in [MyGrammerParser.BYE]:
                localctx = MyGrammerParser.ByeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                localctx.atom = self.match(MyGrammerParser.BYE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 20
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 18
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = MyGrammerParser.InfixExprContext(self, MyGrammerParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 12
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 13
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammerParser.T__0 or _la==MyGrammerParser.T__1):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 14
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MyGrammerParser.InfixExprContext(self, MyGrammerParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 16
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MyGrammerParser.T__2 or _la==MyGrammerParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 17
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 22
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




