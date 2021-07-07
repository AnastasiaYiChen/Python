'____author___' == 'Anastasia'



import random

# Function printarray
def printarray(t):
    for i in range(len(t)):
        for j in range(len(t)):
            if j == m - 1:
                print(t[i][j])
            else:
                print(t[i][j], end='|')

# Function countstars
def countstar(t, x, y):
    count = 0
    for i in range(len(t)):
        for j in range(len(t)):
            if x - 1 >= 0 and y - 1 >= 0 and t[x-1][y-1] == '*':
                count += 1
            if y - 1 >= 0 and t[x][y-1] == '*':
                count += 1
            if x + 1 <= len(t[i]) - 1 and y - 1 >= 0 and t[x+1][y-1] == '*':
                count += 1
            if x - 1 >= 0 and t[x-1][y] == '*':
                count += 1
            if x + 1 <= len(t[i]) - 1 and t[x+1][y] == '*':
                count += 1
            if x - 1 >= 0 and y + 1 <= len(t) - 1 and t[x-1][y+1] == '*':
                count += 1
            if y + 1 <= len(t) - 1 and t[x][y+1] == '*':
                count += 1
            if x + 1 <= len(t[i]) - 1 and y + 1 <= len(t) - 1 and t[x+1][y+1] == '*':
                count += 1
            return count

# initialize the array
m = 50
t = [["_" for i in range(m)] for j in range(m)]
# printarray(t)

# create random star
starcount = 2000
for i in range(starcount):
    thei = random.randint(0, m - 1)
    thej = random.randint(0, m - 1)
    t[thei][thej] = '*'

printarray(t)
print('---------------------------------------------Original Array---------------------------------------------------')


# destroy the star when it's around by 2 stars and reborn with have three neighbors
runcount = 10000
for k in range(runcount):
    for i in range(len(t)):
        for j in range(len(t)):
            totalcountaround = countstar(t, i, j)
            if t[i][j] == '*' and (totalcountaround < 2 or totalcountaround > 3):
                t[i][j] = '_'
            elif t[i][j] == '_' and totalcountaround == 3:
                 t[i][j] = '*'


    print('--------------------------------------No:', (k + 1), '-----------------------------------------------------')
    printarray(t)