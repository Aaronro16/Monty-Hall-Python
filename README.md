# Monty Hall  Problem in Python 
#### (With Jupyter Notebook)

This is personal, to get familiar with GitHub, Classes, Pandas and plotting in Python using Jupyter Notebook. This provide a simple test of exploration of the [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem). This is the descption of the problem:

        Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice? 
        (obteined in the page of the link)

Here I will show you that if you are in this situation you have to switch the door if you can. This will be performed with code in Python that emulate the game. 

**First lets create the class contest wich will have:
- The election door of the participant modelate as a list
- The location of the prize behind the doors as a list
- The function "go" that will run the contest according the strategy of input
- The return of the function "go" is True (Win) or False (Lose)


    ```python
    from random import randint

    class Contest:
        def __init__(self,dqty):
            self.dqty = dqty 
            self.participant = []
            self.prize = []
            for i in range(dqty):
                self.participant.append(0)
                self.prize.append(0)

        # The next function emulate the contest
        def go(self):
            participant = self.participant.copy()
            prize = self.prize.copy()
            participant[randint(0, self.dqty)-1] = 1 
            prize[randint(0, self.dqty-1)] = 1
            for i in range(len(participant)):
                if participant[i] == 0 and participant[i] == prize[i]:
                    participant[i] = 'x'
                    break
            pos_changed = participant.index(0)
            if prize[pos_changed] == 1:
                return True
            elif prize[pos_changed] == 0:
                return False
    ```
