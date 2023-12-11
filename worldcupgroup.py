import numpy as np
#*********
def team (i) :
    if i == 0 :
        return 'Spain'
    elif i == 1 :
        return 'Iran'
    elif i == 2 :
        return 'Portugal'
    elif i == 3 :
        return 'Moroco'
#***********
mat_team = np.identity(4,dtype=int)
for i in range(4) :    
    team1 = team(i)
    for j in range(i,4) :
        if i == j :
            continue       
        team2 = team(j)
        natije = input(f'enter natije {team1} - {team2}   :  ')
        (a,b) = natije.split('-')
        mat_team[i][j] = a
        mat_team[j][i] = b``
#*************
for i in range(4) :
    wins = 0
    loses = 0
    draws = 0
    goal_att = 0
    goal_def = 0 
    for j in range(4) :
        if i == j :
            continue
        if mat_team[i][j] > mat_team[j][i] :
            wins += 1
        elif mat_team[i][j] < mat_team[j][i] :
            loses += 1
        elif mat_team[i][j] == mat_team[j][i] :
            draws += 1
        goal_att += mat_team[i][j]
        goal_def += mat_team[j][i]
    print(f'Team : {team(i)} ,wins : {wins} , loses : {loses} , draws : {draws} , goaldifference : {goal_att - goal_def} , points : {(wins*3)+(draws)}')             
#************
print(mat_team)



