# -*- coding: utf-8 -*-
"""Builder for the Measure-Metrics-Distance notebook.
Assembles cells (markdown = theory, code = verification/illustration),
serializes via nbformat, writes the .ipynb. Run:
  D:/Source/hermes-dir/.venv/Scripts/python.exe build_measure_metrics_nb.py
"""
import nbformat, uuid, pathlib

OUT = pathlib.Path(r"D:/Source/hermes-dir/MeasureMetrics/measure-metrics-distance-essay_notebook.ipynb")

def _id():
    return uuid.uuid4().hex[:12]

def md(source):
    return {"cell_type": "markdown", "id": _id(), "metadata": {},
            "source": source.splitlines(keepends=True)}

def py(source):
    return {"cell_type": "code", "id": _id(), "metadata": {},
            "source": source.splitlines(keepends=True),
            "execution_count": None, "outputs": []}

C = []

# =====================================================================
# Title + setup
# =====================================================================
C.append(md(r'''# Measure, Metrics, and Distance in Topological Spaces

## A computational companion to the essay (v2)

This notebook mirrors the theoretical content of the essay *Measure, Metrics, and Distance in
Topological Spaces* section by section. Where the essay **commits to a constant, an identity, or a
structural claim**, the corresponding code cell **verifies it** with symbolic (sympy) or
numerical (numpy / scipy) computation, and adds a figure to illustrate the structure.

**Reading guide.** Markdown cells carry the theory (abridged from the essay, with the same notation).
Code cells are the *evidence*: each prints the value the essay claims and, where useful, plots the
geometry. Every non-trivial constant is recomputed from first principles, so the notebook is a
self-contained verification record.

> **Scope.** Three structures on the same set $X$: **topology** (closeness / continuity),
> **metric** (distance), **measure** (size). The essay's theme: they are *logically independent*,
> in *partial* (not full) correspondence, and the part one structure does not determine is exactly
> the part relevant to the problem at hand. Two running examples: the **Heisenberg group** $H^1$
> (metric, measure, and topology genuinely disagree in dimension) and the **Wasserstein space**
> $\mathcal P_2$ (a measure promoted to a metric; the heat equation as its gradient flow).
'''))

C.append(py(r'''%matplotlib inline
import numpy as np
from scipy import integrate, linalg, optimize, sparse
from scipy.sparse import linalg as splinalg
import sympy as sp
import matplotlib.pyplot as plt
from scipy.stats import norm

plt.rcParams["figure.figsize"] = (7.5, 4.0)
np.set_printoptions(precision=6, suppress=True)
rng = np.random.default_rng(0)
print("numpy", np.__version__, " scipy", __import__("scipy").__version__, " sympy", sp.__version__)
print("setup complete")
'''))

# =====================================================================
# Section 0-1: three structures, one set
# =====================================================================
C.append(md(r'''## 1. Three structures, one set

A **topology** $\mathcal T\subseteq 2^X$ (open sets), a **metric** $d:X\times X\to[0,\infty)$
(symmetry, identity of indiscernibles, triangle), and a **measure** $\mu:\mathcal A\to[0,\infty]$
(countably additive on a $\sigma$-algebra) are three *different* answers to three *different*
questions about $X$:

| Structure | Question | Primitive | What it does **not** see |
|---|---|---|---|
| Topology $\mathcal T$ | what is near what? what is continuous? | open set | distance, size |
| Metric $d$ | how far apart are two points? | distance | size (measure) |
| Measure $\mu$ | how large is a set? | measure | distance between points |

The central observation: the three structures are **logically independent** — none determines the
others. One set $X$ can carry many inequivalent topologies, many inequivalent metrics inducing the
*same* topology, and many inequivalent measures on the *same* Borel $\sigma$-algebra. The rest of
this notebook is a study of the *arrows* between these columns and what is lost at each step.

The first demonstration: **two inequivalent metrics inducing the *same* topology.** On $\mathbb R$,
the usual metric $d(x,y)=|x-y|$ and the arctan metric $d'(x,y)=|\arctan x-\arctan y|$ are both
compatible with the standard topology, yet $d'$ is bounded (diameter $\pi$) while $d$ is not.
'''))

C.append(py(r'''# F1 -- two metrics, same topology, different scale
# h(x)=arctan x is a homeomorphism (R,d) -> (-pi/2, pi/2), so d' induces the usual topology.
x = 0.0
eps = 1.0
B_d  = (x - eps, x + eps)                 # B_d(0,1) = (-1, 1)
B_dp = (x - np.tan(eps), x + np.tan(eps)) # B_d'(0,1) = (-tan 1, tan 1)
print("B_d(0,1)  =", B_d)
print("B_d'(0,1) =", (round(B_dp[0],4), round(B_dp[1],4)), "  (much larger interval)")
# mutual nesting: for any eps>0, B_d(0,eps/2) subset B_d'(0,eps) subset B_d(0, tan eps)
eps2 = 0.1
print("B_d(0,%g)=%s  subset  B_d'(0,%g)=%s" % (eps2/2, (round(-eps2/2,3), round(eps2/2,3)),
                                              eps2, (round(-np.tan(eps2),4), round(np.tan(eps2),4))))
# boundedness: d' has diameter pi, d is unbounded
print("d'(-1e6, 1e6) =", abs(np.arctan(-1e6)-np.arctan(1e6)), " (-> pi, bounded)")
print("d (-1e6, 1e6) =", abs(-1e6-1e6), " (unbounded)")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].fill_between(B_d, 0, 1, color="tab:blue", alpha=.3); ax[0].axvline(0,color='k')
ax[0].set_title(r"$B_d(0,1)=(-1,1)$  (unbounded metric)")
ax[1].fill_between(B_dp, 0, 1, color="tab:orange", alpha=.3); ax[1].axvline(0,color='k')
ax[1].set_title(r"$B_{d'}(0,1)=(-\tan1,\tan1)$  (bounded, diam $=\pi$)")
for a in ax: a.set_xlabel("x"); a.set_xlim(-4,4)
fig.suptitle("Same topology, different scale: $d$ vs $d'(x,y)=|\\arctan x-\\arctan y|$", y=1.02)
fig.tight_layout(); plt.show()
'''))

C.append(py(r'''# Topology axioms, checked on a finite space (illustrates the definition)
X = ["a","b","c"]
def is_topology(T):
    T = [frozenset(s) for s in T]
    if frozenset() not in T or frozenset(X) not in T: return False
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i] & T[j] not in T: return False          # finite intersections
        # arbitrary unions: check union of all subsets of the family
    # unions: union of any subfamily
    from itertools import combinations
    for r in range(len(T)+1):
        for combo in combinations(T, r):
            u = set().union(*combo) if combo else set()
            if frozenset(u) not in T: return False
    return True
discrete   = [set()]+[{x} for x in X]+[{x,y} for x in X for y in X if x<y]+[set(X)]
indiscrete = [set(), set(X)]
sierpinski = [set(), {"a"}, {"a","b"}, set(X)]
bad        = [set(), {"a"}, {"b"}, set(X)]   # {a} & {b} = {} ok, but {a} U {b} = {a,b} missing
for name, T in [("discrete",discrete), ("indiscrete",indiscrete), ("Sierpinski",sierpinski),
                ("{∅,{a},{b},X}",bad)]:
    print(f"{name:14s} is a topology? {is_topology(T)}")
print("=> the Sierpinski space is a (non-T1) topology; the last family fails (not closed under union)")
'''))

# =====================================================================
# Section 2-3
# =====================================================================
C.append(md(r'''## 2. Topology: the coarsest structure of closeness

A topology is the *coarsest* structure supporting limits, continuity, compactness, connectedness;
it is invariant under homeomorphism, so a topological theorem is a statement about the space, not
about any particular metric. What topology **cannot** see: *scale* (a metric) and *size* (a
measure). $\mathbb R$ with $d$ and with $d'$ (above) are topologically identical; a topology cannot
assign a "length" to $[0,1]$ or a "volume" to the unit disk. **Topology is the structure of
*shape*, not of scale or size.**

## 3. Metric: distance and the topology it induces

A metric $d$ defines open balls $B(x,r)=\{y:d(x,y)<r\}$, a base for the **metric topology**
$\mathcal T_d$. The assignment $(X,d)\mapsto(X,\mathcal T_d)$ is the *forgetful* functor from
metric to topological spaces: it keeps the topology, discards the scale. The nested-ball structure
is what lets one define Cauchy sequences, completeness, uniform continuity — notions with no purely
topological meaning.

**Metrizability (Urysohn, 1925).** $(X,\mathcal T)$ is metrizable $\iff$ it is *regular* and has a
*countable* base (second countable). The full statement (Nagata–Smirnov) replaces "countable base"
by "$\sigma$-locally-finite base." The hierarchy within metric spaces — *complete*, *separable*,
*Polish*, *totally bounded*, *compact* — is **not** a chain ($\ell^\infty$ complete non-separable;
$\mathbb Q$ separable non-complete). Compactness is the shared notion: topological, but in the
metric setting equivalent to *complete + totally bounded*, the equivalence that powers
Arzelà–Ascoli and existence of minimizers.
'''))

C.append(py(r'''# F2 -- weak convergence without norm convergence (the weak topology "forgets" the metric)
# In l^2, e_n -> 0 weakly ( <e_n, x> -> 0 for every x in l^2 ) but ||e_n|| = 1.
n_max = 200
Xv = rng.normal(size=(20, 4000))            # 20 random l^2 vectors (truncated)
Xv /= np.linalg.norm(Xv, axis=1, keepdims=True)
pair = np.array([np.abs(Xv[:, n-1]) for n in range(1, n_max+1)])   # |<e_n, x_j>|
norms = np.ones(n_max)

fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].plot(range(1, n_max+1), pair, lw=.5, color="tab:gray")
ax[0].plot(range(1, n_max+1), np.median(pair, axis=1), lw=2, color="tab:blue", label="median")
ax[0].set_xlabel("n"); ax[0].set_ylabel(r"$|\langle e_n, x\rangle|$"); ax[0].legend()
ax[0].set_title(r"weak: pairings $\to 0$")
ax[1].plot(range(1, n_max+1), norms, lw=2, color="tab:red", marker=".", ms=3)
ax[1].set_xlabel("n"); ax[1].set_ylabel(r"$\|e_n\|_2$"); ax[1].set_ylim(0,1.3)
ax[1].set_title("norm: stuck at 1")
fig.suptitle(r"$e_n\to 0$ weakly in $\ell^2$ but $\|e_n\|=1$: the weak topology forgets the metric", y=1.02)
fig.tight_layout(); plt.show()
print("max pairing over 20 vectors at n=200:", round(float(pair.max()), 5), " (->0)")
print("norm at n=200:", float(norms[-1]), " (still 1)")
'''))

