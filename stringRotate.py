def StringRotate(st):
    tmpCh=""
    length=len(st)-1
    res=[]
    res.append(st)
    if len(st)==0:
        return res
    while length:
        tmpCh=st[0]
        st=st[1:]
        st=st+tmpCh
        res.append(st)
        length=length-1
    return res

if __name__=="__main__":
    st=input("Enter your world please: ")
    print(StringRotate(st))