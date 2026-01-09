from setuptools import find_packages,setup
from typing import List

HYPNEN_E_DOT='-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    this function will return the list of requirments
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPNEN_E_DOT in requirments:
            requirments.remove(HYPNEN_E_DOT)

    return requirments

setup(
name='mlproject',
version='0.0.1',
author="kashyap",
author_email="asvkashyap@gmail.com",
packages= find_packages(),
install_requires=get_requirments('requirements.txt')

)