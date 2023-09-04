def compile_and_print_msg(msg_args: list[str], do_print: bool):
    ''' Method to join LIST of strings and print it to the console '''
    compiled_msg = ' '.join(msg_args)
    if do_print:
        print(compiled_msg)
    else:
        return compiled_msg