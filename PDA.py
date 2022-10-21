class PDA:

    def __init__(self, M):
        self.M = M

    def run(self, M, level=0):
        transision_story = []
        input_string = list(M['d4'][1][::-1])
        stack = M['d4'][2]
        rules = M['d1']
        string_char = input_string.pop() if input_string else ''
        stack_char = stack.pop() if stack else 'h0'
        if level > 10 or len(stack) > 30:
            return False
        while True:
            transision_story.append(['s0', [string_char] + input_string[::-1], (stack + [stack_char])[::-1]])

            if str.isupper(stack_char):  # Если символ Недетерминированный
                # Находим правило для перехода
                current_rule = None
                for rule in rules:
                    if rule[2] == stack_char:
                        current_rule = rule
                        break
                possible_ends = current_rule[4]

                if len(possible_ends) == 1:  # Если переход детерминированный
                    stack += list(possible_ends[0])[::-1]
                    stack_char = stack.pop() if stack else 'h0'
                else:
                    for end in possible_ends:
                        M_new = M
                        M_new['d4'] = ['s0', [string_char]+input_string[::-1], stack + list(end)[::-1]]
                        new_story = self.run(M_new, level+1)
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




