class Solution {
  public:
    bool makeChanges(int N, int K, int target, vector<int> &coins) {
        // code here
        vector <int> moves(target+1,0);
        for(int i=0;i<N;i++){
            if(coins[i]<=target){
                moves[coins[i]]=1;
            }
        }
        for(int i=1;i<K;i++){
            vector <int> freshmoves(target+1,0);
            for(int j=0;j<=target;j++){
                if(moves[j]==1){
                    for(int k=0;k<N;k++){
                        if((j+coins[k])<=target){
                            freshmoves[j+coins[k]]=1;
                        }
                    }
                }
            }
            moves=freshmoves;
        }
        return moves[target]==1;
    }
};