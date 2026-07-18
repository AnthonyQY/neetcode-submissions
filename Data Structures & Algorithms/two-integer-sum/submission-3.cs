public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> indicesMap = new();

        for(int i = 0; i < nums.Length; i++){
            int complement = target - nums[i]; // the value we need
            if(indicesMap.ContainsKey(complement)){
                return new int[2] {indicesMap[complement], i};
            }

            indicesMap.Add(nums[i], i);
        }

        return new int[2];
    }
}
