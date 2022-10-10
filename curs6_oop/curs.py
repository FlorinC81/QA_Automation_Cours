from prima_mea_clasa import Person

class CursProgramare:

    def __init__(self,compania, nume, durata, data_inceput, nr_locuri = 10):
        self.compania = compania
        self.nume = nume
        self.durata = durata
        self.data_inceput = data_inceput
        self. nr_locuri_disponibile = nr_locuri
        self.studenti = []
    def inscriere_student(self,student):
        # Aici am putea de exemplu daca a trecut data de inceput si daca nu sa inscriem studentul
        if self.nr_locuri_disponibile > 0:
            self.studenti.append(student)
            self.nr_locuri_disponibile-=1
            print(f"Studentul {self.nume} a fost inscris cu succes")
        else:
            print("ne pare rau, nu mai sunt locuri disponibile")

    def descriere_curs(self):
        print(f"{self.nume} [{self.compania}] - {self.durata} zile")
        print("-"*88)
        for student in self.studenti:
            print(f"{student.nume} {student.prenume} ({student.varsta})")
        if not self.studenti:
            print("Nu sunt inca stidenti inscrisi")
        print()

curs_python = CursProgramare("IT Factory", "Introducere in Python", 120, "2023-01-01")
curs_python.descriere_curs()

mihai = Person("Suciu","Mihai", 22, 1.70)
florian = Person("Chetves", "Florian", 28, 1.85)

curs_python.inscriere_student(mihai)
curs_python.inscriere_student(florian)

print()
curs_python.descriere_curs()

curs_python.inscriere_student(
    Person("Briceag", "Marcela", 33, 1.64)
)
curs_python.inscriere_student(
    Person("Lazarica", "Petrut", 48, 1.80)
)

curs_python.descriere_curs()
