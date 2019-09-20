# Generated from /home/viet/Courses/PPL/assignment1/ass1/initial/src/main/mp/parser/MP.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete listener for a parse tree produced by MPParser.
class MPListener(ParseTreeListener):

    # Enter a parse tree produced by MPParser#program.
    def enterProgram(self, ctx:MPParser.ProgramContext):
        pass

    # Exit a parse tree produced by MPParser#program.
    def exitProgram(self, ctx:MPParser.ProgramContext):
        pass


    # Enter a parse tree produced by MPParser#vardeclaration.
    def enterVardeclaration(self, ctx:MPParser.VardeclarationContext):
        pass

    # Exit a parse tree produced by MPParser#vardeclaration.
    def exitVardeclaration(self, ctx:MPParser.VardeclarationContext):
        pass


    # Enter a parse tree produced by MPParser#vardeclarationlist.
    def enterVardeclarationlist(self, ctx:MPParser.VardeclarationlistContext):
        pass

    # Exit a parse tree produced by MPParser#vardeclarationlist.
    def exitVardeclarationlist(self, ctx:MPParser.VardeclarationlistContext):
        pass


    # Enter a parse tree produced by MPParser#parameter.
    def enterParameter(self, ctx:MPParser.ParameterContext):
        pass

    # Exit a parse tree produced by MPParser#parameter.
    def exitParameter(self, ctx:MPParser.ParameterContext):
        pass


    # Enter a parse tree produced by MPParser#singletype.
    def enterSingletype(self, ctx:MPParser.SingletypeContext):
        pass

    # Exit a parse tree produced by MPParser#singletype.
    def exitSingletype(self, ctx:MPParser.SingletypeContext):
        pass


    # Enter a parse tree produced by MPParser#arraytype.
    def enterArraytype(self, ctx:MPParser.ArraytypeContext):
        pass

    # Exit a parse tree produced by MPParser#arraytype.
    def exitArraytype(self, ctx:MPParser.ArraytypeContext):
        pass


    # Enter a parse tree produced by MPParser#funcdeclaration.
    def enterFuncdeclaration(self, ctx:MPParser.FuncdeclarationContext):
        pass

    # Exit a parse tree produced by MPParser#funcdeclaration.
    def exitFuncdeclaration(self, ctx:MPParser.FuncdeclarationContext):
        pass


    # Enter a parse tree produced by MPParser#procdeclaration.
    def enterProcdeclaration(self, ctx:MPParser.ProcdeclarationContext):
        pass

    # Exit a parse tree produced by MPParser#procdeclaration.
    def exitProcdeclaration(self, ctx:MPParser.ProcdeclarationContext):
        pass


    # Enter a parse tree produced by MPParser#statementpart.
    def enterStatementpart(self, ctx:MPParser.StatementpartContext):
        pass

    # Exit a parse tree produced by MPParser#statementpart.
    def exitStatementpart(self, ctx:MPParser.StatementpartContext):
        pass


    # Enter a parse tree produced by MPParser#assignstatement.
    def enterAssignstatement(self, ctx:MPParser.AssignstatementContext):
        pass

    # Exit a parse tree produced by MPParser#assignstatement.
    def exitAssignstatement(self, ctx:MPParser.AssignstatementContext):
        pass


    # Enter a parse tree produced by MPParser#ifstatement.
    def enterIfstatement(self, ctx:MPParser.IfstatementContext):
        pass

    # Exit a parse tree produced by MPParser#ifstatement.
    def exitIfstatement(self, ctx:MPParser.IfstatementContext):
        pass


    # Enter a parse tree produced by MPParser#whilestatement.
    def enterWhilestatement(self, ctx:MPParser.WhilestatementContext):
        pass

    # Exit a parse tree produced by MPParser#whilestatement.
    def exitWhilestatement(self, ctx:MPParser.WhilestatementContext):
        pass


    # Enter a parse tree produced by MPParser#forstatement.
    def enterForstatement(self, ctx:MPParser.ForstatementContext):
        pass

    # Exit a parse tree produced by MPParser#forstatement.
    def exitForstatement(self, ctx:MPParser.ForstatementContext):
        pass


    # Enter a parse tree produced by MPParser#breakstatement.
    def enterBreakstatement(self, ctx:MPParser.BreakstatementContext):
        pass

    # Exit a parse tree produced by MPParser#breakstatement.
    def exitBreakstatement(self, ctx:MPParser.BreakstatementContext):
        pass


    # Enter a parse tree produced by MPParser#continuestatement.
    def enterContinuestatement(self, ctx:MPParser.ContinuestatementContext):
        pass

    # Exit a parse tree produced by MPParser#continuestatement.
    def exitContinuestatement(self, ctx:MPParser.ContinuestatementContext):
        pass


    # Enter a parse tree produced by MPParser#returnstatement.
    def enterReturnstatement(self, ctx:MPParser.ReturnstatementContext):
        pass

    # Exit a parse tree produced by MPParser#returnstatement.
    def exitReturnstatement(self, ctx:MPParser.ReturnstatementContext):
        pass


    # Enter a parse tree produced by MPParser#compoundstatement.
    def enterCompoundstatement(self, ctx:MPParser.CompoundstatementContext):
        pass

    # Exit a parse tree produced by MPParser#compoundstatement.
    def exitCompoundstatement(self, ctx:MPParser.CompoundstatementContext):
        pass


    # Enter a parse tree produced by MPParser#withstatement.
    def enterWithstatement(self, ctx:MPParser.WithstatementContext):
        pass

    # Exit a parse tree produced by MPParser#withstatement.
    def exitWithstatement(self, ctx:MPParser.WithstatementContext):
        pass


    # Enter a parse tree produced by MPParser#callstatement.
    def enterCallstatement(self, ctx:MPParser.CallstatementContext):
        pass

    # Exit a parse tree produced by MPParser#callstatement.
    def exitCallstatement(self, ctx:MPParser.CallstatementContext):
        pass


    # Enter a parse tree produced by MPParser#expressions.
    def enterExpressions(self, ctx:MPParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by MPParser#expressions.
    def exitExpressions(self, ctx:MPParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by MPParser#exp0.
    def enterExp0(self, ctx:MPParser.Exp0Context):
        pass

    # Exit a parse tree produced by MPParser#exp0.
    def exitExp0(self, ctx:MPParser.Exp0Context):
        pass


    # Enter a parse tree produced by MPParser#exp1.
    def enterExp1(self, ctx:MPParser.Exp1Context):
        pass

    # Exit a parse tree produced by MPParser#exp1.
    def exitExp1(self, ctx:MPParser.Exp1Context):
        pass


    # Enter a parse tree produced by MPParser#exp2.
    def enterExp2(self, ctx:MPParser.Exp2Context):
        pass

    # Exit a parse tree produced by MPParser#exp2.
    def exitExp2(self, ctx:MPParser.Exp2Context):
        pass


    # Enter a parse tree produced by MPParser#exp3.
    def enterExp3(self, ctx:MPParser.Exp3Context):
        pass

    # Exit a parse tree produced by MPParser#exp3.
    def exitExp3(self, ctx:MPParser.Exp3Context):
        pass


    # Enter a parse tree produced by MPParser#exp4.
    def enterExp4(self, ctx:MPParser.Exp4Context):
        pass

    # Exit a parse tree produced by MPParser#exp4.
    def exitExp4(self, ctx:MPParser.Exp4Context):
        pass


    # Enter a parse tree produced by MPParser#exp5.
    def enterExp5(self, ctx:MPParser.Exp5Context):
        pass

    # Exit a parse tree produced by MPParser#exp5.
    def exitExp5(self, ctx:MPParser.Exp5Context):
        pass


    # Enter a parse tree produced by MPParser#exp6.
    def enterExp6(self, ctx:MPParser.Exp6Context):
        pass

    # Exit a parse tree produced by MPParser#exp6.
    def exitExp6(self, ctx:MPParser.Exp6Context):
        pass


    # Enter a parse tree produced by MPParser#operand.
    def enterOperand(self, ctx:MPParser.OperandContext):
        pass

    # Exit a parse tree produced by MPParser#operand.
    def exitOperand(self, ctx:MPParser.OperandContext):
        pass


    # Enter a parse tree produced by MPParser#funccall.
    def enterFunccall(self, ctx:MPParser.FunccallContext):
        pass

    # Exit a parse tree produced by MPParser#funccall.
    def exitFunccall(self, ctx:MPParser.FunccallContext):
        pass


    # Enter a parse tree produced by MPParser#arrayindex.
    def enterArrayindex(self, ctx:MPParser.ArrayindexContext):
        pass

    # Exit a parse tree produced by MPParser#arrayindex.
    def exitArrayindex(self, ctx:MPParser.ArrayindexContext):
        pass


