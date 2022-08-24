# sudo apt install python3-enchant
import string, enchant

start_word="1a23oo"

all_letters_list = list(string.ascii_lowercase)
exception_list = ['r','n','v','h','m']
start_list = [item for item in all_letters_list if item not in exception_list]
possible_words = list()
dict = enchant.Dict("en")
for i in start_list:
    for j in start_list:
        for k in start_list:
            word = start_word.replace("1",i).replace("2",j).replace("3",k)
            possible_words.append(word)
            if dict.check(word):
                print(word)
print(len(possible_words))
