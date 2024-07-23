from setuptools import find_packages,setup

def req(filepath):

    requirements=[]

    with open(filepath) as file_obj:

        requirements=file_obj.readlines()

        requirements=[i.replace("\n"," ") for i in requirements]

        if '-e .' in requirements:

            requirements.remove('-e .')

    return requirements

setup(

    name='trail',

    version='0.0.1',

    packages=find_packages(),

    install_requires=req('requirements.txt'),
)

