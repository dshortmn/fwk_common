from os import getcwd


def GetCommonPath():
    current_directory = getcwd()
    return current_directory


def GetCurrentPath():
    current_directory = __file__  # .rsplit('/', 2)[0]
    return current_directory
