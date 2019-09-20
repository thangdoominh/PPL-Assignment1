// Generated from MC.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class MCParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, PRITYPE=3, VOIDTYPE=4, If=5, Else=6, For=7, Do=8, While=9, 
		Break=10, Continue=11, Return=12, Put=13, Ln=14, Get=15, ADD=16, MUL=17, 
		LOGICNOT=18, LOGICOR=19, NOTEQ=20, LESS=21, LESSEQ=22, AS=23, SUB=24, 
		DIV=25, MOD=26, LOGICAND=27, EQ=28, GREATER=29, GREATEREQ=30, LS=31, RS=32, 
		LP=33, RP=34, LB=35, RB=36, SEMI=37, COMMA=38, ID=39, INTLIT=40, FLOATLIT=41, 
		BOOLEANLIT=42, STRINGLIT=43, LINECOMMENT=44, BLOCKCOMMENT=45, WS=46, ERROR_CHAR=47, 
		UNCLOSE_STRING=48, ILLEGAL_ESCAPE=49;
	public static final int
		RULE_prog = 0, RULE_declar = 1, RULE_vardeclar = 2, RULE_variable = 3, 
		RULE_funcdeclar = 4, RULE_para = 5, RULE_types = 6, RULE_array_type = 7, 
		RULE_array_pointer_type = 8, RULE_input_apt = 9, RULE_output_apt = 10, 
		RULE_expr = 11, RULE_operands = 12, RULE_ele_array = 13, RULE_function_call = 14, 
		RULE_staments = 15, RULE_if_st = 16, RULE_for_st = 17, RULE_do_while = 18, 
		RULE_break_st = 19, RULE_continue_st = 20, RULE_return_st = 21, RULE_expression = 22, 
		RULE_block = 23, RULE_special_fuction = 24;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "declar", "vardeclar", "variable", "funcdeclar", "para", "types", 
			"array_type", "array_pointer_type", "input_apt", "output_apt", "expr", 
			"operands", "ele_array", "function_call", "staments", "if_st", "for_st", 
			"do_while", "break_st", "continue_st", "return_st", "expression", "block", 
			"special_fuction"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'put'", "'get'", null, null, null, null, null, null, null, null, 
			null, null, null, "'Ln'", null, "'+'", "'*'", "'!'", "'||'", "'!='", 
			"'<'", "'<='", "'='", "'-'", "'/'", "'%'", "'&&'", "'=='", "'>'", "'>='", 
			"'['", "']'", "'{'", "'}'", "'('", "')'", "';'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "PRITYPE", "VOIDTYPE", "If", "Else", "For", "Do", "While", 
			"Break", "Continue", "Return", "Put", "Ln", "Get", "ADD", "MUL", "LOGICNOT", 
			"LOGICOR", "NOTEQ", "LESS", "LESSEQ", "AS", "SUB", "DIV", "MOD", "LOGICAND", 
			"EQ", "GREATER", "GREATEREQ", "LS", "RS", "LP", "RP", "LB", "RB", "SEMI", 
			"COMMA", "ID", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRINGLIT", "LINECOMMENT", 
			"BLOCKCOMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE"
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
	public String getGrammarFileName() { return "MC.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MCParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<DeclarContext> declar() {
			return getRuleContexts(DeclarContext.class);
		}
		public DeclarContext declar(int i) {
			return getRuleContext(DeclarContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(50);
				declar();
				}
				}
				setState(53); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==PRITYPE || _la==VOIDTYPE );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarContext extends ParserRuleContext {
		public VardeclarContext vardeclar() {
			return getRuleContext(VardeclarContext.class,0);
		}
		public FuncdeclarContext funcdeclar() {
			return getRuleContext(FuncdeclarContext.class,0);
		}
		public DeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterDeclar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitDeclar(this);
		}
	}

	public final DeclarContext declar() throws RecognitionException {
		DeclarContext _localctx = new DeclarContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declar);
		try {
			setState(57);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(55);
				vardeclar();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(56);
				funcdeclar();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclarContext extends ParserRuleContext {
		public TerminalNode PRITYPE() { return getToken(MCParser.PRITYPE, 0); }
		public List<VariableContext> variable() {
			return getRuleContexts(VariableContext.class);
		}
		public VariableContext variable(int i) {
			return getRuleContext(VariableContext.class,i);
		}
		public TerminalNode SEMI() { return getToken(MCParser.SEMI, 0); }
		public List<TerminalNode> COMMA() { return getTokens(MCParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MCParser.COMMA, i);
		}
		public VardeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardeclar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterVardeclar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitVardeclar(this);
		}
	}

	public final VardeclarContext vardeclar() throws RecognitionException {
		VardeclarContext _localctx = new VardeclarContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vardeclar);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(PRITYPE);
			setState(60);
			variable();
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(61);
				match(COMMA);
				setState(62);
				variable();
				}
				}
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(68);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LS() { return getToken(MCParser.LS, 0); }
		public TerminalNode INTLIT() { return getToken(MCParser.INTLIT, 0); }
		public TerminalNode RS() { return getToken(MCParser.RS, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_variable);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(ID);
			setState(74);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LS) {
				{
				setState(71);
				match(LS);
				setState(72);
				match(INTLIT);
				setState(73);
				match(RS);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdeclarContext extends ParserRuleContext {
		public TypesContext types() {
			return getRuleContext(TypesContext.class,0);
		}
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LB() { return getToken(MCParser.LB, 0); }
		public TerminalNode RB() { return getToken(MCParser.RB, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public List<ParaContext> para() {
			return getRuleContexts(ParaContext.class);
		}
		public ParaContext para(int i) {
			return getRuleContext(ParaContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MCParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MCParser.COMMA, i);
		}
		public FuncdeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdeclar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterFuncdeclar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitFuncdeclar(this);
		}
	}

	public final FuncdeclarContext funcdeclar() throws RecognitionException {
		FuncdeclarContext _localctx = new FuncdeclarContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_funcdeclar);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			types();
			setState(77);
			match(ID);
			setState(78);
			match(LB);
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PRITYPE) {
				{
				setState(79);
				para();
				setState(84);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(80);
					match(COMMA);
					setState(81);
					para();
					}
					}
					setState(86);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(89);
			match(RB);
			setState(90);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParaContext extends ParserRuleContext {
		public TerminalNode PRITYPE() { return getToken(MCParser.PRITYPE, 0); }
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LS() { return getToken(MCParser.LS, 0); }
		public TerminalNode INTLIT() { return getToken(MCParser.INTLIT, 0); }
		public TerminalNode RS() { return getToken(MCParser.RS, 0); }
		public ParaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterPara(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitPara(this);
		}
	}

	public final ParaContext para() throws RecognitionException {
		ParaContext _localctx = new ParaContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_para);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			match(PRITYPE);
			setState(93);
			match(ID);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LS) {
				{
				setState(94);
				match(LS);
				setState(95);
				match(INTLIT);
				setState(96);
				match(RS);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypesContext extends ParserRuleContext {
		public TerminalNode PRITYPE() { return getToken(MCParser.PRITYPE, 0); }
		public TerminalNode VOIDTYPE() { return getToken(MCParser.VOIDTYPE, 0); }
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Array_pointer_typeContext array_pointer_type() {
			return getRuleContext(Array_pointer_typeContext.class,0);
		}
		public TypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_types; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterTypes(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitTypes(this);
		}
	}

	public final TypesContext types() throws RecognitionException {
		TypesContext _localctx = new TypesContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_types);
		try {
			setState(103);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(99);
				match(PRITYPE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(100);
				match(VOIDTYPE);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(101);
				array_type();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(102);
				array_pointer_type();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_typeContext extends ParserRuleContext {
		public TerminalNode PRITYPE() { return getToken(MCParser.PRITYPE, 0); }
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LS() { return getToken(MCParser.LS, 0); }
		public TerminalNode INTLIT() { return getToken(MCParser.INTLIT, 0); }
		public TerminalNode RS() { return getToken(MCParser.RS, 0); }
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterArray_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitArray_type(this);
		}
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_array_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(105);
			match(PRITYPE);
			setState(106);
			match(ID);
			setState(107);
			match(LS);
			setState(108);
			match(INTLIT);
			setState(109);
			match(RS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_pointer_typeContext extends ParserRuleContext {
		public Input_aptContext input_apt() {
			return getRuleContext(Input_aptContext.class,0);
		}
		public Output_aptContext output_apt() {
			return getRuleContext(Output_aptContext.class,0);
		}
		public Array_pointer_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_pointer_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterArray_pointer_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitArray_pointer_type(this);
		}
	}

	public final Array_pointer_typeContext array_pointer_type() throws RecognitionException {
		Array_pointer_typeContext _localctx = new Array_pointer_typeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_array_pointer_type);
		try {
			setState(113);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				input_apt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(112);
				output_apt();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Input_aptContext extends ParserRuleContext {
		public TerminalNode PRITYPE() { return getToken(MCParser.PRITYPE, 0); }
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LS() { return getToken(MCParser.LS, 0); }
		public TerminalNode RS() { return getToken(MCParser.RS, 0); }
		public Input_aptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_input_apt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterInput_apt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitInput_apt(this);
		}
	}

	public final Input_aptContext input_apt() throws RecognitionException {
		Input_aptContext _localctx = new Input_aptContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_input_apt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(PRITYPE);
			setState(116);
			match(ID);
			setState(117);
			match(LS);
			setState(118);
			match(RS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Output_aptContext extends ParserRuleContext {
		public TerminalNode PRITYPE() { return getToken(MCParser.PRITYPE, 0); }
		public TerminalNode LS() { return getToken(MCParser.LS, 0); }
		public TerminalNode RS() { return getToken(MCParser.RS, 0); }
		public Output_aptContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_output_apt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterOutput_apt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitOutput_apt(this);
		}
	}

	public final Output_aptContext output_apt() throws RecognitionException {
		Output_aptContext _localctx = new Output_aptContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_output_apt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(PRITYPE);
			setState(121);
			match(LS);
			setState(122);
			match(RS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(MCParser.LB, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode RB() { return getToken(MCParser.RB, 0); }
		public TerminalNode LS() { return getToken(MCParser.LS, 0); }
		public List<OperandsContext> operands() {
			return getRuleContexts(OperandsContext.class);
		}
		public OperandsContext operands(int i) {
			return getRuleContext(OperandsContext.class,i);
		}
		public TerminalNode RS() { return getToken(MCParser.RS, 0); }
		public TerminalNode SUB() { return getToken(MCParser.SUB, 0); }
		public TerminalNode LOGICNOT() { return getToken(MCParser.LOGICNOT, 0); }
		public TerminalNode LESS() { return getToken(MCParser.LESS, 0); }
		public TerminalNode LESSEQ() { return getToken(MCParser.LESSEQ, 0); }
		public TerminalNode GREATER() { return getToken(MCParser.GREATER, 0); }
		public TerminalNode GREATEREQ() { return getToken(MCParser.GREATEREQ, 0); }
		public TerminalNode MUL() { return getToken(MCParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(MCParser.DIV, 0); }
		public TerminalNode MOD() { return getToken(MCParser.MOD, 0); }
		public TerminalNode ADD() { return getToken(MCParser.ADD, 0); }
		public TerminalNode LOGICAND() { return getToken(MCParser.LOGICAND, 0); }
		public TerminalNode LOGICOR() { return getToken(MCParser.LOGICOR, 0); }
		public TerminalNode AS() { return getToken(MCParser.AS, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(125);
				match(LB);
				setState(126);
				expr(0);
				setState(127);
				match(RB);
				}
				break;
			case 2:
				{
				setState(129);
				match(LS);
				setState(130);
				operands();
				setState(131);
				match(RS);
				}
				break;
			case 3:
				{
				setState(133);
				_la = _input.LA(1);
				if ( !(_la==LOGICNOT || _la==SUB) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(134);
				expr(8);
				}
				break;
			case 4:
				{
				setState(135);
				operands();
				setState(136);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LESS) | (1L << LESSEQ) | (1L << GREATER) | (1L << GREATEREQ))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(137);
				operands();
				}
				break;
			case 5:
				{
				setState(139);
				operands();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(159);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(157);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(142);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(143);
						_la = _input.LA(1);
						if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << DIV) | (1L << MOD))) != 0)) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(144);
						expr(8);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(145);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(146);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(147);
						expr(7);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(148);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(149);
						match(LOGICAND);
						setState(150);
						expr(5);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(151);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(152);
						match(LOGICOR);
						setState(153);
						expr(4);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(154);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(155);
						match(AS);
						setState(156);
						expr(2);
						}
						break;
					}
					} 
				}
				setState(161);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class OperandsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode INTLIT() { return getToken(MCParser.INTLIT, 0); }
		public Ele_arrayContext ele_array() {
			return getRuleContext(Ele_arrayContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public OperandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operands; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterOperands(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitOperands(this);
		}
	}

	public final OperandsContext operands() throws RecognitionException {
		OperandsContext _localctx = new OperandsContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_operands);
		try {
			setState(166);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(162);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(163);
				match(INTLIT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(164);
				ele_array();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(165);
				function_call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Ele_arrayContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LS() { return getToken(MCParser.LS, 0); }
		public TerminalNode INTLIT() { return getToken(MCParser.INTLIT, 0); }
		public TerminalNode RS() { return getToken(MCParser.RS, 0); }
		public Ele_arrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ele_array; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterEle_array(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitEle_array(this);
		}
	}

	public final Ele_arrayContext ele_array() throws RecognitionException {
		Ele_arrayContext _localctx = new Ele_arrayContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_ele_array);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(ID);
			setState(169);
			match(LS);
			setState(170);
			match(INTLIT);
			setState(171);
			match(RS);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MCParser.ID, 0); }
		public TerminalNode LB() { return getToken(MCParser.LB, 0); }
		public TerminalNode RB() { return getToken(MCParser.RB, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(MCParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(MCParser.COMMA, i);
		}
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterFunction_call(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitFunction_call(this);
		}
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_function_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(173);
			match(ID);
			setState(174);
			match(LB);
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LOGICNOT) | (1L << SUB) | (1L << LS) | (1L << LB) | (1L << ID) | (1L << INTLIT))) != 0)) {
				{
				setState(175);
				expr(0);
				setState(180);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(176);
					match(COMMA);
					setState(177);
					expr(0);
					}
					}
					setState(182);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(185);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StamentsContext extends ParserRuleContext {
		public If_stContext if_st() {
			return getRuleContext(If_stContext.class,0);
		}
		public For_stContext for_st() {
			return getRuleContext(For_stContext.class,0);
		}
		public Do_whileContext do_while() {
			return getRuleContext(Do_whileContext.class,0);
		}
		public Break_stContext break_st() {
			return getRuleContext(Break_stContext.class,0);
		}
		public Continue_stContext continue_st() {
			return getRuleContext(Continue_stContext.class,0);
		}
		public Return_stContext return_st() {
			return getRuleContext(Return_stContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public StamentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_staments; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterStaments(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitStaments(this);
		}
	}

	public final StamentsContext staments() throws RecognitionException {
		StamentsContext _localctx = new StamentsContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_staments);
		try {
			setState(195);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case If:
				enterOuterAlt(_localctx, 1);
				{
				setState(187);
				if_st();
				}
				break;
			case For:
				enterOuterAlt(_localctx, 2);
				{
				setState(188);
				for_st();
				}
				break;
			case Do:
				enterOuterAlt(_localctx, 3);
				{
				setState(189);
				do_while();
				}
				break;
			case Break:
				enterOuterAlt(_localctx, 4);
				{
				setState(190);
				break_st();
				}
				break;
			case Continue:
				enterOuterAlt(_localctx, 5);
				{
				setState(191);
				continue_st();
				}
				break;
			case Return:
				enterOuterAlt(_localctx, 6);
				{
				setState(192);
				return_st();
				}
				break;
			case LOGICNOT:
			case SUB:
			case LS:
			case LB:
			case ID:
			case INTLIT:
				enterOuterAlt(_localctx, 7);
				{
				setState(193);
				expression();
				}
				break;
			case LP:
				enterOuterAlt(_localctx, 8);
				{
				setState(194);
				block();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stContext extends ParserRuleContext {
		public TerminalNode If() { return getToken(MCParser.If, 0); }
		public TerminalNode LB() { return getToken(MCParser.LB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RB() { return getToken(MCParser.RB, 0); }
		public List<StamentsContext> staments() {
			return getRuleContexts(StamentsContext.class);
		}
		public StamentsContext staments(int i) {
			return getRuleContext(StamentsContext.class,i);
		}
		public TerminalNode Else() { return getToken(MCParser.Else, 0); }
		public If_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterIf_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitIf_st(this);
		}
	}

	public final If_stContext if_st() throws RecognitionException {
		If_stContext _localctx = new If_stContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_if_st);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(197);
			match(If);
			setState(198);
			match(LB);
			setState(199);
			expr(0);
			setState(200);
			match(RB);
			setState(201);
			staments();
			setState(204);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(202);
				match(Else);
				setState(203);
				staments();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_stContext extends ParserRuleContext {
		public TerminalNode For() { return getToken(MCParser.For, 0); }
		public TerminalNode LB() { return getToken(MCParser.LB, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(MCParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(MCParser.SEMI, i);
		}
		public TerminalNode RB() { return getToken(MCParser.RB, 0); }
		public StamentsContext staments() {
			return getRuleContext(StamentsContext.class,0);
		}
		public For_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterFor_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitFor_st(this);
		}
	}

	public final For_stContext for_st() throws RecognitionException {
		For_stContext _localctx = new For_stContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_for_st);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(206);
			match(For);
			setState(207);
			match(LB);
			setState(208);
			expr(0);
			setState(209);
			match(SEMI);
			setState(210);
			expr(0);
			setState(211);
			match(SEMI);
			setState(212);
			expr(0);
			setState(213);
			match(RB);
			setState(214);
			staments();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Do_whileContext extends ParserRuleContext {
		public TerminalNode Do() { return getToken(MCParser.Do, 0); }
		public StamentsContext staments() {
			return getRuleContext(StamentsContext.class,0);
		}
		public TerminalNode While() { return getToken(MCParser.While, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MCParser.SEMI, 0); }
		public Do_whileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterDo_while(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitDo_while(this);
		}
	}

	public final Do_whileContext do_while() throws RecognitionException {
		Do_whileContext _localctx = new Do_whileContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_do_while);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			match(Do);
			setState(217);
			staments();
			setState(218);
			match(While);
			setState(219);
			expr(0);
			setState(220);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_stContext extends ParserRuleContext {
		public TerminalNode Break() { return getToken(MCParser.Break, 0); }
		public TerminalNode SEMI() { return getToken(MCParser.SEMI, 0); }
		public Break_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterBreak_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitBreak_st(this);
		}
	}

	public final Break_stContext break_st() throws RecognitionException {
		Break_stContext _localctx = new Break_stContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_break_st);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(222);
			match(Break);
			setState(223);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_stContext extends ParserRuleContext {
		public TerminalNode Continue() { return getToken(MCParser.Continue, 0); }
		public TerminalNode SEMI() { return getToken(MCParser.SEMI, 0); }
		public Continue_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterContinue_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitContinue_st(this);
		}
	}

	public final Continue_stContext continue_st() throws RecognitionException {
		Continue_stContext _localctx = new Continue_stContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_continue_st);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(Continue);
			setState(226);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_stContext extends ParserRuleContext {
		public TerminalNode Return() { return getToken(MCParser.Return, 0); }
		public TerminalNode SEMI() { return getToken(MCParser.SEMI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Return_stContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_st; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterReturn_st(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitReturn_st(this);
		}
	}

	public final Return_stContext return_st() throws RecognitionException {
		Return_stContext _localctx = new Return_stContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_return_st);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(Return);
			setState(230);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LOGICNOT) | (1L << SUB) | (1L << LS) | (1L << LB) | (1L << ID) | (1L << INTLIT))) != 0)) {
				{
				setState(229);
				expr(0);
				}
			}

			setState(232);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(MCParser.SEMI, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			expr(0);
			setState(235);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(MCParser.LP, 0); }
		public TerminalNode RP() { return getToken(MCParser.RP, 0); }
		public List<StamentsContext> staments() {
			return getRuleContexts(StamentsContext.class);
		}
		public StamentsContext staments(int i) {
			return getRuleContext(StamentsContext.class,i);
		}
		public List<VardeclarContext> vardeclar() {
			return getRuleContexts(VardeclarContext.class);
		}
		public VardeclarContext vardeclar(int i) {
			return getRuleContext(VardeclarContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(237);
			match(LP);
			setState(242);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRITYPE) | (1L << If) | (1L << For) | (1L << Do) | (1L << Break) | (1L << Continue) | (1L << Return) | (1L << LOGICNOT) | (1L << SUB) | (1L << LS) | (1L << LP) | (1L << LB) | (1L << ID) | (1L << INTLIT))) != 0)) {
				{
				setState(240);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case If:
				case For:
				case Do:
				case Break:
				case Continue:
				case Return:
				case LOGICNOT:
				case SUB:
				case LS:
				case LP:
				case LB:
				case ID:
				case INTLIT:
					{
					setState(238);
					staments();
					}
					break;
				case PRITYPE:
					{
					setState(239);
					vardeclar();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(244);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(245);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Special_fuctionContext extends ParserRuleContext {
		public TerminalNode Put() { return getToken(MCParser.Put, 0); }
		public TerminalNode LB() { return getToken(MCParser.LB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RB() { return getToken(MCParser.RB, 0); }
		public TerminalNode Ln() { return getToken(MCParser.Ln, 0); }
		public TerminalNode Get() { return getToken(MCParser.Get, 0); }
		public Special_fuctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_special_fuction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).enterSpecial_fuction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MCListener ) ((MCListener)listener).exitSpecial_fuction(this);
		}
	}

	public final Special_fuctionContext special_fuction() throws RecognitionException {
		Special_fuctionContext _localctx = new Special_fuctionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_special_fuction);
		try {
			setState(260);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(247);
				match(T__0);
				{
				setState(248);
				match(Put);
				setState(249);
				match(LB);
				setState(250);
				expr(0);
				setState(251);
				match(RB);
				}
				}
				break;
			case Ln:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(253);
				match(Ln);
				setState(254);
				match(LB);
				setState(255);
				match(RB);
				}
				}
				break;
			case T__1:
				enterOuterAlt(_localctx, 3);
				{
				setState(256);
				match(T__1);
				setState(257);
				match(Get);
				setState(258);
				match(LB);
				setState(259);
				match(RB);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 11:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 4);
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63\u0109\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\3\2\6\2\66\n\2\r\2\16\2\67\3\3\3\3\5\3<\n\3\3\4\3\4\3\4\3\4"+
		"\7\4B\n\4\f\4\16\4E\13\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5M\n\5\3\6\3\6\3\6"+
		"\3\6\3\6\3\6\7\6U\n\6\f\6\16\6X\13\6\5\6Z\n\6\3\6\3\6\3\6\3\7\3\7\3\7"+
		"\3\7\3\7\5\7d\n\7\3\b\3\b\3\b\3\b\5\bj\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n"+
		"\3\n\5\nt\n\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u008f\n\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u00a0\n\r\f\r"+
		"\16\r\u00a3\13\r\3\16\3\16\3\16\3\16\5\16\u00a9\n\16\3\17\3\17\3\17\3"+
		"\17\3\17\3\20\3\20\3\20\3\20\3\20\7\20\u00b5\n\20\f\20\16\20\u00b8\13"+
		"\20\5\20\u00ba\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\5\21\u00c6\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00cf\n\22\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3"+
		"\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\5\27\u00e9\n\27\3\27"+
		"\3\27\3\30\3\30\3\30\3\31\3\31\3\31\7\31\u00f3\n\31\f\31\16\31\u00f6\13"+
		"\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3"+
		"\32\3\32\5\32\u0107\n\32\3\32\2\3\30\33\2\4\6\b\n\f\16\20\22\24\26\30"+
		"\32\34\36 \"$&(*,.\60\62\2\6\4\2\24\24\32\32\4\2\27\30\37 \4\2\23\23\33"+
		"\34\4\2\22\22\32\32\2\u0115\2\65\3\2\2\2\4;\3\2\2\2\6=\3\2\2\2\bH\3\2"+
		"\2\2\nN\3\2\2\2\f^\3\2\2\2\16i\3\2\2\2\20k\3\2\2\2\22s\3\2\2\2\24u\3\2"+
		"\2\2\26z\3\2\2\2\30\u008e\3\2\2\2\32\u00a8\3\2\2\2\34\u00aa\3\2\2\2\36"+
		"\u00af\3\2\2\2 \u00c5\3\2\2\2\"\u00c7\3\2\2\2$\u00d0\3\2\2\2&\u00da\3"+
		"\2\2\2(\u00e0\3\2\2\2*\u00e3\3\2\2\2,\u00e6\3\2\2\2.\u00ec\3\2\2\2\60"+
		"\u00ef\3\2\2\2\62\u0106\3\2\2\2\64\66\5\4\3\2\65\64\3\2\2\2\66\67\3\2"+
		"\2\2\67\65\3\2\2\2\678\3\2\2\28\3\3\2\2\29<\5\6\4\2:<\5\n\6\2;9\3\2\2"+
		"\2;:\3\2\2\2<\5\3\2\2\2=>\7\5\2\2>C\5\b\5\2?@\7(\2\2@B\5\b\5\2A?\3\2\2"+
		"\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2EC\3\2\2\2FG\7\'\2\2G\7\3\2"+
		"\2\2HL\7)\2\2IJ\7!\2\2JK\7*\2\2KM\7\"\2\2LI\3\2\2\2LM\3\2\2\2M\t\3\2\2"+
		"\2NO\5\16\b\2OP\7)\2\2PY\7%\2\2QV\5\f\7\2RS\7(\2\2SU\5\f\7\2TR\3\2\2\2"+
		"UX\3\2\2\2VT\3\2\2\2VW\3\2\2\2WZ\3\2\2\2XV\3\2\2\2YQ\3\2\2\2YZ\3\2\2\2"+
		"Z[\3\2\2\2[\\\7&\2\2\\]\5\60\31\2]\13\3\2\2\2^_\7\5\2\2_c\7)\2\2`a\7!"+
		"\2\2ab\7*\2\2bd\7\"\2\2c`\3\2\2\2cd\3\2\2\2d\r\3\2\2\2ej\7\5\2\2fj\7\6"+
		"\2\2gj\5\20\t\2hj\5\22\n\2ie\3\2\2\2if\3\2\2\2ig\3\2\2\2ih\3\2\2\2j\17"+
		"\3\2\2\2kl\7\5\2\2lm\7)\2\2mn\7!\2\2no\7*\2\2op\7\"\2\2p\21\3\2\2\2qt"+
		"\5\24\13\2rt\5\26\f\2sq\3\2\2\2sr\3\2\2\2t\23\3\2\2\2uv\7\5\2\2vw\7)\2"+
		"\2wx\7!\2\2xy\7\"\2\2y\25\3\2\2\2z{\7\5\2\2{|\7!\2\2|}\7\"\2\2}\27\3\2"+
		"\2\2~\177\b\r\1\2\177\u0080\7%\2\2\u0080\u0081\5\30\r\2\u0081\u0082\7"+
		"&\2\2\u0082\u008f\3\2\2\2\u0083\u0084\7!\2\2\u0084\u0085\5\32\16\2\u0085"+
		"\u0086\7\"\2\2\u0086\u008f\3\2\2\2\u0087\u0088\t\2\2\2\u0088\u008f\5\30"+
		"\r\n\u0089\u008a\5\32\16\2\u008a\u008b\t\3\2\2\u008b\u008c\5\32\16\2\u008c"+
		"\u008f\3\2\2\2\u008d\u008f\5\32\16\2\u008e~\3\2\2\2\u008e\u0083\3\2\2"+
		"\2\u008e\u0087\3\2\2\2\u008e\u0089\3\2\2\2\u008e\u008d\3\2\2\2\u008f\u00a1"+
		"\3\2\2\2\u0090\u0091\f\t\2\2\u0091\u0092\t\4\2\2\u0092\u00a0\5\30\r\n"+
		"\u0093\u0094\f\b\2\2\u0094\u0095\t\5\2\2\u0095\u00a0\5\30\r\t\u0096\u0097"+
		"\f\6\2\2\u0097\u0098\7\35\2\2\u0098\u00a0\5\30\r\7\u0099\u009a\f\5\2\2"+
		"\u009a\u009b\7\25\2\2\u009b\u00a0\5\30\r\6\u009c\u009d\f\4\2\2\u009d\u009e"+
		"\7\31\2\2\u009e\u00a0\5\30\r\4\u009f\u0090\3\2\2\2\u009f\u0093\3\2\2\2"+
		"\u009f\u0096\3\2\2\2\u009f\u0099\3\2\2\2\u009f\u009c\3\2\2\2\u00a0\u00a3"+
		"\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\31\3\2\2\2\u00a3"+
		"\u00a1\3\2\2\2\u00a4\u00a9\7)\2\2\u00a5\u00a9\7*\2\2\u00a6\u00a9\5\34"+
		"\17\2\u00a7\u00a9\5\36\20\2\u00a8\u00a4\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8"+
		"\u00a6\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\33\3\2\2\2\u00aa\u00ab\7)\2\2"+
		"\u00ab\u00ac\7!\2\2\u00ac\u00ad\7*\2\2\u00ad\u00ae\7\"\2\2\u00ae\35\3"+
		"\2\2\2\u00af\u00b0\7)\2\2\u00b0\u00b9\7%\2\2\u00b1\u00b6\5\30\r\2\u00b2"+
		"\u00b3\7(\2\2\u00b3\u00b5\5\30\r\2\u00b4\u00b2\3\2\2\2\u00b5\u00b8\3\2"+
		"\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8"+
		"\u00b6\3\2\2\2\u00b9\u00b1\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2"+
		"\2\2\u00bb\u00bc\7&\2\2\u00bc\37\3\2\2\2\u00bd\u00c6\5\"\22\2\u00be\u00c6"+
		"\5$\23\2\u00bf\u00c6\5&\24\2\u00c0\u00c6\5(\25\2\u00c1\u00c6\5*\26\2\u00c2"+
		"\u00c6\5,\27\2\u00c3\u00c6\5.\30\2\u00c4\u00c6\5\60\31\2\u00c5\u00bd\3"+
		"\2\2\2\u00c5\u00be\3\2\2\2\u00c5\u00bf\3\2\2\2\u00c5\u00c0\3\2\2\2\u00c5"+
		"\u00c1\3\2\2\2\u00c5\u00c2\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c4\3\2"+
		"\2\2\u00c6!\3\2\2\2\u00c7\u00c8\7\7\2\2\u00c8\u00c9\7%\2\2\u00c9\u00ca"+
		"\5\30\r\2\u00ca\u00cb\7&\2\2\u00cb\u00ce\5 \21\2\u00cc\u00cd\7\b\2\2\u00cd"+
		"\u00cf\5 \21\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf#\3\2\2\2"+
		"\u00d0\u00d1\7\t\2\2\u00d1\u00d2\7%\2\2\u00d2\u00d3\5\30\r\2\u00d3\u00d4"+
		"\7\'\2\2\u00d4\u00d5\5\30\r\2\u00d5\u00d6\7\'\2\2\u00d6\u00d7\5\30\r\2"+
		"\u00d7\u00d8\7&\2\2\u00d8\u00d9\5 \21\2\u00d9%\3\2\2\2\u00da\u00db\7\n"+
		"\2\2\u00db\u00dc\5 \21\2\u00dc\u00dd\7\13\2\2\u00dd\u00de\5\30\r\2\u00de"+
		"\u00df\7\'\2\2\u00df\'\3\2\2\2\u00e0\u00e1\7\f\2\2\u00e1\u00e2\7\'\2\2"+
		"\u00e2)\3\2\2\2\u00e3\u00e4\7\r\2\2\u00e4\u00e5\7\'\2\2\u00e5+\3\2\2\2"+
		"\u00e6\u00e8\7\16\2\2\u00e7\u00e9\5\30\r\2\u00e8\u00e7\3\2\2\2\u00e8\u00e9"+
		"\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\7\'\2\2\u00eb-\3\2\2\2\u00ec"+
		"\u00ed\5\30\r\2\u00ed\u00ee\7\'\2\2\u00ee/\3\2\2\2\u00ef\u00f4\7#\2\2"+
		"\u00f0\u00f3\5 \21\2\u00f1\u00f3\5\6\4\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1"+
		"\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5"+
		"\u00f7\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\7$\2\2\u00f8\61\3\2\2\2"+
		"\u00f9\u00fa\7\3\2\2\u00fa\u00fb\7\17\2\2\u00fb\u00fc\7%\2\2\u00fc\u00fd"+
		"\5\30\r\2\u00fd\u00fe\7&\2\2\u00fe\u0107\3\2\2\2\u00ff\u0100\7\20\2\2"+
		"\u0100\u0101\7%\2\2\u0101\u0107\7&\2\2\u0102\u0103\7\4\2\2\u0103\u0104"+
		"\7\21\2\2\u0104\u0105\7%\2\2\u0105\u0107\7&\2\2\u0106\u00f9\3\2\2\2\u0106"+
		"\u00ff\3\2\2\2\u0106\u0102\3\2\2\2\u0107\63\3\2\2\2\27\67;CLVYcis\u008e"+
		"\u009f\u00a1\u00a8\u00b6\u00b9\u00c5\u00ce\u00e8\u00f2\u00f4\u0106";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}