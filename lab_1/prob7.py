import re


s = "Candva, demult, acum 1000 de ani traia o printesa intr-un castel. Si printesa intr-o zi auzi cum aparuse pe meleagurile sale un cufar fermecat din care iesea grai omenesc. Printesa curioasa strabatu 7 ulite si 7 piete; ajunse la cufar si vazu ca toti stateau la 100 metri distanta de el si se mirau. Din cufar intr-adevar se auzeau vorbe nedeslusite. Printesa curajoasa se duse sa-i vorbeasca. Il intreba cine e si ce dorinte are. Raspunsul fu: \"Sunt Ion am cazut in cufar si m-am ferecat din gresala. As dori sa ies.\". Printesa deschise cufarul si-l elibera pe Ion. \"Multumesc\" spuse Ion. Si astfel, povestea cufarului fermecat a fost deslusita."

#1
print(len(s))


#2
def not_isalnum(a):
    return [x for x in a if x.isalnum() is False]


v = not_isalnum(s)
v = {x for x in v}
print(v)


#3
splitter = ""
for x in v:
    splitter += "\\" + x + "|"
g = re.split(splitter[:-1], s)
print([x for x in g if x is not ""])

#4
print([cuv for cuv in g if cuv.endswith("ul")])

#5
print(re.findall('\w*-\w*', s))



