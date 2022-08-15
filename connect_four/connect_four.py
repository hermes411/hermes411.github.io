#Connect Four
#Rules:
#   This is a player vs player game. Players take turns choosing a column number.

class Board:

    #constructor
    def __init__(self):
        self.all_nums = ["1", "2", "3", "4", "5", "6", "7"]
        self.dash_line = ["---", "-", "---", "-", "---", "-", "---", "-", "---", "-", "---", "-", "---"]
        self.num_row = [" 1 ", " ", " 2 ", " ", " 3 ", " ", " 4 ", " ", " 5 ", " ", " 6 ", " ", " 7 "]
        self.row6 = ["   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   "]
        self.row5 = ["   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   "]
        self.row4 = ["   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   "]
        self.row3 = ["   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   "]
        self.row2 = ["   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   "]
        self.row1 = ["   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   "]
        self.all_rows = [self.row6, self.row5, self.row4, self.row3, self.row2, self.row1]

    #prints out the playing board
    def print(self):
        for row in self.all_rows:
            temp1 = ""
            temp2 = ""
            for index in range(len(row)):
                temp1 += row[index]
                temp2 += self.dash_line[index]
            print(temp1)
            print(temp2)
        temp = ""
        for element in self.num_row:
            temp += element
        print(temp)

    #resets the playing board
    #needed to use indexing to update the list, could not assign a new list to a row
    def reset(self):
        reset_row = ["   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   ", "|", "   "]
        reset_all_nums = ["1", "2", "3", "4", "5", "6", "7"]
        for row in self.all_rows:
            for index in range(len(row)):
                row[index] = reset_row[index]
        for num in reset_all_nums:
            self.all_nums.append(num)

    #plays out a turn
    def play(self, player):
        col = ""
        while col not in self.all_nums:
            col = input("\n" + player.name + ", which column are you putting your piece into? ")
            if col not in self.all_nums:
                print("Invalid column, choose a column 1-7 with a free space!")
        
        index = self.num_row.index(" " + col + " ")
        row_board = self.row1
        for row in reversed(self.all_rows):
            if self.empty(row, index):
                row[index] = " " + player.piece + " "
                row_board = row
                if (row == self.row6):
                    self.all_nums.remove(col)
                break
        
        return self.four_in_a_row(row_board, index, player)

    #checks to see if all_nums is empty
    def nums_empty(self):
        return self.all_nums == 0

    #checks to see if a block is empty
    def empty(self, row, index):
        if row[index] == "   ":
            return True

    #checks to see if the piece being played results in a connect four
    def four_in_a_row(self, row, index, player):
        return self.check_horizontal(row, index, player) or self.check_vertical(row, index, player) or self.check_forward_diagonal(row, index, player) or self.check_backward_diagonal(row, index, player)


    #returns true if the piece is part of a horizontal connect four, false otherwise
    def check_horizontal(self, row, index, player):
        counter = 1
        
        #check pieces to the left
        index_counter = 2
        while index - index_counter >= 0:
            if row[index - index_counter] == " " + player.piece + " ":
                counter += 1
                index_counter += 2
            else:
                break
        
        #check pieces to the right
        index_counter = 2
        while index + index_counter <= len(row):
            if row[index + index_counter] == " " + player.piece + " ":
                counter += 1
                index_counter += 2
            else:
                break

        if counter >= 4:
            return True
        
        return False

    #returns true if the piece is part of a vertical connect four, false otherwise
    def check_vertical(self, row, index, player):
        counter = 1
        all_rows_index = self.all_rows.index(row)
        
        index_counter = 1
        while all_rows_index + index_counter < len(self.all_rows):
            if self.all_rows[all_rows_index + index_counter][index] == " " + player.piece + " ":
                counter += 1
                index_counter += 1
            else:
                break
        
        if counter >= 4:
            return True
        
        return False

    #returns true if the piece is part of a forward diagonal connect four, false otherwise
    def check_forward_diagonal(self, row, index, player):
        counter = 1
        all_rows_index = self.all_rows.index(row)

        #check pieces creating a diagonal in the northeast direction
        all_rows_counter = 1
        index_counter = 2
        while all_rows_index - all_rows_counter >= 0 and index + index_counter <= len(row):
            if self.all_rows[all_rows_index - all_rows_counter][index + index_counter] == " " + player.piece + " ":
                counter += 1
                all_rows_counter += 1
                index_counter += 2
            else:
                break
        
        #check pieces creating a diagonal in the southwest direction
        all_rows_counter = 1
        index_counter = 2
        while all_rows_index + all_rows_counter < len(self.all_rows) and index - index_counter >= 0:
            if self.all_rows[all_rows_index + all_rows_counter][index - index_counter] == " " + player.piece + " ":
                counter += 1
                all_rows_counter += 1
                index_counter += 2
            else:
                break

        if counter >= 4:
            return True
        
        return False

    #returns true if the piece is part of a backward diagonal connect four, false otherwise
    def check_backward_diagonal(self, row, index, player):
        counter = 1
        all_rows_index = self.all_rows.index(row)

        #check pieces creating a diagonal in the northwest direction
        all_rows_counter = 1
        index_counter = 2
        while all_rows_index - all_rows_counter >= 0 and index - index_counter >= 0:
            if self.all_rows[all_rows_index - all_rows_counter][index - index_counter] == " " + player.piece + " ":
                counter += 1
                all_rows_counter += 1
                index_counter += 2
            else:
                break
        
        #check pieces creating a diagonal in the southeast direction
        all_rows_counter = 1
        index_counter = 2
        while all_rows_index + all_rows_counter < len(self.all_rows) and index + index_counter <= len(row):
            if self.all_rows[all_rows_index + all_rows_counter][index + index_counter] == " " + player.piece + " ":
                counter += 1
                all_rows_counter += 1
                index_counter += 2
            else:
                break

        if counter >= 4:
            return True
        
        return False


