import inspect
from os import getcwd, path


def GetCommonPath():
    current_directory = getcwd()
    return current_directory


def GetCurrentPath():
    current_directory = __file__  # .rsplit('/', 2)[0]
    return current_directory


def get_caller_info():
    """
    Returns the absolute path and name of the module that called this function.
    """
    # inspect.stack()[1] gets the frame of the direct caller
    caller_frame = inspect.stack()[1]

    # Extract the filename from the frame information
    caller_filepath = caller_frame.filename

    # Make the path absolute
    absolute_path = path.abspath(caller_filepath)

    # Get the module name (filename without extension)
    module_name = path.splitext(path.basename(absolute_path))[0]

    # Clean up the reference to the frame to avoid potential reference cycles
    del caller_frame

    return absolute_path, module_name
