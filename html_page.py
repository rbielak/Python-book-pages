#!/usr/bin/python
#
#  Class for generating HTML pages
#

class Html_Page:

    def __init__ (self, t="", h=""):
        self.title = t
        self.heading = h

    def generate_heading (self, bgcolor=""):
        #
        # Generate heading for a page
        #
        self.f.write ("<html>\n")
        self.f.write ("<head>\n")
        self.f.write ("<title>" + self.title + "</title>\n")
        self.f.write ("</head>\n")
        self.f.write ("<body bgcolor=" + bgcolor + ">\n")
        self.f.write ("<h1 align=center>" + self.heading + "</h1>\n")

    def generate_body (self):
        #
        # Empty function - to be redefined in a descendant
        #
        print("")

    def generate_trailer (self):
        #
        # generate the trailer for a page
        #
        self.f.write ("</body>\n")
        self.f.write ("</html>\n")
    
    def generate (self, bgcolor=""):
        self.generate_heading (bgcolor)
        self.generate_body ()
        self.generate_trailer ()

#
# Code to test this class
#


if __name__ == "__main__":
    p = Html_Page ("This is the title", "<i>This is the top heading</i>")
    p.generate ("lightblue")

