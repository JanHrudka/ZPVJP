#!/usr/bin/env python3
class Staty():
    def __init__(self, jmeno, lidi, plochy = '?', hustota = -6666666):
        self.jmeno = jmeno
        self.lidi = lidi
        self.plochy = plochy
        self.hustota = hustota

    def __repr__(self):
        return '{}: {} {} {}'.format(self.jmeno, self.lidi, self.plochy, self.hustota)

def is_in(List,  x):
    for i in range(len(List)):
        if x == str(List[i]).split(': ')[0]:
            return True
    return False

def index_of(List, x):
    for i in range(len(List)):
        if x == str(List[i]).split(': ')[0]:
            return i

def hustota(List):
    for i in range(len(List)):
        if(str(List[i]).split(':')[1].split(' ')[0] != '?' and str(List[i]).split(':')[1].split(' ')[1] != '?'):
            List[i] = Staty(List[i].jmeno,List[i].lidi,List[i].plochy, float(List[i].lidi)/float(List[i].plochy))

staty = []

with open('staty_lidi.log', 'r', encoding='utf-8') as soubor:
    for line in soubor:
        jmeno, lidi = line.strip().split(': ')
        staty.append(Staty(jmeno, lidi))

with open('staty_plochy.log', 'r', encoding='utf-8') as soubor:
    for line in soubor:
        jmeno, plochy = line.strip().split(': ')
        if(is_in(staty,jmeno)):
            i = index_of(staty,jmeno)
            staty[i] = Staty(staty[i].jmeno, staty[i].lidi, plochy)
        else:
            staty.append(Staty(jmeno, '?',plochy))

hustota(staty)

def e_sort(emp):
    return emp.hustota

for stat in sorted(staty, key=e_sort, reverse=True):
    print(str(stat).replace("-6666666","?"))

with open('staty.log', 'w', encoding='utf-8') as soubor:
    for line in sorted(staty, key=e_sort, reverse=True):
        soubor.write(str(line) + '\n')