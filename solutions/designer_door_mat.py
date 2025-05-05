# URL: https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())

#top
for i in range(1, N, 2):
    print((".|." * i).center(M, "-"))

#welcome
print("WELCOME".center(M, "-"))

#bottom
for i in range(N-2, 0, -2):
    print((".|." * i).center(M, "-"))
