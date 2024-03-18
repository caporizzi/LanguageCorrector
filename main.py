#words list from https://github.com/hbenbel/French-Dictionary/tree/master
import pandas



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
    listOfEverything=[adj,adv,conj,det,dictionary,noun,prep,pron,verb]

    text=open("texttocorrect.txt")
    for line in text:
        for word in line.split( ):
            ""
    text.close()
