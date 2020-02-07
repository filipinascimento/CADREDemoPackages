import os.path
import query2xnet
import xnet2wordcloud
import xnet2figure
import xnet2communities_wordcloud
import importlib

importlib.reload(query2xnet);
importlib.reload(xnet2wordcloud);
importlib.reload(xnet2figure);
importlib.reload(xnet2communities_wordcloud);

minYear = 2000
minKCore = 1
queryID = "ee732263-ef2b-4912-87c1-de0bd1b54a11";
workingDirectory = "demo_data"
queriesDirectory = os.path.join(workingDirectory,"query-results");
outputNetworkDirectory = os.path.join(workingDirectory,"networks");
outputFiguresDirectory = os.path.join(workingDirectory,"figures");

os.makedirs(outputNetworkDirectory, exist_ok=True)
os.makedirs(outputFiguresDirectory, exist_ok=True)

query2xnet.mag_query_input_to_xnet(
	os.path.join(queriesDirectory,"%s.csv"%queryID),
	os.path.join(queriesDirectory,"%s_edges.csv"%queryID),
	os.path.join(outputNetworkDirectory,"%s.xnet"%queryID)
)

xnet2wordcloud.xnet_input_to_wordcloud(
	os.path.join(outputNetworkDirectory,"%s.xnet"%queryID),
	os.path.join(outputFiguresDirectory,"%s_wordcloud.pdf"%queryID),
)

xnet2figure.xnet_input_to_figure(
	os.path.join(outputNetworkDirectory,"%s.xnet"%queryID),
	os.path.join(outputFiguresDirectory,"%s_vis.pdf"%queryID),
	minYear=minYear,
	minKCore=minKCore
)

xnet2communities_wordcloud.xnet_input_to_communities_wordcloud(
	os.path.join(outputNetworkDirectory,"%s.xnet"%queryID),
	os.path.join(outputFiguresDirectory,"%s_communities_wc.pdf"%queryID),
	minYear=minYear,
	minKCore=minKCore
)
