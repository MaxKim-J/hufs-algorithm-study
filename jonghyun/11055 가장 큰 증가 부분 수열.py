def dp_lis(seq, save, pos):
    if save[pos]!=0:
        pass
    elif pos==0:
        save[pos]=seq[pos]
    else:
        max_idx=pos
        for i in range(pos-1, -1, -1):
            tmp_idx=dp_lis(seq,save,i)
            if save[max_idx] < save[tmp_idx] and seq[i]<seq[pos]:
                max_idx=tmp_idx;
        save[pos]=save[max_idx]+seq[pos]
    
    for i in save:
        print(i,end=" ")
    print()

    return pos


if __name__=="__main__":
    n=int(input())

    seq=list(map(int, input().split(" ")))
    save=[0 for i in range(n)]
    
    dp_lis(seq, save, n-1)

    max=0
    for i in save:
        if max < i:
            max = i

    print(max)
    




