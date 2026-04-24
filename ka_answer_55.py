import sys

def reverse(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def main():
    input_data = sys.stdin.read().split()
    if not input_data: return

    k = int(input_data[0])
    s = list(input_data[1])
    n = len(s)

    # 1. 整体反转：abcdefg -> gfedcba
    reverse(s, 0, n - 1)

    # 2. 反转前 k 个：gfedcba -> fg edcba (假设 k=2)
    reverse(s, 0, k - 1)

    # 3. 反转后面 n-k 个：fg edcba -> fg abcde
    reverse(s, k, n - 1)

    print("".join(s))

main()