print('This program allows you to find a lost card within a set of cards ranging from 1 to N. N is the number of cards you need to tell this program by entering it below at the start. Then enter the cards you have one by one.')
N = int(input())
sum = 0
for i in range(1, N + 1):
    sum += i
for i in range(1, N):
    sum = sum - int(input())
print(sum)
