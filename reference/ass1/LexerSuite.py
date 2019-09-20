import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def Test_001(self):
        self.assertTrue(TestLexer.test("_ABC_abc", "_ABC_abc,<EOF>", 1))
    
    def Test_002(self):
        self.assertTrue(TestLexer.test("_123 123", "_123, 123,<EOF>", 2))

    def Test_003(self):
        self.assertTrue(TestLexer.test("123123", "123123,<EOF>", 3))
    
    def Test_004(self):
        self.assertTrue(TestLexer.test("CSVNmmZZZ", "CSVNmmZZZ,<EOF>", 4))

    def Test_005(self):
        self.assertTrue(TestLexer.test("VN123", "VN123,<EOF>", 5))

    def Test_006(self):
        self.assertTrue(TestLexer.test("123_VN123", "123, _VN123,<EOF>", 6))

    def Test_007(self):
        self.assertTrue(TestLexer.test("bla_bla_bla", "bla_bla_bla,<EOF>", 7))

    def Test_008(self):
        self.assertTrue(TestLexer.test("ONE_TWO_THREE", "ONE_TWO_THREE,<EOF>", 8))

    def Test_009(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_2_THREE,<EOF>", 9))

    def Test_010(self):
        self.assertTrue(TestLexer.test("0ONE_2_THREE4_FIVE", "0, ONE_2_THREE4_FIVE,<EOF>", 10))

    def Test_011(self):
        self.assertTrue(TestLexer.test("", "ONE_, 2, _THREE,<EOF>", 11))

    def Test_012(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 12))

    def Test_013(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 13))

    def Test_014(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 14))

    def Test_015(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 15))

    def Test_016(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 16))

    def Test_017(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 17))
    
    def Test_018(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 18))
    
    def Test_019(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 19))
    
    def Test_020(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 20))
    
    def Test_021(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 21))
    
    def Test_022(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 22))
    
    def Test_023(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 23))
    
    def Test_024(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 24))
    
    def Test_025(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 25))
    
    def Test_026(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 26))

    def Test_027(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 27))

    def Test_028(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 28))

    def Test_029(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 29))

    def Test_030(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 30))

    def Test_031(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 31))

    def Test_032(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 32))

    def Test_033(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 33))

    def Test_034(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 34))

    def Test_035(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 35))

    def Test_036(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 36))

    def Test_037(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 37))

    def Test_038(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 38))

    def Test_039(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 39))

    def Test_040(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 40))

    def Test_041(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 41))

    def Test_042(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 42))

    def Test_043(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 43))

    def Test_044(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 44))

    def Test_045(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 45))

    def Test_046(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 46))

    def Test_047(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 47))

    def Test_048(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 48))

    def Test_049(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 49))

    def Test_050(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 50))

    def Test_051(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 51))

    def Test_052(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 52))

    def Test_053(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 53))

    def Test_054(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 54))

    def Test_055(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 55))

    def Test_056(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 56))

    def Test_057(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 57))

    def Test_058(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 58))

    def Test_059(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 59))

    def Test_060(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 60))

    def Test_061(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 61))

    def Test_062(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 62))

    def Test_063(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 63))

    def Test_064(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 64))

    def Test_065(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 65))

    def Test_066(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 66))

    def Test_067(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 67))

    def Test_068(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 68))

    def Test_069(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 69))

    def Test_070(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 70))

    def Test_071(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 71))

    def Test_072(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 72))

    def Test_073(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 73))

    def Test_074(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 74))

    def Test_075(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 75))

    def Test_076(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 76))

    def Test_077(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 77))

    def Test_078(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 78))

    def Test_079(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 79))

    def Test_080(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 80))

    def Test_081(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 81))

    def Test_082(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 82))

    def Test_083(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 83))

    def Test_084(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 84))

    def Test_085(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 85))

    def Test_086(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 86))

    def Test_087(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 87))

    def Test_088(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 88))

    def Test_089(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 89))

    def Test_090(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 90))

    def Test_091(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 91))

    def Test_092(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 92))

    def Test_093(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 93))

    def Test_094(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 94))

    def Test_095(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 95))

    def Test_096(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 96))

    def Test_097(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 97))

    def Test_098(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 98))

    def Test_099(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 99))

    def Test_100(self):
        self.assertTrue(TestLexer.test("ONE_2_THREE", "ONE_, 2, _THREE,<EOF>", 100))
