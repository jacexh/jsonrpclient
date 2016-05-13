import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("jsonrpclient/__init__.py", 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='jsonrpclient',
    version=version,
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
    install_requires=["requests>=2.9.0"])
