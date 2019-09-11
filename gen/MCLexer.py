# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/PPL-Assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0149\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\6\b\u008d\n\b\r")
        buf.write("\b\16\b\u008e\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u0097\n\t\f")
        buf.write("\t\16\t\u009a\13\t\3\t\3\t\3\n\3\n\3\n\3\n\7\n\u00a2\n")
        buf.write("\n\f\n\16\n\u00a5\13\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\7")
        buf.write("\13\u00ae\n\13\f\13\16\13\u00b1\13\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\6,\u0116\n,\r,\16,\u0117")
        buf.write("\3-\3-\5-\u011c\n-\3.\3.\5.\u0120\n.\3.\3.\3.\3.\3.\5")
        buf.write(".\u0127\n.\5.\u0129\n.\3/\3/\5/\u012d\n/\3/\3/\5/\u0131")
        buf.write("\n/\3/\3/\3\60\3\60\5\60\u0137\n\60\3\61\3\61\3\61\3\61")
        buf.write("\7\61\u013d\n\61\f\61\16\61\u0140\13\61\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\u00a3\2\65\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65\3\2\13\5\2\13\f\17\17\"\"\4\2\13")
        buf.write("\f\16\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2--//\4\2")
        buf.write("GGgg\t\2$$^^ddhhppttvv\6\2\n\f\16\17$$^^\2\u0156\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\3i\3\2\2\2\5m\3\2\2\2\7u\3\2\2\2\t|\3\2\2\2\13\u0082")
        buf.write("\3\2\2\2\r\u0087\3\2\2\2\17\u008c\3\2\2\2\21\u0092\3\2")
        buf.write("\2\2\23\u009d\3\2\2\2\25\u00ab\3\2\2\2\27\u00b2\3\2\2")
        buf.write("\2\31\u00b8\3\2\2\2\33\u00c1\3\2\2\2\35\u00c6\3\2\2\2")
        buf.write("\37\u00ca\3\2\2\2!\u00cd\3\2\2\2#\u00d0\3\2\2\2%\u00d6")
        buf.write("\3\2\2\2\'\u00db\3\2\2\2)\u00e1\3\2\2\2+\u00e3\3\2\2\2")
        buf.write("-\u00e5\3\2\2\2/\u00e7\3\2\2\2\61\u00e9\3\2\2\2\63\u00eb")
        buf.write("\3\2\2\2\65\u00ed\3\2\2\2\67\u00ef\3\2\2\29\u00f2\3\2")
        buf.write("\2\2;\u00f5\3\2\2\2=\u00f8\3\2\2\2?\u00fa\3\2\2\2A\u00fc")
        buf.write("\3\2\2\2C\u00ff\3\2\2\2E\u0102\3\2\2\2G\u0104\3\2\2\2")
        buf.write("I\u0106\3\2\2\2K\u0108\3\2\2\2M\u010a\3\2\2\2O\u010c\3")
        buf.write("\2\2\2Q\u010e\3\2\2\2S\u0110\3\2\2\2U\u0112\3\2\2\2W\u0115")
        buf.write("\3\2\2\2Y\u011b\3\2\2\2[\u0128\3\2\2\2]\u012c\3\2\2\2")
        buf.write("_\u0136\3\2\2\2a\u0138\3\2\2\2c\u0143\3\2\2\2e\u0145\3")
        buf.write("\2\2\2g\u0147\3\2\2\2ij\7k\2\2jk\7p\2\2kl\7v\2\2l\4\3")
        buf.write("\2\2\2mn\7d\2\2no\7q\2\2op\7q\2\2pq\7n\2\2qr\7g\2\2rs")
        buf.write("\7c\2\2st\7p\2\2t\6\3\2\2\2uv\7u\2\2vw\7v\2\2wx\7t\2\2")
        buf.write("xy\7k\2\2yz\7p\2\2z{\7i\2\2{\b\3\2\2\2|}\7h\2\2}~\7n\2")
        buf.write("\2~\177\7q\2\2\177\u0080\7c\2\2\u0080\u0081\7v\2\2\u0081")
        buf.write("\n\3\2\2\2\u0082\u0083\7x\2\2\u0083\u0084\7q\2\2\u0084")
        buf.write("\u0085\7k\2\2\u0085\u0086\7f\2\2\u0086\f\3\2\2\2\u0087")
        buf.write("\u0088\7]\2\2\u0088\u0089\5W,\2\u0089\u008a\7_\2\2\u008a")
        buf.write("\16\3\2\2\2\u008b\u008d\t\2\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\u008e\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0091\b\b\2\2\u0091\20\3\2")
        buf.write("\2\2\u0092\u0093\7\61\2\2\u0093\u0094\7\61\2\2\u0094\u0098")
        buf.write("\3\2\2\2\u0095\u0097\n\3\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009b\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\b")
        buf.write("\t\2\2\u009c\22\3\2\2\2\u009d\u009e\7\61\2\2\u009e\u009f")
        buf.write("\7,\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\13\2\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a7\7,\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00aa\b\n\2\2\u00aa\24\3\2\2\2\u00ab\u00af")
        buf.write("\t\4\2\2\u00ac\u00ae\t\5\2\2\u00ad\u00ac\3\2\2\2\u00ae")
        buf.write("\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2")
        buf.write("\u00b0\26\3\2\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3\7d\2")
        buf.write("\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7")
        buf.write("c\2\2\u00b6\u00b7\7m\2\2\u00b7\30\3\2\2\2\u00b8\u00b9")
        buf.write("\7e\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7w\2\2\u00bf\u00c0\7g\2\2\u00c0\32\3\2\2\2\u00c1\u00c2")
        buf.write("\7g\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\34\3\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8")
        buf.write("\7q\2\2\u00c8\u00c9\7t\2\2\u00c9\36\3\2\2\2\u00ca\u00cb")
        buf.write("\7k\2\2\u00cb\u00cc\7h\2\2\u00cc \3\2\2\2\u00cd\u00ce")
        buf.write("\7f\2\2\u00ce\u00cf\7q\2\2\u00cf\"\3\2\2\2\u00d0\u00d1")
        buf.write("\7y\2\2\u00d1\u00d2\7j\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4")
        buf.write("\7n\2\2\u00d4\u00d5\7g\2\2\u00d5$\3\2\2\2\u00d6\u00d7")
        buf.write("\7v\2\2\u00d7\u00d8\7t\2\2\u00d8\u00d9\7w\2\2\u00d9\u00da")
        buf.write("\7g\2\2\u00da&\3\2\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd")
        buf.write("\7c\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0(\3\2\2\2\u00e1\u00e2\7-\2\2\u00e2*\3\2\2")
        buf.write("\2\u00e3\u00e4\7/\2\2\u00e4,\3\2\2\2\u00e5\u00e6\7,\2")
        buf.write("\2\u00e6.\3\2\2\2\u00e7\u00e8\7\61\2\2\u00e8\60\3\2\2")
        buf.write("\2\u00e9\u00ea\7#\2\2\u00ea\62\3\2\2\2\u00eb\u00ec\7\'")
        buf.write("\2\2\u00ec\64\3\2\2\2\u00ed\u00ee\7~\2\2\u00ee\66\3\2")
        buf.write("\2\2\u00ef\u00f0\7(\2\2\u00f0\u00f1\7(\2\2\u00f18\3\2")
        buf.write("\2\2\u00f2\u00f3\7#\2\2\u00f3\u00f4\7?\2\2\u00f4:\3\2")
        buf.write("\2\2\u00f5\u00f6\7?\2\2\u00f6\u00f7\7?\2\2\u00f7<\3\2")
        buf.write("\2\2\u00f8\u00f9\7>\2\2\u00f9>\3\2\2\2\u00fa\u00fb\7@")
        buf.write("\2\2\u00fb@\3\2\2\2\u00fc\u00fd\7>\2\2\u00fd\u00fe\7?")
        buf.write("\2\2\u00feB\3\2\2\2\u00ff\u0100\7@\2\2\u0100\u0101\7?")
        buf.write("\2\2\u0101D\3\2\2\2\u0102\u0103\7?\2\2\u0103F\3\2\2\2")
        buf.write("\u0104\u0105\7]\2\2\u0105H\3\2\2\2\u0106\u0107\7_\2\2")
        buf.write("\u0107J\3\2\2\2\u0108\u0109\7}\2\2\u0109L\3\2\2\2\u010a")
        buf.write("\u010b\7\177\2\2\u010bN\3\2\2\2\u010c\u010d\7*\2\2\u010d")
        buf.write("P\3\2\2\2\u010e\u010f\7+\2\2\u010fR\3\2\2\2\u0110\u0111")
        buf.write("\7=\2\2\u0111T\3\2\2\2\u0112\u0113\7.\2\2\u0113V\3\2\2")
        buf.write("\2\u0114\u0116\t\6\2\2\u0115\u0114\3\2\2\2\u0116\u0117")
        buf.write("\3\2\2\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("X\3\2\2\2\u0119\u011c\5[.\2\u011a\u011c\5]/\2\u011b\u0119")
        buf.write("\3\2\2\2\u011b\u011a\3\2\2\2\u011cZ\3\2\2\2\u011d\u011f")
        buf.write("\t\7\2\2\u011e\u0120\5W,\2\u011f\u011e\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0122\7\60\2\2\u0122")
        buf.write("\u0129\5W,\2\u0123\u0124\5W,\2\u0124\u0126\7\60\2\2\u0125")
        buf.write("\u0127\5W,\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u011d\3\2\2\2\u0128\u0123\3\2\2\2")
        buf.write("\u0129\\\3\2\2\2\u012a\u012d\5[.\2\u012b\u012d\5W,\2\u012c")
        buf.write("\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d\u012e\3\2\2\2")
        buf.write("\u012e\u0130\t\b\2\2\u012f\u0131\t\7\2\2\u0130\u012f\3")
        buf.write("\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133")
        buf.write("\5W,\2\u0133^\3\2\2\2\u0134\u0137\5%\23\2\u0135\u0137")
        buf.write("\5\'\24\2\u0136\u0134\3\2\2\2\u0136\u0135\3\2\2\2\u0137")
        buf.write("`\3\2\2\2\u0138\u013e\7$\2\2\u0139\u013a\7^\2\2\u013a")
        buf.write("\u013d\t\t\2\2\u013b\u013d\n\n\2\2\u013c\u0139\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3")
        buf.write("\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0141\u0142\7$\2\2\u0142b\3\2\2\2\u0143\u0144")
        buf.write("\13\2\2\2\u0144d\3\2\2\2\u0145\u0146\13\2\2\2\u0146f\3")
        buf.write("\2\2\2\u0147\u0148\13\2\2\2\u0148h\3\2\2\2\21\2\u008e")
        buf.write("\u0098\u00a3\u00af\u0117\u011b\u011f\u0126\u0128\u012c")
        buf.write("\u0130\u0136\u013c\u013e\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    BOOLTYPE = 2
    STRINGTYPE = 3
    FLOATTYPE = 4
    VOIDTYPE = 5
    ARRAYTPE = 6
    WS = 7
    COMMENTS_LINE = 8
    COMMENTS_BLOCK = 9
    ID = 10
    BREAK = 11
    CONTINUE = 12
    ELSE = 13
    FOR = 14
    IF = 15
    DO = 16
    WHILE = 17
    TRUE = 18
    FALSE = 19
    ADD_OP = 20
    SUB_OP = 21
    MUL_OP = 22
    DIV_OP = 23
    NOT_OP = 24
    MOD_OP = 25
    OR_OP = 26
    AND_OP = 27
    NOT_EQUAL_OP = 28
    EQUAL_OP = 29
    LESS_OP = 30
    GREATER_OP = 31
    LESS_EQUAL_OP = 32
    GREATER_EQUAL_OP = 33
    ASSIGN_OP = 34
    LSB = 35
    RSB = 36
    LP = 37
    RP = 38
    LB = 39
    RB = 40
    SEMI = 41
    COMMA = 42
    INTLIT = 43
    FLOATLIT = 44
    FRAC = 45
    EXPONENT = 46
    BOOLLIT = 47
    STRINGLIT = 48
    ERROR_CHAR = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51

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
            "ARRAYTPE", "WS", "COMMENTS_LINE", "COMMENTS_BLOCK", "ID", "BREAK", 
            "CONTINUE", "ELSE", "FOR", "IF", "DO", "WHILE", "TRUE", "FALSE", 
            "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", "MOD_OP", 
            "OR_OP", "AND_OP", "NOT_EQUAL_OP", "EQUAL_OP", "LESS_OP", "GREATER_OP", 
            "LESS_EQUAL_OP", "GREATER_EQUAL_OP", "ASSIGN_OP", "LSB", "RSB", 
            "LP", "RP", "LB", "RB", "SEMI", "COMMA", "INTLIT", "FLOATLIT", 
            "FRAC", "EXPONENT", "BOOLLIT", "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "BOOLTYPE", "STRINGTYPE", "FLOATTYPE", "VOIDTYPE", 
                  "ARRAYTPE", "WS", "COMMENTS_LINE", "COMMENTS_BLOCK", "ID", 
                  "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "DO", "WHILE", 
                  "TRUE", "FALSE", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
                  "NOT_OP", "MOD_OP", "OR_OP", "AND_OP", "NOT_EQUAL_OP", 
                  "EQUAL_OP", "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", 
                  "GREATER_EQUAL_OP", "ASSIGN_OP", "LSB", "RSB", "LP", "RP", 
                  "LB", "RB", "SEMI", "COMMA", "INTLIT", "FLOATLIT", "FRAC", 
                  "EXPONENT", "BOOLLIT", "STRINGLIT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


