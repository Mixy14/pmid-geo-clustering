from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def build_text_corpus(dataset_list):
    corpus = []
    for d in dataset_list:
        combined = " ".join([
            d.get("title", ""),
            d.get("summary", ""),
            d.get("taxon", ""),
            d.get("overall_design", "")
        ])
        corpus.append(combined)
    return corpus

def tfidf_and_cluster(corpus, n_clusters=3):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(corpus)

    pca = PCA(n_components=2)
    reduced = pca.fit_transform(tfidf_matrix.toarray())

    model = KMeans(n_clusters=n_clusters)
    labels = model.fit_predict(reduced)

    return reduced, labels