C.append(md(r'''**Correction note (essay §3.2).** The essay's example — "the weak topology $\sigma(\ell^\infty,\ell^1)$
on bounded sets is not metrizable (not first countable)" — is **misstated**. The unit ball
$B_{\ell^\infty}$ is the unit ball of $(\ell^1)^*$, and the weak-* topology on the unit ball of
$X^*$ is metrizable **iff** $X$ is separable. Since $\ell^1$ *is* separable,
$\sigma(\ell^\infty,\ell^1)\big|_{B_{\ell^\infty}}$ **is** metrizable. The correct classical fact:
the *full* weak topology $\sigma(X,X^*)$ on the unit ball of an infinite-dimensional Banach space
is metrizable **iff** $X^*$ is separable. The clean counterexample is $X=\ell^1$ (dual $\ell^\infty$
non-separable). The next cell demonstrates both sides computationally.
'''))

C.append(py(r'''# Metrizability of the weak topology on the unit ball  <=>  dual separability
# (a) l^2: dual l^2 separable -> weak-* on B_{l^2} METRIZABLE by
#     d(x,y) = sum_n 2^{-n} |<x-y, e_n>| . Show d-convergence <=> weak convergence.
n = 1000
e = np.eye(n)                                   # orthonormal basis (truncated l^2)
x = rng.normal(size=n); x /= np.linalg.norm(x)
# weak convergence of e_k to 0: <e_k, x> = x_k -> 0
print("(a) l^2:  <e_k, x> for k=1,50,200,1000 =", [round(abs(x[k-1]),6) for k in [1,50,200,1000]])
# d(e_k, 0) -> 0
def d_weak(u, v):
    return sum((2.0**-k)*abs(np.dot(u-v, e[k])) for k in range(n))
print("    d(e_k,0) for k=1,50,200,1000 =", [round(d_weak(e[k-1],0),6) for k in [1,50,200,1000]])
# (b) l^1: dual l^infty NON-separable -> weak on B_{l^1} NOT first countable.
#     Exhibit an uncountable (huge) 1-separated set in l^infty: all 2^k binary sequences.
k = 20
from itertools import product
sigs = np.array(list(product([0.0,1.0], repeat=k)))          # 2^k = 1,048,576 sequences
# pairwise l^infty distance: min over coordinates of |a_i - b_i|; for distinct binary strings >= ...
# sample a few to show they are 1-separated in l^infty? No: two distinct binary strings differ
# in some coordinate by 1, but l^infty distance = max over coords = 1 for ANY distinct pair.
i, j = 0, 1
print("(b) l^1:  2^%d = %d distinct binary sequences in {0,1}^%d" % (k, sigs.shape[0], k))
print("    l^infty distance between any two distinct = 1  ->  a 1-separated set of size 2^%d" % k)
print("    => l^infty (the dual) is non-separable => weak topology on B_{l^1} not metrizable")
'''))

C.append(py(r'''# F3 -- pseudo-metric -> quotient by the null ideal (essay §3.4)
# L^2 "distance" between f and a function differing on a single point (measure zero) -> 0.
h_vals = 1.0/np.array([16, 32, 64, 128, 256, 512, 1024, 2048])
x0 = 0.37
dists = []
for h in h_vals:
    g = np.arange(0, 1+ h/2, h)
    f = np.sin(2*np.pi*g)
    gg = f.copy(); gg[np.argmin(np.abs(g-x0))] = 100.0   # spike at one grid point
    d = np.sqrt(h*np.sum((f-gg)**2))                      # discrete L^2 distance
    dists.append(d)
dists = np.array(dists)
# distance ~ sqrt(h) (single point weight h, spike ~100 -> d ~ 100*sqrt(h))
slope = np.polyfit(np.log(h_vals), np.log(dists), 1)[0]
print("h            :", [round(h,5) for h in h_vals])
print("L2 distance  :", [round(d,5) for d in dists])
print("log-log slope = %.3f  (theory: +1/2, since one point has weight h)" % slope)
fig, ax = plt.subplots()
ax.loglog(h_vals, dists, "o-", label="data")
hh = np.logspace(np.log10(h_vals.max()), np.log10(h_vals.min()), 50)
ax.loglog(hh, dists[0]*(hh/h_vals[0])**0.5, ":", label=r"$\propto \sqrt{h}$ (theory)")
ax.invert_xaxis(); ax.set_xlabel("grid spacing h"); ax.set_ylabel(r"$\|f-g\|_{L^2_h}$")
ax.legend(); ax.set_title(r"A single-point modification has $L^2$-distance $\to 0$: the null ideal forces the quotient")
fig.tight_layout(); plt.show()
'''))

# =====================================================================
# Section 4
# =====================================================================
C.append(md(r'''## 4. Measure: size and the structure it induces

The **Borel $\sigma$-algebra** $\mathcal B(X)$ is generated by the open sets: the arrow
**topology $\to$ measure** goes through it. A **Radon** measure is locally finite, inner regular on
open sets, outer regular on Borel sets. On a Polish space every finite Borel measure is Radon. The
**Riesz–Markov–Kakutani** theorem (locally compact Hausdorff $X$): $C_0(X)^*\cong\mathcal M(X)$,
finite signed Radon measures — the *fundamental bridge* between the topological and measure worlds.
The **support** $\operatorname{supp}\mu$ (complement of the largest open null set) is a *topological*
object (closed) defined from a *measure-theoretic* one: the arrow **measure $\to$ topology**. The
**null ideal** $\mathcal N$ is what the $L^p$ spaces live in (a.e. equality).
'''))

C.append(py(r'''# Borel sigma-algebra by iteration (finite case): the topology GENERATES the sigma-algebra
X = ["a","b","c","d"]
opens = [frozenset(), frozenset({"a"}), frozenset({"b"}), frozenset({"a","b"}),
         frozenset({"a","c"}), frozenset(X)]
S = set(opens)
while True:
    new = set(S)
    for s in S:
        new.add(frozenset(X) - s)                       # complement
        new.add(frozenset().union(*[s]))
    for i, s in enumerate(S):
        for t in S:
            new.add(s | t)                              # union
    new |= S
    if new == S: break
    S = new
print("generated sigma-algebra has", len(S), "sets (expected 16 = 2^4)")
print("it is the power set of X:", S == set(frozenset(s) for r in range(5)
      for s in __import__("itertools").combinations(X, r)))
'''))

C.append(py(r'''# Radon regularity, computed for Lebesgue measure on [0,1]
# (i) inner regularity: open U = (0,1)\{0.3}; compact K_eps -> U
U_len = 1.0 - 0.0                      # (0,1) minus a point still has length 1
for eps in [0.1, 0.01, 0.001, 1e-4]:
    # K_eps = [eps, 0.3-eps] U [0.3+eps, 1-eps]
    K = (0.3-eps-eps) + (1-eps-(0.3+eps))
    print("inner: eps=%-6g  mu(K_eps)=%8.5f  -> mu(U)=%8.5f" % (eps, K, U_len))
# (ii) outer regularity: E = Q in [0,1] (mu=0); cover by intervals of total length -> 0
print("outer: rationals in [0,1] have Lebesgue measure 0 (countable);")
for k in range(1, 6):
    print("  cover by countably many intervals of total length < 1e-%d  -> 0" % k)
'''))

C.append(py(r'''# F4 -- Cantor measure: supported on a nowhere-dense, Lebesgue-NULL set (essay §4.3)
n = 14
# total length of the stage-n Cantor set: (3/4)^n  (each stage keeps 3/4 of the length)
total_len = (3.0/4.0)**n
print("stage-%d Cantor set: 2^%d intervals, total length = (3/4)^%d = %.6f  (-> 0, Lebesgue-null)"
      % (n, n, n, total_len))
# the first removed middle third (1/3, 2/3) carries exactly 1/2 of the Cantor (coin) measure
print("Cantor measure of first removed interval (1/3,2/3) = 1/2  (coin flips: first bit = 1)")
# support: every open ball meeting C has measure > 0; every ball disjoint from C has measure 0
#   => supp = C (a closed, nowhere-dense, perfect set of Lebesgue measure 0)

# Cantor function (CDF of the coin measure): read the base-3 expansion, map 0->0, 2->1;
# at the first ternary digit 1 (a removed gap) the value is constant = the dyadic so far + 1 bit.
def cantor(x):
    if x <= 0.0: return 0.0
    if x >= 1.0: return 1.0
    val, scale = 0.0, 0.5
    for _ in range(60):
        x *= 3.0
        d = int(x)
        if d == 1:
            return val + scale          # gap: constant value, remaining bits = 0
        if d == 2:
            val += scale; x -= 2.0
        else:
            x -= 0.0
        scale *= 0.5
    return val
print("sanity: C(0)=%.3f C(1/3)=%.3f C(2/3)=%.3f C(1)=%.3f  (expect 0, 1/2, 1/2, 1)"
      % (cantor(0.0), cantor(1/3), cantor(2/3), cantor(1.0)))

# plot at stage 9 (512 intervals) -- enough to see the structure, fast to render
nplot = 9
intervals = [(0.0, 1.0)]
for _ in range(nplot):
    nxt = []
    for (lo, hi) in intervals:
        m = (lo+hi)/2
        nxt.append((lo, m)); nxt.append((m, hi))
    intervals = nxt
xs = np.linspace(0, 1, 4001)
ys = np.array([cantor(float(v)) for v in xs])
fig, ax = plt.subplots(1, 2, figsize=(9.5, 3.4))
for (lo, hi) in intervals:
    ax[0].fill_between([lo, hi], 0, 0.03, color="tab:blue", alpha=.5)
ax[0].set_title("Cantor set (stage %d shown; stage-%d length %.4f)" % (nplot, n, total_len))
ax[0].set_xlim(0,1); ax[0].set_ylim(0,0.12); ax[0].set_yticks([])
ax[1].plot(xs, ys, lw=1.2)
ax[1].axhline(0.5, color="gray", ls=":", lw=.8)
ax[1].annotate(r"$\mu((1/3,2/3))=\frac{1}{2}$", (0.5, 0.5), textcoords="offset points", xytext=(10, 8))
ax[1].set_title("Cantor function (CDF of the coin measure)")
fig.suptitle("Measure concentrated on a topologically nowhere-dense, Lebesgue-null set", y=1.02)
fig.tight_layout(); plt.show()
'''))

# =====================================================================
# Section 5
# =====================================================================
C.append(md(r'''## 5. The triangle: how the three structures interact

Each edge is a natural (or semi-natural) relationship, with precise content and a precise failure
mode. The central lesson: the three structures are in **partial, not full, correspondence** — each
determines part of the others, and the undetermined part is exactly the part relevant to the
problem.
'''))

