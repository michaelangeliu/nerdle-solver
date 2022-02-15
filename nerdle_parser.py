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

def generate_all_match_patterns(eq, equation_set):
    with open('nerdle_matches.txt', 'a') as f:
        answer = dict()
        for alt_eq in equation_set:
            match_pattern = compare_equations(eq, alt_eq)
            if answer.get(match_pattern):
                answer[match_pattern] += 1
            else:
                answer[match_pattern] = 1

        f.write(f"\'{eq}\': {answer}\n")
        print(eq)
        return answer

if __name__ == "__main__":
    with open('nerdle_sorted.txt', 'r') as f:
        equations = f.readlines()
        formatted_equations = list(map(lambda x: x.strip(), equations))

        equations_tuple = tuple((eq, formatted_equations) for eq in formatted_equations)

        with Pool(8) as p:
            answer = p.starmap(generate_all_match_patterns, equations_tuple)
