from phase3 import *

radtamas=[]
for k,v in ravabet.dic.items():
    for sus in v:
        for sh in shakhs.dic[sus].hamrahha:
            for cal in hamrah.dic[sh]:
                if tamas.dic[cal].prev in shakhs.dic[k].hamrahha:
                    radtamas.append([k,sus,tamas.dic[cal].zaman])
                elif tamas.dic[cal].next in shakhs.dic[k].hamrahha:
                    radtamas.append([sus,k,tamas.dic[cal].zaman])

print('phase 4')
for i in radtamas:
    print(i[0],'->',i[1],':',i[2])
