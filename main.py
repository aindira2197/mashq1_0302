# string
# 1
matn = "salom dunyo"
matn = matn.title()
print(matn)

# 2
import re

matn = "Bu (birinchi) va (ikkinchi) qavs"
natija = re.findall(r'\(([^)]+)\)', matn)

print(natija)

# 3
gmail = "1jnskn@gamil.domen"
if gmail in "@" and gmail in "domen":
    print(True)
else:
    print(False)

# 4
matn = "salom dunyo"
noyob = ""

for i in matn:
    if matn.count(i) == 1:
        noyob += i

print(matn)
print(noyob)

# 5
matn = "Aziza"
matn = matn.lower()

if matn == matn[::-1]:
    print("palidrom")

else:
    print("palidrom emas")

# 6
matn = "Bu matnda eng kop uchraydigan soz shu matnda"

sozlar = matn.lower().split()
eng_kop = max(sozlar, key=sozlar.count)

print(eng_kop, sozlar.count(eng_kop))

# 7
matn = "1234567890"
yangi = ""

for i in range(len(matn)):
    yangi += matn[i]
    if (i + 1) % 3 == 0 and i != len(matn) - 1:
        yangi += "-"

print(yangi)
