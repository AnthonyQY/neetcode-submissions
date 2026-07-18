public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> complementNeededMap = new();

        for(int i = 0; i < nums.Length; i++){
            int complement = target - nums[i];
            if(complementNeededMap.ContainsKey(nums[i])){
                return new int[2] {complementNeededMap[nums[i]], i};
            }

            complementNeededMap.Add(complement, i);
        }

        return new int[2];
    }
}
