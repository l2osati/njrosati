from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='njrosati',
    version='0.0.3',
    author='Nick Rosati',
    author_email='l2osati@gmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/l2osati/njrosati',
    project_urls = {
        "Bug Tracker": "https://github.com/l2osati/njrosati/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
)
