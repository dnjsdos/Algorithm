from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:


        val_indices = []
        for i, num in enumerate(nums):

            if num != val:
                if len(val_indices) == 0:
                    continue

                else:
                    idx = val_indices.pop(0)
                    nums[idx] = num
                    nums[i] = "_"
                    val_indices.append(i)
                    continue

            else:
                nums[i] = "_"
                val_indices.append(i)
                continue

        k = len(nums) - len(val_indices)

        return k
