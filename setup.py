from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    HYPHEN_E_DOT = '-e .'

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
name = 'dsproject',
version = '0.0.1',
author = 'AayCode',
author_email = 'aaaayshamansuri786@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)

