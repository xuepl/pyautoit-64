
#1. 本地打包
python setup.py sdist  
#2. 发布版本
pip install twine
twine upload dist/pyautoit-win64-1.0.0.tar.gz