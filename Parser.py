import re

class Parser:

    def __init__(self, file_name, input_string):
        self.file_name = file_name
        self.input_string = input_string
        self.M = {}
        self.M['Z'] = set()
        self.M['P'] = set()
        self.M['d1'] = []

    def run(self):
        with open(self.file_name) as file:

            line = file.readline()
            while line and line != '\n':
                line = re.sub(r"\n", '', line)
                line = line.split('>', 1)
                line[1] = line[1].split('|')

                # Получаем множество Терминальных символов Z
                self.M['Z'].add(line[0])
                for string in line[1]:
                    self.M['Z'].update(set(string))

                # Фильтруем из Z терминальные символы P
                self.M['P'] = set(filter(lambda s: not str.isupper(s), self.M['Z']))

                # Получаем функции перехода первого типа
                if line[0] == 'E':
                    self.M['d1'].append(['s0', 'ANY_SYMBOL', line[0], 's0', line[1]])
                else:
                    self.M['d1'].append(['s0', '', line[0], 's0', [string[::-1] for string in line[1]]])

                line = file.readline()


        # Получаем функции перехода второго типа
        self.M['d2'] = []
        for s in self.M['P']:
            self.M['d2'].append(['s0', s, s, 's0', ''])

        self.M['d3'] = ['s0', '', 'h0', 's0', '']

        stack = list(self.M['d1'][0][2])
        self.M['d4'] = ['s0', self.input_string, ['h0']+stack]

        return self.M

    def __str__(self):
        M = self.M
        for key in M.keys():
            print(f'------------------------------- {key} ---------------------')
            if key == 'd1' or key == 'd2':
                for item in M[key]:
                    print(item)
            else:
                print(M[key])
        return ''