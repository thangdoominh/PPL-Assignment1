// Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/reference/A.Sang-K15/MC.g4 by ANTLR 4.7.2

	package mc.parser;

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MCParser}.
 */
public interface MCListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MCParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MCParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MCParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(MCParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(MCParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#vardecla}.
	 * @param ctx the parse tree
	 */
	void enterVardecla(MCParser.VardeclaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#vardecla}.
	 * @param ctx the parse tree
	 */
	void exitVardecla(MCParser.VardeclaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#idlist}.
	 * @param ctx the parse tree
	 */
	void enterIdlist(MCParser.IdlistContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#idlist}.
	 * @param ctx the parse tree
	 */
	void exitIdlist(MCParser.IdlistContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#id}.
	 * @param ctx the parse tree
	 */
	void enterId(MCParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#id}.
	 * @param ctx the parse tree
	 */
	void exitId(MCParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#idalone}.
	 * @param ctx the parse tree
	 */
	void enterIdalone(MCParser.IdaloneContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#idalone}.
	 * @param ctx the parse tree
	 */
	void exitIdalone(MCParser.IdaloneContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#idarray}.
	 * @param ctx the parse tree
	 */
	void enterIdarray(MCParser.IdarrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#idarray}.
	 * @param ctx the parse tree
	 */
	void exitIdarray(MCParser.IdarrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#funcdecla}.
	 * @param ctx the parse tree
	 */
	void enterFuncdecla(MCParser.FuncdeclaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#funcdecla}.
	 * @param ctx the parse tree
	 */
	void exitFuncdecla(MCParser.FuncdeclaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#arraypointertype}.
	 * @param ctx the parse tree
	 */
	void enterArraypointertype(MCParser.ArraypointertypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#arraypointertype}.
	 * @param ctx the parse tree
	 */
	void exitArraypointertype(MCParser.ArraypointertypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#paralist_decla}.
	 * @param ctx the parse tree
	 */
	void enterParalist_decla(MCParser.Paralist_declaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#paralist_decla}.
	 * @param ctx the parse tree
	 */
	void exitParalist_decla(MCParser.Paralist_declaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#paradecla}.
	 * @param ctx the parse tree
	 */
	void enterParadecla(MCParser.ParadeclaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#paradecla}.
	 * @param ctx the parse tree
	 */
	void exitParadecla(MCParser.ParadeclaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MCParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MCParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#statementpart}.
	 * @param ctx the parse tree
	 */
	void enterStatementpart(MCParser.StatementpartContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#statementpart}.
	 * @param ctx the parse tree
	 */
	void exitStatementpart(MCParser.StatementpartContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MCParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MCParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void enterIfstmt(MCParser.IfstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#ifstmt}.
	 * @param ctx the parse tree
	 */
	void exitIfstmt(MCParser.IfstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#dowhilestmt}.
	 * @param ctx the parse tree
	 */
	void enterDowhilestmt(MCParser.DowhilestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#dowhilestmt}.
	 * @param ctx the parse tree
	 */
	void exitDowhilestmt(MCParser.DowhilestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#forstmt}.
	 * @param ctx the parse tree
	 */
	void enterForstmt(MCParser.ForstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#forstmt}.
	 * @param ctx the parse tree
	 */
	void exitForstmt(MCParser.ForstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakstmt(MCParser.BreakstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#breakstmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakstmt(MCParser.BreakstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void enterContinuestmt(MCParser.ContinuestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#continuestmt}.
	 * @param ctx the parse tree
	 */
	void exitContinuestmt(MCParser.ContinuestmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void enterReturnstmt(MCParser.ReturnstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#returnstmt}.
	 * @param ctx the parse tree
	 */
	void exitReturnstmt(MCParser.ReturnstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#funccall}.
	 * @param ctx the parse tree
	 */
	void enterFunccall(MCParser.FunccallContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#funccall}.
	 * @param ctx the parse tree
	 */
	void exitFunccall(MCParser.FunccallContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#paralist_call}.
	 * @param ctx the parse tree
	 */
	void enterParalist_call(MCParser.Paralist_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#paralist_call}.
	 * @param ctx the parse tree
	 */
	void exitParalist_call(MCParser.Paralist_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#para_call}.
	 * @param ctx the parse tree
	 */
	void enterPara_call(MCParser.Para_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#para_call}.
	 * @param ctx the parse tree
	 */
	void exitPara_call(MCParser.Para_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#expressionstmt}.
	 * @param ctx the parse tree
	 */
	void enterExpressionstmt(MCParser.ExpressionstmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#expressionstmt}.
	 * @param ctx the parse tree
	 */
	void exitExpressionstmt(MCParser.ExpressionstmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(MCParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(MCParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp1}.
	 * @param ctx the parse tree
	 */
	void enterExp1(MCParser.Exp1Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp1}.
	 * @param ctx the parse tree
	 */
	void exitExp1(MCParser.Exp1Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp2}.
	 * @param ctx the parse tree
	 */
	void enterExp2(MCParser.Exp2Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp2}.
	 * @param ctx the parse tree
	 */
	void exitExp2(MCParser.Exp2Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp3}.
	 * @param ctx the parse tree
	 */
	void enterExp3(MCParser.Exp3Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp3}.
	 * @param ctx the parse tree
	 */
	void exitExp3(MCParser.Exp3Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp4}.
	 * @param ctx the parse tree
	 */
	void enterExp4(MCParser.Exp4Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp4}.
	 * @param ctx the parse tree
	 */
	void exitExp4(MCParser.Exp4Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp5}.
	 * @param ctx the parse tree
	 */
	void enterExp5(MCParser.Exp5Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp5}.
	 * @param ctx the parse tree
	 */
	void exitExp5(MCParser.Exp5Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp6}.
	 * @param ctx the parse tree
	 */
	void enterExp6(MCParser.Exp6Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp6}.
	 * @param ctx the parse tree
	 */
	void exitExp6(MCParser.Exp6Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp7}.
	 * @param ctx the parse tree
	 */
	void enterExp7(MCParser.Exp7Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp7}.
	 * @param ctx the parse tree
	 */
	void exitExp7(MCParser.Exp7Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp8}.
	 * @param ctx the parse tree
	 */
	void enterExp8(MCParser.Exp8Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp8}.
	 * @param ctx the parse tree
	 */
	void exitExp8(MCParser.Exp8Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp9}.
	 * @param ctx the parse tree
	 */
	void enterExp9(MCParser.Exp9Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp9}.
	 * @param ctx the parse tree
	 */
	void exitExp9(MCParser.Exp9Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#exp10}.
	 * @param ctx the parse tree
	 */
	void enterExp10(MCParser.Exp10Context ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#exp10}.
	 * @param ctx the parse tree
	 */
	void exitExp10(MCParser.Exp10Context ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#operand}.
	 * @param ctx the parse tree
	 */
	void enterOperand(MCParser.OperandContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#operand}.
	 * @param ctx the parse tree
	 */
	void exitOperand(MCParser.OperandContext ctx);
}