#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class Student:
    def __init__(self, name, age, HP=0, IQ=0):
        self.name = name
        self.age = age
        self.HP = HP
        self.IQ = IQ

    def eat(self):
        while self.HP < 100:
            print("eat something")
            self.HP += 10

    def study(self, is_again=False):
        if is_again:
            print("study again...")
            diff = random.randrange(1, 50)
            self.IQ += diff
            self.HP -= diff
        else:
            print("study hard")
            self.IQ += random.randrange(1, 100)

    def status(self):
        print("now status: name(" + self.name + ") age(" + str(self.age) + ") HP(" +
              str(self.HP) + ") IQ(" + str(self.IQ) + ")")


if __name__ == "__main__":
    student_one = Student("Hicup", 15)

    print("in the morning")

    student_one.eat()
    student_one.status()

    if student_one.IQ < 100:
        student_one.study()
    student_one.status()

    while student_one.IQ < 100:
        student_one.study(True)

    student_one.status()
