import requests
from AcquireJSON import aquireJSON, jsonSummary
from wealthSphereObjectsAndMethods import tickerDataBase, miniDataBase


def commands(command):
    if command == 'a':
        askForTicker = input('Enter a stock ticker.')
        miniDataBase.addTicker(askForTicker)
        return True
    elif command == 'r':
        askForTicker = input('Enter a stock ticker.')
        miniDataBase.removeTicker(askForTicker)
        return True
    elif command == 'x':
        miniDataBase.removeAllTickers()
        return True
    elif command == 'v':
        miniDataBase.seeTickers()
        return True
    elif command == 's':
        jsonSummary()
        return True
    else:
        return False



def askForCommand():
    commands = ['a', 'r', 'x', 'v', 's']
    isRunning = True
    while isRunning:
        command = input('Type a commmand a/r/x/v/s: ')
        if command in commands:
            isRunning = False
        else:
            print('Please give a valid command')
            
    return command

def leaveApplication():
    validCommands = ['Y', 'N']
    isRunning = True
    while isRunning:
        askToLeave = input("If you want to continue press 'Y' if you want to leave press 'N'. ")
        if askToLeave.upper() in validCommands:
            isRunning = False
        else:
            print('Please type a vald command')

    return validCommands


def main():
    print('')
    print('')
    print('')

    isRunning = True
    while isRunning:
        for index in range(3):
            print('')
        headline = [f"Welcome to Wealth Sphere.", f"Press 'a to add", f"Press'r' to remove", f"ress 'x' to remove all," f"Press'v' to view", f"Press and 's' to see all news of latest news in watchlist."]
        for line in headline:
            print(line)
        command = askForCommand()
        if command == 'a':
            commands('a')
        elif command == 'r':
            commands('r')
        elif command == 'x':
            commands('x')
        elif command == 'v':
            commands('v')
        else:
            commands('s')
            decision = leaveApplication()
            if decision == "N":
                pass
            elif decision == 'Y':
                isRunning = False      
main()


