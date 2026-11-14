class Library:
  library_name = "City Library"
  total_books = 0

  def __init__(self, book_title, author, copies):
    self.book_title = book_title
    self.author = author
    self.copies = copies
    Library.total_books += copies 
  
  #Instance Method --->
  def borrow_books(self):
    if self.copies > 0:
      self.copies -= 1
      Library.total_books -= 1
      print(f"You borrowed '{self.title}',Copies left: {self.copies}")
    else:
      print(f"{self.title} is not available")
    
  def return_books(self):
    self.copies += 1
    Library.total_books += 1
    print(f"You returned{self.title}, Copies left: {self.copies}")

  def display_info(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")
    print(f"Copies: {self.copies}")

  #Class Method --->
  @classmethod
  def get_total_books(cls):
    return cls.total_books

  #Static Method  --->
  @staticmethod
  def library_policy():
    print("Please Maintain Silence in the Class")
  

