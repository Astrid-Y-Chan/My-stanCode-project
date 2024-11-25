"""
File: anagram.py (0628 version 2)
Name: Astrid Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program will find all anagrams for the word that the user inputs.
    """
    ####################
    print(f'Welcome to stanCode "Anagram Generator" ({EXIT} to quit)')
    while True:
        target_word = input('Find anagrams for: ')
        start = time.time()
        if target_word == EXIT:
            break
        anagrams_lst = find_anagrams(target_word)
        print(f'{len(anagrams_lst)} anagrams: {anagrams_lst}')
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
    ####################


def read_dictionary():
    read_dictionary_helper('')


def read_dictionary_helper(target_word):
    """
    :param target_word: str, the word that users input.
    :return: set(), words in the dictionary that are the same length as the target_word.
    """
    dictionary_s = set()
    with open(FILE, 'r') as f:
        for word in f:
            word = word.strip()
            if len(target_word) == len(word):
                dictionary_s.add(word)
    return dictionary_s


def find_anagrams(s):
    """
    :param s: str, the word that users input.
    :return: lst, anagrams of the s
    """
    dictionary_s = read_dictionary_helper(s)
    alpha_lst = []
    for ch in s:
        alpha_lst.append(ch)
    return find_anagrams_helper(s, "", alpha_lst, [], dictionary_s)


def find_anagrams_helper(target_word, current_s, alpha_lst, anagrams_lst, dictionary_s):
    """
    :param target_word: str, the word that users input.
    :param current_s: str, a string that has been reorganized.
    :param alpha_lst: lst, a list that contains all letters of the target_word.
    :param anagrams_lst: lst, a list storing anagrams of the target_word.
    :param dictionary_s: set(), words in the dictionary that are the same length as the target_word.
    :return: lst, all anagrams of the target_word
    """
    if len(current_s) == len(target_word):
        if current_s not in anagrams_lst:  # check the current_s is non-repetitive.
            if current_s in dictionary_s:  # check the current is a anagram.
                print(f'Searching...')
                print(f'Found: {current_s}')
                anagrams_lst.append(current_s)

    else:
        for i in range(len(alpha_lst)):
            # Choose
            ch = alpha_lst.pop(0)
            current_s += ch
            # Explore
            # if has_prefix_helper(current_s, dictionary_s):
            #     find_anagrams_helper(target_word, current_s, alpha_lst, anagrams_lst, dictionary_s)
            # It works faster without using the 'has_prefix_helper' function.
            find_anagrams_helper(target_word, current_s, alpha_lst, anagrams_lst, dictionary_s)
            # Un-choose
            current_s = current_s[:-1]
            alpha_lst.append(ch)
    return anagrams_lst


def has_prefix(sub_s):
    """
    :param sub_s: str, a string that needs to be checked
    :return: bool
    """
    has_prefix_helper(sub_s, set())


def has_prefix_helper(sub_s, dictionary_s):
    """
    :param sub_s: str, a string that needs to be checked
    :param dictionary_s: set(), words in the dictionary.
    :return: bool
    This function will check if the sub_s has the same starting letter as words in the dictionary_s
    and returns True or False.
    """
    for word in dictionary_s:
        while word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
