word_list = {
            "LOL": "a response to something funny",
            "CRINGE": "something strange or embarrassing",
            "ROFL": "answer to a joke",
            "SHEESH": "slight disapproval",
            "CREEPY": "terrible, ominous",
            "AGGRO": "become aggressive/angry",
            "JK": "just kidding",
            "OMG": "o my God, something shocking",
            }

i = 0

while i < 5:
    word = input("Write a word to see its definition: ")
    if word in word_list.keys():
        print(word_list[word])
    else:
        print("Word not found!")
    i += 1
