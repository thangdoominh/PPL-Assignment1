import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

# -------------- VAR DECLARE -----------------------
	def test_var_decl_200(self):
		input = """void thang()
			{
				int a;
				float b[3];
			}
            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 200))
	def test_var_decl_201(self):
		input = """void thang(){int a;float b[];}
		            """
		expect = "Error on line 1 col 27: ]"
		self.assertTrue(TestParser.checkParser(input, expect, 201))
	def test_var_decl_202(self):
		input = """ int ;
		            """
		expect = "Error on line 1 col 5: ;"
		self.assertTrue(TestParser.checkParser(input, expect, 202))
	def test_var_decl_203(self):
		input = """int thang(int a, int b, float c, int f[]){}
		            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect,203))
	def test_var_decl_204(self):
		input = """int thang(int a, int b, float c, int f[]){
		            """
		expect = "Error on line 2 col 14: <EOF>"
		self.assertTrue(TestParser.checkParser(input, expect, 204))
	def test_var_decl_205(self):
		input = """ boolean ___a[3];
		            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 205))
	def test_var_decl_206(self):
		input = """string []; 
		            """
		expect = "Error on line 1 col 9: ;"
		self.assertTrue(TestParser.checkParser(input, expect, 206))
	def test_var_decl_207(self):
		input = """float a,b,c,d[2];
                    int a,b[2];
		            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 207))
	def test_var_decl_208(self):
		input = """void (int thang){}
		            """
		expect = "Error on line 1 col 5: ("
		self.assertTrue(TestParser.checkParser(input, expect, 208))
	def test_var_decl_209(self):
		input = """void _int(int a){}
		            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 209))
	def test_var_decl_210(self):
		input = """void main(){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    float a[25];
            }"""
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 210))

# ------------- Function decl --------------------------------
	def test_func_decl_211(self):
		input = """int main()
			{
			}
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 211)))
	def test_func_decl_212(self):
		input = """void[] nu(int a, int b){} 
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 212)))
	def test_func_decl_213(self):
		input = """void[] abc(int a[], int b[]){}
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 213)))
	def test_func_decl_214(self):
		input = """void[] abc(int a[], int b[[){}
		"""
		expect = "Error on line 1 col 26: ["
		self.assertTrue((TestParser.checkParser(input, expect, 214)))
	def test_func_decl_215(self):
		input = """void a(){}
int b(){}
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 215)))
	def test_func_decl_216(self):
		input = """void a(){
int b(){}
		"""
		expect = "Error on line 2 col 5: ("
		self.assertTrue((TestParser.checkParser(input, expect, 216)))
	def test_func_decl_217(self):
		input = """void a(int a, float b[] ){}
int b(boolean array[]){}
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 217)))
	def test_func_decl_218(self):
		input = """void a(int a, float b[] ){int b(boolean array[]){}}
		"""
		expect = "Error on line 1 col 31: ("
		self.assertTrue((TestParser.checkParser(input, expect, 218)))
	def test_func_decl_219(self):
		input = """void a(int a, float b[] ){int b;{}}
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 219)))
	def test_func_decl_220(self):
		input = """void a(int a, float b[] ){int b;{float v[3];}}
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 220)))

	def test_func_decl_221(self):
		input = """
int func(int a, float b[])
{
	if (a = b)
		a;
}
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 221)))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))
	def test_func_decl_22(self):
		input = """
		"""
		expect = ""
		self.assertTrue((TestParser.checkParser(input, expect, )))