"""
HANDIN 6 (Ancestors)

This handin is done by:
    202405797 Johannes Bøgh Fangel
    202407470 Valdemar Scheel

Reflection upon solution:
    Hard Parts: We had a little problem getting the recursive part to work, as we had first put it, 
    so that the ancestors method was used on a NoneType for those Person that didn't have fathers 
    or mothers notated. We fixed this by implementing the if-statements in the method. We also had 
    a problem redefining the __str__ method for the AnnotatedPerson class, we solved this as we had 
    made an error in the return of the ancestors method by returning self.name as the first index 
    in the tuple instead of just self. Another problem was in the print_tree function, where we tried
    concatenating strings and our Person-object. To not the same code twice, one could also use super()
    in the __str__ method in the AnnotatedPerson class.'
"""

class Person:
    def __init__(self,name=None,mother=None,father=None,born=None,died=None):
        self.name   = name
        self.father = father
        self.mother = mother
        self.born   = born
        self.died   = died
        if self.died == None:
            self.died = ''

    def __str__(self):
        return f"{self.name} {self.born}-{self.died}"


    def ancestors(self):
        if self == None:
            return '-'
        return (str(self),self.father.ancestors() if self.father else '-', self.mother.ancestors() if self.mother else '-')
                # if self.father else '-' checks if it an object. If it is, True, else it will be None and False. This stops recursion


class AnnotatedPerson(Person):
    def __init__(self,name=None,mother=None,father=None,born=None,died=None,note=None):
        super().__init__(name,mother,father,born,died)
        self.note = note

    def __str__(self):
        return f"{self.name} {self.born}-{self.died} [{self.note}]"
        

louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')
family_tree = margrethe_ii.ancestors()

def print_tree(tree, prefix=''):
        node, *children = tree
        print(prefix + '--', node)
        prefix = prefix + '  |'
        
        for child in children:
            print_tree(child, prefix)
   
print('Family Tree of Margrethe II.')
print_tree(family_tree)



# Alternative Solution

class Person():
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died
        
    def __str__(self):
        if self.died == None:
            return self.name + f' {self.born}-'
        else:
            return self.name + f' {self.born}-{self.died}'
    
    def ancestors(self):
        if self.father == None and self.father == None:
            return (self, '-', '-')
        
        elif self.mother == None:
            return (self, self.father.ancestors(), '-')
        
        elif self.father == None:
            return (self, '-', self.mother.ancestors())
        
        else:
            return (self, self.father.ancestors(), self.mother.ancestors())

class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note=None):
        super().__init__(name, mother, father, born, died)
        self.note = note
    
    def __str__(self):
        return super().__str__() + ' [' + self.note + ']'
    

louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Former Queen of Denmark')
prince_henrik = Person('Prince Henrik', None, None, 1934, 2018)
frederik_10 = AnnotatedPerson('Frederik 10.', prince_henrik, margrethe_ii, 1968, note='King of Denmark')

family_tree = frederik_10.ancestors()  