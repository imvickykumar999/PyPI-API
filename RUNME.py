
import os

os.system('pip install -r requirements.txt')

os.system('python setup.py sdist bdist_wheel')

os.system('twine upload dist/*')
