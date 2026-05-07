'''
HANDIN 6 (ancestors)

This handin is done by (study ids and names of up to three students):

    202406267 Andreas Wind

Reflection upon solution:

    Jeg syntes at det var en lidt mærkelig måde at jeg tjekker om mother
    eller father er None. Man kunne måske have gjort det på en nemmere
    måde, men det virker sådan som jeg har gjort :)
    Jeg kunne ikke helt få den der print_tree funktion til at printe det
    helt rigtige. Jeg fik den ikke til at printe None-ancestors som 
    "|---". Men tænkte at siden det var uden for opgavens omfang, så 
    behøvede jeg ikke at bøvle med det.
'''


class Person:

    def __init__(self, name = None, mother = None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died
    
    def __str__(self):
        if self.died != None:
            return str(str(self.name) + " " + str(self.born) + "-" + str(self.died))
        else:
            return str(str(self.name) + " " + str(self.born) + "-")
    
    def ancestors(self):
        if (self.father != None) and (self.mother != None):
            return (self.__str__()  , (self.father).ancestors(), (self.mother).ancestors())
        elif (self.mother != None):
            return (self.__str__(), "-", (self.mother).ancestors())
        elif (self.father != None):
            return (self.__str__(), (self.father).ancestors(), "-")
        else:
            return (self.__str__(), "-", "-")

class AnnotatedPerson(Person):

    def __init__(self, name = None, mother = None, father=None, born=None, died=None, note=None):
        self.note = note
        super().__init__(name, mother, father, born, died)

    def __str__(self):
        return f"{super().__str__()} [{self.note}]"
    
    def ancestors(self):
        return super().ancestors()
    

# fra ex9.2
def print_tree(tree, prefix = ""):

    for i in range(len(tree)):

        if type(tree[i]) == str and (tree[i] !="-"): 
            print(prefix, "--",tree[i])

        elif type(tree[i]) == tuple:
            print_tree(tree[i], prefix + "  |") 

    
louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')

print_tree(margrethe_ii.ancestors())

