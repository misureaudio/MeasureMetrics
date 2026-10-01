# -*- coding: utf-8 -*-
"""Headless execution of the notebook against the workspace venv kernel."""
import json, os, tempfile, pathlib, time
NB = pathlib.Path(r"D:/Source/hermes-dir/MeasureMetrics/measure-metrics-distance-essay_notebook.ipynb")
VENV_PY = r"D:\Source\hermes-dir\.venv\Scripts\python.exe"

spec_root = tempfile.mkdtemp(prefix="jdata_")
kdir = os.path.join(spec_root, "kernels", "venv-py")
os.makedirs(kdir)
with open(os.path.join(kdir, "kernel.json"), "w") as f:
    json.dump({"argv": [VENV_PY, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
               "display_name": "venv-py", "language": "python",
               "env": {"MPLBACKEND": "Agg"}}, f)
os.environ["JUPYTER_DATA_DIR"] = spec_root

import nbclient, nbformat
from nbformat import read
nb = read(str(NB), as_version=4)
client = nbclient.NotebookClient(nb, kernel_name="venv-py", timeout=1800)
t0 = time.time()
client.execute()
nbformat.write(nb, str(NB))
print("executed OK in %.1f s" % (time.time()-t0))
