# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/reference/Github/assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete generic visitor for a parse tree produced by MCParser.

class MCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MCParser#program.
    def visitProgram(self, ctx:MCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#declar.
    def visitDeclar(self, ctx:MCParser.DeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardeclar.
    def visitVardeclar(self, ctx:MCParser.VardeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#variable.
    def visitVariable(self, ctx:MCParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdeclar.
    def visitFuncdeclar(self, ctx:MCParser.FuncdeclarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#para.
    def visitPara(self, ctx:MCParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#types.
    def visitTypes(self, ctx:MCParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_type.
    def visitArray_type(self, ctx:MCParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#array_pointer_type.
    def visitArray_pointer_type(self, ctx:MCParser.Array_pointer_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#input_apt.
    def visitInput_apt(self, ctx:MCParser.Input_aptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#output_apt.
    def visitOutput_apt(self, ctx:MCParser.Output_aptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expr.
    def visitExpr(self, ctx:MCParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#operands.
    def visitOperands(self, ctx:MCParser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#ele_array.
    def visitEle_array(self, ctx:MCParser.Ele_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#function_call.
    def visitFunction_call(self, ctx:MCParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#staments.
    def visitStaments(self, ctx:MCParser.StamentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#if_st.
    def visitIf_st(self, ctx:MCParser.If_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#for_st.
    def visitFor_st(self, ctx:MCParser.For_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#do_while.
    def visitDo_while(self, ctx:MCParser.Do_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#break_st.
    def visitBreak_st(self, ctx:MCParser.Break_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#continue_st.
    def visitContinue_st(self, ctx:MCParser.Continue_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#return_st.
    def visitReturn_st(self, ctx:MCParser.Return_stContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#expression.
    def visitExpression(self, ctx:MCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block.
    def visitBlock(self, ctx:MCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#special_fuction.
    def visitSpecial_fuction(self, ctx:MCParser.Special_fuctionContext):
        return self.visitChildren(ctx)



del MCParser