import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',None)
pd.set_option('display.width',500)

#combine with different dataset

#https://www.kaggle.com/datasets/joebeachcapital/students-performance
df=pd.read_csv("dataset/DATA.csv")
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
