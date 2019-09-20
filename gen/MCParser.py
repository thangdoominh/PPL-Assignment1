# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/PPL-Assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0136\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\3\2\6\2H\n\2\r\2")
        buf.write("\16\2I\3\2\3\2\3\3\3\3\5\3P\n\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\7\6[\n\6\f\6\16\6^\13\6\3\7\3\7\5\7b\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\5\nn\n\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nx\n\n\f\n\16\n{\13\n")
        buf.write("\5\n}\n\n\3\n\3\n\5\n\u0081\n\n\3\13\3\13\5\13\u0085\n")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\7\f\u008d\n\f\f\f\16\f")
        buf.write("\u0090\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u009c\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00a5")
        buf.write("\n\16\3\17\3\17\6\17\u00a9\n\17\r\17\16\17\u00aa\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\5\25\u00cd")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00d5\n\26\f")
        buf.write("\26\16\26\u00d8\13\26\3\27\3\27\3\27\3\27\3\27\3\27\7")
        buf.write("\27\u00e0\n\27\f\27\16\27\u00e3\13\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u00ea\n\30\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u00f1\n\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u00f9\n")
        buf.write("\32\f\32\16\32\u00fc\13\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\7\33\u0104\n\33\f\33\16\33\u0107\13\33\3\34\3\34\3")
        buf.write("\34\5\34\u010c\n\34\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0114\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u011b\n\36\3")
        buf.write("\37\3\37\5\37\u011f\n\37\3 \3 \3!\3!\3!\5!\u0126\n!\3")
        buf.write("!\3!\3\"\3\"\3\"\7\"\u012d\n\"\f\"\16\"\u0130\13\"\3#")
        buf.write("\3#\5#\u0134\n#\3#\2\6*,\62\64$\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BD\2\t\3\2\3")
        buf.write("\6\3\2\33\34\3\2\35 \3\2\23\24\4\2\25\26\30\30\4\2\24")
        buf.write("\24\27\27\5\2\22\22*+./\2\u0136\2G\3\2\2\2\4O\3\2\2\2")
        buf.write("\6Q\3\2\2\2\bU\3\2\2\2\nW\3\2\2\2\fa\3\2\2\2\16c\3\2\2")
        buf.write("\2\20h\3\2\2\2\22m\3\2\2\2\24\u0084\3\2\2\2\26\u0089\3")
        buf.write("\2\2\2\30\u009b\3\2\2\2\32\u009d\3\2\2\2\34\u00a6\3\2")
        buf.write("\2\2\36\u00b0\3\2\2\2 \u00ba\3\2\2\2\"\u00bd\3\2\2\2$")
        buf.write("\u00c0\3\2\2\2&\u00c4\3\2\2\2(\u00cc\3\2\2\2*\u00ce\3")
        buf.write("\2\2\2,\u00d9\3\2\2\2.\u00e9\3\2\2\2\60\u00f0\3\2\2\2")
        buf.write("\62\u00f2\3\2\2\2\64\u00fd\3\2\2\2\66\u010b\3\2\2\28\u0113")
        buf.write("\3\2\2\2:\u011a\3\2\2\2<\u011e\3\2\2\2>\u0120\3\2\2\2")
        buf.write("@\u0122\3\2\2\2B\u0129\3\2\2\2D\u0133\3\2\2\2FH\5\4\3")
        buf.write("\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2\2JK\3\2\2\2K")
        buf.write("L\7\2\2\3L\3\3\2\2\2MP\5\6\4\2NP\5\22\n\2OM\3\2\2\2ON")
        buf.write("\3\2\2\2P\5\3\2\2\2QR\5\b\5\2RS\5\n\6\2ST\7(\2\2T\7\3")
        buf.write("\2\2\2UV\t\2\2\2V\t\3\2\2\2W\\\5\f\7\2XY\7)\2\2Y[\5\f")
        buf.write("\7\2ZX\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\13\3\2")
        buf.write("\2\2^\\\3\2\2\2_b\5\16\b\2`b\5\20\t\2a_\3\2\2\2a`\3\2")
        buf.write("\2\2b\r\3\2\2\2cd\7\22\2\2de\7\"\2\2ef\7*\2\2fg\7#\2\2")
        buf.write("g\17\3\2\2\2hi\7\22\2\2i\21\3\2\2\2jn\5\b\5\2kn\7\7\2")
        buf.write("\2ln\5\24\13\2mj\3\2\2\2mk\3\2\2\2ml\3\2\2\2no\3\2\2\2")
        buf.write("op\7\22\2\2p|\7&\2\2qr\5\b\5\2ry\5\f\7\2st\7)\2\2tu\5")
        buf.write("\b\5\2uv\5\f\7\2vx\3\2\2\2ws\3\2\2\2x{\3\2\2\2yw\3\2\2")
        buf.write("\2yz\3\2\2\2z}\3\2\2\2{y\3\2\2\2|q\3\2\2\2|}\3\2\2\2}")
        buf.write("~\3\2\2\2~\u0080\7\'\2\2\177\u0081\5\26\f\2\u0080\177")
        buf.write("\3\2\2\2\u0080\u0081\3\2\2\2\u0081\23\3\2\2\2\u0082\u0085")
        buf.write("\5\b\5\2\u0083\u0085\7\7\2\2\u0084\u0082\3\2\2\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\7\"\2\2")
        buf.write("\u0087\u0088\7#\2\2\u0088\25\3\2\2\2\u0089\u008e\7$\2")
        buf.write("\2\u008a\u008d\5\6\4\2\u008b\u008d\5\30\r\2\u008c\u008a")
        buf.write("\3\2\2\2\u008c\u008b\3\2\2\2\u008d\u0090\3\2\2\2\u008e")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0091\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0091\u0092\7%\2\2\u0092\27\3\2\2")
        buf.write("\2\u0093\u009c\5\32\16\2\u0094\u009c\5\34\17\2\u0095\u009c")
        buf.write("\5\36\20\2\u0096\u009c\5 \21\2\u0097\u009c\5\"\22\2\u0098")
        buf.write("\u009c\5$\23\2\u0099\u009c\5&\24\2\u009a\u009c\5\26\f")
        buf.write("\2\u009b\u0093\3\2\2\2\u009b\u0094\3\2\2\2\u009b\u0095")
        buf.write("\3\2\2\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2\u009b")
        buf.write("\u0098\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a\3\2\2\2")
        buf.write("\u009c\31\3\2\2\2\u009d\u009e\7\r\2\2\u009e\u009f\7&\2")
        buf.write("\2\u009f\u00a0\5(\25\2\u00a0\u00a1\7\'\2\2\u00a1\u00a4")
        buf.write("\5\30\r\2\u00a2\u00a3\7\13\2\2\u00a3\u00a5\5\30\r\2\u00a4")
        buf.write("\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\33\3\2\2\2\u00a6")
        buf.write("\u00a8\7\16\2\2\u00a7\u00a9\5\30\r\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a9\u00aa\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\7\17\2\2\u00ad")
        buf.write("\u00ae\5(\25\2\u00ae\u00af\7(\2\2\u00af\35\3\2\2\2\u00b0")
        buf.write("\u00b1\7\f\2\2\u00b1\u00b2\7&\2\2\u00b2\u00b3\5(\25\2")
        buf.write("\u00b3\u00b4\7(\2\2\u00b4\u00b5\5(\25\2\u00b5\u00b6\7")
        buf.write("(\2\2\u00b6\u00b7\5(\25\2\u00b7\u00b8\7\'\2\2\u00b8\u00b9")
        buf.write("\5\30\r\2\u00b9\37\3\2\2\2\u00ba\u00bb\7\b\2\2\u00bb\u00bc")
        buf.write("\7(\2\2\u00bc!\3\2\2\2\u00bd\u00be\7\t\2\2\u00be\u00bf")
        buf.write("\7(\2\2\u00bf#\3\2\2\2\u00c0\u00c1\7\n\2\2\u00c1\u00c2")
        buf.write("\5(\25\2\u00c2\u00c3\7(\2\2\u00c3%\3\2\2\2\u00c4\u00c5")
        buf.write("\5(\25\2\u00c5\u00c6\7(\2\2\u00c6\'\3\2\2\2\u00c7\u00c8")
        buf.write("\5*\26\2\u00c8\u00c9\7!\2\2\u00c9\u00ca\5(\25\2\u00ca")
        buf.write("\u00cd\3\2\2\2\u00cb\u00cd\5*\26\2\u00cc\u00c7\3\2\2\2")
        buf.write("\u00cc\u00cb\3\2\2\2\u00cd)\3\2\2\2\u00ce\u00cf\b\26\1")
        buf.write("\2\u00cf\u00d0\5,\27\2\u00d0\u00d6\3\2\2\2\u00d1\u00d2")
        buf.write("\f\4\2\2\u00d2\u00d3\7\31\2\2\u00d3\u00d5\5,\27\2\u00d4")
        buf.write("\u00d1\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7+\3\2\2\2\u00d8\u00d6\3\2\2")
        buf.write("\2\u00d9\u00da\b\27\1\2\u00da\u00db\5.\30\2\u00db\u00e1")
        buf.write("\3\2\2\2\u00dc\u00dd\f\4\2\2\u00dd\u00de\7\32\2\2\u00de")
        buf.write("\u00e0\5.\30\2\u00df\u00dc\3\2\2\2\u00e0\u00e3\3\2\2\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2-\3\2\2")
        buf.write("\2\u00e3\u00e1\3\2\2\2\u00e4\u00e5\5\60\31\2\u00e5\u00e6")
        buf.write("\t\3\2\2\u00e6\u00e7\5\60\31\2\u00e7\u00ea\3\2\2\2\u00e8")
        buf.write("\u00ea\5\60\31\2\u00e9\u00e4\3\2\2\2\u00e9\u00e8\3\2\2")
        buf.write("\2\u00ea/\3\2\2\2\u00eb\u00ec\5\62\32\2\u00ec\u00ed\t")
        buf.write("\4\2\2\u00ed\u00ee\5\62\32\2\u00ee\u00f1\3\2\2\2\u00ef")
        buf.write("\u00f1\5\62\32\2\u00f0\u00eb\3\2\2\2\u00f0\u00ef\3\2\2")
        buf.write("\2\u00f1\61\3\2\2\2\u00f2\u00f3\b\32\1\2\u00f3\u00f4\5")
        buf.write("\64\33\2\u00f4\u00fa\3\2\2\2\u00f5\u00f6\f\4\2\2\u00f6")
        buf.write("\u00f7\t\5\2\2\u00f7\u00f9\5\64\33\2\u00f8\u00f5\3\2\2")
        buf.write("\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\63\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe")
        buf.write("\b\33\1\2\u00fe\u00ff\5\66\34\2\u00ff\u0105\3\2\2\2\u0100")
        buf.write("\u0101\f\4\2\2\u0101\u0102\t\6\2\2\u0102\u0104\5\66\34")
        buf.write("\2\u0103\u0100\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0105\u0106\3\2\2\2\u0106\65\3\2\2\2\u0107\u0105")
        buf.write("\3\2\2\2\u0108\u0109\t\7\2\2\u0109\u010c\5\66\34\2\u010a")
        buf.write("\u010c\58\35\2\u010b\u0108\3\2\2\2\u010b\u010a\3\2\2\2")
        buf.write("\u010c\67\3\2\2\2\u010d\u010e\5:\36\2\u010e\u010f\7\"")
        buf.write("\2\2\u010f\u0110\5(\25\2\u0110\u0111\7#\2\2\u0111\u0114")
        buf.write("\3\2\2\2\u0112\u0114\5:\36\2\u0113\u010d\3\2\2\2\u0113")
        buf.write("\u0112\3\2\2\2\u01149\3\2\2\2\u0115\u0116\7&\2\2\u0116")
        buf.write("\u0117\5(\25\2\u0117\u0118\7\'\2\2\u0118\u011b\3\2\2\2")
        buf.write("\u0119\u011b\5<\37\2\u011a\u0115\3\2\2\2\u011a\u0119\3")
        buf.write("\2\2\2\u011b;\3\2\2\2\u011c\u011f\5> \2\u011d\u011f\5")
        buf.write("@!\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011f=\3")
        buf.write("\2\2\2\u0120\u0121\t\b\2\2\u0121?\3\2\2\2\u0122\u0123")
        buf.write("\7\22\2\2\u0123\u0125\7&\2\2\u0124\u0126\5B\"\2\u0125")
        buf.write("\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0128\7\'\2\2\u0128A\3\2\2\2\u0129\u012e\5D#\2")
        buf.write("\u012a\u012b\7(\2\2\u012b\u012d\5D#\2\u012c\u012a\3\2")
        buf.write("\2\2\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012f")
        buf.write("\3\2\2\2\u012fC\3\2\2\2\u0130\u012e\3\2\2\2\u0131\u0134")
        buf.write("\5> \2\u0132\u0134\5(\25\2\u0133\u0131\3\2\2\2\u0133\u0132")
        buf.write("\3\2\2\2\u0134E\3\2\2\2\36IO\\amy|\u0080\u0084\u008c\u008e")
        buf.write("\u009b\u00a4\u00aa\u00cc\u00d6\u00e1\u00e9\u00f0\u00fa")
        buf.write("\u0105\u010b\u0113\u011a\u011e\u0125\u012e\u0133")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'boolean'", "'string'", "'float'", 
                     "'void'", "'break'", "'continue'", "'return'", "'else'", 
                     "'for'", "'if'", "'do'", "'while'", "'true'", "'false'", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'!'", "'%'", 
                     "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", "'<='", 
                     "'>='", "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", 
                     "';'", "','" ]

    symbolicNames = [ "<INVALID>", "INTTYPE", "BOOLTYPE", "STRINGTYPE", 
                      "FLOATTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "RETURN", 
                      "ELSE", "FOR", "IF", "DO", "WHILE", "TRUE", "FALSE", 
                      "ID", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                      "MOD_OP", "OR_OP", "AND_OP", "NOT_EQUAL_OP", "EQUAL_OP", 
                      "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", "GREATER_EQUAL_OP", 
                      "ASSIGN_OP", "LSB", "RSB", "LP", "RP", "LB", "RB", 
                      "SEMI", "COMMA", "INTLIT", "FLOATLIT", "FRAC", "EXPONENT", 
                      "BOOLLIT", "STRINGLIT", "COMMENTS_LINE", "COMMENTS_BLOCK", 
                      "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_vardeclaration = 2
    RULE_singletype = 3
    RULE_idlist = 4
    RULE_idtail = 5
    RULE_idarray = 6
    RULE_idsingle = 7
    RULE_funcdeclaration = 8
    RULE_arraypointertype = 9
    RULE_block = 10
    RULE_statement = 11
    RULE_ifstmt = 12
    RULE_dowhilestmt = 13
    RULE_forstmt = 14
    RULE_breakstmt = 15
    RULE_continuestmt = 16
    RULE_returnstmt = 17
    RULE_expressionstmt = 18
    RULE_expression = 19
    RULE_exp1 = 20
    RULE_exp2 = 21
    RULE_exp3 = 22
    RULE_exp4 = 23
    RULE_exp5 = 24
    RULE_exp6 = 25
    RULE_exp7 = 26
    RULE_exp8 = 27
    RULE_exp9 = 28
    RULE_exp10 = 29
    RULE_operand = 30
    RULE_funccall = 31
    RULE_paralist_call = 32
    RULE_para_call = 33

    ruleNames =  [ "program", "declaration", "vardeclaration", "singletype", 
                   "idlist", "idtail", "idarray", "idsingle", "funcdeclaration", 
                   "arraypointertype", "block", "statement", "ifstmt", "dowhilestmt", 
                   "forstmt", "breakstmt", "continuestmt", "returnstmt", 
                   "expressionstmt", "expression", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "exp7", "exp8", "exp9", "exp10", 
                   "operand", "funccall", "paralist_call", "para_call" ]

    EOF = Token.EOF
    INTTYPE=1
    BOOLTYPE=2
    STRINGTYPE=3
    FLOATTYPE=4
    VOIDTYPE=5
    BREAK=6
    CONTINUE=7
    RETURN=8
    ELSE=9
    FOR=10
    IF=11
    DO=12
    WHILE=13
    TRUE=14
    FALSE=15
    ID=16
    ADD_OP=17
    SUB_OP=18
    MUL_OP=19
    DIV_OP=20
    NOT_OP=21
    MOD_OP=22
    OR_OP=23
    AND_OP=24
    NOT_EQUAL_OP=25
    EQUAL_OP=26
    LESS_OP=27
    GREATER_OP=28
    LESS_EQUAL_OP=29
    GREATER_EQUAL_OP=30
    ASSIGN_OP=31
    LSB=32
    RSB=33
    LP=34
    RP=35
    LB=36
    RB=37
    SEMI=38
    COMMA=39
    INTLIT=40
    FLOATLIT=41
    FRAC=42
    EXPONENT=43
    BOOLLIT=44
    STRINGLIT=45
    COMMENTS_LINE=46
    COMMENTS_BLOCK=47
    WS=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

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

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                self.declaration()
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

            self.state = 73
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MCParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.vardeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardeclaration" ):
                listener.enterVardeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardeclaration" ):
                listener.exitVardeclaration(self)

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
            self.state = 79
            self.singletype()
            self.state = 80
            self.idlist()
            self.state = 81
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingletype" ):
                listener.enterSingletype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingletype" ):
                listener.exitSingletype(self)

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
            self.state = 83
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdlist" ):
                listener.enterIdlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdlist" ):
                listener.exitIdlist(self)

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
            self.state = 85
            self.idtail()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 86
                self.match(MCParser.COMMA)
                self.state = 87
                self.idtail()
                self.state = 92
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdtail" ):
                listener.enterIdtail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdtail" ):
                listener.exitIdtail(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdtail" ):
                return visitor.visitIdtail(self)
            else:
                return visitor.visitChildren(self)




    def idtail(self):

        localctx = MCParser.IdtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_idtail)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.idarray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdarray" ):
                listener.enterIdarray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdarray" ):
                listener.exitIdarray(self)

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
            self.state = 97
            self.match(MCParser.ID)
            self.state = 98
            self.match(MCParser.LSB)
            self.state = 99
            self.match(MCParser.INTLIT)
            self.state = 100
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdsingle" ):
                listener.enterIdsingle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdsingle" ):
                listener.exitIdsingle(self)

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
            self.state = 102
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


        def block(self):
            return self.getTypedRuleContext(MCParser.BlockContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.COMMA)
            else:
                return self.getToken(MCParser.COMMA, i)

        def getRuleIndex(self):
            return MCParser.RULE_funcdeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdeclaration" ):
                listener.enterFuncdeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdeclaration" ):
                listener.exitFuncdeclaration(self)

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
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 104
                self.singletype()
                pass

            elif la_ == 2:
                self.state = 105
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.state = 106
                self.arraypointertype()
                pass


            self.state = 109
            self.match(MCParser.ID)
            self.state = 110
            self.match(MCParser.LB)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE))) != 0):
                self.state = 111
                self.singletype()
                self.state = 112
                self.idtail()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 113
                    self.match(MCParser.COMMA)
                    self.state = 114
                    self.singletype()
                    self.state = 115
                    self.idtail()
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 124
            self.match(MCParser.RB)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LP:
                self.state = 125
                self.block()


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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArraypointertype" ):
                listener.enterArraypointertype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArraypointertype" ):
                listener.exitArraypointertype(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraypointertype" ):
                return visitor.visitArraypointertype(self)
            else:
                return visitor.visitChildren(self)




    def arraypointertype(self):

        localctx = MCParser.ArraypointertypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arraypointertype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INTTYPE, MCParser.BOOLTYPE, MCParser.STRINGTYPE, MCParser.FLOATTYPE]:
                self.state = 128
                self.singletype()
                pass
            elif token in [MCParser.VOIDTYPE]:
                self.state = 129
                self.match(MCParser.VOIDTYPE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 132
            self.match(MCParser.LSB)
            self.state = 133
            self.match(MCParser.RSB)
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

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def vardeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VardeclarationContext)
            else:
                return self.getTypedRuleContext(MCParser.VardeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block

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

        localctx = MCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(MCParser.LP)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.ID) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LP) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 138
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MCParser.INTTYPE, MCParser.BOOLTYPE, MCParser.STRINGTYPE, MCParser.FLOATTYPE]:
                    self.state = 136
                    self.vardeclaration()
                    pass
                elif token in [MCParser.BREAK, MCParser.CONTINUE, MCParser.RETURN, MCParser.FOR, MCParser.IF, MCParser.DO, MCParser.ID, MCParser.SUB_OP, MCParser.NOT_OP, MCParser.LP, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT]:
                    self.state = 137
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifstmt(self):
            return self.getTypedRuleContext(MCParser.IfstmtContext,0)


        def dowhilestmt(self):
            return self.getTypedRuleContext(MCParser.DowhilestmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MCParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MCParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MCParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MCParser.ReturnstmtContext,0)


        def expressionstmt(self):
            return self.getTypedRuleContext(MCParser.ExpressionstmtContext,0)


        def block(self):
            return self.getTypedRuleContext(MCParser.BlockContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_statement

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

        localctx = MCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.ifstmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.dowhilestmt()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.forstmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.breakstmt()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.continuestmt()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.returnstmt()
                pass
            elif token in [MCParser.ID, MCParser.SUB_OP, MCParser.NOT_OP, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 151
                self.expressionstmt()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 152
                self.block()
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


    class IfstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_ifstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfstmt" ):
                listener.enterIfstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfstmt" ):
                listener.exitIfstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MCParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(MCParser.IF)
            self.state = 156
            self.match(MCParser.LB)
            self.state = 157
            self.expression()
            self.state = 158
            self.match(MCParser.RB)
            self.state = 159
            self.statement()
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 160
                self.match(MCParser.ELSE)
                self.state = 161
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_dowhilestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDowhilestmt" ):
                listener.enterDowhilestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDowhilestmt" ):
                listener.exitDowhilestmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhilestmt" ):
                return visitor.visitDowhilestmt(self)
            else:
                return visitor.visitChildren(self)




    def dowhilestmt(self):

        localctx = MCParser.DowhilestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dowhilestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MCParser.DO)
            self.state = 166 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 165
                self.statement()
                self.state = 168 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.ID) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LP) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

            self.state = 170
            self.match(MCParser.WHILE)
            self.state = 171
            self.expression()
            self.state = 172
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MCParser.ExpressionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def statement(self):
            return self.getTypedRuleContext(MCParser.StatementContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_forstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForstmt" ):
                listener.enterForstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForstmt" ):
                listener.exitForstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MCParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MCParser.FOR)
            self.state = 175
            self.match(MCParser.LB)
            self.state = 176
            self.expression()
            self.state = 177
            self.match(MCParser.SEMI)
            self.state = 178
            self.expression()
            self.state = 179
            self.match(MCParser.SEMI)
            self.state = 180
            self.expression()
            self.state = 181
            self.match(MCParser.RB)
            self.state = 182
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_breakstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakstmt" ):
                listener.enterBreakstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakstmt" ):
                listener.exitBreakstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MCParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MCParser.BREAK)
            self.state = 185
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_continuestmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinuestmt" ):
                listener.enterContinuestmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinuestmt" ):
                listener.exitContinuestmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MCParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MCParser.CONTINUE)
            self.state = 188
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_returnstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnstmt" ):
                listener.enterReturnstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnstmt" ):
                listener.exitReturnstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MCParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(MCParser.RETURN)
            self.state = 191
            self.expression()
            self.state = 192
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionstmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expressionstmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionstmt" ):
                listener.enterExpressionstmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionstmt" ):
                listener.exitExpressionstmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionstmt" ):
                return visitor.visitExpressionstmt(self)
            else:
                return visitor.visitChildren(self)




    def expressionstmt(self):

        localctx = MCParser.ExpressionstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expressionstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expression()
            self.state = 195
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def ASSIGN_OP(self):
            return self.getToken(MCParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expression

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




    def expression(self):

        localctx = MCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.exp1(0)
                self.state = 198
                self.match(MCParser.ASSIGN_OP)
                self.state = 199
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(MCParser.Exp1Context,0)


        def OR_OP(self):
            return self.getToken(MCParser.OR_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp1" ):
                listener.enterExp1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp1" ):
                listener.exitExp1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 212
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 207
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 208
                    self.match(MCParser.OR_OP)
                    self.state = 209
                    self.exp2(0) 
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(MCParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(MCParser.Exp2Context,0)


        def AND_OP(self):
            return self.getToken(MCParser.AND_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp2" ):
                listener.enterExp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp2" ):
                listener.exitExp2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 223
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 218
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 219
                    self.match(MCParser.AND_OP)
                    self.state = 220
                    self.exp3() 
                self.state = 225
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp4Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp4Context,i)


        def EQUAL_OP(self):
            return self.getToken(MCParser.EQUAL_OP, 0)

        def NOT_EQUAL_OP(self):
            return self.getToken(MCParser.NOT_EQUAL_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp3" ):
                listener.enterExp3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp3" ):
                listener.exitExp3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = MCParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.exp4()
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT_EQUAL_OP or _la==MCParser.EQUAL_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.exp4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Exp5Context)
            else:
                return self.getTypedRuleContext(MCParser.Exp5Context,i)


        def LESS_OP(self):
            return self.getToken(MCParser.LESS_OP, 0)

        def LESS_EQUAL_OP(self):
            return self.getToken(MCParser.LESS_EQUAL_OP, 0)

        def GREATER_OP(self):
            return self.getToken(MCParser.GREATER_OP, 0)

        def GREATER_EQUAL_OP(self):
            return self.getToken(MCParser.GREATER_EQUAL_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp4" ):
                listener.enterExp4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp4" ):
                listener.exitExp4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = MCParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.exp5(0)
                self.state = 234
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS_OP) | (1 << MCParser.GREATER_OP) | (1 << MCParser.LESS_EQUAL_OP) | (1 << MCParser.GREATER_EQUAL_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 235
                self.exp5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.exp5(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def exp5(self):
            return self.getTypedRuleContext(MCParser.Exp5Context,0)


        def ADD_OP(self):
            return self.getToken(MCParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(MCParser.SUB_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp5" ):
                listener.enterExp5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp5" ):
                listener.exitExp5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)



    def exp5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 243
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 244
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD_OP or _la==MCParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 245
                    self.exp6(0) 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(MCParser.Exp6Context,0)


        def DIV_OP(self):
            return self.getToken(MCParser.DIV_OP, 0)

        def MUL_OP(self):
            return self.getToken(MCParser.MUL_OP, 0)

        def MOD_OP(self):
            return self.getToken(MCParser.MOD_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp6" ):
                listener.enterExp6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp6" ):
                listener.exitExp6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 254
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 255
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL_OP) | (1 << MCParser.DIV_OP) | (1 << MCParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 256
                    self.exp7() 
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(MCParser.Exp7Context,0)


        def SUB_OP(self):
            return self.getToken(MCParser.SUB_OP, 0)

        def NOT_OP(self):
            return self.getToken(MCParser.NOT_OP, 0)

        def exp8(self):
            return self.getTypedRuleContext(MCParser.Exp8Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp7" ):
                listener.enterExp7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp7" ):
                listener.exitExp7(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = MCParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUB_OP, MCParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB_OP or _la==MCParser.NOT_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.exp7()
                pass
            elif token in [MCParser.ID, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.exp8()
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


    class Exp8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp9(self):
            return self.getTypedRuleContext(MCParser.Exp9Context,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_exp8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp8" ):
                listener.enterExp8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp8" ):
                listener.exitExp8(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = MCParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp8)
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.exp9()
                self.state = 268
                self.match(MCParser.LSB)
                self.state = 269
                self.expression()
                self.state = 270
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.exp9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def exp10(self):
            return self.getTypedRuleContext(MCParser.Exp10Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp9

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp9" ):
                listener.enterExp9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp9" ):
                listener.exitExp9(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp9" ):
                return visitor.visitExp9(self)
            else:
                return visitor.visitChildren(self)




    def exp9(self):

        localctx = MCParser.Exp9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp9)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(MCParser.LB)
                self.state = 276
                self.expression()
                self.state = 277
                self.match(MCParser.RB)
                pass
            elif token in [MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.exp10()
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


    class Exp10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MCParser.OperandContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MCParser.FunccallContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_exp10

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp10" ):
                listener.enterExp10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp10" ):
                listener.exitExp10(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp10" ):
                return visitor.visitExp10(self)
            else:
                return visitor.visitChildren(self)




    def exp10(self):

        localctx = MCParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp10)
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.funccall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MCParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.ID) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0)):
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


    class FunccallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def paralist_call(self):
            return self.getTypedRuleContext(MCParser.Paralist_callContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funccall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunccall" ):
                listener.enterFunccall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunccall" ):
                listener.exitFunccall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MCParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(MCParser.ID)
            self.state = 289
            self.match(MCParser.LB)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.ID) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 290
                self.paralist_call()


            self.state = 293
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Paralist_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Para_callContext)
            else:
                return self.getTypedRuleContext(MCParser.Para_callContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def getRuleIndex(self):
            return MCParser.RULE_paralist_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParalist_call" ):
                listener.enterParalist_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParalist_call" ):
                listener.exitParalist_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist_call" ):
                return visitor.visitParalist_call(self)
            else:
                return visitor.visitChildren(self)




    def paralist_call(self):

        localctx = MCParser.Paralist_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_paralist_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.para_call()
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.SEMI:
                self.state = 296
                self.match(MCParser.SEMI)
                self.state = 297
                self.para_call()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MCParser.OperandContext,0)


        def expression(self):
            return self.getTypedRuleContext(MCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_para_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara_call" ):
                listener.enterPara_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara_call" ):
                listener.exitPara_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara_call" ):
                return visitor.visitPara_call(self)
            else:
                return visitor.visitChildren(self)




    def para_call(self):

        localctx = MCParser.Para_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_para_call)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.expression()
                pass


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
        self._predicates[20] = self.exp1_sempred
        self._predicates[21] = self.exp2_sempred
        self._predicates[24] = self.exp5_sempred
        self._predicates[25] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp5_sempred(self, localctx:Exp5Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




