# no of sticks
#input [1,8,1,8,8] sides of rectangle #[4,2,3,2,3,4,5,1].....>[4,2,3] ..>12 after removing non repeated elements
#rect....> opp sides are equal
#remove non repeated items becuase


def max_area(no_sticks,arr):

    #removing non repeated elements and append repeated item
    if len(arr)==no_sticks:
        res=[]
        for i in arr:
            if arr.count(i)>=2 and i not in res:
                res.append(i)

        sum=0
        #finding product of elemets
        for i in range(len(res)):
            for j in range(i+1,len(res)):
                if res[i]*res[j]>sum:
                    sum=res[i]*res[j]


        print(sum)
    else:
        print("enter elemets based on no_of sticks")





max_area(no_sticks=int(input("enter no of sticks")),arr=eval(input("enter liost")))
