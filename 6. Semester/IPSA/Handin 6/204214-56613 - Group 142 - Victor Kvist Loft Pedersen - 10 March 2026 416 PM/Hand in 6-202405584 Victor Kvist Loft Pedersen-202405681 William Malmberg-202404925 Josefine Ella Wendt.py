'''
HANDIN 6 (ancestors)

This handin is done by (study ids and names of up to three students):

    202405681 William Malmberg
    202405584 Victor Kvist Loft Pedersen
    202404925 Josefine Ella Luci Sandy Dorothea Wendt
    

Reflection upon solution:
There were not a lot of problems with building up the class and inherit it to the annotated version.
There were some issues with the recursion part, where the part of calling itself was a bit tricky 
to realise. At the same time, we spend some time discussing how to make it look exactly like his
version of the solution with the else statement in the str and ancestors methods.
'''

#Defining class
class Person:
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died

    def __str__(self):
        died = self.died if self.died else ''

        return f'{self.name} {self.born}-{died}'
    
    def ancestors(self):        
        father_side = self.father.ancestors() if self.father else '-'
        mother_side = self.mother.ancestors() if self.mother else '-'
        
        return (self.__str__(), father_side, mother_side)
    

#Defining subclass:
class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note=None):
        self.note = note
        super().__init__(name, mother, father, born, died)

    def __str__(self):
        str1 = super().__str__()
        return str1 + f' [{self.note}]'
    
#Test:
louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')

def print_tree(tree, prefix=""):
    # Print the current node
    print(prefix + "--" + tree[0])

    # Loop through the children
    for child in tree[1:]:
        # Call the function recursively
        print_tree(child, prefix + "  |")


print_tree(margrethe_ii.ancestors())