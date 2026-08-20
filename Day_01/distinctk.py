# You wish to help Ashish, who possesses a collection of N strings, some of which may be duplicated, and has been assigned the task of finding the kth unique string.

# If the number of unique strings is less than k, he needs to display -1. Considering you are Ashish's best friend can you assist him with this challenge?


def find_unique(s, k):
    unique = []

    for member in s:
        if s.count(member) == 1:
            unique.append(member)

    if k > len(unique):
        return -1
    else:
        return unique[k-1]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    s = data[1:n+1]
    k = int(data[n+1])
    result = find_unique(s, k)
    print(result)


if __name__ == "__main__":
    main()