import Pizza
import Decorator
import locale
import csv
import datetime

#Türkçe karakterleri okumak için
locale.getpreferredencoding()

#Siparişten sonra müşteri verileri csv veritabanına kayıt ediliyor
def databaseYaz(isim, tcno, kkno, desc, ordertime, kksifre):
    # Veritabanı ekleme modunda açılıyor
    with open('Orders_Database.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        #parametreler listeye keleniyor
        #Bunun sebebi writerow() fonksiyonunun liste kabul etmesi.
        liste = [isim, tcno, kkno, desc, ordertime, kksifre]
        #Satır halinde veritabanına kayıt ediliyor
        writer.writerow(liste)

def databaseOku():
    #Programın sonunda kayıtlı müşteriler ekrana yazdırılıyor
    #csv veritabanı dosyası okuma modunda açılıyor
    with open('Orders_Database.csv', 'r') as file:
        reader = csv.reader(file)
        #Tüm satırlar döngü içinde okuluyor ve ekrana yazdırılıyor
        for row in reader:
            print(row)
                
def main():
    #Program içinde kullanılacak değişkenler tanımlanıyor
    toplamFiyat = 0
    pizzaAciklama = ""
    
    #Menu menu.txt dosyasından alınıyor
    #Utf-8 ile Türkçe karakterler sorunsuz ekrana yazdırılıyor
    f = open("menu.txt", encoding='utf-8')
    print(f.read())

    #Kullanıcıdan Pizza seçimi isteniyor
    print("Pizza Seç: ")
    pizzasec = input()

    #Kullanıcı seçimine göre sınıftan nesne türetiliyor.
    #Toplam fiyata ekleniyor.
    match pizzasec:
        case "1":
            print("Klasik pizza seçtiniz!")
            k = Pizza.Klasik()
            print(k.get_description())
            print("Klasik Pizza Fiyat: {}".format(k.get_cost()))
            toplamFiyat += k.get_cost()
            pizzaAciklama = k.get_description()
        case "2":
            print("Margarita pizza seçtiniz!")
            m = Pizza.Margherita()
            print(m.get_description())
            print("Margherita Pizza Fiyat: {}".format(m.get_cost()))
            toplamFiyat += m.get_cost()
            pizzaAciklama = m.get_description()
        case "3":
            print("Türk pizza seçtiniz!")
            t = Pizza.TurkPizza()
            print(t.get_description())
            print("Margherita Pizza Fiyat: {}".format(t.get_cost()))
            toplamFiyat += t.get_cost()
            pizzaAciklama = t.get_description()
        case "4":
            print("Dominos pizza seçtiniz!")
            d = Pizza.DominosPizza()
            print(d.get_description())
            print("Margherita Pizza Fiyat: {}".format(d.get_cost()))
            toplamFiyat += d.get_cost()
            pizzaAciklama = d.get_description()
        #Yanlış seçimde programdan çıkış yapılıyor
        case default:
            print("Yanlış seçim")
            exit()

    #Pizza seçiminin ardından sos seçimi yapılıyor
    #Seçime göre sınıftan nesne türetiliyor
    print("Sos Seç: ")
    sossec = input()

    match sossec:
        case "11":
            d = Decorator.Zeytin()
            print(d.get_description())
            print(d.get_cost())
            toplamFiyat += d.get_cost()
            pizzaAciklama += ' ' + d.get_description()
            
        case "12":
            d = Decorator.Mantar()
            print(d.get_description())
            print(d.get_cost())
            toplamFiyat += d.get_cost()
            pizzaAciklama += ' ' + d.get_description()
        case "13":
            d = Decorator.KeciPeyniri()
            print(d.get_description())
            print(d.get_cost())
            toplamFiyat += d.get_cost()
            pizzaAciklama += ' ' + d.get_description()
        case "14":
            d = Decorator.Et()
            print(d.get_description())
            print(d.get_cost())
            toplamFiyat += d.get_cost()
            pizzaAciklama += ' ' + d.get_description()
        case "15":
            d = Decorator.Sogan()
            print(d.get_description())
            print(d.get_cost())
            toplamFiyat += d.get_cost()
            pizzaAciklama += ' ' + d.get_description()
        case "16":
            d = Decorator.Misir()
            print(d.get_description())
            print(d.get_cost())
            toplamFiyat += d.get_cost()
            pizzaAciklama += ' ' + d.get_description()
        #Yanlış seçimde programdan çıkış yapılıyor
        case default:
            print("Yanlış seçim")
            exit()

    #Toplam ödenecek fiyat
    print("Toplam Ödeyeceğiniz Tutar: {}".format(toplamFiyat))
    #Kullanıcıdan kişisel bilgiler alınıyor
    print("İsminizi giriniz: ")
    isim = input()

    print("TC Kimlik No giriniz: ")
    tc = input()

    print("Kredi Kartı No giriniz: ")
    kkno = input()

    print("Kredi Kartı Şifresi giriniz: ")
    kksifre = input()

    #Kullanıcı bilgileri, tarih ve açıklama ile birlikte veritabanına yazılıyor
    databaseYaz(isim, tc, kkno, pizzaAciklama, datetime.datetime.now().strftime("%c"), kksifre)

#main metodu çağırılıyor.
main()
#Veritabanındaki bilgiler ekrana yazdırılıyor.
print("\n\n\nKayıtlı müşteriler okunuyor...\n\n\n")
databaseOku()

