from elasticsearch import Elasticsearch

es = Elasticsearch("localhost:9200")
#es.indices.create(index="pubchem", ignore=400)

print("*" * 80)

result = es.get(index="pubchem", id="200")
#result = es.search(index="pubchem", body={"query": {"multi_match": {"query": ".alpha.-Ribazole", "fields": ["*"]}}})

print(result)