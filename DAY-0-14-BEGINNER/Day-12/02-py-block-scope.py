# there is no block scope in python

if 3>2:
    a_variable = 10



game_level = 3
enemies = [ 'Skeleton','Zombie','Alien']

def creat_enemy():
      if game_level<5:
         new_enemy =enemies[0]

print(new_enemy)     #Skeleton