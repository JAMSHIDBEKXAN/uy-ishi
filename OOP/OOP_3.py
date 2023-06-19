class Futbolchi:
    def __init__(self, ism, yoshi, transfer_narxi, oyligi, gollar_soni):
        self.ism = ism
        self.yoshi = yoshi
        self.transfer_narxi = transfer_narxi
        self.oyligi = oyligi
        self.gollar_soni = gollar_soni

    def __str__(self):
        return f"""
ismi: {self.ism}
yoshi: {self.yoshi}
transfer_narxi: {self.transfer_narxi}        
oyligi: {self.oyligi}
gollar_soni: {self.gollar_soni}"""


class Murabbiy:
    def __init__(self, ism, yoshi, tajribasi, oyligi):
        self.ism = ism
        self.yoshi = yoshi
        self.tajribasi = tajribasi
        self.oyligi = oyligi

    def __str__(self):
        return f"""
ismi: {self.ism}
yoshi: {self.yoshi}
tajribasi: {self.tajribasi}
oyligi: {self.oyligi}"""


class Klub:
    def __init__(self, nomi, orni,kuboklar_soni):
        self.nomi = nomi
        self.orni = orni
        self.kuboklar_soni=kuboklar_soni
        self.futbolchilar = []
        self.murabbiylar = []

    def add_futbolchi(self, obj: Futbolchi):
        if obj.gollar_soni > 150:
            self.futbolchilar.append(obj)

    def add_murabbiy(self, obj2: Murabbiy):
        if obj2.tajribasi > 1:
            self.murabbiylar.append(obj2)

    def malumot(self):
        futbolchilar = "\n".join([f"\t{futbolchi}" for futbolchi in self.futbolchilar])
        murabbiylar = "\n".join([f"\t{murabbiy}" for murabbiy in self.murabbiylar])
        return f"""
{self.nomi}, 
turnir jadvalidagi orni: {self.orni}
kuboklar soni: {self.kuboklar_soni}
Futbolchilar:
{futbolchilar}
Murabbiylar:
{murabbiylar}"""


f1 = Futbolchi('Rooney', 37, 50, 35, 345)
f2 = Futbolchi('Messi', 36, 120, 600, 1100)
f3 = Futbolchi('Rashford', 24, 130, 21, 215)
f4 = Futbolchi('Pedri', 18, 170, 19, 48)
f5 = Futbolchi('Gavi', 16, 150, 17, 53)
f6 = Futbolchi('Greenwood', 21, 80, 25, 120)

m1 = Murabbiy('Gvardiola', 55, 15, 20)
m2 = Murabbiy('Ser Alex Ferguson', 65, 22, 25)

k1 = Klub('Manchester United', 2,35)
k1.add_futbolchi(f1)
k1.add_futbolchi(f3)
k1.add_futbolchi(f6)
k1.add_murabbiy(m2)

k2 = Klub('Barcelona', 1,42)
k2.add_futbolchi(f2)
k2.add_futbolchi(f4)
k2.add_futbolchi(f5)
k2.add_murabbiy(m1)

print(k1.malumot())
print(k2.malumot())
