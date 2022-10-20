class PDA:

    def __init__(self, M):
        self.M = M

    def run(self, M):
        transision_story = []
        input_string = list(M['d4'][1][::-1])
        stack = M['d4'][2]
        rules = M['d1']
        string_char = input_string.pop() if input_string else ''
        stack_char = stack.pop() if stack else 'h0'

        if len(stack) > 100:
            return False
        while True:
            transision_story.append(['s0', [string_char] + input_string[::-1], stack + [stack_char]])
            if str.isupper(stack_char):  # Если символ Недетерминированный
                # Находим правило для перехода
                current_rule = None
                for rule in rules:
                    if rule[2] == stack_char:
                        current_rule = rule
                        break
                possible_ends = current_rule[4]

                if len(possible_ends) == 1:  # Если переход детерминированный
                    stack += list(possible_ends[0])
                    stack_char = stack.pop() if stack else 'h0'
                else:
                    for end in possible_ends:
                        M_new = M
                        M_new['d4'] = ['s0', [string_char]+input_string[::-1], stack + list(end)]
                        new_story = self.run(M_new)
                        if new_story:
                            return transision_story + new_story
                    return False

            else:  # Если символ Детерминированный
                if string_char == stack_char:
                    string_char = input_string.pop() if input_string else ''
                    stack_char = stack.pop() if stack else 'h0'
                elif stack_char == 'h0' and string_char == '':
                    return transision_story
                else:
                    return False




