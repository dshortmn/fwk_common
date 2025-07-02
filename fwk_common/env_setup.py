import inspect
from os import getcwd, path


def GetCommonPath():
    current_directory = getcwd()
    return current_directory


def GetCurrentPath():
    current_directory = __file__  # .rsplit('/', 2)[0]
    return current_directory


def GetPathInfo():
    # inspect.stack()[1] gets the frame of the direct caller
    caller_frame = inspect.stack()[1]
    # Extract the filename from the frame information
    caller_filepath = caller_frame.filename
    # Make the path absolute
    absolute_path = path.abspath(caller_filepath)
    directory_path = path.dirname(absolute_path)
    config_path = path.join(directory_path, "config")
    sql_path = path.join(directory_path, "sql")
    del caller_frame

    return config_path, sql_path
