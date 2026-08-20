# Problem Statement
# The royal family exchanges gifts at Christmas, where the youngest member receives gifts from everyone but doesn't give any gifts. Given the data for all the exchanged gifts among the family members, you need to identify the youngest member, who is the one receiving gifts from everyone but not giving any.

# Note: A family member does not give more than one gift to the same member

def find_youngest_member(n, m, gifts):
    if n > 1:
        all_a = set()
        receive = {}

        for a, b in gifts:
            all_a.add(a)
            receive[b] = receive.get(b, 0) + 1

        for member in receive:
            if member not in all_a and receive[member] == n - 1:
                return member

        return -1

    else:
        return 1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of family members
    m = int(data[1])  # Number of gifts exchanged
    
    gifts = []
    index = 2
    for _ in range(m):
        a_i = int(data[index])
        b_i = int(data[index + 1])
        gifts.append((a_i, b_i))
        index += 2
    
    # Call user logic function and print the output
    result = find_youngest_member(n, m, gifts)
    print(result)

if __name__ == "__main__":
    main()