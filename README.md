# PubMed-GEO Dataset Clustering Tool

This tool takes PubMed PMIDs, finds associated GEO datasets, processes and clusters their descriptions using TF-IDF, and visualizes the results.

## Features
- Fetches GEO datasets using PubMed PMIDs
- Extracts metadata fields (Title, Summary, Taxon, Overall Design)
- Uses TF-IDF and KMeans to cluster dataset descriptions
- Provides an interactive 2D visualization of clusters
- Simple web interface with Flask

## Setup

1. Clone this repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the app:
   ```
   python app.py
   ```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

## Example Use
Paste one PMID per line and submit. You’ll see a scatter plot showing dataset clusters and their links to PMIDs.

---
MIT License
