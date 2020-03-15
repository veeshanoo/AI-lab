import time
import random

class Elev:
    adder = 1

    @classmethod
    def increment(cls):
        cls.adder += 1
        return cls


    def __init__(self, name=None, sanatate=90, inteligenta=20, oboseala=0, buna_dispozitie=100):
        # atribute de instanta
        self.name = "Necunoscut_" + str(Elev.increment()) if name is None else name
        self.sanatate = sanatate
        self.inteligenta = inteligenta
        self.oboseala = oboseala
        self.buna_dispozitie = buna_dispozitie
        self.current_activity = ""
        self.current_hour = 9
        self.is_final = 0 # 0 1 sau 2
        self.contribution = 1.0
        self.activities = dict()
        self.durata = 0

    def print_activities(self):
        print(self.name + ": ")
        for key, value in self.activities.items():
            print(key, value)


    def is_occupied(self):
        return self.current_activity != ""

    def asd(self):
        if self.is_final == 0:
            return "exista"
        if self.is_final == 1:
            return "mort"
        if self.is_final == 2:
            return "absolvit"


    def desfasoara_activitate(self, activitate):
        self.current_activity = activitate
        self.durata = activitate.durata
        self.activities[self.current_activity.name] = 0

    def trece_ora(self):
        if self.current_activity == "":
            return False

        self.current_hour += 1

        self.activities[self.current_activity.name] += 1

        self.sanatate += self.current_activity.factor_sanatate * self.contribution / self.current_activity.durata
        self.inteligenta += self.current_activity.factor_inteligenta * self.contribution / self.current_activity.durata
        self.buna_dispozitie += self.current_activity.factor_dispozitie * self.contribution / self.current_activity.durata
        self.oboseala += self.current_activity.factor_oboseala * self.contribution / self.current_activity.durata

        self.sanatate = max(0, self.sanatate)
        self.sanatate = min(100, self.sanatate)
        self.inteligenta = max(0, self.inteligenta)
        self.inteligenta = min(100, self.inteligenta)
        self.buna_dispozitie = max(0, self.buna_dispozitie)
        self.buna_dispozitie = min(100, self.buna_dispozitie)
        self.oboseala = max(0, self.oboseala)
        self.oboseala = min(100, self.oboseala)

        if self.current_activity.name != "dormit":
            self.sanatate -= 1

        self.durata -= 1
        if self.durata == 0:
            self.current_activity = ""


        if self.sanatate == 0 or self.buna_dispozitie == 0:
            self.is_final = 1
            return True

        if self.inteligenta == 100:
            self.is_final = 2
            print(self.name + " a terminat scoala")
            return True

        if self.oboseala == 100:
            self.contribution = 0.5
        else:
            self.contribution = 1


    def testeaza_final(self):
        return self.is_final != 0


    def afiseaza_raport(self):
        pass


    def __repr__(self):
        return "nume={} sanatate={} inteligenta={} oboseala={} buna_dispozitie={}".format(self.name, self.sanatate, self.inteligenta, self.oboseala, self.buna_dispozitie)

class Activity:

    def __init__(self, name, factor_sanatate, factor_inteligenta, factor_oboseala, factor_dispozitie, durata):
        self.durata = float(durata)
        self.factor_dispozitie = float(factor_dispozitie)
        self.factor_oboseala = float(factor_oboseala)
        self.factor_inteligenta = float(factor_inteligenta)
        self.factor_sanatate = float(factor_sanatate)
        self.name = name



activities = []
students = []
current_time = 9


def simulare():
    global current_time
    global students
    global activities

    with open("tst.in") as fin:
        for line in fin.readlines():
            line = line[:-1]
            activities.append(Activity(*line.split(" ")))

    students.append(Elev("Jenea"))
    students.append(Elev("Daras"))
    students.append(Elev("Pi"))

    while True:
        pl = input("care ore afisam?\n")
        if pl == "gata":
            break

        nr = int(pl)
        pause_time = current_time + nr
        while current_time < pause_time:
            for student in students:
                if not student.testeaza_final():
                    print(student)
                    print(student.asd())
                    # continue


                if not student.is_occupied():
                    student.desfasoara_activitate(random.choice(activities))

                student.trece_ora()
                print(student)
                student.print_activities()
                print()
                print("  " + student.asd())
            current_time += 1
            time.sleep(1)


simulare()
