# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# print(nums1.index(nums1[-1]))
# from collections import Counter
# num_ = Counter(nums1)
# n1 = set(nums1)
# n2 = set(nums2)
# print(n1.intersection(n2))
# print(n1 &n2)
input = [1,3,2,2]
from collections import Counter
ans =Counter(input)
print(ans.most_common())
for key,val in ans.most_common():
    print(key,val)


# #58 
# # s = "   fly me   to   the moon  "
# # print(len(s.rstrip().split(" ")[-1]))

# # a = "11"

# # print(bin(int(a)))
# # d = {'32':1,"25":2}
# # for di in d.items():
# #     print(di[0])
# #A->1
# # print((ord('A')-64)*26+(ord('B')-64))
# # s = "sad"
# # for ss in s:
# #     print(ss)
# # columnTitle="AB"
# # col = len(columnTitle)
# # ans =0
# # for s in columnTitle:
# #     ans+=(ord(s)-64)*(26**(col-1))
# #     col-=1
# # print(ans)
# # s = "foo"
# # t = "bar"
# # for ss,tt in zip(s,t):
# #     print(ord(ss)-ord(tt))
# # b = "add"
# # s = {'d', 'a'}
# # a = list(s)
# # a.sort(key =b.index)
# # print(a)

# # s = "anagram"
# # t = "nagaram"
# # ss,tt = [0]*27,[0]*27
# # for a in s:
# #     print(ord(a))
# #     ss[ord(a)-97] +=1
    
# # for b in t:
# #     tt[ord(b)-97] +=1 
 
# # for x,y in zip(ss,tt):
# #     if x!=y:
# #         print('l')
# #         break

# # s = 88
# # a = str(s)
# # # b = a.split(num = -1)
# # print(len(a))
# # pattern = "abba"
# # s = "dog cat cat dog"
# # d = dict()
# # f = s.split(" ")
# # for p,ss in zip(pattern,f):
# #     if p not in d:
# #         d[p] = ss
# # st = ""
# # # print(d)
# # # print(pattern)
# # # for i,p in enumerate(list(pattern)):
# # #     print(p)
# # #     st += d[p]+" "
# # # st =st.lstrip()
# # # print(st)
# # print(list(map(pattern.index, pattern)))

# #回溯算法
# from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def dfs(nums, size, depth, path, used, res):
#             if depth == size:
#                 res.append(path[:])
#                 return

#             for i in range(size):
#                 if not used[i]:
#                     used[i] = True
#                     path.append(nums[i])

#                     dfs(nums, size, depth + 1, path, used, res)

#                     used[i] = False
#                     path.pop()

#         size = len(nums)
#         if len(nums) == 0:
#             return []

#         used = [False for _ in range(size)]
#         res = []
#         dfs(nums, size, 0, [], used, res)
#         return res

# def spiralOrder(matrix: List[List[int]]) -> List[int]:
#         #只能模拟
#         m,n = len(matrix),len(matrix[0])
#         ans =[]
#         i,j=0,0
#         #改成while
#         while i < m and  j < n:
#             #满足左闭右开
#             if i<=m-1 and 0<=j<=n//2:
#                 ans.append(matrix[i][j])
#                 j+=1

#             elif j>n//2 and 0<=i<m-1:
#                 ans.append(matrix[i][j])
#                 i+=1
#             #右->左
#             elif i>=m//2 and 0<j<=n-1:
#                 ans.append(matrix[i][j])
#                 j-=1
#             #下->上
#             elif 0<j<n-1 and 0<i<=m//2:
#                 ans.append(matrix[i][j])
#                 j-=1
#         print(ans)
#         # return ans   
# if __name__ == '__main__':
#     # nums = [1, 2, 3]
#     # solution = Solution()
#     # res = solution.permute(nums)
#     # print(res)
#     # s= 'abc#dd'
#     # s = list(s)
#     # s[2]='s'
#     # print(s)
#     # res = [[1,1,2],[1,2,1],[2,1,1]]
#     # res2 = list(set(map(tuple,res)))
#     # for ii in res2:
#     #     ii = list(ii)
#     #     print(type(ii))
#     # print(res2)
#     matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     # ans = []
#     spiralOrder(matrix)
#     # print(ans)

