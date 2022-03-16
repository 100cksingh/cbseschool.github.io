# Problem  in codes
# part 1
# from this import d



# def main():
#     # f=open("textfile.txt","w+")
#     f=open("textfile.txt","a")

#     for i in range(10):
#         f.write("This is line"+str(i)+"\r\n")

#         f.close()

# part 2
# from importlib.resources import contents


# def main():

#     f=open("textfile.txt","r")
#     if f.mode=='r':
#         contents=f.read()
#         print(contents)
    
# if __name__=="__main__":
#     main()

# part 3
from importlib.resources import contents


def main():

    f=open("textfile.txt","r")
    if f.mode=='r':
        fl=f.readlines()
        for x in fl:
            print(x)

