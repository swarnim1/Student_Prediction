from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
    name='Student_prediction',
    version='1.0',
    author='Swarnim Dixit',
    author_email='dixitswarnim1@gmail.com.com',
    description='Introduxtion project to me',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/swarnim1/Student_Prediction',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
