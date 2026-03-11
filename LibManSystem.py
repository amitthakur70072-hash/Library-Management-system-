library=[]
def add_books():
    book=input("enter book name to be added: ")
    library.append(book)
    print(f"'{book}' has been added")

def issue_book():
    book=input("enter book name to be issue: ")
    if book in library:
        library.remove(book)
        print(f"{book} has been issued")
    else:
        print("book not found")

def return_book():
    book=input("enter the book name to be returned: ")
    library.append(book)
    print("book has been returned")

def view_book():
    if not library:
        print("no books are present in library")
    else:
        print("List of books")
        idx=1
        for book in library:
            print(f"{idx}. {book}")
            idx+=1

        print()

while(True):
    print("-----Library Management System-------"
    print("1. Add book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. View book")
    print("5. exit")

    choice=int(input("enter your choice : "))
    if choice==1:
        add_books()
    elif choice==2:
        issue_book()
    elif choice==3:
        return_book()
    elif choice==4:
        view_book()
    elif choice==5:
        print("Thank you")
        break
    else:
        print("invalid choice. Try again  ")




