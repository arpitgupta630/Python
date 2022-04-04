def divide(dividend, divisior):
    try:
        return dividend / divisior
    except ZeroDivisionError:
        return 'Can not divide any Value by Zero'
    except TypeError:
        return 'Can not divide String and numbers'

print(divide(4,0))
print(divide(4,3))
print(divide(9,'5'))