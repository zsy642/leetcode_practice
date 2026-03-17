def mySqrt( x: int) -> int:
    left=0
    right=46341
    while True:
        mid=(left+right)//2
        if mid**2>x:
            right=mid-1
        elif mid**2<x:
            left=mid+1
        else:
            return mid
        if right<left:
            return right

def main():
    return 0
    
if __name__ == '__main__':
    main()