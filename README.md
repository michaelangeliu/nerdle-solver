# Nerdle Solver

## Background

The game: [https://nerdlegame.com](https://nerdlegame.com)

The inspiration: [https://www.youtube.com/watch?v=v68zYyaEmEA](https://www.youtube.com/watch?v=v68zYyaEmEA)

## Usage

1. Install python3
2. `python3 nerdle_generatory.py` - writes to "nerdle.txt" with a hypothetical list of valid nerdle combinations based on a state machine of which characters are valid fo each position, based on the previously selected characters in the equation
3. `python3 nerdle_parser.py` - reads "nerdle_sorted.txt" and writes to "nerdle_matches.txt" to determine the possible matches. Using Pool(8) to take advantage of a computer with multiple cores, depending on your system, you may need to change that number. "nerdle_sorted.txt" is just an alphabetized version of "nerdle.txt" from above, which isn't entirely necessary, but helped with my readability.
4. `python3 nerdle_analyzer.py` - reads "nerdle_matches.txt" and writes to "nerdle_bits.txt" and "nerdle_ranking.txt". Given the matches, tries to skip some of the match generation writing and jump directly into analysis of bits of information