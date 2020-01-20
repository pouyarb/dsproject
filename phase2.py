from yal import *

suspect_name=[]
suspect_key=[]
for k,v in shakhs.dic.items():
    if ((v.mahalekar == 'بنادر') or (v.mahalekar == 'گمرک')):
        havemashin = False
        for m in v.mashinha:
            if int(malekiat.dic[m].tamalok[0:4])>2018:
               suspect_name.append(v.name)
               suspect_key.append(k)
               havemashin = True
               break
        if (havemashin == False):
            for m in v.khaneha:
                if int(malekiat.dic[m].tamalok[0:4])>2017:
                    suspect_name.append(v.name)
                    suspect_key.append(k)
                    havemashin = True
                    break
        if (havemashin == False):
            for i in v.family:
                for j in shakhs.dic[i].mashinha:
                    if int(malekiat.dic[j].tamalok[0:4])>2017:
                        suspect_name.append(v.name)
                        suspect_key.append(k)
                        havemashin=True
                        break
                if havemashin == True:
                    break
                for j in shakhs.dic[i].khaneha:
                    if int(malekiat.dic[j].tamalok[0:4])>2017:
                        suspect_name.append(v.name)
                        suspect_key.append(k)
                        havemashin=True
                        break
                if havemashin == True:
                    break

print(suspect_name)