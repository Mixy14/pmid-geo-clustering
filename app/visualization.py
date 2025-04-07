import plotly.express as px

def plot_clusters(reduced, labels, pmid_links):
    fig = px.scatter(
        x=reduced[:, 0],
        y=reduced[:, 1],
        color=labels.astype(str),
        hover_name=pmid_links,
        title="GEO Dataset Clusters"
    )
    fig.write_html("app/templates/plot.html", auto_open=False)
