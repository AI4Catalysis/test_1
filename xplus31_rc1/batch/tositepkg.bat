@cd ..
set pkgroot=%_my_PYTHON_ENV_ROOT%\Python3.11.9\Lib\site-packages
python setup.py build --build-lib %pkgroot%
python setup.py egg_info --egg-base %pkgroot%