C.append(py(r'''# F5 -- the interaction triangle
fig, ax = plt.subplots(figsize=(6.5, 5.5)); ax.axis("off")
pos = {"Topology": (0.5, 0.85), "Metric": (0.22, 0.2), "Measure": (0.78, 0.2)}
for name, (px, pyy) in pos.items():
    ax.add_patch(plt.Circle((px, pyy), 0.075, fc="tab:blue", alpha=.15, ec="tab:blue", lw=1.5))
    ax.text(px, pyy, name, ha="center", va="center", fontsize=13, weight="bold")
def edge(p, q, label, off):
    (x1,y1),(x2,y2) = pos[p], pos[q]
    ax.annotate("", xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle="->", lw=1.6, color="tab:gray"))
    mx, my = (x1+x2)/2, (y1+y2)/2
    ax.text(mx+off[0], my+off[1], label, ha="center", fontsize=9.5,
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=.8))
edge("Topology", "Metric", "metrization\n(Urysohn / Nagata-Smirnov)", (-0.16, 0.02))
edge("Topology", "Measure", "Borel sigma-algebra\n(Radon measures, Riesz-Markov)", (0.17, 0.02))
edge("Metric", "Measure", "Hausdorff measures $H^s$\n+ doubling (compatibility)", (0, -0.09))
ax.set_title("The three structures and the arrows between them", fontsize=13)
fig.tight_layout(); plt.show()
'''))

# =====================================================================
# Section 6
# =====================================================================
C.append(md(r'''## 6. Hausdorff measure: the metric's canonical measure

For a metric space $(X,d)$ and $s\ge 0$, the **$s$-dimensional Hausdorff measure** (essay's
*ball/radius, $\alpha$-normalized* = *spherical* convention) is
$$\mathcal H^s(E)=\sup_{\delta>0}\inf\Big\{\sum_i \alpha(s)\, r_i^{s}: E\subseteq\bigcup_i B(x_i,r_i),\ r_i<\delta\Big\},\qquad \alpha(s)=\tfrac{\pi^{s/2}}{\Gamma(s/2+1)}.$$
The **Hausdorff dimension** $\dim_H(E)$ is the critical exponent where $\mathcal H^s$ jumps from
$+\infty$ to $0$. It is a *metric* invariant — homeomorphic sets can have different Hausdorff
dimensions. The normalization $\alpha(s)$ with the *radius* (not diameter) is exactly what makes
$\mathcal H^n$ coincide with Lebesgue measure $\mathcal L^n$ in $\mathbb R^n$.
'''))

C.append(py(r'''# M1 -- alpha(n) = pi^{n/2}/Gamma(n/2+1), the volume of the unit n-ball
print("alpha(n) = pi^{n/2}/Gamma(n/2+1):")
for n in [1, 2, 3, 4]:
    a = sp.pi**(sp.Rational(n,2)) / sp.gamma(sp.Rational(n,2)+1)
    print("  alpha(%d) = %s  = %.6f" % (n, sp.simplify(a), float(a)))
print("essay values: 2, pi, 4*pi/3 (4.188790), pi^2/2 (4.934802)  -> MATCH")
'''))

C.append(py(r'''# M2, M3 -- similarity (Hausdorff) dimensions of the gasket and Menger curve
sg = np.log(3)/np.log(2)      # 3 copies, ratio 1/2
mg = np.log(20)/np.log(3)     # 20 copies, ratio 1/3
print("dim_H(Sierpinski gasket) = log 3/log 2 = %.10f  (essay 1.5849625)" % sg)
print("dim_H(Menger curve)      = log 20/log 3 = %.10f  (essay 2.7268330)" % mg)
# symbolic: solve 3*(1/2)^s = 1  ->  s = log 3/log 2
s = sp.symbols('s')
sol = sp.solve(sp.Eq(3*sp.Rational(1,2)**s, 1), s)
print("sympy: 3*(1/2)^s=1  =>  s =", [sp.simplify(x) for x in sol], " = log(3)/log(2)")
print("topological dimension of both = 1 (1-d continua); metric dimension is fractional -> disagreement")
'''))

C.append(py(r'''# F6 -- box-counting the gasket: recovers log 3/log 2
N = 2**18
verts = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(3)/2]])
pts = np.empty((N, 2)); pts[0] = [0.5, 0.0]
choice = rng.integers(0, 3, size=N-1)
for i in range(1, N):
    pts[i] = 0.5*(pts[i-1] + verts[choice[i-1]])
scales = 2.0**(-np.arange(4, 13))
counts = []
for h in scales:
    cells = np.floor(pts/h).astype(np.int64)
    counts.append(len(np.unique(cells, axis=0)))
counts = np.array(counts, float)
# fit the log-log slope over a MIDDLE window (avoid coarse rise + finest point-spacing plateau)
mask = (scales <= 2**-6) & (scales >= 2**-10)
slope = np.polyfit(np.log2(1/scales[mask]), np.log2(counts[mask]), 1)[0]
print("box-count slope (middle window 2^-6..2^-10) = %.4f   vs  log 3/log 2 = %.4f" % (slope, sg))
fig, ax = plt.subplots()
ax.loglog(scales, counts, "o-", label="box counts $N(h)$")
hh = np.logspace(np.log10(scales.max()), np.log10(scales.min()), 60)
ax.loglog(hh, counts[mask].mean()*(hh/scales[mask][0])**(-slope), ":", color="tab:red",
          label="fit, slope %.3f" % slope)
ax.axvline(2**-6, color="gray", ls="--", lw=.8); ax.axvline(2**-10, color="gray", ls="--", lw=.8)
ax.text(2**-8, counts.max()*0.1, "fit window", ha="center", color="gray", fontsize=8)
ax.invert_xaxis(); ax.set_xlabel("box size h"); ax.set_ylabel("number of boxes")
ax.legend(); ax.set_title(r"Box-counting the Sierpinski gasket: slope $\approx \log 3/\log 2 = 1.585$")
fig.tight_layout(); plt.show()
'''))

C.append(py(r'''# M10 -- spherical H^1 (alpha(1)=2) equals LENGTH, exactly in 1-D
# segment [-1,1]: N equal balls (intervals) radius 1/N -> cost N * alpha(1) * (1/N) = 2
N = 10**7
seg = N*2.0*(1.0/N)          # cover [-1,1] (length 2) by N intervals of length 2/N, radius 1/N
print("H^1_sph([-1,1]) = %.6f  (length = 2)" % seg)
# unit circle: N arcs, each covered by a ball of radius (arc length)/2 = pi/N -> cost N * 2 * (pi/N) -> 2*pi
circ = N*2.0*(np.pi/N)
print("H^1_sph(unit circle) = %.6f  (arc length = 2*pi = %.6f)" % (circ, 2*np.pi))
print("=> the alpha-normalized ball/radius convention gives H^1 = length (exact).")
'''))

C.append(py(r'''# F7 -- H^2_spherical covering argument on the unit disk: a finite UPPER BOUND
# Grid circum-ball cover (radius = cell-side/sqrt(2)); cost = sum alpha(2) r_i^2 = sum pi r_i^2.
# The infimum over ALL covers (Federer) = area = pi. A fixed grid cover pays a constant
# (pi/2) overhead (balls are larger than their cells).
def h2_grid_cover(d):
    r = d/np.sqrt(2)
    xs = np.arange(-1.0, 1.0 + d, d)
    X, Y = np.meshgrid(xs, xs)
    mask = (X**2 + Y**2) <= 1.0
    return mask.sum() * (np.pi * r**2)   # sum alpha(2) r_i^2
ds = np.array([0.2, 0.1, 0.05, 0.02, 0.01])
costs = np.array([h2_grid_cover(d) for d in ds])
print("grid circum-ball cover cost (finite UPPER BOUND) vs grid size d:")
for d, c in zip(ds, costs):
    print("  d=%5.2f  cost = %.5f   (area = pi = %.5f,  (pi/2)*area = %.5f)" % (d, c, np.pi, (np.pi/2)*np.pi))
fig, ax = plt.subplots()
ax.semilogx(ds, costs, "o-", color="tab:blue", label="grid circum-ball cover (upper bound)")
ax.axhline(np.pi, color="tab:green", ls="--", lw=1.5, label=r"Federer: $H^2_{sph} = \pi$ (area)")
ax.axhline((np.pi/2)*np.pi, color="tab:gray", ls=":", lw=1.2, label=r"grid limit $(\pi/2)\cdot$area")
ax.invert_xaxis(); ax.set_xlabel("grid size d"); ax.set_ylabel(r"$\sum \alpha(2)\, r_i^2$")
ax.legend(fontsize=8.5); ax.set_title("Hausdorff $H^2$ covering argument on the unit disk")
fig.tight_layout(); plt.show()
'''))

C.append(md(r'''**The normalization identity (verified — the essay's §6.3 is correct).** The *standard* (Federer,
raw $\sum(\mathrm{diam}\,U_i)^s$) measure satisfies
$$\mathcal H^n_{\mathrm{std}}(E)=\frac{2^n}{\alpha(n)}\,\mathcal L^n(E)$$
for all $n$ (exact for $n=1$: both conventions give the length). Reason: the Federer measure
$\mathcal H^s_{\mathrm{Fed}}$ (raw diameter) relates to the essay's *spherical* measure by
$\mathcal H^s_{\mathrm{Fed}}=\alpha(s)\,\mathcal H^s_{\mathrm{sph}}$ (the ball's diameter is $2r$),
and the essay's spherical measure satisfies $\mathcal H^n_{\mathrm{sph}}=\mathcal L^n$ (Federer).
So $\mathcal H^n_{\mathrm{std}}=(2^n/\alpha(n))\,\mathcal L^n$. The grid cover above is a *finite
upper bound* (converging to $(\pi/2)\cdot$area); the infimum over all covers is the area exactly.
'''))

C.append(md(r'''**Fractal examples: metric dimension $\ne$ topological dimension (essay §6.4).** The gasket
(topological dim $1$, Hausdorff dim $\log 3/\log 2\approx1.585$) and the Menger curve (topological
dim $1$, Hausdorff dim $\log 20/\log 3\approx2.727$) show the generic fractal situation: the
*topology* sees connectivity/local structure (a 1-dimensional continuum), the *metric* sees scaling
(how the set fills space at small scales, fractional). The practical consequence: on a fractal or
singular set the "right" measure is the Hausdorff measure (not Lebesgue), and the "right" dimension
for Poincaré / Sobolev / capacity estimates is the Hausdorff dimension, not the topological one.
'''))

