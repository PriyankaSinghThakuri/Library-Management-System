# to extract data from .txt file

def read_Book():
    file = open("Books.txt","r")
    contents = file.readlines()
    list_Book = []
    dictionary_Book = {}
    for i in contents:
        list_Book.append(i.replace("\n","").split(","))
    for i in range(len(list_Book)):
        key = list_Book[i][0]
        value = []
        for j in range(1, len(list_Book[0])):
            value.append(list_Book[i][j])
            dictionary_Book[key] = value
    return dictionary_Book
dictionary_Book = read_Book()
def Book_name():
    Book_name = []
    for key in dictionary_Book.keys():
        Book_name.append(key)
    return Book_name
