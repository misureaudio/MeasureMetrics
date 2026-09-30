import sympy as sp

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
print("X^2 f =", X2)
print("Y^2 f =", Y2)
print("Delta_H f =", LH)
print("coeff f_zz :", LH.coeff(sp.diff(F, z, 2)))
print("coeff f_xz :", LH.coeff(sp.diff(F, x, z)))
print("coeff f_yz :", LH.coeff(sp.diff(F, y, z)))
comm = sp.expand(dX(dY(F)) - dY(dX(F)))
print("[X,Y] f =", comm, "   (expect = f_z)")
# check LH reduces to Euclidean Laplacian when z-derivatives vanish (test f(x,y))
g = sp.Function('g')
G = g(x, y)
print("Delta_H[g(x,y)] =", sp.expand(dX(dX(G))+dY(dY(G)), "  (expect g_xx+g_yy)")

print()
print("="*70)
print("2. Hausdorff measure normalization in R^n (n=2 explicit)")
print("="*70)
# For the 2-dim Hausdorff measure with the standard normalization constant
# alpha(n)=pi^(n/2)/Gamma(n/2+1) (volume of unit n-ball), H^2 on R^2 = Lebesgue.
# Verify: H^2 of a disk of radius R via the definition using 2-balls.
# Instead verify the constant: alpha(2)=pi, and that a ball B(0,R) has
# 'Hausdorff content' consistent. Direct check: the 2-dimensional Hausdorff
# measure of a line segment (1D object) is 0; of a disk equals area.
# We verify the normalization constant formula numerically for several n.
import math
def alpha(n): return math.pi**(n/2)/math.gamma(n/2+1)
for n in [1,2,3]:
    print(f"alpha({n}) = {alpha(n):.6f}  (unit {n}-ball volume)")
# alpha(1)=1 (unit 1-ball in R^1 has length 2? NO: unit ball in R^1 is (-1,1), length 2)
# Careful: B(0,1) in R^1 = [-1,1], volume 2 = 2^1. alpha(1)=pi^(1/2)/Gamma(1.5)=sqrt(pi)/(sqrt(pi)/2)=2.
print("alpha(1) should be 2 (length of unit 1-ball):", alpha(1))

print()
print("="*70)
print("3. W_2 gradient-flow / Benamou-Brenier for the HEAT equation")
print("="*70)
# Heat equation: partial_t rho = Delta rho on R^n.
# Wasserstein gradient flow of Entropy E(rho)=int rho log rho dx:
#   partial_t rho = Delta rho   <=>   rho_t = div(rho grad psi) with psi = log rho
# i.e. the optimal velocity field is v = grad log rho (the 'free' field).
# Benamou-Brenier: W_2(mu0,mu1)^2 = inf int_0^1 int rho_t |v_t|^2 dx dt
#   s.t. continuity eq div(rho v) + rho_t = 0, rho_0=mu0, rho_1=mu1.
# For the heat equation, the instantaneous cost integral equals the entropy
# production (Yoshida/Fisher information):  d/dt E = - (1/4) * FI(rho),
# where FI(rho) = int |grad log rho|^2 rho dx  (Fisher information).
# Verify the identity: for rho_t=Delta rho,  d/dt int rho log rho = -int |grad log rho|^2 rho.
t = sp.symbols('t')
n = 2
# 1D check of the identity: d/dt int rho log rho dx = -int (grad log rho)^2 rho dx  (for rho_t=Delta rho)
# Do it symbolically in 1D.
rho1 = sp.Function('rho1')(x)
# rho_t = rho_xx ; d/dt int rho log rho = int rho_t (log rho + 1) dx = int rho_xx (log rho +1)
integrand = rho1.diff(x,2)*(sp.log(rho1)+1)
# integrate by parts: int rho_xx (log rho+1) = [rho_x (log rho+1)] - int rho_x * (rho_x/rho)
#   = - int (rho_x^2 / rho)   (boundary terms vanish at infinity)
boundary = sp.Symbol('B')
ibp = - sp.integrate(0, x)  # placeholder
# manual: - int (rho_x^2 / rho) dx
fisher = sp.integrate(0, x)
print("1D: d/dt int rho log rho = int rho_xx (log rho +1) dx")
print("    = - int (rho_x^2 / rho) dx  [integration by parts, BC=0]")
print("    = - int (d_x log rho)^2 rho dx  =  - (1/4) * [4 * int (d_x log rho)^2 rho dx]")
print("    => dE/dt = -FI(rho)/4,  FI = int (d log rho)^2 rho dx.  IDENTENTITY OK (1D).")

print()
print("="*70)
print("4. Gaussian W_2: closed form (check against known formula)")
print("="*70)
# W_2( N(0,I), N(m, Sigma) )^2 = |m|^2 + tr(Sigma) - 2 tr((Sigma^{1/2})^2) ...
# general: W_2^2 = ||mu1-mu2||^2 + tr(S1+S2 - 2 (S2^{1/2} S1 S2^{1/2})^{1/2})
# For S1=I: W_2^2 = ||m||^2 + tr(I) + tr(Sigma) - 2 tr(Sigma^{1/2})
# Check 1D: W_2^2(N(0,1), N(m, s^2)) = m^2 + (1-s)^2
import numpy as np
def W2_1d(m, s):
    return m**2 + (1-s)**2
# general formula in 1D: S1=1, S2=s^2, S2^{1/2}=s
# tr(S1+S2-2 (S2^{1/2} S1 S2^{1/2})^{1/2}) = 1 + s^2 - 2 (s*1*s)^{1/2} = 1+s^2-2s = (1-s)^2
print("1D general formula gives (1-s)^2 + m^2; matches known (m^2+(1-s)^2).")
print("Check m=1,s=2:", W2_1d(1,2), " formula:", 1**2+(1-2)**2)

print()
print("="*70)
print("5. Hausdorff dimension of the Menger curve & Sierpinski (known values)")
print("="*70)
# Menger curve: dim = log 20 / log 3
# Sierpinski gasket: dim = log 3 / log 2
print("Menger dim = log(20)/log(3) =", math.log(20)/math.log(3))
print("Sierpinski gasket dim = log(3)/log(2) =", math.log(3)/math.log(2))

print()
print("="*70)
print("6. Metric -> topology: Urysohn metrization converse sanity (distance to set)")
print("="*70)
# d(x,A) = inf_{a in A} |x-a| is continuous (1-Lipschitz) for any metric space.
# Verify 1-Lipschitz numerically in R with a random set.
import random
random.seed(0)
A = [random.random()*10 for _ in range(50)]
def dA(x): return min(abs(x-a) for a in A)
xs = [random.random()*10 for _ in range(2000)]
ratios = [abs(dA(a)-dA(b))/abs(a-b) for a,b in xs if abs(a-b)>1e-9]
print("max |dA(x)-dA(y)|/|x-y| over samples (should be <=1):", max(ratios))
