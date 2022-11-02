try:
    raise ExceptionGroup("Exception Group for multiple errors", (
        ValueError("This is a value error"),
        TypeError("This is a type error"),
        KeyError("This is a Key error"),
        AttributeError('This is an Attribute Error'),
        AttributeError('This is another Attribute Error')
    ))

except* AttributeError as err:
    raise err
except* (ValueError, TypeError) as err:
    raise err
except* KeyError as err:
    raise err
