# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/PPL-Assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0140\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\3\2\6\2J\n")
        buf.write("\2\r\2\16\2K\3\2\3\2\3\3\3\3\5\3R\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\7\6]\n\6\f\6\16\6`\13\6\3\7\3\7\5")
        buf.write("\7d\n\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\5\np\n")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\nz\n\n\f\n\16\n}")
        buf.write("\13\n\5\n\177\n\n\3\n\3\n\5\n\u0083\n\n\3\13\3\13\5\13")
        buf.write("\u0087\n\13\3\13\3\13\3\13\3\f\3\f\7\f\u008e\n\f\f\f\16")
        buf.write("\f\u0091\13\f\3\f\5\f\u0094\n\f\3\f\3\f\3\r\6\r\u0099")
        buf.write("\n\r\r\r\16\r\u009a\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00a5\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u00ae\n\17\3\20\3\20\7\20\u00b2\n\20\f\20\16")
        buf.write("\20\u00b5\13\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00d7\n\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\7\27\u00df\n\27\f\27\16\27\u00e2\13\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\7\30\u00ea\n\30\f\30\16\30\u00ed\13")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\5\31\u00f4\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u00fb\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\7\33\u0103\n\33\f\33\16\33\u0106\13\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\7\34\u010e\n\34\f\34\16\34\u0111")
        buf.write("\13\34\3\35\3\35\3\35\5\35\u0116\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u011e\n\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u0125\n\37\3 \3 \5 \u0129\n \3!\3!\3\"\3\"\3\"\5")
        buf.write("\"\u0130\n\"\3\"\3\"\3#\3#\3#\7#\u0137\n#\f#\16#\u013a")
        buf.write("\13#\3$\3$\5$\u013e\n$\3$\2\6,.\64\66%\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("\2\t\3\2\3\6\3\2\33\34\3\2\35 \3\2\23\24\4\2\25\26\30")
        buf.write("\30\4\2\24\24\27\27\5\2\22\22*+./\2\u0140\2I\3\2\2\2\4")
        buf.write("Q\3\2\2\2\6S\3\2\2\2\bW\3\2\2\2\nY\3\2\2\2\fc\3\2\2\2")
        buf.write("\16e\3\2\2\2\20j\3\2\2\2\22o\3\2\2\2\24\u0086\3\2\2\2")
        buf.write("\26\u008b\3\2\2\2\30\u0098\3\2\2\2\32\u00a4\3\2\2\2\34")
        buf.write("\u00a6\3\2\2\2\36\u00af\3\2\2\2 \u00ba\3\2\2\2\"\u00c4")
        buf.write("\3\2\2\2$\u00c7\3\2\2\2&\u00ca\3\2\2\2(\u00ce\3\2\2\2")
        buf.write("*\u00d6\3\2\2\2,\u00d8\3\2\2\2.\u00e3\3\2\2\2\60\u00f3")
        buf.write("\3\2\2\2\62\u00fa\3\2\2\2\64\u00fc\3\2\2\2\66\u0107\3")
        buf.write("\2\2\28\u0115\3\2\2\2:\u011d\3\2\2\2<\u0124\3\2\2\2>\u0128")
        buf.write("\3\2\2\2@\u012a\3\2\2\2B\u012c\3\2\2\2D\u0133\3\2\2\2")
        buf.write("F\u013d\3\2\2\2HJ\5\4\3\2IH\3\2\2\2JK\3\2\2\2KI\3\2\2")
        buf.write("\2KL\3\2\2\2LM\3\2\2\2MN\7\2\2\3N\3\3\2\2\2OR\5\6\4\2")
        buf.write("PR\5\22\n\2QO\3\2\2\2QP\3\2\2\2R\5\3\2\2\2ST\5\b\5\2T")
        buf.write("U\5\n\6\2UV\7(\2\2V\7\3\2\2\2WX\t\2\2\2X\t\3\2\2\2Y^\5")
        buf.write("\f\7\2Z[\7)\2\2[]\5\f\7\2\\Z\3\2\2\2]`\3\2\2\2^\\\3\2")
        buf.write("\2\2^_\3\2\2\2_\13\3\2\2\2`^\3\2\2\2ad\5\16\b\2bd\5\20")
        buf.write("\t\2ca\3\2\2\2cb\3\2\2\2d\r\3\2\2\2ef\7\22\2\2fg\7\"\2")
        buf.write("\2gh\7*\2\2hi\7#\2\2i\17\3\2\2\2jk\7\22\2\2k\21\3\2\2")
        buf.write("\2lp\5\b\5\2mp\7\7\2\2np\5\24\13\2ol\3\2\2\2om\3\2\2\2")
        buf.write("on\3\2\2\2pq\3\2\2\2qr\7\22\2\2r~\7&\2\2st\5\b\5\2t{\5")
        buf.write("\f\7\2uv\7)\2\2vw\5\b\5\2wx\5\f\7\2xz\3\2\2\2yu\3\2\2")
        buf.write("\2z}\3\2\2\2{y\3\2\2\2{|\3\2\2\2|\177\3\2\2\2}{\3\2\2")
        buf.write("\2~s\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0082")
        buf.write("\7\'\2\2\u0081\u0083\5\26\f\2\u0082\u0081\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\23\3\2\2\2\u0084\u0087\5\b\5\2\u0085")
        buf.write("\u0087\7\7\2\2\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\7\"\2\2\u0089\u008a\7")
        buf.write("#\2\2\u008a\25\3\2\2\2\u008b\u008f\7$\2\2\u008c\u008e")
        buf.write("\5\6\4\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0093\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0092\u0094\5\30\r\2\u0093\u0092")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u0096\7%\2\2\u0096\27\3\2\2\2\u0097\u0099\5\32\16\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u0098\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\31\3\2\2\2\u009c\u00a5\5\34")
        buf.write("\17\2\u009d\u00a5\5\36\20\2\u009e\u00a5\5 \21\2\u009f")
        buf.write("\u00a5\5\"\22\2\u00a0\u00a5\5$\23\2\u00a1\u00a5\5&\24")
        buf.write("\2\u00a2\u00a5\5(\25\2\u00a3\u00a5\5\26\f\2\u00a4\u009c")
        buf.write("\3\2\2\2\u00a4\u009d\3\2\2\2\u00a4\u009e\3\2\2\2\u00a4")
        buf.write("\u009f\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a4\u00a1\3\2\2\2")
        buf.write("\u00a4\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\33\3\2")
        buf.write("\2\2\u00a6\u00a7\7\r\2\2\u00a7\u00a8\7&\2\2\u00a8\u00a9")
        buf.write("\5*\26\2\u00a9\u00aa\7\'\2\2\u00aa\u00ad\5\32\16\2\u00ab")
        buf.write("\u00ac\7\13\2\2\u00ac\u00ae\5\32\16\2\u00ad\u00ab\3\2")
        buf.write("\2\2\u00ad\u00ae\3\2\2\2\u00ae\35\3\2\2\2\u00af\u00b3")
        buf.write("\7\16\2\2\u00b0\u00b2\5\32\16\2\u00b1\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7\7")
        buf.write("\17\2\2\u00b7\u00b8\5*\26\2\u00b8\u00b9\7(\2\2\u00b9\37")
        buf.write("\3\2\2\2\u00ba\u00bb\7\f\2\2\u00bb\u00bc\7&\2\2\u00bc")
        buf.write("\u00bd\5*\26\2\u00bd\u00be\7(\2\2\u00be\u00bf\5*\26\2")
        buf.write("\u00bf\u00c0\7(\2\2\u00c0\u00c1\5*\26\2\u00c1\u00c2\7")
        buf.write("\'\2\2\u00c2\u00c3\5\32\16\2\u00c3!\3\2\2\2\u00c4\u00c5")
        buf.write("\7\b\2\2\u00c5\u00c6\7(\2\2\u00c6#\3\2\2\2\u00c7\u00c8")
        buf.write("\7\t\2\2\u00c8\u00c9\7(\2\2\u00c9%\3\2\2\2\u00ca\u00cb")
        buf.write("\7\n\2\2\u00cb\u00cc\5*\26\2\u00cc\u00cd\7(\2\2\u00cd")
        buf.write("\'\3\2\2\2\u00ce\u00cf\5*\26\2\u00cf\u00d0\7(\2\2\u00d0")
        buf.write(")\3\2\2\2\u00d1\u00d2\5,\27\2\u00d2\u00d3\7!\2\2\u00d3")
        buf.write("\u00d4\5*\26\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5,\27\2")
        buf.write("\u00d6\u00d1\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7+\3\2\2")
        buf.write("\2\u00d8\u00d9\b\27\1\2\u00d9\u00da\5.\30\2\u00da\u00e0")
        buf.write("\3\2\2\2\u00db\u00dc\f\4\2\2\u00dc\u00dd\7\31\2\2\u00dd")
        buf.write("\u00df\5.\30\2\u00de\u00db\3\2\2\2\u00df\u00e2\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1-\3\2\2")
        buf.write("\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\b\30\1\2\u00e4\u00e5")
        buf.write("\5\60\31\2\u00e5\u00eb\3\2\2\2\u00e6\u00e7\f\4\2\2\u00e7")
        buf.write("\u00e8\7\32\2\2\u00e8\u00ea\5\60\31\2\u00e9\u00e6\3\2")
        buf.write("\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec")
        buf.write("\3\2\2\2\u00ec/\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef")
        buf.write("\5\62\32\2\u00ef\u00f0\t\3\2\2\u00f0\u00f1\5\62\32\2\u00f1")
        buf.write("\u00f4\3\2\2\2\u00f2\u00f4\5\62\32\2\u00f3\u00ee\3\2\2")
        buf.write("\2\u00f3\u00f2\3\2\2\2\u00f4\61\3\2\2\2\u00f5\u00f6\5")
        buf.write("\64\33\2\u00f6\u00f7\t\4\2\2\u00f7\u00f8\5\64\33\2\u00f8")
        buf.write("\u00fb\3\2\2\2\u00f9\u00fb\5\64\33\2\u00fa\u00f5\3\2\2")
        buf.write("\2\u00fa\u00f9\3\2\2\2\u00fb\63\3\2\2\2\u00fc\u00fd\b")
        buf.write("\33\1\2\u00fd\u00fe\5\66\34\2\u00fe\u0104\3\2\2\2\u00ff")
        buf.write("\u0100\f\4\2\2\u0100\u0101\t\5\2\2\u0101\u0103\5\66\34")
        buf.write("\2\u0102\u00ff\3\2\2\2\u0103\u0106\3\2\2\2\u0104\u0102")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105\65\3\2\2\2\u0106\u0104")
        buf.write("\3\2\2\2\u0107\u0108\b\34\1\2\u0108\u0109\58\35\2\u0109")
        buf.write("\u010f\3\2\2\2\u010a\u010b\f\4\2\2\u010b\u010c\t\6\2\2")
        buf.write("\u010c\u010e\58\35\2\u010d\u010a\3\2\2\2\u010e\u0111\3")
        buf.write("\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\67")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\t\7\2\2\u0113")
        buf.write("\u0116\58\35\2\u0114\u0116\5:\36\2\u0115\u0112\3\2\2\2")
        buf.write("\u0115\u0114\3\2\2\2\u01169\3\2\2\2\u0117\u0118\5<\37")
        buf.write("\2\u0118\u0119\7\"\2\2\u0119\u011a\5*\26\2\u011a\u011b")
        buf.write("\7#\2\2\u011b\u011e\3\2\2\2\u011c\u011e\5<\37\2\u011d")
        buf.write("\u0117\3\2\2\2\u011d\u011c\3\2\2\2\u011e;\3\2\2\2\u011f")
        buf.write("\u0120\7&\2\2\u0120\u0121\5*\26\2\u0121\u0122\7\'\2\2")
        buf.write("\u0122\u0125\3\2\2\2\u0123\u0125\5> \2\u0124\u011f\3\2")
        buf.write("\2\2\u0124\u0123\3\2\2\2\u0125=\3\2\2\2\u0126\u0129\5")
        buf.write("@!\2\u0127\u0129\5B\"\2\u0128\u0126\3\2\2\2\u0128\u0127")
        buf.write("\3\2\2\2\u0129?\3\2\2\2\u012a\u012b\t\b\2\2\u012bA\3\2")
        buf.write("\2\2\u012c\u012d\7\22\2\2\u012d\u012f\7&\2\2\u012e\u0130")
        buf.write("\5D#\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131")
        buf.write("\3\2\2\2\u0131\u0132\7\'\2\2\u0132C\3\2\2\2\u0133\u0138")
        buf.write("\5F$\2\u0134\u0135\7(\2\2\u0135\u0137\5F$\2\u0136\u0134")
        buf.write("\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0138")
        buf.write("\u0139\3\2\2\2\u0139E\3\2\2\2\u013a\u0138\3\2\2\2\u013b")
        buf.write("\u013e\5@!\2\u013c\u013e\5*\26\2\u013d\u013b\3\2\2\2\u013d")
        buf.write("\u013c\3\2\2\2\u013eG\3\2\2\2\37KQ^co{~\u0082\u0086\u008f")
        buf.write("\u0093\u009a\u00a4\u00ad\u00b3\u00d6\u00e0\u00eb\u00f3")
        buf.write("\u00fa\u0104\u010f\u0115\u011d\u0124\u0128\u012f\u0138")
        buf.write("\u013d")
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
    RULE_statementpart = 11
    RULE_statement = 12
    RULE_ifstmt = 13
    RULE_dowhilestmt = 14
    RULE_forstmt = 15
    RULE_breakstmt = 16
    RULE_continuestmt = 17
    RULE_returnstmt = 18
    RULE_expressionstmt = 19
    RULE_expression = 20
    RULE_exp1 = 21
    RULE_exp2 = 22
    RULE_exp3 = 23
    RULE_exp4 = 24
    RULE_exp5 = 25
    RULE_exp6 = 26
    RULE_exp7 = 27
    RULE_exp8 = 28
    RULE_exp9 = 29
    RULE_exp10 = 30
    RULE_operand = 31
    RULE_funccall = 32
    RULE_paralist_call = 33
    RULE_para_call = 34

    ruleNames =  [ "program", "declaration", "vardeclaration", "singletype", 
                   "idlist", "idtail", "idarray", "idsingle", "funcdeclaration", 
                   "arraypointertype", "block", "statementpart", "statement", 
                   "ifstmt", "dowhilestmt", "forstmt", "breakstmt", "continuestmt", 
                   "returnstmt", "expressionstmt", "expression", "exp1", 
                   "exp2", "exp3", "exp4", "exp5", "exp6", "exp7", "exp8", 
                   "exp9", "exp10", "operand", "funccall", "paralist_call", 
                   "para_call" ]

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
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 70
                self.declaration()
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.VOIDTYPE))) != 0)):
                    break

            self.state = 75
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
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.vardeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
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
            self.state = 81
            self.singletype()
            self.state = 82
            self.idlist()
            self.state = 83
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
            self.state = 85
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
            self.state = 87
            self.idtail()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.COMMA:
                self.state = 88
                self.match(MCParser.COMMA)
                self.state = 89
                self.idtail()
                self.state = 94
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
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.idarray()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
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
            self.state = 99
            self.match(MCParser.ID)
            self.state = 100
            self.match(MCParser.LSB)
            self.state = 101
            self.match(MCParser.INTLIT)
            self.state = 102
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
            self.state = 104
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
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 106
                self.singletype()
                pass

            elif la_ == 2:
                self.state = 107
                self.match(MCParser.VOIDTYPE)
                pass

            elif la_ == 3:
                self.state = 108
                self.arraypointertype()
                pass


            self.state = 111
            self.match(MCParser.ID)
            self.state = 112
            self.match(MCParser.LB)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE))) != 0):
                self.state = 113
                self.singletype()
                self.state = 114
                self.idtail()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.COMMA:
                    self.state = 115
                    self.match(MCParser.COMMA)
                    self.state = 116
                    self.singletype()
                    self.state = 117
                    self.idtail()
                    self.state = 123
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 126
            self.match(MCParser.RB)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LP:
                self.state = 127
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
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.INTTYPE, MCParser.BOOLTYPE, MCParser.STRINGTYPE, MCParser.FLOATTYPE]:
                self.state = 130
                self.singletype()
                pass
            elif token in [MCParser.VOIDTYPE]:
                self.state = 131
                self.match(MCParser.VOIDTYPE)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 134
            self.match(MCParser.LSB)
            self.state = 135
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


        def statementpart(self):
            return self.getTypedRuleContext(MCParser.StatementpartContext,0)


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
            self.state = 137
            self.match(MCParser.LP)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.BOOLTYPE) | (1 << MCParser.STRINGTYPE) | (1 << MCParser.FLOATTYPE))) != 0):
                self.state = 138
                self.vardeclaration()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.ID) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LP) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 144
                self.statementpart()


            self.state = 147
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementpartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MCParser.StatementContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_statementpart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementpart" ):
                listener.enterStatementpart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementpart" ):
                listener.exitStatementpart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementpart" ):
                return visitor.visitStatementpart(self)
            else:
                return visitor.visitChildren(self)




    def statementpart(self):

        localctx = MCParser.StatementpartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statementpart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 149
                self.statement()
                self.state = 152 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.ID) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LP) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0)):
                    break

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
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.ifstmt()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.dowhilestmt()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.forstmt()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.breakstmt()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 158
                self.continuestmt()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 159
                self.returnstmt()
                pass
            elif token in [MCParser.ID, MCParser.SUB_OP, MCParser.NOT_OP, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 7)
                self.state = 160
                self.expressionstmt()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 161
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
        self.enterRule(localctx, 26, self.RULE_ifstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(MCParser.IF)
            self.state = 165
            self.match(MCParser.LB)
            self.state = 166
            self.expression()
            self.state = 167
            self.match(MCParser.RB)
            self.state = 168
            self.statement()
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 169
                self.match(MCParser.ELSE)
                self.state = 170
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
        self.enterRule(localctx, 28, self.RULE_dowhilestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MCParser.DO)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.RETURN) | (1 << MCParser.FOR) | (1 << MCParser.IF) | (1 << MCParser.DO) | (1 << MCParser.ID) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LP) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 174
                self.statement()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(MCParser.WHILE)
            self.state = 181
            self.expression()
            self.state = 182
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
        self.enterRule(localctx, 30, self.RULE_forstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(MCParser.FOR)
            self.state = 185
            self.match(MCParser.LB)
            self.state = 186
            self.expression()
            self.state = 187
            self.match(MCParser.SEMI)
            self.state = 188
            self.expression()
            self.state = 189
            self.match(MCParser.SEMI)
            self.state = 190
            self.expression()
            self.state = 191
            self.match(MCParser.RB)
            self.state = 192
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
        self.enterRule(localctx, 32, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MCParser.BREAK)
            self.state = 195
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
        self.enterRule(localctx, 34, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MCParser.CONTINUE)
            self.state = 198
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
        self.enterRule(localctx, 36, self.RULE_returnstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MCParser.RETURN)
            self.state = 201
            self.expression()
            self.state = 202
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
        self.enterRule(localctx, 38, self.RULE_expressionstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.expression()
            self.state = 205
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
        self.enterRule(localctx, 40, self.RULE_expression)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.exp1(0)
                self.state = 208
                self.match(MCParser.ASSIGN_OP)
                self.state = 209
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 217
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 218
                    self.match(MCParser.OR_OP)
                    self.state = 219
                    self.exp2(0) 
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 228
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 229
                    self.match(MCParser.AND_OP)
                    self.state = 230
                    self.exp3() 
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_exp3)
        self._la = 0 # Token type
        try:
            self.state = 241
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.exp4()
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==MCParser.NOT_EQUAL_OP or _la==MCParser.EQUAL_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.exp4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
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
        self.enterRule(localctx, 48, self.RULE_exp4)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.exp5(0)
                self.state = 244
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LESS_OP) | (1 << MCParser.GREATER_OP) | (1 << MCParser.LESS_EQUAL_OP) | (1 << MCParser.GREATER_EQUAL_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self.exp5(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.exp6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp5)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD_OP or _la==MCParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.exp6(0) 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL_OP) | (1 << MCParser.DIV_OP) | (1 << MCParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 266
                    self.exp7() 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 54, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUB_OP, MCParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB_OP or _la==MCParser.NOT_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 273
                self.exp7()
                pass
            elif token in [MCParser.ID, MCParser.LB, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
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
        self.enterRule(localctx, 56, self.RULE_exp8)
        try:
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.exp9()
                self.state = 278
                self.match(MCParser.LSB)
                self.state = 279
                self.expression()
                self.state = 280
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
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
        self.enterRule(localctx, 58, self.RULE_exp9)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(MCParser.LB)
                self.state = 286
                self.expression()
                self.state = 287
                self.match(MCParser.RB)
                pass
            elif token in [MCParser.ID, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.BOOLLIT, MCParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
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
        self.enterRule(localctx, 60, self.RULE_exp10)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
        self.enterRule(localctx, 62, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
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
        self.enterRule(localctx, 64, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(MCParser.ID)
            self.state = 299
            self.match(MCParser.LB)
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.ID) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.BOOLLIT) | (1 << MCParser.STRINGLIT))) != 0):
                self.state = 300
                self.paralist_call()


            self.state = 303
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
        self.enterRule(localctx, 66, self.RULE_paralist_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.para_call()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.SEMI:
                self.state = 306
                self.match(MCParser.SEMI)
                self.state = 307
                self.para_call()
                self.state = 312
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
        self.enterRule(localctx, 68, self.RULE_para_call)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.operand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
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
        self._predicates[21] = self.exp1_sempred
        self._predicates[22] = self.exp2_sempred
        self._predicates[25] = self.exp5_sempred
        self._predicates[26] = self.exp6_sempred
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
         




