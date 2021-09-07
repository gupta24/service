import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='middleware_service',
    version='0.0.1',
    author='Rahul',
    author_email='rahul.gupta@adcuratio.com',
    description='for data authentication by middleware',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gupta24/service',
    project_urls = {
        "Bug Tracker": "https://github.com/gupta24/service/issues"
    },
    license='MIT',
    packages=find_packages(include=['middleware_service', 'middleware_service.*']),
    install_requires=[],
    include_package_data=True,
    zip_safe=False
)
