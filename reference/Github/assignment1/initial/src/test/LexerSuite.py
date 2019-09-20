import unittest
from TestUtils import TestLexer

count = 100

class LexerSuite(unittest.TestCase):

    def test_a_identifier(self):
        """test Identifiers"""
        global count
        test_case = ['abc','abc_','a_bc','aCBbdc','aC_Bbdc','aAsVN','aAsVN_','WQEWQ_asdsa','_QWEa_sdWQ_E', '_a_Z_', '___',
                    'Boolean','Break','Continute','Else','For','floaT','If','inT','Return','Void','Do','whiLe','sTring','True','False']
        solution = ['abc,<EOF>','abc_,<EOF>','a_bc,<EOF>','aCBbdc,<EOF>','aC_Bbdc,<EOF>','aAsVN,<EOF>','aAsVN_,<EOF>','WQEWQ_asdsa,<EOF>',
                    '_QWEa_sdWQ_E,<EOF>', '_a_Z_,<EOF>', '___,<EOF>','Boolean,<EOF>','Break,<EOF>','Continute,<EOF>','Else,<EOF>',
                    'For,<EOF>','floaT,<EOF>','If,<EOF>','inT,<EOF>','Return,<EOF>','Void,<EOF>',
                    'Do,<EOF>','whiLe,<EOF>','sTring,<EOF>','True,<EOF>','False,<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1

    def test_b_intlit(self):
        """test Intlit"""
        global count
        test_case = ['123a123','12321_213213','65460ASDE_1234','234231','021321']
        solution = ['123,a123,<EOF>','12321,_213213,<EOF>',
                    '65460,ASDE_1234,<EOF>',
                    '234231,<EOF>','021321,<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1
    
    def test_c_separator(self):
        """test Separator"""
        global count
        test_case = ['[123a123]','(12321_213213)','{65460ASDE_1234}','234231;','021321,']
        solution = ['[,123,a123,],<EOF>','(,12321,_213213,),<EOF>',
                    '{,65460,ASDE_1234,},<EOF>',
                    '234231,;,<EOF>','021321,,,<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1
    
    def test_d_operator(self):
        """test Operator"""
        global count
        test_case = ['++','--','**','/','%','!==!','|||','!===','<<=','>>=','&&&']
        solution = ['+,+,<EOF>','-,-,<EOF>','*,*,<EOF>','/,<EOF>','%,<EOF>','!=,=,!,<EOF>','||,|,<EOF>',
                    '!=,==,<EOF>','<,<=,<EOF>','>,>=,<EOF>','&&,&,<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1
    
    def test_e_keyword(self):
        """test Keyword"""
        global count
        test_case = ['boolean','break','continute','else','for','float','if','int','return','void','do','while','string','true','false',
        'Int','Bool','Float','String','IntLn','BoolLn','FloatLn','StringLn','Ln']
        solution = ['boolean,<EOF>','break,<EOF>','continute,<EOF>','else,<EOF>','for,<EOF>','float,<EOF>','if,<EOF>',
                    'int,<EOF>','return,<EOF>','void,<EOF>','do,<EOF>','while,<EOF>','string,<EOF>','true,<EOF>','false,<EOF>',
                    'Int,<EOF>','Bool,<EOF>','Float,<EOF>','String,<EOF>','IntLn,<EOF>','BoolLn,<EOF>','FloatLn,<EOF>','StringLn,<EOF>','Ln,<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1
    
    def test_f_string(self):
        """test String"""
        global count
        test_case = ['"21321321321"','"wqesaDSADsd231"','"\\\".,?/!@#$%^&()_+=-"','"ab\bads\fgad\tsad  qw\ndasdabc"',
                    '"boolean"','"break"','"continute"','"else"','"for"','"float"','"if"','"int"']
        solution = ['"21321321321",<EOF>','"wqesaDSADsd231",<EOF>','"\\\".,?/!@#$%^&()_+=-",<EOF>','"ab\bads\fgad\tsad  qw\ndasdabc",<EOF>',
                    '"boolean",<EOF>','"break",<EOF>','"continute",<EOF>','"else",<EOF>','"for",<EOF>','"float",<EOF>','"if",<EOF>','"int",<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1
        
    def test_g_float(self):
        """test Floatlit"""
        global count
        test_case = ['123.123','12321.21E3213','65460.123e-1234','234231.','.21321','.123E-123','.123e213','.','.e3213','123.e-123','435.E654']
        solution = ['123.123,<EOF>','12321.21E3213,<EOF>','65460.123e-1234,<EOF>','234231.,<EOF>','.21321,<EOF>','.123E-123,<EOF>','.123e213,<EOF>',
                    '.,<EOF>','.,e3213,<EOF>','123.,e,-,123,<EOF>','435.,E654,<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1
    
    def test_h_comment(self):
        """test Comment"""
        global count
        test_case = ['//asdqwewqdcasr!@$#%@#DSAF\n','//123231.3121\n3e123213','//1232\r1321.12312e-213213','//.213E213123\r','////\n//////\r',
                    '/*qweasdsad\nsedaqwdas\rsadsadsadas*/','/*qweasdsad\nseda//qwdas\rsadsadsadas*/']
        solution = ['<EOF>','3e123213,<EOF>','1321.12312e-213213,<EOF>','<EOF>','<EOF>','<EOF>','<EOF>']
        for i in range(len(test_case)):
            self.assertTrue(TestLexer.checkLexeme(
                test_case[i],solution[i],count))
            count += 1
    
    
