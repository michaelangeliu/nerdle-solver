zero_set = [0]
number_set = [1,2,3,4,5,6,7,8,9]
equals_set = ['=']
operator_set = ['+','-','*','/']

character_set = zero_set + number_set + operator_set + equals_set
character_set_wo_equals = zero_set + number_set + operator_set

def should_skip_curr_char(prev_char, curr_char):
    return prev_char in (operator_set + equals_set)\
        and (
            curr_char in (operator_set + equals_set)
            or curr_char == 0
        )

f = open("nerdle.txt", "a")
count = 0

for c1 in number_set:
    for c2 in character_set_wo_equals:
        if c1 == 0 and c2 in number_set:
            continue
        for c3 in (number_set if ('=' in f"{c1}{c2}") else character_set):
            if (should_skip_curr_char(c2, c3)):
                continue
            for c4 in (number_set if ('=' in f"{c1}{c2}{c3}") else character_set):
                if (should_skip_curr_char(c3, c4)):
                    continue
                for c5 in (number_set if ('=' in f"{c1}{c2}{c3}{c4}") else character_set):
                    if (should_skip_curr_char(c4, c5)):
                        continue
                    for c6 in (number_set if ('=' in f"{c1}{c2}{c3}{c4}{c5}") else character_set):
                        if (should_skip_curr_char(c5, c6)):
                            continue
                        for c7 in (number_set if ('=' in f"{c1}{c2}{c3}{c4}{c5}{c6}") else character_set):
                            if (should_skip_curr_char(c6, c7)):
                                continue
                            for c8 in number_set:
                                eq = f"{c1}{c2}{c3}{c4}{c5}{c6}{c7}{c8}"
                                if eq.count('=') != 1:
                                    continue

                                eq_split = eq.split('=', 1)
                                if (eval(eq_split[0]) == int(eq_split[1])):
                                    count += 1
                                    f.write(eq + '\n')
                                    if count % 100 == 0:
                                        print(eq)
f.close()
print(count)