import pandas as pd

class raas:
    def __init__(self,key = 0):
        self.key=key


class hesabbanki(raas):

    dic={}

    def __init__(self,codemeli=0,namebank=0,shshaba=0,shhesab=0):
        super(hesabbanki,self).__init__(shshaba)
        self.codemeli=codemeli
        self.namebank=namebank
        self.shhesab=shhesab
        self.in_tarakonesh=[]
        self.out_tarakonesh=[]


class khane(raas):

    dic={}

    def __init__(self,codemeli=0,gheymat=0,codeposti=0,metraj=0,addres=0):
        super(khane,self).__init__(codeposti)
        self.codemeli=codemeli
        self.gheymat=gheymat
        self.metraj=metraj
        self.addres=addres


class mashin(raas):

    dic={}

    def __init__(self,pelak=0,codemeli=0,model=0,rang=0):
        super(mashin,self).__init__(pelak)
        self.codemeli=codemeli
        self.model=model
        self.rang=rang


class hamrah(raas):

    dic={}

    def __init__(self,codemeli=0,sim=0,operator=0):
        super(hamrah,self).__init__(sim)
        self.codemeli=codemeli
        self.operator=operator
        self.in_tamas=[]
        self.out_tamas=[]

class shakhs(raas):

    dic={}

    def __init__(self,name=0,familyname=0,codemeli=0,tarikhtavalod=0,mahaletavalod=0,mahalekar=0):
        super(shakhs,self).__init__(codemeli)
        self.name=name
        self.familyname=familyname
        self.tarikhtavalod=tarikhtavalod
        self.mahaletavalod=mahaletavalod
        self.mahalekar=mahalekar
        self.mashinha=[]
        self.khaneha=[]
        self.family=[]
        self.hesabha=[]
        self.hamrahha=[]

 
hesabbanki_csv = pd.read_csv('accounts.csv')
hesabbanki_csv.columns = ['codemeli' , 'namebank', 'shshaba' , 'shhesab']

mashin_csv = pd.read_csv('cars.csv')
mashin_csv.columns= ['model' ,'codemeli','pelak','rang']

khane_csv = pd.read_csv('homes.csv')
khane_csv.columns = ['codemeli', 'gheymat','codeposti','metraj','addres']

hamrah_csv = pd.read_csv('phones.csv')
hamrah_csv.columns = ['codemeli','sim','operator']

shakhs_csv = pd.read_csv('people.csv')
shakhs_csv.drop(columns= 'address',axis =1,inplace = True)
shakhs_csv.columns = ['name','familyname','codemeli','tarikhtavalod','mahaletavalod','mahalekar']

l=len(shakhs_csv)
for i in range(l):
    shakhs.dic[str(shakhs_csv[i:i + 1]['codemeli'].iloc[0])] =shakhs(shakhs_csv[i:i + 1]['name'].iloc[0], shakhs_csv[i:i + 1]['familyname'].iloc[0], shakhs_csv[i:i + 1]['tarikhtavalod'].iloc[0], shakhs_csv[i:i + 1]['mahaletavalod'].iloc[0], shakhs_csv[i:i + 1]['mahalekar'].iloc[0])

l=len(khane_csv)
for i in range(l):
    khane.dic[khane_csv[i:i + 1]['codeposti'].iloc[0]] =khane(khane_csv[i:i + 1]['codemeli'].iloc[0], khane_csv[i:i + 1]['gheymat'].iloc[0], khane_csv[i:i + 1]['codeposti'].iloc[0], khane_csv[i:i + 1]['metraj'].iloc[0], khane_csv[i:i + 1]['addres'].iloc[0])

l=len(mashin_csv)
for i in range(l):
    mashin.dic[mashin_csv[i:i + 1]['pelak'].iloc[0]] =mashin(mashin_csv[i:i + 1]['pelak'].iloc[0], mashin_csv[i:i + 1]['codemeli'].iloc[0], mashin_csv[i:i + 1]['model'].iloc[0], mashin_csv[i:i + 1]['rang'].iloc[0])

l =len(hamrah_csv)
for i in range(l):
    hamrah.dic[hamrah_csv[i:i + 1]['sim'].iloc[0]] =hamrah(str(hamrah_csv[i:i + 1]['codemeli'].iloc[0]), hamrah_csv[i:i + 1]['sim'].iloc[0], hamrah_csv[i:i + 1]['operator'].iloc[0])
    shakhs.dic[str(hamrah_csv[i:i + 1]['codemeli'].iloc[0])].hamrahha.append(hamrah_csv[i:i + 1]['sim'].iloc[0])

l=len(hesabbanki_csv)
for i in range(l):
    hesabbanki.dic[str(hesabbanki_csv[i:i + 1]['shhesab'].iloc[0])] =hesabbanki(str(hesabbanki_csv[i:i + 1]['codemeli'].iloc[0]), str(hesabbanki_csv[i:i + 1]['namebank'].iloc[0]), hesabbanki_csv[i:i + 1]['shshaba'].iloc[0], str(hesabbanki_csv[i:i + 1]['shhesab'].iloc[0]))
    shakhs.dic[str(hesabbanki_csv[i:i + 1]['codemeli'].iloc[0])].hesabha.append(str(hesabbanki_csv[i:i + 1]['codemeli'].iloc[0]))
