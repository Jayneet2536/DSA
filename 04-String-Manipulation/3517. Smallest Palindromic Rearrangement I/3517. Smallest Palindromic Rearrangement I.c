
class Solution {
public:
    string smallestPalindrome(string s) {
        
        int freq[26] = {0};

        for(char c : s)
            freq[c - 'a']++;

        int idx = -1;

        for(int i = 0; i < 26; ++i){
            if(freq[i] & 1){
                idx = i;
                break;
            }
        }

        string res = ;

        if(idx != -1){
            freq[idx]--;
            res += idx + 'a';
        }

        for(int i = 25; i >= 0; --i){
            
            if(!freq[i])
                continue;

            int len = freq[i] / 2;
            
            string t(len, 'a' + i);
            
            res = t + res + t;
        }

        return res;
    }
};
