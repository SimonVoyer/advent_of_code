import os, numpy as np


BINGO_SIZE = 5


def giant_squid_bingo(input_path:str) -> list:
    """
    Anticipate the score of the boards that are first and last to win to appease a giant squid.
    """
    #generate bingo boards from the input
    bingo_boards = []
    with open(input_path, 'r', encoding="utf-8") as file:
        drawn_numbers = next(file, None).replace('\n', '').split(',')
        line = next(file, None)
        while line:
            bingo_board = {}
            for i in range(BINGO_SIZE):
                row = next(file,None).split()
                for j in range(BINGO_SIZE):
                    bingo_board[row[j]] = (i,j)
            bingo_boards.append(bingo_board)
            line = next(file, None)

    #generate validation boards
    nb_of_boards = len(bingo_boards)
    validation_boards = []
    for _ in range(nb_of_boards):
        validation_boards.append(np.zeros((BINGO_SIZE, BINGO_SIZE)))
    
    #find the winning board
    order_of_wins = {} #add ordered dict entries with key = board index and value = number index
    for i in range(len(drawn_numbers)):
        number = drawn_numbers[i]

        for j in range(nb_of_boards):
            hasnt_won = j not in order_of_wins
            game_board = bingo_boards[j]
            validation_board = validation_boards[j]

            #add flag if the number is on the bingo card
            if number in game_board and hasnt_won:
                indexes = game_board[number]
                validation_board[indexes[0]][indexes[1]] = 1
            
            #check if the flags in the board sums to 5 on any axis
            if np.isin(5, np.sum(validation_board, axis=0)) or np.isin(5,np.sum(validation_board, axis=1)):
                if hasnt_won:
                    order_of_wins[j] = i

    #calculate the scores
    ordered_board_indexes = list(order_of_wins.keys())
    ordered_number_indexes = list(order_of_wins.values())

    selected_boards = [bingo_boards[ordered_board_indexes[0]], bingo_boards[ordered_board_indexes[-1]]]
    selected_validations = [validation_boards[ordered_board_indexes[0]], validation_boards[ordered_board_indexes[-1]]]
    selected_numbers = [drawn_numbers[ordered_number_indexes[0]], drawn_numbers[ordered_number_indexes[-1]]]

    scores = []
    for i in range(len(selected_boards)):
        score = 0
        bingo_board = selected_boards[i]
        validation_board = selected_validations[i]
        for key in bingo_board:
            indexes = bingo_board[key]
            if not validation_board[indexes[0]][indexes[1]]:
                score += int(key)
        score *= int(selected_numbers[i])
        scores.append(score)
    return scores


if __name__ == "__main__":
    cwd = os.getcwd()
    path = os.path.join(cwd, "input", "day4.txt")
    print(f"Winning and losing board scores : {giant_squid_bingo(path)}.")