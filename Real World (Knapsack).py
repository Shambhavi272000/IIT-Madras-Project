# 0-1 Knapsack Problem 
# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack
WW = int(input("\nEnter total weight."))
NN = int(input("\nEnter number of elements"))
vv = list(map(int,input("\nEnter the values : ").strip().split()))[:NN]
ww = list(map(int,input("\nEnter the weights : ").strip().split()))[:NN]
def knapsack01(W,N,v,w) :
    DP = [[0 for i in range(W+1)] for j in range(N+1)] 
    for i in range(1,N+1) :
        for j in range(1,W+1) :
            if w[i-1] <= j : 
                DP[i][j] = max(v[i-1]+DP[i-1][j-w[i-1]],DP[i-1][j]) 
            else :
                DP[i][j] = DP[i-1][j]
    return DP[N][W]
print(knapsack01(WW,NN,vv,ww))