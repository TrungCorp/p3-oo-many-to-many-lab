class Author:
    def __init__(self,name):
        self.name = name
        self.contract_list = []
        self.book_list = []
        self.royalty_total = 0
    def contracts(self):
        return self.contract_list
    def books(self):
        return self.book_list
    def sign_contract(self,book,date, royalties):
        new_obj = Contract(self,book,date,royalties)
        return new_obj
    def total_royalties(self):
        return self.royalty_total



class Book:
    def __init__(self,title):
        self.title = title
        self.book_list = []
        self.author_list = []
    def contracts(self):
        return self.book_list
    def authors(self):
        return self.author_list


class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    @classmethod
    def contracts_by_date(cls,date=None):
        
        new_obj = [contract for contract in cls.all if contract.date == date]
        return new_obj
        
        
    
    
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if(isinstance(author,Author)):
            self._author = author
            author.contract_list.append(self)
            
        else:
            raise Exception("Error, argument is not of type Author class")
        
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,date):
        if(isinstance(date,str)):
            self._date = date
        else:
            raise Exception("Error, object is not of type string")
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,book):
        if(isinstance(book,Book)):
            self._book = book
            self.author.book_list.append(book)
            book.book_list.append(self)
            book.author_list.append(self.author)
            
        else:
            raise Exception("Error, object is not of type Book")
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self,royalties):
        if(isinstance(royalties,int)):
            self._royalties = royalties
            self.author.royalty_total += royalties
        else:
            raise Exception("Error, object is not of type integer")