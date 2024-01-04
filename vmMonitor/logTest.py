import logging
from datetime import datetime
# Configure the root logger
logging.basicConfig(level=logging.DEBUG,format="")#,format="")

Debug = 0   #Printa tudo
Warning = 0 #Printa só input 
Info = 0    #Printa só input das selecionadas

# Function decorator for logging
def rowsLog(log_level=logging.DEBUG,identifier="ND",alwaysLog=False,dev=False):#log_args=True, log_output=True
    time = datetime.now().strftime("%H:%M:%S")
    def decorator(func):
        def wrapper(*args, **kwargs):
            if log_level == logging.ERROR:
                if dev:
                    logging.log(log_level, f"{time} {identifier} {func.__name__}")
                    logging.log(log_level, f"{time}   {identifier} arg: {args}, {kwargs}")
                    result = func(*args, **kwargs)
                    logging.log(log_level, f"{time}   {identifier} out: {result}")
                    return result
                else:
                    result = func(*args, **kwargs)
                    return result
            elif log_level == logging.INFO:
                if alwaysLog:
                    logging.log(log_level, f"{time} {identifier} {func.__name__}")
                    logging.log(log_level, f"{time}   {identifier} arg: {args}, {kwargs}")
                    result = func(*args, **kwargs)
                    return result
                else:
                    result = func(*args, **kwargs)
                    return result
            elif log_level == logging.WARNING:
                logging.log(log_level, f"{time} {identifier} {func.__name__}")
                logging.log(log_level, f"{time}   {identifier} arg: {args}, {kwargs}")
                result = func(*args, **kwargs)
                return result
            elif log_level == logging.DEBUG:
                logging.log(log_level, f"{time} {identifier} {func.__name__}")
                logging.log(log_level, f"{time}   {identifier} arg: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logging.log(log_level, f"{time}   {identifier} out: {result}")
                return result

        return wrapper

    return decorator

# Example usage:
# logLevel = "DEBUG"  # Set the desired log level for the entire file
# if logLevel == "DEBUG":
#     logLevel = logging.DEBUG
# elif logLevel == "WARNING":
#     logLevel = logging.WARNING
# elif logLevel == "INFO":
#     logLevel = logging.INFO
# elif logLevel == "ERROR":
#     logLevel = logging.ERROR





# @rowsLog(log_level=logLevel,identifier="tt",dev=True)
# def example_function1(x, y):
#     return x + y

# @rowsLog(log_level=logLevel,alwaysLog=True)
# def example_function2(a, b):
#     return a * b

# @rowsLog(log_level=logLevel, alwaysLog=True,dev=True)
# def example_function3():
#     return "Hello, world!"


# # # Example usage of the functions
# print(example_function1(2, 3))
# # example_function2(4, 5)
# # example_function3()

