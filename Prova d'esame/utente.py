from rischieste import *

class Utente:
    def __init__(self, nome, stipendio, ruolo, responsabile):
        self.nome = nome
        self.stipendio = stipendio
        self.ruolo = ruolo
        self.responsabile = responsabile
        self.rich = list()

    def get_stipendio(self):
        return self.stipendio

    def get_nome(self):
        return self.nome
    
    def get_ruolo(self):
        return self.ruolo
    
    def get_responsabile(self):
        return self.responsabile
    
    def get_richieste(self):
        return self.rich
    
    def nuova_richiesta(self):
        s = int(input("Inserisci le ore di lavoro per la richiesta: "))
        self.rich.append(Richieste(s,'In attesa'))
    
    def vis_richieste(self):
        if self.rich == []:
            print("Errore!!!")
            return 0
        else:
            print("Le richieste sono: ")
            c = 0
            for i in self.rich:
                print(f'{c}. Richiesta di {i.get_ore()} ore - Status: {i.get_status()}')
                c+=1

    def tot_denaro(self):
        s = 0
        for i in self.rich:
            if i.get_status() == 'Accetto':
                s+=i.get_ore()
        print("Le ore accettate sono totali: ",s," con il gadagno di ",s*self.stipendio)

    def esporta_richiesta(self):
        self.vis_richieste()
        s = int(input("Quale richiesta vuoi eportare??? "))
        with open(f'{self.get_nome()}_Richiesta {s}.txt','w') as exp:
            exp.write(f'Richiesta di {self.rich[s].get_ore()} ore - Status: {self.rich[s].get_status()}')