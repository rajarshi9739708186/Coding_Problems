def FirstRepeatedWord(list_of_Words):
    Word_Frequency = {}

    for word in list_of_Words:
        try:
            # Already existing in Dictionary
            # Adding in Dictionary for Second time
            Word_Frequency[word] += 1
            return word
        except:
            # Add in dictionary for First time
            Word_Frequency[word] = 1

    return "No Repeated Word"

Sentence = input("Provide sentence : ")
print(FirstRepeatedWord(Sentence.split()))