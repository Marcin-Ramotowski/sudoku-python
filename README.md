# Sudoku
This program is a desktop implementation of the popular number puzzle game, Sudoku. The design and functionality of the game are based on the Sudoku.com application by EasyBrain Studio available in the Google Play Store. Moreover this application collaborate with Sudoku-Generator API available on the RapidApi website in order to get random board and solution to this.

## Installation and Usage
To run the program, you need to have Python interpreter installed on your computer and subscribed Sudoku-Generator API from https://rapidapi.com/gregor-i/api/sudoku-generator1. Usage of this API is free for using 1000 objects per day. In the .env file you have to fill such atributes: X-RapidAPI-Key and X-RapidAPI-Host. Values of the atributes you can copy from the code snippet from the right column on the RapidAPI website indicated in this section. Before running the program, make sure you have the packages in your environment: `requests` and `python-dotenv`, which are required to run the application.

## How to Play
The game window consists of a board and a control panel at the bottom. The user fills in the board fields by first selecting a button with a number, which they want to input into the free field of the board. Then, they click on the selected field, and if the number can be placed in the field, it appears as text in that field. When all the fields are completed, then a window is displayed informing the user of the win and allowing the user to choose between restarting or quitting the game. You have limit of 3 mistakes per game. If you exceed this limit you will lose the game. Fails counter is placed to the right of board.

## Features
The game has the following functionalities:
- At the start of the game, the player selects the difficulty level by clicking on the corresponding button. The player's choice is sent along with a Get request to the API from where a board of the selected difficulty level will be drawn.
- Fields that are pre-filled at the start of the game are inactive, and the player cannot modify their values. These fields do not have a callback.
- The user can have only one button with a number pressed at a time. If they press another button, the previously pressed one becomes inactive.
- Notes mode - used to record potential values that could be placed in empty fields. To activate it, the user needs to press the 'N' button. Displayed numbers are presented in ascending order and can be both added to and removed from the pool.
- Fields that the user has filled with a final value (not in notes mode) turn green.
- After filling in all the fields, the user receives a notification about winning the game and can choose to play again or quit the game.

## Game Interface
![sudoku](https://github.com/Marcin-Ramotowski/Sudoku/assets/109000485/babd18e4-7358-40e7-8de0-5db3af593a6c)