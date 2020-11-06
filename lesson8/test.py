def get_max_subseq(s) -> int:
    counter = 1
    maxi = 0
    if len(s) == 0:
        counter = 0
    elif len(s) == 1:
        counter = 1
    else: 
        for i in range(len(s)-1):  
            if s[i] == s[i+1]:
                counter += 1
            else:
                if counter > maxi:
                    maxi = counter
                counter = 1
        print(f'{counter}')           

get_max_subseq("a")