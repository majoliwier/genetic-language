# Generated from C:/Users/Oliwier/Desktop/genetyczne/genetic-language/grammar/MiniLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,1,1,
        1,1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,3,6,63,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,72,8,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,86,8,7,10,7,12,
        7,89,9,7,1,7,0,1,14,8,0,2,4,6,8,10,12,14,0,4,1,0,7,9,1,0,10,11,1,
        0,12,17,1,0,18,19,93,0,16,1,0,0,0,2,19,1,0,0,0,4,32,1,0,0,0,6,34,
        1,0,0,0,8,40,1,0,0,0,10,46,1,0,0,0,12,62,1,0,0,0,14,71,1,0,0,0,16,
        17,3,2,1,0,17,18,5,0,0,1,18,1,1,0,0,0,19,23,5,1,0,0,20,22,3,4,2,
        0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,
        1,0,0,0,25,23,1,0,0,0,26,27,5,2,0,0,27,3,1,0,0,0,28,33,3,10,5,0,
        29,33,3,6,3,0,30,33,3,8,4,0,31,33,3,12,6,0,32,28,1,0,0,0,32,29,1,
        0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,5,1,0,0,0,34,35,5,20,0,0,35,
        36,5,3,0,0,36,37,3,14,7,0,37,38,5,4,0,0,38,39,3,2,1,0,39,7,1,0,0,
        0,40,41,5,21,0,0,41,42,5,3,0,0,42,43,3,14,7,0,43,44,5,4,0,0,44,45,
        3,2,1,0,45,9,1,0,0,0,46,47,5,24,0,0,47,48,5,5,0,0,48,49,3,14,7,0,
        49,50,5,6,0,0,50,11,1,0,0,0,51,52,5,22,0,0,52,53,5,3,0,0,53,54,5,
        24,0,0,54,55,5,4,0,0,55,63,5,6,0,0,56,57,5,23,0,0,57,58,5,3,0,0,
        58,59,3,14,7,0,59,60,5,4,0,0,60,61,5,6,0,0,61,63,1,0,0,0,62,51,1,
        0,0,0,62,56,1,0,0,0,63,13,1,0,0,0,64,65,6,7,-1,0,65,66,5,3,0,0,66,
        67,3,14,7,0,67,68,5,4,0,0,68,72,1,0,0,0,69,72,5,24,0,0,70,72,5,25,
        0,0,71,64,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,87,1,0,0,0,73,74,
        10,7,0,0,74,75,7,0,0,0,75,86,3,14,7,8,76,77,10,6,0,0,77,78,7,1,0,
        0,78,86,3,14,7,7,79,80,10,5,0,0,80,81,7,2,0,0,81,86,3,14,7,6,82,
        83,10,4,0,0,83,84,7,3,0,0,84,86,3,14,7,5,85,73,1,0,0,0,85,76,1,0,
        0,0,85,79,1,0,0,0,85,82,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,
        1,0,0,0,88,15,1,0,0,0,89,87,1,0,0,0,6,23,32,62,71,85,87
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "')'", "'='", "';'", 
                     "'*'", "'/'", "'%'", "'+'", "'-'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", "'while'", 
                     "'if'", "'input'", "'output'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WHILE", "IF", "INPUT", "OUTPUT", "ID", "NUMBER", 
                      "WS" ]

    RULE_program = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_whileStatement = 3
    RULE_ifStatement = 4
    RULE_assignStatement = 5
    RULE_ioStatement = 6
    RULE_expression = 7

    ruleNames =  [ "program", "block", "statement", "whileStatement", "ifStatement", 
                   "assignStatement", "ioStatement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    WHILE=20
    IF=21
    INPUT=22
    OUTPUT=23
    ID=24
    NUMBER=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def EOF(self):
            return self.getToken(MiniLangParser.EOF, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.block()
            self.state = 17
            self.match(MiniLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(MiniLangParser.T__0)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32505856) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(MiniLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(MiniLangParser.AssignStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MiniLangParser.WhileStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniLangParser.IfStatementContext,0)


        def ioStatement(self):
            return self.getTypedRuleContext(MiniLangParser.IoStatementContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.assignStatement()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.whileStatement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.ifStatement()
                pass
            elif token in [22, 23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.ioStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MiniLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MiniLangParser.WHILE)
            self.state = 35
            self.match(MiniLangParser.T__2)
            self.state = 36
            self.expression(0)
            self.state = 37
            self.match(MiniLangParser.T__3)
            self.state = 38
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniLangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniLangParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MiniLangParser.IF)
            self.state = 41
            self.match(MiniLangParser.T__2)
            self.state = 42
            self.expression(0)
            self.state = 43
            self.match(MiniLangParser.T__3)
            self.state = 44
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = MiniLangParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(MiniLangParser.ID)
            self.state = 47
            self.match(MiniLangParser.T__4)
            self.state = 48
            self.expression(0)
            self.state = 49
            self.match(MiniLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(MiniLangParser.INPUT, 0)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def OUTPUT(self):
            return self.getToken(MiniLangParser.OUTPUT, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniLangParser.RULE_ioStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoStatement" ):
                listener.enterIoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoStatement" ):
                listener.exitIoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIoStatement" ):
                return visitor.visitIoStatement(self)
            else:
                return visitor.visitChildren(self)




    def ioStatement(self):

        localctx = MiniLangParser.IoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ioStatement)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(MiniLangParser.INPUT)
                self.state = 52
                self.match(MiniLangParser.T__2)
                self.state = 53
                self.match(MiniLangParser.ID)
                self.state = 54
                self.match(MiniLangParser.T__3)
                self.state = 55
                self.match(MiniLangParser.T__5)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.match(MiniLangParser.OUTPUT)
                self.state = 57
                self.match(MiniLangParser.T__2)
                self.state = 58
                self.expression(0)
                self.state = 59
                self.match(MiniLangParser.T__3)
                self.state = 60
                self.match(MiniLangParser.T__5)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExpressionContext,i)


        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(MiniLangParser.NUMBER, 0)

        def getRuleIndex(self):
            return MiniLangParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 65
                self.match(MiniLangParser.T__2)
                self.state = 66
                self.expression(0)
                self.state = 67
                self.match(MiniLangParser.T__3)
                pass
            elif token in [24]:
                self.state = 69
                self.match(MiniLangParser.ID)
                pass
            elif token in [25]:
                self.state = 70
                self.match(MiniLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 85
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 73
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 74
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 75
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 77
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 79
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 80
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 81
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = MiniLangParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 83
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 84
                        self.expression(5)
                        pass

             
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




