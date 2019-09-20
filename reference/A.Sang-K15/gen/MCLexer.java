// Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/reference/A.Sang-K15/MC.g4 by ANTLR 4.7.2

	package mc.parser;

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MCLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BOOLLIT=1, BOOLTYPE=2, BREAK=3, CONTINUE=4, ELSE=5, FOR=6, IF=7, RETURN=8, 
		DO=9, WHILE=10, TRUE=11, FALSE=12, STRINGTYPE=13, FLOATTYPE=14, INTTYPE=15, 
		VOIDTYPE=16, ID=17, INTLIT=18, FLOATLIT=19, FRAC=20, EXP=21, ILLEGAL_ESCAPE=22, 
		STRINGLIT=23, LB=24, RB=25, LP=26, RP=27, LSB=28, RSB=29, SEMI=30, COMMA=31, 
		WS=32, ADDOP=33, SUBOP=34, MULOP=35, DIVOP=36, MODOP=37, NOTOP=38, OROP=39, 
		ANDOP=40, NOTEQUALOP=41, EQUALOP=42, LESSOP=43, GREATEROP=44, LEOREQUOP=45, 
		GROREQUOP=46, ASSIGNOP=47, BLOCKCOM=48, LINECOM=49, UNCLOSE_STRING=50, 
		ERROR_CHAR=51;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"BOOLLIT", "BOOLTYPE", "BREAK", "CONTINUE", "ELSE", "FOR", "IF", "RETURN", 
			"DO", "WHILE", "TRUE", "FALSE", "STRINGTYPE", "FLOATTYPE", "INTTYPE", 
			"VOIDTYPE", "ID", "INTLIT", "FLOATLIT", "FRAC", "EXP", "ILLEGAL_ESCAPE", 
			"STRINGLIT", "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COMMA", "WS", 
			"ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", "OROP", "ANDOP", 
			"NOTEQUALOP", "EQUALOP", "LESSOP", "GREATEROP", "LEOREQUOP", "GROREQUOP", 
			"ASSIGNOP", "BLOCKCOM", "LINECOM", "UNCLOSE_STRING", "ERROR_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'boolean'", "'break'", "'continue'", "'else'", "'for'", 
			"'if'", "'return'", "'do'", "'while'", "'true'", "'false'", "'string'", 
			"'float'", "'int'", "'void'", null, null, null, null, null, null, null, 
			"'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", null, "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'!'", "'||'", "'&&'", "'!='", "'=='", "'<'", 
			"'>'", "'<='", "'>='", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BOOLLIT", "BOOLTYPE", "BREAK", "CONTINUE", "ELSE", "FOR", "IF", 
			"RETURN", "DO", "WHILE", "TRUE", "FALSE", "STRINGTYPE", "FLOATTYPE", 
			"INTTYPE", "VOIDTYPE", "ID", "INTLIT", "FLOATLIT", "FRAC", "EXP", "ILLEGAL_ESCAPE", 
			"STRINGLIT", "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COMMA", "WS", 
			"ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOTOP", "OROP", "ANDOP", 
			"NOTEQUALOP", "EQUALOP", "LESSOP", "GREATEROP", "LEOREQUOP", "GROREQUOP", 
			"ASSIGNOP", "BLOCKCOM", "LINECOM", "UNCLOSE_STRING", "ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	@Override
	public Token emit() {
	    switch (getType()) {
	    case UNCLOSE_STRING:
	        Token result = super.emit();
	        // you'll need to define this method
	        throw new UncloseString(result.getText());

	    case ILLEGAL_ESCAPE:
	    	result = super.emit();
	    	throw new IllegalEscape(result.getText());

	    case ERROR_CHAR:
	    	result = super.emit();
	    	throw new ErrorToken(result.getText());

	    default:
	        return super.emit();
	    }
	}


	public MCLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 21:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		case 22:
			STRINGLIT_action((RuleContext)_localctx, actionIndex);
			break;
		case 49:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:

			                              String s = getText();
			                              int i = 0;
			                              for(i=0; i<s.length(); i++) {
			                                  char a = s.charAt(i+1);
			                              Boolean b = ((a != 'b') && (a != 'f') && (a != 'r') && (a != 'n')&& (a != 't')&& (a != '\'')&& (a != '"')&& (a != '\\'));
			                                  if (( s.charAt(i) == '\\') && (b == true)) {break;}
			                              }
			                              s = s.substring(1,i+2);
			                              setText(s);
			                          
			break;
		}
	}
	private void STRINGLIT_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:

			    String s = getText();
			    s = s.substring(1,s.length()-1);
			    setText(s);

			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:

			    String s = getText();
			    s = s.substring(1,s.length());
			    setText(s);

			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65\u0161\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\3\2\3\2\5\2l\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3"+
		"\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3"+
		"\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3"+
		"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3"+
		"\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\7\22\u00c4\n\22\f\22"+
		"\16\22\u00c7\13\22\3\23\6\23\u00ca\n\23\r\23\16\23\u00cb\3\24\3\24\5\24"+
		"\u00d0\n\24\3\25\5\25\u00d3\n\25\3\25\3\25\3\25\3\25\3\25\5\25\u00da\n"+
		"\25\5\25\u00dc\n\25\3\26\3\26\5\26\u00e0\n\26\3\26\3\26\5\26\u00e4\n\26"+
		"\3\26\3\26\3\27\3\27\7\27\u00ea\n\27\f\27\16\27\u00ed\13\27\3\27\3\27"+
		"\3\27\7\27\u00f2\n\27\f\27\16\27\u00f5\13\27\3\27\3\27\3\30\3\30\7\30"+
		"\u00fb\n\30\f\30\16\30\u00fe\13\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32"+
		"\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\6!\u0114\n"+
		"!\r!\16!\u0115\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3("+
		"\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3"+
		"\61\3\61\3\61\3\61\7\61\u0142\n\61\f\61\16\61\u0145\13\61\3\61\3\61\3"+
		"\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u0150\n\62\f\62\16\62\u0153\13"+
		"\62\3\62\3\62\3\63\3\63\7\63\u0159\n\63\f\63\16\63\u015c\13\63\3\63\3"+
		"\63\3\64\3\64\5\u00eb\u00f3\u0143\2\65\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21"+
		"\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30"+
		"/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.["+
		"/]\60_\61a\62c\63e\64g\65\3\2\13\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2"+
		"GGgg\4\2--//\n\2$$))^^ddhhppttvv\4\2\f\f$$\5\2\13\f\17\17\"\"\4\2\f\f"+
		"\17\17\2\u0170\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3"+
		"\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2"+
		"\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3"+
		"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2"+
		"\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2"+
		"9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3"+
		"\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2"+
		"\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2"+
		"_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\3k\3\2\2\2\5m\3"+
		"\2\2\2\7u\3\2\2\2\t{\3\2\2\2\13\u0084\3\2\2\2\r\u0089\3\2\2\2\17\u008d"+
		"\3\2\2\2\21\u0090\3\2\2\2\23\u0097\3\2\2\2\25\u009a\3\2\2\2\27\u00a0\3"+
		"\2\2\2\31\u00a5\3\2\2\2\33\u00ab\3\2\2\2\35\u00b2\3\2\2\2\37\u00b8\3\2"+
		"\2\2!\u00bc\3\2\2\2#\u00c1\3\2\2\2%\u00c9\3\2\2\2\'\u00cf\3\2\2\2)\u00db"+
		"\3\2\2\2+\u00df\3\2\2\2-\u00e7\3\2\2\2/\u00f8\3\2\2\2\61\u0102\3\2\2\2"+
		"\63\u0104\3\2\2\2\65\u0106\3\2\2\2\67\u0108\3\2\2\29\u010a\3\2\2\2;\u010c"+
		"\3\2\2\2=\u010e\3\2\2\2?\u0110\3\2\2\2A\u0113\3\2\2\2C\u0119\3\2\2\2E"+
		"\u011b\3\2\2\2G\u011d\3\2\2\2I\u011f\3\2\2\2K\u0121\3\2\2\2M\u0123\3\2"+
		"\2\2O\u0125\3\2\2\2Q\u0128\3\2\2\2S\u012b\3\2\2\2U\u012e\3\2\2\2W\u0131"+
		"\3\2\2\2Y\u0133\3\2\2\2[\u0135\3\2\2\2]\u0138\3\2\2\2_\u013b\3\2\2\2a"+
		"\u013d\3\2\2\2c\u014b\3\2\2\2e\u0156\3\2\2\2g\u015f\3\2\2\2il\5\27\f\2"+
		"jl\5\31\r\2ki\3\2\2\2kj\3\2\2\2l\4\3\2\2\2mn\7d\2\2no\7q\2\2op\7q\2\2"+
		"pq\7n\2\2qr\7g\2\2rs\7c\2\2st\7p\2\2t\6\3\2\2\2uv\7d\2\2vw\7t\2\2wx\7"+
		"g\2\2xy\7c\2\2yz\7m\2\2z\b\3\2\2\2{|\7e\2\2|}\7q\2\2}~\7p\2\2~\177\7v"+
		"\2\2\177\u0080\7k\2\2\u0080\u0081\7p\2\2\u0081\u0082\7w\2\2\u0082\u0083"+
		"\7g\2\2\u0083\n\3\2\2\2\u0084\u0085\7g\2\2\u0085\u0086\7n\2\2\u0086\u0087"+
		"\7u\2\2\u0087\u0088\7g\2\2\u0088\f\3\2\2\2\u0089\u008a\7h\2\2\u008a\u008b"+
		"\7q\2\2\u008b\u008c\7t\2\2\u008c\16\3\2\2\2\u008d\u008e\7k\2\2\u008e\u008f"+
		"\7h\2\2\u008f\20\3\2\2\2\u0090\u0091\7t\2\2\u0091\u0092\7g\2\2\u0092\u0093"+
		"\7v\2\2\u0093\u0094\7w\2\2\u0094\u0095\7t\2\2\u0095\u0096\7p\2\2\u0096"+
		"\22\3\2\2\2\u0097\u0098\7f\2\2\u0098\u0099\7q\2\2\u0099\24\3\2\2\2\u009a"+
		"\u009b\7y\2\2\u009b\u009c\7j\2\2\u009c\u009d\7k\2\2\u009d\u009e\7n\2\2"+
		"\u009e\u009f\7g\2\2\u009f\26\3\2\2\2\u00a0\u00a1\7v\2\2\u00a1\u00a2\7"+
		"t\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4\7g\2\2\u00a4\30\3\2\2\2\u00a5\u00a6"+
		"\7h\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8\7n\2\2\u00a8\u00a9\7u\2\2\u00a9"+
		"\u00aa\7g\2\2\u00aa\32\3\2\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad\7v\2\2\u00ad"+
		"\u00ae\7t\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7i\2\2"+
		"\u00b1\34\3\2\2\2\u00b2\u00b3\7h\2\2\u00b3\u00b4\7n\2\2\u00b4\u00b5\7"+
		"q\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7\7v\2\2\u00b7\36\3\2\2\2\u00b8\u00b9"+
		"\7k\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7v\2\2\u00bb \3\2\2\2\u00bc\u00bd"+
		"\7x\2\2\u00bd\u00be\7q\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7f\2\2\u00c0"+
		"\"\3\2\2\2\u00c1\u00c5\t\2\2\2\u00c2\u00c4\t\3\2\2\u00c3\u00c2\3\2\2\2"+
		"\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6$\3"+
		"\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00ca\t\4\2\2\u00c9\u00c8\3\2\2\2\u00ca"+
		"\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc&\3\2\2\2"+
		"\u00cd\u00d0\5)\25\2\u00ce\u00d0\5+\26\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce"+
		"\3\2\2\2\u00d0(\3\2\2\2\u00d1\u00d3\5%\23\2\u00d2\u00d1\3\2\2\2\u00d2"+
		"\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\7\60\2\2\u00d5\u00dc\5"+
		"%\23\2\u00d6\u00d7\5%\23\2\u00d7\u00d9\7\60\2\2\u00d8\u00da\5%\23\2\u00d9"+
		"\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d2\3\2"+
		"\2\2\u00db\u00d6\3\2\2\2\u00dc*\3\2\2\2\u00dd\u00e0\5)\25\2\u00de\u00e0"+
		"\5%\23\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1"+
		"\u00e3\t\5\2\2\u00e2\u00e4\t\6\2\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2"+
		"\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\5%\23\2\u00e6,\3\2\2\2\u00e7\u00eb"+
		"\7$\2\2\u00e8\u00ea\13\2\2\2\u00e9\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb"+
		"\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2"+
		"\2\2\u00ee\u00ef\7^\2\2\u00ef\u00f3\n\7\2\2\u00f0\u00f2\13\2\2\2\u00f1"+
		"\u00f0\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f3\u00f1\3\2"+
		"\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f6\u00f7\b\27\2\2\u00f7"+
		".\3\2\2\2\u00f8\u00fc\7$\2\2\u00f9\u00fb\n\b\2\2\u00fa\u00f9\3\2\2\2\u00fb"+
		"\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2"+
		"\2\2\u00fe\u00fc\3\2\2\2\u00ff\u0100\7$\2\2\u0100\u0101\b\30\3\2\u0101"+
		"\60\3\2\2\2\u0102\u0103\7*\2\2\u0103\62\3\2\2\2\u0104\u0105\7+\2\2\u0105"+
		"\64\3\2\2\2\u0106\u0107\7}\2\2\u0107\66\3\2\2\2\u0108\u0109\7\177\2\2"+
		"\u01098\3\2\2\2\u010a\u010b\7]\2\2\u010b:\3\2\2\2\u010c\u010d\7_\2\2\u010d"+
		"<\3\2\2\2\u010e\u010f\7=\2\2\u010f>\3\2\2\2\u0110\u0111\7.\2\2\u0111@"+
		"\3\2\2\2\u0112\u0114\t\t\2\2\u0113\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115"+
		"\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0118\b!"+
		"\4\2\u0118B\3\2\2\2\u0119\u011a\7-\2\2\u011aD\3\2\2\2\u011b\u011c\7/\2"+
		"\2\u011cF\3\2\2\2\u011d\u011e\7,\2\2\u011eH\3\2\2\2\u011f\u0120\7\61\2"+
		"\2\u0120J\3\2\2\2\u0121\u0122\7\'\2\2\u0122L\3\2\2\2\u0123\u0124\7#\2"+
		"\2\u0124N\3\2\2\2\u0125\u0126\7~\2\2\u0126\u0127\7~\2\2\u0127P\3\2\2\2"+
		"\u0128\u0129\7(\2\2\u0129\u012a\7(\2\2\u012aR\3\2\2\2\u012b\u012c\7#\2"+
		"\2\u012c\u012d\7?\2\2\u012dT\3\2\2\2\u012e\u012f\7?\2\2\u012f\u0130\7"+
		"?\2\2\u0130V\3\2\2\2\u0131\u0132\7>\2\2\u0132X\3\2\2\2\u0133\u0134\7@"+
		"\2\2\u0134Z\3\2\2\2\u0135\u0136\7>\2\2\u0136\u0137\7?\2\2\u0137\\\3\2"+
		"\2\2\u0138\u0139\7@\2\2\u0139\u013a\7?\2\2\u013a^\3\2\2\2\u013b\u013c"+
		"\7?\2\2\u013c`\3\2\2\2\u013d\u013e\7\61\2\2\u013e\u013f\7,\2\2\u013f\u0143"+
		"\3\2\2\2\u0140\u0142\13\2\2\2\u0141\u0140\3\2\2\2\u0142\u0145\3\2\2\2"+
		"\u0143\u0144\3\2\2\2\u0143\u0141\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143"+
		"\3\2\2\2\u0146\u0147\7,\2\2\u0147\u0148\7\61\2\2\u0148\u0149\3\2\2\2\u0149"+
		"\u014a\b\61\4\2\u014ab\3\2\2\2\u014b\u014c\7\61\2\2\u014c\u014d\7\61\2"+
		"\2\u014d\u0151\3\2\2\2\u014e\u0150\n\n\2\2\u014f\u014e\3\2\2\2\u0150\u0153"+
		"\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0154\3\2\2\2\u0153"+
		"\u0151\3\2\2\2\u0154\u0155\b\62\4\2\u0155d\3\2\2\2\u0156\u015a\7$\2\2"+
		"\u0157\u0159\n\b\2\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158"+
		"\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015d"+
		"\u015e\b\63\5\2\u015ef\3\2\2\2\u015f\u0160\13\2\2\2\u0160h\3\2\2\2\23"+
		"\2k\u00c5\u00cb\u00cf\u00d2\u00d9\u00db\u00df\u00e3\u00eb\u00f3\u00fc"+
		"\u0115\u0143\u0151\u015a\6\3\27\2\3\30\3\b\2\2\3\63\4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}