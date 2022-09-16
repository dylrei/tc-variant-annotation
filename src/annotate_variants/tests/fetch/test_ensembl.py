from unittest.mock import patch

import pytest

from ..mocks import mock_requests_get
from ...fetch.ensembl import load_variant_annotations


@patch('requests.get', side_effect=mock_requests_get)
def test_load_variant_annotations(_):
    happy_path_test_cases = [
        {
            'variant': 'NC_000001.11:g.215674515G>A',
            'expected_output': [
                {
                    'input variant': 'NC_000001.11:g.215674515G>A',
                    'assembly name': 'GRCh38',
                    'seq_region_name': '1',
                    'start': 215674515,
                    'end': 215674515,
                    'most_severe_consequnece': 'missense_variant',
                    'strand': 1,
                    'genes': ['USH2A', 'USH2A']
                }
            ]
        },
        {
            'variant': 'NC_000001.11:g.40819893G>A',
            'expected_output': [{'input variant': 'NC_000001.11:g.40819893G>A', 'assembly name': 'GRCh38', 'seq_region_name': '1', 'start': 40819893, 'end': 40819893, 'most_severe_consequnece': 'missense_variant', 'strand': 1, 'genes': ['KCNQ4', 'KCNQ4', 'KCNQ4', 'KCNQ4']}]
        },
        {
            'variant': 'NC_000002.12:g.39006443C>T',
            'expected_output': [{'input variant': 'NC_000002.12:g.39006443C>T', 'assembly name': 'GRCh38', 'seq_region_name': '2', 'start': 39006443, 'end': 39006443, 'most_severe_consequnece': 'synonymous_variant', 'strand': 1, 'genes': ['SOS1', 'SOS1', 'SOS1', 'SOS1', 'SOS1', 'SOS1', 'SOS1', 'SOS1', 'SOS1', 'SOS1', 'SOS1']}]
        },
        {
            'variant': 'NC_000006.12:g.152387156G>A',
            'expected_output': [{'input variant': 'NC_000006.12:g.152387156G>A', 'assembly name': 'GRCh38', 'seq_region_name': '6', 'start': 152387156, 'end': 152387156, 'most_severe_consequnece': 'synonymous_variant', 'strand': 1, 'genes': ['SYNE1', 'SYNE1', 'SYNE1', 'SYNE1']}]
        },
        {
            'variant': 'NC_000001.11:g.215674515G>A',
            'expected_output': [{'input variant': 'NC_000001.11:g.215674515G>A', 'assembly name': 'GRCh38', 'seq_region_name': '1', 'start': 215674515, 'end': 215674515, 'most_severe_consequnece': 'missense_variant', 'strand': 1, 'genes': ['USH2A', 'USH2A']}]
        },
    ]
    for tc in happy_path_test_cases:
        assert load_variant_annotations([tc['variant']]) == tc['expected_output']

    error_raising_cases = ['NC_000001.11:g.40819893T>A']
    for erc in error_raising_cases:
        with pytest.raises(Exception) as exc_info:
            load_variant_annotations([erc])
        assert 'Unable to parse HGVS notation' in str(exc_info)
