# URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input("Enter number of scores: "))
    arr = list(map(int, input("Enter the scores: ").split()))
    
    # maximum score
    highest = max(arr)

    # Remove all instances of the highest score
    filtered = [x for x in arr if x != highest]

    # the runner-up 
    runner_up = max(filtered)

    print("Runner-up score is:", runner_up)
