import numpy as np, math

print("=== Entropy E(rho)=int rho log rho for 1D heat eq: dE/dt = -FI (constant 1)? ===")
# rho = N(0, s^2), s^2 = s0^2 + 2 t  (1D heat eq: variance grows at rate 2)
# E = int rho log rho = -(1/2) log(2 pi e s^2)   [differential entropy h = -E = (1/2)log(2 pi e s^2)]
# FI = int rho (d log rho)^2 = 1/s^2
s0 = 1.0
for t in [0.0, 0.05, 0.1, 0.3]:
    s2 = s0**2 + 2*t
    E = -0.5*math.log(2*math.pi*math.e*s2)
    s2p = s0**2 + 2*(t+1e-5)
    Ep = -0.5*math.log(2*math.pi*math.e*s2p)
    dEdt = (Ep-E)/1e-5
    FI = 1.0/s2
    print(f"t={t:4.2f}: dE/dt={dEdt:+.6f}  FI={FI:.6f}  dE/dt/(-FI)={dEdt/(-FI):.6f}")

print()
print("=== Hausdorff radius convention: H^s_delta = inf sum omega_s r_i^s, omega_s=pi^{s/2}/Gamma(s/2+1) ===")
def omega(s): return math.pi**(s/2)/math.gamma(s/2+1)
# H^1([0,1]): cover by one ball radius 0.5 -> omega_1 * 0.5^1
print("H^1([0,1]) =", omega(1)*0.5, " (expect 1 = Lebesgue length)")
# H^2(unit disk): cover by one ball radius 1 -> omega_2 * 1^2
print("H^2(disk)  =", omega(2)*1.0, " (expect pi = Lebesgue area)")
# H^3(unit ball): cover by one ball radius 1 -> omega_3 * 1^3
print("H^3(ball)  =", omega(3)*1.0, " (expect 4pi/3 = Lebesgue volume)")
print("=> radius convention with omega_s gives H^n = L^n.  (diameter convention needs omega_s/2^s.)")
