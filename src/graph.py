import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from old import *

old_data = Graph()
old_data.debug_create_test_data()
print(old_data.vertexes)

N = 10
node_indices = list(range(N))

debug_pallete = Spectral8
debug_pallete.append('#ff0000')
debug_pallete.append('#0000ff')

plot = figure(title='Graph Layout Demonstration', x_range=(0,500), y_range=(0,500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(debug_pallete, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

graph.edge_renderer.data_source.data = dict(
    start=[0]*N,
    end=node_indices)

### start of layout code
#looks like this is setting the position of the vertexes 
# circ = [i*2*math.pi/N for i in node_indices]
x = [vertexes.pos['x'] for vertexes in old_data.vertexes]
y = [vertexes.pos['y'] for vertexes in old_data.vertexes]



graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)
 
plot.renderers.append(graph)

output_file('graph.html')
show(plot)