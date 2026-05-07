"""
HANDIN 6 

This handin is done by:

202407098 Johanne Stubkjær
202408622 Magnus Overgaard
202405571 Jonas Ullgren

Reflection upon solution:

This was a nice and very direct and intuitive assignment. cool to match classes with a recursive tactic. we also learned how
the __ __ functions work. Used pythontutor a bit to see where things got messed up. tried af lot of complicated and intricate
solutions - none worked. and then it turned out we could just make two more functions (recursive_mothers and recursive_fathers)
instead of everything being constructed inside ancestors(). pls ignore that the birth years dont match at all lol.
"""

class Person():
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died
    
    def __str__(self):
        if self.died == None:
            return f'{self.name}: {self.born} - '
        return f'{self.name}: {self.born} - {self.died}'
    
    def recursive_mothers(self, mothers):
        
        if mothers == None:
            mothers = []

        if self.mother == None:
            return mothers

        mothers.append(str(self.mother))
        return self.mother.recursive_mothers(mothers)
        
    def recursive_fathers(self, fathers):

        if fathers == None:
            fathers = []

        if self.father == None:
            return fathers
        
        fathers.append(str(self.father))
        return self.father.recursive_fathers(fathers)

    def ancestors(self, mothers=None, fathers=None):

        mothers = self.recursive_mothers(mothers)
        fathers = self.recursive_fathers(fathers)

        return (self.__str__(), mothers, fathers)
    
class AnnotatedPerson(Person):
    def __init__(self, name=None, note= None, mother=None, father=None, born=None, died=None):
        super().__init__(name, mother, father, born, died)
        self.note = note
    
    def __str__(self):
        if self.died == None:
            return f'{self.name} [{self.note}]: {self.born} - '
        return f'{self.name} [{self.note}] {self.born} - {self.died}'


#oldeforældre
Anders = Person('Anders', None, None, 1900, 1960)
AneMagdalene = Person('Ane Magdalene', None, None, 1900, 1960)
Hans =   Person('Hans', None, None, 1900, 1960)
Lone =   Person('Lone', None, None, 1901, 1960)

#bedsteforældre
Alys = Person('Alys', None, None, 1905, 2015)
Otto = Person('Otto', Lone, Hans, 1901, 2010)
Martha = AnnotatedPerson('Martha', 'Coolest Grandma', AneMagdalene, Anders, 1901, 1950)
Laurits = Person('Laurits', None, None, 1901, 1980)

#forældre
Rita = Person('Rita', Martha, Laurits, 1967)
Lasse = Person('Lasse', Alys, Otto, 1958)

#mig
Johanne = Person('Johanne', Rita, Lasse, 2002 )

#Martha.__str__()
def print_tree(tree, pre=""):
    print(pre + "| -- " + tree[0]) 
    for child in tuple(tree[1:]):
        newpre = "|   " + pre 
        print_tree(child, newpre)

print(Johanne.ancestors())