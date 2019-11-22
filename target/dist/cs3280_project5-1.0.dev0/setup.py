#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'cs3280_project5',
        version = '1.0',
        description = 'Project for CS3280 : Scans ports',
        long_description = ' Takes an ip address and a port or a pair\n                              of ports and determines whether there the \n                              port is listening or not. ',
        author = 'Thomas Whaley',
        author_email = 'twhaley1@my.westga.edu',
        license = '',
        url = '',
        scripts = [],
        packages = [],
        namespace_packages = [],
        py_modules = ['portscan'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