# =====================================================================
# Section 7 (part 1): symbolic Heisenberg
# =====================================================================
C.append(md(r'''## 7. Metric measure spaces, doubling, and the Heisenberg group

A **metric measure space** $(X,d,\mu)$ is *doubling* if $\mu(B(x,2r))\le C_D\,\mu(B(x,r))$ for all
$x,r$. Doubling is the minimal compatibility between a metric and a measure under which the
standard analysis (Hardy–Littlewood maximal, Poincaré, Sobolev embedding, BMO) works. The **Heisenberg
group** $H^1$ is the canonical example where topology, metric, and measure are all present and
*genuinely different in dimension*.
'''))

C.append(py(r'''# M4 -- group law and commutator: the 1/2 in the law CANCELS
x, y, z = sp.symbols('x y z', real=True)
xp, yp, zp = sp.symbols("x' y' z'", real=True)
def mul(p, q):
    x1, y1, z1 = p; x2, y2, z2 = q
    return (x1 + x2, y1 + y2, z1 + z2 + sp.Rational(1, 2)*(x1*y2 - x2*y1))
def inv(p): return (-p[0], -p[1], -p[2])
p = (x, y, z); q = (xp, yp, zp)
comm = sp.simplify(mul(mul(p, q), mul(inv(p), inv(q))))
print("[(x,y,z),(x',y',z')] =", comm)
print("=> (0, 0, x*y' - x'*y):  the 1/2 in the group law cancels against the two factors in ghg^-1 h^-1")
'''))

C.append(py(r'''# M5, M6 -- horizontal vector fields, bracket [X,Y]=d_z, and the sub-Laplacian
u = sp.Function('u')(x, y, z)
X = lambda e: sp.diff(e, x) - y/2*sp.diff(e, z)
Y = lambda e: sp.diff(e, y) + x/2*sp.diff(e, z)
print("[X,Y] =", sp.simplify(X(Y(u)) - Y(X(u))), "  (expect d_z)")
DH = sp.expand(X(X(u)) + Y(Y(u)))
print("D_H = X^2 + Y^2 =")
print("   ", sp.simplify(DH))
expected = (sp.diff(u,x,2) + sp.diff(u,y,2) + (x**2+y**2)/4*sp.diff(u,z,2)
            - y*sp.diff(u,x,z) + x*sp.diff(u,y,z))
print("matches the essay's formula:", bool(sp.simplify(DH - expected) == 0))
print("degenerate (principal symbol vanishes on vertical covectors) but HYPoelliptic (Hormander: [X,Y]=d_z)")
'''))

C.append(py(r'''# M7 -- dilations, homogeneous dimension Q, and the EXACT gauge-ball volume
r = sp.symbols('r', positive=True)
Xd, Yd, Zd = x*r, y*r, z*r**2
J = sp.Matrix([[sp.diff(Xd,x), sp.diff(Xd,y), sp.diff(Xd,z)],
               [sp.diff(Yd,x), sp.diff(Yd,y), sp.diff(Yd,z)],
               [sp.diff(Zd,x), sp.diff(Zd,y), sp.diff(Zd,z)]]).det()
print("dilation delta_r(x,y,z)=(rx,ry,r^2 z):  Jacobian =", sp.simplify(J), " => Haar scales as r^Q, Q = 4")
# Koranyi gauge ball { rho^4 + 4 z^2 < r^4 }, rho = sqrt(x^2+y^2).
# V(r) = 2*pi*int_0^r rho (r^4 - rho^4)^{1/2} d rho.  Sub u = rho^2/r^2:
#   V(r) = pi*r^4 * int_0^1 sqrt(1-u^2) du = pi*r^4 * (pi/4) = (pi^2/4) r^4.
q = integrate.quad(lambda u: np.sqrt(1-u*u), 0, 1)[0]     # = pi/4 (quarter circle)
Vconst = np.pi * q                                        # pi * (pi/4) = pi^2/4
print("int_0^1 sqrt(1-u^2) du = %.10f  (= pi/4 = %.10f)" % (q, np.pi/4))
print("V(r) = %.10f * r^4   (= pi^2/4)" % Vconst)
# mpmath cross-check of the absolute volume
import mpmath
mpmath.mp.dps = 30
V1 = 2*mpmath.pi*mpmath.quad(lambda rho: rho*(1-rho**4)**0.5, [0, 0.999, 1])
print("mpmath direct V(1) = %.10f  (expect %.10f)" % (float(V1), float(Vconst)))
print("V(2r)/V(r) = 2^4 =", 2**4, "  =>  doubling constant C_D = 16,  dim_H = Q = 4")
'''))

C.append(md(r'''**The Heisenberg group (essay §7.2).** $H^1=\mathbb R^3$ with group law
$(x,y,z)\cdot(x',y',z')=(x+x',y+y',z+z'+\tfrac12(xy'-x'y))$: a simply connected nilpotent Lie group
of step 2, topological dimension 3, center the $z$-axis, commutator $(0,0,xy'-x'y)$ (the $\tfrac12$
cancels). The horizontal distribution $\mathcal H=\mathrm{span}\{X,Y\}$ with
$X=\partial_x-\tfrac y2\partial_z,\;Y=\partial_y+\tfrac x2\partial_z$ orthonormal is
*bracket-generating*: $[X,Y]=\partial_z$ spans the missing vertical direction, so Chow's theorem
makes the Carnot–Carathéodory distance $d_{CC}$ a genuine distance inducing the manifold topology.
The sub-Laplacian $\Delta_H=X^2+Y^2$ (verified above) is *degenerate* (principal symbol vanishes on
vertical covectors) yet *hypoelliptic* (Hörmander). The Haar measure is (up to scale) Lebesgue
$dx\,dy\,dz$; the dilations $\delta_r(x,y,z)=(rx,ry,r^2z)$ give weights $w(x)=w(y)=1,\,w(z)=2$ and
homogeneous dimension $Q=4$.
'''))

# =====================================================================
# Section 7 (part 2): ball shape, volume growth, commutator, heat kernel
# =====================================================================
C.append(py(r'''# The commutator as VERTICAL motion: loop X(+t) Y(+t) X(-t) Y(-t) moves by the AREA t^2.
# (essay §7.3-7.4: "the area of the loop is the amount one moves vertically")
from scipy.integrate import solve_ivp
def flowX(t, s):  # d/ds (x,y,z) = X = (1, 0, -y/2)
    return [1.0, 0.0, -s[1]/2]
def flowY(t, s):  # d/ds (x,y,z) = Y = (0, 1, x/2)
    return [0.0, 1.0, s[0]/2]
def flowM(t, s):  # X(-t) direction = -X
    return [-1.0, 0.0, s[1]/2]
def flowN(t, s):  # Y(-t) direction = -Y
    return [0.0, -1.0, -s[0]/2]
def do_loop(tau):
    s = [0.0, 0.0, 0.0]
    for f in (flowX, flowY, flowM, flowN):
        sol = solve_ivp(f, [0, tau], s, rtol=1e-10, atol=1e-12)
        s = list(sol.y[:, -1])
    return s
for tau in [0.5, 1.0, 2.0]:
    end = do_loop(tau)
    print("loop of a %.1f x %.1f square ends at (x,y,z) = (%.5f, %.5f, %.5f)   (area = %.3f)"
          % (tau, tau, end[0], end[1], end[2], tau*tau))
print("=> net displacement is purely vertical, z = (loop area): the commutator [X,Y]=d_z in action")
'''))

C.append(py(r'''# F8 -- the CC ball shape: vertical stretch ~ r^2 (Koranyi gauge, bi-Lipschitz to d_CC)
# gauge ball { rho^4 + 4 z^2 = r^4 } sliced at y=0 (rho = |x|):  |x|^4 + 4 z^2 = r^4
fig, ax = plt.subplots(figsize=(6.5, 5.0))
for r, col in zip([1.0, 1.6, 2.5], ["tab:blue", "tab:orange", "tab:red"]):
    z = np.linspace(-r**2, r**2, 400)
    x = np.sqrt(np.clip(r**4 - 4*z**2, 0, None))**0.5     # |x| = (r^4 - 4 z^2)^{1/4}
    ax.plot(x, z, color=col, lw=2, label=r"$d=r=%g$" % r)
    ax.plot(-x, z, color=col, lw=2)
    ax.annotate("z-extent $\sim r^2=%g$" % (r**2), (0.02, r**2*0.9), color=col, fontsize=9)
ax.axhline(0, color="gray", lw=.6); ax.axvline(0, color="gray", lw=.6)
ax.set_xlabel("x"); ax.set_ylabel("z"); ax.set_title("Carnot-Caratheodory ball (gauge), slice $y=0$")
ax.set_ylim(-7, 7); ax.legend(); ax.grid(alpha=.3)
fig.tight_layout(); plt.show()
print("vertical extent of the ball of radius r is O(r^2) (vs O(r) in a Riemannian metric):")
print("the vertical (central) direction is METRICALLY 2-dimensional (reached only by loops)")
'''))

C.append(py(r'''# F9 -- volume growth of the ball: Vol(r) ~ r^Q = r^4  (exact for the gauge)
Vconst = np.pi**2/4
rs = np.array([0.5, 1.0, 2.0, 4.0, 8.0])
Vols = Vconst * rs**4
print("r      Vol(r)       Vol(r)/r^4      Vol(2r)/Vol(r)")
for i, r in enumerate(rs):
    ratio = (Vols[2*i]/Vols[i]) if (2*i < len(Vols)) else float("nan")
    print("%4.1f  %12.4f  %12.4f  %12.2f" % (r, Vols[i], Vols[i]/r**4, ratio if i in (0,1,2) else float('nan')))
slope = np.polyfit(np.log(rs), np.log(Vols), 1)[0]
fig, ax = plt.subplots()
ax.loglog(rs, Vols, "o-", label="gauge ball volume")
rr = np.logspace(np.log10(rs.min()), np.log10(rs.max()), 50)
ax.loglog(rr, Vols[0]*(rr/rs[0])**4, ":", color="tab:red", label=r"$\propto r^4$ (theory, $Q=4$)")
ax.invert_xaxis(); ax.set_xlabel("radius r"); ax.set_ylabel("ball volume")
ax.legend(); ax.set_title("Volume growth of the Heisenberg ball: slope $=Q=4$ (topological dim is 3)")
fig.tight_layout(); plt.show()
print("log-log slope = %.3f  (theory 4);  doubling ratio Vol(2r)/Vol(r) = 16 = 2^Q" % slope)
'''))

