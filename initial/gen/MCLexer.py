# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/PPL-Assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u012d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\6\7\u0085\n\7\r\7\16\7\u0086\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\7\b\u008f\n\b\f\b\16\b\u0092\13\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\7\t\u009a\n\t\f\t\16\t\u009d\13\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\7\n\u00a6\n\n\f\n\16\n\u00a9\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\6")
        buf.write("+\u010e\n+\r+\16+\u010f\3,\3,\5,\u0114\n,\3-\5-\u0117")
        buf.write("\n-\3-\3-\3-\3-\3-\5-\u011e\n-\5-\u0120\n-\3.\3.\3/\3")
        buf.write("/\5/\u0126\n/\3\60\3\60\3\61\3\61\3\62\3\62\3\u009b\2")
        buf.write("\63\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63\3\2\7\5\2\13\f\17\17")
        buf.write("\"\"\4\2\13\f\16\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;")
        buf.write("\2\u0136\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\3e\3")
        buf.write("\2\2\2\5i\3\2\2\2\7q\3\2\2\2\tx\3\2\2\2\13~\3\2\2\2\r")
        buf.write("\u0084\3\2\2\2\17\u008a\3\2\2\2\21\u0095\3\2\2\2\23\u00a3")
        buf.write("\3\2\2\2\25\u00aa\3\2\2\2\27\u00b0\3\2\2\2\31\u00b9\3")
        buf.write("\2\2\2\33\u00be\3\2\2\2\35\u00c2\3\2\2\2\37\u00c5\3\2")
        buf.write("\2\2!\u00c8\3\2\2\2#\u00ce\3\2\2\2%\u00d3\3\2\2\2\'\u00d9")
        buf.write("\3\2\2\2)\u00db\3\2\2\2+\u00dd\3\2\2\2-\u00df\3\2\2\2")
        buf.write("/\u00e1\3\2\2\2\61\u00e3\3\2\2\2\63\u00e5\3\2\2\2\65\u00e7")
        buf.write("\3\2\2\2\67\u00ea\3\2\2\29\u00ed\3\2\2\2;\u00f0\3\2\2")
        buf.write("\2=\u00f2\3\2\2\2?\u00f4\3\2\2\2A\u00f7\3\2\2\2C\u00fa")
        buf.write("\3\2\2\2E\u00fc\3\2\2\2G\u00fe\3\2\2\2I\u0100\3\2\2\2")
        buf.write("K\u0102\3\2\2\2M\u0104\3\2\2\2O\u0106\3\2\2\2Q\u0108\3")
        buf.write("\2\2\2S\u010a\3\2\2\2U\u010d\3\2\2\2W\u0113\3\2\2\2Y\u011f")
        buf.write("\3\2\2\2[\u0121\3\2\2\2]\u0125\3\2\2\2_\u0127\3\2\2\2")
        buf.write("a\u0129\3\2\2\2c\u012b\3\2\2\2ef\7k\2\2fg\7p\2\2gh\7v")
        buf.write("\2\2h\4\3\2\2\2ij\7d\2\2jk\7q\2\2kl\7q\2\2lm\7n\2\2mn")
        buf.write("\7g\2\2no\7c\2\2op\7p\2\2p\6\3\2\2\2qr\7u\2\2rs\7v\2\2")
        buf.write("st\7t\2\2tu\7k\2\2uv\7p\2\2vw\7i\2\2w\b\3\2\2\2xy\7h\2")
        buf.write("\2yz\7n\2\2z{\7q\2\2{|\7c\2\2|}\7v\2\2}\n\3\2\2\2~\177")
        buf.write("\7x\2\2\177\u0080\7q\2\2\u0080\u0081\7k\2\2\u0081\u0082")
        buf.write("\7f\2\2\u0082\f\3\2\2\2\u0083\u0085\t\2\2\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\b\7\2\2")
        buf.write("\u0089\16\3\2\2\2\u008a\u008b\7\61\2\2\u008b\u008c\7\61")
        buf.write("\2\2\u008c\u0090\3\2\2\2\u008d\u008f\n\3\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0093\3\2\2\2\u0092\u0090\3\2\2\2")
        buf.write("\u0093\u0094\b\b\2\2\u0094\20\3\2\2\2\u0095\u0096\7\61")
        buf.write("\2\2\u0096\u0097\7,\2\2\u0097\u009b\3\2\2\2\u0098\u009a")
        buf.write("\13\2\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u009f\7,\2\2\u009f\u00a0\7")
        buf.write("\61\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\b\t\2\2\u00a2")
        buf.write("\22\3\2\2\2\u00a3\u00a7\t\4\2\2\u00a4\u00a6\t\5\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a9\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\24\3\2\2\2\u00a9\u00a7\3\2")
        buf.write("\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af\7m\2\2\u00af\26")
        buf.write("\3\2\2\2\u00b0\u00b1\7e\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7v\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\u00b7\7w\2\2\u00b7\u00b8\7g\2\2\u00b8\30")
        buf.write("\3\2\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc")
        buf.write("\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\32\3\2\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7t\2\2\u00c1\34")
        buf.write("\3\2\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7h\2\2\u00c4\36")
        buf.write("\3\2\2\2\u00c5\u00c6\7f\2\2\u00c6\u00c7\7q\2\2\u00c7 ")
        buf.write("\3\2\2\2\u00c8\u00c9\7y\2\2\u00c9\u00ca\7j\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd\7g\2\2\u00cd\"")
        buf.write("\3\2\2\2\u00ce\u00cf\7v\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7w\2\2\u00d1\u00d2\7g\2\2\u00d2$\3\2\2\2\u00d3\u00d4")
        buf.write("\7h\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7n\2\2\u00d6\u00d7")
        buf.write("\7u\2\2\u00d7\u00d8\7g\2\2\u00d8&\3\2\2\2\u00d9\u00da")
        buf.write("\7-\2\2\u00da(\3\2\2\2\u00db\u00dc\7/\2\2\u00dc*\3\2\2")
        buf.write("\2\u00dd\u00de\7,\2\2\u00de,\3\2\2\2\u00df\u00e0\7\61")
        buf.write("\2\2\u00e0.\3\2\2\2\u00e1\u00e2\7#\2\2\u00e2\60\3\2\2")
        buf.write("\2\u00e3\u00e4\7\'\2\2\u00e4\62\3\2\2\2\u00e5\u00e6\7")
        buf.write("~\2\2\u00e6\64\3\2\2\2\u00e7\u00e8\7(\2\2\u00e8\u00e9")
        buf.write("\7(\2\2\u00e9\66\3\2\2\2\u00ea\u00eb\7#\2\2\u00eb\u00ec")
        buf.write("\7?\2\2\u00ec8\3\2\2\2\u00ed\u00ee\7?\2\2\u00ee\u00ef")
        buf.write("\7?\2\2\u00ef:\3\2\2\2\u00f0\u00f1\7>\2\2\u00f1<\3\2\2")
        buf.write("\2\u00f2\u00f3\7@\2\2\u00f3>\3\2\2\2\u00f4\u00f5\7>\2")
        buf.write("\2\u00f5\u00f6\7?\2\2\u00f6@\3\2\2\2\u00f7\u00f8\7@\2")
        buf.write("\2\u00f8\u00f9\7?\2\2\u00f9B\3\2\2\2\u00fa\u00fb\7?\2")
        buf.write("\2\u00fbD\3\2\2\2\u00fc\u00fd\7]\2\2\u00fdF\3\2\2\2\u00fe")
        buf.write("\u00ff\7_\2\2\u00ffH\3\2\2\2\u0100\u0101\7}\2\2\u0101")
        buf.write("J\3\2\2\2\u0102\u0103\7\177\2\2\u0103L\3\2\2\2\u0104\u0105")
        buf.write("\7*\2\2\u0105N\3\2\2\2\u0106\u0107\7+\2\2\u0107P\3\2\2")
        buf.write("\2\u0108\u0109\7=\2\2\u0109R\3\2\2\2\u010a\u010b\7.\2")
        buf.write("\2\u010bT\3\2\2\2\u010c\u010e\t\6\2\2\u010d\u010c\3\2")
        buf.write("\2\2\u010e\u010f\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110V\3\2\2\2\u0111\u0114\5Y-\2\u0112\u0114")
        buf.write("\5[.\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114X")
        buf.write("\3\2\2\2\u0115\u0117\5U+\2\u0116\u0115\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\7\60\2\2\u0119")
        buf.write("\u0120\5U+\2\u011a\u011b\5U+\2\u011b\u011d\7\60\2\2\u011c")
        buf.write("\u011e\5U+\2\u011d\u011c\3\2\2\2\u011d\u011e\3\2\2\2\u011e")
        buf.write("\u0120\3\2\2\2\u011f\u0116\3\2\2\2\u011f\u011a\3\2\2\2")
        buf.write("\u0120Z\3\2\2\2\u0121\u0122\3\2\2\2\u0122\\\3\2\2\2\u0123")
        buf.write("\u0126\5#\22\2\u0124\u0126\5%\23\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0124\3\2\2\2\u0126^\3\2\2\2\u0127\u0128\13\2\2")
        buf.write("\2\u0128`\3\2\2\2\u0129\u012a\13\2\2\2\u012ab\3\2\2\2")
        buf.write("\u012b\u012c\13\2\2\2\u012cd\3\2\2\2\r\2\u0086\u0090\u009b")
        buf.write("\u00a7\u010f\u0113\u0116\u011d\u011f\u0125\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    BOOLTYPE = 2
    STRINGTYPE = 3
    FLOATTYPE = 4
    VOIDTYPE = 5
    WS = 6
    COMMENTS_LINE = 7
    COMMENTS_BLOCK = 8
    ID = 9
    BREAK = 10
    CONTINUE = 11
    ELSE = 12
    FOR = 13
    IF = 14
    DO = 15
    WHILE = 16
    TRUE = 17
    FALSE = 18
    ADD_OP = 19
    SUB_OP = 20
    MUL_OP = 21
    DIV_OP = 22
    NOT_OP = 23
    MOD_OP = 24
    OR_OP = 25
    AND_OP = 26
    NOT_EQUAL_OP = 27
    EQUAL_OP = 28
    LESS_OP = 29
    GREATER_OP = 30
    LESS_EQUAL_OP = 31
    GREATER_EQUAL_OP = 32
    ASSIGN_OP = 33
    LSB = 34
    RSB = 35
    LP = 36
    RP = 37
    LB = 38
    RB = 39
    SEMI = 40
    COMMA = 41
    INTLIT = 42
    FLOATLIT = 43
    FRAC = 44
    EXPONENT = 45
    BOOLLIT = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'boolean'", "'string'", "'float'", "'void'", "'break'", 
            "'continue'", "'else'", "'for'", "'if'", "'do'", "'while'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'!'", "'%'", 
            "'|'", "'&&'", "'!='", "'=='", "'<'", "'>'", "'<='", "'>='", 
            "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "BOOLTYPE", "STRINGTYPE", "FLOATTYPE", "VOIDTYPE", 
            "WS", "COMMENTS_LINE", "COMMENTS_BLOCK", "ID", "BREAK", "CONTINUE", 
            "ELSE", "FOR", "IF", "DO", "WHILE", "TRUE", "FALSE", "ADD_OP", 
            "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", "MOD_OP", "OR_OP", "AND_OP", 
            "NOT_EQUAL_OP", "EQUAL_OP", "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", 
            "GREATER_EQUAL_OP", "ASSIGN_OP", "LSB", "RSB", "LP", "RP", "LB", 
            "RB", "SEMI", "COMMA", "INTLIT", "FLOATLIT", "FRAC", "EXPONENT", 
            "BOOLLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "BOOLTYPE", "STRINGTYPE", "FLOATTYPE", "VOIDTYPE", 
                  "WS", "COMMENTS_LINE", "COMMENTS_BLOCK", "ID", "BREAK", 
                  "CONTINUE", "ELSE", "FOR", "IF", "DO", "WHILE", "TRUE", 
                  "FALSE", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                  "MOD_OP", "OR_OP", "AND_OP", "NOT_EQUAL_OP", "EQUAL_OP", 
                  "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", "GREATER_EQUAL_OP", 
                  "ASSIGN_OP", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", 
                  "COMMA", "INTLIT", "FLOATLIT", "FRAC", "EXPONENT", "BOOLLIT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


