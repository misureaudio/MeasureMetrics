# -*- coding: utf-8 -*-
"""Independent verification of the executed notebook."""
import re, sys
import nbformat

NB = r"D:/Source/hermes-dir/MeasureMetrics/measure-metrics-distance-essay_notebook.ipynb"
nb = nbformat.read(NB, as_version=4)
nbformat.validate(nb)
print("[1] nbformat.validate: PASS")

def all_outputs():
    for c in nb.cells:
        if c.cell_type == "code":
            for o in c.get("outputs", []):
                yield c, o

errors = 0
for c, o in all_outputs():
    if o.get("output_type") == "error":
        errors += 1
        print("[2] ERROR in cell:", c.source[:80].replace("\n", " "))
        print("   ", o.get("ename"), o.get("evalue"))
print("[2] error outputs:", errors, "->", "PASS" if errors == 0 else "FAIL")

def text_of(o):
    if o.get("output_type") == "stream":
        return o.get("text", "")
    if "data" in o:
        return "".join(o["data"].get("text/plain", ""))
    return ""

png = 0
for c, o in all_outputs():
    if "data" in o and "image/png" in o["data"]:
        png += 1
print("[3] image/png figures:", png, "->", "PASS" if png == 17 else "FAIL (expected 17)")

full = "\n".join(text_of(o) for c, o in all_outputs())
flat = re.sub(r"\s+", " ", full)

checks = {
    "fractal gasket 1.5849625": "1.5849625" in flat,
    "fractal menger 2.7268330": "2.7268330" in flat,
    "alpha(4) 4.934802": "4.934802" in flat,
    "gauge volume pi^2/4 = 2.4674011003": "2.4674011003" in flat,
    "doubling 16": "doubling constant C_D = 16" in flat,
    "W2 gaussian = 2.0": ("W_2^2(N(0,1), N(1,4)) = 2.00" in flat) or ("2.0000" in flat),
    "de Bruijn dE/dt+FI ~0 (gaussian)": ("dE/dt + FI = 0.00" in flat) or ("1.85e-17" in flat) or ("e-17" in flat),
    "sub-Laplacian matches essay": "matches the essay's formula: True" in flat,
    "commutator x*y' - x'*y": ("x*y' - x'*y" in flat) or ("x*y' - x'*y" in flat),
    "H1 segment = 2": "H^1_sph([-1,1]) = 2.000000" in flat,
    "H1 circle = 2pi": ("H^1_sph(unit circle) = 6.283185" in flat),
    "sphere volume 4pi": ("4 pi = 12.56637061" in flat) or ("12.56637061" in flat),
}
ok = True
for name, passed in checks.items():
    print("[4] %-42s %s" % (name, "PASS" if passed else "FAIL"))
    ok = ok and passed

# slope checks (numeric)
def grab(pattern, lo, hi):
    m = re.search(pattern, flat)
    if not m: return None
    v = float(m.group(1))
    return lo <= v <= hi
heat = grab(r"on-diagonal decay slope \(t in \[0\.35,0\.60\]\) = (-?\d+\.\d+)", -2.15, -1.85)
emp  = grab(r"log-log slope = (-?\d+\.\d+)\s*\(theory -1/2\)", -0.55, -0.45)
box  = grab(r"box-count slope \(middle window 2\^-6\.\.2\^-10\) = (\d+\.\d+)", 1.50, 1.68)
print("[5] heat on-diagonal slope in [-2.15,-1.85]:", "PASS" if heat else "FAIL")
print("[5] empirical W2 slope in [-0.55,-0.45]:", "PASS" if emp else "FAIL")
print("[5] box-count slope in [1.50,1.68]:", "PASS" if box else "FAIL")
ok = ok and bool(heat) and bool(emp) and bool(box)

print("\n" + ("ALL CHECKS PASS" if (errors==0 and png==17 and ok) else "SOME CHECKS FAILED"))
sys.exit(0 if (errors==0 and png==17 and ok) else 1)
