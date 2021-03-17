#
# Example file for working with conditional statements
#


def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    # if x < y:
    #     st = "x is less than y"
    # elif x == y:
    #     st = "x is the same than y"
    # else:
    #     st = "x is greater than y"

    # conditional statements let you use "a if C else b"
    st = 'x is the less than y' if (x < y) else "x is greater or than same than y"
    print(st)
if __name__ == "__main__":
    main()
