import inspect
from os import path


def stack_size(stack):
    if not isinstance(stack, list):
        raise TypeError("stack must be a list")
    if not all(isinstance(item, object) for item in stack):
        raise TypeError("all items in stack must be object")
    if not stack:
        return 0
    return len(stack)


def GetCallingPath(steps=1):
    xsize = stack_size(inspect.stack())
    # print(f"GetCallingPath: stack size = {xsize}, steps = {steps}")
    if steps < 1 or steps >= xsize:
        raise ValueError(f"steps must be between 1 and {xsize - 1}, got {steps}")
    caller_frame = inspect.stack()[steps]
    # Extract the filename from the frame information
    caller_filepath = caller_frame.filename

    # Clean up the frame reference to avoid memory leaks
    del caller_frame
    return path.abspath(caller_filepath)


def GetConfigPathInfo(inPath=None):
    if inPath is None:
        absolute_path = GetCallingPath(2)
    else:
        absolute_path = path.abspath(inPath)
    print(f"GetConfigPathInfo: absolute_path = {absolute_path}")
    directory_path = path.dirname(absolute_path)
    config_path = path.join(directory_path, "config")
    sql_path = path.join(directory_path, "sql")
    if not path.exists(config_path):
        raise FileNotFoundError(f"Config path does not exist: {config_path}")
    if not path.exists(sql_path):
        raise FileNotFoundError(f"SQL path does not exist: {sql_path}")
    if not path.isdir(config_path):
        raise NotADirectoryError(f"Config path is not a directory: {config_path}")
    if not path.isdir(sql_path):
        raise NotADirectoryError(f"SQL path is not a directory: {sql_path}")
    return config_path, sql_path
