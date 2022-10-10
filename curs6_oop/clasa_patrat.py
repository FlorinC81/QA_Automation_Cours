
class Patrat:
   """
   Functia init  se numeste CONSTRUCTORUL  clasei, pentru ca de aici se construiesc obiecte
   """
   def __init__(self, latura, culoare = "alb"):
        self.lat = latura
        self.culoare = culoare
   def aria(self):
        return self.lat**2


patrat_alb = Patrat(12)
print(patrat_alb.lat)
print(patrat_alb.culoare)
print()
print(patrat_alb.aria())
print()
patrat_rosu = Patrat(5, "rosu")
print(patrat_rosu.lat)
print(patrat_rosu.culoare)