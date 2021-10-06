#Programmazione ad oggetti
###

class SSC_Napoli:

    # Attributi di Classe
    rosa = 27

    #Metodo costruttore
    def __init__(self,nome, cognome, anno, numero_maglia, stipendio):

        # Attributi di Istanza
        self.nome = nome
        self.cognome = cognome
        self.anno = anno
        self.numero_maglia = numero_maglia
        self.stipendio =stipendio
        
    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.nome}"\n Cognome: {self.cognome}\n Anno: {self.anno}\n Numero_maglia: {self.numero_maglia}\n Stipendio: {self.stipendio}' 
    
insigne = SSC_Napoli("Lorenzo","Insigne",1991,24, 4.5)

osimhen = SSC_Napoli("Victor","Osimhen",1998,9, 4.5)

lozano = SSC_Napoli("Hirving","Lozano",1995,11, 4.5)

print("Il tipo di variabile costruita è:")
print(insigne)
print(osimhen)
print(lozano)

print("\nLa singola scheda è:")
print (insigne.scheda())
print (osimhen.scheda())
print(lozano.scheda())

print("\n\naltro metodo per visualizzare le informazioni (__dict__):")

print(insigne.__dict__)
print(osimhen.__dict__)
print(lozano.__dict__)
