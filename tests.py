from AcquireJSON import jsonSummary, aquireJSON
from main import commands, askForCommand, main, leaveApplication
from validateTicker import validation
from wealthSphereObjectsAndMethods import tickerDataBase, miniDataBase
import json 
import requests

def testCommands():
    validCommands = ['a', 'r', 'x', 'v', 's']
    for item in validCommands:
        assert testCommands(item) == True
    invalidCommands = [3, '5', None, '14', 3.14]
    for item in invalidCommands:
        assert testCommands(item) == False
    return True


def testValidation():
    assert validation('aapl') == 200
    assert validation('Not a valid stock ticker') != 200
    return True


def printTests():
    print(testValidation())
    print(testCommands())
