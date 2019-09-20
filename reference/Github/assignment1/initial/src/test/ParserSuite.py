import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """ Test 1 """
        input = """
            int i;
            int f(){
                return 200 ;
            }
            void main(){
                int main;
                main = f();
                putIntLn(main);
                {
                    int i;
                    int main;
                    int f;
                    main = f = i = 100;
                    putIntLn(i);
                    putIntLn(main);
                    putIntLn(f);
                }
                putIntLn(main);
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))