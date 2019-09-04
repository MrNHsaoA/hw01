a='        '
for i in range(9,0,-1):

    for kg in range(1,2):

        print(a*(22-i),end='') 

    for j in range(i,0,-1):
        
        print(f"{j:2d}x{i:<2d}={i*j:2d}",end='')

    print()
