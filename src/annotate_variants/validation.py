import os


def validate_sys_argv(args):
    if len(args) != 3:
        raise RuntimeError(f'Wrong number of arguments; Example invocation:\n'
                           f'\tannotate-variants input_file_path.txt output_file_path.tsv')


def validate_api_response(response):
    if not response.ok:
        raise RuntimeError(f'Response ({response.status_code}): {response.text}')


def validate_path(path, mode):
    file_exists = os.path.exists(path)
    if mode == 'r':
        if not file_exists:
            raise RuntimeError(f'No such input file: {path}')
    elif mode == 'w':
        if file_exists:
            raise RuntimeError(f'Output file arleady exists: {path}')
    else:
        # just in case
        raise NotImplementedError(f'Unsupported file access mode: {mode}')
