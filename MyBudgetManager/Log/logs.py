import logging
import os


path_log_debug_file = os.path.abspath(
    "MyBudgetManager/Debug_And_Info/MyBudgetManagerLogDebug.txt")
path_log_info_file = os.path.abspath(
    "MyBudgetManager/Debug_And_Info/MyBudgetManagerLogInfo.txt")


# Create the Logger
logger = logging.getLogger("My Budget Manager")
logger.setLevel(logging.DEBUG)

# Create the Handler for logging data to a file
debug_log = logging.FileHandler(
    path_log_debug_file, mode='a')
debug_log.setLevel(logging.DEBUG)
info_log = logging.FileHandler(
    path_log_info_file, mode='a')
info_log.setLevel(logging.INFO)

# Create a Formatter for formatting the log messages
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    "%Y-%m-%d %H:%M:%S")

# Add the Formatter to the Handler
debug_log.setFormatter(formatter)
info_log.setFormatter(formatter)

# Add the Handler to the Logger
logger.addHandler(debug_log)
logger.addHandler(info_log)
