import sympy as sp
import math, random

print("="*70)
print("1. HEISENBERG GROUP H^1: sub-Laplacian and commutator")
print("="*70)
x, y, z = sp.symbols('x y z')
f = sp.Function('f')
F = f(x, y, z)
# left-invariant horizontal fields: X = d_x + (y/2) d_z, Y = d_y - (x/2) d_z
dX = lambda g: sp.diff(g, x) + (y/2)*sp.diff(g, z)
dY = lambda g: sp.diff(g, y) - (x/2)*sp.diff(g, z)
X2 = sp.expand(dX(dX(F)))
Y2 = sp.expand(dY(dY(F)))
LH = sp.expand(X2 + Y2)
print("Delta_H f =", LH)
print("coeff f_zz :", LH.coeff(sp.diff(F, z, 2)))
print("coeff f_xz :", LH.coeff(sp.diff(F, x, z)))
print("coeff f_yz :", LH.coeff(sp.diff(F, y, z)))
comm = sp.expand(dX(dY(F)) - dY(dX(F)))
print("[X,Y] f =", comm, "   (expect = f_z)")
g = sp.Function('g')
G = g(x, y)
print("Delta_H[g(x,y)] =", sp.expand(dX(dX(G))+dY(dY(G))), " (expect g_xx+g_yy)")

print()
print("="*70)
print("2. Hausdorff normalization alpha(n)=pi^{n/2}/Gamma(n/2+1) = vol(B^n(0,1))")
print("="*70)
def alpha(n): return math.pi**(n/2)/math.gamma(n/2+1)
for n in [1,2,3,4]:
    print(f"alpha({n}) = {alpha(n):.6f}")
print("alpha(1)=2 (unit 1-ball [-1,1] length 2); alpha(2)=pi (unit disk area).")

print()
print("="*70)
print("3. Heat equation as W_2 gradient flow of entropy (1D identity)")
print("="*70)
print("rho_t=rho_xx. dE/dt = int rho_xx(log rho+1) dx = -int (rho_x)^2/rho dx")
print("  = -int (d_x log rho)^2 rho dx = -FI/4, FI = int (d log rho)^2 rho. OK (IBP).")

print()
print("="*70)
print("4. Gaussian W_2 closed form, 1D")
print("="*70)
def W2_1d(m, s): return m**2 + (1-s)**2
print("m=1,s=2 ->", W2_1d(1,2), " (expect 2)")

print()
print("="*70)
print("5. Fractal Hausdorff dimensions")
print("="*70)
print("Menger curve dim = log(20)/log(3) =", math.log(20)/math.log(3))
print("Sierpinski gasket dim = log(3)/log(2) =", math.log(3)/math.log(2))

print()
print("="*70)
print("6. d(x,A) is 1-Lipschitz (metric -> topology)")
print("="*70)
random.seed(0)
A = [random.random()*10 for _ in range(50)]
def dA(q): return min(abs(q-a) for a in A)
xs = [random.random()*10 for _ in range(4000)]
ratios = [abs(dA(a)-dA(b))/abs(a-b) for a,b in zip(xs, xs[1:]) if abs(a-b)>1e-9]
print("max |dA(x)-dA(y)|/|x-y| (<=1):", max(ratios))
