from elasticsearch import Elasticsearch
import csv

def read_CID_input(file_path, dst_field_name):
    entities = {}
    with open(file_path) as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for pc_id, term in reader:
            if pc_id not in entities:
                entities[pc_id] = {}
            if "id" not in entities[pc_id]:
                entities[pc_id]["id"] = pc_id
                entities[pc_id][dst_field_name] = []
            entities[pc_id][dst_field_name].append(term)
    return entities

# enhance files idea (build json by single file and enhance it)
entities = read_CID_input("/home/kornel/data/pubchem/CID-Synonym-filtered-10k", "synonyms")

es = Elasticsearch("localhost:9200")
es.indices.create(index="pubchem", ignore=400)
print(es.indices)
for pc_id in entities.keys():
	es.index(index="pubchem", id=pc_id, body=entities[pc_id])