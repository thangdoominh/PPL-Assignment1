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
	def test_func_decl_222(self):
		input = """void main(){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    float a[25];
            }"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 222)))
	def test_func_decl_223(self):
		input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    }"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 223)))
	def test_func_decl_224(self):
		input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;}"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 224)))
	def test_func_decl_225(self):
		input = """void main(){
            do a+b;b+c;c>d+f+g;
            while (b[10]);
            }
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 225)))
	def test_func_decl_226(self):
		input = """void main(){
            do a+b; while b[10];
            }"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 226)))
	def test_func_decl_227(self):
		input = """void main(){
            for(i=1;i<x[5];i+1)
                 return;return x+b+c-d;return;
            }
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 227)))
	def test_func_decl_228(self):
		input = """void main(){
            for(i=0;i<a[10];i+1)
                 break;break;break;
            }
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 228)))
	def test_func_decl_229(self):
		input = """boolean first;
                string createPointer(int a, boolean b[]){
                    {
                        {}
                    }
                }
                float beHumble(){}
                int second;
		"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 229)))
	def test_func_decl_230(self):
		input = """
				boolean first;
                void createPointer(int a, boolean b[]){
                    int a, b, c;
                    int[] main(){}
                }
                float beHumble(){}
                int second;
				"""
		expect = "Error on line 5 col 23: ["
		self.assertTrue((TestParser.checkParser(input, expect, 230)))

	def test_exp_231(self):
		input = """
				void main()
				{
                    x=y;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 231)))
	def test_exp_232(self):
		input = """
				void main()
				{
                    z=x=c=v=b;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 232)))
	def test_exp_233(self):
		input = """
				void main()
				{
                    x||y;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 233)))
	def test_exp_234(self):
		input = """
				void main()
				{
					x && y;
                    x||y;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 234)))
	def test_exp_235(self):
		input = """
				void main()
				{
                    x||y||z||q||p;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 235)))
	def test_exp_236(self):
		input = """
				void main()
				{
                    x||y||z||q||p;
                    x == y;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 236)))
	def test_exp_237(self):
		input = """
				void main()
				{
                    x||y||z||q||p;
                    x == y;
                    x != y;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 237)))
	def test_exp_238(self):
		input = """
				void main()
				{
                    x&&y&&z&&q&&p;
                    x == y;
                    x != y;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 238)))
	def test_exp_239(self):
		input = """
				void main()
				{
                    a==b==c!=d;
                    a!=c==e;
                }
				"""
		expect = "Error on line 4 col 24: =="
		self.assertTrue((TestParser.checkParser(input, expect, 239)))
	def test_exp_240(self):
		input = """
				void amIEmpty(int a){
                    int[] a(){};
                }
				"""
		expect = "Error on line 3 col 23: ["
		self.assertTrue((TestParser.checkParser(input, expect, 240)))
	def test_exp_241(self):
		input = """
				void main()
				{
                    a>b>c>d>=e>=f;
                    a<=d<abc;
                }
				"""
		expect = "Error on line 4 col 23: >"
		self.assertTrue((TestParser.checkParser(input, expect, 241)))
	def test_exp_242(self):
		input = """
				void main()
				{
                    a==b==c!=d;
                    a!=c==e;
                }
				"""
		expect = "Error on line 4 col 24: =="
		self.assertTrue((TestParser.checkParser(input, expect, 242)))
	def test_exp_243(self):
		input = """
				void main()
				{
                    x/y;
                    y*x;
                    a%a;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 243)))
	def test_exp_244(self):
		input = """
				void main()
				{
                    a+b;
                    c-d;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 244)))
	def test_exp_245(self):
		input = """
				void main()
				{
                    x<y;
                    x>y;
                    x>=y;
                    x<=y;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 245)))
	def test_exp_246(self):
		input = """
				void main()
				{
                    a==b==c!=d;
                    x == y;
                }
				"""
		expect = "Error on line 4 col 24: =="
		self.assertTrue((TestParser.checkParser(input, expect, 246)))
	def test_exp_247(self):
		input = """
				void main()
				{
                    x+b+c-y-e+f-g;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 247)))
	def test_exp_248(self):
		input = """
				void main()
				{
                    -------a;
                    !!!!!!b;
                    ----!!-!-!c;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 248)))
	def test_exp_249(self):
		input = """
				void main()
				{
                    x[99];
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 249)))
	def test_exp_250(self):
		input = """
				void main()
				{
                    fooo();
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 250)))
	def test_exp_251(self):
		input = """
				void main()
				{
                    (y--x)[foo() + x + goo( y[10])];
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 251)))
	def test_exp_252(self):
		input = """
				void main()
				{
                    x<y-c*-a[x+foo(true,"test")];
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 252)))
	def test_exp_253(self):
		input = """
				void main()
				{
                    y+x&&!a+3+-d;
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 253)))
	def test_exp_254(self):
		input = """
				void main()
				{
                    (y--x)[foo() + x + goo( y[10])];
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 254)))
	def test_exp_255(self):
		input = """
				void main()
				{
                    (!!x----y)[foo("thy")[x+y]];
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 255)))
	def test_exp_256(self):
		input = """
				void main()
				{
                    (!!x----y)[foo("thy",flase,true,abc,_xyz)[a+b]];
                }
				"""
		expect = "successful"
		self.assertTrue((TestParser.checkParser(input, expect, 256)))

	def test_if_statement_257(self):
		input = """
	            void main(){
                    if(goDown(floor4))
                        if(goDown(floor3))
                            if(goDown(floor2))
                                if(goDown(floor1))
                                    if(goDown(basement))
                                        printf("Hello Annabelle!");
                                    else
                                        goUp();
                                else
                                    goUp();
                            else
                                goUp();
                        else
                            printf("You shouldn't go to the basement :)))");
                    else
                }
	            """
		expect = "Error on line 18 col 16: }"
		self.assertTrue(TestParser.checkParser(input, expect, 257))

	def test_if_statement_258(self):
		input = """
	            void main(){
                    letMakeAStair(true);
                    if(stair){
                        //do nothing
                    }
                    else
                        if(stair){
                            //do nothing}}}}}}
                        }
                        else
                            if(stair){
                                {// do nothing}
                            }}
                            else{
                                {// do nothing}
                }}}
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 258))

	def test_if_statement_259(self):
		input = """
	            void main(){
                    if(1)
                        if(2)
                            if(3)
                                if(4)
                                    if(5)
                    dung();
                    hanh(true);
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 259))

	def test_if_statement_260(self):
		input = """
	            void main(){
                    do{
                        {
                            printf("Easy testcase");
                        }
                    }
                    while(busy == false);
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 260))
	def test_if_statement_261(self):
		input = """
	            void main(int a, float b, string c[],){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    }
	            """
		expect = "Error on line 2 col 50: )"
		self.assertTrue(TestParser.checkParser(input, expect, 261))
	def test_if_statement_262(self):
		input = """
				void main(){
                    if (a >= b) {
                        break;
                    } else {
                        continue;
                    }
	            """
		expect = "Error on line 8 col 13: <EOF>"
		self.assertTrue(TestParser.checkParser(input, expect, 262))

	def test_do_statement_263(self):
		input = """
				void main(){
                    do
                        {do
                            do
                                do
                                    DO;
                                while(x);
                            while(x);}
                        while(x);
                    while(x);
	            """
		expect = "Error on line 9 col 37: }"
		self.assertTrue(TestParser.checkParser(input, expect, 263))

	def test_do_statement_264(self):
		input = """
				void main(){
                    do{
                        sitDown;
                        beHumble;
                    }while(living);
                    whiLe(feeling);
                    whiLe(breathing);
                    whIle(youStillCan);
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 264))

	def test_265(self):
		input = """
				void main(){
                    (!!ab)[foo("true\\n",true,true,abc,_xyz)[a+b]];
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 265))

	def test_266(self):
		input = """
				void main(){
	                (ab)[foo(,true,true,xyz)[x+y]];
	               }
		           """
		expect = "Error on line 3 col 26: ,"
		self.assertTrue(TestParser.checkParser(input, expect, 266))

	def test_267(self):
		input = """
				int main() {
                /* adasd 
                do return; while 1;
            } 
        }*/
	            """
		expect = "Error on line 7 col 13: <EOF>"
		self.assertTrue(TestParser.checkParser(input, expect, 267))

	def test_268(self):
		input = """
				int main() {
                    bob(2)[3 + abc + foo(2)[65 + fob(2) * 7 + (14 || 5)]];
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 268))

	def test_269(self):
		input = """
				void main(string a, boolean b){
                    return a / b * c - d + e != true;
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 269))

	def test_270(self):
		input = """
				void main(string x, boolean y){
                    a*x- y + d * e;
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 270))

	def test_271(self):
		input = """
				void main(){
                    if (a >= b) {
                      break;
                    } else {
                        return a[foo(a[b&&c],"test",true)];
                    }
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 271))

	def test_272(self):
		input = """
				void main(){
            if (a >= b) {
                break;
            } else {
                continue;
            }
        }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 272))

	def test_273(self):
		input = """
				void main(string a, boolean b){
                a =x ;
        }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 273))

	def test_274(self):
		input = """void main(){
            main(a+b[c-d]);
            {
                if (x) {
                    x;
                } else z;
            }
        }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 274))

	def test_275(self):
		input = """
				void thua_so_nguyen_to()
                    {
                        int str_length = strlen(str);
                        int j , i=2, sum;
                        for (i = 0; str[i] != 0; i*i) {
                        if (str[i]==a) 
                            j+1;
                            a+b+c;
                        else {
                            arr[j] = arr[j] * 10 + (str[i] - 48);
                        }
                    }
                }
                fclose(file_o);
                    }
	            """
		expect = "Error on line 4 col 39: ="
		self.assertTrue(TestParser.checkParser(input, expect, 275))

	def test_276(self):
		input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }
            void main(int a, float b, string c[]){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    else{
                        do a+b;b+c;c>d+f;
                        while b[10];
                        if(true)
                        {
                            {{{{{return;}}}}}
                        }
                    }
                    
            }
		        """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 276))
	def test_277(self):
		input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }
            void main(int a, float b, string c[]){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    else
                        do a+b;b+c;c>d+f;
                        while b[10];
                    }
            }
	            """
		expect = "Error on line 11 col 12: }"
		self.assertTrue(TestParser.checkParser(input, expect, 277))
	def test_278(self):
		input = """void main(string a, boolean b){}
                    int[] abc(){
                        if(1) 2+3;
                        else{
                            do a+b;b+c;c>d+f;
                            while x[1];
                        }
                    }

	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 278))
	def test_279(self):
		input = """void main(string a, boolean b){}
                    int[] abc(){
                        if(a+b-c) a+b;
                        else{
                            do a+b;b+c;c>d+f;
                            while b[10];
                    }
                    }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 279))
	def test_280(self):
		input = """void main(){
            if(!!a-----b)
            {
                (foo()*2)[foo("test",true,true,abc,_xyz)[a+b]];
            }
        }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 280))
	def test_281(self):
		input = """int var, var[9];
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 281))
	def test_282(self):
		input = """
				boolean first;
                string createPointer(int a, boolean b[]){
                    {
                        {}
                    }
                }
                float beHumble(){}
                int second;
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 282))
	def test_283(self):
		input = """
				void main(){
                    (x---b)[foo(x,-----a)[a+b]];
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 283))
	def test_284(self):
		input = """
				void main(){
                    (!x---b)[foo(xxx,-----a)[a+b]];
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 284))
	def test_285(self):
		input = """
				void main(){
                    (x---b)[foo(xa,-----a)[a-b]];
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 285))
	def test_286(self):
		input = """void main(){
                abcd==b;
                abc!=b;
	            }"""
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 286))
	def test_287(self):
		input = """void main(){
                a>b+c*-a[b+c+foo(true,"test")];
            }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 287))
	def test_288(self):
		input = """void main(){
                    a>b+c*-a[b+c+foo(true,"test")];
            }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 288))
	def test_289(self):
		input = """
				void main(){}
                    int[] abc(){}
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 289))
	def test_290(self):
		input = """
				void main(){}
                    int[] xx(){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;}
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 290))
	def test_291(self):
		input = """
				oid main(int a, string c[]){boolean aa;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) 
                        if(a*b) b+c;
                    else b+c;}
	            """
		expect = "Error on line 2 col 4: oid"
		self.assertTrue(TestParser.checkParser(input, expect, 291))
	def test_292(self):
		input = """
				void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) 
                        if(a*b) b+c;
                    else b+c;}
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 292))
	def test_293(self):
		input = """
				string[] moreThanICanSay(string toYou){
                    printf("I love you!");
                }
                float[] countNumbers(){}
                int var, var1, var2[999];
                boolean var[999], bool[0];
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 293))
	def test_294(self):
		input = """
				void amIEmpty(int a){
                    int[] a(){};
                }
	            """
		expect = "Error on line 3 col 23: ["
		self.assertTrue(TestParser.checkParser(input, expect, 294))
	def test_295(self):
		input = """
				void main(){
                    if(believe == true)
                        stronger = yes;
                        if(kind == true)
                            better = yes;
                            if(fear == no)
                                success = yes;
                    else{
                        cout("Keep fighting!");
                    }
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 295))
	def test_296(self):
		input = """
				void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1){
                        for(something; something; something){
                            {//do nothing
                        }}
                    }
                    break;
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 296))
	def test_297(self):
		input = """
				void main(){
                    for(test; all; statements)
                        if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                                return true;
                                continue;
                            while(stillRunning());
                    printf("Congrats!");
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 297))
	def test_298(self):
		input = """
				void main(){
                    for(foo(a[3]); !fap(a+b,a*b[3+2*6[3]]); i = i + 3.3e-12)
                        do
                            A = A(((((3)))));
                            B = (3.e-2+0.e3)[(4.5+2)[abc]];
                        while(A || B && C || D && E == F);
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 298))
	def test_299(self):
		input = """
				void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        if(shitHappens)
                            whoCares();
                    for(exp; exp; exp){
                        {
                            stillWhoCares();
                        }
                    }
                    {
                        nowThisIsFun();
                    }
                }
	            """
		expect = "successful"
		self.assertTrue(TestParser.checkParser(input, expect, 299))
