# bookbot
BookBot is my first project!

Requirements to use:

1) a txt file containing the text for static analyis
2) path to the text

How it works:

1) gets path from txt file
2) opens it, saves to string and closes again
3) counts the total number of words for the report
4) converts string to lowercase, makes a unique list of chars in alphabetical order. Then a dictionary with count per char
5) filters out non-alphabetical chars
6) creates a list of dictionaries per character, which allows sorting by their count
7) generates a report which lists number of words + occurences of each letter in descending order