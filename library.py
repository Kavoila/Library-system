class Library:
    def __init__(self,isbn,title,author,publisher,pages,price,copies):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher
        self._pages = pages
        self._price = price
        self._copies  = copies
    def in_stock(self):
        if self._copies >0:
            return ('True')
        else:
            return('False')
        
  
    def display (self):
        print (  self._isbn,
        self._title,
        self._price ,
        self._copies )
   
    def sell(self, number):
        self.number = number
        if self._copies > 0 :
            new_copies = self._copies - self.number 
        else :
             return (' Oops!The book requested is out of stock')
    @property    
    def get_sells(self):
        return self._copies
    @get_sells.setter
    def get_sells (self,val):
        self._copies = val
    @property
    def price(self):
        return self._price
    @price.setter
    def price (self,new_price):
        if 100<= new_price<=2000:
            self._price = new_price
        else:
            raise ValueError('price must range between a 100 and 2,000 shillings')
   
         
if __name__  == '__main__':      
    book1 = Library('957-4-36-547417-1','Quantum physics','Stephen','Pan', 350, 200, 10)
    book2 = Library( '652-6-86-748413-3',' Dynamic of Cartography', 'Jack','Copy press',400,220,20)
    book3 = Library('957-7-39-347216-2', 'Modern survey','John','ISK',500,300,5)
    book4 = Library('957-7-39-347216-2','IT in Context','Jack','Tylor',400,200,100)

book1.display()
book2.display()
book3.display()
book4.display()


Library_books = [book1,book2,book3,book4]
for book in Library_books:
   book.display()  
    



        
