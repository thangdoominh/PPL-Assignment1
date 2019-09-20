# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardeclaration.
    def visitVardeclaration(self, ctx:MPParser.VardeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#vardeclarationlist.
    def visitVardeclarationlist(self, ctx:MPParser.VardeclarationlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#parameter.
    def visitParameter(self, ctx:MPParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#singletype.
    def visitSingletype(self, ctx:MPParser.SingletypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arraytype.
    def visitArraytype(self, ctx:MPParser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcdeclaration.
    def visitFuncdeclaration(self, ctx:MPParser.FuncdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procdeclaration.
    def visitProcdeclaration(self, ctx:MPParser.ProcdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statementpart.
    def visitStatementpart(self, ctx:MPParser.StatementpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignstatement.
    def visitAssignstatement(self, ctx:MPParser.AssignstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstatement.
    def visitIfstatement(self, ctx:MPParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestatement.
    def visitWhilestatement(self, ctx:MPParser.WhilestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstatement.
    def visitForstatement(self, ctx:MPParser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstatement.
    def visitBreakstatement(self, ctx:MPParser.BreakstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continuestatement.
    def visitContinuestatement(self, ctx:MPParser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstatement.
    def visitReturnstatement(self, ctx:MPParser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compoundstatement.
    def visitCompoundstatement(self, ctx:MPParser.CompoundstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstatement.
    def visitWithstatement(self, ctx:MPParser.WithstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#callstatement.
    def visitCallstatement(self, ctx:MPParser.CallstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#expressions.
    def visitExpressions(self, ctx:MPParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp0.
    def visitExp0(self, ctx:MPParser.Exp0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp5.
    def visitExp5(self, ctx:MPParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp6.
    def visitExp6(self, ctx:MPParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand.
    def visitOperand(self, ctx:MPParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funccall.
    def visitFunccall(self, ctx:MPParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#arrayindex.
    def visitArrayindex(self, ctx:MPParser.ArrayindexContext):
        return self.visitChildren(ctx)



del MPParser