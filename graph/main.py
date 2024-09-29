from matplotlib import pyplot
import pandas as pd
from matplotlib.ticker import LogLocator
import re

def sizename(e):
    if e==0:
        return "0"
    return "%d%%" % (e*100)

def diffname(e):
    if e==0:
        return "0"
    return "%.2f" % e

def graph(src, title, dest):
    pyplot.style.use("ggplot")
    csv = pd.read_csv(src)
    r = range((len(csv.keys())-1)//2)
    names = [ [
        csv.keys()[i*2+2], csv.keys()[i*2+1] ] for i in r ]
    print( names )
    fig, ax = pyplot.subplots()
    ax.set_xscale('log', base=2)
    ax.xaxis.set_major_formatter(lambda e, pos: sizename(e))

    ax.set_xlabel('file size (ratio to PNG)')
    ax.set_ylabel('average pixel value error')

    ax.set_yscale('log', base=2)
    ax.yaxis.set_major_formatter(lambda e, pos: diffname(e))
    # ax.yaxis.set_minor_locator(LogLocator(base=2))
    # ax.yaxis.set_major_locator(LogLocator(base=2))
    if title=="turtle":
        ax.set_xlim(0.45,1.1)
    for xn, yn in names:
        print(xn,yn)
        ax.set_title(title)
        ax.plot(csv[xn], csv[yn], label=xn.split("_")[0])
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.savefig(dest)
    # ax.barh(x, y0, color="red", align="edge", height=0.4)
    # ax.barh(x, y1, color="blue", align="edge", height=-0.4)
    # ax.set_yticklabels(ax.get_yticklabels(), fontsize=10)
    # print(data_fns, title, fn)

def hgraph(src, title, dest):
    pyplot.style.use("ggplot")
    csv = pd.read_csv(src)
    r = range((len(csv.keys())-1)//2)
    names = [ [
        csv.keys()[i*2+2], csv.keys()[i*2+1] ] for i in r ]
    print( names )
    fig, ax = pyplot.subplots()
    ax.xaxis.set_major_formatter(lambda e, pos: sizename(e))

    ax.set_xlabel('file size (ratio to PNG)')
    ax.set_ylabel('average pixel value error')

    ax.yaxis.set_major_formatter(lambda e, pos: diffname(e))
    if title=="turtle":
        ax.set_xlim(0.45,1.1)
    for xn, yn in names:
        print(xn,yn)
        ax.set_title(title)
        ax.plot(csv[xn], csv[yn], label=xn.split("_")[0])
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.savefig(dest)

images = ["jfish", "ham", "voro", "cloud", "turtle", "dog"]

def loq():
    for fn in images:
        graph(fn+".csv", fn, "charts/"+fn+".png")

def hiq():
    for fn in images:
        hgraph("hiq_"+fn+".csv", fn, "charts/h_"+fn+".png")

loq()
hiq()
