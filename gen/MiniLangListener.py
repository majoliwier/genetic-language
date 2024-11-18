# Generated from C:/Users/Oliwier/Desktop/genetyczne/genetic-language/grammar/MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete listener for a parse tree produced by MiniLangParser.
class MiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by MiniLangParser#program.
    def enterProgram(self, ctx:MiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniLangParser#program.
    def exitProgram(self, ctx:MiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniLangParser#block.
    def enterBlock(self, ctx:MiniLangParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniLangParser#block.
    def exitBlock(self, ctx:MiniLangParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniLangParser#statement.
    def enterStatement(self, ctx:MiniLangParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#statement.
    def exitStatement(self, ctx:MiniLangParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#whileStatement.
    def enterWhileStatement(self, ctx:MiniLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#whileStatement.
    def exitWhileStatement(self, ctx:MiniLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ifStatement.
    def enterIfStatement(self, ctx:MiniLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ifStatement.
    def exitIfStatement(self, ctx:MiniLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#assignStatement.
    def enterAssignStatement(self, ctx:MiniLangParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#assignStatement.
    def exitAssignStatement(self, ctx:MiniLangParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#ioStatement.
    def enterIoStatement(self, ctx:MiniLangParser.IoStatementContext):
        pass

    # Exit a parse tree produced by MiniLangParser#ioStatement.
    def exitIoStatement(self, ctx:MiniLangParser.IoStatementContext):
        pass


    # Enter a parse tree produced by MiniLangParser#expression.
    def enterExpression(self, ctx:MiniLangParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniLangParser#expression.
    def exitExpression(self, ctx:MiniLangParser.ExpressionContext):
        pass



del MiniLangParser