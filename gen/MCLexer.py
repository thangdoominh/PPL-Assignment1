# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/PPL-Assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0166\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\7\21")
        buf.write("\u00c0\n\21\f\21\16\21\u00c3\13\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\6)\u00fa")
        buf.write("\n)\r)\16)\u00fb\3*\3*\5*\u0100\n*\3+\5+\u0103\n+\3+\5")
        buf.write("+\u0106\n+\3+\3+\3+\3+\3+\5+\u010d\n+\5+\u010f\n+\3,\3")
        buf.write(",\5,\u0113\n,\3,\3,\5,\u0117\n,\3,\3,\3-\3-\5-\u011d\n")
        buf.write("-\3.\3.\3.\3.\7.\u0123\n.\f.\16.\u0126\13.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\7/\u012f\n/\f/\16/\u0132\13/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\7\60\u013a\n\60\f\60\16\60\u013d\13\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\6\61\u0145\n\61\r\61\16\61\u0146")
        buf.write("\3\61\3\61\3\62\3\62\7\62\u014d\n\62\f\62\16\62\u0150")
        buf.write("\13\62\3\62\3\62\3\62\5\62\u0155\n\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\63\7\63\u015d\n\63\f\63\16\63\u0160\13\63\3")
        buf.write("\63\3\63\3\64\3\64\3\64\4\u013b\u014e\2\65\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[")
        buf.write("/]\60_\61a\62c\63e\64g\65\3\2\13\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\3\2\62;\4\2--//\4\2GGgg\t\2$$^^ddhhppttvv\6\2\n\f")
        buf.write("\16\17$$^^\4\2\13\f\16\17\5\2\13\f\17\17\"\"\2\u0178\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\3i\3\2\2\2\5m\3\2\2\2\7u\3\2\2\2\t|\3\2\2\2\13")
        buf.write("\u0082\3\2\2\2\r\u0087\3\2\2\2\17\u008d\3\2\2\2\21\u0096")
        buf.write("\3\2\2\2\23\u009d\3\2\2\2\25\u00a2\3\2\2\2\27\u00a6\3")
        buf.write("\2\2\2\31\u00a9\3\2\2\2\33\u00ac\3\2\2\2\35\u00b2\3\2")
        buf.write("\2\2\37\u00b7\3\2\2\2!\u00bd\3\2\2\2#\u00c4\3\2\2\2%\u00c6")
        buf.write("\3\2\2\2\'\u00c8\3\2\2\2)\u00ca\3\2\2\2+\u00cc\3\2\2\2")
        buf.write("-\u00ce\3\2\2\2/\u00d0\3\2\2\2\61\u00d3\3\2\2\2\63\u00d6")
        buf.write("\3\2\2\2\65\u00d9\3\2\2\2\67\u00dc\3\2\2\29\u00de\3\2")
        buf.write("\2\2;\u00e0\3\2\2\2=\u00e3\3\2\2\2?\u00e6\3\2\2\2A\u00e8")
        buf.write("\3\2\2\2C\u00ea\3\2\2\2E\u00ec\3\2\2\2G\u00ee\3\2\2\2")
        buf.write("I\u00f0\3\2\2\2K\u00f2\3\2\2\2M\u00f4\3\2\2\2O\u00f6\3")
        buf.write("\2\2\2Q\u00f9\3\2\2\2S\u00ff\3\2\2\2U\u010e\3\2\2\2W\u0112")
        buf.write("\3\2\2\2Y\u011c\3\2\2\2[\u011e\3\2\2\2]\u012a\3\2\2\2")
        buf.write("_\u0135\3\2\2\2a\u0144\3\2\2\2c\u014a\3\2\2\2e\u0158\3")
        buf.write("\2\2\2g\u0163\3\2\2\2ij\7k\2\2jk\7p\2\2kl\7v\2\2l\4\3")
        buf.write("\2\2\2mn\7d\2\2no\7q\2\2op\7q\2\2pq\7n\2\2qr\7g\2\2rs")
        buf.write("\7c\2\2st\7p\2\2t\6\3\2\2\2uv\7u\2\2vw\7v\2\2wx\7t\2\2")
        buf.write("xy\7k\2\2yz\7p\2\2z{\7i\2\2{\b\3\2\2\2|}\7h\2\2}~\7n\2")
        buf.write("\2~\177\7q\2\2\177\u0080\7c\2\2\u0080\u0081\7v\2\2\u0081")
        buf.write("\n\3\2\2\2\u0082\u0083\7x\2\2\u0083\u0084\7q\2\2\u0084")
        buf.write("\u0085\7k\2\2\u0085\u0086\7f\2\2\u0086\f\3\2\2\2\u0087")
        buf.write("\u0088\7d\2\2\u0088\u0089\7t\2\2\u0089\u008a\7g\2\2\u008a")
        buf.write("\u008b\7c\2\2\u008b\u008c\7m\2\2\u008c\16\3\2\2\2\u008d")
        buf.write("\u008e\7e\2\2\u008e\u008f\7q\2\2\u008f\u0090\7p\2\2\u0090")
        buf.write("\u0091\7v\2\2\u0091\u0092\7k\2\2\u0092\u0093\7p\2\2\u0093")
        buf.write("\u0094\7w\2\2\u0094\u0095\7g\2\2\u0095\20\3\2\2\2\u0096")
        buf.write("\u0097\7t\2\2\u0097\u0098\7g\2\2\u0098\u0099\7v\2\2\u0099")
        buf.write("\u009a\7w\2\2\u009a\u009b\7t\2\2\u009b\u009c\7p\2\2\u009c")
        buf.write("\22\3\2\2\2\u009d\u009e\7g\2\2\u009e\u009f\7n\2\2\u009f")
        buf.write("\u00a0\7u\2\2\u00a0\u00a1\7g\2\2\u00a1\24\3\2\2\2\u00a2")
        buf.write("\u00a3\7h\2\2\u00a3\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5")
        buf.write("\26\3\2\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7h\2\2\u00a8")
        buf.write("\30\3\2\2\2\u00a9\u00aa\7f\2\2\u00aa\u00ab\7q\2\2\u00ab")
        buf.write("\32\3\2\2\2\u00ac\u00ad\7y\2\2\u00ad\u00ae\7j\2\2\u00ae")
        buf.write("\u00af\7k\2\2\u00af\u00b0\7n\2\2\u00b0\u00b1\7g\2\2\u00b1")
        buf.write("\34\3\2\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write("\u00b5\7w\2\2\u00b5\u00b6\7g\2\2\u00b6\36\3\2\2\2\u00b7")
        buf.write("\u00b8\7h\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7n\2\2\u00ba")
        buf.write("\u00bb\7u\2\2\u00bb\u00bc\7g\2\2\u00bc \3\2\2\2\u00bd")
        buf.write("\u00c1\t\2\2\2\u00be\u00c0\t\3\2\2\u00bf\u00be\3\2\2\2")
        buf.write("\u00c0\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\"\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c5")
        buf.write("\7-\2\2\u00c5$\3\2\2\2\u00c6\u00c7\7/\2\2\u00c7&\3\2\2")
        buf.write("\2\u00c8\u00c9\7,\2\2\u00c9(\3\2\2\2\u00ca\u00cb\7\61")
        buf.write("\2\2\u00cb*\3\2\2\2\u00cc\u00cd\7#\2\2\u00cd,\3\2\2\2")
        buf.write("\u00ce\u00cf\7\'\2\2\u00cf.\3\2\2\2\u00d0\u00d1\7~\2\2")
        buf.write("\u00d1\u00d2\7~\2\2\u00d2\60\3\2\2\2\u00d3\u00d4\7(\2")
        buf.write("\2\u00d4\u00d5\7(\2\2\u00d5\62\3\2\2\2\u00d6\u00d7\7#")
        buf.write("\2\2\u00d7\u00d8\7?\2\2\u00d8\64\3\2\2\2\u00d9\u00da\7")
        buf.write("?\2\2\u00da\u00db\7?\2\2\u00db\66\3\2\2\2\u00dc\u00dd")
        buf.write("\7>\2\2\u00dd8\3\2\2\2\u00de\u00df\7@\2\2\u00df:\3\2\2")
        buf.write("\2\u00e0\u00e1\7>\2\2\u00e1\u00e2\7?\2\2\u00e2<\3\2\2")
        buf.write("\2\u00e3\u00e4\7@\2\2\u00e4\u00e5\7?\2\2\u00e5>\3\2\2")
        buf.write("\2\u00e6\u00e7\7?\2\2\u00e7@\3\2\2\2\u00e8\u00e9\7]\2")
        buf.write("\2\u00e9B\3\2\2\2\u00ea\u00eb\7_\2\2\u00ebD\3\2\2\2\u00ec")
        buf.write("\u00ed\7}\2\2\u00edF\3\2\2\2\u00ee\u00ef\7\177\2\2\u00ef")
        buf.write("H\3\2\2\2\u00f0\u00f1\7*\2\2\u00f1J\3\2\2\2\u00f2\u00f3")
        buf.write("\7+\2\2\u00f3L\3\2\2\2\u00f4\u00f5\7=\2\2\u00f5N\3\2\2")
        buf.write("\2\u00f6\u00f7\7.\2\2\u00f7P\3\2\2\2\u00f8\u00fa\t\4\2")
        buf.write("\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fcR\3\2\2\2\u00fd\u0100")
        buf.write("\5U+\2\u00fe\u0100\5W,\2\u00ff\u00fd\3\2\2\2\u00ff\u00fe")
        buf.write("\3\2\2\2\u0100T\3\2\2\2\u0101\u0103\t\5\2\2\u0102\u0101")
        buf.write("\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0105\3\2\2\2\u0104")
        buf.write("\u0106\5Q)\2\u0105\u0104\3\2\2\2\u0105\u0106\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0108\7\60\2\2\u0108\u010f\5Q)\2")
        buf.write("\u0109\u010a\5Q)\2\u010a\u010c\7\60\2\2\u010b\u010d\5")
        buf.write("Q)\2\u010c\u010b\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f")
        buf.write("\3\2\2\2\u010e\u0102\3\2\2\2\u010e\u0109\3\2\2\2\u010f")
        buf.write("V\3\2\2\2\u0110\u0113\5U+\2\u0111\u0113\5Q)\2\u0112\u0110")
        buf.write("\3\2\2\2\u0112\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0116\t\6\2\2\u0115\u0117\t\5\2\2\u0116\u0115\3\2\2\2")
        buf.write("\u0116\u0117\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\5")
        buf.write("Q)\2\u0119X\3\2\2\2\u011a\u011d\5\35\17\2\u011b\u011d")
        buf.write("\5\37\20\2\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011d")
        buf.write("Z\3\2\2\2\u011e\u0124\7$\2\2\u011f\u0120\7^\2\2\u0120")
        buf.write("\u0123\t\7\2\2\u0121\u0123\n\b\2\2\u0122\u011f\3\2\2\2")
        buf.write("\u0122\u0121\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3")
        buf.write("\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0127\u0128\7$\2\2\u0128\u0129\b.\2\2\u0129\\")
        buf.write("\3\2\2\2\u012a\u012b\7\61\2\2\u012b\u012c\7\61\2\2\u012c")
        buf.write("\u0130\3\2\2\2\u012d\u012f\n\t\2\2\u012e\u012d\3\2\2\2")
        buf.write("\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3")
        buf.write("\2\2\2\u0131\u0133\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0134")
        buf.write("\b/\3\2\u0134^\3\2\2\2\u0135\u0136\7\61\2\2\u0136\u0137")
        buf.write("\7,\2\2\u0137\u013b\3\2\2\2\u0138\u013a\13\2\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u013c\3\2\2\2")
        buf.write("\u013b\u0139\3\2\2\2\u013c\u013e\3\2\2\2\u013d\u013b\3")
        buf.write("\2\2\2\u013e\u013f\7,\2\2\u013f\u0140\7\61\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0142\b\60\3\2\u0142`\3\2\2\2\u0143\u0145")
        buf.write("\t\n\2\2\u0144\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148\3\2\2\2")
        buf.write("\u0148\u0149\b\61\3\2\u0149b\3\2\2\2\u014a\u014e\7$\2")
        buf.write("\2\u014b\u014d\13\2\2\2\u014c\u014b\3\2\2\2\u014d\u0150")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014e\u014c\3\2\2\2\u014f")
        buf.write("\u0154\3\2\2\2\u0150\u014e\3\2\2\2\u0151\u0152\7^\2\2")
        buf.write("\u0152\u0155\n\7\2\2\u0153\u0155\t\b\2\2\u0154\u0151\3")
        buf.write("\2\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157")
        buf.write("\b\62\4\2\u0157d\3\2\2\2\u0158\u015e\7$\2\2\u0159\u015a")
        buf.write("\7^\2\2\u015a\u015d\t\7\2\2\u015b\u015d\n\b\2\2\u015c")
        buf.write("\u0159\3\2\2\2\u015c\u015b\3\2\2\2\u015d\u0160\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0161\3")
        buf.write("\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\b\63\5\2\u0162")
        buf.write("f\3\2\2\2\u0163\u0164\13\2\2\2\u0164\u0165\b\64\6\2\u0165")
        buf.write("h\3\2\2\2\26\2\u00c1\u00fb\u00ff\u0102\u0105\u010c\u010e")
        buf.write("\u0112\u0116\u011c\u0122\u0124\u0130\u013b\u0146\u014e")
        buf.write("\u0154\u015c\u015e\7\3.\2\b\2\2\3\62\3\3\63\4\3\64\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    BOOLTYPE = 2
    STRINGTYPE = 3
    FLOATTYPE = 4
    VOIDTYPE = 5
    BREAK = 6
    CONTINUE = 7
    RETURN = 8
    ELSE = 9
    FOR = 10
    IF = 11
    DO = 12
    WHILE = 13
    TRUE = 14
    FALSE = 15
    ID = 16
    ADD_OP = 17
    SUB_OP = 18
    MUL_OP = 19
    DIV_OP = 20
    NOT_OP = 21
    MOD_OP = 22
    OR_OP = 23
    AND_OP = 24
    NOT_EQUAL_OP = 25
    EQUAL_OP = 26
    LESS_OP = 27
    GREATER_OP = 28
    LESS_EQUAL_OP = 29
    GREATER_EQUAL_OP = 30
    ASSIGN_OP = 31
    LSB = 32
    RSB = 33
    LP = 34
    RP = 35
    LB = 36
    RB = 37
    SEMI = 38
    COMMA = 39
    INTLIT = 40
    FLOATLIT = 41
    FRAC = 42
    EXPONENT = 43
    BOOLLIT = 44
    STRINGLIT = 45
    COMMENTS_LINE = 46
    COMMENTS_BLOCK = 47
    WS = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'boolean'", "'string'", "'float'", "'void'", "'break'", 
            "'continue'", "'return'", "'else'", "'for'", "'if'", "'do'", 
            "'while'", "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", 
            "'!'", "'%'", "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", 
            "'<='", "'>='", "'='", "'['", "']'", "'{'", "'}'", "'('", "')'", 
            "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "BOOLTYPE", "STRINGTYPE", "FLOATTYPE", "VOIDTYPE", 
            "BREAK", "CONTINUE", "RETURN", "ELSE", "FOR", "IF", "DO", "WHILE", 
            "TRUE", "FALSE", "ID", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", 
            "NOT_OP", "MOD_OP", "OR_OP", "AND_OP", "NOT_EQUAL_OP", "EQUAL_OP", 
            "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", "GREATER_EQUAL_OP", 
            "ASSIGN_OP", "LSB", "RSB", "LP", "RP", "LB", "RB", "SEMI", "COMMA", 
            "INTLIT", "FLOATLIT", "FRAC", "EXPONENT", "BOOLLIT", "STRINGLIT", 
            "COMMENTS_LINE", "COMMENTS_BLOCK", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "INTTYPE", "BOOLTYPE", "STRINGTYPE", "FLOATTYPE", "VOIDTYPE", 
                  "BREAK", "CONTINUE", "RETURN", "ELSE", "FOR", "IF", "DO", 
                  "WHILE", "TRUE", "FALSE", "ID", "ADD_OP", "SUB_OP", "MUL_OP", 
                  "DIV_OP", "NOT_OP", "MOD_OP", "OR_OP", "AND_OP", "NOT_EQUAL_OP", 
                  "EQUAL_OP", "LESS_OP", "GREATER_OP", "LESS_EQUAL_OP", 
                  "GREATER_EQUAL_OP", "ASSIGN_OP", "LSB", "RSB", "LP", "RP", 
                  "LB", "RB", "SEMI", "COMMA", "INTLIT", "FLOATLIT", "FRAC", 
                  "EXPONENT", "BOOLLIT", "STRINGLIT", "COMMENTS_LINE", "COMMENTS_BLOCK", 
                  "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[44] = self.STRINGLIT_action 
            actions[48] = self.ILLEGAL_ESCAPE_action 
            actions[49] = self.UNCLOSE_STRING_action 
            actions[50] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            				self.text = self.text[1:-1]
            			
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            					raise IllegalEscape(self.text[1:])
            				
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            					raise UncloseString(self.text[1:])
            				
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            					raise ErrorToken(self.text)
            				
     


