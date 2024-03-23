#words list from https://github.com/hbenbel/French-Dictionary/tree/master
import pandas
import string


if __name__ == '__main__':
    adj=pandas.read_csv("French-Dictionary-master/dictionary/adj.csv")
    adv = pandas.read_csv("French-Dictionary-master/dictionary/adv.csv")
    conj = pandas.read_csv("French-Dictionary-master/dictionary/conj.csv")
    det = pandas.read_csv("French-Dictionary-master/dictionary/det.csv")
    dictionary = pandas.read_csv("French-Dictionary-master/dictionary/dictionary.csv")
    noun = pandas.read_csv("French-Dictionary-master/dictionary/noun.csv")
    prep = pandas.read_csv("French-Dictionary-master/dictionary/prep.csv")
    pron = pandas.read_csv("French-Dictionary-master/dictionary/pron.csv")
    verb = pandas.read_csv("French-Dictionary-master/dictionary/verb.csv")
    more = pandas.read_csv("more.csv")#csv with correct words not in dictionary like "des" (yes, really)
    listOfEverything=[adj,adv,conj,det,noun,prep,pron,verb,dictionary,more]


    notFound=[] #list of word not in dictionary
    with open("texttocorrect.txt", "r", encoding="utf-8") as text:
        for line in text:
            line=line.translate(str.maketrans('', '', string.punctuation))#remove punctuation
            for word in line.split( ):
                if word.__contains__("'"):
                    pass
                else:
                    notFound.append(word)#put the word in notfound, if then present in csv remove it
                    for i in listOfEverything:
                        if word.lower() in i["form"].values:
                            #print(f"found {word.lower()}")
                            notFound.pop()
                            break
    text.close()
    print(notFound)
    lettersAmount=[]#amount of each letter's present in a word
    for i in notFound:#count each letter, put the number in a dict
        letters:dict={}
        letters.update({"word":i})
        for j in i:
            if letters.get(j):
                letters.update({j:(letters[j]+1)})
            else:
                letters.update({j:1})
        lettersAmount.append(letters)
    print(lettersAmount)
    potentialCorrections:dict= {}
    """for i in lettersAmount:
        print(i)"""
    # take each word in the dictionary and count the letters, then compare
    # it to the words not found. If the distance between both is smaller than
    # 3, then add the word in the suggestions.
    for i in listOfEverything:
        for values in i["form"].values:
            letters:dict={}
            for l in str(values):
                if letters.get(l):
                    letters.update({l: (letters[l] + 1)})
                else:
                    letters.update({l: 1})
            for errors in lettersAmount:
                distance=0
                for le in errors.items():
                    if not le[0] == "word":
                        if letters.get(le[0]):
                            distance+=le[1]-letters.get(le[0])
                        else:
                            distance+=le[1]
                    for le in letters.items():
                        if not errors.get(le[0]):
                            distance+=le[1]
                if distance<3:
                    if potentialCorrections.get(errors["word"]):
                        potentialCorrections.update({errors["word"]:potentialCorrections[errors["word"]].append(values)})
                    else:
                        potentialCorrections.update({errors["word"]:[values]})
    print(potentialCorrections)
