# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/PPL-Assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0143\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\6\7\u0087\n\7\r\7\16\7\u0088\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\7\b\u0091\n\b\f\b\16\b\u0094\13\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\7\t\u009c\n\t\f\t\16\t\u009f\13\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\7\n\u00a8\n\n\f\n\16\n\u00ab")
        buf.write("\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\6+\u0110\n+\r+\16+\u0111\3,\3,\5,\u0116\n,\3-")
        buf.write("\3-\5-\u011a\n-\3-\3-\3-\3-\3-\5-\u0121\n-\5-\u0123\n")
        buf.write("-\3.\3.\5.\u0127\n.\3.\3.\5.\u012b\n.\3.\3.\3/\3/\5/\u0131")
        buf.write("\n/\3\60\3\60\3\60\3\60\7\60\u0137\n\60\f\60\16\60\u013a")
        buf.write("\13\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\u009d")
        buf.write("\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64\3\2\13\5\2\13\f\17")
        buf.write("\17\"\"\4\2\13\f\16\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\4\2--//\4\2GGgg\t\2$$^^ddhhppttvv\6\2\n\f\16\17$$^^")
        buf.write("\2\u0150\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\3g\3\2\2\2\5k\3\2\2\2\7s\3\2\2\2\tz\3\2\2\2\13")
        buf.write("\u0080\3\2\2\2\r\u0086\3\2\2\2\17\u008c\3\2\2\2\21\u0097")
        buf.write("\3\2\2\2\23\u00a5\3\2\2\2\25\u00ac\3\2\2\2\27\u00b2\3")
        buf.write("\2\2\2\31\u00bb\3\2\2\2\33\u00c0\3\2\2\2\35\u00c4\3\2")
        buf.write("\2\2\37\u00c7\3\2\2\2!\u00ca\3\2\2\2#\u00d0\3\2\2\2%\u00d5")
        buf.write("\3\2\2\2\'\u00db\3\2\2\2)\u00dd\3\2\2\2+\u00df\3\2\2\2")
        buf.write("-\u00e1\3\2\2\2/\u00e3\3\2\2\2\61\u00e5\3\2\2\2\63\u00e7")
        buf.write("\3\2\2\2\65\u00e9\3\2\2\2\67\u00ec\3\2\2\29\u00ef\3\2")
        buf.write("\2\2;\u00f2\3\2\2\2=\u00f4\3\2\2\2?\u00f6\3\2\2\2A\u00f9")
        buf.write("\3\2\2\2C\u00fc\3\2\2\2E\u00fe\3\2\2\2G\u0100\3\2\2\2")
        buf.write("I\u0102\3\2\2\2K\u0104\3\2\2\2M\u0106\3\2\2\2O\u0108\3")
        buf.write("\2\2\2Q\u010a\3\2\2\2S\u010c\3\2\2\2U\u010f\3\2\2\2W\u0115")
        buf.write("\3\2\2\2Y\u0122\3\2\2\2[\u0126\3\2\2\2]\u0130\3\2\2\2")
        buf.write("_\u0132\3\2\2\2a\u013d\3\2\2\2c\u013f\3\2\2\2e\u0141\3")
        buf.write("\2\2\2gh\7k\2\2hi\7p\2\2ij\7v\2\2j\4\3\2\2\2kl\7d\2\2")
        buf.write("lm\7q\2\2mn\7q\2\2no\7n\2\2op\7g\2\2pq\7c\2\2qr\7p\2\2")
        buf.write("r\6\3\2\2\2st\7u\2\2tu\7v\2\2uv\7t\2\2vw\7k\2\2wx\7p\2")
        buf.write("\2xy\7i\2\2y\b\3\2\2\2z{\7h\2\2{|\7n\2\2|}\7q\2\2}~\7")
        buf.write("c\2\2~\177\7v\2\2\177\n\3\2\2\2\u0080\u0081\7x\2\2\u0081")
        buf.write("\u0082\7q\2\2\u0082\u0083\7k\2\2\u0083\u0084\7f\2\2\u0084")
        buf.write("\f\3\2\2\2\u0085\u0087\t\2\2\2\u0086\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2")
        buf.write("\u0089\u008a\3\2\2\2\u008a\u008b\b\7\2\2\u008b\16\3\2")
        buf.write("\2\2\u008c\u008d\7\61\2\2\u008d\u008e\7\61\2\2\u008e\u0092")
        buf.write("\3\2\2\2\u008f\u0091\n\3\2\2\u0090\u008f\3\2\2\2\u0091")
        buf.write("\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u0095\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\b")
        buf.write("\b\2\2\u0096\20\3\2\2\2\u0097\u0098\7\61\2\2\u0098\u0099")
        buf.write("\7,\2\2\u0099\u009d\3\2\2\2\u009a\u009c\13\2\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u009d\3")
        buf.write("\2\2\2\u00a0\u00a1\7,\2\2\u00a1\u00a2\7\61\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\b\t\2\2\u00a4\22\3\2\2\2\u00a5\u00a9")
        buf.write("\t\4\2\2\u00a6\u00a8\t\5\2\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\24\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\7d\2")
        buf.write("\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7")
        buf.write("c\2\2\u00b0\u00b1\7m\2\2\u00b1\26\3\2\2\2\u00b2\u00b3")
        buf.write("\7e\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7v\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7w\2\2\u00b9\u00ba\7g\2\2\u00ba\30\3\2\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7n\2\2\u00bd\u00be\7u\2\2\u00be\u00bf")
        buf.write("\7g\2\2\u00bf\32\3\2\2\2\u00c0\u00c1\7h\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7t\2\2\u00c3\34\3\2\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7h\2\2\u00c6\36\3\2\2\2\u00c7\u00c8")
        buf.write("\7f\2\2\u00c8\u00c9\7q\2\2\u00c9 \3\2\2\2\u00ca\u00cb")
        buf.write("\7y\2\2\u00cb\u00cc\7j\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce")
        buf.write("\7n\2\2\u00ce\u00cf\7g\2\2\u00cf\"\3\2\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4$\3\2\2\2\u00d5\u00d6\7h\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7n\2\2\u00d8\u00d9\7u\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da&\3\2\2\2\u00db\u00dc\7-\2\2\u00dc(\3\2\2")
        buf.write("\2\u00dd\u00de\7/\2\2\u00de*\3\2\2\2\u00df\u00e0\7,\2")
        buf.write("\2\u00e0,\3\2\2\2\u00e1\u00e2\7\61\2\2\u00e2.\3\2\2\2")
        buf.write("\u00e3\u00e4\7#\2\2\u00e4\60\3\2\2\2\u00e5\u00e6\7\'\2")
        buf.write("\2\u00e6\62\3\2\2\2\u00e7\u00e8\7~\2\2\u00e8\64\3\2\2")
        buf.write("\2\u00e9\u00ea\7(\2\2\u00ea\u00eb\7(\2\2\u00eb\66\3\2")
        buf.write("\2\2\u00ec\u00ed\7#\2\2\u00ed\u00ee\7?\2\2\u00ee8\3\2")
        buf.write("\2\2\u00ef\u00f0\7?\2\2\u00f0\u00f1\7?\2\2\u00f1:\3\2")
        buf.write("\2\2\u00f2\u00f3\7>\2\2\u00f3<\3\2\2\2\u00f4\u00f5\7@")
        buf.write("\2\2\u00f5>\3\2\2\2\u00f6\u00f7\7>\2\2\u00f7\u00f8\7?")
        buf.write("\2\2\u00f8@\3\2\2\2\u00f9\u00fa\7@\2\2\u00fa\u00fb\7?")
        buf.write("\2\2\u00fbB\3\2\2\2\u00fc\u00fd\7?\2\2\u00fdD\3\2\2\2")
        buf.write("\u00fe\u00ff\7]\2\2\u00ffF\3\2\2\2\u0100\u0101\7_\2\2")
        buf.write("\u0101H\3\2\2\2\u0102\u0103\7}\2\2\u0103J\3\2\2\2\u0104")
        buf.write("\u0105\7\177\2\2\u0105L\3\2\2\2\u0106\u0107\7*\2\2\u0107")
        buf.write("N\3\2\2\2\u0108\u0109\7+\2\2\u0109P\3\2\2\2\u010a\u010b")
        buf.write("\7=\2\2\u010bR\3\2\2\2\u010c\u010d\7.\2\2\u010dT\3\2\2")
        buf.write("\2\u010e\u0110\t\6\2\2\u010f\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("V\3\2\2\2\u0113\u0116\5Y-\2\u0114\u0116\5[.\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0114\3\2\2\2\u0116X\3\2\2\2\u0117\u0119")
        buf.write("\t\7\2\2\u0118\u011a\5U+\2\u0119\u0118\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c\7\60\2\2\u011c")
        buf.write("\u0123\5U+\2\u011d\u011e\5U+\2\u011e\u0120\7\60\2\2\u011f")
        buf.write("\u0121\5U+\2\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0123\3\2\2\2\u0122\u0117\3\2\2\2\u0122\u011d\3\2\2\2")
        buf.write("\u0123Z\3\2\2\2\u0124\u0127\5Y-\2\u0125\u0127\5U+\2\u0126")
        buf.write("\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u012a\t\b\2\2\u0129\u012b\t\7\2\2\u012a\u0129\3")
        buf.write("\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d")
        buf.write("\5U+\2\u012d\\\3\2\2\2\u012e\u0131\5#\22\2\u012f\u0131")
        buf.write("\5%\23\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("^\3\2\2\2\u0132\u0138\7$\2\2\u0133\u0134\7^\2\2\u0134")
        buf.write("\u0137\t\t\2\2\u0135\u0137\n\n\2\2\u0136\u0133\3\2\2\2")
        buf.write("\u0136\u0135\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3")
        buf.write("\2\2\2\u0138\u0139\3\2\2\2\u0139\u013b\3\2\2\2\u013a\u0138")
        buf.write("\3\2\2\2\u013b\u013c\7$\2\2\u013c`\3\2\2\2\u013d\u013e")
        buf.write("\13\2\2\2\u013eb\3\2\2\2\u013f\u0140\13\2\2\2\u0140d\3")
        buf.write("\2\2\2\u0141\u0142\13\2\2\2\u0142f\3\2\2\2\21\2\u0088")
        buf.write("\u0092\u009d\u00a9\u0111\u0115\u0119\u0120\u0122\u0126")
        buf.write("\u012a\u0130\u0136\u0138\3\b\2\2")
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
    STRINGLIT = 47
    ERROR_CHAR = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50

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
            "BOOLLIT", "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "BOOLTYPE", "STRINGTYPE", "FLOATTYPE", "VOIDTYPE", 
                  "WS", "COMMENTS_LINE", "COMMENTS_BLOCK", "ID", "BREAK", 
                  "CONTINUE", "ELSE", "FOR", "IF", "DO", "WHILE", "TRUE", 
                  "FALSE", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                  "MOD_OP", "OR_OP", "AND_OP", "NOT_EQUAL_OP", "EQUAL_OP", 
                  "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", "GREATER_EQUAL_OP", 
                  "ASSIGN_OP", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", 
                  "COMMA", "INTLIT", "FLOATLIT", "FRAC", "EXPONENT", "BOOLLIT", 
                  "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

