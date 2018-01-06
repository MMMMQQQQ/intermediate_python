import sys
import logging

def error_handling():
    return ' {}. {}, line:{}'.format(sys.exc_info()[0],
                                          sys.exc_info()[1],
                                          sys.exc_info()[2].tb_lineno)

# it will return the traceback object, and it is the real error that we are looking for
try:
    a+b
except Exception as e:
    # print(sys.exc_info()[0])
    # print(sys.exc_info()[1])
    # print(sys.exc_info()[2].tb_lineno)
    # print('Error: {}. {}, line:{}'.format(sys.exc_info()[0],
    #                                       sys.exc_info()[1],
    #                                       sys.exc_info()[2].tb_lineno))
    logging.error(error_handling())