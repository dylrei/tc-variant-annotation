import sys

from .fetch import load_annotations
from .output import write_output_file
from .validation import validate_path, validate_sys_argv


def annotate_variants(input_path, output_path):
    validate_path(input_path, 'r')
    validate_path(output_path, 'w')
    variant_ids = load_variants(input_path)
    write_output_file(output_path=output_path, data=load_annotations(variant_ids))
    print(f'Success! Results stored in {output_path}')


def load_variants(input_path):
    with open(input_path, 'r') as file_handle:
        contents = file_handle.readlines()
        if not contents:
            raise RuntimeError(f'Specified input file {input_path} is empty')
        return contents


def main():
    validate_sys_argv(sys.argv)
    annotate_variants(input_path=sys.argv[1], output_path=sys.argv[2])
