import setuptools
from typing import list

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()

Hypen_e_dot="-e ."

def get_requirwments(file_path:str)->list[str]:
    '''
    This function will return list of the requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    
    return requirements



__version__ = "0.0.0"

REPO_NAME = "ML_Project"
AUTHOR_USER_NAME = "Anshu Kumari"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "anshu.ak238@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    # long_description=long_description,
    # long_description_content="text/markdown",
    # url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    # project_urls={
    #     "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    # },
    # package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    install_requires=get_requirements('requirements.txt')
)