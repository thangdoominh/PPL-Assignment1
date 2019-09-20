// Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/reference/A.Sang-K15/MC.g4 by ANTLR 4.7.2

	package mc.parser;

import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MCParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MCVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MCParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MCParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#declaration}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaration(MCParser.DeclarationContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#vardecla}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardecla(MCParser.VardeclaContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#idlist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdlist(MCParser.IdlistContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#id}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitId(MCParser.IdContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#idalone}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdalone(MCParser.IdaloneContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#idarray}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdarray(MCParser.IdarrayContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#funcdecla}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncdecla(MCParser.FuncdeclaContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#arraypointertype}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArraypointertype(MCParser.ArraypointertypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#paralist_decla}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParalist_decla(MCParser.Paralist_declaContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#paradecla}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParadecla(MCParser.ParadeclaContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(MCParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#statementpart}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatementpart(MCParser.StatementpartContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(MCParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#ifstmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfstmt(MCParser.IfstmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#dowhilestmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDowhilestmt(MCParser.DowhilestmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#forstmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForstmt(MCParser.ForstmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#breakstmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakstmt(MCParser.BreakstmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#continuestmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinuestmt(MCParser.ContinuestmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#returnstmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnstmt(MCParser.ReturnstmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#funccall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunccall(MCParser.FunccallContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#paralist_call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParalist_call(MCParser.Paralist_callContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#para_call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPara_call(MCParser.Para_callContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#expressionstmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionstmt(MCParser.ExpressionstmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(MCParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp1(MCParser.Exp1Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp2(MCParser.Exp2Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp3(MCParser.Exp3Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp4(MCParser.Exp4Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp5}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp5(MCParser.Exp5Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp6}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp6(MCParser.Exp6Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp7}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp7(MCParser.Exp7Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp8}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp8(MCParser.Exp8Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp9}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp9(MCParser.Exp9Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp10}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp10(MCParser.Exp10Context ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#operand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperand(MCParser.OperandContext ctx);
}