# Sudoku
Ten program jest desktopową implementacją popularnej gry Sudoku. Projekt i funkcjonalność gry oparte są na aplikacji Sudoku.com autorstwa EasyBrain Studio dostępnej w sklepie Google Play. Ponadto ta aplikacja współpracuje z Sudoku-Generator API w celu uzyskania losowej tablicy wraz z jej rozwiązaniem.

## Instalacja i użytkowanie
Aby uruchomić program, musisz mieć zainstalowany Matlab na swoim komputerze oraz aktywną subskrybcję Sudoku-Generator API dostępnego pod adresem: https://rapidapi.com/gregor-i/api/sudoku-generator1. Korzystanie z tego API jest bezpłatne do maksymalnie 1000 obiektów dziennie. W pliku .env należy wypełnić następujące atrybuty: X-RapidAPI-Key i X-RapidAPI-Host. Wartości tych atrybutów można skopiować z fragmentu kodu z prawej kolumny na stronie RapidAPI wskazanej w tej sekcji. Przed uruchomieniem programu upewnij się, że masz w swoim środowisku pakiety: `requests` oraz `python-dotenv`, które są wymagane do uruchomienia aplikacji.

## Jak grać
Okno gry składa się z planszy i panelu sterowania u dołu ekranu. Użytkownik wypełnia pola planszy wybierając najpierw przycisk z cyfrą, którą chce wprowadzić w wolnym polu planszy. Następnie klika na zaznaczone pole i wtedy jeśli numer można umieścić w tym polu, pojawia się on w jego wnętrzu jako tekst. Po wypełnieniu wszystkich pól wyświetlone zostanie okno informujące użytkownika o wygranej i pozwalające użytkownikowi wybrać pomiędzy ponownym uruchomieniem gry a jej zakończeniem.

## Funkcje
Gra posiada następujące funkcjonalności:
- Na początku gry gracz wybiera poziom trudności klikając na odpowiedni przycisk. Wybór gracza jest wysyłany wraz z żądaniem Get do API, z którego zostanie odebrana wygenerowana losowo plansza o wybranym poziomie trudności.
- Pola, które są wstępnie wypełnione na początku gry są nieaktywne, a gracz nie może modyfikować ich wartości.
- Użytkownik może mieć aktywny tylko jeden przycisk z cyfrą na raz. Jeśli naciśniesz inny przycisk, przycisk który był wciśnięty wcześniej staje się nieaktywny.
- Tryb Notatek - służy do rejestrowania potencjalnych wartości, które mogą być umieszczone w pustych polach. Aby go aktywować, użytkownik musi nacisnąć przycisk 'N'. Wyświetlane liczby są przedstawione w porządku rosnącym i mogą być zarówno dodawane, jak i usuwane z puli.
- Pola, które użytkownik wypełnił ostateczną wartością zmieniają kolor na zielony.
- Po wypełnieniu wszystkich pól, użytkownik otrzymuje powiadomienie o wygranej i może wybrać poziom trudności ponownie lub zakończyć rozgrywkę.

## Interfejs gry
![sudoku](https://github.com/Marcin-Ramotowski/Sudoku/assets/109000485/babd18e4-7358-40e7-8de0-5db3af593a6c)