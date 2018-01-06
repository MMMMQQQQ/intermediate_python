from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            return 'a {} wrapped up box of {}'.format(style,str(item()))
        return wrapped_item
    return add_wrapping

@add_wrapping_with_style('beautiful')
def new_gpu():
    return 'a new Tesla P100 GPU'

def new_bicycle():
    return 'a new bicycle'
print(new_gpu())
print(new_gpu.__name__)
print(new_bicycle.__name__)