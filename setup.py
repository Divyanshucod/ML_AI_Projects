from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirement(file_path:str)->List[str]:
    requirements=[]

    with open(file_path,'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements 

setup(
name="ML_AI_Projects",
version='0.0.1',
author='Divyanshu',
author_email='ultimateg657@gmail.com',
packages=find_packages(),
install_requires = get_requirement('requirements.txt')

)