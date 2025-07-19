import io

def look_up_bonus(ability_score):
    ability_bonus = { 6: -2, 7: -2, 8: -1, 9: -1,
                     10: 0, 11: 0, 12: 1, 13: 1, 
                     14: 2, 15: 2, 16: 3, 17: 3,
                     18: 4 }

    return ability_bonus[ability_score]

def look_up_hp(con_bonus, class_name):
    pass
