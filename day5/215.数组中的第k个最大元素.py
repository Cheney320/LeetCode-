#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def partition(self, arr, l, r):
        import random
        index = random.randint(l, r)
        arr[l], arr[index] = arr[index], arr[l]
        v = arr[l]
        # arr[l+1...j] > v; arr[j+1...i-1] < v
        j = l
        for i in range(l+1, r+1):
            if arr[i] > v:
                arr[j+1],arr[i] = arr[i], arr[j+1]
                j += 1
        arr[l], arr[j] = arr[j], arr[l]
        return j

    # 求出arr[l...r]范围里第k大的数
    def selection(self, arr, l, r, k):
        if l == r: return arr[l]
        p = self.partition(arr, l, r)
        # 索引从0开始，所以k-1
        if p == k-1: return arr[p]
        elif p > k-1: return self.selection(arr, l, p-1, k)
        else: return self.selection(arr, p+1, r, k)

    # 对arr[l...r]部分进行快速排序
    def quickSort(self, arr, l, r):
        if l >= r: return
        p = self.partition(arr, l, r)
        self.quickSort(arr, l, p-1)
        self.quickSort(arr, p+1, r)

    def findKthLargest(self, nums, k):
        # self.quickSort(nums, 0, len(nums)-1)
        # return nums[k-1]
        return self.selection(nums, 0, len(nums)-1, k)
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,3,1,2,4,5,5,6,7,8]
    print(s.findKthLargest(nums, 2))
