# Digital Design Worksheet 2


### Simple Minesweeper Game, using the console



###### When the program is first run, the user is prompted to choose from one of 3 options for the size of the board
1. 6x6
2. 8x8
3. 10x10
* The number of bombs is calculated depending on the size, the formula is (size^2)*0.2, e.g: (6^2) * 0.2 = 7.2 (rounded to the nearest integer = 7).
* The user then enters the number of the row, then column, then 'F' or 'O' to either flag or open the cell as shown in the screenshot below.
* Per Minesweeper rules, the cell selected by the user will display the amount of mines in a 1-cell proximity around it in all directions (in this case 1).

![first_prompt](./user_prompt.png)
<hr>

###### As one of the main classes, the following 'Input' abstract class has been implemented to read input from the user

```
class Input(ABC):
    @abstractmethod
    def read(self):
        pass
```
<hr>

###### In the instance the user enters an invalid row or column value, they would receive the following result and be asked to enter a valid value again

![invalid row/col value](./invalid_row_col.png)
<hr>

###### In the instance the user enters an invalid character, anything other than 'F' or 'O', they would receive the following result and be asked to enter a valid character again

![invalid action](./invalid_action.png)
<hr>

###### In the instace where the user wanted to flag a certain cell, an 'F' will be in place of the X on the board as shown below

* There is a score tracker, that increments your score by 10 each time the user opens a cell that is not a mine, the score is printed with the board every time a cell is opened.

![flag](./flag.png)
<hr>

###### In the instance where the user lost by landing on a mine, in the following two pictures, one will display the board printing all mines present on the board as the '*' and the other picture showing a 'play again' prompt being used to play again

![game loss](./game_loss.png)
![play again](./play_again.png)
<hr>








