from faker import Faker
fake = Faker(locale="fr_FR")

print(fake.name())
# Victor Barre

print(fake.address())
# 930, boulevard de Barbier
# 56914 Saint Simone-les-Bains

print(fake.text())

print('---------------------------------------')

from faker import Faker
fake = Faker(locale="fr_CA")

for _ in range(10):
    print(fake.name())

# Louis Blouin
# Dominique Forget
# Emmanuelle Langlois-Lauzon
# Jean Pilon
# Audrey Gagné
# Sylvie Drolet
# Stéphanie Smith
# Louise Dufresne
# Robert-René Labbé
# Rémy Thériault


print('----------------------------------------')

from random import randint 
import pandas as pd 
 
fake = Faker()
 
def input_data(x):
   
    # pandas dataframe
    data = pd.DataFrame()
    for i in range(0, x):
        data.loc[i,'id']= randint(1, 100)
        data.loc[i,'name']= fake.name()
        data.loc[i,'address']= fake.address()
        data.loc[i,'latitude']= str(fake.latitude())
        data.loc[i,'longitude']= str(fake.longitude())
    return data
   

print(input_data(10))

print('####################################')

from faker import Faker

fake = Faker()

for _ in range(500):
    print(fake.unique.first_name())

# Au bout de 1,000 itérations, on obtient l'erreur
# faker.exceptions.UniquenessException: Got duplicated values after 1,000 iterations

print('"""""""""""""""""""""""""""""""""""""""""""""')

from faker import Faker

fake = Faker()

for _ in range(5):
    print(fake.file_path())

# /career/several.css
# /near/author.gif
# /lawyer/red.mp4
# /prevent/operation.flac
# /site/home.csv

print('#################################')
from faker import Faker

fake = Faker()

for _ in range(5):
    print(fake.file_path(depth=5, category='video'))

# /cell/both/small/style/reflect/strong.avi
# /many/buy/it/popular/maybe/drive.mp4
# /teach/really/finish/southern/however/image.mov
# /include/first/senior/argue/next/mother.avi
# /pick/color/every/within/along/outside.mp4
