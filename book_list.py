#
# Book list
#

import book
import string

class Book_List:

    def __init__ (self):
        self.contents = []

    def cmp(a, b):
        return (a > b) - (a < b)

    def make_from_file (self, file):
        #
        # Read the file and create a book list
        #
        lines = file.readlines ()
        self.contents = []
        #
        # Parse each line and create a list of Book objects
        #
        for one_line in lines:
            # It's  not a comment or empty line
            if (len(one_line) > 0) and (one_line[0] != "#"):
                # Split into tokens
                tokens = one_line[:-1].split(":", 1)
                if len (tokens) > 0:
                    if tokens[0] == "title":
                        current_book = book.Book (tokens[1].strip())
                        self.contents.append (current_book)
                    elif tokens[0] == "author":
                        current_book.set_author (tokens[1])
                    elif tokens[0] == "subject":
                        current_book.set_subject (tokens[1].strip())
                    elif tokens[0] == "url" and len(tokens) > 1:
                        current_book.set_url (tokens[1].strip())

    def sort_by_author (self):
        #
        # Sort book list by author
        #
        self.contents.sort (key = lambda x : x.last_name)


    def sort_by_title (self):
        #
        # Sort book list by title
        #
        self.contents.sort (key = lambda x : x.title)


    def sort_by_subject (self):
        #
        # Sort by subject
        #
        self.contents.sort (key = lambda x : x.subject)


    def display (self):
        #
        # Print the contents of the list
        #
        for b in self.contents:
            print("-----------------")
            b.display ()
        print("-----------------")


#
# Code to test this class
#
if (__name__ == "__main__"):
    print ("*** testing book_file_parser ****")
    f = open ("books.txt", "r")
    book_list = Book_List ()
    book_list.make_from_file (f)
    book_list.display ()
    book_list.sort_by_author ()
    book_list.display ()
    book_list.sort_by_title ()
    book_list.display ()
    book_list.sort_by_subject ()
    book_list.display ()

