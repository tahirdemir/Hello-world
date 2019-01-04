#json parse etmek icin eklenmesi gereken kutuphane
import json
#ekrana tum veriyi patlatmak icin gerekli
from pprint import pprint
#url den veri cekebilmek icin


#okunacak dosya
with open('tahir.json') as data_file:
    data = json.load(data_file)

#hepsini yazdır
print ("Hepsini yazdirma:")
print(data["ad"])

print(data)
