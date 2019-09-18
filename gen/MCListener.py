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


    # Enter a parse tree produced by MCParser#block.
    def enterBlock(self, ctx:MCParser.BlockContext):
        pass

    # Exit a parse tree produced by MCParser#block.
    def exitBlock(self, ctx:MCParser.BlockContext):
        pass


    # Enter a parse tree produced by MCParser#arraypointertype.
    def enterArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        pass

    # Exit a parse tree produced by MCParser#arraypointertype.
    def exitArraypointertype(self, ctx:MCParser.ArraypointertypeContext):
        pass