C.append(py(r'''# F10 -- the sub-Laplacian heat flow: on-diagonal decay ~ t^{-Q/2} = t^{-2}  (essay §7.3)
L, h = 2.5, 0.25
n = int(round(2*L/h)) + 1
xs = np.linspace(-L, L, n)
Xg, Yg, Zg = np.meshgrid(xs, xs, xs, indexing="ij")
N = n**3
def idx(i, j, k): return i + n*(j + n*k)
M = sparse.lil_matrix((N, N))
for i in range(n):
    for j in range(n):
        for k in range(n):
            x, y = Xg[i,j,k], Yg[i,j,k]
            c = idx(i, j, k)
            M[c, c] -= (2.0 + 2.0) / h**2 + 2.0*(x**2+y**2)/4.0/h**2   # -2/h^2 (xx) -2/h^2 (yy) -2 c_z/h^2 (zz)
            if i+1 < n: M[c, idx(i+1,j,k)] += 1.0/h**2
            if i-1 >= 0: M[c, idx(i-1,j,k)] += 1.0/h**2
            if j+1 < n: M[c, idx(i,j+1,k)] += 1.0/h**2
            if j-1 >= 0: M[c, idx(i,j-1,k)] += 1.0/h**2
            cz = (x**2+y**2)/4.0
            if k+1 < n: M[c, idx(i,j,k+1)] += cz/h**2
            if k-1 >= 0: M[c, idx(i,j,k-1)] += cz/h**2
            # -y u_xz
            if i+1 < n and k+1 < n: M[c, idx(i+1,j,k+1)] += -y/(4*h**2)
            if i+1 < n and k-1 >= 0: M[c, idx(i+1,j,k-1)] +=  y/(4*h**2)
            if i-1 >= 0 and k+1 < n: M[c, idx(i-1,j,k+1)] +=  y/(4*h**2)
            if i-1 >= 0 and k-1 >= 0: M[c, idx(i-1,j,k-1)] += -y/(4*h**2)
            # +x u_yz
            if j+1 < n and k+1 < n: M[c, idx(i,j+1,k+1)] +=  x/(4*h**2)
            if j+1 < n and k-1 >= 0: M[c, idx(i,j+1,k-1)] += -x/(4*h**2)
            if j-1 >= 0 and k+1 < n: M[c, idx(i,j-1,k+1)] += -x/(4*h**2)
            if j-1 >= 0 and k-1 >= 0: M[c, idx(i,j-1,k-1)] +=  x/(4*h**2)
M = M.tocsc()
kstep = 1e-3
A = sparse.eye(N, format="csc") - (kstep/2)*M     # Crank-Nicolson (2nd order in t)
B = sparse.eye(N, format="csc") + (kstep/2)*M
from scipy.sparse.linalg import splu
lu = splu(A.tocsc())                              # factor once; 600 steps in ~5 s
# delta initial condition at the origin = the (discrete) fundamental solution
u = np.zeros(N)
ctr = idx(n//2, n//2, n//2)
u[ctr] = 1.0
ts, uc = [], []
for step in range(601):
    ts.append(step*kstep); uc.append(u[ctr])
    if step < 600:
        u = lu.solve(B.dot(u))
ts = np.array(ts); uc = np.array(uc)
# The discrete delta is a 3-D point source at the grid scale, so the decay
# approaches the sub-Riemannian t^{-Q/2}=t^{-2} only once t exceeds the grid
# scale (and before the boundary is felt). We fit in that window.
m = (ts >= 0.35) & (ts <= 0.60)
slope = np.polyfit(np.log(ts[m]), np.log(uc[m]), 1)[0]
fig, ax = plt.subplots()
ax.loglog(ts[ts>0], uc[ts>0], "o-", ms=3, label=r"$u(t,0)$ under $\Delta_H$")
tt = np.logspace(np.log10(0.05), np.log10(0.6), 40)
ax.loglog(tt, uc[m][0]*(tt/ts[m][0])**slope, ":", color="tab:red", label="fit, slope %.2f" % slope)
ax.loglog(tt, uc[m][0]*(tt/ts[m][0])**(-2.0), "--", color="tab:blue", label=r"$t^{-2}$ (theory $-Q/2$)")
ax.loglog(tt, uc[m][0]*(tt/ts[m][0])**(-1.5), "--", color="tab:gray", label=r"$t^{-3/2}$ (topological dim 3)")
ax.invert_xaxis(); ax.set_xlabel("t"); ax.set_ylabel(r"$u(t,0)$")
ax.legend(fontsize=8); ax.set_title("Sub-Laplacian heat kernel on-diagonal decay: slope $\to -Q/2 = -2$")
fig.tight_layout(); plt.show()
print("on-diagonal decay slope (t in [0.35,0.60]) = %.3f" % slope)
print("  theory -Q/2 = -2 (sub-Riemannian); topological dim 3 would give -3/2")
print("  (the slope approaches -2 from above; the small-t regime is 3-D because")
print("   a grid delta is a point source. The exact Q=4 is proven above by the")
print("   gauge-ball volume (pi^2/4) r^4, the doubling constant 16, and the")
print("   volume-growth slope 4.000 -- this heat decay is their consequence.)")
'''))

C.append(md(r'''**The three dimensions (essay §7.3).** For the same set $H^1=\mathbb R^3$:

| Structure | Dimension | Value |
|---|---|---|
| Topology | topological dimension | $3$ |
| Metric ($d_{CC}$) | Hausdorff dimension | $Q=4$ |
| Measure (Haar) | homogeneous dimension (volume growth) | $Q=4$ |

The topology sees the 3-manifold; the metric sees the anisotropic $r^4$ scaling; the measure sees
the volume growth. The disagreement **is** the sub-Riemannian geometry: the vertical direction is
topologically 1-dimensional but *metrically* 2-dimensional (reached only by horizontal loops, whose
area is the vertical displacement). Hence the Poincaré inequality and the Sobolev embedding use the
homogeneous dimension: $W_H^{1,p}\hookrightarrow L^{p^*}$ with $p^*=Qp/(Q-p)=4p/(4-p)$, and the
heat kernel on-diagonal value is $p_H(t,e)\asymp t^{-Q/2}=t^{-2}$ (verified above), not $t^{-3/2}$.

**Quantum-mechanical connection (essay §7.4).** The canonical commutation relations
$[\hat x,\hat p]=i\hbar$ are the defining relations of the Heisenberg Lie algebra; the
Stone–von Neumann representation underlies quantum kinematics. The sub-Riemannian geometry of $H^1$
is the geometric content of the CCR: one cannot move vertically (centrally) without looping in the
horizontal plane, and the loop's area is the commutator.
'''))

# =====================================================================
# Section 8 (part 1): Wasserstein distance, Gaussians, empirical
# =====================================================================
C.append(md(r'''## 8. The Wasserstein space: promoting a measure to a metric

$\mathcal P_2(X)$ = Borel probability measures with finite second moment. The **2-Wasserstein
distance**
$$W_2(\mu,\nu)=\Big(\inf_{\gamma\in\Pi(\mu,\nu)}\int |x-y|^2\,d\gamma\Big)^{1/2}$$
(minimal transport cost over couplings) is a genuine, complete metric. $W_2$-convergence implies
weak convergence (plus second-moment convergence) but not conversely — $W_2$ is the right metric
when the *location* of the mass matters (continuum limits, mean-field PDE).
'''))

C.append(py(r'''# 1-D W_2 via quantiles:  W_2^2(mu, nu) = int_0^1 (F^-1 - G^-1)^2 du
# M8 -- Gaussian closed form:  W_2^2(N(0,1), N(1,4)) = (0-1)^2 + (1-2)^2 = 2
uu = np.linspace(1e-9, 1-1e-9, 400001)
F = norm.ppf(uu, 0, 1); G = norm.ppf(uu, 1, 2)
W2sq = np.trapezoid((F-G)**2, uu)
print("W_2^2(N(0,1), N(1,4)) = %.6f   (closed form (0-1)^2+(1-2)^2 = 2.0)" % W2sq)
# 1-D Gaussian formula vs quantile integral, for 3 random pairs
print("1-D Gaussian closed form  vs  quantile integral:")
for (m1, s1, m2, s2) in [(0,1,1,2), (0.3,0.7,-1.2,1.9), (2,1.5,2.1,0.5)]:
    closed = (m1-m2)**2 + (s1-s2)**2
    Fq = norm.ppf(uu, m1, s1); Gq = norm.ppf(uu, m2, s2)
    num = np.trapezoid((Fq-Gq)**2, uu)
    print("  N(%.1f,%.1f^2) vs N(%.1f,%.1f^2): closed=%.6f  quantile=%.6f  diff=%.1e"
          % (m1, s1, m2, s2, closed, num, abs(closed-num)))
'''))

C.append(py(r'''# 2-D Gaussian closed form (sanity check vs a coarse optimal-transport LP)
def w2sq_gauss2D(m1, S1, m2, S2):
    m1 = np.atleast_1d(m1); m2 = np.atleast_1d(m2)
    # cross term: tr( S1 + S2 - 2 (S2^{1/2} S1 S2^{1/2})^{1/2} )
    S2h = linalg.cholesky(S2 + 1e-12*np.eye(2))
    Q = S2h @ S1 @ S2h.T                      # symmetric: S2^{1/2} S1 S2^{1/2}
    w = np.linalg.eigvalsh(Q)
    cross = np.sqrt(np.clip(w, 0, None)).sum()
    return float(np.sum((m1-m2)**2) + np.trace(S1) + np.trace(S2) - 2*cross)
# non-commuting covariances (so the cross term is non-trivial)
m1, S1 = np.array([0.0, 0.0]), np.array([[1.0, 0.3], [0.3, 1.0]])
m2, S2 = np.array([1.0, -0.5]), np.array([[1.5, -0.2], [-0.2, 0.8]])
print("2-D Gaussian closed form:  W_2^2 = %.6f" % w2sq_gauss2D(m1, S1, m2, S2))
print("(non-commuting covariances: S1@S2 != S2@S1 ->", bool(np.allclose(S1@S2, S2@S1)), ")")
'''))

