from  setuptools import find_packages,setup;
from typing import List

HYPEN_E_DOT='-e.'

def get_requriments(file_path:str)->List[str]:

    requriments=[]
    with open(file_path) as file_obj:
        requriments=file_obj.readlines()
        requriments= [req.replace("/n","") for req in requriments]
        if(HYPEN_E_DOT) in requriments:
            requriments.remove(HYPEN_E_DOT)
        return requriments


setup(
    name="mlproject",
    version="0.0.1",
    author="Prudhvi",
    author_email='prudhvimohan8@gmail.com',
    packages = find_packages(),
    install_requires=get_requriments('requriments.txt'),
)