# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\3\2\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\7\6-\n\6\f\6\16\6\60\13\6\3\7\3\7")
        buf.write("\5\7\64\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\5")
        buf.write("\n@\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nJ\n\n\f\n\16")
        buf.write("\nM\13\n\5\nO\n\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\5\fZ\n\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\2\3\3\2\3\6\2\\\2\31\3\2\2\2\4!\3\2\2\2\6#\3\2")
        buf.write("\2\2\b\'\3\2\2\2\n)\3\2\2\2\f\63\3\2\2\2\16\65\3\2\2\2")
        buf.write("\20:\3\2\2\2\22?\3\2\2\2\24U\3\2\2\2\26Y\3\2\2\2\30\32")
        buf.write("\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33")
        buf.write("\34\3\2\2\2\34\35\3\2\2\2\35\36\7\2\2\3\36\3\3\2\2\2\37")
        buf.write("\"\5\6\4\2 \"\5\22\n\2!\37\3\2\2\2! \3\2\2\2\"\5\3\2\2")
        buf.write("\2#$\5\b\5\2$%\5\n\6\2%&\7*\2\2&\7\3\2\2\2\'(\t\2\2\2")
        buf.write("(\t\3\2\2\2).\5\f\7\2*+\7+\2\2+-\5\f\7\2,*\3\2\2\2-\60")
        buf.write("\3\2\2\2.,\3\2\2\2./\3\2\2\2/\13\3\2\2\2\60.\3\2\2\2\61")
        buf.write("\64\5\16\b\2\62\64\5\20\t\2\63\61\3\2\2\2\63\62\3\2\2")
        buf.write("\2\64\r\3\2\2\2\65\66\7\13\2\2\66\67\7$\2\2\678\7,\2\2")
        buf.write("89\7%\2\29\17\3\2\2\2:;\7\13\2\2;\21\3\2\2\2<@\5\b\5\2")
        buf.write("=@\7\7\2\2>@\5\26\f\2?<\3\2\2\2?=\3\2\2\2?>\3\2\2\2@A")
        buf.write("\3\2\2\2AB\7\13\2\2BN\7(\2\2CD\5\b\5\2DK\5\f\7\2EF\7+")
        buf.write("\2\2FG\5\b\5\2GH\5\f\7\2HJ\3\2\2\2IE\3\2\2\2JM\3\2\2\2")
        buf.write("KI\3\2\2\2KL\3\2\2\2LO\3\2\2\2MK\3\2\2\2NC\3\2\2\2NO\3")
        buf.write("\2\2\2OP\3\2\2\2PQ\7)\2\2QR\7&\2\2RS\5\24\13\2ST\7\'\2")
        buf.write("\2T\23\3\2\2\2UV\3\2\2\2V\25\3\2\2\2WZ\5\b\5\2XZ\7\7\2")
        buf.write("\2YW\3\2\2\2YX\3\2\2\2Z[\3\2\2\2[\\\7$\2\2\\]\7%\2\2]")
        buf.write("\27\3\2\2\2\n\33!.\63?KNY")
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
                      "FLOATTYPE", "VOIDTYPE", "COMMENTS_LINE", "COMMENTS_BLOCK", 
                      "WS", "ID", "BREAK", "CONTINUE", "ELSE", "FOR", "IF", 
                      "DO", "WHILE", "TRUE", "FALSE", "ADD_OP", "SUB_OP", 
                      "MUL_OP", "DIV_OP", "NOT_OP", "MOD_OP", "OR_OP", "AND_OP", 
                      "NOT_EQUAL_OP", "EQUAL_OP", "LESS_OP", "GREATER_OP", 
                      "LESS_EQUAL_OP", "GREATER_EQUAL_OP", "ASSIGN_OP", 
                      "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", "COMMA", 
                      "INTLIT", "FLOATLIT", "FRAC", "EXPONENT", "BOOLLIT", 
                      "STRINGLIT", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_vardeclaration = 2
    RULE_singletype = 3
    RULE_idlist = 4
    RULE_idtail = 5
    RULE_idarray = 6
    RULE_idsingle = 7
    RULE_funcdeclaration = 8
    RULE_block = 9
    RULE_arraypointertype = 10

    ruleNames =  [ "program", "declaration", "vardeclaration", "singletype", 
                   "idlist", "idtail", "idarray", "idsingle", "funcdeclaration", 
                   "block", "arraypointertype" ]

    EOF = Token.EOF
    INTTYPE=1
    BOOLTYPE=2
    STRINGTYPE=3
    FLOATTYPE=4
    VOIDTYPE=5
    COMMENTS_LINE=6
    COMMENTS_BLOCK=7
    WS=8
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
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50

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

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclarationContext,i)


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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.declaration()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

            self.state = 27
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclaration(self):
            return self.getTypedRuleContext(MCParser.VardeclarationContext,0)


        def funcdeclaration(self):
            return self.getTypedRuleContext(MCParser.FuncdeclarationContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.vardeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.funcdeclaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singletype(self):
            return self.getTypedRuleContext(MCParser.SingletypeContext,0)


        def idlist(self):
            return self.getTypedRuleContext(MCParser.IdlistContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_vardeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclaration" ):
                return visitor.visitVardeclaration(self)
            else:
                return visitor.visitChildren(self)




    def vardeclaration(self):

        localctx = MCParser.VardeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.singletype()
            self.state = 34
            self.idlist()
            self.state = 35
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingletypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def BOOLTYPE(self):
            return self.getToken(MCParser.BOOLTYPE, 0)

        def STRINGTYPE(self):
            return self.getToken(MCParser.STRINGTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_singletype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingletype" ):
                return visitor.visitSingletype(self)
            else:
                return visitor.visitChildren(self)




    def singletype(self):

        localctx = MCParser.SingletypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_singletype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE))) != 0)):
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


    class IdlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idtail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.IdtailContext)
            else:
                return self.getTypedRuleContext(MCParser.IdtailContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MCParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.idtail()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 40
                self.match(MCParser.COMMA)
                self.state = 41
                self.idtail()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdtailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idarray(self):
            return self.getTypedRuleContext(MCParser.IdarrayContext,0)


        def idsingle(self):
            return self.getTypedRuleContext(MCParser.IdsingleContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_idtail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdtail" ):
                return visitor.visitIdtail(self)
            else:
                return visitor.visitChildren(self)




    def idtail(self):

        localctx = MCParser.IdtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idtail)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.idarray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.idsingle()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdarrayContext(ParserRuleContext):

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
            return MCParser.RULE_idarray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdarray" ):
                return visitor.visitIdarray(self)
            else:
                return visitor.visitChildren(self)




    def idarray(self):

        localctx = MCParser.IdarrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_idarray)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(MCParser.ID)
            self.state = 52
            self.match(MCParser.LSB)
            self.state = 53
            self.match(MCParser.INTLIT)
            self.state = 54
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdsingleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_idsingle

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdsingle" ):
                return visitor.visitIdsingle(self)
            else:
                return visitor.visitChildren(self)




    def idsingle(self):

        localctx = MCParser.IdsingleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idsingle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def block(self):
            return self.getTypedRuleContext(MCParser.BlockContext,0)


        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def singletype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.SingletypeContext)
            else:
                return self.getTypedRuleContext(MCParser.SingletypeContext,i)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def arraypointertype(self):
            return self.getTypedRuleContext(MCParser.ArraypointertypeContext,0)


        def idtail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.IdtailContext)
            else:
                return self.getTypedRuleContext(MCParser.IdtailContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_funcdeclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdeclaration" ):
                return visitor.visitFuncdeclaration(self)
            else:
                return visitor.visitChildren(self)




    def funcdeclaration(self):

        localctx = MCParser.FuncdeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcdeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 58
                self.singletype()
                pass

            elif la_ == 2:
                self.state = 59
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.state = 60
                self.arraypointertype()
                pass


            self.state = 63
            self.match(MCParser.ID)
            self.state = 64
            self.match(MCParser.LB)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE))) != 0):
                self.state = 65
                self.singletype()
                self.state = 66
                self.idtail()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 67
                    self.match(MCParser.COMMA)
                    self.state = 68
                    self.singletype()
                    self.state = 69
                    self.idtail()
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 78
            self.match(MCParser.RB)
            self.state = 79
            self.match(MCParser.LP)
            self.state = 80
            self.block()
            self.state = 81
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MCParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)

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

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def singletype(self):
            return self.getTypedRuleContext(MCParser.SingletypeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arraypointertype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraypointertype" ):
                return visitor.visitArraypointertype(self)
            else:
                return visitor.visitChildren(self)




    def arraypointertype(self):

        localctx = MCParser.ArraypointertypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_arraypointertype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INTTYPE, MCParser.BOOLTYPE, MCParser.STRINGTYPE, MCParser.FLOATTYPE]:
                self.state = 85
                self.singletype()
                pass
            elif token in [MCParser.VOIDTYPE]:
                self.state = 86
                self.match(MCParser.VOIDTYPE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 89
            self.match(MCParser.LSB)
            self.state = 90
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





