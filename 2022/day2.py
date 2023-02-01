import os


ROCK = 0
PAPER = 1
SCISSORS = 2

OPPONENT_CHOICE_INDEX = 0
PLAYER_CHOICE_INDEX = 2
RESULT_INDEX = 2

WIN = 6
DRAW = 3
LOSE = 0

RULEBOOK = {
    #keys for the opponent's choices
    'A':ROCK,
    'B':PAPER,
    'C':SCISSORS,

    #score associated with each choice
    ROCK:1,
    PAPER:2,
    SCISSORS:3
}


def rps_rule_decryption1(input_path:str) -> int:
    """
    Returns the player's score for the rock-paper-scissors tournament with the first decryption of the guide.
    """
    score = 0

    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            opponent_choice = RULEBOOK[line[OPPONENT_CHOICE_INDEX]]
            encrypted_char = line[PLAYER_CHOICE_INDEX]
            player_choice = ROCK if encrypted_char=='X' else PAPER if encrypted_char == 'Y' else SCISSORS

            score += RULEBOOK[player_choice]
            # taken from Christopher Shroba's message on https://stackoverflow.com/questions/41457556/rock-paper-scissors-get-winner-mathematically#answers
            if (opponent_choice + 1) % 3 == player_choice:
                score += WIN
            elif  player_choice == opponent_choice:
                score += DRAW
    return score


def rps_rule_decryption2(input_path:str) -> int:
    """
    Returns the player's score for the rock-paper-scissors tournament with the second decryption of the guide.
    """
    score = 0

    with open(input_path, 'r', encoding="utf-8") as file:
        for line in file:
            opponent_choice = RULEBOOK[line[OPPONENT_CHOICE_INDEX]]
            encrypted_char = line[RESULT_INDEX]
            result = LOSE if encrypted_char=='X' else DRAW if encrypted_char == 'Y' else WIN
            score += result

            #determine what the player picked based on the opponent's choice and the result, then lookup the corresponding score in the rulebook
            if result == DRAW:
                score += RULEBOOK[opponent_choice]
            elif result == WIN:
                score += RULEBOOK[(opponent_choice+1)%3]
            else : #result == LOSE
                score += RULEBOOK[(opponent_choice-1)%3]
    return score


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day2.txt")
    print(f"Rock paper scissors tournament score with the first decryption : {rps_rule_decryption1(path)}.")
    print(f"Rock paper scissors tournament score with the second decryption : {rps_rule_decryption2(path)}.")