import basic

print('Durt 1.0.0 type q() to exit')
while True:
    text = input('> ')
    result, error = basic.run(text)
    if error: print(error.as_string())
    else: print(result)
    
