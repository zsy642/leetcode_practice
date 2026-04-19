import re
def tool(n):
    res=[]
    for i in range(1, n):
        if i==567:
            res.append(566)
        else:
            res.append(i)
    print("(",res,",",[566,567],'),')

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list2listnode(nums,circle=0,type=0):
    dummy=ListNode(next=nums[0])
    n0=ListNode(nums[0])
    one=n0
    circleone=dummy
    for i in range(0, len(nums)):
        one.next=ListNode(nums[i])
        one=one.next
        if i== circle:
            circleone=one
    if type==1:
        one.next=circleone
    return n0

def listnode2list(head):
    res=[]
    while head:
        res.append(head.val)
        head=head.next
    return res

def test():
    for i in range(1, 1000):
        print(i**0.5)

def testre(num,resnum):
    with open(r'测试原始数据.txt','r',encoding='utf-8') as f:
        text=f.read()
        testtext=r'(	)+(测试用例:)?(.+)\n'*num
        testrule=re.compile(testtext)
        testtexts=testrule.findall(text)
        print(testtexts)
        restext=r'(期望结果:)(.+)'+r'((\n)(.+))+'*(resnum-1)
        resrule=re.compile(restext)
        restexts=resrule.search(text)
        #print(restexts.group(2),restexts.group(5))
        resnum=2
        for i in testtexts:
            tmpstr=f'{i[2]},'
            for j in range (2,num+1):
                tmpstr+=f'{i[3*j-1]},'
            tmpstr+=f'{restexts.group(resnum)})'
            resnum+=3
            print("("+tmpstr+',')



def get_leetcode_data_gemini(file_path, num):
    """
    file_path: 文件路径
    num: 每个测试用例包含的参数行数 (比如 4Sum 就是 2 行: nums 和 target)
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 提取“测试用例”之后到“测试结果”之前的所有行
    case_section = re.search(r'测试用例:(.*?)测试结果:', content, re.S) #S是让.可以匹配\n
    # 2. 提取“测试结果”之后的所有行
    res_section = re.search(r'期望结果:(.*)', content, re.S)

    if not case_section or not res_section:
        print("错误：未找到指定的标签格式，请检查文档内容。")
        return []

    # 3. 清洗数据：转为行列表，去除多余空格
    def clean_lines(text):
        lines = [line.strip() for line in text.split('\n') if line.strip()] #strip去除两边空格
        return lines

    all_cases = clean_lines(case_section.group(1))
    all_results = clean_lines(res_section.group(1))

    # 4. 按 num 将用例分组 (比如每 2 行合成一个 tuple)
    grouped_cases = [tuple(all_cases[i : i + num]) for i in range(0, len(all_cases), num)]
    # 5. 组合并打印
    final_data = list(zip(grouped_cases, all_results))
    print("--- 格式化后的测试数据 ---")
    for case, res in final_data:
        # 这里输出成 (arg1, arg2, ..., expected) 的形式，方便直接复制到代码里
        formatted_case = ", ".join(case)
        print(f"({formatted_case}, {res}),")

    return final_data

if __name__ == '__main__':
    get_leetcode_data_gemini(r'测试原始数据.txt',1)
    pass