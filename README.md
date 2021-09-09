# for middleware service package 

** check the python and pip version and update latest version


** install and create the virtual environment on current os
- $ pip install virtualenv
- $ virtualenv env_name


** check and upgrade the pip and setuptool packages
- $ python -m pip install --upgrade pip setuptools wheel


** install the middleware package in the venv using given command
- $ pip3 install git+https://github.com/gupta24/service


** run middleware package on virtualenv
- $ uvicorn middleware_service.src.main:app --reload

