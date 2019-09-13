# PPL-Assignment1
Lexer &amp; Recognizer

HCMC University of Technology Faculty of Computer Science & Engineering
Assignment 1
Lexer & Recognizer
   Author
Dr. Nguyen Hua Phung
August 25, 2019

In this assignment, you are required to submit three files MC.g4, LexerSuite.py and Parser- Suite.py. Note that you must submit 3 files, NOT compress them.
• Modify MC.g4 to detect tokens and check grammar of MC programs. • Make 100 testcases in LexerSuite.py to test your lexer rule.
• For lexical errors, please throw the exception as follows:
– ErrorToken(<char>): when the lexer detects an unrecognized character
– UnclosedString(<unclosed string>): when the lexer detects an unterminated string. The unclosed string is from the beginning of the string (without the quote) to the newline or end of file, exclusively.
– IllegalEscapeInString(<wrong string): when the lexer detects an illegal escape in string. The wrong string is from the beginning of the string (without the quote) to the illegal escape, inclusively.
• Make 100 testcases in ParserSuite.py to test your grammar rules. You can assume that there is at most one error in each test case.
The deadline of both phases of assignment 1 is announced in the class website.
