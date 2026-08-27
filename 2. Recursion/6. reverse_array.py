#--------------------xx BRUTE FORCE METHOD xx---------------------#
# def rev_array(arr):
#     r_arr =arr[::-1]
#     return r_arr
        
#--------------------xx Using Build-In Function xx---------------------# 
# def rev_array(arr):
#     arr.reverse()
#     return arr

#--------------------xx Better Approach(using pointers) xx---------------------# 
def rev_array(arr):
    p1 = 0
    p2= len(arr)-1
    while p1<p2:
        arr[p1],arr[p2]=arr[p2],arr[p1]
        p1+=1
        p2-=1
    return arr

arr =[5,4,3,2,1]
print (rev_array(arr))