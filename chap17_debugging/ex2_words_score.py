"""
Consider that vowels in the alphabet are a, e, i, o, u and y.
Function score_words takes a list of lowercase words as an argument and returns a score as follows:
The score of a single word is 2 if the word contains an even number of vowels. 
Otherwise, the score of this word is 1. 
The score for the whole list of words is the sum of scores of all words in the list.

Example:

"""

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

def main():
    words = str(input("Enter the words:"))
    result = score_words(words.split())
    return result

if __name__ == "__main__":
    print("Score of word(s): {}".format(main()))
