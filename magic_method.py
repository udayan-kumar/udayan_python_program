# MAGIC METHOD --> DUNDER METHOD (DOUBLE UNDERSCORE) __INIT__ , __STR__ , __EQ__ ..... THEY ARE AUTOMETICALLY CALLED BY MANY OF PYTHON'S BUILT-IN OPERATION .... THEY ALLOW DEVELOPERS TO DEFINE OR CUSTOMIZE THE BEHAVIOUR OF OBKECTS

class Book:

    def __init__(self , title , author , num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author} of {self.num_pages} pages"
    
    def __eq__(self , other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self , other):
        return self.num_pages < other.num_pages
    
    def __gt__(self , other):
        return self.num_pages > other.num_pages
    
    def __add__(self , other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self , key):
        if key == "title":
            return self.title
        if key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key {key} is not found"
    
# book1 = Book("the hobbit" , "j.r.r. tolkien" , 310)
# book2 = Book("harry potter and the philospher's stone" , "j.k. rowling" , 223)
# book3 = Book("the lion, the witch and the wardrobe" , "c.s. lewis" , 172)


book1 = Book("the hobbit" , "j.r.r. tolkien" , 310)
book2 = Book("the hobbit" , "j.r.r. tolkien" , 223)
book3 = Book("the lion, the witch and the wardrobe" , "c.s. lewis" , 172)

# print(book1)
# print(book2)
# print(book3)

print(book1 == book2)
print(book1 > book2)
print(book1 < book2)
print(book1 + book2)
print("lion" in book3)
print("udayan" in book3)
print(book2['title'])
print(book2['author'])
print(book2['num_pages'])
print(book2['udayan'])