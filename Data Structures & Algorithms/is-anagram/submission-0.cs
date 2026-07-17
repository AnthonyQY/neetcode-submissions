public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> charMapS = new();

        foreach(char c in s){
            charMapS[c] = charMapS.GetValueOrDefault(c) + 1;
        }

        Dictionary<char, int> charMapT = new();

        foreach(char c in t){
            charMapT[c] = charMapT.GetValueOrDefault(c) + 1;
        }

        foreach(KeyValuePair<char, int> kvp in charMapT){
            if(!charMapS.ContainsKey(kvp.Key)){
                return false;
            }

            if(kvp.Value != charMapS[kvp.Key]){
                return false;
            }
        }

        foreach(KeyValuePair<char, int> kvp in charMapS){
            if(!charMapT.ContainsKey(kvp.Key)){
                return false;
            }

            if(kvp.Value != charMapT[kvp.Key]){
                return false;
            }
        }

        return true;
    }
}
