# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u0204\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u009e\n\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\5\16\u00b6\n\16\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20\u00cd\n")
        buf.write("\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\7(\u0105\n(\f(\16(\u0108\13(")
        buf.write("\3)\6)\u010b\n)\r)\16)\u010c\3*\6*\u0110\n*\r*\16*\u0111")
        buf.write("\3*\3*\7*\u0116\n*\f*\16*\u0119\13*\3*\3*\6*\u011d\n*")
        buf.write("\r*\16*\u011e\3*\5*\u0122\n*\3*\6*\u0125\n*\r*\16*\u0126")
        buf.write("\3*\3*\6*\u012b\n*\r*\16*\u012c\3*\5*\u0130\n*\5*\u0132")
        buf.write("\n*\5*\u0134\n*\3+\3+\5+\u0138\n+\3,\3,\3,\7,\u013d\n")
        buf.write(",\f,\16,\u0140\13,\3,\3,\3-\3-\5-\u0146\n-\3-\6-\u0149")
        buf.write("\n-\r-\16-\u014a\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:")
        buf.write("\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3=\3=\3=\5=\u01a5\n")
        buf.write("=\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01b5\n")
        buf.write("?\3@\3@\3@\3@\3@\3@\3@\3@\5@\u01bf\n@\3A\3A\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\5A\u01cb\nA\3B\3B\3B\3B\3B\3B\3B\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\5B\u01db\nB\3C\3C\3C\3C\7C\u01e1\nC\fC\16")
        buf.write("C\u01e4\13C\3C\3C\3C\3C\3D\3D\3D\3D\7D\u01ee\nD\fD\16")
        buf.write("D\u01f1\13D\3D\3D\3D\3D\3D\3E\6E\u01f9\nE\rE\16E\u01fa")
        buf.write("\3E\3E\3F\3F\3G\3G\3H\3H\2\2I\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_\2a\2")
        buf.write("c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081")
        buf.write("\2\u0083\2\u0085.\u0087/\u0089\60\u008b\61\u008d\62\u008f")
        buf.write("\63\3\2\13\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2GGgg\3")
        buf.write("\2\63;\t\2$$^^ddhhppttvv\3\2\"\"\4\2\f\f\17\17\5\2\13")
        buf.write("\f\17\17\"\"\2\u020f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2\u0085\3\2")
        buf.write("\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\2\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0095")
        buf.write("\3\2\2\2\7\u009d\3\2\2\2\t\u009f\3\2\2\2\13\u00a1\3\2")
        buf.write("\2\2\r\u00a3\3\2\2\2\17\u00a5\3\2\2\2\21\u00a7\3\2\2\2")
        buf.write("\23\u00a9\3\2\2\2\25\u00ab\3\2\2\2\27\u00ad\3\2\2\2\31")
        buf.write("\u00af\3\2\2\2\33\u00b5\3\2\2\2\35\u00b7\3\2\2\2\37\u00cc")
        buf.write("\3\2\2\2!\u00ce\3\2\2\2#\u00d1\3\2\2\2%\u00d4\3\2\2\2")
        buf.write("\'\u00d7\3\2\2\2)\u00da\3\2\2\2+\u00dd\3\2\2\2-\u00e0")
        buf.write("\3\2\2\2/\u00e2\3\2\2\2\61\u00e4\3\2\2\2\63\u00e6\3\2")
        buf.write("\2\2\65\u00e8\3\2\2\2\67\u00ea\3\2\2\29\u00ec\3\2\2\2")
        buf.write(";\u00ee\3\2\2\2=\u00f0\3\2\2\2?\u00f2\3\2\2\2A\u00f4\3")
        buf.write("\2\2\2C\u00f6\3\2\2\2E\u00f8\3\2\2\2G\u00fa\3\2\2\2I\u00fc")
        buf.write("\3\2\2\2K\u00fe\3\2\2\2M\u0100\3\2\2\2O\u0102\3\2\2\2")
        buf.write("Q\u010a\3\2\2\2S\u0133\3\2\2\2U\u0137\3\2\2\2W\u0139\3")
        buf.write("\2\2\2Y\u0143\3\2\2\2[\u014c\3\2\2\2]\u0154\3\2\2\2_\u015a")
        buf.write("\3\2\2\2a\u0164\3\2\2\2c\u0169\3\2\2\2e\u016d\3\2\2\2")
        buf.write("g\u0173\3\2\2\2i\u0176\3\2\2\2k\u017a\3\2\2\2m\u0181\3")
        buf.write("\2\2\2o\u0186\3\2\2\2q\u0189\3\2\2\2s\u018f\3\2\2\2u\u0196")
        buf.write("\3\2\2\2w\u019b\3\2\2\2y\u01a4\3\2\2\2{\u01a6\3\2\2\2")
        buf.write("}\u01b4\3\2\2\2\177\u01be\3\2\2\2\u0081\u01ca\3\2\2\2")
        buf.write("\u0083\u01da\3\2\2\2\u0085\u01dc\3\2\2\2\u0087\u01e9\3")
        buf.write("\2\2\2\u0089\u01f8\3\2\2\2\u008b\u01fe\3\2\2\2\u008d\u0200")
        buf.write("\3\2\2\2\u008f\u0202\3\2\2\2\u0091\u0092\7r\2\2\u0092")
        buf.write("\u0093\7w\2\2\u0093\u0094\7v\2\2\u0094\4\3\2\2\2\u0095")
        buf.write("\u0096\7i\2\2\u0096\u0097\7g\2\2\u0097\u0098\7v\2\2\u0098")
        buf.write("\6\3\2\2\2\u0099\u009e\5i\65\2\u009a\u009e\5[.\2\u009b")
        buf.write("\u009e\5e\63\2\u009c\u009e\5s:\2\u009d\u0099\3\2\2\2\u009d")
        buf.write("\u009a\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\b\3\2\2\2\u009f\u00a0\5m\67\2\u00a0\n\3\2\2\2\u00a1")
        buf.write("\u00a2\5g\64\2\u00a2\f\3\2\2\2\u00a3\u00a4\5a\61\2\u00a4")
        buf.write("\16\3\2\2\2\u00a5\u00a6\5c\62\2\u00a6\20\3\2\2\2\u00a7")
        buf.write("\u00a8\5o8\2\u00a8\22\3\2\2\2\u00a9\u00aa\5q9\2\u00aa")
        buf.write("\24\3\2\2\2\u00ab\u00ac\5]/\2\u00ac\26\3\2\2\2\u00ad\u00ae")
        buf.write("\5_\60\2\u00ae\30\3\2\2\2\u00af\u00b0\5k\66\2\u00b0\32")
        buf.write("\3\2\2\2\u00b1\u00b6\5\177@\2\u00b2\u00b6\5}?\2\u00b3")
        buf.write("\u00b6\5\u0081A\2\u00b4\u00b6\5\u0083B\2\u00b5\u00b1\3")
        buf.write("\2\2\2\u00b5\u00b2\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4")
        buf.write("\3\2\2\2\u00b6\34\3\2\2\2\u00b7\u00b8\7N\2\2\u00b8\u00b9")
        buf.write("\7p\2\2\u00b9\36\3\2\2\2\u00ba\u00bb\7K\2\2\u00bb\u00bc")
        buf.write("\7p\2\2\u00bc\u00cd\7v\2\2\u00bd\u00be\7H\2\2\u00be\u00bf")
        buf.write("\7n\2\2\u00bf\u00c0\7q\2\2\u00c0\u00c1\7c\2\2\u00c1\u00cd")
        buf.write("\7v\2\2\u00c2\u00c3\7D\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00cd\7n\2\2\u00c6\u00c7\7U\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca\7k\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cd\7i\2\2\u00cc\u00ba\3\2\2\2\u00cc\u00bd")
        buf.write("\3\2\2\2\u00cc\u00c2\3\2\2\2\u00cc\u00c6\3\2\2\2\u00cd")
        buf.write(" \3\2\2\2\u00ce\u00cf\7~\2\2\u00cf\u00d0\7~\2\2\u00d0")
        buf.write("\"\3\2\2\2\u00d1\u00d2\7#\2\2\u00d2\u00d3\7?\2\2\u00d3")
        buf.write("$\3\2\2\2\u00d4\u00d5\7>\2\2\u00d5\u00d6\7?\2\2\u00d6")
        buf.write("&\3\2\2\2\u00d7\u00d8\7(\2\2\u00d8\u00d9\7(\2\2\u00d9")
        buf.write("(\3\2\2\2\u00da\u00db\7?\2\2\u00db\u00dc\7?\2\2\u00dc")
        buf.write("*\3\2\2\2\u00dd\u00de\7@\2\2\u00de\u00df\7?\2\2\u00df")
        buf.write(",\3\2\2\2\u00e0\u00e1\7>\2\2\u00e1.\3\2\2\2\u00e2\u00e3")
        buf.write("\7@\2\2\u00e3\60\3\2\2\2\u00e4\u00e5\7?\2\2\u00e5\62\3")
        buf.write("\2\2\2\u00e6\u00e7\7/\2\2\u00e7\64\3\2\2\2\u00e8\u00e9")
        buf.write("\7\61\2\2\u00e9\66\3\2\2\2\u00ea\u00eb\7\'\2\2\u00eb8")
        buf.write("\3\2\2\2\u00ec\u00ed\7#\2\2\u00ed:\3\2\2\2\u00ee\u00ef")
        buf.write("\7-\2\2\u00ef<\3\2\2\2\u00f0\u00f1\7,\2\2\u00f1>\3\2\2")
        buf.write("\2\u00f2\u00f3\7]\2\2\u00f3@\3\2\2\2\u00f4\u00f5\7_\2")
        buf.write("\2\u00f5B\3\2\2\2\u00f6\u00f7\7}\2\2\u00f7D\3\2\2\2\u00f8")
        buf.write("\u00f9\7\177\2\2\u00f9F\3\2\2\2\u00fa\u00fb\7*\2\2\u00fb")
        buf.write("H\3\2\2\2\u00fc\u00fd\7+\2\2\u00fdJ\3\2\2\2\u00fe\u00ff")
        buf.write("\7=\2\2\u00ffL\3\2\2\2\u0100\u0101\7.\2\2\u0101N\3\2\2")
        buf.write("\2\u0102\u0106\t\2\2\2\u0103\u0105\t\3\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107P\3\2\2\2\u0108\u0106\3\2\2\2\u0109")
        buf.write("\u010b\t\4\2\2\u010a\u0109\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010dR\3\2\2")
        buf.write("\2\u010e\u0110\t\4\2\2\u010f\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0134\5Y-\2\u0114\u0116\t\4\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2")
        buf.write("\u0117\u0118\3\2\2\2\u0118\u011a\3\2\2\2\u0119\u0117\3")
        buf.write("\2\2\2\u011a\u011c\7\60\2\2\u011b\u011d\t\4\2\2\u011c")
        buf.write("\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120\u0122\5")
        buf.write("Y-\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0134")
        buf.write("\3\2\2\2\u0123\u0125\t\4\2\2\u0124\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u0131\7\60\2\2\u0129\u012b")
        buf.write("\t\4\2\2\u012a\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012f\3\2\2\2")
        buf.write("\u012e\u0130\5Y-\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2")
        buf.write("\2\2\u0130\u0132\3\2\2\2\u0131\u012a\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u010f\3\2\2\2\u0133")
        buf.write("\u0117\3\2\2\2\u0133\u0124\3\2\2\2\u0134T\3\2\2\2\u0135")
        buf.write("\u0138\5u;\2\u0136\u0138\5w<\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138V\3\2\2\2\u0139\u013e\5{>\2\u013a")
        buf.write("\u013d\5y=\2\u013b\u013d\13\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2\2\u013e\u013c\3")
        buf.write("\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140\u013e")
        buf.write("\3\2\2\2\u0141\u0142\5{>\2\u0142X\3\2\2\2\u0143\u0145")
        buf.write("\t\5\2\2\u0144\u0146\7/\2\2\u0145\u0144\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0149\t\6\2\2")
        buf.write("\u0148\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u0148\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014bZ\3\2\2\2\u014c\u014d")
        buf.write("\7d\2\2\u014d\u014e\7q\2\2\u014e\u014f\7q\2\2\u014f\u0150")
        buf.write("\7n\2\2\u0150\u0151\7g\2\2\u0151\u0152\7c\2\2\u0152\u0153")
        buf.write("\7p\2\2\u0153\\\3\2\2\2\u0154\u0155\7d\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156\u0157\7g\2\2\u0157\u0158\7c\2\2\u0158\u0159")
        buf.write("\7m\2\2\u0159^\3\2\2\2\u015a\u015b\7e\2\2\u015b\u015c")
        buf.write("\7q\2\2\u015c\u015d\7p\2\2\u015d\u015e\7v\2\2\u015e\u015f")
        buf.write("\7k\2\2\u015f\u0160\7p\2\2\u0160\u0161\7w\2\2\u0161\u0162")
        buf.write("\7v\2\2\u0162\u0163\7g\2\2\u0163`\3\2\2\2\u0164\u0165")
        buf.write("\7g\2\2\u0165\u0166\7n\2\2\u0166\u0167\7u\2\2\u0167\u0168")
        buf.write("\7g\2\2\u0168b\3\2\2\2\u0169\u016a\7h\2\2\u016a\u016b")
        buf.write("\7q\2\2\u016b\u016c\7t\2\2\u016cd\3\2\2\2\u016d\u016e")
        buf.write("\7h\2\2\u016e\u016f\7n\2\2\u016f\u0170\7q\2\2\u0170\u0171")
        buf.write("\7c\2\2\u0171\u0172\7v\2\2\u0172f\3\2\2\2\u0173\u0174")
        buf.write("\7k\2\2\u0174\u0175\7h\2\2\u0175h\3\2\2\2\u0176\u0177")
        buf.write("\7k\2\2\u0177\u0178\7p\2\2\u0178\u0179\7v\2\2\u0179j\3")
        buf.write("\2\2\2\u017a\u017b\7t\2\2\u017b\u017c\7g\2\2\u017c\u017d")
        buf.write("\7v\2\2\u017d\u017e\7w\2\2\u017e\u017f\7t\2\2\u017f\u0180")
        buf.write("\7p\2\2\u0180l\3\2\2\2\u0181\u0182\7x\2\2\u0182\u0183")
        buf.write("\7q\2\2\u0183\u0184\7k\2\2\u0184\u0185\7f\2\2\u0185n\3")
        buf.write("\2\2\2\u0186\u0187\7f\2\2\u0187\u0188\7q\2\2\u0188p\3")
        buf.write("\2\2\2\u0189\u018a\7y\2\2\u018a\u018b\7j\2\2\u018b\u018c")
        buf.write("\7k\2\2\u018c\u018d\7n\2\2\u018d\u018e\7g\2\2\u018er\3")
        buf.write("\2\2\2\u018f\u0190\7u\2\2\u0190\u0191\7v\2\2\u0191\u0192")
        buf.write("\7t\2\2\u0192\u0193\7k\2\2\u0193\u0194\7p\2\2\u0194\u0195")
        buf.write("\7i\2\2\u0195t\3\2\2\2\u0196\u0197\7v\2\2\u0197\u0198")
        buf.write("\7t\2\2\u0198\u0199\7w\2\2\u0199\u019a\7g\2\2\u019av\3")
        buf.write("\2\2\2\u019b\u019c\7h\2\2\u019c\u019d\7c\2\2\u019d\u019e")
        buf.write("\7n\2\2\u019e\u019f\7u\2\2\u019f\u01a0\7g\2\2\u01a0x\3")
        buf.write("\2\2\2\u01a1\u01a2\7^\2\2\u01a2\u01a5\t\7\2\2\u01a3\u01a5")
        buf.write("\t\b\2\2\u01a4\u01a1\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("z\3\2\2\2\u01a6\u01a7\7$\2\2\u01a7|\3\2\2\2\u01a8\u01a9")
        buf.write("\7H\2\2\u01a9\u01aa\7n\2\2\u01aa\u01ab\7q\2\2\u01ab\u01ac")
        buf.write("\7c\2\2\u01ac\u01b5\7v\2\2\u01ad\u01ae\7H\2\2\u01ae\u01af")
        buf.write("\7n\2\2\u01af\u01b0\7q\2\2\u01b0\u01b1\7c\2\2\u01b1\u01b2")
        buf.write("\7v\2\2\u01b2\u01b3\7N\2\2\u01b3\u01b5\7p\2\2\u01b4\u01a8")
        buf.write("\3\2\2\2\u01b4\u01ad\3\2\2\2\u01b5~\3\2\2\2\u01b6\u01b7")
        buf.write("\7K\2\2\u01b7\u01b8\7p\2\2\u01b8\u01bf\7v\2\2\u01b9\u01ba")
        buf.write("\7K\2\2\u01ba\u01bb\7p\2\2\u01bb\u01bc\7v\2\2\u01bc\u01bd")
        buf.write("\7N\2\2\u01bd\u01bf\7p\2\2\u01be\u01b6\3\2\2\2\u01be\u01b9")
        buf.write("\3\2\2\2\u01bf\u0080\3\2\2\2\u01c0\u01c1\7D\2\2\u01c1")
        buf.write("\u01c2\7q\2\2\u01c2\u01c3\7q\2\2\u01c3\u01cb\7n\2\2\u01c4")
        buf.write("\u01c5\7D\2\2\u01c5\u01c6\7q\2\2\u01c6\u01c7\7q\2\2\u01c7")
        buf.write("\u01c8\7n\2\2\u01c8\u01c9\7N\2\2\u01c9\u01cb\7p\2\2\u01ca")
        buf.write("\u01c0\3\2\2\2\u01ca\u01c4\3\2\2\2\u01cb\u0082\3\2\2\2")
        buf.write("\u01cc\u01cd\7U\2\2\u01cd\u01ce\7v\2\2\u01ce\u01cf\7t")
        buf.write("\2\2\u01cf\u01d0\7k\2\2\u01d0\u01d1\7p\2\2\u01d1\u01db")
        buf.write("\7i\2\2\u01d2\u01d3\7U\2\2\u01d3\u01d4\7v\2\2\u01d4\u01d5")
        buf.write("\7t\2\2\u01d5\u01d6\7k\2\2\u01d6\u01d7\7p\2\2\u01d7\u01d8")
        buf.write("\7i\2\2\u01d8\u01d9\7N\2\2\u01d9\u01db\7p\2\2\u01da\u01cc")
        buf.write("\3\2\2\2\u01da\u01d2\3\2\2\2\u01db\u0084\3\2\2\2\u01dc")
        buf.write("\u01dd\7\61\2\2\u01dd\u01de\7\61\2\2\u01de\u01e2\3\2\2")
        buf.write("\2\u01df\u01e1\13\2\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e4")
        buf.write("\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3")
        buf.write("\u01e5\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\t\t\2\2")
        buf.write("\u01e6\u01e7\3\2\2\2\u01e7\u01e8\bC\2\2\u01e8\u0086\3")
        buf.write("\2\2\2\u01e9\u01ea\7\61\2\2\u01ea\u01eb\7,\2\2\u01eb\u01ef")
        buf.write("\3\2\2\2\u01ec\u01ee\13\2\2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f3\7")
        buf.write(",\2\2\u01f3\u01f4\7\61\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6")
        buf.write("\bD\2\2\u01f6\u0088\3\2\2\2\u01f7\u01f9\t\n\2\2\u01f8")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01f8\3\2\2\2")
        buf.write("\u01fa\u01fb\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\b")
        buf.write("E\2\2\u01fd\u008a\3\2\2\2\u01fe\u01ff\13\2\2\2\u01ff\u008c")
        buf.write("\3\2\2\2\u0200\u0201\13\2\2\2\u0201\u008e\3\2\2\2\u0202")
        buf.write("\u0203\13\2\2\2\u0203\u0090\3\2\2\2\36\2\u009d\u00b5\u00cc")
        buf.write("\u0106\u010c\u0111\u0117\u011e\u0121\u0126\u012c\u012f")
        buf.write("\u0131\u0133\u0137\u013c\u013e\u0145\u014a\u01a4\u01b4")
        buf.write("\u01be\u01ca\u01da\u01e2\u01ef\u01fa\3\b\2\2")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    PRITYPE = 3
    VOIDTYPE = 4
    If = 5
    Else = 6
    For = 7
    Do = 8
    While = 9
    Break = 10
    Continue = 11
    Return = 12
    Put = 13
    Ln = 14
    Get = 15
    LOGICOR = 16
    NOTEQ = 17
    LESSEQ = 18
    LOGICAND = 19
    EQ = 20
    GREATEREQ = 21
    LESS = 22
    GREATER = 23
    AS = 24
    SUB = 25
    DIV = 26
    MOD = 27
    LOGICNOT = 28
    ADD = 29
    MUL = 30
    LS = 31
    RS = 32
    LP = 33
    RP = 34
    LB = 35
    RB = 36
    SEMI = 37
    COMMA = 38
    ID = 39
    INTLIT = 40
    FLOATLIT = 41
    BOOLEANLIT = 42
    STRINGLIT = 43
    LINECOMMENT = 44
    BLOCKCOMMENT = 45
    WS = 46
    ERROR_CHAR = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'put'", "'get'", "'Ln'", "'||'", "'!='", "'<='", "'&&'", "'=='", 
            "'>='", "'<'", "'>'", "'='", "'-'", "'/'", "'%'", "'!'", "'+'", 
            "'*'", "'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "PRITYPE", "VOIDTYPE", "If", "Else", "For", "Do", "While", "Break", 
            "Continue", "Return", "Put", "Ln", "Get", "LOGICOR", "NOTEQ", 
            "LESSEQ", "LOGICAND", "EQ", "GREATEREQ", "LESS", "GREATER", 
            "AS", "SUB", "DIV", "MOD", "LOGICNOT", "ADD", "MUL", "LS", "RS", 
            "LP", "RP", "LB", "RB", "SEMI", "COMMA", "ID", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "LINECOMMENT", "BLOCKCOMMENT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "PRITYPE", "VOIDTYPE", "If", "Else", "For", 
                  "Do", "While", "Break", "Continue", "Return", "Put", "Ln", 
                  "Get", "LOGICOR", "NOTEQ", "LESSEQ", "LOGICAND", "EQ", 
                  "GREATEREQ", "LESS", "GREATER", "AS", "SUB", "DIV", "MOD", 
                  "LOGICNOT", "ADD", "MUL", "LS", "RS", "LP", "RP", "LB", 
                  "RB", "SEMI", "COMMA", "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                  "STRINGLIT", "EX", "BOOLEAN", "BREAK", "CONTINUTE", "ELSE", 
                  "FOR", "FLOAT", "IF", "INT", "RETURN", "VOID", "DO", "WHILE", 
                  "STRING", "TRUE", "FALSE", "STRINGKEY", "DOUQUOTES", "Float", 
                  "Int", "Bool", "String", "LINECOMMENT", "BLOCKCOMMENT", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


