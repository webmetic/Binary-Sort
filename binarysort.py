#input list
l=[10,9,8,7,6,5,4,3,2,1]

#list being created
n=[l[0]]

#comparing the value of l[i] with the centre of the List 'n'
for t in range(1,len(l)):
    a=l[t] #the element being compared
    g=t  #length of the list at the moment
    j=g//2 #the index at the centre of the list
    while  g!=j and g!=0 and j!=t:  
        if a<n[j]:
            g=j 
            j=j//2
        else:
            j=j+1+(g-j-1)//2    #g is the second last value of j
    else:
        n.insert(j,a)

print("Sorted Array:",n)
