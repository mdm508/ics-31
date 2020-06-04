from collections import namedtuple
from graphics import *

Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]


'''
(1) Implement the function abbreviate that takes the name of a month as input and returns its three-letter abbreviation. In fact, it should take any string as input and return its first three characters, as these examples illustrate:
'''
def abbreviate(month:str) -> str:
  '''
  returns first three characters of month
  '''
  return month[0:3]

assert abbreviate('January') == 'Jan'
assert abbreviate('abril') == 'abr'


def calculate_shipping(weight:float) -> float:
  '''
  given the weight of a package calculate
  how much it costs to ship the package.
  '''
  if weight < 2.0:
    return 2.0
  elif weight < 10:
    return 5.0
  else:
    return 1.5 * (weight - 10) + 5


assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 1.5*(15 - 10) + 5
assert calculate_shipping(12) == 1.5*(12 - 10) + 5



def draw_square(x0:int, y0:int, side:int):
  '''
  draw a square where left corner
  is x0,y0
  '''
  pass


Book = namedtuple('Book', 'author title genre year price instock')

b1 = Book("J.K Rowling", "Harry Potter and the Goblet of Fire", "Fantasy", 2005, 9.00, 200)
b2 = Book("Ernest Hemingway", "Old man and the sea", "Fiction", 1952, 0.00, 10)
b3 = Book("Jane Austen", "Pride and Prejudice", "Fiction", 1813, 15.00, 5)

#e1
print("e1")
booklist = [b3, b1, b2]
for b in booklist:
    print(b.title)
print()

def get_title(book:Book):
    return book.title

#e2
print("e2")
s_list = sorted(booklist, key=get_title)
for b in s_list: print(b.title)
print()

#e3
print("e3")
new_list = []
for b in booklist:
    new_book = Book(b.author, b.title, b.genre, b.year, b.price * 1.10 , b.instock)
    new_list.append(new_book)
booklist = new_list

for b in booklist:
    print(b.title, b.price)
print()

#e4
book_count = 0
for b in booklist:
    book_count = book_count + b.instock
print(book_count)

#e5
def book_value(b:Book):
    return b1.price * b1.instock

assert book_value(b1) == b1.price * b1.instock


