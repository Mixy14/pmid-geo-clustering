import requests
from bs4 import BeautifulSoup

def fetch_gse_ids_for_pmid(pmid):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi"
    params = {
        "dbfrom": "pubmed",
        "db": "gds",
        "linkname": "pubmed_gds",
        "id": pmid,
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, "xml")
    gse_ids = [id_tag.text for id_tag in soup.find_all("Id")]
    return gse_ids

def fetch_gse_metadata(gse_id):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    params = {
        "db": "gds",
        "id": gse_id,
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, "xml")
    doc = soup.find("DocSum")
    
    metadata = {}
    for item in doc.find_all("Item"):
        name = item.get("Name")
        if name in ["title", "summary", "taxon", "overall_design", "gse"]:
            metadata[name] = item.text
    return metadata
