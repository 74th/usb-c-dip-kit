import os
from invoke import task

@task(default=True)
def package(c, n=""):
    if n == "":
        n = os.path.basename(os.path.abspath("."))
    c.run("rm -rf order/*", warn=True)
    c.run(f"cp plot/{n}-F_Cu.gbr order/{n}.GTL")
    c.run(f"cp plot/{n}-B_Cu.gbr order/{n}.GBL")
    c.run(f"cp plot/{n}-F_Mask.gbr order/{n}.GTS")
    c.run(f"cp plot/{n}-B_Mask.gbr order/{n}.GBS")
    c.run(f"cp plot/{n}-F_Silkscreen.gbr order/{n}.GTO")
    c.run(f"cp plot/{n}-B_Silkscreen.gbr order/{n}.GBO")
    c.run(f"cp plot/{n}-PTH.drl order/{n}.TXT")
    c.run(f"cp plot/{n}-NPTH.drl order/{n}-NPTH.TXT")
    c.run(f"cp plot/{n}-Edge_Cuts.gbr order/{n}.GML")
    with c.cd("order"):
        c.run(f"zip _.zip {n}*")
        c.run(f"mv _.zip {n}.zip")
