import Player
import TacticCards
import Fight

res = []
for i in range(1000):
    test = Fight.Ground_fight(5,0,0,2)
    res.append(test.complete_fight())
print(f' rebels won {res.count(1)} times, empire won {res.count(2)} times and there were {res.count(0)} ties')





