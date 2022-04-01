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


## April 1 2022 Commit:
- Created main.py, forms.py, logic.py, index.html, possible-words.html
- Wrote the logic, which works other than the indexing which goes out of range, *needs fixing*
- Created Flask app, including db config for future SQLite implementation
- Created forms for green and yellow letters, along with form for available letters
- Wrote jinja for possible-words.html to display all possible words, *although still need to implement dictionary API to only show valid words*
- Added endpoint and headers in main.py for dictionary API, *No API KEY yet*

### TODO:
- Create API key on Merriam-Webster for Collegiate dictionary 
- Fix indexing issues on logic.py
- Implement dictionary API to check for valid words, then delete invalid words from possible-words.txt
- Migrate from .txt to SQLite
