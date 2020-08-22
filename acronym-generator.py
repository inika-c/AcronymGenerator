'''
This program takes in keywords and creates an acronym that's easy to memorise.
This is a useful tool for studying.
'''
import random
import os
import sys


class Error(Exception):
    pass


class NotLettersError(Error):
    # Raised when the input doesn't consist of letters
    pass


class NullEntry(Error):
    # Raised when no input is given
    pass


def main():

    content_list = file_reader()
    first_letters = execution(content_list)


'''
shuffle(word) takes in a String and returns a shuffled version.
'''


def shuffle(word):

    word_copy = word
    shuffled = ""
    i = 0

    # Constructs a jumbled word
    while (i < len(word_copy)):
        randomLetter = random.randint(0, (len(word)-1))
        letter = word[randomLetter]  # Chooses a random letter
        shuffled += letter  # Appends it to the string
        i += 1
        # Removes the letter from the original word
        word = word.replace(letter, '', 1)

    return shuffled


'''
file_reader() doesn't take in anything, but returns a list with all the 
words in the file.
'''


def file_reader():

    my_file = open(
        "/Users/Inika/Desktop/Projects/acronym-generator/english.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")  # Creates a list with every word
    my_file.close()
    return content_list


'''
keyword_acceptor() doesn't take in anything, but returns the inputs from the user.
It also does checks and validates the inputs.
'''


def keyword_acceptor():

    numbers = "0123456789!@#$%^&*()-_,.?;:"  # String for entries not to accept

    print("Begin adding keywords and enter 'done' whenever you're done")

    end = False
    keywords = []

    while end != True:
        try:
            point = input("Keyword: ")
            if point == "":
                raise NullEntry  # Raises an error if nothing is entered
            if point in numbers:
                raise NotLettersError  # Raises an error if letters aren't entered
            if point == 'done':
                end = True
                continue
            keywords.append(point)  # Adds each keyword to the list
        except NullEntry:
            print("Must enter a word, try again!")
            print()
        except NotLettersError:
            print("Must only enter letters, try again!")
            print()

    return keywords


'''
letter(keywords) takes in the keywords inputted and returns the first letters of each 
of them as a formed string.
'''


def letters(keywords):

    first_letters = ""
    for i in keywords:
        beginning = i[0]
        first_letters += beginning  # Adds the first character of every word to the string
    return first_letters


'''
execution(content_list) takes in the list of words from the file and controls the execution.
It doesn't return anything.
'''


def execution(content_list):

    keywords = keyword_acceptor()
    first_letters = letters(keywords)
    count = 0
    # Loops till either the word is in the word list, or the number of iterations is greater than 1000
    while first_letters not in content_list:
        first_letters = shuffle(first_letters)
        count += 1
        if count > 1000:
            print(
                "Unfortunately no word can be made with those letters. Try substituting synonyms for a keyword.")
            os.execl(sys.executable, sys.executable,
                     *sys.argv)  # Restarts the script

    final_acronym(first_letters)


'''
final_acronym(first_letters) takes in the word created. It prints the final output out.
'''


def final_acronym(first_letters):

    print()
    print("Acronym to remember:")
    print(first_letters)


main()
