"""Verilen tabloyu sinav_sonuc isimli bir sözlük oluşturarak ona aktarınız. (Sözlüğün
anahtarları tablo başlıkları olacak. Örneğin, isim, cinsiyet vs.)"""
sinav_sonuc = {'isimler': ['ayse K.', 'Ahmet M.', 'Nuri C.', 'Nawar T.', 'Suzan T.', 'Ala B.'],
               'cinsiyet': ['K', 'E', 'E', 'E', 'K', 'K'], 'matematik': [60, 40, 97, 45, 56, 95],
               'turkce': [70, 30, 23, 80, 78, 46]}
"""Kullanıcının klavyeden girdiği bilgileri (öğrencinin ismi, cinsiyeti, matematik dersinden
aldığı not, Türkçe dersinden aldığı not), oluşturduğunuz sinav_sonuc isimli sözlüğe
kaydeden bir fonksiyon tanımlayınız."""
def yeni_kayit():
    yeni_ismi = []
    yeni_cinsiyet = []
    yeni_mat_not = []
    yeni_turkce_not = []
    yeni_isim1 = []
    #Kullanıcıdan klavyeden 2 yeni kayıt girmesini isteyiniz
    for i in range(2):
        isim = input("isim giriniz :")
        cinsiyet = input("cinsiyet giriniz :")
        mat_notu = input("Matematik notu giriniz:")
        turkce_notu = input("turkce notu giriniz :")
        yeni_ismi.append(isim)
        yeni_cinsiyet.append(cinsiyet)
        yeni_mat_not.append(mat_notu)
        yeni_turkce_not.append(turkce_notu)
        print(yeni_ismi)
        print(yeni_cinsiyet)
        print(yeni_mat_not)
        print(yeni_turkce_not)
        """Girilen yeni kayıtlarla birlikte güncellenmiş olan tabloyu (sinav_sonuc sözlüğünü)
ekrana yazdırınız."""
    for k in range(2):
        sinav_sonuc['isimler'].append(yeni_ismi[k])
        sinav_sonuc['cinsiyet'].append(yeni_cinsiyet[k])
        sinav_sonuc['matematik'].append(yeni_mat_not[k])
        sinav_sonuc['turkce'].append(yeni_turkce_not[k])
        
        print(sinav_sonuc["isimler"],'\n')
        print(sinav_sonuc["cinsiyet"], '\n')
        print(sinav_sonuc["matematik"],'\n')
        print(sinav_sonuc["turkce"])

yeni_kayit()