class Person:
    
    def __init__(self, names, age):
        if not isinstance(names, list) or len(names) < 1:
            raise ValueError('Names must be a non-empty list.')
        self.__names = names

        if age < 0:
            raise ValueError('Age cannot be negative.')
        self.__age = age
    
    def getFullName(self):
        return ' '.join(self.__names)
    
    def birthday(self):
        self.__age += 1

    def getAge(self):
        return self.__age 

    def getNameHarvardFormat(self):
        last_name = self.__names[-1]
        initials = ''.join([name[0].upper() for name in self.__names[:-1]])
        return f'{last_name}, {initials}'

    def __repr__(self):
        return self.getNameHarvardFormat()


class Book:
    
    def __init__(self, authors, title, publisher, publishYear, publishPlace):
        if not isinstance(authors, list) or len(authors) < 1:
            raise ValueError('Authors must be a non-empty list of Person objects.')
        for author in authors:
            if not isinstance(author, Person):
                raise ValueError('Authors must be a non-empty list of Person objects.')
        self.__authors = authors
        
        self.__title = title
        self.__publisher = publisher
        
        if publishYear < 0:
            raise ValueError('Publish year cannot be negative.')
        self.__publishYear = publishYear
        
        self.__publishPlace = publishPlace
        
    def displayAuthors(self):
        print(self.__authors)

    def getHarvardReference(self):
        authors_str = ', '.join([str(author) for author in self.__authors])
        return f'{authors_str} {self.__publishYear}, {self.__title}, {self.__publisher}, {self.__publishPlace}.'

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
