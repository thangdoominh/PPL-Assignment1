# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
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


    # Visit a parse tree produced by MCParser#declaration.
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#vardeclaration.
    def visitVardeclaration(self, ctx:MCParser.VardeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#singletype.
    def visitSingletype(self, ctx:MCParser.SingletypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idlist.
    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idtail.
    def visitIdtail(self, ctx:MCParser.IdtailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idarray.
    def visitIdarray(self, ctx:MCParser.IdarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#idsingle.
    def visitIdsingle(self, ctx:MCParser.IdsingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#funcdeclaration.
    def visitFuncdeclaration(self, ctx:MCParser.FuncdeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#block.
    def visitBlock(self, ctx:MCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MCParser#arraypointertype.
    def visitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        return self.visitChildren(ctx)



del MCParser