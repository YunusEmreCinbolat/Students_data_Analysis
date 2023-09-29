import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

#combine with different dataset

#https://www.kaggle.com/datasets/joebeachcapital/students-performance
df=pd.read_csv("DATA.csv")
print(df.head(10000000))

#ayrıntılı analiz
#print(df.info())
#print(df.isnull().sum())

#future engineering alanını dahil et
age_group=["22-25", "18-21", "26-"]
age_intervals = df['1'].value_counts()

# almak istenen sonuca göre detaylı görselleştirme araçlarını  incele (chart tipi)

# Number of people by age range View results
print(age_intervals)
plt.figure(figsize=(12,6))
sns.barplot(x=age_group, y=age_intervals, data=age_intervals, palette='viridis')
plt.title("Yas gruplarına göre öğrenci sayisi")
plt.xlabel("Yas aralıkları")
plt.ylabel("Kisi sayısı")
plt.show()

# Number of people by gender View results
gender_gore_distribution=df["2"].value_counts()
plt.figure(figsize=(12,6))
sns.barplot(x=["Erkek","Kadın"], y=gender_gore_distribution, data=gender_gore_distribution, palette='viridis')
plt.title("Cinsiyete göre dağılım")
plt.xlabel("Cinsiyet")
plt.ylabel("Kişi sayısı")

plt.show()

# Number of sexes by each age group View results
for age_group in age_intervals.index:
    mourning_data = df[df['1'] == age_group]
    gender_distribution = mourning_data["2"].value_counts()
    print(f'{age_group} Yaş Grubu Cinsiyet Dağılımı:')
    print(gender_distribution)
    print("\n")
    plt.figure(figsize=(12, 6))
    sns.barplot(x=gender_distribution, y=["Erkek", "Kadın"], palette="viridis")
    plt.title(f'{age_group.numerator} Yaş Grubu Cinsiyet Dağılımı')
    plt.xlabel("Cinsiyet")
    plt.ylabel("Kişi Sayısı")
    plt.show()

#How many students graduated from which type of high school
high_school_group_name=["Devlet", "Özel", "Diğer"]
high_school_group=df['3'].value_counts()
print(high_school_group)
plt.figure(figsize=(12,6))
sns.barplot(x=high_school_group_name, y=high_school_group, data=high_school_group, palette="viridis")
plt.xlabel("Lise türü")
plt.ylabel("Kişi sayısı")
plt.show()

#Number of students according to scholarship amounts
scholarship_kisi=df["4"].value_counts()
scholarship_amount=["50", "75", "100", "25", "0"]
sns.barplot(x=scholarship_amount, y=scholarship_kisi, data=scholarship_kisi, palette='viridis')
plt.xlabel("Burs miktarları")
plt.ylabel("Kişi sayısı")
plt.show()

print("Ek Calisma")
ek_calisma=df["5"].value_counts()
print(ek_calisma)

print("Sanatsal etkinlik")
sanatsal_etkinlik=df["6"].value_counts()
print(sanatsal_etkinlik)

print("Partner")
partner_sayisi=df["7"].value_counts()
print(partner_sayisi)

print("Toplam maas")
toplam_maas=df["8"].value_counts()
print(toplam_maas)

print("Ulasim")
ulasim=df["9"].value_counts()
print(ulasim)

print("Konaklama")
konaklama=df["10"].value_counts()
print(konaklama)

print("Anne egitimi")
anne_egitim=df["11"].value_counts()
print(anne_egitim)

print("Baba egitim")
baba_egitim=df["12"].value_counts()
print(baba_egitim)

print("Kız kardes")
kiz_kardes=df["13"].value_counts()
print(kiz_kardes)

print("Ebeveyn durumu")
ebeveyn_durum=df["14"].value_counts()
print(ebeveyn_durum)

print("Anne meslegi")
anne_meslek=df["15"].value_counts()
print(anne_meslek)

print("Baba meslegi")
baba_meslegi=df["16"].value_counts()
print(baba_meslegi)

print("Haftalik calisma saati")
haftalik_calisma_saati=df["17"].value_counts()
print(haftalik_calisma_saati)

print("Bilimsel olmayayan Okuma sıklığı")
bilimsel_olmayan_okuma_araligi=df["18"].value_counts()
print(bilimsel_olmayan_okuma_araligi)

print("Bilimsel Okuma sıklığı")
bilimsel_okuma_araligi=df["19"].value_counts()
print(bilimsel_okuma_araligi)

print("Etkinlik katilim")
etkinlik_katilim=df["20"].value_counts()
print(etkinlik_katilim)

print("Etkinliklerin başarıya etkisi")
etkinlik_basari_etki=df["21"].value_counts()
print(etkinlik_basari_etki)

print("Ders devam")
ders_devam=df["22"].value_counts()
print(ders_devam)

print("Ara sınavlara hazırlık biçimi")
ara_sinav_hazirlik_bicim=df["23"].value_counts()
print(ara_sinav_hazirlik_bicim)

print("Ara sınalara hazırlık zaman")
ara_sinav_hazirlik_zaman=df["24"].value_counts()
print(ara_sinav_hazirlik_zaman)

print("Derste not alma")
derste_not_alma=df["25"].value_counts()
print(derste_not_alma)

print("Ders dinleme")
ders_dinleme=df["26"].value_counts()
print(ders_dinleme)

print("Tartismanin derse etkisi")
tartisma_ders_etki=df["27"].value_counts()
print(baba_egitim)

print("flip sinif")
flip_sinif=df["28"].value_counts()
print(flip_sinif)

print("Somn yarıyıl genel not ortalamasi")
son_yariyil_not=df["29"].value_counts()
print(son_yariyil_not)

print("Mezuniyet not beklentisi")
mezuniyet_not_beklentisi=df["30"].value_counts()
print(mezuniyet_not_beklentisi)


print("Mezuniyet derecesi")
mezuniyet_derecesi=df["32"].value_counts()
print(mezuniyet_derecesi)





