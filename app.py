from flask import Flask, request, render_template
from app.api import fetch_gse_ids_for_pmid, fetch_gse_metadata
from app.processing import build_text_corpus, tfidf_and_cluster
from app.visualization import plot_clusters

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pmid_text = request.form["pmids"]
        pmid_list = pmid_text.strip().split()
        all_datasets = []
        pmid_links = []

        for pmid in pmid_list:
            gse_ids = fetch_gse_ids_for_pmid(pmid)
            for gse_id in gse_ids:
                metadata = fetch_gse_metadata(gse_id)
                all_datasets.append(metadata)
                pmid_links.append(f"PMID:{pmid} → GSE:{gse_id}")

        corpus = build_text_corpus(all_datasets)
        reduced, labels = tfidf_and_cluster(corpus)
        plot_clusters(reduced, labels, pmid_links)

        return render_template("plot.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
