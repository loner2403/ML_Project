import sys
import logging

def error_message_detial(error,error_detial:sys):
    _,_,exc_tb=error_detial.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] Line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detial:sys):
        super().__init__(error_message)
        self.error_message=error_message_detial(error_message,error_detial=error_detial)

    def __str__(self):
        return self.error_message
    
