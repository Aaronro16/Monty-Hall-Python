from random import randint

class Contest:
    def __init__(self,dqty,strategy):
        self.dqty = dqty 
        self.strategy = strategy
        self.participant = []
        self.prize = []
        for i in range(dqty):
            self.participant.append(0)
            self.prize.append(0)
        
    def go(self):
        participant = self.participant.copy()
        prize = self.prize.copy()
        if self.strategy == "Monty":
            participant[randint(0, self.dqty)-1] = 1 
            prize[randint(0, self.dqty-1)] = 1
            while participant.count(0)-1:
                for i in range(len(participant)):
                    if participant[i] == 0 and participant[i] == prize[i]:
                        participant[i] = 'x'
                        pos_init = participant.index(1)
                        pos_changed = participant.index(0)
                        participant[pos_init] = 0
                        participant[pos_changed] = 1
                        break

            if prize[participant.index(1)] == 1:
                return True
            elif prize[participant.index(1)] == 0:
                return False
        elif self.strategy == "None":
            participant[randint(0, self.dqty)-1] = 1 
            prize[randint(0, self.dqty-1)] = 1
            pos_selected = participant.index(1)
            if prize[pos_selected] == 1:
                return True
            elif prize[pos_selected] == 0:
                return False

class Result:
    def __init__(self):
        self.wins = [0]
        self.looses = [0]
    def add(self,value):
        if value:
            self.wins.append(self.wins[-1]+1)
            self.looses.append(self.looses[-1])
        else:
            self.wins.append(self.wins[-1])
            self.looses.append(self.looses[-1]+1)


        


concurso = Contest(3,"Monty")
Resultado = Result()

for i in range(20000):
    Resultado.add(concurso.go())
print(f"Victorias : {Resultado.wins[-1]}, Derrotas: {Resultado.looses[-1]}")

