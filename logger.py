
def log_error(error_message):
    """
    This function appends the error message to the file, ensuring that 
    each error message is written on a new line. If 'error_log.txt' 
    does not exist, it will be created.

    Parameters:
        error_message (str): The error message to be logged.

    Returns:
        None
    """
    # Open 'error_log.txt' in append mode ('a'). 
    # If the file doesn't exist, it will be created.
    with open('error_log.txt', 'a') as f:
        # Writing the error message to the file and add a newline character for separation.
        f.write(error_message + "\n")