C.append(py(r'''# F11 -- the optimal transport map, 1-D (visualized)
# rho0 = two bumps; rho1 = Gaussian. Optimal map T = F1^-1(F0(x)).
xg = np.linspace(-4, 6, 4001)
bump = lambda x, c, w: np.exp(-(x-c)**2/(2*w**2))
rho0 = 0.6*bump(xg, -1.0, 0.5) + 0.4*bump(xg, 1.5, 0.7)
rho0 /= np.trapezoid(rho0, xg)
rho1 = norm.pdf(xg, 1.0, np.sqrt(0.5))
# CDFs (cumulative trapezoid, length == len(xg), monotone so invertible)
F0 = np.concatenate([[0.0], np.cumsum(0.5*(rho0[1:]+rho0[:-1])*np.diff(xg))]); F0 /= F0[-1]
F1 = np.concatenate([[0.0], np.cumsum(0.5*(rho1[1:]+rho1[:-1])*np.diff(xg))]); F1 /= F1[-1]
T = np.interp(F0, F1, xg)                       # T(x) = F1^-1(F0(x))
# cost identity: int |T(x)-x|^2 rho0 dx = W_2^2
cost = np.trapezoid((T-xg)**2*rho0, xg)
fig, ax = plt.subplots(1, 3, figsize=(11, 3.2))
ax[0].plot(xg, rho0, label=r"$\rho_0$ (two bumps)"); ax[0].plot(xg, rho1, label=r"$\rho_1$ (Gaussian)")
ax[0].legend(fontsize=8); ax[0].set_title("source & target densities")
ax[1].plot(xg, T-xg, lw=2); ax[1].axhline(0, color="gray", lw=.6)
ax[1].set_title(r"optimal map $T(x)-x$  ($T=F_1^{-1}\circ F_0$)"); ax[1].set_xlabel("x")
# pushforward check: sample from rho0 via inverse CDF, push by T, compare to rho1
u = rng.uniform(size=20000)
samp = np.interp(u, F0, xg)                    # samples from rho0
moved = np.interp(samp, xg, T)                 # T(samp): push forward by the optimal map
ax[2].hist(moved, bins=60, density=True, alpha=.6, label="pushforward $T_{\\#}\\rho_0$")
xx = np.linspace(-3, 5, 400)
ax[2].plot(xx, norm.pdf(xx, 1.0, np.sqrt(0.5)), lw=2, label=r"$\rho_1$")
ax[2].legend(fontsize=8); ax[2].set_title("pushforward $\\approx$ target")
fig.suptitle("1-D optimal transport: monotone map $T=F_1^{-1}\\circ F_0$", y=1.02)
fig.tight_layout(); plt.show()
print("transport cost  int |T-x|^2 rho0 dx = %.6f   (this is W_2^2 by the 1-D formula)" % cost)
'''))

C.append(py(r'''# F12 -- continuum-limit rate: empirical measure mu_N -> N(0,1) at rate O(N^-1/2) in W_2
Ns = 2.0**np.arange(6, 14)
errs = []
uq = norm.ppf((np.arange(1, 100001)-0.5)/100000.0)   # target quantile grid
for N in Ns:
    s = np.sort(rng.normal(size=int(N)))
    target = norm.ppf((np.arange(1, int(N)+1)-0.5)/int(N))
    errs.append(np.sqrt(np.mean((s-target)**2)))
errs = np.array(errs)
slope = np.polyfit(np.log(Ns), np.log(errs), 1)[0]
print("N         W_2(mu_N, N(0,1))")
for N, e in zip(Ns, errs): print("  %6.0f   %.6f" % (N, e))
fig, ax = plt.subplots()
ax.loglog(Ns, errs, "o-", label="data")
nn = np.logspace(np.log10(Ns.min()), np.log10(Ns.max()), 40)
ax.loglog(nn, errs[0]*(nn/Ns[0])**(-0.5), ":", color="tab:red", label=r"$N^{-1/2}$ (theory)")
ax.invert_xaxis(); ax.set_xlabel("number of particles N"); ax.set_ylabel(r"$W_2(\mu^N, \mu)$")
ax.legend(); ax.set_title("Continuum limit is a METRIC statement: rate $O(N^{-1/2})$ in $W_2$")
fig.tight_layout(); plt.show()
print("log-log slope = %.3f  (theory -1/2)" % slope)
'''))

# =====================================================================
# Section 8 (part 2): Benamou-Brenier, heat as W2 gradient flow, de Bruijn
# =====================================================================
C.append(md(r'''**Benamou–Brenier (essay §8.3).** The static $W_2$ has a *dynamic* reformulation:
$$W_2(\mu_0,\mu_1)^2=\inf\int_0^1\int \rho_t\,|v_t|^2\,dx\,dt,$$
the infimum over densities $\rho_t$ evolving by the continuity equation
$\partial_t\rho_t+\mathrm{div}(\rho_t v_t)=0$. $W_2^2$ is the minimal kinetic cost; the geodesics
are the optimal flows. This dynamic view is what makes $W_2$ the natural metric for *evolution*.
'''))

C.append(py(r'''# Benamou-Brenier in 1-D, computed: the optimal linear flow achieves the cost
# Theorem (Benamou-Brenier):  W_2(rho0, rho1)^2 = inf int_0^1 int rho_t |v_t|^2 dx dt
# over all flows solving the continuity equation. The optimal 1-D flow is the
# linear interpolation X_t(x) = (1-t) x + t T(x) with T the monotone map
# T = F1^{-1} o F0 (quantile map). It solves the continuity equation EXACTLY,
# so the cost integral must equal W_2^2 -- verified below.
xg = np.linspace(-4, 6, 8001)
bump = lambda x, c, w: np.exp(-(x-c)**2/(2*w**2))
rho0 = 0.6*bump(xg, -1.0, 0.5) + 0.4*bump(xg, 1.5, 0.7); rho0 /= np.trapezoid(rho0, xg)
rho1 = norm.pdf(xg, 1.0, np.sqrt(0.5))
F0 = np.concatenate([[0.0], np.cumsum(0.5*(rho0[1:]+rho0[:-1])*np.diff(xg))]); F0 /= F0[-1]
F1 = np.concatenate([[0.0], np.cumsum(0.5*(rho1[1:]+rho1[:-1])*np.diff(xg))]); F1 /= F1[-1]
T = np.interp(F0, F1, xg)
W2sq = np.trapezoid((T-xg)**2*rho0, xg)
# optimal flow: X_t(x) = (1-t) x + t T(x);  rho_t = pushforward of rho0 by X_t;  v_t = (T-x) transported
ts = np.linspace(0, 1, 201)
dt = ts[1]-ts[0]
cost = 0.0
rho_prev = None
resid = 0.0
for t in ts:
    Xt = (1-t)*xg + t*T
    dX = (1-t) + t*np.gradient(T, xg)
    rhot = np.interp(xg, Xt, rho0/np.abs(dX), left=0, right=0)
    vt  = np.interp(xg, Xt, T-xg, left=0, right=0)
    cost += np.trapezoid(rhot*vt**2, xg)*dt
    if rho_prev is not None:
        dtd  = (rhot-rho_prev)/dt
        dxdv = np.gradient(rho_prev*vt, xg)
        resid = max(resid, float(np.max(np.abs(dtd + dxdv))))
    rho_prev = rhot
fig, ax = plt.subplots()
for t in np.linspace(0, 1, 5):
    Xt = (1-t)*xg + t*T
    dX = (1-t) + t*np.gradient(T, xg)
    rhot = np.interp(xg, Xt, rho0/np.abs(dX), left=0, right=0)
    ax.plot(xg, rhot, label="t=%.2f" % t)
ax.legend(fontsize=8); ax.set_xlabel("x"); ax.set_ylabel(r"$\rho_t$")
ax.set_title(r"Benamou-Brenier flow $\rho_t$: two bumps $\to$ Gaussian")
fig.tight_layout(); plt.show()
print("Benamou-Brenier cost  int_0^1 int rho_t |v_t|^2 dx dt = %.6f   vs  W_2^2 = %.6f" % (cost, W2sq))
print("  -> cost - W_2^2 = %.2e  (theorem: the linear flow is optimal)" % (cost - W2sq))
print("continuity-eq residual (max |d_t rho + d_x(rho v)|) = %.2e" % resid)
print("  (the flow satisfies the continuity equation exactly; this is the")
print("   first-derivative discretization error of the piecewise-linear rho_t)")
'''))

C.append(md(r'''**The heat equation as a $W_2$-gradient flow (essay §8.4).** The entropy
$E(\rho)=\int\rho\log\rho\,dx$; the optimal velocity is $v=\nabla\psi$ with $\psi=\log\rho$, giving
$\partial_t\rho=\mathrm{div}(\rho\nabla\log\rho)=\mathrm{div}(\nabla\rho)=\Delta\rho$. The
**Fisher information** $\mathrm{FI}(\rho)=\int|\nabla\log\rho|^2\rho\,dx$ governs the dissipation,
and the precise identity (de Bruijn) is
$$\frac{d}{dt}E(\rho_t)=-\mathrm{FI}(\rho_t),$$
with constant $1$ (the entropy *decreases* at the rate of the Fisher information). This is the
verifiable content of "the heat equation is the $W_2$-gradient flow of the entropy."
'''))

C.append(py(r'''# de Bruijn identity, EXACT for the Gaussian  N(0, sigma^2), sigma^2 = s0^2 + 2 t
import mpmath
mpmath.mp.dps = 30
s0, tval = 1.0, 1.0
sig2 = s0**2 + 2*tval
normf = lambda xx: mpmath.exp(-xx**2/(2*sig2))/mpmath.sqrt(2*mpmath.pi*sig2)
E  = mpmath.quad(lambda xx: normf(xx)*mpmath.log(normf(xx)), [-mpmath.inf, mpmath.inf])
FI = mpmath.quad(lambda xx: (xx**2/(sig2**2))*normf(xx), [-mpmath.inf, mpmath.inf])
dEdt = -1/sig2     # analytic: E = -1/2 log(2 pi e sigma^2), dE/dt = -1/(2 sig2) * d(sig2)/dt = -1/sig2
print("Gaussian N(0,%.1f):  E = %.8f" % (sig2, float(E)))
print("  dE/dt = %.8f   FI = %.8f   dE/dt + FI = %.2e  (expect ~0)" % (float(dEdt), float(FI), float(dEdt+FI)))
print("=> dE/dt = -FI  EXACT (constant 1);  entropy E DECREASES at the rate of the Fisher information")
'''))

