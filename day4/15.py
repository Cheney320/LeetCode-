"""
15.三数之和
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
思路一：
1. 先将数组进行排序
2. 从左侧开始，选定一个值为 定值 ，右侧进行求解，获取与其相加为0的两个值
3. 类似于快排，定义首和尾
    首尾与 定值 相加
    等于 0，记录这三个值
    小于 0，首部右移
    大于 0，尾部左移
    定值右移，重复该步骤
"""
# def threeSum(nums):
#     res = []
#     nums.sort()
#     if nums[0] <= 0 and nums[-1] >= 0:
#         i = 0
#         while i < len(nums) - 2:
#             if nums[i] > 0: break   # 最左侧大于0，无解
            
#             left = i+1
#             right = len(nums)-1
        
#             while left < right:
#                 s = nums[i]+nums[left]+nums[right]

#                 if s == 0:
#                     res.append([nums[i],nums[left],nums[right]])
                    
#                 if s <= 0:
#                     left += 1
#                     while nums[left] == nums[left-1] and left<len(nums)-1: 
#                         left += 1
                            
#                 else:
#                     right -= 1

#             i += 1
#             while nums[i] == nums[i-1]: 
#                 i += 1     # 避免出现重复结果
#                 if i == len(nums) - 1: break

#     return res


"""
思路二：
对排序后的数组进行遍历, 将每个元素的相反数作为key, 元素所在的位置作为
value存入哈希表中, 两次遍历数组不断检查 a + b 之和是否存在于哈希表中.
时间复杂度 O(n ^ 2)
空间复杂度 O(n)
"""
def threeSum(nums):
    if len(nums) < 3:
        return []
    target_hash = {-x: i for i, x in enumerate(nums)}
    res = []
    res_hash = {}
    for i, first in enumerate(nums):
        # 当前元素与前一个元素相同时, 可直接跳过以优化性能
        if i > 0 and first == nums[i - 1]:
            continue
        for j,second in enumerate(nums[i + 1:]):
            # 检查两数之和是否存在于哈希表中
            if first + second in target_hash:
                target_index = target_hash[first + second]
                if target_index == i or target_index == i + j + 1:
                    continue
                # 将找到的结果存入另一个哈希表中, 避免包含重复结果
                row = sorted([first, second, nums[target_index]])
                key = ",".join([str(x) for x in row])
                if key not in res_hash:
                    res.append(row)
                    res_hash[key] = True
    return res


nums = [-1, 0, 1, 2, -1, -4]
# nums = [0,0,0,0,0,0]
# nums = [1,1,-2]
print(threeSum(nums))

        



