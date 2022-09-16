from ..output import write_output_file


def test_write_output_file():
    variant_data = [{
        'input variant': 'NC_000006.12:g.152387156G>A',
        'assembly name': 'GRCh38',
        'seq_region_name': '6',
        'start': 152387156,
        'end': 152387156,
        'most_severe_consequnece': 'synonymous_variant',
        'strand': 1,
        'genes': ['SYNE1', 'SYNE1', 'SYNE1', 'SYNE1']
    }]
    expected_tsv_contents = "input variant\tassembly name\tseq_region_name\tstart\tend\tmost_severe_consequnece\t" \
                            "strand\tgenes\nNC_000006.12:g.152387156G>A\tGRCh38\t6\t152387156\t152387156\t" \
                            "synonymous_variant\t1\t[\'SYNE1\', \'SYNE1\', \'SYNE1\', \'SYNE1\']\n"

    write_output_file('test_output.tsv', variant_data)
    with open('test_output.tsv', 'r') as output_file:
        assert output_file.read() == expected_tsv_contents

