from matplotlib import pyplot
import pandas as pd
from matplotlib.ticker import LogLocator
import re

colmap = {"jpeg":"black", "webp":"blue", "jp2":"#0a0", "avif":"red" }

def numstr(e):
    if abs(e-round(e))<0.01:
        return "%d" % e
    return "%.2f" % e

def sizename(e):
    if e==0:
        return "0"
    if e<1:
        return "1/"+numstr(1/e)
    else:
        return numstr(e)

def diffname(e):
    if e==int(e):
        return "%d" % e
    return "1/%d" % (1/e)

def sizename_h(e):
    if e==0:
        return "0"
    return "%d%%" % (e*100)

def diffname_h(e):
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
    for xn, yn in names:
        print(xn,yn)
        ax.set_title(title)
        label = label=xn.split("_")[0]
        col = colmap[label]
        ax.plot(csv[xn], csv[yn], label=label, color=col)
        ix=0
        for i in [1,50,75,90,99]:
            ax.scatter(csv[xn][(i-1):i], csv[yn][(i-1):i], zorder=2, s=[100,25][ix], color=col)
            ix ^= 1

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
    ax.xaxis.set_major_formatter(lambda e, pos: sizename_h(e))

    ax.set_xlabel('file size (ratio to PNG)')
    ax.set_ylabel('average pixel value error')

    ax.yaxis.set_major_formatter(lambda e, pos: diffname_h(e))
    for xn, yn in names:
        print(xn,yn)
        ax.set_title(title)
        label = label=xn.split("_")[0]
        col = colmap[label]
        ax.plot(csv[xn], csv[yn], label=label, color=col)
        ax.scatter(csv[xn][1:], csv[yn][1:], zorder=2, s=100, color=col)
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
