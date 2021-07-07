'____author____' == 'Anastasia'


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

m = 10
t = [["_" for i in range(m)] for j in range(m)]

# create diamond star
starcount = 10
for i in range(starcount):
    for j in range(starcount):
        #t[i][j] = '*'
        t[0][4] = '*'
        t[1][3] = '*'
        t[1][4] = '*'
        t[1][5] = '*'
        t[2][2] = '*'
        t[2][3] = '*'
        t[2][4] = '*'
        t[2][5] = '*'
        t[2][6] = '*'
        t[3][1] = '*'
        t[3][2] = '*'
        t[3][3] = '*'
        t[3][4] = '*'
        t[3][5] = '*'
        t[3][6] = '*'
        t[3][7] = '*'
        t[4][0] = '*'
        t[4][1] = '*'
        t[4][2] = '*'
        t[4][3] = '*'
        t[4][4] = '*'
        t[4][5] = '*'
        t[4][6] = '*'
        t[4][7] = '*'
        t[4][8] = '*'
        t[4][9] = '*'
        t[5][1] = '*'
        t[5][2] = '*'
        t[5][3] = '*'
        t[5][4] = '*'
        t[5][5] = '*'
        t[5][6] = '*'
        t[5][7] = '*'
        t[5][8] = '*'
        t[6][2] = '*'
        t[6][3] = '*'
        t[6][4] = '*'
        t[6][5] = '*'
        t[6][6] = '*'
        t[6][7] = '*'
        t[7][3] = '*'
        t[7][4] = '*'
        t[7][5] = '*'
        t[7][6] = '*'
        t[8][4] = '*'
        t[8][5] = '*'
        t[9][5] = '*'


printarray(t)
print('-----------------------------------------------Original Array-------------------------------------------------')


# destroy the star when it's around by 2 stars and reborn with have three neighbors
runcount = 4
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