#
# Book list
#

import book
import string

class Book_List:

    def __init__ (self):
        self.contents = []
    

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
                tokens = string.split (one_line)
                if len (tokens) > 0:
                    if (tokens[0] == "title:"):
                        current_book = book.Book (string.join (tokens[1:]))
                        self.contents.append (current_book)
                    elif (tokens[0] == "author:"):
                        current_book.set_author (string.join (tokens[1:]))
                    elif (tokens[0] == "subject:"):
                        current_book.set_subject (string.join (tokens[1:]))
                    elif (tokens[0] == "url:"):
                        current_book.set_url (string.join (tokens[1:]))

			    
    def sort_by_author (self):
        #
        # Sort book list by author
        #
        def cmp_author (x, y):
            res = cmp (x.last_name, y.last_name)
            if res == 0:
                res = cmp (x.first_name, y.first_name)
                if res == 0:
                    res = cmp (x.title, y.title)
            return res

        self.contents.sort (cmp_author)


    def sort_by_title (self):
        #
        # Sort book list by title
        #
        self.contents.sort (lambda x, y: cmp (x.title, y.title))


    def sort_by_subject (self):
        #
        # Sort by subject
        #
        def cmp_subject (x, y):
            res = cmp (x.subject, y.subject)
            if res == 0:
                res = cmp (x.title, y.title)
            return res

        self.contents.sort (cmp_subject)


    def display (self):
        #
        # Print the contents of the list
        #
        for b in self.contents:
            print "-----------------"
            b.display ()
        print "-----------------"

#
# Code to test this class
#
if (__name__ == "__main__"):
    print "*** testing book_file_parser ****"
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

