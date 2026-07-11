from services.google.search import search_google
from services.pubmed.search import search_pubmed
from services.companies.gsk import search_gsk

keyword = "Mo-Rez"

print("===================================")
print("Gary Medical Intelligence Assistant")
print("===================================")

search_google(keyword)

search_pubmed(keyword)

search_gsk(keyword)

print("Search Finished")
