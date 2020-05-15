print("***************** Welcome ********************")
print("heaviest word function")
print("python version 3.6+")
print("run this script to test the function by yourself")
print("or run test_problem2 for unittest script ")

# all alphabets
alphabet_dict = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, \
    "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,\
    "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
}


def heaviest_word(sentence):
    # a dict to put all calculated words
    all_words_sums = {}
    # split sentence into list of words
    words_list = sentence.split(" ")
    # loop through all words in words_list
    for word in words_list:
        # split current word into a list of characters
        chars_list = [c for c in word]
        word_weight = 0
        # loop through all characters of current word
        for c in chars_list:
            # calculate each character and add to word_weight
            word_weight += alphabet_dict[c]
        # add key , value to all words dictionary
        all_words_sums[word] = word_weight
    # return the (first) key with maximum weight
    first_max_word = max(all_words_sums, key=all_words_sums.get)
    return first_max_word


if __name__ == '__main__':
    sentence = input("Please enter a sentence of words : ")
    print("The Heaviest word is ({})".format(str(heaviest_word(sentence))))
