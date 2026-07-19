public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {

        Dictionary<string, List<string>> frequencyMap = new();

        
        foreach(string str in strs){
            string freqSig = string.Join(",", CreateFrequencyArray(str));
            if(!frequencyMap.ContainsKey(freqSig)){
                frequencyMap.Add(freqSig, new List<string>());
            }
            frequencyMap[freqSig].Add(str);
        }

        List<List<string>> groupList = new();
        foreach(KeyValuePair<string, List<string>> kvp in frequencyMap){
            var group = kvp.Value;
            groupList.Add(group);
        }

        return groupList;
    }

    private int[] CreateFrequencyArray(string str){
        int[] frequencyArray = new int[26];
        foreach(char c in str){
            int idx = c - 'a';
            frequencyArray[idx] = frequencyArray[idx] + 1;
        }

        return frequencyArray;
    }
}
