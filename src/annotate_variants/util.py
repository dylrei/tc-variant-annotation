import os


def load_variants(input_path):
    _validate_path(input_path, 'r')
    with open(input_path, 'r') as file_handle:
        contents = file_handle.readlines()
        if not contents:
            raise RuntimeError(f'Specified input file {input_path} is empty')
        return contents


def load_output_file(output_path):
    _validate_path(output_path, 'w')
    with open(output_path, 'w') as file_handle:
        return file_handle


def validate_api_response(response):
    if not response.ok:
        raise RuntimeError(f'Response ({response.status_code}): {response.text}')


def _validate_path(path, mode):
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
