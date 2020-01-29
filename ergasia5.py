g = open("alex.txt","r")
string = g.read()
import re  #vazw ta tou arxiou se lista opou ta kanw split gia na ta exw ksexorista san lexis 

mystr = string
wordList = re.sub("[^\w]", " ",  mystr).split()
#print(wordList)
la={}
total = 0
for a in range (0,len(wordList)):
    leterwords = 0
    for h in wordList[a]:#metraw posa gramata exi kathe leksi edo 
        la[a]=la.get(a,0)+1
        leterwords = leterwords +1
    if leterwords > 2:
        print(wordList[a],"einai leksi pou tha allaxei")
for a, word in enumerate(wordList):#enumerate ta elements tis listas gia adikatasasi
    if len(word) > 3:#logiki sinthiki an to mikos mias leksis einai megalitero apo 3 
        wordList[a] = word[1:] + word[:1]#allazo to ellement etsi oste na einai opos to thelo me to 1o gramma sto tellos 
        print(wordList[a]+"ay")#print ta tis listas me to teliko -ay xoris na kani kati se afta pou exun ligotero apo 3 grammata 
    
    
