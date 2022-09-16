import csv

field_names = ['input variant', 'assembly name', 'seq_region_name', 'start', 'end', 'most_severe_consequnece', 'strand',
               'genes']

def write_output_file(output_path, data):
    with open(output_path, 'w') as output_file:
        writer = csv.DictWriter(output_file, delimiter='\t', fieldnames=field_names)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
