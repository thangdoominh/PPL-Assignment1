// Generated from MC.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MCParser}.
 */
public interface MCListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MCParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(MCParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(MCParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#declar}.
	 * @param ctx the parse tree
	 */
	void enterDeclar(MCParser.DeclarContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#declar}.
	 * @param ctx the parse tree
	 */
	void exitDeclar(MCParser.DeclarContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#vardeclar}.
	 * @param ctx the parse tree
	 */
	void enterVardeclar(MCParser.VardeclarContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#vardeclar}.
	 * @param ctx the parse tree
	 */
	void exitVardeclar(MCParser.VardeclarContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(MCParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(MCParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#funcdeclar}.
	 * @param ctx the parse tree
	 */
	void enterFuncdeclar(MCParser.FuncdeclarContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#funcdeclar}.
	 * @param ctx the parse tree
	 */
	void exitFuncdeclar(MCParser.FuncdeclarContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#para}.
	 * @param ctx the parse tree
	 */
	void enterPara(MCParser.ParaContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#para}.
	 * @param ctx the parse tree
	 */
	void exitPara(MCParser.ParaContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#types}.
	 * @param ctx the parse tree
	 */
	void enterTypes(MCParser.TypesContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#types}.
	 * @param ctx the parse tree
	 */
	void exitTypes(MCParser.TypesContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#array_type}.
	 * @param ctx the parse tree
	 */
	void enterArray_type(MCParser.Array_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#array_type}.
	 * @param ctx the parse tree
	 */
	void exitArray_type(MCParser.Array_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#array_pointer_type}.
	 * @param ctx the parse tree
	 */
	void enterArray_pointer_type(MCParser.Array_pointer_typeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#array_pointer_type}.
	 * @param ctx the parse tree
	 */
	void exitArray_pointer_type(MCParser.Array_pointer_typeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#input_apt}.
	 * @param ctx the parse tree
	 */
	void enterInput_apt(MCParser.Input_aptContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#input_apt}.
	 * @param ctx the parse tree
	 */
	void exitInput_apt(MCParser.Input_aptContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#output_apt}.
	 * @param ctx the parse tree
	 */
	void enterOutput_apt(MCParser.Output_aptContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#output_apt}.
	 * @param ctx the parse tree
	 */
	void exitOutput_apt(MCParser.Output_aptContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(MCParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(MCParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#operands}.
	 * @param ctx the parse tree
	 */
	void enterOperands(MCParser.OperandsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#operands}.
	 * @param ctx the parse tree
	 */
	void exitOperands(MCParser.OperandsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#ele_array}.
	 * @param ctx the parse tree
	 */
	void enterEle_array(MCParser.Ele_arrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#ele_array}.
	 * @param ctx the parse tree
	 */
	void exitEle_array(MCParser.Ele_arrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#function_call}.
	 * @param ctx the parse tree
	 */
	void enterFunction_call(MCParser.Function_callContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#function_call}.
	 * @param ctx the parse tree
	 */
	void exitFunction_call(MCParser.Function_callContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#staments}.
	 * @param ctx the parse tree
	 */
	void enterStaments(MCParser.StamentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#staments}.
	 * @param ctx the parse tree
	 */
	void exitStaments(MCParser.StamentsContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#if_st}.
	 * @param ctx the parse tree
	 */
	void enterIf_st(MCParser.If_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#if_st}.
	 * @param ctx the parse tree
	 */
	void exitIf_st(MCParser.If_stContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#for_st}.
	 * @param ctx the parse tree
	 */
	void enterFor_st(MCParser.For_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#for_st}.
	 * @param ctx the parse tree
	 */
	void exitFor_st(MCParser.For_stContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#do_while}.
	 * @param ctx the parse tree
	 */
	void enterDo_while(MCParser.Do_whileContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#do_while}.
	 * @param ctx the parse tree
	 */
	void exitDo_while(MCParser.Do_whileContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#break_st}.
	 * @param ctx the parse tree
	 */
	void enterBreak_st(MCParser.Break_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#break_st}.
	 * @param ctx the parse tree
	 */
	void exitBreak_st(MCParser.Break_stContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#continue_st}.
	 * @param ctx the parse tree
	 */
	void enterContinue_st(MCParser.Continue_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#continue_st}.
	 * @param ctx the parse tree
	 */
	void exitContinue_st(MCParser.Continue_stContext ctx);
	/**
	 * Enter a parse tree produced by {@link MCParser#return_st}.
	 * @param ctx the parse tree
	 */
	void enterReturn_st(MCParser.Return_stContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#return_st}.
	 * @param ctx the parse tree
	 */
	void exitReturn_st(MCParser.Return_stContext ctx);
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
	 * Enter a parse tree produced by {@link MCParser#special_fuction}.
	 * @param ctx the parse tree
	 */
	void enterSpecial_fuction(MCParser.Special_fuctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MCParser#special_fuction}.
	 * @param ctx the parse tree
	 */
	void exitSpecial_fuction(MCParser.Special_fuctionContext ctx);
}