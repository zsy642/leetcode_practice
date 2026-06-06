from tool import list2binarytree,BinaryTree
def connect(root) :
    if not root:
        return root
    currmost = root
    lastmost = root.left or root.right
    while currmost or lastmost:
        while not lastmost and currmost:
            lastmost = currmost.left or currmost.right
            if not lastmost:currmost = currmost.next

        current = lastmost
        lastcurr = None
        while currmost:
            if current and current.next:
                current = current.next

            if currmost.left and currmost.right:
                lastcurr = currmost.right
                if current != currmost.left: current.next = currmost.left
                current = currmost.left
            else:
                if current!=(currmost.left or currmost.right):lastcurr = currmost.left or currmost.right

            current.next = lastcurr
            currmost = currmost.next

        currmost = lastmost
        lastmost = None

    return root
#root=list2binarytree([1,2])
root=BinaryTree(1)
root.right=BinaryTree(2)
root.right.left=BinaryTree(3)
root.right.left.left=BinaryTree(4)
connect(root)