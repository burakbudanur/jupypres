from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.patches import FancyArrowPatch, Circle
import matplotlib as mpl
import numpy as np 
from IPython.display import Video

current_figure = None

def slide(layout, size=(16, 9), title=None):

    global current_figure

    sl = plt.figure(figsize=size, FigureClass=Slide).subplot_mosaic(layout)
    fig = plt.gcf()

    empty   = ['E', 'F', 'G', 'H']
    text    = ['T', 'U', 'V', 'W']

    for label in sl:
        if (label in empty + text):
            sl[label].axis("off")
        else: 
            sl[label].tick_params(labelsize=16)
    
    if title:
        fig.suptitle("\n"+title+"\n", fontsize=36, linespacing=0.25)

    current_figure = fig

    return sl


def duplicate_slide():

    global current_figure

    fig = current_figure 
    slide = {}
    

    for ax in fig.axes:
        slide[ax.get_label()] = ax

    return slide, fig


def show():

    plt.show()


def cross(ax, x, y, length=1.0, lw=1.0, color='red', yscale=1.0):

    ax.plot(np.array([x - length, x + length]), 
            np.array([y - length, y + length]) * yscale, 
            color=color, lw=lw)

    ax.plot(np.array([x + length, x - length]), 
            np.array([y - length, y + length]) * yscale,
            color=color, lw=lw)


def circle(ax, x, y, scale = 1.0, color='red', **kwargs):

    c = Circle((x,y), scale, edgecolor=color, facecolor='none', **kwargs)
    ax.add_patch(c)


def arrow(ax, x, y, 
angle=0, scale=1.0, mutation_scale=10, color='red', lw=4.0, arrowstyle='-|>'): 

    angle = (angle / 180) * np.pi 

    arr = FancyArrowPatch((x, y), 
                          (x + scale * np.cos(angle), 
                           y + scale * np.sin(angle)),
                          mutation_scale=mutation_scale,
                          facecolor=color,
                          edgecolor=color,
                          arrowstyle=arrowstyle,
                          lw=lw
                          )
    ax.add_patch(arr)



def image(ax, fname):

    ax.imshow(mpl.image.imread(fname))


def center_text(ax, x, y, text, fontsize=24, color='black'):

    ax.text(x, y, text, 
            fontsize=fontsize, 
            horizontalalignment="center", 
            verticalalignment="center", 
            color=color)

def left_text(ax, x, y, text, fontsize=24, color='black'):
    
    ax.text(x, y, text, 
            fontsize=fontsize, 
            horizontalalignment="left", 
            verticalalignment="center", 
            color=color)


Video = Video

class Slide(Figure):
    """
    See:
    ---------
    matplotlib.pyplot.figure
    """

    