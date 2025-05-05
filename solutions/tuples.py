# URL: https://www.hackerrank.com/challenges/python-tuples/problem

n = int(input())
int_list = tuple(map(int, input().split()))
print(hash(int_list))