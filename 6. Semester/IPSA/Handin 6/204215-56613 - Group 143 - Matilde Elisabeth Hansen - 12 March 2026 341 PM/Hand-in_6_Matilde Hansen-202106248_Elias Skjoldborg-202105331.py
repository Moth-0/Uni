
'''
HANDIN 6 (ancestors)

This handin is done by:

    202106248 Matilde E. Hansen
    202105331 Elias R. Skjoldborg

Reflection upon solution: 

We create a class person, that returns a persons name and their birth year and year of death. The ancestor method of this class should be printing
that persons ancestors, and their ancestors and so on. We therefore want to call the ancestor function within itself, to produce tuples of ancestors recursively.
This recursive function had to call on both mothers and fathers and their respective parents. The recursive function does this only if the mother or the father of
a person actually exists. This is in order to end the recursive loop, such that it stops calling on parents that aren't defined. When making the subclass 
AnnotatedPerson we noticed that the parent class Person was overwriting annotated persons to just persons, such that the notes of those were removed. We solved
this by defining a __str__ function in both parent class and subclass, such that the AnnotatedPerson is called with the note. We finally copied the code from task
9.2 to print the ancestor tuples as trees.
'''
class Person():

    def __init__(self,name = None, mother = None, father = None, born = '', died = ''): # mother and father are objects that are created from a class that has
                                                                                        # the ancestor method (aka the Person class and it's subclass AnnotatedPerson)
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died

    def __str__(self):
        return f'{self.name} ({self.born} - {self.died})'
    
    def ancestors(self):
        mother_ancestor = '-'
        father_ancestor = '-'

        if self.mother != None:
            mother_ancestor = self.mother.ancestors()                           # Here we run a recursive function over ancestors as long as the person has a mother

        if self.father != None:
            father_ancestor = self.father.ancestors()                           # or a father
        
        return(self.__str__(), father_ancestor, mother_ancestor)                # Here self.__str__() calls on either a Person or an AnnotatedPerson, such that the
                                                                                # note is added, because __str__ is defined in both classes

class AnnotatedPerson(Person):

    def __init__(self, name = None, mother = None, father = None, born = '', died = '', note = ''):
        super().__init__(name, mother, father, born, died)
        self.note = note

    def __str__(self):
        return f'{self.name} ({self.born} - {self.died})' + f'[{self.note}]'

def print_tree(tree, prefix ="--", indent=""):
    label = tree[0]
    print(indent + prefix + label)
    for child in tree[1:]:
        print_tree(child, prefix ="|--", indent = indent + "|  ")

louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note= 'Queen of Denmark')

print_tree(margrethe_ii.ancestors())
