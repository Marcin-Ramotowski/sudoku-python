import tkinter as tk
from tkinter import messagebox, ttk
from api_talker import (get_sudoku_from_api, get_solution_from_api)


def start_game():
    global root
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Sudoku Game")
    root.withdraw()
    choose_difficulty()


def choose_difficulty():
    def set_difficulty(diff):
        global difficulty
        difficulty = diff
        diff_window.destroy()
        root.deiconify()
        create_sudoku_board(difficulty)

    diff_window = tk.Toplevel(root)

    label = tk.Label(diff_window, text="Wybierz poziom trudności:")
    label.pack(padx=10, pady=10)

    button_frame = ttk.Frame(diff_window)
    button_frame.pack(padx=10, pady=10)

    style = ttk.Style()
    style.configure("TButton", padding=3)

    easy_button = ttk.Button(button_frame, text="Easy", command=lambda: set_difficulty("easy"))
    medium_button = ttk.Button(button_frame, text="Medium", command=lambda: set_difficulty("medium"))
    hard_button = ttk.Button(button_frame, text="Hard", command=lambda: set_difficulty("hard"))

    easy_button.pack(side="left", padx=5, pady=5)
    medium_button.pack(side="left", padx=5, pady=5)
    hard_button.pack(side="left", padx=5, pady=5)
    diff_window.mainloop()


def create_sudoku_board(difficulty):
    global handles
    global solution

    sudoku = get_sudoku_from_api(difficulty)
    solution = get_solution_from_api(sudoku)
    
    num_converter = lambda char: 0 if char == '.' else int(char)
    sudoku = [[num_converter(char) for char in sudoku[i:i+9]] for i in range(0,81,9)][::-1]
    solution = [[num_converter(char) for char in solution[i:i+9]] for i in range(0,81,9)][::-1]

    moves = 81 - sum(1 for row in sudoku for value in row if value)

    sudoku_btn = [[None for _ in range(9)] for _ in range(9)]
    for row in range(9):
        for col in range(9):
            x = 40 + col * 40
            y = 270 - row * 30
            number = sudoku[row][col]
            if number == 0:
                sudoku_btn[row][col] = tk.Button(root, text='', width=3, height=1,
                                                 font=("Helvetica", 12, "bold"), bg="white",
                                                 command=lambda r=row, c=col: sudoku_btn_callback(r, c))
            else:
                sudoku_btn[row][col] = tk.Button(root, text=str(number), width=3, height=1,
                                                 font=("Helvetica", 12, "bold"), bg="white")
            sudoku_btn[row][col].place(x=x, y=y)

    num_btn = []
    for num in range(1, 10):
        x = 40 + (num - 1) * 40
        y = 330
        num_btn.append(tk.Button(root, text=str(num), width=3, height=1,
                                 font=("Helvetica", 12, "bold"), bg="white",
                                 command=lambda n=num: num_btn_callback(n)))
        num_btn[num - 1].place(x=x, y=y)
    
    positions = [(160, 30, 2, 273), (280, 30, 2, 273), (40, 120, 360, 2), (40, 210, 360, 2)]
    for position in positions:
        tk.Label(root, bg="black").place(x=position[0], y=position[1], width=position[2], height=position[3])

    handles = {'sudoku': sudoku, 'current_num': 0, 'moves': moves, 'sudoku_btn': sudoku_btn,
               'num_btn': num_btn}
    root.mainloop()


def check_number(sudoku, num, row, col):
    if sudoku[row][col] != 0:
        return False
    if solution[row][col] != num:
        return False
    return True


def sudoku_btn_callback(row, col):
    current_num = handles['current_num']
    sudoku = handles['sudoku']
    moves = handles['moves']
    prev_value = handles['sudoku_btn'][row][col]['text']

    if check_number(sudoku, current_num, row, col):
        sudoku[row][col] = current_num
        if not prev_value:
            moves -= 1
        handles['sudoku_btn'][row][col]['text'] = str(current_num)
        handles['sudoku_btn'][row][col]['bg'] = 'lightgreen'
    else:
        messagebox.showerror("Błąd!", "Błąd! Tutaj nie możesz wstawić tej cyfry.")

    if moves == 0:
        answer = messagebox.askquestion("Wygrana", "Gratulacje, rozwiązałeś Sudoku!\nCzy chcesz zagrać jeszcze raz?")
        if answer == "yes":
            root.destroy()
            start_game()
        else:
            root.destroy()

    handles['moves'] = moves
    handles['sudoku'] = sudoku


def num_btn_callback(num):
    prev_num = handles['current_num']
    handles['current_num'] = num
    handles['num_btn'][prev_num-1]['relief'] = 'raised'
    handles['num_btn'][num-1]['relief'] = 'sunken'


if __name__ == "__main__":
    start_game()