import Player
import TacticCards
import random

class Ground_fight():

    def __init__(self, reb_trooper, reb_walker, imp_trooper, imp_walker):
        self.reb = Player.Player(reb_walker, reb_trooper)
        self.imp = Player.Player(imp_walker, imp_trooper)

    def combat_turn(self, priority_type: int, player_1: Player, player_2: Player ):
        if priority_type == 0: # prioritize assigning damage to undamaged target instead of overkilling
            roll = player_1.roll() # Generate roll

            # PROCESS BLACK NORMAL HITS
            normal_hits = roll[0].get(1, 0)
            if not player_2.no_troopers():
                for i in range(normal_hits):
                    trooper = player_2.trooper_arr[i%len(player_2.trooper_arr)]
                    trooper.hp -= 1


            # PROCESS RED NORMAL HITS
            normal_hits = roll[1].get(1, 0)
            if not player_2.no_troopers():
                for i in range(normal_hits):
                    trooper = player_2.trooper_arr[i%len(player_2.trooper_arr)]
                    trooper.hp -= 1


            # PROCESS DIRECT HITS
            direct_hits = roll[0].get(2, 0) + roll[1].get(2, 0)
            if not player_2.no_walkers():
                for i in range(direct_hits):
                    walker = player_2.walker_arr[i%len(player_2.walker_arr)]
                    walker.hp -= 1
            else:
                for i in range(direct_hits):
                    trooper = player_2.trooper_arr[i%len(player_2.trooper_arr)]
                    trooper.hp -= 1

            #PROCESS TACTIC CARDS
            tactic_cards = roll[0].get(4, 0) + roll[1].get(4, 0)
            for i in range(tactic_cards):
                result=random.choice([0,1]) # 0 represents one damage, 1 represents one block
                if result:
                    if not player_2.no_walkers():
                        walker = player_2.walker_arr[i%len(player_2.walker_arr)]
                        walker.hp -= 1
                    else:
                        trooper = player_2.trooper_arr[i%len(player_2.trooper_arr)]
                        trooper.hp -= 1
                # else:
                #     if not player_1.no_walkers():
                #         for walker in player_1.walker_arr:
                #             if walker.hp < walker.max_hp:
                #                 walker.hp += 1
                #     else:
                #         for trooper in player_1.trooper_arr:
                #             if trooper.hp < trooper.max_hp:
                #                 trooper.hp += 1
    
    def complete_fight(self):
        player_1 = self.reb
        player_2 = self.imp

        while (not player_1.is_over() and not player_2.is_over()):
            self.combat_turn(0, player_1, player_2)
            self.combat_turn(0, player_2, player_1)
            player_1.process_turn()
            player_2.process_turn()

            if player_1.is_over() or player_2.is_over():
                if player_1.is_over() and not player_2.is_over():
                    return 2
                if player_2.is_over() and not player_1.is_over():
                    return 1
                else:
                    return 0
    



            

            




