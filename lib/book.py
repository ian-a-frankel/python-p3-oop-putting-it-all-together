#!/usr/bin/env python3

class Book:
    def __init__(self, title, pages_count):
        
        self.title = title

        if type(pages_count) == int:
            self._page_count = pages_count
        else:
            print("page_count must be an integer")

    @property
    def page_count(self):
            return(self._page_count)
        
    @page_count.setter
    def page_count(self, new_page_count):
        if isinstance(new_page_count,int):
            self._page_count = new_page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
         print("Flipping the page...wow, you read fast!")
    
        