class Player:

    #constructor
    def __init__(self, piece, name):
        self.piece = piece
        self.name = name


#makes the piece to be used on the board for the player
def make_piece(piece, name):
    invalid_piece = True
    while invalid_piece:
        piece = input(name + ", what would you like your piece to be? ")
        if (len(piece) == 1):
            invalid_piece = False
        else:
            print("Invalid piece! Please be one character!")
    return piece


#looks at the result of a turn to see if a player has won or a stalemate has occured. If so, the players
#are asked if they want to play again. If yes, returns false. Otherwise, returns true. This returns true
#if a turn did not result in a win or a loss.
def define_result(result, board, winner, loser):
    if board.nums_empty() == True:
        print("This game has ended in a stalemate!")
        return play_again(winner, loser)
    elif result == True:
        print(winner.name + " has won!")
        return play_again(board, winner, loser)
    return False


#returns true if both players want to play again. Otherwise, returns false.
def play_again(board, winner, loser):
    answer_1 = ""
    while answer_1 != "yes" and answer_1 != "no":
        answer_1 = input(winner.name + ", would you like to play again? plz respond either yes or no? ")
    
    answer_2 = ""
    while answer_2 != "yes" and answer_1 != "no":
        answer_2 = input(loser.name + ", would you like to play again? plz respond either yes or no? ")

    if (answer_1 == "yes" and answer_2 == "yes"):
        board.reset()
        return False
    return True

def main():

    player_one_piece = make_piece("", "Player One")
    player_two_piece = make_piece("", "Player Two")
    while player_two_piece == player_one_piece:
        print("Cannot be the same piece as Player One")
        player_two_piece = make_piece("", "Player Two")
    
    player_one = Player(player_one_piece, "Player One")
    player_two = Player(player_two_piece, "Player Two")
    
    board = Board()
    
    over = False

    while not over:
        board.print()
        result = board.play(player_one)
        if result == True:
            board.print()
        over = define_result(result, board, player_one, player_two)
        if result == False:
            board.print()
            result = board.play(player_two)
            if result == True:
                board.print()
            over = define_result(result, board, player_two, player_one)
        


if __name__ == "__main__":
    main()