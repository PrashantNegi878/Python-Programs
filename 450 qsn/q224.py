class Solution:
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        arr=[]
        total=0.0
        output=0.0
        temp=0.0
        for i in range (len(Items)):
            arr.append([Items[i].value/Items[i].weight,Items[i].value,Items[i].weight])
        arr.sort(reverse=True)
        # print(arr)
        i=0
        while total<W:
            if total+arr[i][2]<=W:
                total+=arr[i][2]
                output+=arr[i][1]
                # print("Output = ",output)
                i+=1
            else:
                temp=W-total
                # print(temp)
                total=total+temp
                output+=arr[i][0]*temp
                # print("Output = ",output)
                break
        return output