

def fetchpermutations(s):
    index = 0
    arr = []
    str = [i for i in s]
    
    def permute(str, index, arr):
        s = len(str)
        if s-1 == index:
            arr.append("".join(str))
            return
        
        for i in range(index, s):
            str[index], str[i] = str[i], str[index]
            permute(str, index+1, arr)
            str[index], str[i] = str[i], str[index]
    
    permute(str, index, arr)

    sorted(arr)

    for i in arr:
        print(i)

s="abc"
fetchpermutations(s)



