def func(lst):
    output_lst=[]
    for a in range(len(lst)):
        for b in range(a+1,len(lst)):
            if lst[a]*lst[b]%2==0 and (lst[a]+lst[b])%2==1:
                output_lst.append((lst[a],lst[b]))
    print("Product even and sum odd pairs are: ")
    print(output_lst)


func([2,9,6,2,3,-3])
