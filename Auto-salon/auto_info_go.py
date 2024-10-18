#Shohjahon G'aybullayev 11.10.2024.
#Salondagi automobillarni saqlovchi funksiya tuzulgan
#hamma uchun bu narsa
def auto_info(kompaniya,model,rang,karobka,yil,narxi=None):
    '''Automobillar haqida malumot beruvchi dastur'''
    auto={'kompaniya':kompaniya,
          'model':model,
          'rang':rang,
          'karobka':karobka,
          'yil':yil,
          'narxi':narxi}
    return auto
##print("Saytimizdagi autolar ro'yxatini shakllantiramz!!!")
def auto_kirit(): 
    autolar=[]
    while True: 
        print("\nQuyidagi ma'lumotlarni kiring",end=" ")
        kompaniya=input("Qaysi kompaniya: ")
        model=input("Qaysi model: ")
        rang=input("Qaysi rang: ")
        karobka=input("Karobkasi: ")
        yil=input("Qaysi yil: ")
        narxi=input("Qancha narxi: ")
        if kompaniya.lower()=="bmw":  
            autolar.append(auto_info(kompaniya.upper(), model, rang, karobka, yil, narxi))
        else:
            autolar.append(auto_info(kompaniya.title(), model, rang, karobka, yil, narxi))
        javob=input("Yana auto qo'shasizmi(yes/no)")
        if javob=='no': 
            break
        return autolar
def auto_print(): 
    print(f"{autolar['kompaniya']}ning {autolar['model'].title()} automobili {autolar['rang']} rangli {autolar['karobka']}  {auto['yil']}-yili chiqarilgan Narxi:{autolar['narxi']}$")
    