from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = [line.rstrip('\n') for line in file_obj]

        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Aravint Annamalai',
    author_email='aravint2001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