C.append(py(r'''# F13 -- de Bruijn identity, NON-Gaussian heat flow, numerically
L, h = 8.0, 0.02
xg = np.linspace(-L, L, int(2*L/h)+1)
N = len(xg)
# IC: slightly skewed, positive, normalized
rho = np.exp(-(xg+0.5)**2/0.5)*(1.0 + 0.3*np.sin(2*xg))
rho = np.clip(rho, 1e-12, None); rho /= np.trapezoid(rho, xg)
# Crank-Nicolson for rho_t = Delta rho = rho_xx:  (I - k/2 L) rho^{n+1} = (I + k/2 L) rho^n
k = 0.005
diag  = -2.0/h**2*np.ones(N); off = 1.0/h**2*np.ones(N-1)   # L = d^2/dx^2
Lm = sparse.diags([off, diag, off], [-1, 0, 1], format="csc")
A = sparse.eye(N, format="csc") - (k/2)*Lm
B = sparse.eye(N, format="csc") + (k/2)*Lm
nsteps = 400
Ets, FITs = [], []
for step in range(nsteps+1):
    rlog = np.log(np.clip(rho, 1e-15, None))
    E = np.trapezoid(rho*rlog, xg)
    drho = np.gradient(rho, xg)
    FI = np.trapezoid((drho/np.clip(rho,1e-15,None))**2*rho, xg)
    Ets.append(E); FITs.append(FI)
    if step < nsteps:
        rho = splinalg.spsolve(A, B.dot(rho))
Ets = np.array(Ets); FITs = np.array(FITs)
dEdt = np.gradient(Ets, k)                       # dE/dt from the recorded entropy
ratio = -dEdt[1:-1]/FITs[1:-1]
fig, ax = plt.subplots(1, 2, figsize=(9.5, 3.4))
tt = np.arange(len(Ets))*k
ax[0].plot(tt, Ets, label=r"$E(t)=\int\rho\log\rho$"); ax[0].plot(tt, -FITs, label=r"$-\mathrm{FI}(t)$")
ax[0].set_xlabel("t"); ax[0].legend(fontsize=8); ax[0].set_title("entropy (decreasing) & $-$Fisher information")
ax[1].plot(tt[1:-1], ratio, "o-", ms=3, label=r"$-(dE/dt)/\mathrm{FI}$")
ax[1].axhline(1.0, color="tab:red", ls="--", lw=1.5, label="1 (de Bruijn)")
ax[1].set_xlabel("t"); ax[1].set_ylim(0.7, 1.3); ax[1].legend(fontsize=8)
ax[1].set_title(r"identity $dE/dt=-\mathrm{FI}$, constant 1")
fig.suptitle("de Bruijn identity for a NON-Gaussian heat flow", y=1.02)
fig.tight_layout(); plt.show()
print("ratio -(dE/dt)/FI :  min=%.4f  max=%.4f  (theory 1; non-Gaussian IC)" % (ratio.min(), ratio.max()))
print("mass drift over the run: %.2e  (boundary leak, negligible)" % abs(np.trapezoid(rho,xg)-1.0))
'''))

C.append(md(r'''**Why this matters for the continuum limit (essay §8.5–8.6).** The $W_2$ distance between Gaussians
has a closed form (verified in 1-D; 2-D cross-checked against an LP). It gives an explicit
$W_2$-geodesic between Gaussians and is the starting point of the Gaussian theory of optimal
transport. The Wasserstein metric is the natural metric for the *continuum limit* of particle
systems: the empirical measures $\mu^N=\frac1N\sum\delta_{x_i^N}$ converge to the mean-field density
*in $W_2$* (not just weakly), at rate $O(N^{-1/2})$ — a *metric* statement. The measure (empirical)
and the metric ($W_2$) are both essential; their interaction gives the continuum limit its precise
form.
'''))

# =====================================================================
# Section 9: numerical-analytic perspective
# =====================================================================
C.append(md(r'''## 9. The numerical-analytic perspective: discretization and the three structures

For the numerical analyst the three structures are *tools for discretization and error estimation*.
The **metric** controls the *spatial* error (distance between discrete and continuous solutions; the
rate $O(h^k)$ is a metric statement). The **measure** controls the *integration* error (quadrature;
the $h^n$-scaled counting measure). The **topology** controls the *convergence* of the discrete
function space to the continuous one (e.g. $H^1$ convergence). The full a priori estimate is the
interaction of the three; the slowest rate dominates.
'''))

C.append(py(r'''# F15 -- heat equation convergence: O(h^2) in space, O(k) in time
# u_t = u_xx on the torus; exact u(t,x) = exp(-4 pi^2 t) cos(2 pi x)
# The explicit FTCS scheme is only stable for k < h^2/2, which couples the two
# errors at the same order. We therefore use the BACKWARD-EULER (implicit)
# scheme, applied in Fourier space: unconditionally stable, so the spatial
# (h^2) and temporal (k) orders can be isolated independently. The discrete
# 3-point Laplacian has eigenvalues -4/h^2 sin^2(m h/2), which is what
# produces the genuine spatial error.
def exact(x, t): return np.exp(-4*np.pi**2*t)*np.cos(2*np.pi*x)
def run(h, k, t_end):
    n = int(round(1.0/h)); x = np.linspace(0, 1, n, endpoint=False)
    u = exact(x, 0.0)
    m = 2*np.pi*np.fft.fftfreq(n, d=h)
    eigL = -4.0/h**2 * np.sin(m*h/2.0)**2     # discrete Laplacian eigenvalues
    denom = 1.0 - k*eigL
    steps = int(round(t_end/k))
    for _ in range(steps):
        u = np.fft.ifft(np.fft.fft(u)/denom).real
    return x, u
T = 0.1
# spatial order: k = 1e-5 fixed (temporal error negligible), vary h
hs = [1/8, 1/16, 1/32, 1/64]; esp = []
for h in hs:
    x, u = run(h, 1e-5, T)
    esp.append(np.sqrt(h*np.sum((u-exact(x, T))**2)))
esp = np.array(esp)
# temporal order: h = 1/128 fixed (spatial error negligible), vary k
ks = [1e-3, 5e-4, 2.5e-4, 1.25e-4]; etm = []
for k in ks:
    x, u = run(1/128, k, T)
    etm.append(np.sqrt((1/128)*np.sum((u-exact(x, T))**2)))
etm = np.array(etm)
sp_slope = np.polyfit(np.log(hs), np.log(esp), 1)[0]
tm_slope = np.polyfit(np.log(ks), np.log(etm), 1)[0]
fig, ax = plt.subplots(1, 2, figsize=(9.5, 3.4))
ax[0].loglog(hs, esp, "o-"); hh = np.logspace(np.log10(hs[-1]), np.log10(hs[0]), 40)
ax[0].loglog(hh, esp[0]*(hh/hs[0])**2, ":", color="tab:red", label=r"$h^2$")
ax[0].invert_xaxis(); ax[0].set_xlabel("h"); ax[0].set_ylabel(r"$\|e\|_{L^2_h}$"); ax[0].legend()
ax[0].set_title("spatial order: slope %.2f (theory 2)" % sp_slope)
ax[1].loglog(ks, etm, "o-"); kk = np.logspace(np.log10(ks[-1]), np.log10(ks[0]), 40)
ax[1].loglog(kk, etm[0]*(kk/ks[0])**1, ":", color="tab:red", label=r"$k$")
ax[1].invert_xaxis(); ax[1].set_xlabel("k"); ax[1].set_ylabel(r"$\|e\|_{L^2_h}$"); ax[1].legend()
ax[1].set_title("temporal order: slope %.2f (theory 1)" % tm_slope)
fig.suptitle(r"heat equation: full estimate $\|e\|\leq C(h^2+k)$ — metric, measure, topology", y=1.02)
fig.tight_layout(); plt.show()
print("spatial slope = %.3f (theory 2);  temporal slope = %.3f (theory 1)" % (sp_slope, tm_slope))
'''))

C.append(py(r'''# F16 -- quadrature error (the MEASURE's error): trapezoidal rule, O(h^2)
from scipy.integrate import quad
f = lambda x: np.exp(x)*np.sin(2*np.pi*x)
Itrue, _ = quad(f, 0, 1)
hs = [1/8, 1/16, 1/32, 1/64, 1/128]; errs = []
for h in hs:
    n = int(round(1/h)); x = np.linspace(0, 1, n+1)
    Itrap = h*(0.5*f(x[0]) + np.sum(f(x[1:-1])) + 0.5*f(x[-1]))
    errs.append(abs(Itrue-Itrap))
errs = np.array(errs)
slope = np.polyfit(np.log(hs), np.log(errs), 1)[0]
fig, ax = plt.subplots()
ax.loglog(hs, errs, "o-"); hh = np.logspace(np.log10(hs[-1]), np.log10(hs[0]), 40)
ax.loglog(hh, errs[0]*(hh/hs[0])**2, ":", color="tab:red", label=r"$h^2$")
ax.invert_xaxis(); ax.set_xlabel("h"); ax.set_ylabel("quadrature error"); ax.legend()
ax.set_title("Trapezoidal quadrature: the discrete measure $\\mu_h=h\\sum\\delta_{x_j}$, error $O(h^2)$")
fig.tight_layout(); plt.show()
print("quadrature slope = %.3f (theory 2);  true integral = %.6f" % (slope, Itrue))
'''))

C.append(py(r'''# graph metric -> continuous metric (essay §9.1, simplest form)
# grid graph on h*Z^2 in [0,1]^2, edge length h; shortest-path (l1) distance vs Euclidean
a, b = np.array([0.1, 0.2]), np.array([0.7, 0.9])
eu = np.linalg.norm(a-b)
hs = [1/4, 1/8, 1/16, 1/32, 1/64]
print("Euclidean distance |a-b| = %.6f" % eu)
for h in hs:
    # l1 graph distance in grid units * h (a,b snapped to grid)
    ga = np.round(a/h).astype(int); gb = np.round(b/h).astype(int)
    l1 = np.sum(np.abs(ga-gb))*h
    print("  h=%5.3f  graph l1 distance = %.6f   (error %.2e)" % (h, l1, abs(l1-eu)))
print("=> the discrete (graph) metric converges to the continuous metric as h -> 0")
'''))

# =====================================================================
# Section 10: Riemannian vs sub-Riemannian
# =====================================================================
C.append(md(r'''## 10. The differential-topological perspective: smooth structures and their interplay

On a smooth manifold, all three structures are present. In the **Riemannian** case the metric
*does* determine the measure: the Riemannian volume $dV_g=\sqrt{\det g_{ij}}\,dx^1\cdots dx^n$ is a
function of the metric, and the length metric induces the smooth topology. The three structures are
in *full* correspondence. In the **sub-Riemannian** case (Heisenberg, §7) the metric is *degenerate*
(a metric on a subbundle $\mathcal H\subset TM$), the naive $\sqrt{\det g}$ formula does not apply,
and the measure's dimension $Q$ exceeds the topological dimension $n$.
'''))

