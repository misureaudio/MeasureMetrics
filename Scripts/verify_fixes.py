import sympy as sp

print("="*70)
print("A. Heisenberg group commutator [g,h] (group law z+z'+1/2(xy'-x'y))")
print("="*70)
x, y, z, xp, yp, zp = sp.symbols("x y z xp yp zp")
def mul(a, b):
    # a=(a1,a2,a3), b=(b1,b2,b3); law (p1,p2,p3).(q1,q2,q3)=(p1+q1,p2+q2,p3+q3+1/2(p1 q2 - q1 p2))
    return (sp.expand(a[0]+b[0]), sp.expand(a[1]+b[1]),
            sp.expand(a[2]+b[2] + sp.Rational(1,2)*(a[0]*b[1] - b[0]*a[1])))
def inv(a):
    # (x,y,z)^{-1} = (-x,-y,-z)  (verify below)
    return (-a[0], -a[1], -a[2])
g  = (x, y, z)
h  = (xp, yp, zp)
# verify inverse
print("g*inv(g) =", tuple(sp.expand(c) for c in mul(g, inv(g))), " (expect (0,0,0))")
comm = mul(mul(mul(g, h), inv(g)), inv(h))
print("[g,h] =", tuple(sp.expand(c) for c in comm))
print("  -> z-component =", sp.expand(comm[2]), "  (is it x*yp - xp*y ?)",
      sp.simplify(comm[2] - (x*yp - xp*y)) == 0)

print()
print("="*70)
print("B. Entropy dissipation for the heat equation, Gaussian check")
print("="*70)
t, s0 = sp.symbols('t s0', positive=True)
n = 2  # dimension (symbolic n would be heavier; use n=2 and note the pattern)
s = 2*t + s0  # covariance param, s' = 2  =>  rho_t = Delta rho
# rho = (2 pi s)^(-n/2) exp(-|x|^2 / (2 s));  E = int rho log rho = (n/2) log(2 pi e s)
E = (n/2)*(sp.log(2*sp.pi*sp.E) + sp.log(s))
dEdt = sp.simplify(sp.diff(E, t))
# Fisher information FI = int rho |grad log rho|^2 = tr(Sigma)/s^2 ... = n/s
FI = n/s
print("dE/dt =", dEdt)
print("FI    =", FI)
print("dE/dt + FI =", sp.simplify(dEdt + FI), "  (expect 0  =>  dE/dt = -FI, constant 1)")

# differential entropy h = -E ;  de Bruijn: dh/dt = +FI  (for rho_t = Delta rho)
print("dh/dt =", sp.simplify(-dEdt), " = FI (constant 1).  [1/2 only if rho_t = (1/2)Delta rho]")

print()
print("="*70)
print("C. Hausdorff measure normalization: ball convention gives H^1([0,1])=1")
print("="*70)
# Ball convention: H^s_delta = inf sum alpha(s) r_i^s, cover by balls B(x_i,r_i), r_i<delta.
# In R^1, alpha(1)=2 (length of unit 1-ball). To cover [0,1] (length 1) by balls of
# radius r_i (each covers length 2 r_i): need sum 2 r_i >= 1, i.e. sum r_i >= 1/2.
# H^1([0,1]) = alpha(1) * (1/2) = 2 * 1/2 = 1 = Lebesgue.  Check:
alpha1 = 2.0
print("H^1([0,1]) =", alpha1*0.5, " (expect 1 = Lebesgue length).  OK")
import math
for s in [1,2,3]:
    print(f"alpha({s}) = pi^{s/2}/Gamma({s/2}+1) = {math.pi**(s/2)/math.gamma(s/2+1):.6f}")
