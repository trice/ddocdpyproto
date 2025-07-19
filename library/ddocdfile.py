
from library.ddocdlib import look_up_bonus

def save_character(abilities, hp, class_name):
    file_name = f"new_{class_name}.txt"
    file_lines = []
    ability_initials = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

    file_lines.append("==============================\n")
    file_lines.append(f"Class: {class_name}\n")
    file_lines.append("Experience: 0XP\n")
    file_lines.append(f"Hit Points: {hp}\n")
    file_lines.append("==============================\n")
    file_lines.append("Equipment: Staff, Rags, A head full of hopes and dreams\n")
    file_lines.append("==============================\n")
    file_lines.append("Ability Scores:\n")
    
    for i in range(len(abilities)):
        bonus = look_up_bonus(abilities[i])
        plus_or_minus = " "
        if bonus > 11:
            plus_or_minus = "+"
        file_lines.append(f"    {ability_initials[i]}: {abilities[i]} {plus_or_minus} {str(bonus)}\n")
   
    file_lines.append("==============================\n")

    with open(file_name, 'w') as file:
        file.writelines(file_lines)
