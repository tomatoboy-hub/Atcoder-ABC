T = int(input())

def judge(a,s):
    """
    x and (s - x) = aとなるようなxがあるかどうか? 
    xの探索範囲が s / 2 か 2 << 30 てどんくらいだ? 
    2147483648だから無理か 
    T = 10**5だから一つ当たり O(1)じゃないと無理くね? ~> てことは一発でぱこんと出せるんだろ
     
    """


for i in range(T):
    a,s = map(int,input().split())
    print("Yes" if judge(a,s) else "No")