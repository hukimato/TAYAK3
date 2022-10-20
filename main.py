from Parser import Parser
from PDA import PDA

F1 = 'test1.txt'
F2 = 'test2.txt'
F3 = 'test3.txt'
F = 'test.txt'

parser = Parser(F, 'a+a*a')
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

# for key in M.keys():
#     print(f'-------------------------------{key} ---------------------')
#     if key == 'd1' or key == 'd2':
#         for item in M[key]:
#             print(item)
#     else:
#         print(M[key])