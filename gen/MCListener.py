# Generated from /Users/dominhthang/Thang/HK-191/Principles-Of-Programming-Languages/Assignment/PPL-Assignment1/initial/src/main/mc/parser/MC.g4 by ANTLR 4.7.2
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


    # Enter a parse tree produced by MCParser#declaration.
    def enterDeclaration(self, ctx:MCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MCParser#declaration.
    def exitDeclaration(self, ctx:MCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MCParser#vardeclaration.
    def enterVardeclaration(self, ctx:MCParser.VardeclarationContext):
        pass

    # Exit a parse tree produced by MCParser#vardeclaration.
    def exitVardeclaration(self, ctx:MCParser.VardeclarationContext):
        pass


    # Enter a parse tree produced by MCParser#singletype.
    def enterSingletype(self, ctx:MCParser.SingletypeContext):
        pass

    # Exit a parse tree produced by MCParser#singletype.
    def exitSingletype(self, ctx:MCParser.SingletypeContext):
        pass


    # Enter a parse tree produced by MCParser#idlist.
    def enterIdlist(self, ctx:MCParser.IdlistContext):
        pass

    # Exit a parse tree produced by MCParser#idlist.
    def exitIdlist(self, ctx:MCParser.IdlistContext):
        pass


    # Enter a parse tree produced by MCParser#idtail.
    def enterIdtail(self, ctx:MCParser.IdtailContext):
        pass

    # Exit a parse tree produced by MCParser#idtail.
    def exitIdtail(self, ctx:MCParser.IdtailContext):
        pass


    # Enter a parse tree produced by MCParser#idarray.
    def enterIdarray(self, ctx:MCParser.IdarrayContext):
        pass

    # Exit a parse tree produced by MCParser#idarray.
    def exitIdarray(self, ctx:MCParser.IdarrayContext):
        pass


    # Enter a parse tree produced by MCParser#idsingle.
    def enterIdsingle(self, ctx:MCParser.IdsingleContext):
        pass

    # Exit a parse tree produced by MCParser#idsingle.
    def exitIdsingle(self, ctx:MCParser.IdsingleContext):
        pass


    # Enter a parse tree produced by MCParser#funcdeclaration.
    def enterFuncdeclaration(self, ctx:MCParser.FuncdeclarationContext):
        pass

    # Exit a parse tree produced by MCParser#funcdeclaration.
    def exitFuncdeclaration(self, ctx:MCParser.FuncdeclarationContext):
        pass


    # Enter a parse tree produced by MCParser#paralist_decla.
    def enterParalist_decla(self, ctx:MCParser.Paralist_declaContext):
        pass

    # Exit a parse tree produced by MCParser#paralist_decla.
    def exitParalist_decla(self, ctx:MCParser.Paralist_declaContext):
        pass


    # Enter a parse tree produced by MCParser#paradecla.
    def enterParadecla(self, ctx:MCParser.ParadeclaContext):
        pass

    # Exit a parse tree produced by MCParser#paradecla.
    def exitParadecla(self, ctx:MCParser.ParadeclaContext):
        pass


    # Enter a parse tree produced by MCParser#arraypointertype.
    def enterArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        pass

    # Exit a parse tree produced by MCParser#arraypointertype.
    def exitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        pass


    # Enter a parse tree produced by MCParser#block.
    def enterBlock(self, ctx:MCParser.BlockContext):
        pass

    # Exit a parse tree produced by MCParser#block.
    def exitBlock(self, ctx:MCParser.BlockContext):
        pass


    # Enter a parse tree produced by MCParser#statement.
    def enterStatement(self, ctx:MCParser.StatementContext):
        pass

    # Exit a parse tree produced by MCParser#statement.
    def exitStatement(self, ctx:MCParser.StatementContext):
        pass


    # Enter a parse tree produced by MCParser#ifstmt.
    def enterIfstmt(self, ctx:MCParser.IfstmtContext):
        pass

    # Exit a parse tree produced by MCParser#ifstmt.
    def exitIfstmt(self, ctx:MCParser.IfstmtContext):
        pass


    # Enter a parse tree produced by MCParser#dowhilestmt.
    def enterDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        pass

    # Exit a parse tree produced by MCParser#dowhilestmt.
    def exitDowhilestmt(self, ctx:MCParser.DowhilestmtContext):
        pass


    # Enter a parse tree produced by MCParser#forstmt.
    def enterForstmt(self, ctx:MCParser.ForstmtContext):
        pass

    # Exit a parse tree produced by MCParser#forstmt.
    def exitForstmt(self, ctx:MCParser.ForstmtContext):
        pass


    # Enter a parse tree produced by MCParser#breakstmt.
    def enterBreakstmt(self, ctx:MCParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by MCParser#breakstmt.
    def exitBreakstmt(self, ctx:MCParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by MCParser#continuestmt.
    def enterContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by MCParser#continuestmt.
    def exitContinuestmt(self, ctx:MCParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by MCParser#returnstmt.
    def enterReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by MCParser#returnstmt.
    def exitReturnstmt(self, ctx:MCParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by MCParser#expressionstmt.
    def enterExpressionstmt(self, ctx:MCParser.ExpressionstmtContext):
        pass

    # Exit a parse tree produced by MCParser#expressionstmt.
    def exitExpressionstmt(self, ctx:MCParser.ExpressionstmtContext):
        pass


    # Enter a parse tree produced by MCParser#expression.
    def enterExpression(self, ctx:MCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MCParser#expression.
    def exitExpression(self, ctx:MCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MCParser#exp1.
    def enterExp1(self, ctx:MCParser.Exp1Context):
        pass

    # Exit a parse tree produced by MCParser#exp1.
    def exitExp1(self, ctx:MCParser.Exp1Context):
        pass


    # Enter a parse tree produced by MCParser#exp2.
    def enterExp2(self, ctx:MCParser.Exp2Context):
        pass

    # Exit a parse tree produced by MCParser#exp2.
    def exitExp2(self, ctx:MCParser.Exp2Context):
        pass


    # Enter a parse tree produced by MCParser#exp3.
    def enterExp3(self, ctx:MCParser.Exp3Context):
        pass

    # Exit a parse tree produced by MCParser#exp3.
    def exitExp3(self, ctx:MCParser.Exp3Context):
        pass


    # Enter a parse tree produced by MCParser#exp4.
    def enterExp4(self, ctx:MCParser.Exp4Context):
        pass

    # Exit a parse tree produced by MCParser#exp4.
    def exitExp4(self, ctx:MCParser.Exp4Context):
        pass


    # Enter a parse tree produced by MCParser#exp5.
    def enterExp5(self, ctx:MCParser.Exp5Context):
        pass

    # Exit a parse tree produced by MCParser#exp5.
    def exitExp5(self, ctx:MCParser.Exp5Context):
        pass


    # Enter a parse tree produced by MCParser#exp6.
    def enterExp6(self, ctx:MCParser.Exp6Context):
        pass

    # Exit a parse tree produced by MCParser#exp6.
    def exitExp6(self, ctx:MCParser.Exp6Context):
        pass


    # Enter a parse tree produced by MCParser#exp7.
    def enterExp7(self, ctx:MCParser.Exp7Context):
        pass

    # Exit a parse tree produced by MCParser#exp7.
    def exitExp7(self, ctx:MCParser.Exp7Context):
        pass


    # Enter a parse tree produced by MCParser#exp8.
    def enterExp8(self, ctx:MCParser.Exp8Context):
        pass

    # Exit a parse tree produced by MCParser#exp8.
    def exitExp8(self, ctx:MCParser.Exp8Context):
        pass


    # Enter a parse tree produced by MCParser#exp9.
    def enterExp9(self, ctx:MCParser.Exp9Context):
        pass

    # Exit a parse tree produced by MCParser#exp9.
    def exitExp9(self, ctx:MCParser.Exp9Context):
        pass


    # Enter a parse tree produced by MCParser#exp10.
    def enterExp10(self, ctx:MCParser.Exp10Context):
        pass

    # Exit a parse tree produced by MCParser#exp10.
    def exitExp10(self, ctx:MCParser.Exp10Context):
        pass


    # Enter a parse tree produced by MCParser#operand.
    def enterOperand(self, ctx:MCParser.OperandContext):
        pass

    # Exit a parse tree produced by MCParser#operand.
    def exitOperand(self, ctx:MCParser.OperandContext):
        pass


    # Enter a parse tree produced by MCParser#funccall.
    def enterFunccall(self, ctx:MCParser.FunccallContext):
        pass

    # Exit a parse tree produced by MCParser#funccall.
    def exitFunccall(self, ctx:MCParser.FunccallContext):
        pass


    # Enter a parse tree produced by MCParser#paralist_call.
    def enterParalist_call(self, ctx:MCParser.Paralist_callContext):
        pass

    # Exit a parse tree produced by MCParser#paralist_call.
    def exitParalist_call(self, ctx:MCParser.Paralist_callContext):
        pass


    # Enter a parse tree produced by MCParser#para_call.
    def enterPara_call(self, ctx:MCParser.Para_callContext):
        pass

    # Exit a parse tree produced by MCParser#para_call.
    def exitPara_call(self, ctx:MCParser.Para_callContext):
        pass


