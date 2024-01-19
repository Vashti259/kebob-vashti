""" Start a data analytics."""

Import pathlib


def create_project_(directory_name: str): 
"""
Creates a project sub-directory.
:param directory_name: Name to be created, e.g "test"
"""
 pathlib.Path(directory name).mkdir(exit ok=True)
 
 
def main():
"""Scaffold a project. """
create_project_directory(directory_name='test') # name the parameter
create_project_directory(directory_name='docs') # name the parameter


if __name_ --'_main_':
    main()    