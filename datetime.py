"""
Creates a datetime file
"""

from datetime import datetime as dtdatetime

filename=dtdatetime.now()

#create a file
def create_file():
    """This function creates a file"""
    with open(str(filename), "w") as file:
        file.write("")

create_file()
