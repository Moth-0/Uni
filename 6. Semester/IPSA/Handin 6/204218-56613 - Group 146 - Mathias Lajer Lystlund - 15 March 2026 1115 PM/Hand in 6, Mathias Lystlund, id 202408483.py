'''
HANDIN 6 (Ancestors)

This handin is done by Mathias Lystlund, id: 202408483

Reflection upon solution:

I approached the problem by first creating a Person class that stores the basic
information shared by all individuals, such as name, parents, and birth and death years.
I then extended this structure with an AnnotatedPerson subclass so that I could add extra
information like titles or notes without changing the base class. Finally, I used a recursive
Ancestors() method to create a tuple, that can be used as an argument for the tree printing 
program of exercise 9.2.
    
'''

class Person():
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died


    def __str__(self):
        name = str(self.name)
        born = str(self.born)
        if self.died == None:
            died = ' '
        else:
            died = str(self.died)
        
        return name +' ' + born + '-' + died + ' '
    
    def Ancestors(self):
        
        father = self.father
        mother = self.mother
        anc = [] 
        anc.append(str(self.__str__()))
        
        if father != None:
            anc.append(((father.Ancestors())))
        if mother != None:
            anc.append(((mother.Ancestors())))
        return tuple(anc)
    

    

        

class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note=None):
        super().__init__(name, mother, father, born, died)
        self.note = note

    def __str__(self):
        base = super().__str__()
        if self.note is None:
            return base
        return base + ' [' + str(self.note) + ']'




louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')
print(louise_af_SN)
print(margrethe_ii.Ancestors())


def node(prefix, anc):
        if len(anc[0]) == 0:
            return None
        for i in anc:
            if isinstance(i, str):
                print(prefix + i)

            if isinstance(i, tuple):
                node('  |' + prefix, i)
                
            if i == None:
                 print(prefix)


print(node('--', margrethe_ii.Ancestors()))