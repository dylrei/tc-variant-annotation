import pytest

from ..tests.mocks import MockResponse
from ..validation import validate_sys_argv, validate_api_response, validate_path


def test_validate_sys_argv():
    valid_args = ['_', 'input/file/path.txt', 'output/file/path.txt']
    invalid_cases = [
        ['_', 'input/file/path.txt'],
        ['_', 'input/file/path.txt', 'output/file/path.txt', '-unsupported_option']
    ]

    assert validate_sys_argv(valid_args) is None

    for invalid_case in invalid_cases:
        with pytest.raises(Exception) as exc_info:
            validate_sys_argv(invalid_case)
        assert 'Wrong number of arguments' in str(exc_info)


def test_validiate_api_response():
    error_message = 'this is an error message'
    valid_response = MockResponse({'data': 'anything but an error'})
    invalid_response = MockResponse({'error': error_message})

    assert validate_api_response(valid_response) is None

    with pytest.raises(Exception) as exc_info:
        validate_api_response(invalid_response)
    assert error_message in str(exc_info)


def test_validate_path():
    existing_files = ['valid_variants.txt', 'error_variants.txt']
    non_existing_files = ['bogus_file.txt', 'valid_variants.tsv', 'valid_variants']

    for existing_path in existing_files:
        assert validate_path(existing_path, 'r') is None
        with pytest.raises(Exception) as exc_info:
            validate_path(existing_path, 'w')
        assert 'Output file arleady exists' in str(exc_info)

    for non_existing_path in non_existing_files:
        assert validate_path(non_existing_path, 'w') is None
        with pytest.raises(Exception) as exc_info:
            validate_path(non_existing_path, 'r')
        assert 'No such input file' in str(exc_info)
