import configparser
import codecs
import pandas as pd

# Создание экземпляра ConfigParser
sev = configparser.ConfigParser()
zu='_________________________________________'
# Чтение INI-файла в кодировке Windows-1251
with codecs.open('sev.ini', 'r', encoding='windows-1251') as file:
    sev.read_file(file)
    
adr=[]#адрес для загрузки - [Cells, общ...]
table=[]#вся табл[[общ,тип][знак,типы]]
    
# загрузка табл
def load(y_x,adr,table):
    m=''
    y,x=map(int, y_x.split())
    if not adr:
        #adr=['Cells','общ','int']
        adr=['Cells']
        #s=общ<.>тип<.>биб
        s = sev.get('StringGrid1', 'Cells')
        #спис 1го столба
        table = [s.split('<.>')] 
    else:
        #d=>Cells<.>общ
        d='<.>'.join(adr[:x+1]+[table[x][y]])
        if sev.has_option('StringGrid1',d):
            #s=общ<.>тип<.>биб
            s = sev.get('StringGrid1', d)
            #adr=['Cells','общ','int']
            adr=d.split('<.>')
            if len(table)>x+1:
                #print('=')
                table[x+1]=s.split('<.>')
            else:
                #print('append')
                table.append(s.split('<.>'))
                #table=[[общ,тип,биб][знак, др, др]]
            print(zu)
            print('/'.join(d.split('<.>')))
        else:
        	print('подменю нет:\n'+d)
        if sev.has_option('Memo1',d):
            print(zu)
            s = sev.get('Memo1', d)
            s=s.split('<.>')
            m='\n'.join(s)
    return adr, table, m
    
adr,table,m=load('0 0',[],[])	
df=pd.DataFrame(table)#визуал табл
dft = df.transpose()
print(dft)

while True:
    print(zu)
    #загрузка др столба
    yx=input('выбери ячейку [y x]\n')
    adr,table,m=load(yx,adr,table)	
    df=pd.DataFrame(table)#визуал табл
    dft = df.transpose()
    print(dft)
    if m:
    	print(zu)
    	print(m)