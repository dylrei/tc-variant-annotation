## Challenge Response

### Overview
This package installs a command line utility that fetches variant annotation data and saves them in a TSV.

### Setup / Installation
Install this package from its git repository:
```shell
python -m pip install git+https://github.com/dylrei/tc-variant-annotation.git
```

### Usage
```shell
annotate-variants input_file_path.txt output_file_path.tsv
```
HGVS identities should be listed one-per-line in `input_file.txt`. An error will be raised if `output_file_path.tsv` exists.

### Examples
Create a TSV with variant annotations for valid HGVS identifiers:
```shell
annotate-variants valid_variants.txt output.tsv
```

Include an invalid HGVS to see how errors are handled:
```shell
annotate-variants error_variants.txt not_used.tsv
```