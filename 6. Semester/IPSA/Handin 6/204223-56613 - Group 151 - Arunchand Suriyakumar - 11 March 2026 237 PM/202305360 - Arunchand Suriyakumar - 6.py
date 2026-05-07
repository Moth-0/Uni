#%%
#Exercise 12.2 - handin 6 (ancestors)

'''
HANDIN 6 (Handin 6 - ancestors)

This handin is done by 
    202305360: Arunchand Suriyakumar

Reflection upon solution:
    When creating the class Person, we make a init-function that has keywords arguments
    set to None if nothing is provided. The string function is made such that it doesnt
    show anything if the person is still alive

    The ancestor function is made by recursion. Here it only matters if the object has 
    a father, which is a person, and a mother, which is a person. If not, we replace by
    '-'- If they are persons, we recursively go through their family tree

    The subclass is made with an addition to the init-function, hence, we used "super"

    When running the case with the royal family, we get the correct result.

'''

#%%
class Person():
    def __init__(self, name=None, mother=None, father=None, born=None, died=None):
        self.name = name
        self.mother = mother
        self.father = father
        self.born = born
        self.died = died
    
    def __str__(self):
        if self.died == None:
            self.died = ''
        return f'{self.name} ({self.born}-{self.died})'
    
    def ancestors(self):
        if isinstance(self.father, Person):
            f = self.father.ancestors()
        else: #Base case
            f = '-'
        if isinstance(self.mother, Person):
            m = self.mother.ancestors()
        else: #Base case
            m = '-'

        return (self.__str__(), f, m)

class AnnotatedPerson(Person):
    def __init__(self, name=None, mother=None, father=None, born=None, died=None, note = None):
        self.note = note
        super().__init__(name, mother, father, born, died) 
    
    def __str__(self):
        return super().__str__() + ' ' + self.note
    


#%%
louise_af_HK = Person('Louise of Hessen-Kassel', None, None, 1817, 1898)
christian_9  = Person('Christian 9.', None, None, 1818, 1906)
louise_af_SN = AnnotatedPerson('Louise of Sweden-Norway', None, None, 1851, 1926, 'born Princess of Sweden and Norway')
frederik_8   = Person('Frederik 8.', louise_af_HK, christian_9, 1870, 1947)
christian_10 = Person('Christian 10.', louise_af_SN, frederik_8, 1870, 1947)
ingrid       = AnnotatedPerson('Ingrid of Sweden', None, None, 1910, 2000, 'Queen of Denmark 1947-1970')
frederik_9   = Person('Fredrik 9.', None, christian_10, 1899, 1972)
margrethe_ii  = AnnotatedPerson('Margrethe II', ingrid, frederik_9, 1940, note='Queen of Denmark')


margrethe_ii.ancestors()



