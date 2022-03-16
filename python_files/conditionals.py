from curses.ascii import STX


def main():
    x,y=100,100

    if(x < y):
     st="x is less than y"
    elif(x==y):
        st="x is the same as y"
    else:
     st="x is greater than y"
    print(st)

# conditional statemnents, this codes has errors of importing
    st="x is less than y" if(x<y) else "x is greater than or the same as y"
    print(st)

if __name__=="__main__":
    main()


