class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        ans = [0] * length_nums * 2
        length_ans = len(ans)

        for i in range(length_nums):
            ans[i] = nums[i]
            print("ans[i] = nums[i]")
            print(f"{ans[i]}={nums[i]}")
            ans[length_nums + i] = nums[i]
            print("ans[length_nums - i - 1] = nums[i]")
            print(f"ans[{length_nums - i - 1}]={nums[i]}")
        return ans



