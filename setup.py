import setuptools
from distutils.core import setup
setup(
    name = 'xgbfir',
    packages = ['xgbfir'],
    version = '0.3.1',
    description = 'Xgbfir is a XGBoost model dump parser, which ranks features as well as feature interactions by different metrics',
    author = 'Boris Kostenko',
    author_email = 'limexp@mail.ru',
    url = 'https://github.com/limexp/xgbfir',
    download_url = 'https://github.com/limexp/xgbfir/releases/tag/v0.3.1',
    keywords = ['xgbfir', 'XGBoost', 'xgbfi', 'machine learning', 'ML'], 
    classifiers = ['Development Status :: 4 - Beta', 'Environment :: Console', 'Topic :: Scientific/Engineering :: Information Analysis', 'Natural Language :: English', 'Programming Language :: Python', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6'],
    entry_points={'console_scripts':['xgbfir = xgbfir.main:entry_point']},
    install_requires=['xlsxwriter>=0.9.3'],
)
