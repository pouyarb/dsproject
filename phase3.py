from phase2 import *

def bfs(ls,ghachaghchi,level):
    for i in ls:
        star=set()
        mg=hesabbanki.dic[tarakonesh.dic[i].prev]
        if shakhs.dic[mg.codemeli].mahalekar == 'قاچاقچی':
            ghachaghchi.append(mg.codemeli)
            continue
        if level<4:
            for tar in mg.in_tarakonesh:
                if tarakonesh.dic[tar].zaman < tarakonesh.dic[i].zaman:
                    star=star|{tar,}
    return list(star)


ravabet={}
for p in suspect_key:
    ghachaghchi=[]
    x=[]
    for hes in shakhs.dic[p].hesabha:
        x.extend(hesabbanki.dic[hes].in_tarakonesh)
    for i in range(5):
        x=bfs(x,ghachaghchi,i)
    if len(ghachaghchi)>0:
        ravabet[p]=ghachaghchi
