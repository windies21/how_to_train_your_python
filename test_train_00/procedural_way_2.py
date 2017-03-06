#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


if __name__ == "__main__":
    name = "Hicup"
    age = 15
    HP = 0
    IQ = 0

    print("in the morning")

    while HP < 100:
        print("eat something")
        HP += 10

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    if IQ < 100:
        print("study hard")
        IQ += random.randrange(1, 100)

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    while IQ < 100:
        print("study again...")
        diff = random.randrange(1, 50)
        IQ += diff
        HP -= diff

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    name = "Astrid"
    age = 13
    HP = 0
    IQ = 0

    print("in the morning")

    while HP < 100:
        print("eat something")
        HP += 10

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    if IQ < 100:
        print("study hard")
        IQ += random.randrange(1, 100)

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    while IQ < 100:
        print("study again...")
        diff = random.randrange(1, 50)
        IQ += diff
        HP -= diff

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    name = "Toothless"
    age = 5
    HP = 0
    IQ = 0

    print("in the morning")

    while HP < 100:
        print("eat something")
        HP += 10

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    if IQ < 100:
        print("study hard")
        IQ += random.randrange(1, 100)

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")

    while IQ < 100:
        print("study again...")
        diff = random.randrange(1, 50)
        IQ += diff
        HP -= diff

    print("now status: name(" + name + ") age(" + str(age) + ") HP(" + str(HP) + ") IQ(" + str(IQ) + ")")
