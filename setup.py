# coding:utf-8

from setuptools import setup, find_packages
import  io
VERSION = '0.0.1'

with io.open("README.md", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="gqUtil",
    version=VERSION,
    description=(
        'gq的工具'
    ),
    long_description=long_description,
    author='gaoqiang',
    author_email='gaoqiang1112@163.com',
    maintainer='gaoqiang',
    maintainer_email='gaoqiang1112@163.com',
    license='BSD License',
    packages=find_packages(exclude=('tests', 'tests.*')),
    platforms=["all"],
    url=
)
# setup(
#     url='<项目的网址，我一般都是github的url>',
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Operating System :: OS Independent',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: BSD License',
#         'Programming Language :: Python',
#         'Programming Language :: Python :: Implementation',
#         'Programming Language :: Python :: 2',
#         'Programming Language :: Python :: 2.7',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.6',
#         'Topic :: Software Development :: Libraries'
#     ],
# )