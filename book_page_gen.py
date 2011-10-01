#!/usr/bin/python
# This script generates HTML pages for my book index. The input is 
# a file that describes each book: title, author, subject and URL
# of the book's reviews
#
# Args: <book-description-file>
#
import sys
from book_list import Book_List
from books_pages import Authors_Page, Titles_Page, Subjects_Page

#
# Get the list of books from a file
#
f = open (sys.argv[1], "r")
book_list = Book_List ()
book_list.make_from_file (f)
f.close ()
#
# Sort the list by author and generate an HTML page
#
book_list.sort_by_author ()
author_page = Authors_Page ()
author_page.set_book_list (book_list.contents)
author_page.generate ("lightblue")
# Sort the list by title and generate an HTML page
#
book_list.sort_by_title ()
titles_page = Titles_Page ()
titles_page.set_book_list (book_list.contents)
titles_page.generate ("lightblue")

# Sort the list by title and generate an HTML page
#
book_list.sort_by_subject ()
subject_page = Subjects_Page ()
subject_page.set_book_list (book_list.contents)
subject_page.generate ("lightblue")




