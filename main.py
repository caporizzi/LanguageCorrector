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
    more = pandas.read_csv("more.csv")
    listOfEverything=[adj,adv,conj,det,noun,prep,pron,verb,dictionary,more]


    notFound=[]
    with open("texttocorrect.txt", "r", encoding="utf-8") as text:
        for line in text:
            line=line.translate(str.maketrans('', '', string.punctuation))
            for word in line.split( ):
                if word.__contains__("'"):
                    pass
                else:
                    notFound.append(word)
                    for i in listOfEverything:
                        if word.lower() in i["form"].values:
                            #print(f"found {word.lower()}")
                            notFound.pop()
                            break
    text.close()
    print(notFound)