#!/usr/bin/env python3
class Prvky():
    def __init__(self, značka, hmotnost, pořadí, en, els, valency):
        self.značka = značka
        self.hmotnost = hmotnost
        self.pořadí = pořadí
        self.en = en
        self.els = els
        self.valency = valency

    def __repr__(self):
        return '({},{},{},{},{},{})'.format(self.značka, self.hmotnost, self.pořadí, self.en, self.els, self.valency)

prvky = []

with open('prvky.txt', 'r', encoding='utf-8') as soubor:
    for řádka in soubor:
        značka, hmotnost, pořadí, en, els, valency = řádka.strip().split(';')
        prvky.append(Prvky(značka.strip('"'), float(hmotnost), int(pořadí.split(':')[-1]),float(en.split(':')[-1]),int(els.split(':')[-1]),valency.split(':')[-1].strip()))

def e_sort(emp):
    return emp.en

for prvek in sorted(prvky, key=e_sort):
    print(prvek)