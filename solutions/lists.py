# URL: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    new_list = []


    for _ in range(N):
        command =  input().split()
        action = command[0]

        if action =="insert":
            new_list.insert(int(command[1]), int(command[2]))
        elif action == "print":
            print(new_list)
        elif action == "remove":
            new_list.remove(int(command[1]))
        elif action == "append":
            new_list.append(int(command[1]))
        elif action =="sort":
            new_list.sort()
        elif action == "pop":
            new_list.pop()
        elif action == "reverse":
            new_list.reverse()
