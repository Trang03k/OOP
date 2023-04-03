#task 1
class Person:
    
    def __init__(self,names,age):
        if not isinstance(names,list) :
            raise ValueError('Names can not be empty')
        self.__names = names

        if age < 0:
            raise ValueError("Age is not negative number")
        self.__age = age
    
    def getFullName(self):
        return ' '.join(self.__names)
    
    def birthday(self):
        self.__age += 1
    

    def getAge(self):
        return self.__age 
    
    def getNameHarvardFormat(self):
        last_name = self.__names[-1]
        initials =''.join([name[0].upper() for name in self.__names[:-1]])
        return f'{last_name}, {initials}'
            
   
    def __repr__(self):
        return self.getNameHarvardFormat()
programmer = Person(['Augusta', 'Ada', 'King'], 36)
print(programmer.getFullName(), 'is', programmer.getAge())
programmer.birthday()
print(programmer.getFullName(), 'is', programmer.getAge())
print(programmer.getNameHarvardFormat())
print(programmer)

#Task 2

class Book:
    def __init__(self, authors,title,publisher,publishYear,publishPlace):
    
        if not isinstance(authors,list):
            raise ValueError('authors can not be empty')
        for author in authors:
            if not isinstance(author,Person):
                raise ValueError('Error')
        self.__authors = authors
        
        self.__title = title
        self.__publisher =publisher
        
        if publishYear < 0:
            raise ValueError('Year can not be negative number')
        self.__publishYear = publishYear
        
        self.__publishPlace = publishPlace

    def displayAuthors(self):
        print(self.__authors)
    
    def getHarvardReference(self):
        authors_str = ','.join([str(author) for author in self.__authors])
        return f'{authors_str} {self.__publishYear},{self.__title},{self.__publisher},{self.__publishPlace}'
    
    def __str__(self):
        return self.getHarvardReference()
    
   

programmer = Person(['Augusta', 'Ada', 'King'], 36)
engineer = Person(['Charles', 'Babbage'], 50)
actualAuthor = Person(['Sydney','Padua'], 30)
book = Book([programmer, engineer, actualAuthor],
 'The Thrilling Adventures of Lovelace and Babbage',
 'Penguin Books', 2015, 'Westminster')
print(book)
book.displayAuthors()
