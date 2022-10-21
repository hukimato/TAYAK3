from Parser import Parser
from PDA import PDA

F1 = 'test1.txt'
F2 = 'test2.txt'
F3 = 'test3.txt'
F = 'test.txt'

F_str = 'a+a*a'
F1_str = 'm/abc/'
F1_str1 = '!/abc/'
F1_str2 = '/abc/'
F2_str = 'abxy'
F3_str = 'ba'


parser = Parser(F1, F1_str2)
M = parser.run()
print(parser)
PDA = PDA(M)
story = PDA.run(M)
if story:
    print('Строка допускается автоматом')
    for mov in story:
        print(mov)
else:
    print('NOT OK')
