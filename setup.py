from setuptools import find_packages,setup 
from typing import List


hyphen_e='-e .'
def get_packages(file_path:str)->List[str]:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[lines.replace("\n","") for lines in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements


setup(
      name="mlops_project",
      version= '0.0.1',
      author='Ubaid Shah',
      author_email='ubaidhaina@gmail.com',
      packages=find_packages(),
      install_requires=get_packages('requirements.txt')
)