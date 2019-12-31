import os
import random as rnd
import time

print("Enter number of rows:")
M = int(input()) + 2
print("\nEnter number of coloumns")
N = int(input()) + 2

count = 0
field = []
new_field = []
for i in range(M):
    field.append([0] * N)
for i in range(M):
    new_field.append([0] * N)

count = [0, 0, 0, 0]

for i in range(1, M - 1):
    for j in range(1, N - 1):
        seed = rnd.randint(0, 3)
        if seed == 0:
            field[i][j] = 0
        elif seed == 1:
            field[i][j] = 1
        elif seed == 2:
            field[i][j] = 2
        elif seed == 3:
            field[i][j] = 3
            
while 1:
    os.system("clear")
    print("\n")
            
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if field[i][j] == 0:
                print("   ", end = "  ")
            elif field[i][j] == 1:
                print("@@@", end = "  ")
            elif field[i][j] == 2:
                print(">()", end = "  ")
            elif field[i][j] == 3:
                print("\o/", end = "  ")
        print("\n")
            
    time.sleep(1)
    
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            
            count = [0, 0, 0, 0]
            
            count[field[i][j - 1]] += 1
            count[field[i][j + 1]] += 1
            count[field[i + 1][j]] += 1
            count[field[i - 1][j]] += 1
            count[field[i + 1][j + 1]] += 1
            count[field[i - 1][j + 1]] += 1
            count[field[i + 1][j - 1]] += 1
            count[field[i - 1][j - 1]] += 1
            
            if field[i][j] == 0:
                if count[2] == 3:
                    new_field[i][j] = 2;
                elif count[3] == 3:
                    new_field[i][j] = 3;
                    
            elif field[i][j] == 2:
                if count[2] > 3:
                    new_field[i][j] = 0
                elif count[2] < 2:
                    new_field[i][j] = 0
                
            elif field[i][j] == 3:
                if count[3] > 3:
                    new_field[i][j] = 0
                if count[3] < 2:
                    new_field[i][j] = 0
                    
            else:
                new_field[i][j] = field[i][j]
                
    count = 0
    for i in range(1, M - 1):
        for j in range(1, N - 1):
            if field[i][j] == new_field[i][j]:
                count += 1
            field[i][j] = new_field[i][j]

    if count == (M - 2) * (N - 2):
        break