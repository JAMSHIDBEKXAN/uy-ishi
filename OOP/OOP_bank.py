class Card:
    def __init__(self, nomi, srok):
        self.__balance = 0
        self.__pin = 2908
        self.nomi = nomi
        self.srok = srok
        self.oylik = 3000000

    def get_balance(self):
        return self.__balance

    def set_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("Pin kodi o'zgartirildi.")
        else:
            print("pin kod xato terildi.")

    def set_balance_minus(self, pin):
        if pin == self.__pin:
            mablag
            if self.__balance >= mablag:
                self.__balance -= mablag
                print(f"{mablag} so'm yechildi.")
            else:
                print("Kartadagi mablag' kam.")
        else:
            print("pin kod xato.")

    def set_balance_plus(self, pin):
        if pin == self.__pin:
            mablag
            self.__balance += mablag
            print(f"{mablag} so'm muvaffaqiyatli qo'shildi.")
        else:
            print("pin kod xato.")

    def all_balance(self, pin,mablag):
        if pin == self.__pin:
            mablag = self.__balance
            self.__balance = 0
            print(f"{mablag} so'm yechildi.")
        else:
            print("pin kod xato.")

    def oylik_chiqim(self):
        self.__balance -= self.oylik

if __name__ == "__main__":
    kard = Card("HUMO", "29-11-2028")
    while True:
        print("""
[1] -> Balance ko'rish
[2] -> Balance qo'shish
[3] -> Balansdan pul yechish
[4] -> Pin almashtirish
[0] -> Exit   
        """)
        tanlov = input("Tanlang: ")
        if tanlov == "1":
            pin = int(input("Pin kodni kiriting: "))
            print(f"Joriy balans: {kard.get_balance()} so'm.")

        elif tanlov == "2":
            pin = int(input("Pin kodni kiriting: "))
            mablag = int(input("Qancha mablag' qo'shasiz? "))
            kard.set_balance_plus(pin,mablag)

        elif tanlov == "3":
            pin = int(input("Pin kodni kiriting: "))
            mablag = int(input("Qancha mablag' yechasiz? "))
            kard.set_balance_minus(pin, mablag)

        elif tanlov == "4":
            old_pin = int(input("Joriy pin kodni kiriting: "))
            new_pin = int(input("Yangi pin kodni kiriting: "))
            kard.set_pin(old_pin, new_pin)

        elif tanlov == "0":
            break

    kard.all_balance(2908)
