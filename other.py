class Book:

    def __init__(self, isbn, title, category, publisher, year_published):
        self.isbn = isbn
        self.title = title
        self.category = category
        self.publisher = publisher
        self.year_published = year_published

    def __lt__(self, other):
        return self.category < other.category

    def __repr__(self):
        return f"Book({self.isbn}, {self.title}, {self.category}, {self.publisher}, {self.year_published})"


records = [{'ISBN (PK)': 2, 'Title': 'Python Cookbook ', 'Category': 'Category 1', 'Publisher': 'Denise', 'Year_Published': 495},
               {'ISBN (PK)': 2, 'Title': 'Python Cookbook ', 'Category': 'Category 2', 'Publisher': 'Zaren', 'Year_Published': 325},
               {'ISBN (PK)': 4, 'Title': 'Python Cookbook ', 'Category': 'Category 3', 'Publisher': 'Nat', 'Year_Published': 1275},
               {'ISBN (PK)': 4, 'Title': 'Python Cookbook ', 'Category': 'Category 2', 'Publisher': 'Lylia', 'Year_Published': 1379},
               {'ISBN (PK)': 3, 'Title': 'Python Cookbook ', 'Category': 'Category 1', 'Publisher': 'Dino', 'Year_Published': 2189},
               {'ISBN (PK)': 3, 'Title': 'Python Cookbook ', 'Category': 'Category 4', 'Publisher': 'Johnson', 'Year_Published': 1275},
               {'ISBN (PK)': 5, 'Title': 'Python Cookbook ', 'Category': 'Category 5', 'Publisher': 'Kagura', 'Year_Published': 1435},
               {'ISBN (PK)': 2, 'Title': 'Python Cookbook ', 'Category': 'Category 3', 'Publisher': 'Stitch', 'Year_Published': 1379},
               {'ISBN (PK)': 4, 'Title': 'Python Cookbook ', 'Category': 'Category 1', 'Publisher': 'Alice', 'Year_Published': 1534},
               {'ISBN (PK)': 4, 'Title': 'Python Cookbook ', 'Category': 'Category 2', 'Publisher': 'Nathan', 'Year_Published': 1189}]

def display_menu():
        print("** Book Management System **")
        menu = ["1. Display of all the books' records", 
            "2. Add a new book", 
            "3. Sort books by their Category in ascending order using Bubble sort and display the outcome",
            "4. Sort the Publisher in decending order using only Selection sort and display outcome"]
        print(*menu, sep='\n')

def AllRecords():
    for x in records:
        print("\nCategory:", x['Category'])
        print("Publisher:", x['Publisher'])
        print("Number of ISBN (PK):", x['ISBN (PK)'])
        print("Category Year_Published Per Person: Year {}".format(x['Year_Published']) , '\n')

def addnew():
    PK = str(input("Please key in the PK of the book: "))
    Title = str(input("Please key in the Title of the book: "))
    Category = str(input("Please key in the Category of the book: "))
    Publisher = str(input("Please key in the Publisher of the book: "))
    Year = input("Please key in the Year of the book: ")
    if Year.isdigit():
            Year = int(Year)
    else:
        print("Year shoud be integer")
        addnew()
    
    dict = {'ISBN (PK)': PK, 'Title': Title, 'Category': Category, 'Publisher': Publisher, 'Year_Published': Year}
    records.append(dict.copy())
    print("book has been added")

def BubbleSort():
    length = len(records)

    for i in range(length - 1, 0, -1):
        for j in range(i):
            if records[j]['Category'] > records[j + 1]['Category']:
                tmp = records[j]
                records[j] = records[j + 1]
                records[j + 1]= tmp
    print("\nRecords have been sorted by Category")

def SelectionSort():
    length = len(records)

    for i in range(length - 1):
        smallNdx = i
        for j in range(i + 1, length):
            if records[j]['Publisher'] > records[smallNdx]['Publisher']:
                smallNdx = j
        if smallNdx != i:
            tmp = records[i]
            records[i] = records[smallNdx]
            records[smallNdx] = tmp

    print("\nRecords have been sorted by Publisher in descending order")

while True:
        display_menu()
        choice = input("Please choose from the above selection (Q to quit): ")
        choice.upper()
        if choice == '1':
            AllRecords()
            continue
        if choice == '2':
            addnew()
            continue
        elif choice == '3':
            BubbleSort()
            AllRecords()
            continue
        elif choice == '4':
            SelectionSort()
            AllRecords()
            continue

        elif choice == 'Q' or choice == 'q':
            print("\nExiting application. Goodbye!")
            break
        else:
            print("Please enter a valid value")


if __name__ == "__main__":
    display_menu()
