from .ensembl import load_variant_annotations as ensembl_loader

# In a future version, we may wish to specify source in a .env file and use a different loader
# Leave room for that when needed, for now just assume Ensembl
SOURCE = 'ensembl'

loader = {
    'ensembl': ensembl_loader,
}


def load_annotations(variant_ids):
    if SOURCE not in loader:
        raise RuntimeError(f'No loader configured for source {SOURCE}')
    return loader[SOURCE](variant_ids)
