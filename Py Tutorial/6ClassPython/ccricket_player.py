from datetime import datetime

class CricketPlayer:
    teamSize = 11
    def __init__(self,first,last,year):
        self.firstName = first
        self.lastName = last
        self.birthYear = year
        self.scores = []

    def add_score(self,score):
        self.scores.append(score)
        
    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)
    
    def getAge(self):
       current_year = datetime.now().year
       return current_year-self.birthYear
    
    def __str__(self):
        return (f"{self.firstName} {self.lastName} is from India")
    
    def __lt__(self,other):
      return self.getAge() < other.getAge()


virat = CricketPlayer("virat","kohli",1988)
virat.add_score(80)
virat.add_score(90)
average = virat.get_avg_score

david = CricketPlayer("virat","kohli",1989)

print(virat.firstName)
print(virat.lastName)
print(virat.birthYear)
print(virat.teamSize)
print(virat.scores)
print(virat.get_avg_score())
print(virat.getAge())

print(virat)
print(virat <  david)
