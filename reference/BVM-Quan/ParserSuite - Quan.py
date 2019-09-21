import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    #VAR DECLARE
    def test_var_decl_1(self):
        
        input = """ string ;
            """
        expect = "Error on line 1 col 8: ;"
        self.assertTrue(TestParser.checkParser(input,expect,200))
    def test_var_decl_2(self):
        
        input = """int a[10];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_var_decl_3(self):
        
        input = """int a,b[56];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_var_decl_4(self):
        
        input = """float a,b,c,a[10];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_var_decl_5(self):
        
        input = """ boolean _int;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_var_decl_6(self):
        
        input = """float a,b,c,d[12];
                    int a,b[12];
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_var_decl_7(self):
        
        input = """boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_var_decl_8(self):
        
        input = """void main(){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    float a[25];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    #func decl
    def test_func_decl_1(self):
        
        input = """void main(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_func_decl_2(self):
        
        input = """int[] abc(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_func_decl_3(self):
        
        input = """void main(){}
                    int[] abc(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    def test_func_decl_4(self):
        
        input = """void main(int a, float b, string c[]){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_func_decl_5(self):
        
        input = """void main(){}
                int[] abc(){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_func_decl_6(self):
        
        input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))
    #if statement
    def test_func_decl_7(self):
        
        input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    else b+c;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_func_decl_8(self):
        
        input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_func_decl_9(self):
        
        input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) 
                        if(a*b) b+c;
                    else b+c;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_func_decl_10(self):
        
        input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) 
                        if(a*b) b+c;
                        else b+c;
                    else a[10]=2;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_func_decl_11(self):
        
        input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) 
                        if(a*b) b+c;
                    else b+c;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_func_decl_12(self):
        
        input = """void main(int a, float b, string c[]){boolean a;
                    int b,b[10];
                    string c[12],d,e,f;
                    if(a+b-c) 
                        if(a*b) 
                        if((a[a[b+c]]))
                        if(true) b/c;
                    else b+c;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    #DOWHILE
    def test_func_decl_13(self):
        
        input = """void main(){
            do a+b;b+c;c>d+f;
            while b[10];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_func_decl_14(self):
        
        input = """void main(){
            do a+b;b+c;c>d+f;
            while (b[10]);
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_func_decl_15(self):
        
        input = """void main(){
            do a+b; while b[10];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    #forState
    def test_func_decl_16(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1) 
            do a+b; while b[10];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_func_decl_17(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 for(i=0;i<a[10];i+1)
                    do a+b; while b[10];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_func_decl_18(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 for(i=0;i<a[10];i+1)
                    for(i=0;i<a[10];i+1)
                        do a+b; while b[10];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    #continue
    def test_func_decl_19(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 continue;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_func_decl_20(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 continue;continue;continue;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    #break state
    def test_func_decl_21(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 break;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_func_decl_22(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 break;break;break;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    #return
    def test_func_decl_23(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_func_decl_24(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 return;return;return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_func_decl_25(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                return a+b+c-d;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_func_decl_26(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 return;return a+b+c-d;return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    #expState
    def test_exp_1(self):
        
        input = """void main(){
                a=b;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_exp_2(self):
        
        input = """void main(){
                a=b=c=d=e;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_exp_3(self):
        
        input = """void main(){
                a||b;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_exp_4(self):
        
        input = """void main(){
                a||b||c||d||e;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_exp_5(self):
        
        input = """void main(){
            for(i=0;i<a[10];i+1)
                 return;return a+b+c-d;return;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_exp_6(self):
        
        input = """void main(){
                a&&b;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_exp_7(self):
        
        input = """void main(){
                a&&b&&c&&d;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_exp_8(self):
        
        input = """void main(){
                a==b;
                a!=b;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    def test_exp_9(self):
        
        input = """void main(){
                a==b==c!=d;
                a!=c==e;
            }"""
        expect = "Error on line 2 col 20: =="
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_exp_10(self):
        
        input = """void main(){
                a>b;
                a<b;
                a>=b;
                a<=b;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_exp_11(self):
        
        input = """void main(){
                a>b>c>d>=e>=f;
                a<=d<abc;
            }"""
        expect = "Error on line 2 col 19: >"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_exp_12(self):
        
        input = """void main(){
            a+b;
            c-d;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_exp_13(self):
        
        input = """void main(){
                a+b+C-d-e+f-g;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_exp_14(self):
        
        input = """void main(){
                a/b;
                a*b;
                a%b;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_exp_15(self):
        
        input = """void main(){
                a*b*c/d/e%f%g;
                a*b/c%f*g;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_exp_16(self):
        
        input = """void main(){
                -a;
                !b;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    def test_exp_17(self):
        
        input = """void main(){
                -------a;
                !!!!!!b;
                ----!!-!-!c;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_exp_18(self):
        
        input = """void main(){
                a[12];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_exp_19(self):
        
        input = """void main(){
                foo();
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_exp_20(self):
        
        input = """void main(){
                foo(a+b,c*d,true,false,"test");
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    #Mix exp
    def test_exp_21(self):
        
        input = """void main(){
                a[b+foo(a+b*(c>d),true,"test",-----a[1])];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_exp_22(self):
        
        input = """void main(){
                a&&!b+c+-d;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    def test_exp_23(self):
        
        input = """void main(){
                a>b+c*-a[b+c+foo(true,"test")];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_exp_24(self):
        
        input = """void main(){
                (a----b)[foo() + 2+goo(a[2])];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_exp_25(self):
        
        input = """void main(){
            (!!a-----b)[foo("test")[a+b]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_exp_26(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",-----a)[a+b]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_exp_27(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",!!!!b)[a+b]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_exp_28(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    #block
    def test_block_1(self):
        
        input = """void main(){
            {{{{}}}}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_block_2(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            float a;
            {{{{a+b-c;}}}}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_block_3(self):
        
        input = """void main(){
            {a+b;}
            {b+c;}
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    #mix all
    def test_all_1(self):
        
        input = """
            void main(int a, float b, string c[],){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    }"""
        expect = "Error on line 4 col 49: )"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_all_2(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }
            void main(int a, float b, string c[],){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    {
                        do a+b;b+c;c>d+f;
                        while b[10];
                    }
            }"""
        expect = "Error on line 4 col 49: )"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_all_3(self):
        
        input = """void main({
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }
            void main(int a, float b, string c[],){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    {
                        do a+b;b+c;c>d+f;
                        while b[10];
                    }
            }"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_all_4(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }
            void main(int a, float b, string c[]){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    else{
                        do a+b;b+c;c>d+f;
                        while b[10];
                    }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_all_5(self):
        
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
            }"""
        expect = "Error on line 11 col 12: }"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_all_6(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }
            void main(int a, float b, string c[]){
                    string c[12],d,e,f;
                    if(a+b-c) a+b;
                    {
                        do 
                        {
                            a+b;b+c;c>d+f;
                            do
                            {
                                foo(a[2]);
                            }
                        }
                        while b[10];
                    }
            }"""
        expect = "Error on line 15 col 24: }"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_all_7(self):
        
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
                            return;
                        }
                    }
                    
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_all_8(self):
        
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
                    
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_all_9(self):
        
        input = """int main()
                    {
                        int luachon;
                        menu();
                        scanf("%d",luachon);
                        switch(luachon);
                        {}
                    return 0;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_all_10(self):
        
        input = """void thua_so_nguyen_to()
                {
                    int str_length = strlen(str);
                    int j , i, sum;
                    for (i = 0; str[i] != 0; i*i) {
                    if (str[i]==a) {
                        j+1;
                    }
                    else {
                        arr[j] = arr[j] * 10 + (str[i] - 48);
                    }
                }
                }
                fclose(file_o);

                }"""
        expect = "Error on line 3 col 35: ="
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_all_11(self):
        
        input = """void thua_so_nguyen_to()
                    {
                        int str_length = strlen(str);
                        int j , i=2, sum;
                        for (i = 0; str[i] != 0; i*i) {
                        if (str[i]==a) {
                            j+1;
                        }
                        else {
                            arr[j] = arr[j] * 10 + (str[i] - 48);
                        }
                    }
                }
                fclose(file_o);
                    }"""
        expect = "Error on line 3 col 39: ="
        self.assertTrue(TestParser.checkParser(input,expect,275))
    def test_all_12(self):
        
        input = """void thua_so_nguyen_to()
                    {
                        fflush(stdin);
                        int arr[MAX];
                        char str[2048];
                        printf("Input: ");
                        fprintf(file_o,"*********NEW TEST*********\\n");
                        for(int m=0;m<=j;m++)
                        {
                            int k=2,temp;
                            fprintf(file_o,"%d=",arr[m]);
                            while (arr[m] != 1)
                            {
                                if (arr[m] % k == 0)
                                {
                                    if(arr[m]!=temp)
                                    fprintf(file_o,"*");
                                    fprintf(file_o,"%d",k);
                                    arr[m] = k;
                                }

                                else
                                    k+2;
                            }
                        }
                        fclose(file_o);

                    }"""
        expect = "Error on line 4 col 32: MAX"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_all_13(self):
        
        input = """void thua_so_nguyen_to()
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
                    }"""
        expect = "Error on line 3 col 39: ="
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_all_14(self):
        
        input = """void main(string a, boolean b){}
                    int[] abc(){
                        if(a+b-c) a+b;
                        else{
                            do a+b;b+c;c>d+f;
                            while b[10];
                    }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_all_15(self):
        
        input = """void main(string a, boolean b){
                        boolean a;
                        int b,b[10];
                        string c[12],d,e,f;
                    }
                    int[] abc(){}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_all_16(self):
        
        input = """void main(string a, boolean b){
            a - b + c / d * e;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_all_17(self):
        
        input = """void main(string a, boolean b){
            if () a + b;
        }"""
        expect = "Error on line 2 col 16: )"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_all_18(self):
        
        input = """void main(string a, boolean b){
            if (a;) a;
        }"""
        expect = "Error on line 2 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_all_19(self):
        
        input = """void main(string a, boolean b){
            if (a) else ;
        }"""
        expect = "Error on line 2 col 19: else"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_all_20(self):
        
        input = """int main() {
                /* adasd 
                do return; while 1;
            } 
        }*/"""
        expect = "Error on line 5 col 11: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_all_21(self):
        
        input = """int main() {
            bob(2)[3 + abc + foo(2)[65 + fob(2) * 7 + (14 || 5)]];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    def test_all_22(self):
        
        input = """void main(string a, boolean b){
            return a / b * c - d + e != true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_all_23(self):
        
        input = """void main(string a, boolean b){
            do ; while a;
        }"""
        expect = "Error on line 2 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_all_24(self):
        
        input = """void main(string a, boolean b){
            do a; while 
        }"""
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_all_25(self):
        
        input = """void main(string a, boolean b){
            {{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_all_26(self):
        
        input = """void main(){
            main(a+b[c-d]);
            {
                if (a) {
                    a;
                } else b;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_all_27(self):
        
        input = """void main(){
            if (a >= b) {
                break;
            } else {
                continue;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_all_28(self):
        
        input = """void main(){
            if (a >= b) {
                break;
            } else {
                return a[foo(a[b&&c],"test",true)];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_all_29(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            do{
                if(!!!a)
                {
                    return;
                }
            }while (a>0)
            }"""
        expect = "Error on line 9 col 12: }"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_all_30(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_all_31(self):
        
        input = """void main(){
            (!!ab)[foo("true\\n",true,true,abc,_xyz)[a+b]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    def test_all_32(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b]];
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_all_33(self):
        
        input = """void main(){
            if(!!a-----b)
            {
                (foo()*2)[foo("test",true,true,abc,_xyz)[a+b]];
            }
            
            }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_all_34(self):
        
        input = """void main(){
                do
                {
                    a+b;
                }
                while ;
                do{

                }while(a>0);
            }"""
        expect = "Error on line 6 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_all_35(self):
        
        input = """void main(){
            (!!a-----b)[foo("test",true,true,abc,_xyz)[a+b][a][2]];
            }"""
        expect = "Error on line 2 col 59: ["
        self.assertTrue(TestParser.checkParser(input,expect,299))
