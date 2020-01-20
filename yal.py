from raas import *
import pandas as pd

class yal:
    def __init__(self,key = 0,next = None, prev = None):
        self.key=key
        self.next= next
        self.prev=prev

class malekiat(yal):

    dic={}

    def __init__(self,sabteahval=0, tamalok=0, pardakhti=0, next=None, prev=None):
        super(malekiat,self).__init__(sabteahval,next,prev)
        self.tamalok=tamalok
        self.pardakhti=pardakhti
          
class tarakonesh(yal):

    dic={}

    def __init__(self,shomare=0, zaman=0, mablagh=0, next=None, prev=None):
        super(tarakonesh,self).__init__(shomare,next,prev)
        self.zaman=zaman
        self.mablagh=mablagh

class tamas(yal):

    dic={}

    def __init__(self,shomare=0,zaman=0,modat=0, next=None, prev=None):
        super(tamas,self).__init__(shomare,next,prev)
        self.zaman=zaman
        self.modat=modat

class family(yal):

    dic={}
    
    def __init__(self,tarkibi=0, nesbat=0, shoruenesbat=0, next=None, prev=None):
        super(family,self).__init__(tarkibi,next,prev)
        self.nesbat=nesbat
        self.shoruenesbat=shoruenesbat


tamsa_csv=pd.read_csv('calls.csv')
tamsa_csv.columns=['prev','next','shomare','zaman','modat']

malekiat_csv = pd.read_csv('ownerships.csv')
malekiat_csv.columns = ['prev','next','sabteahval','tamalok', 'pardakhti']

family_csv = pd.read_csv('relationships.csv')
family_csv.columns = ['prev','next','nesbat','shoruenesbat']

tarakonesh_csv = pd.read_csv('transactions.csv')
tarakonesh_csv.columns = ['prev','next','shomare','zaman','mablagh']

l=len(tamsa_csv)
for i in range(l):
    a=tamsa_csv[i:i+1]['shomare'].iloc[0]
    tamas.dic[a] =tamas(a, tamsa_csv[i:i + 1]['zaman'].iloc[0], tamsa_csv[i:i + 1]['modat'].iloc[0], tamsa_csv[i:i + 1]['next'].iloc[0], tamsa_csv[i:i + 1]['prev'].iloc[0])
    hamrah.dic[tamsa_csv[i:i + 1]['next'].iloc[0]].in_tamas.append(a)
    hamrah.dic[tamsa_csv[i:i + 1]['prev'].iloc[0]].out_tamas.append(a)



l=len(tarakonesh_csv)
for i in range(1,l):
    a=str(tamsa_csv[i:i+1]['shomare'].iloc[0])
    tarakonesh.dic[a] =tarakonesh(a, tarakonesh_csv[i:i + 1]['zaman'].iloc[0], str(tarakonesh_csv[i:i + 1]['mablagh'].iloc[0]), str(tarakonesh_csv[i:i + 1]['next'].iloc[0]), str(tarakonesh_csv[i:i + 1]['prev'].iloc[0]))
    hesabbanki.dic[str(tarakonesh_csv[i:i + 1]['next'].iloc[0])].in_tarakonesh.append(a)
    hesabbanki.dic[str(tarakonesh_csv[i:i + 1]['prev'].iloc[0])].out_tarakonesh.append(a)
print('transaction read')

l=len(malekiat_csv)
for i in range(l):
    a=malekiat_csv[i:i+1]['sabteahval'].iloc[0]
    malekiat.dic[a] =malekiat(a, malekiat_csv[i:i + 1]['tamalok'].iloc[0], malekiat_csv[i:i + 1]['pardakhti'].iloc[0], malekiat_csv[i:i + 1]['next'].iloc[0], malekiat_csv[i:i + 1]['prev'].iloc[0])
    if malekiat_csv[i:i+1]['next'].iloc[0] in khane.dic:
        shakhs.dic[str(malekiat_csv[i:i + 1]['prev'].iloc[0])].khaneha.append(a)
    else:
        shakhs.dic[str(malekiat_csv[i:i + 1]['prev'].iloc[0])].mashinha.append(a)
print('ownerships read')

l=len(family_csv)
for i in range(l):
    a=str(family_csv[i:i+1]['prev'].iloc[0])+ "+" +str(family_csv[i:i+1]['next'].iloc[0])
    family.dic[a] =family(a, family_csv[i:i + 1]['nesbat'].iloc[0], family_csv[i:i + 1]['shoruenesbat'].iloc[0], family_csv[i:i + 1]['next'].iloc[0], family_csv[i:i + 1]['prev'].iloc[0])
    shakhs.dic[str(family_csv[i:i + 1]['prev'].iloc[0])].family.append(family_csv[i:i + 1]['next'].iloc[0])
print('relationships read')
