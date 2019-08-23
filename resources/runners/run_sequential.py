'''
Created on Aug 23, 2019

@author: fbarbu15
'''

from subprocess import check_call

chrome_cmd = 'export BROWSER=docker_chrome && pytest tests/hotels_tests.py'
firefox_cmd = 'export BROWSER=docker_firefox && pytest tests/hotels_tests.py'
print("RUNNING SUITE ON <<CHROME>> BROWSER INSIDE DOCKER CONTAINER")
print("###########################################################")
check_call(chrome_cmd, shell=True)
print("RUNNING SUITE ON <<FIREFOX>> BROWSER INSIDE DOCKER CONTAINER")
print("############################################################")
check_call(firefox_cmd, shell=True)
