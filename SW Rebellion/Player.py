import TroopTypes
import numpy as np

class Player():

    def __init__(self, n_walker, n_trooper):

        self.walker_arr = []
        self.trooper_arr = []

        for i in range(n_walker):
            self.walker_arr.append(TroopTypes.Walker())

        for i in range(n_trooper):
            self.trooper_arr.append(TroopTypes.Trooper())

    def dices(self):
        red_dice_counter = 0
        black_dice_counter = 0

        for walker in self.walker_arr:
            red_dice_counter += walker.red_die
            black_dice_counter += walker.black_die
        
        for trooper in self.trooper_arr:
            red_dice_counter += trooper.red_die
            black_dice_counter += trooper.black_die
        
        if black_dice_counter > 5:
            black_dice_counter = 5
        if red_dice_counter >5:
            red_dice_counter = 5
        
        return (black_dice_counter, red_dice_counter)
    
    def roll(self):
        outcomes = [1, 2, 3, 4] # 1 is nothing, 2 is normal hit, 3 is direct hit, 4 is tactic card
        probabilities = [1/6, 2/6, 2/6, 1/6]

        # Create the discrete probability distribution
        red_res = np.random.choice(outcomes, size=self.dices()[1], p=probabilities)
        black_res = np.random.choice(outcomes, size=self.dices()[0], p=probabilities)

        red_unique, red_counts = np.unique(red_res, return_counts= True)
        black_unique, black_counts = np.unique(black_res, return_counts= True)
        return (dict(zip(black_unique, black_counts)),dict(zip(red_unique, red_counts)))
    
    def troopers(self):
        return len(self.trooper_arr)
    
    def no_troopers(self):
        return len(self.trooper_arr) == 0

    def walkers(self):
        return len(self.walker_arr)
    
    def no_walkers(self):
        return len(self.walker_arr) == 0

    def is_over(self):
        return self.no_troopers() and self.no_walkers()
    
    def process_turn(self):

        remove_walker = []
        for i, walker in enumerate(self.walker_arr):
            if walker.hp <= 0:
                remove_walker.append(i)

        remove_trooper = []
        for i, trooper in enumerate(self.trooper_arr):
            if trooper.hp <= 0:
                remove_trooper.append(i)

        for index in sorted(remove_walker, reverse=True):
            del self.walker_arr[index]
        for index in sorted(remove_trooper, reverse=True):
            del self.trooper_arr[index]

        return self.is_over()
    

