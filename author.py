class Author:
    '''Creating the Author class, which takes the author's name and biography. 
    The class has the functionality to display the author's information, edit the name 
    and biography and to retrieve the author's name.'''
    def __init__(self, name, biog):
        self.name = name # author's first and last name
        self.biog = biog # author's biography
    
    def set_name(self, new_name):
        self.name = new_name # update the name
    
    def set_biog(self, new_biog):
        self.biog = new_biog # update the biography
    
    def get_author(self):
        return self.name # retrieve the author's name
    
    def display_author(self):
        # Display the author with the following format:
        # author_name
        #   -  biography
        print(f'\n\033[1m{self.name}\033[0m')
        print(f" - {self.biog}")