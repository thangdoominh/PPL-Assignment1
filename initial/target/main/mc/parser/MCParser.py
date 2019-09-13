# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\5\5\34")
        buf.write("\n\5\3\6\3\6\3\6\5\6!\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\3\2\3\7")
        buf.write("\2(\2\20\3\2\2\2\4\24\3\2\2\2\6\26\3\2\2\2\b\33\3\2\2")
        buf.write("\2\n\35\3\2\2\2\f$\3\2\2\2\16)\3\2\2\2\20\21\5\4\3\2\21")
        buf.write("\22\7\t\2\2\22\23\7\2\2\3\23\3\3\2\2\2\24\25\t\2\2\2\25")
        buf.write("\5\3\2\2\2\26\27\5\n\6\2\27\30\7*\2\2\30\7\3\2\2\2\31")
        buf.write("\34\5\n\6\2\32\34\7,\2\2\33\31\3\2\2\2\33\32\3\2\2\2\34")
        buf.write("\t\3\2\2\2\35\36\7\13\2\2\36 \7(\2\2\37!\5\b\5\2 \37\3")
        buf.write("\2\2\2 !\3\2\2\2!\"\3\2\2\2\"#\7)\2\2#\13\3\2\2\2$%\7")
        buf.write("\13\2\2%&\7$\2\2&\'\7,\2\2\'(\7%\2\2(\r\3\2\2\2)*\5\4")
        buf.write("\3\2*+\7$\2\2+,\7%\2\2,\17\3\2\2\2\4\33 ")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'boolean'", "'string'", "'float'", 
                     "'void'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'break'", "'continue'", "'else'", "'for'", "'if'", 
                     "'do'", "'while'", "'true'", "'false'", "'+'", "'-'", 
                     "'*'", "'/'", "'!'", "'%'", "'|'", "'&&'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'='", "'['", 
                     "']'", "'{'", "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "INTTYPE", "BOOLTYPE", "STRINGTYPE", 
                      "FLOATTYPE", "VOIDTYPE", "WS", "COMMENTS_LINE", "COMMENTS_BLOCK", 
                      "ID", "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "DO", 
                      "WHILE", "TRUE", "FALSE", "ADD_OP", "SUB_OP", "MUL_OP", 
                      "DIV_OP", "NOT_OP", "MOD_OP", "OR_OP", "AND_OP", "NOT_EQUAL_OP", 
                      "EQUAL_OP", "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", 
                      "GREATER_EQUAL_OP", "ASSIGN_OP", "LSB", "RSB", "LP", 
                      "RP", "LB", "RB", "SEMI", "COMMA", "INTLIT", "FLOATLIT", 
                      "FRAC", "EXPONENT", "BOOLLIT", "STRINGLIT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mctype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4
    RULE_arrayid = 5
    RULE_arraypointertype = 6

    ruleNames =  [ "program", "mctype", "body", "exp", "funcall", "arrayid", 
                   "arraypointertype" ]

    EOF = Token.EOF
    INTTYPE=1
    BOOLTYPE=2
    STRINGTYPE=3
    FLOATTYPE=4
    VOIDTYPE=5
    WS=6
    COMMENTS_LINE=7
    COMMENTS_BLOCK=8
    ID=9
    BREAK=10
    CONTINUE=11
    ELSE=12
    FOR=13
    IF=14
    DO=15
    WHILE=16
    TRUE=17
    FALSE=18
    ADD_OP=19
    SUB_OP=20
    MUL_OP=21
    DIV_OP=22
    NOT_OP=23
    MOD_OP=24
    OR_OP=25
    AND_OP=26
    NOT_EQUAL_OP=27
    EQUAL_OP=28
    LESS_OP=29
    GREATER_OP=30
    LESS_EQUAL_OP=31
    GREATER_EQUAL_OP=32
    ASSIGN_OP=33
    LSB=34
    RSB=35
    LP=36
    RP=37
    LB=38
    RB=39
    SEMI=40
    COMMA=41
    INTLIT=42
    FLOATLIT=43
    FRAC=44
    EXPONENT=45
    BOOLLIT=46
    STRINGLIT=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def COMMENTS_LINE(self):
            return self.getToken(MCParser.COMMENTS_LINE, 0)

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.mctype()
            self.state = 15
            self.match(MCParser.COMMENTS_LINE)
            self.state = 16
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MctypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = MCParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mctype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MCParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.funcall()
            self.state = 21
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.funcall()
                pass
            elif token in [MCParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(MCParser.INTLIT)
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


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MCParser.ExpContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MCParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(MCParser.ID)
            self.state = 28
            self.match(MCParser.LB)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID or _la==MCParser.INTLIT:
                self.state = 29
                self.exp()


            self.state = 32
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arrayid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayid" ):
                return visitor.visitArrayid(self)
            else:
                return visitor.visitChildren(self)




    def arrayid(self):

        localctx = MCParser.ArrayidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MCParser.ID)
            self.state = 35
            self.match(MCParser.LSB)
            self.state = 36
            self.match(MCParser.INTLIT)
            self.state = 37
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraypointertypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mctype(self):
            return self.getTypedRuleContext(MCParser.MctypeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arraypointertype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraypointertype" ):
                return visitor.visitArraypointertype(self)
            else:
                return visitor.visitChildren(self)




    def arraypointertype(self):

        localctx = MCParser.ArraypointertypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arraypointertype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.mctype()
            self.state = 40
            self.match(MCParser.LSB)
            self.state = 41
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





