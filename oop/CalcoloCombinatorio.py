# classe calcolo combinatorio

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self,str):
        self.__N = len(stringa)
        self.__stringa = str
        self.__listStringa = list(stringa)

    def charRipetuti(self):

        word = list(parola) 
        caratteriripetuti={}
        nCaratteri = 0
        count = 0

        for i in word:
            if (i in caratteriripetuti): 
                caratteriripetuti[str(i)] += 1
        else:
            caratteriripetuti[str(i)] = 1 
        for i in caratteriripetuti:
            if caratteriripetuti[i]>1:
                count+=1
                nCaratteri += caratteriripetuti[i]

    def combUtil(self):
        f = open("C:/Users/User/Desktop/python/oop/words.italian.txt", 'r')
        for riga in f:

           p = f.readline()

           if self.__stringa in p:
               print("è una parola italiana")
           #else:
               #print("non è una parola italiana")
   # PERMUTAZIONI

    def nPermutSenzaRip(self):
        '''
        restituire il numero di permutazioni SENZA ripetizione
        '''
        return 0

    def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        '''
        restituire il numero di disposizioni semplici SENZA ripetizione
        '''
        return 0

    def nDispSemplConRip(self):
        '''
        restituire il numero di disposizioni semplici CON ripetizione
        '''
        return 0

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

parola = calcComb(str(input("inserisci una stringa: ")))
parola.charRipetuti()

