from pprint import pprint
import re

with open('index.html', 'r', encoding='utf8') as file:
    content = file.read()

# Exo2 regex to get all links
# my_regex = "href=\"(.+?)\""

# Exo3 regex to get only article links
my_regex = "href=\"(.+/article/.+?)\""


res = re.findall(my_regex, content)

# Exo4 Pour chaque lien, extrayez la date et affichez-la au format « yyyy-mm-dd ».
# for link in res:
#     date_regex = "(\d{4})/(\d{2})/(\d{2})"
#     date = re.search(date_regex, link)
#     if date is not None:
#         # res[res.index(link)] = date.group(1) + "-" + date.group(2) + "-" + date.group(3)
#         res[res.index(link)] = date[1] + "-" + date[2] + "-" + date[3]

# Exo5 Instanciez un dictionnaire, qui contiendra les dates et le nombre d’articles publiés ce jour.
# Pour chaque date, incrémentez le compteur
dates = {}
for link in res:
    date_regex = "(\d{4})/(\d{2})/(\d{2})"
    date = re.search(date_regex,link)
    if date is not None:
        date = date[1] + "-" + date[2] + "-" + date[3]
        if date in dates:
            dates[date] += 1
        else:
            dates[date] = 1

# Exo6 Ecrivez ces statistiques dans un fichier.
with open('stats.txt', 'w', encoding='utf8') as file:
    file.write(str(dates))



pprint(dates)