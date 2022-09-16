import requests

from ..util import validate_api_response

base_url = 'http://rest.ensembl.org/vep/human/hgvs/%(variant_id)s'
headers = {'Content-type': 'application/json'}


def load_variant_annotations(variant_ids):
    output = list()
    for variant_id in variant_ids:
        url = base_url % {'variant_id': variant_id}
        response = requests.get(url, headers=headers)
        validate_api_response(response)
        variant_annotations = response.json()[0]
        output.append({
            'input variant': variant_annotations['input'],
            'assembly name': variant_annotations['assembly_name'],
            'seq_region_name': variant_annotations['seq_region_name'],
            'start': variant_annotations['start'],
            'end': variant_annotations['end'],
            'most_severe_consequnece': variant_annotations['most_severe_consequence'],
            'strand': variant_annotations['strand'],
            'genes': [g['gene_symbol'] for g in variant_annotations['transcript_consequences']],
        })
    return output
