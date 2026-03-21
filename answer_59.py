from typing import List
def generateMatrix( n: int) -> List[List[int]]:
    res=[[None]*n for _ in range (n)]
    def real_gene(res,n,i=0,j=0,num=1):
        head=i
        tail=j
        if n<1:
            return
        for j in range (tail,n):
            res[i][j]=num
            num+=1
        for i in range (head+1,n):
            res[i][j]=num
            num+=1
        for j in range (n-2,tail-1,-1):
            res[i][j]=num
            num+=1
        for i in range (n-2,head,-1):
            res[i][j]=num
            num+=1
        real_gene(res,n-1,i,j+1,num)
    real_gene(res,n)
    return res




def main():
    return 0
    
if __name__ == '__main__':
    main()