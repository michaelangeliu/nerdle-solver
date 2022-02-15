from multiprocessing import Pool
from math import log2

def compare_equations(eq_a, eq_b):
    match_str = ''

    for i, char in enumerate(eq_a):
        if char == eq_b[i]:
            match_str += 'g'
        elif char in eq_b:
            match_str += 'p'
        else:
            match_str += 'b'

    return match_str

def calculate_expected_information(eq, equation_set):
    with open('nerdle_bits.txt', 'a') as f:
        answer = dict()
        for alt_eq in equation_set:
            match_pattern = compare_equations(eq, alt_eq)
            if answer.get(match_pattern):
                answer[match_pattern] += 1
            else:
                answer[match_pattern] = 1

        patterns = answer.keys()
        total_possibilities = len(equation_set)
        expected_information = []
        for pattern in patterns:
            probability = answer[pattern] / total_possibilities
            bits = log2(1/probability)
            expected_value = probability * bits
            expected_information.append(expected_value)

        f.write(f"\'{eq}\': {sum(expected_information)}\n")
        print(f"\'{eq}\': {sum(expected_information)}")
        return expected_information

if __name__ == "__main__":
    with open('nerdle.txt', 'r') as f:
        equations = f.readlines()
        formatted_equations = list(map(lambda x: x.strip(), equations))

        equations_tuple = tuple((eq, formatted_equations) for eq in formatted_equations)

        with Pool(8) as p:
            answer = p.starmap(calculate_expected_information, equations_tuple)

    with open('nerdle_bits.txt', 'r') as f:
        equations = f.readlines()
        formatted_equations = list(map(lambda x: x.strip().split(': ', 1), equations))

        ranked_equations = map(lambda eq: f"{eq[1]}\t{eq[0]}\n", formatted_equations)

        with open('nerdle_ranking.txt', 'w') as g:
            for eq in ranked_equations:
                g.write(eq)

