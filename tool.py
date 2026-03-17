def tool(n):
    res=[]
    for i in range(1, n):
        if i==567:
            res.append(566)
        else:
            res.append(i)
    print("(",res,",",[566,567],'),')

def test():
    for i in range(1, 1000):
        print(i**0.5)

if __name__ == '__main__':
    # for i in range(957, 1000):
    #     tool(i)
    test()