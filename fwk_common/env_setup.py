import inspect
from os import path


def GetCallingPath():
    caller_frame = inspect.stack()[1]
    # Extract the filename from the frame information
    caller_filepath = caller_frame.filename
    del caller_frame
    return path.abspath(caller_filepath)


def GetConfigPathInfo(inPath=None):
    if inPath is None:
        caller_frame = inspect.stack()[1]
        # Extract the filename from the frame information
        caller_filepath = caller_frame.filename
        del caller_frame
        absolute_path = path.abspath(caller_filepath)
    else:
        absolute_path = path.abspath(inPath)

    directory_path = path.dirname(absolute_path)
    config_path = path.join(directory_path, "config")
    sql_path = path.join(directory_path, "sql")

    return config_path, sql_path
