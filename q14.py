#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q14
"""

COUNTRIES = [
    "Brazil",
    "Cameroon",
    "Chile",
    "Greece",
    "Uruguay",
    "Italy",
    "France",
    "Bosnia and Heregovina",
    "Gernany",
    "USA",
    "Russia",
    "Croatia",
    "Spain",
    "Australia",
    "Cote d'lvoire",
    "Costa Rica",
    "Switzerland",
    "Honduras",
    "Iran",
    "Portugal",
    "Belgium",
    "Korea Republic",
    "Mexico",
    "Netherlands",
    "Colombia",
    "Japan",
    "England",
    "Ecuador",
    "Agentina",
    "Nigeria",
    "Ghana",
    "Algeria",
    ]

MAX_CNT = 0
MAX_SHIRITORI = []


def shiritori(depth, key, chain):
    """
    しりとり
    """
    global MAX_CNT
    global MAX_SHIRITORI
    total_cnt = 0

    # キーワードで始まる国を探す
    next_countries = []
    for i in COUNTRIES:
        if i[0].upper() == key[0].upper():
            next_countries += [i]

    if not next_countries:
        return 0

    for i in next_countries:
        if i not in chain:
            chain.append(i)

            total_cnt = shiritori(depth + 1, i[-1].upper(), chain)
            if total_cnt > MAX_CNT:
                MAX_CNT = total_cnt
                MAX_SHIRITORI = chain[:]

            chain.pop()

    return depth


for country in COUNTRIES:
    shiritori(0, country, [])

print(MAX_CNT, " : ", MAX_SHIRITORI)
