export TWINE_USERNAME=${PYPI_USER}
export TWINE_PASSWORD=${PYPI_PASSWD}

pip install --upgrade pip setuptools wheel
pip install twine

cd pypow/

python setup.py sdist
twine upload --skip-existing dist/*