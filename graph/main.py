from matplotlib import pyplot
import pandas as pd
from matplotlib.ticker import LogLocator
import re

def sizename(e):
    if e<1e3:
        return "%d" % e
    if e<1e4:
        return "%.1fk" % (e*1e-3)
    if e<1e6:
        return "%.1fk" % (e*1e-3)
    if e<1e7:
        return "%dM" % (e*1e-6)
    if e<1e9:
        return "%dM" % (e*1e-6)

def graph(src, title, dest):
    pyplot.style.use("ggplot")
    csv = pd.read_csv(src)
    r = range((len(csv.keys())-1)//2)
    names = [ [
        csv.keys()[i*2+2], csv.keys()[i*2+1] ] for i in r ]
    print( names )
    fig, ax = pyplot.subplots()
    ax.set_xscale('log', base=10)
    ax.xaxis.set_major_formatter(lambda e, pos: sizename(e))

    ax.set_yscale('log', base=2)
    ax.yaxis.set_major_formatter(lambda e, pos: ("%d" % e))
    # ax.yaxis.set_minor_locator(LogLocator(base=2))
    # ax.yaxis.set_major_locator(LogLocator(base=2))
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


def main():
    for fn in ["a", "voro"]:
        graph(fn+".csv", fn, fn+".png")


main()
