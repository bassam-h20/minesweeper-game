#Bassam Ali
#Student ID - 21047697
#
# references:
#
#- Weber, B. (n.d.) Python enumerate(): Simplify Looping With Counters. Available from: https://realpython.com/python-enumerate/ [Accessed 18 January 2023]. 
#- W3Schools (n.d.) Python set() Function. Available from: https://www.w3schools.com/python/ref_func_set.asp [Accessed 18 January 2023]. 
#- W3Schools (n.d.) Python String join() Method. Available from: https://www.w3schools.com/python/ref_string_join.asp [Accessed 18 Jan 2023].
#- @bestharadhakrishna (2021) Abstract Classes in Python. Available from: https://www.geeksforgeeks.org/abstract-classes-in-python/ [Accessed 18 January 2023]. 
#- Ramos, L.P. (n.d.) Python's map(): Processing Iterables Without a Loop. Available from: https://realpython.com/python-map-function/#:~:text=Python%27s%20map()%20is%20a,them%20into%20a%20new%20iterable. [Accessed 18 January 2023]. 
#- Ramos, L.P. (n.d.) Python Class Constructors: Control Your Object Instantiation. Available from: https://realpython.com/python-class-constructor/#:~:text=As%20a%20quick%20example%2C%20check,self.name%7D!%22) [Accessed 18 January 2023]. 
#- @pawan_asipu (2022) set add() in python. Available from: https://www.geeksforgeeks.org/set-add-python/ [Accessed 18 January 2023]. 
#- @retr0 (2022) Python String format() method. Available from: https://www.geeksforgeeks.org/python-string-format-method/ [Accessed 18 January 2023]. 


import random
from abc import ABC, abstractmethod

#class for taking user input
class Input(ABC):
    @abstractmethod
    def read(self):
        pass

#class for game logic
class Minesweeper:
    #initalizing variables
    def __init__(self, size):
        self.size = size
        self.board = [[0 for x in range(self.size)] for y in range(self.size)]
        self.hidden_board = [['X' for x in range(self.size)] for y in range(self.size)]
        self.bombs = self.generate_bombs()
        self.game_over = False
        self.flagged_bombs = 0
        self.score = 0


    #checking if game is over or not by counting number of unrevealed cells in hidden_board
    #and number of flagged bombs, comparing the sum of the two 
    #to figure if all cells have been either revealed or flagged and game is over
    #returns True if game is over, and returns False otherwise
    def is_game_over(self):
        unrevealed_cells = sum(row.count('X') for row in self.hidden_board)
        return unrevealed_cells + self.flagged_bombs == self.size ** 2

    #getting choice of which board size
    def get_board_size():
        while True:
            try:
                size = int(input("Enter board size (6, 8, 10): "))
                if size not in [6, 8, 10]:
                    print("Invalid input. Please enter 6, 8, or 10.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return size

    

    #generating random coordinates for location of mines on the board
    def generate_bombs(self):
        bombs = set()
        while len(bombs) < int(self.size ** 2 * 0.2):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            bombs.add((x, y))
        return bombs
    

    #couting number of bombs surrounding the chosen cell by the user
    def count_bombs(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x+i, y+j) in self.bombs:
                    count += 1
        return count

    #shows the location of all mines on board
    def show_bombs(self):
        for x, y in self.bombs:
          self.hidden_board[x][y] = '*'

    #allows user to flag a position
    def flag_position(self, x, y):
        self.hidden_board[x][y] = 'F'
        self.flagged_bombs += 1

    #allowing user to show the chosen cell, if chosen cell is a bomb, all of the board's mines are revealed
    def open_position(self, x, y):
        if (x, y) in self.bombs: 
            self.game_over = True
            print("BOMB! Game Over.")
        else:
            count = self.count_bombs(x, y)
            self.board[x][y] = count
            self.hidden_board[x][y] = count
            #score increment by 10 each time user guesses cell without bomb
            self.score+= 10
            self.check_win()
        if self.is_game_over() and self.flagged_bombs == len(self.bombs):
            self.game_over = True
            
    #printing board with current score
    def print_board(self):
        print("\nCurrent score: ",self.score)
        print("  " + " ".join(map(str, range(1, self.size+1))))
        for i, row in enumerate(self.hidden_board):
            print("{} ".format(i+1) + " ".join(map(str,row)))

    #checks if the user has won
    def check_win(self):
        unrevealed_cells = sum(row.count('X') for row in self.hidden_board)
        #checks if unrevealed cells on the board are equal to the number of the mines on the board
        #so if user flags all correct spaces that contain bombs, 
        # and reveals all cells that are not mines, the user wins
        if unrevealed_cells == len(self.bombs) and self.flagged_bombs == len(self.bombs):
            self.game_over = True
            print("You Win!")

            
            
    


#class for handling user input and connecting input to game logic
class UserInput(Input):
    def __init__(self, game):
        self.game = game

    def read(self):
        while True:
            try:
                x = int(input("Enter row number: ")) - 1
                y = int(input("Enter column number: ")) - 1
                if x < 0 or x >= self.game.size or y < 0 or y >= self.game.size:
                    print("Invalid input. Please enter a valid row and column number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid row and column number.")

        while True:
            action = input("Enter 'f' to flag position or 'o' to open position: ")
            if action == 'f':
                self.game.flag_position(x, y)
                break
            elif action == 'o':
                self.game.open_position(x, y)
                break
            else:
                print("Invalid input. Please enter 'f' or 'o'.")



def main():
    while True:
        # Initialize game and user input
        size = Minesweeper.get_board_size()
        game = Minesweeper(size)
        
        user_input = UserInput(game)

        # Play game
        while not game.game_over:
            game.print_board()
            user_input.read()
            if game.is_game_over():
                break
        game.show_bombs()
        game.print_board()

        # Ask user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    
    




if __name__ == "__main__":
    main()
