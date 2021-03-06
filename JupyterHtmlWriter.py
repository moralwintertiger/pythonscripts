###Author: https://nipunbatra.github.io/blog/2017/Jupyter-powered-blog.html


import sys
from nbconvert import HTMLExporter
import nbformat

##define notebook_file using your file name (...ipynb)

notebook_file = sys.argv[1]
html_exporter = HTMLExporter()
nb = nbformat.reads(open(notebook_file, 'r').read(), as_version=4)

(body, resources) = html_exporter.from_notebook_node(nb)
html_file = notebook_file.replace(".ipynb", ".html")
html_file_writer = open(html_file, 'w')
html_file_writer.write(body)
html_file_writer.close()
