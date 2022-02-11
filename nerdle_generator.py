zero_set = ['0']
number_set = ['1','2','3','4','5','6','7','8','9']
equals_set = ['=']
operator_set = ['+','-','*','/']

f = open("nerdle.txt", "a")

def last_character_is_equals(curr_string):
    return curr_string[-1] == '='

def last_character_is_divider(curr_string):
    return curr_string[-1] == '/'

def last_character_is_operator(curr_string):
    return curr_string[-1] in operator_set

def last_character_is_starting_zero(curr_string):
    return curr_string[-1] in zero_set and curr_string[-2] in operator_set

def select_char_set(curr_string):
    if len(curr_string) == 0:
        return (zero_set + number_set)
    elif len(curr_string) == 1:
        if curr_string[-1] in zero_set: return operator_set
        else: return (zero_set + number_set + operator_set)
    elif len(curr_string) == 2:
        if last_character_is_divider(curr_string): return number_set
        elif last_character_is_operator(curr_string): return (zero_set + number_set)
        else: return (zero_set + number_set + operator_set)
    elif len(curr_string) == 3:
        if last_character_is_divider(curr_string): return number_set
        elif last_character_is_operator(curr_string): return (zero_set + number_set)
        elif last_character_is_starting_zero(curr_string): return operator_set
        else: return (zero_set + number_set + operator_set)
    elif len(curr_string) == 4:
        if last_character_is_divider(curr_string): return number_set
        elif last_character_is_operator(curr_string): return (zero_set + number_set)
        elif last_character_is_starting_zero(curr_string): return operator_set
        else: return (zero_set + number_set + operator_set + equals_set)
    elif len(curr_string) == 5:
        if last_character_is_divider(curr_string): return number_set
        elif last_character_is_operator(curr_string): return (zero_set + number_set)
        elif last_character_is_equals(curr_string): return number_set
        elif last_character_is_starting_zero(curr_string): return equals_set
        else: return (zero_set + number_set + equals_set)
    elif len(curr_string) == 6:
        if last_character_is_equals(curr_string): return number_set
        elif last_character_is_starting_zero(curr_string): return equals_set
        else: return (zero_set + number_set + equals_set)
    elif len(curr_string) == 7:
        return (zero_set + number_set)
    else:
        return []

for c1 in select_char_set(f""):
    for c2 in select_char_set(f"{c1}"):
        for c3 in select_char_set(f"{c1}{c2}"):
            for c4 in select_char_set(f"{c1}{c2}{c3}"):
                for c5 in select_char_set(f"{c1}{c2}{c3}{c4}"):
                    for c6 in select_char_set(f"{c1}{c2}{c3}{c4}{c5}"):
                        for c7 in select_char_set(f"{c1}{c2}{c3}{c4}{c5}{c6}"):
                            for c8 in select_char_set(f"{c1}{c2}{c3}{c4}{c5}{c6}{c7}"):
                                eq = f"{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}"
                                if eq.count('=') != 1:
                                    continue

                                eq_split = eq.split('=', 1)
                                eq_str = eq_split[0]
                                sum_str = eq_split[1]

                                if (eval(eq_str) == int(sum_str)):
                                    f.write(eq + '\n')
                                    print(eq)
f.close()