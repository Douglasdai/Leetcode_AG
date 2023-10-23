#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #撞墙法
        #字节21年面试题
        if not matrix:return []
        x=y=0
        res = []
        dx = [0,1,0,-1]         
        dy = [1,0,-1,0]  
        di=0  
        visited = set()
        m,n  = len(matrix) ,len(matrix[0])
        for i in range(m*n):
            res.append(matrix[x][y])
            visited.add((x,y))
            tx,ty = x+dx[di],y+dy[di]
            if 0<=tx<m and 0<=ty<n and (tx,ty) not in visited:
                x,y = tx,ty
            else:
                di = (di+1)%4
                x,y = x + dx[di],y+dy[di]  
        return res


        #python 特殊做法
        result = []
        while matrix:
            result += matrix.pop(0)  # 取矩阵第一行并删除
            matrix = list(zip(*matrix))[::-1]  # 旋转矩阵
        return result


# @lc code=end

