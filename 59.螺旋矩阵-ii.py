#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix =[[0 for _ in range(n)] for _ in range(n)]
        #填数
        count=1
        l,r,t,b = 0,n-1,0,n-1
        #模拟
        while count<=n*n:
            #开始
            #左闭右开
            #l->r
            for i in range(l,r+1):
                matrix[t][i] =count
                count+=1
            t+=1
            #t->b
            for i in range(t,b+1):
                matrix[i][r] = count
                count+=1
            r-=1
            #r->l
            #这里是重点 看一看
            for i in range(r,l-1,-1):
                matrix[b][i]=count
                count+=1
            b-=1
            #b->top
            for i in range(b,t-1,-1):
                matrix[i][l] = count
                count+=1
            l+=1
        return matrix


# @lc code=end

