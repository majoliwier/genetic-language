# Generated from C:/Users/Oliwier/Desktop/genetyczne/genetic-language/grammar/MiniLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniLangParser import MiniLangParser
else:
    from MiniLangParser import MiniLangParser

# This class defines a complete generic visitor for a parse tree produced by MiniLangParser.

class MiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniLangParser#program.
    def visitProgram(self, ctx:MiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#block.
    def visitBlock(self, ctx:MiniLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#statement.
    def visitStatement(self, ctx:MiniLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#whileStatement.
    def visitWhileStatement(self, ctx:MiniLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ifStatement.
    def visitIfStatement(self, ctx:MiniLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#assignStatement.
    def visitAssignStatement(self, ctx:MiniLangParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#ioStatement.
    def visitIoStatement(self, ctx:MiniLangParser.IoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniLangParser#expression.
    def visitExpression(self, ctx:MiniLangParser.ExpressionContext):
        return self.visitChildren(ctx)



del MiniLangParser