"""Domain Model of Calc."""


def validate_number(result, number):
    """Validate if the number and join it with the previous result."""
    if number == ',' and len(result) == 0:
        result = '0,0' + result
    else:
        result = '{}{}'.format(result, str(number))
    return result


def do_calculation(calculation):
    """Execute the calculator."""
    result = str(calculation).replace(',', '.')
    result = eval(result)
    result = str(result)
    if len(result) > 2 and result[-2:] == '.0':
        result = result[:-2]
    result = result.replace('.', ',')
    return str(result)
