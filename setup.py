import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "end---to-end-text-summarizer"
AUTHOR_USER_NAME = "preetamjumech"
SRC_REPO = "textSummarizer"
AUTTHOR_EMAIL = "preetamjumech@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description= "A simple project for text summarization",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)