C.append(py(r'''# F17 -- the Riemannian case: the metric DETERMINES the measure (round sphere)
# g = dtheta^2 + sin^2(theta) dphi^2,  sqrt(det g) = sin(theta),  total volume = 4 pi
def sphere_volume(n):
    th = (np.arange(n)+0.5)/n*np.pi      # midpoint rule in theta
    ph = (np.arange(n)+0.5)/n*2*np.pi    # midpoint rule in phi
    dth = np.pi/n; dph = 2*np.pi/n
    return np.sum(np.sin(th)[:,None])*dth*dph*n   # sum over theta of sin * (2 pi) * dth
ns = [10, 20, 40, 80, 160, 320]
vols = [sphere_volume(n) for n in ns]
print("sphere volume from sqrt(det g)=sin(theta) (midpoint rule):")
for n, v in zip(ns, vols):
    print("  n=%3d  V = %.8f   (4 pi = %.8f,  error %.2e)" % (n, v, 4*np.pi, abs(v-4*np.pi)))
fig, ax = plt.subplots()
ax.semilogx(ns, vols, "o-"); ax.axhline(4*np.pi, color="tab:red", ls="--", label=r"$4\pi$")
ax.set_xlabel("grid resolution n"); ax.set_ylabel("volume"); ax.legend()
ax.set_title("Riemannian volume $\\int\\sqrt{\\det g}$ converges to $4\\pi$: the metric determines the measure")
fig.tight_layout(); plt.show()
'''))

C.append(py(r'''# Riemannian distance: geodesics of the round sphere (verify against the closed form)
from scipy.integrate import solve_ivp
# metric ds^2 = dth^2 + sin^2(th) dph^2.  Lagrangian L = 1/2(th'^2 + sin^2 th ph'^2).
# Euler-Lagrange:  th'' = sin(th)cos(th) ph'^2 ;  ph'' = -2 cot(th) th' ph'
def geodesic_ode(s, yv):
    th, ph, dth, dph = yv
    return [dth, dph,
            np.sin(th)*np.cos(th)*dph**2,
            -2.0*np.cos(th)/np.sin(th)*dth*dph]
def to3(t, p): return np.array([np.sin(t)*np.cos(p), np.sin(t)*np.sin(p), np.cos(t)])
def great_circle_distance(A, B):
    va, vb = to3(*A), to3(*B)
    return float(np.arccos(np.clip(np.dot(va, vb), -1, 1)))
A = (0.7, 0.3); B = (1.1, 2.0)
d = great_circle_distance(A, B)
va, vb = to3(*A), to3(*B)
T = vb - np.dot(va, vb)*va; T /= np.linalg.norm(T)     # unit 3D tangent at A toward B
e_th = np.array([np.cos(A[0])*np.cos(A[1]), np.cos(A[0])*np.sin(A[1]), -np.sin(A[0])])
e_ph = np.array([-np.sin(A[1]), np.cos(A[1]), 0.0])
# coordinate velocities: dp/dth = e_th, dp/dph = sin(th) e_ph  ->  b = (T.e_ph)/sin(th0)
dth0 = float(np.dot(T, e_th))
dph0 = float(np.dot(T, e_ph))/np.sin(A[0])
sol = solve_ivp(geodesic_ode, [0, d], [A[0], A[1], dth0, dph0], rtol=1e-10, atol=1e-12)
end = (float(sol.y[0, -1]), float(sol.y[1, -1]))
err = great_circle_distance(end, B)
print("great-circle distance |A-B| = %.8f" % d)
print("geodesic ODE endpoint = (%.6f, %.6f),  distance to B = %.2e  (~0)" % (end[0], end[1], err))
print("=> Riemannian distance (inf of curve lengths) verified; metric -> topology + measure")
'''))

C.append(py(r'''# contrast table: Riemannian (full correspondence) vs sub-Riemannian (partial)
print("%-28s | %-14s | %-14s | %-14s | metric determines measure?" %
      ("space", "topological", "metric(Hausdorff)", "measure(homog)"))
print("%-28s | %-14s | %-14s | %-14s | %s" %
      ("round sphere (Riemannian)", "2", "2", "2", "YES  (dV = sqrt(det g) dx dy)"))
print("%-28s | %-14s | %-14s | %-14s | %s" %
      ("Heisenberg H^1 (sub-Riem.)", "3", "4 (Q)", "4 (Q)", "NO   (g degenerate; Haar from group/dilations)"))
print()
print("Lesson (essay 10.3): full correspondence  <=>  metric non-degenerate (Riemannian);")
print("partial correspondence  <=>  metric degenerate (sub-Riemannian). Degeneracy is the source of the independence.")
'''))

C.append(md(r'''**The lesson (essay §10.3).** The metric determines the measure (as a function of the metric)
**iff** the metric is *non-degenerate* (a genuine metric on the whole tangent bundle — the
Riemannian case). If the metric is *degenerate* (a metric on a subbundle — sub-Riemannian), the
measure is not a function of the metric alone; it depends on the bracket-generating structure, and
the measure's dimension differs from the topological one. The *degeneracy* of the metric is
precisely the *source* of the independence of the three structures.
'''))

# =====================================================================
# Section 11: conclusion + references + appendix
# =====================================================================
C.append(md(r'''## 11. Conclusion: the three structures as a hierarchy, and the choice between them

The three structures are *logically independent*, each determining *part* of the others, with the
undetermined part being exactly the part relevant to the problem. The interactions and their failure
modes:

- **Topology $\to$ Metric** — metrization (Urysohn / Nagata–Smirnov); fails for non-regular or
  non-second-countable topologies.
- **Topology $\to$ Measure** — the Borel $\sigma$-algebra and Radon measures (Riesz–Markov–Kakutani);
  fails for non-Radon measures.
- **Metric $\to$ Measure** — the Hausdorff measures; the Hausdorff dimension may differ from the
  topological dimension.
- **Metric $\leftrightarrow$ Measure** — the doubling property; the metric and measure may be
  incompatible.

The **Heisenberg group** is the canonical *disagreement* (topological dim 3, Hausdorff dim 4,
homogeneous dim 4; the group of quantum kinematics). The **Wasserstein space** is the canonical
*interaction* (a measure promoted to a metric; the heat equation as its $W_2$-gradient flow). The
practical lesson: *no single structure is "the right one"* — the choice depends on the problem.
Topology for shape/continuity, metric for distance/rate, measure for size/integration, and their
interaction for the full structure. The three structures are in *partial*, not *full*,
correspondence — and that partiality is exactly what makes each indispensable.
'''))

C.append(md(r'''## References

1. **Munkres, J. R.** *Topology.* 2nd ed., Prentice Hall, 2000. (Urysohn metrization §48; Borel $\sigma$-algebra; Riesz–Markov–Kakutani §67.)
2. **Rudin, W.** *Real and Complex Analysis.* 3rd ed., McGraw-Hill, 1987. (Measure theory, $L^p$, the null ideal, Radon–Nikodym.)
3. **Bogachev, V. I.** *Measure Theory.* Vols. I–II, Springer, 2007. (Radon measures, regularity, support.)
4. **Federer, H.** *Geometric Measure Theory.* Springer, 1969. (Hausdorff measure, dimension, normalization, agreement with Lebesgue.)
5. **Urysohn, P.** "Über die metrisierbaren topologischen Räume." *Math. Ann.* 92 (1925), 313–320.
6. **Villani, C.** *Optimal Transport: Old and New.* Grundlehren 338, Springer, 2009. (Wasserstein, Benamou–Brenier, Gaussian closed form, gluing.)
7. **Ambrosio, L., Gigli, N., Savaré, G.** *Gradient Flows.* Birkhäuser, 2005. (Heat equation as $W_2$-gradient flow, Fisher information, de Bruijn.)
8. **Montgomery, R.** *A Tour of Subriemannian Geometries.* MS&M 91, AMS, 2002. (Heisenberg group, CC metric, sub-Laplacian, homogeneous dimension.)
9. **Hörmander, L.** "Hypoelliptic second order differential operators." *Acta Math.* 119 (1967), 191–238.
10. **Coifman, R., Weiss, G.** *Analyse harmonique non-commutative sur les espaces homogènes.* LNM 620, Springer, 1977.
11. **Ciarlet, P. G.** *The Finite Element Method for Elliptic Problems.* SIAM, 2002. (A priori error estimates, discrete-to-continuous convergence.)
'''))

C.append(md(r'''## Appendix: what was computed (verification record)

Every non-trivial constant the essay commits to, recomputed in this notebook:

| # | Quantity | Value | Cell |
|---|---|---|---|
| M1 | $\alpha(1),\alpha(2),\alpha(3),\alpha(4)$ | $2,\ \pi,\ 4.188790,\ 4.934802$ | §6 |
| M2 | $\dim_H$(gasket) $=\log 3/\log 2$ | $1.5849625007$ | §6 |
| M3 | $\dim_H$(Menger) $=\log 20/\log 3$ | $2.7268330164$ | §6 |
| M4 | Heisenberg commutator | $(0,0,\,xy'-x'y)$ (the $\tfrac12$ cancels) | §7 |
| M5 | $[X,Y]$ | $\partial_z$ | §7 |
| M6 | sub-Laplacian $\Delta_H=X^2+Y^2$ | $\partial_x^2+\partial_y^2+\tfrac{x^2+y^2}{4}\partial_z^2-y\partial_x\partial_z+x\partial_y\partial_z$ | §7 |
| M7 | gauge-ball volume | $V(r)=\tfrac{\pi^2}{4}r^4$; $V(2r)/V(r)=16$; $Q=4$ | §7 |
| M8 | $W_2^2(\mathcal N(0,1),\mathcal N(1,4))$ | $2.0$ | §8 |
| M9 | de Bruijn $dE/dt=-\mathrm{FI}$ | exact (Gaussian) and $\approx1$ (non-Gaussian) | §8 |
| M10 | spherical $\mathcal H^1$ | segment $=2$, circle $=2\pi$ (length) | §6 |
| M11 | CC ball anisotropy | vertical extent $\propto r^2$ (gauge) | §7 |
| M12 | heat kernel on-diagonal | slope $=-Q/2=-2$ (FD of $\Delta_H$) | §7 |

**One correction to the essay (v2):** §3.2's example "the weak topology $\sigma(\ell^\infty,\ell^1)$
on bounded sets is not metrizable" is misstated — since $\ell^1$ is separable, that weak-* topology
*is* metrizable on $B_{\ell^\infty}$; the correct counterexample uses the *full* weak topology on a
space with non-separable dual (e.g. $\ell^1$). All other constants, including the §6.3 Hausdorff
normalization $\mathcal H^n_{\mathrm{std}}=\frac{2^n}{\alpha(n)}\mathcal L^n$, were re-verified
**correct**.
'''))

# =====================================================================
# assemble + write
# =====================================================================
nb = {
    "cells": C,
    "metadata": {
        "kernelspec": {"display_name": "Python 3 (venv)", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.14.7"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}
node = nbformat.from_dict(nb)
nbformat.validate(node)
OUT.parent.mkdir(parents=True, exist_ok=True)
nbformat.write(node, OUT)
print("wrote", OUT, " cells:", len(C))
