g = open("alex.txt","r")
string = g.read()
import re  #vazw ta tou arxiou se lista opou ta kanw split gia na ta exw ksexorista san lexis 

mystr = string
wordList = re.sub("[^\w]", " ",  mystr).split()
    
  
la={}

def funct(str): 
          
        
                      
    for a in range(0, len(wordList)): 
          
            
        leterwords = 0
        for h in wordList[a]:#metraw posa gramata exi kathe leksi edo 
            la[a]=la.get(a,0)+1
            leterwords = leterwords + 1
            #ta vazw kai int giati mu evgaze sfalma oti kai kala den einai int kati..
            f_l = int(wordList[a].count('f')) # posa f ta
            F = int(wordList[a].count('F')) 
            c_l = int(wordList[a].count('c')) # posa c
            C = int(wordList[a].count('C')) 
            k_l= int(wordList[a].count('k')) # posa k
            K = int(wordList[a].count('K')) 
            r_l= int(wordList[a].count('r')) # posa r
            R = int(wordList[a].count('R')) 
            bad = f_l + c_l + k_l  + r_l + F + C + K + R
            good = int(leterwords - bad)

        if good > bad:
            print(wordList[a], 'KALH LEXH')  
        else:
            print(wordList[a], 'KAKH LEXH')   
          
def main(): #lew ti einai h main
    with open('alex.txt', 'r') as file:
        funct(str)       #kalw tin funct              
          
main()
