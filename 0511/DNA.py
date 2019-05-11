def comp(seq):
    comp_dict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    seq_comp = ""
    for char in seq:
        seq_comp = seq_comp + comp_dict[char]
    return seq_comp

def rev(seq):
    seq_rev = "".join(reserved(seq))
    return seq_rev

def rev_comp(seq):
    tmp = comp(seq)
    return rev(tmp)
src = input("DNA sepurence : ")
cnvt = int(input("1(Comp), 2(Rev), 3(Rev_Comp) : "))
if(cnvt >= 1 and cnvt <= 3):
    if(cnvt == 1):
        rst = comp(src)
    elif(cnvt == 2):
        rst = rev(src)
    else:
        rst = rev_comp(sec)
    print(src,"->", rst)
else:
    print("1(Comp), 2(Rev), 3(Rev_Comp)!!!")
                                        
