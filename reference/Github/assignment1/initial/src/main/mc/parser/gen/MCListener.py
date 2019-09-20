# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/reference/Github/assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete listener for a parse tree produced by MCParser.
class MCListener(ParseTreeListener):

    # Enter a parse tree produced by MCParser#program.
    def enterProgram(self, ctx:MCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MCParser#program.
    def exitProgram(self, ctx:MCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MCParser#declar.
    def enterDeclar(self, ctx:MCParser.DeclarContext):
        pass

    # Exit a parse tree produced by MCParser#declar.
    def exitDeclar(self, ctx:MCParser.DeclarContext):
        pass


    # Enter a parse tree produced by MCParser#vardeclar.
    def enterVardeclar(self, ctx:MCParser.VardeclarContext):
        pass

    # Exit a parse tree produced by MCParser#vardeclar.
    def exitVardeclar(self, ctx:MCParser.VardeclarContext):
        pass


    # Enter a parse tree produced by MCParser#variable.
    def enterVariable(self, ctx:MCParser.VariableContext):
        pass

    # Exit a parse tree produced by MCParser#variable.
    def exitVariable(self, ctx:MCParser.VariableContext):
        pass


    # Enter a parse tree produced by MCParser#funcdeclar.
    def enterFuncdeclar(self, ctx:MCParser.FuncdeclarContext):
        pass

    # Exit a parse tree produced by MCParser#funcdeclar.
    def exitFuncdeclar(self, ctx:MCParser.FuncdeclarContext):
        pass


    # Enter a parse tree produced by MCParser#para.
    def enterPara(self, ctx:MCParser.ParaContext):
        pass

    # Exit a parse tree produced by MCParser#para.
    def exitPara(self, ctx:MCParser.ParaContext):
        pass


    # Enter a parse tree produced by MCParser#types.
    def enterTypes(self, ctx:MCParser.TypesContext):
        pass

    # Exit a parse tree produced by MCParser#types.
    def exitTypes(self, ctx:MCParser.TypesContext):
        pass


    # Enter a parse tree produced by MCParser#array_type.
    def enterArray_type(self, ctx:MCParser.Array_typeContext):
        pass

    # Exit a parse tree produced by MCParser#array_type.
    def exitArray_type(self, ctx:MCParser.Array_typeContext):
        pass


    # Enter a parse tree produced by MCParser#array_pointer_type.
    def enterArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        pass

    # Exit a parse tree produced by MCParser#array_pointer_type.
    def exitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        pass


    # Enter a parse tree produced by MCParser#input_apt.
    def enterInput_apt(self, ctx:MCParser.Input_aptContext):
        pass

    # Exit a parse tree produced by MCParser#input_apt.
    def exitInput_apt(self, ctx:MCParser.Input_aptContext):
        pass


    # Enter a parse tree produced by MCParser#output_apt.
    def enterOutput_apt(self, ctx:MCParser.Output_aptContext):
        pass

    # Exit a parse tree produced by MCParser#output_apt.
    def exitOutput_apt(self, ctx:MCParser.Output_aptContext):
        pass


    # Enter a parse tree produced by MCParser#expr.
    def enterExpr(self, ctx:MCParser.ExprContext):
        pass

    # Exit a parse tree produced by MCParser#expr.
    def exitExpr(self, ctx:MCParser.ExprContext):
        pass


    # Enter a parse tree produced by MCParser#operands.
    def enterOperands(self, ctx:MCParser.OperandsContext):
        pass

    # Exit a parse tree produced by MCParser#operands.
    def exitOperands(self, ctx:MCParser.OperandsContext):
        pass


    # Enter a parse tree produced by MCParser#ele_array.
    def enterEle_array(self, ctx:MCParser.Ele_arrayContext):
        pass

    # Exit a parse tree produced by MCParser#ele_array.
    def exitEle_array(self, ctx:MCParser.Ele_arrayContext):
        pass


    # Enter a parse tree produced by MCParser#function_call.
    def enterFunction_call(self, ctx:MCParser.Function_callContext):
        pass

    # Exit a parse tree produced by MCParser#function_call.
    def exitFunction_call(self, ctx:MCParser.Function_callContext):
        pass


    # Enter a parse tree produced by MCParser#staments.
    def enterStaments(self, ctx:MCParser.StamentsContext):
        pass

    # Exit a parse tree produced by MCParser#staments.
    def exitStaments(self, ctx:MCParser.StamentsContext):
        pass


    # Enter a parse tree produced by MCParser#if_st.
    def enterIf_st(self, ctx:MCParser.If_stContext):
        pass

    # Exit a parse tree produced by MCParser#if_st.
    def exitIf_st(self, ctx:MCParser.If_stContext):
        pass


    # Enter a parse tree produced by MCParser#for_st.
    def enterFor_st(self, ctx:MCParser.For_stContext):
        pass

    # Exit a parse tree produced by MCParser#for_st.
    def exitFor_st(self, ctx:MCParser.For_stContext):
        pass


    # Enter a parse tree produced by MCParser#do_while.
    def enterDo_while(self, ctx:MCParser.Do_whileContext):
        pass

    # Exit a parse tree produced by MCParser#do_while.
    def exitDo_while(self, ctx:MCParser.Do_whileContext):
        pass


    # Enter a parse tree produced by MCParser#break_st.
    def enterBreak_st(self, ctx:MCParser.Break_stContext):
        pass

    # Exit a parse tree produced by MCParser#break_st.
    def exitBreak_st(self, ctx:MCParser.Break_stContext):
        pass


    # Enter a parse tree produced by MCParser#continue_st.
    def enterContinue_st(self, ctx:MCParser.Continue_stContext):
        pass

    # Exit a parse tree produced by MCParser#continue_st.
    def exitContinue_st(self, ctx:MCParser.Continue_stContext):
        pass


    # Enter a parse tree produced by MCParser#return_st.
    def enterReturn_st(self, ctx:MCParser.Return_stContext):
        pass

    # Exit a parse tree produced by MCParser#return_st.
    def exitReturn_st(self, ctx:MCParser.Return_stContext):
        pass


    # Enter a parse tree produced by MCParser#expression.
    def enterExpression(self, ctx:MCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MCParser#expression.
    def exitExpression(self, ctx:MCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MCParser#block.
    def enterBlock(self, ctx:MCParser.BlockContext):
        pass

    # Exit a parse tree produced by MCParser#block.
    def exitBlock(self, ctx:MCParser.BlockContext):
        pass


    # Enter a parse tree produced by MCParser#special_fuction.
    def enterSpecial_fuction(self, ctx:MCParser.Special_fuctionContext):
        pass

    # Exit a parse tree produced by MCParser#special_fuction.
    def exitSpecial_fuction(self, ctx:MCParser.Special_fuctionContext):
        pass


