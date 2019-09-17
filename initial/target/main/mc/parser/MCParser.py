# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\6\2\24\n\2\r\2\16\2\25\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\5\6#\n\6\3\7\3\7\3\7")
        buf.write("\5\7(\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\2\2\n\2\4\6\b\n\f\16\20\2\3\3\2\3\7\2/\2\23\3\2\2")
        buf.write("\2\4\31\3\2\2\2\6\33\3\2\2\2\b\35\3\2\2\2\n\"\3\2\2\2")
        buf.write("\f$\3\2\2\2\16+\3\2\2\2\20\60\3\2\2\2\22\24\5\4\3\2\23")
        buf.write("\22\3\2\2\2\24\25\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\27\3\2\2\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32\13\2\2")
        buf.write("\2\32\5\3\2\2\2\33\34\t\2\2\2\34\7\3\2\2\2\35\36\5\f\7")
        buf.write("\2\36\37\7*\2\2\37\t\3\2\2\2 #\5\f\7\2!#\7,\2\2\" \3\2")
        buf.write("\2\2\"!\3\2\2\2#\13\3\2\2\2$%\7\13\2\2%\'\7(\2\2&(\5\n")
        buf.write("\6\2\'&\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7)\2\2*\r\3\2\2")
        buf.write("\2+,\7\13\2\2,-\7$\2\2-.\7,\2\2./\7%\2\2/\17\3\2\2\2\60")
        buf.write("\61\5\6\4\2\61\62\7$\2\2\62\63\7%\2\2\63\21\3\2\2\2\5")
        buf.write("\25\"\'")
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
    RULE_declarations = 1
    RULE_mctype = 2
    RULE_body = 3
    RULE_exp = 4
    RULE_funcall = 5
    RULE_arrayid = 6
    RULE_arraypointertype = 7

    ruleNames =  [ "program", "declarations", "mctype", "body", "exp", "funcall", 
                   "arrayid", "arraypointertype" ]

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

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def declarations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclarationsContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclarationsContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.declarations()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.WS) | (1 << MCParser.COMMENTS_LINE) | (1 << MCParser.COMMENTS_BLOCK) | (1 << MCParser.ID) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.ELSE) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.WHILE) | (1 << MCParser.TRUE) | (1 << MCParser.FALSE) | (1 << MCParser.ADD_OP) | (1 << MCParser.SUB_OP) | (1 << MCParser.MUL_OP) | (1 << MCParser.DIV_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.MOD_OP) | (1 << MCParser.OR_OP) | (1 << MCParser.AND_OP) | (1 << MCParser.NOT_EQUAL_OP) | (1 << MCParser.EQUAL_OP) | (1 << MCParser.LESS_OP) | (1 << MCParser.GREATER_OP) | (1 << MCParser.LESS_EQUAL_OP) | (1 << MCParser.GREATER_EQUAL_OP) | (1 << MCParser.ASSIGN_OP) | (1 << MCParser.LSB) | (1 << MCParser.RSB) | (1 << MCParser.LP) | (1 << MCParser.RP) | (1 << MCParser.LB) | (1 << MCParser.RB) | (1 << MCParser.SEMI) | (1 << MCParser.COMMA) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.FRAC) | (1 << MCParser.EXPONENT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.ERROR_CHAR) | (1 << MCParser.UNCLOSE_STRING) | (1 << MCParser.ILLEGAL_ESCAPE))) != 0)):
                    break

            self.state = 21
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MCParser.RULE_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = MCParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.matchWildcard()
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
        self.enterRule(localctx, 4, self.RULE_mctype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
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
        self.enterRule(localctx, 6, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.funcall()
            self.state = 28
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
        self.enterRule(localctx, 8, self.RULE_exp)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.funcall()
                pass
            elif token in [MCParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
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
        self.enterRule(localctx, 10, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MCParser.ID)
            self.state = 35
            self.match(MCParser.LB)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.ID or _la==MCParser.INTLIT:
                self.state = 36
                self.exp()


            self.state = 39
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
        self.enterRule(localctx, 12, self.RULE_arrayid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(MCParser.ID)
            self.state = 42
            self.match(MCParser.LSB)
            self.state = 43
            self.match(MCParser.INTLIT)
            self.state = 44
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
        self.enterRule(localctx, 14, self.RULE_arraypointertype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.mctype()
            self.state = 47
            self.match(MCParser.LSB)
            self.state = 48
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





