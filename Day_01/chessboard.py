

# A chessboard has 8 rows and 8 columns.

# Rows are numbered from 1 to 8
# Columns are labeled from a to h
# The square a1 is black

# Given the position of a square on the chessboard, determine whether the square is Black or White.

def determine_color(s):
    cols = {'a': 1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    columns = cols[s[0]]
    row = int(s[1])

    if (columns+row)%2 == 0:
        return "Black"
    else:
        return "White"

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()  # Read the input string
    
    # Call the user logic function and print the output
    result = determine_color(s)
    print(result)

if __name__ == "__main__":
    main()