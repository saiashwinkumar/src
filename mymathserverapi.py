# Do not run this file directly



from flask import make_response, abort

import mymathlib



def invoke(operation, arg1=0, arg2=0):
    
    print('mymathserverapi.invoke: operation={}, arg1={}, arg2={}'.format(operation, arg1, arg2))

    if operation == 'power':

        result = mymathlib.power(arg1, arg2)

        return {'result': result}

    elif operation == 'factorial':

        try:

            result = mymathlib.factorial(int(arg1))
            return {'result': result}
        
        except (mymathlib.NonIntegerException, mymathlib.NegativeIntegerException) as ex:

            abort(400, 'Unable to invoke {}: {}'.format(operation, ex.args[0]))
    
    elif operation == 'fibonacci':

        try:

            result = mymathlib.fibonacci(int(arg1))
            return {'result': result}
        
        except (mymathlib.NonIntegerException, mymathlib.NegativeIntegerException) as ex:

            abort(400, 'Unable to invoke {}: {}'.format(operation, ex.args[0]))

    else:

        abort(404, 'Invalid operation {}'.format(operation))
