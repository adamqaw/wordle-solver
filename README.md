# wordle-solver
Program to return .txt of potential 5-letter words for wordle. Uses Merriam-Webster dictionary API to lookup words


Logic: 
- input green letters (if any), if no green, there bust be yellows, count green letters
- input yellow letters (if any), if no yellow, there must be greens, count yellows
- type in a string (that will be converted to list) of all available letters
- depending on whether there are greens or not, specify function to run: one green, two greens, or three greens, etc
- If there are both greens and yellows, default to green function 
- if there are ony yellows, word_input = '*****', use all available letters, but word must contain yellow letters, using regex
- add words to possible_words.txt
- Using dictionary API, look up each word from possible_words.txt, if it does not exist, delete word from .txt file.


## April 1 2022
- Created main.py, forms.py
