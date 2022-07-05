# # 한수

# def hansu(num):
#     cnt = 0
#     for i in range(1, num+1):
#         if i <100:
#             cnt += 1
#         else:
#             nums = list(map(int, str(i)))
#             if nums[1]-nums[0] == nums[2]-nums[1]:
#                 cnt += 1
#     return cnt
# num = int(input())
# print(hansu(num))

for i in range(100, 150):
    nums = list(map(int, str(i)))
    print(nums)