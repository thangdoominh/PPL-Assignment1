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


    # Enter a parse tree produced by MCParser#mctype.
    def enterMctype(self, ctx:MCParser.MctypeContext):
        pass

    # Exit a parse tree produced by MCParser#mctype.
    def exitMctype(self, ctx:MCParser.MctypeContext):
        pass


    # Enter a parse tree produced by MCParser#body.
    def enterBody(self, ctx:MCParser.BodyContext):
        pass

    # Exit a parse tree produced by MCParser#body.
    def exitBody(self, ctx:MCParser.BodyContext):
        pass


    # Enter a parse tree produced by MCParser#exp.
    def enterExp(self, ctx:MCParser.ExpContext):
        pass

    # Exit a parse tree produced by MCParser#exp.
    def exitExp(self, ctx:MCParser.ExpContext):
        pass


    # Enter a parse tree produced by MCParser#funcall.
    def enterFuncall(self, ctx:MCParser.FuncallContext):
        pass

    # Exit a parse tree produced by MCParser#funcall.
    def exitFuncall(self, ctx:MCParser.FuncallContext):
        pass


