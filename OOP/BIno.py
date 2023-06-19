class bino:
    def __init__(self,nomi,balandlik):
        self.nomi=nomi
        self.balandlik=balandlik
        
    def info(self):
        if self.balandlik>50:
            print(f"""
nomi:{self.nomi}
balandlik:{self.balandlik }                  """)
        # else:
        #     print(f"{self.nomi} balandlik yetarli emas")


st1= bino('Samo',57)
st2=bino('Anis',42)
st3=bino('LEO',83)
st4=bino('MAN UTD',101)
st5=bino('Ziyo',35)
print(st1.info())
print(st2.info())
print(st3.info())
print(st4.info())
print(st5.info())
# st1.info()
# st2.info()
# st3.info()
# st4.info()
# st5.info()