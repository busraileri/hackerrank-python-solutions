# URL: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
  return  "-".join(line.split())


if __name__ == '__main__':
    line = input()
    print(split_and_join(line))