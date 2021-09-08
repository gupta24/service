from setuptools import setup, find_packages 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


VERSION = '0.0.1'
DESCRIPTION = 'for data authentication by middleware'
LONG_DESCRIPTION = long_description



setup(
    name='middleware_service',
    version=VERSION,
    author='Rahul',
    author_email='rahul.gupta@adcuratio.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/gupta24/service',
    project_urls = {
        "Bug Tracker": "https://github.com/gupta24/service/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)
