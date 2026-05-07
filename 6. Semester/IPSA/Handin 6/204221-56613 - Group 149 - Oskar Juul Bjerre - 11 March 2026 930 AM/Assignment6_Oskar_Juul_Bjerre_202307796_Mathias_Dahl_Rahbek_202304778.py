'''
HANDIN 6 (Ancestors)

202307796 Oskar Juul Bjerre
202304778 Mathias Dahl Rahbek

Reflection upon solution:
Throughout this solution, we got quite frustrated with handling the None-types
in our ancestors function. Our solution still bothers us, since we are not 
utilising class hierarchy optimally, since we are specifying our paramater 
twice, which defeats the purpose of the subclass. We do not know how to 
change this however, a suggestion would be nice :). 
With all this being said, we did not find this assignment very difficult. 
'''

class Person:   # Person class with methods
    def __init__(self, name, mother, father, born, died=' '):  
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died
    def __str__(self):
        return self.name + ' ' + f'{self.born}-{self.died}'
    def ancestors(self):    # Method to acces and return ancestors
        mother = self.mother
        father = self.father
        recursive_father_ancestors = '-' 
        recursive_mother_ancestors = '-'

        if mother !=None:   # Check for end of line
            recursive_mother_ancestors = mother.ancestors()
        if father !=None:
            recursive_father_ancestors = father.ancestors()
        name_string = self.__str__()
        # For pretty printing
        if (isinstance(recursive_mother_ancestors, str) or 
            isinstance(recursive_father_ancestors, str)):
            return (name_string, (recursive_father_ancestors, 
                recursive_mother_ancestors))
        return (name_string, recursive_father_ancestors, 
                recursive_mother_ancestors)
    
    
class AnnotatedPerson(Person):  # Subclass of Person
    def __init__(self, name, mother, father, born, died=' ', note=None):
        self.note = note
        super().__init__(name, mother, father, born, died)
    def __str__(self):
        return super().__str__() + f' [{self.note}]'

def recursive_tuple(tree, indent=-1):   # Print_tree func from ex. 9.2
    if isinstance(tree,str): 
        print(' |'* indent+ '--' +f'{tree}') 
        return []
    for node in tree: 
        recursive_tuple(node, indent=indent+1)


louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851,
                               1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000,
                               'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940,
                                note='Queen of Denmark')

recursive_tuple(margrethe_ii.ancestors())