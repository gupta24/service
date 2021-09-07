import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='middleware_service',
    version='0.0.1',
    author='Rahul',
    description='for data authentication by middleware',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/',
    license='MIT',
    packages=['middleware_service'],
    install_requires=[],
)