class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        vector<int> visit(n, 0);
        vector<vector<string>> res;
        for (int i = 0; i < n; i++) {
            if (!visit[i]) {
                visit[i] = 1;
                vector<string> tmp = {strs[i]};
                string si = strs[i];
                sort(si.begin(), si.end());
                for (int j = 0; j < n; j++) {
                    if (!visit[j]) {
                        string sj = strs[j];
                        sort(sj.begin(), sj.end());
                        if (sj == si) {
                            visit[j] = 1;
                            tmp.push_back(strs[j]);
                        }
                    }
                }
                res.push_back(tmp);
            }
        }
        return res;
    }
};