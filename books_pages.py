from html_page import Html_Page


#
# Generate HTML book page indexed by author
#
class Authors_Page (Html_Page):

    def __init__ (self):
        Html_Page.__init__ (self, "Aviation Books: by Author",
                    "<i>Aviation Books: indexed by Author</i>")
        self.f = open ("books_by_author.html", "w")
        print("Authors page in--> " + self.f.name)

    def set_book_list (self, list):
        self.book_list = list

    def generate_body (self):
        #
        # Generate a table
        #
        self.f.write ("<hr>\n")
        self.f.write ("<center>\n")
        self.f.write ("<table border=0 width=" + '"' + "80%" + '"' + ">\n")
        last_author_ln = ""
        last_author_fn = ""
        for b in self.book_list:
            if (b.last_name[0] == last_author_ln) and (b.first_name[0] == last_author_fn):
                line = "<tr><td></td>"
            else:
                line = "<tr><td>"
                # Print authors names
                i = 0
                while i < len(b.last_name):
                    if i > 0:
                        line = line +  " and "
                    line = line +  b.last_name[i] + ", " + b.first_name[i]
                    i = i + 1
                line = line + " </td>\n"
                last_author_ln = b.last_name[0]
                last_author_fn = b.first_name[0]
            self.f.write (line)
            line = "<td>"
            if len(b.url) != 0:
                line = line + "<a href=" + b.url + "><i>" + '"' + b.title + '"' + "</i></a>"
            else:
                line = line + "<i>" + '"' + b.title + '"' + "</i>"
            line = line + "</td></tr>\n"
            self.f.write (line)
        self.f.write ("</table>\n </center>\n<hr>\n")
        count = len (self.book_list)
        self.f.write ("<center>There are " + ("%1d" % count) + " books in the list</center>\n")

        def generate_trailer (self):
            self.f.write ("<hr>\n")
            self.f.write ("<center><a href=books.html>Back to Aviation Books Top Page</a></center>\n")
            self.f.write ("<hr>\n")
            Html_Page.generate_trailer (self)

#
# Page index by Titles
#
class Titles_Page (Html_Page):

    def __init__ (self):
        Html_Page.__init__ (self, "Aviation Books: by Title",
                    "<i>Aviation Books: indexed by Title</i>")
        self.f = open ("books_by_title.html", "w")
        print ("Titles page in --> " + self.f.name)

    def set_book_list (self, list):
        self.book_list = list

    def generate_body (self):
        #
        # Generate table
        #
        self.f.write ("<hr>\n")
        self.f.write ("<center>\n")
        self.f.write ("<table border=0 width=" + '"' + "80%" + '"' + ">\n")
        for b in self.book_list:
            line = "<tr><td><i>"
            if len(b.url) != 0:
                line = line + "<a href=" + b.url + "><i>" + '"' + b.title + '"' + "</i></a>"
            else:
                line = line + "<i>" + '"' + b.title + '"' + "</i>"
            line = line + "</td><td>"
            # Print authors names
            i = 0
            while i < len (b.last_name):
                if i > 0:
                    line = line + " and "
                line = line +  b.first_name[i] + " " +  b.last_name[i]
                i = i + 1
            line = line + "</td></tr>\n"
            self.f.write (line)
        self.f.write ("</table>\n")
        self.f.write ("</center>\n")
        self.f.write ("<hr>\n")
        count = len (self.book_list)
        self.f.write ("<center>There are " + ("%1d" % count) + " books in the list</center>\n")


    def generate_trailer (self):
        self.f.write ("<hr>\n")
        self.f.write ("<center><a href=books.html>Back to Aviation Books Top Page</a></center>\n")
        self.f.write ("<hr>\n")
        Html_Page.generate_trailer (self)


#
# Create a page indexed by subject
#
class Subjects_Page (Html_Page):

    def __init__ (self):
        Html_Page.__init__ (self, "Aviation Books: by Subject",
                    "<i>Aviation Books: indexed by Subject</i>")
        self.f = open ("books_by_subject.html", "w")
        print("Subject page in --> " + self.f.name)


    def set_book_list (self, list):
        self.book_list = list

    def generate_body (self):
        #
        # Generate table
        #
        self.f.write ("<hr>\n")
        self.f.write ("<center>\n")
        self.f.write ("<table border=0 width=" + '"' + "100%" + '"' + ">\n")
        last_subject = "";
        for b in self.book_list:
            if last_subject != b.subject:
                line = "<tr><td><b>" + b.subject + "</b></td>"
                last_subject = b.subject
            else:
                line = "<tr><td></td>"
            line = line + "<td><i>"
            if len(b.url) != 0:
                line = line + "<a href=" + b.url + "><i>" + '"' + b.title + '"' + "</i></a>"
            else:
                line = line + "<i>" + '"' + b.title + '"' + "</i>"
            line = line + "</td><td>"
            # Authors
            i = 0
            while i < len (b.last_name):
                if i > 0:
                    line = line + " and "
                line = line + b.first_name[i] + " " + b.last_name[i]
                i = i + 1
            line = line + "</td></tr>\n"
            self.f.write (line)
        self.f.write ("</table>\n")
        self.f.write ("</center>\n")
        self.f.write ("<hr>\n")
        count = len (self.book_list)
        self.f.write ("<center>There are " + ("%1d" % count) + " books in the list</center>\n")


    def generate_trailer (self):
        self.f.write ("<hr>\n")
        self.f.write ("<center><a href=books.html>Back to Aviation Books Top Page</a></center>\n")
        self.f.write ("<hr>\n")
        Html_Page.generate_trailer (self)

