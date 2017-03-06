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


class School:
    def __init__(self):
        self.students = []

    def enter(self, student):
        self.students.append(student)

    def morning(self):
        for student in self.students:
            self.eat_and_study(student)

    def eat_and_study(self, student):
        print("in the morning")

        student.eat()
        student.status()

        if student.IQ < 100:
            student.study()
        student.status()

        while student.IQ < 100:
            student.study(True)

        student.status()


if __name__ == "__main__":
    school = School()
    school.enter(Student("Hicup", 15))
    school.enter(Student("Astrid", 13))
    school.enter(Student("Toothless", 5))
    school.morning()
