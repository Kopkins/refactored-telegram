import os

class text_util:
    #clear console so that printing looks clean
    clear_console = lambda: os.system('clear')

    # setup printing of colored items
    print_active = lambda s: print('[1;44m{}[1;m'.format(s))
    print_error = lambda s: print('[1;41m{}[1;m'.format(s))

    error_string = lambda s: '[1;41m{}[1;m'.format(s)

    # status printing
    status_begin = lambda s: print(s, '... ', sep='', end='', flush=True)
    status_done = lambda: print('DONE')
    status_fail = lambda: print('FAILED')
