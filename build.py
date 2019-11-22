from pybuilder.core import use_plugin, init, task, Author
import os, subprocess

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

default_task = "publish"

@init
def set_properties(project):
    project.name = "cs3280_project5"
    project.version = "1.0"
    project.summary = "Project for CS3280 : Scans ports"
    project.description = ''' Takes an ip address and a port or a pair
                              of ports and determines whether there the 
                              port is listening or not. '''
    project.authors = [Author('Thomas Whaley', 'twhaley1@my.westga.edu')]
    
@task
def scan_port_60000():
    callArgs = ['python', 'src/main/python/portscan.py', '127.0.0.1', '60000']
    subprocess.call(callArgs)
    
@task
def scan_port_60000_to_60010():
    callArgs = ['python', 'src/main/python/portscan.py', '127.0.0.1', '60000', '60010']
    subprocess.call(callArgs)
