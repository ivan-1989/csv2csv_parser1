import csv
from transliterate import translit, get_available_language_codes


reader = csv.DictReader(open('/home/ivan/Downloads/1586555246.hosts.csv', 'rb'))
dict = []
dict1 = []
for i in reader:
    dict.append(i)

print (type(dict))

#print (dict)

for i in dict:
    i['status'] = "Active"
    i['IP'] = i['IP']+'/'+i['VM']
    del i['site']
    del i['type']
    del i['AI']
    del i['comm']
    del i['net']
    del i['network category']
    del i['type update']
    del i['MAC']
    del i['e-mail']
    del i['VM']
    i['name'] = i['name'].replace('(', '')
    i['name'] = i['name'].replace(')', '')
    i['name'] = i['name'].replace('+', '')
    i['name'] = i['name'].replace('`', '')
    i['name'] = i['name'].replace("'", '')
    trans = i['name']
    trans = trans.decode('utf-8')
    print(i['name'])
    try:
        i['name'] = str(translit(trans, reversed=True))
        dict1.append(i)
    except:
        dict1.append(i)


#print (type(dict1))

keys = dict1[0].keys()
with open('/home/ivan/test1212.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dict1)