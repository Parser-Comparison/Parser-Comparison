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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\4")
        buf.write("\24\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\7\2\f\n\2\f\2")
        buf.write("\16\2\17\13\2\3\3\3\3\3\3\3\3\2\3\2\4\2\4\2\2\2\22\2\6")
        buf.write("\3\2\2\2\4\20\3\2\2\2\6\7\b\2\1\2\7\b\7\3\2\2\b\r\3\2")
        buf.write("\2\2\t\n\f\4\2\2\n\f\5\2\2\5\13\t\3\2\2\2\f\17\3\2\2\2")
        buf.write("\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\r\3\2\2\2\20")
        buf.write("\21\5\2\2\2\21\22\7\2\2\3\22\5\3\2\2\2\3\r")
        return buf.getvalue()


class MyGrammerParser ( Parser ):

    grammarFileName = "MyGrammer.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "LETTER", "WS" ]

    RULE_s = 0
    RULE_line = 1

    ruleNames =  [ "s", "line" ]

    EOF = Token.EOF
    LETTER=1
    WS=2

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_s

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class LetterExprContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.SContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def LETTER(self):
            return self.getToken(MyGrammerParser.LETTER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetterExpr" ):
                listener.enterLetterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetterExpr" ):
                listener.exitLetterExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetterExpr" ):
                return visitor.visitLetterExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(SContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.SContext
            super().__init__(parser)
            self.left = None # SContext
            self.right = None # SContext
            self.copyFrom(ctx)

        def s(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyGrammerParser.SContext)
            else:
                return self.getTypedRuleContext(MyGrammerParser.SContext,i)


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



    def s(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyGrammerParser.SContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_s, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MyGrammerParser.LetterExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 5
            localctx.atom = self.match(MyGrammerParser.LETTER)
            self._ctx.stop = self._input.LT(-1)
            self.state = 11
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyGrammerParser.InfixExprContext(self, MyGrammerParser.SContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_s)
                    self.state = 7
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 8
                    localctx.right = self.s(3) 
                self.state = 13
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyGrammerParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LineExprContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyGrammerParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def s(self):
            return self.getTypedRuleContext(MyGrammerParser.SContext,0)

        def EOF(self):
            return self.getToken(MyGrammerParser.EOF, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineExpr" ):
                listener.enterLineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineExpr" ):
                listener.exitLineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineExpr" ):
                return visitor.visitLineExpr(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = MyGrammerParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            localctx = MyGrammerParser.LineExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.s(0)
            self.state = 15
            self.match(MyGrammerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.s_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def s_sempred(self, localctx:SContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




