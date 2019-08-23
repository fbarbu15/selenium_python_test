'''
Created on Aug 23, 2019

@author: fbarbu15
'''

from subprocess import Popen

processes = []

chrome_cmd = 'export BROWSER=docker_chrome && pytest tests/hotels_tests.py'
firefox_cmd = 'export BROWSER=docker_firefox && pytest tests/hotels_tests.py'
print("RUNNING SUITE ON <<CHROME>> AND <<FIREFOX>> BROWSERS IN PARALLEL INSIDE DOCKER CONTAINERS")
print("#########################################################################################")
processes.append(Popen(chrome_cmd, shell=True))
processes.append(Popen(firefox_cmd, shell=True))
