import json
import re

test_base = "[\'/*<![CDATA[*/var cartoFbi={\"latitude\":47.21516,\"longitude\":-1.65216,\"title\":\"GYMNASE DE LA CHANGETTERIE\",\"adress\":\"Rue Théophile Guillou\",\"cp\":\"44800\",\"city\":\"Saint-Herblain\",\"errors\":[]};var appId=\"gbzjKrZgFqqTRR0Qzhc9\";var appCode=\"mhhAJdMKSIo4L_CmaDRijg\";;/*]]>*/\']"



result = re.search("\{(.*?)\}", test_base)
print(result[0])

objet = json.loads(result[0])
print(objet['longitude'])

test_base ="javascript:openHere('533001012747')"

result = re.search("\'(.*?)\'", test_base)
print(result.group())