try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import jsonrpclient
import os

setup(
    name='jsonrpclient',
    version=jsonrpclient.__version__,
    packages=['jsonrpclient'],
    url='https://github.com/jacexh/jsonrpclient',
    license='MIT',
    author='Jace Xu',
    author_email='jace@xuh.me',
    description='A JSON-RPC client in Python',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    long_description=open(
        os.path.join(os.path.dirname(__file__), "README.rst"), 'r').read(),
    install_requires=["requests>=2.5.0", "simplejson>=3.5.0"])
