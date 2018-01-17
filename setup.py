# coding:utf-8

from setuptools import setup, find_packages
import  io
VERSION = '0.0.1'

with io.open("README.rst", encoding='utf-8') as f:
    long_description = f.read()
# 这里是读取那个文件里面的必须安装的  这样无论手动 pip install -r requirements.txt 安装
# 还是自动安装install_requires 都是这些信息
install_requires = open("requirements.txt").readlines()

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
    license='MIT',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/gaoqiang1112/gqUtil.git',
    classifiers=[],
    install_requires=install_requires,
)