# Scope 

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#enemies inside function: 2
#enemies outside function: 1




# Local Scope (exists within the function)

#def drink_potion():
 #   potion_strength = 2           #  can only use inside function
  #  print(potion_strength)  # 2

#drink_potion()
#print(potion_strength)  # NameError: name 'potion_strength' is not defined


# Global Scope 

player_health = 10




def drink_potion():
    
    potion_strength = 2          
    print(player_health)  # 10

drink_potion()