public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length){
            return false;
        }

        Dictionary<char, int> charMap = new();

        foreach(char c in s){
            charMap[c] = charMap.GetValueOrDefault(c, 0) + 1;
        }

        foreach(char c in t){
            charMap[c] = charMap.GetValueOrDefault(c, 0) - 1;
            if(charMap[c] <= 0){
                charMap.Remove(c);
            }
        }

        return charMap.Keys.Count == 0;
    }
}
