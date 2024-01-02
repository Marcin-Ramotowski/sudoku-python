import requests
from dotenv import load_dotenv
import os

load_dotenv()
OPTIONS = {"X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
            "X-RapidAPI-Host": os.getenv("X-RapidAPI-Host")}

def get_sudoku_from_api(difficulty):
    # Ustawienie parametrów żądania
    seed = ''  # np. '1234567890'
    url = '/sudoku/generate'
    if seed:
        url = f"{url}?seed={seed}"
    elif difficulty:
        url = f"{url}?difficulty={difficulty}"
    
    # Wysłanie żądania GET i odbiór odpowiedzi
    response = requests.get(f"https://sudoku-generator1.p.rapidapi.com{url}", headers=OPTIONS)
    answer = response.json()
    sudoku = answer["puzzle"]
    print(f'Rozpoczęto grę nr {answer["seed"]}')
    return sudoku

def get_solution_from_api(puzzle):
    # Ustawienie parametrów żądania
    url = '/sudoku/solve'
    if puzzle:
        url = f"{url}?puzzle={puzzle}"
    
    # Wysłanie żądania GET i odbiór odpowiedzi
    response = requests.get(f"https://sudoku-generator1.p.rapidapi.com{url}", headers=OPTIONS)
    solution = response.json()["solution"]
    return solution
