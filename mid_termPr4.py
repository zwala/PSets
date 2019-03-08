
def closest_power(base,num):
    #(2,9)
    ex=0
    for i in range(1,num):
        if abs(base**i - num)<=abs(base**(i+1)-num):
            ex=i
            break
    return ex

#LA=[1,2,3]
#LB=[4,5,6]
#4+10+18=32
def dotProd(LA,LB):
    sum=0
    for each in range(len(LA)):
        sum=sum+(LA[each]*LB[each])
    return sum

L=[[1,2],[3,4],[5,6,7]]
def deep_reverse(l):
    new=[]
    for i in l:
        new.append(i[::-1])
    L[:]=new[::-1]
    return L


def flatten(l):
    newl=[]
    for i in l:
        if type(i)==list:
            newl.extend(flatten(i))
        else:
            newl.append(i)
    return newl
def count7(N):
    if N < 10:
        if N %10 == 7:
            return 1
        else:
            return 0
    elif N % 10 == 7:
        return 1 + count7(N//10)
    else:
        return 0 + count7(N//10)
    
def lessThan4(aList):
    b=[]
    for each in aList: 
        if len(each)<4:
            b.append(each)
    return b


"""
def dict_invert(d):
    inverse={}
    for e in d.keys():
        if d[e] in inverse:
            inverse[d[e]].append(e)
        else:
            inverse[d[e]]=[e]
    for val in inverse.values():
        val.sort()
    return inverse"""
    
def dict_invert(d):
    inverted={}
    for dkey in d.keys():
        if d[dkey] in inverted:
            inverted[d[dkey]].append(dkey)
        else:
            inverted[d[dkey]]=[dkey]
    for val in inverted.values():
        val.sort()
    return inverted

def f(s):
    return 'a' in s
def satisfiesF(L):
    #L=['list','of','strings']
    li=L[:]
    sum=0
    for each in li:
        if f(each)==True:
            sum+=1
        else:
            L.remove(each)
    return sum
    

L=['apple','b','a']
print (satisfiesF(L))
print (L)
    
#run_satisfiesF(L,satisfiesF)    
#Create a dictionary for lyrics:
def lyrics2freq(lyrics):
    newD={}
    for i in lyrics:
        if i in newD:
            newD[i]+=1
        else:
            newD[i]=1