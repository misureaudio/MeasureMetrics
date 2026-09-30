import sympy as sp
x, y, z, xp, yp, zp = sp.symbols("x y z xp yp zp")
def mul(a, b):
    return (sp.expand(a[0]+b[0]), sp.expand(a[1]+b[1]),
            sp.expand(a[2]+b[2] + sp.Rational(1,2)*(a[0]*b[1] - b[0]*a[1])))
def inv(a): return (-a[0], -a[1], -a[2])
g  = (x, y, z)
h  = (xp, yp, zp)
gh   = mul(g, h)
ghginv = mul(gh, inv(g))
comm = mul(ghginv, inv(h))
print("g*h         =", tuple(gh))
print("g*h*g^-1    =", tuple(ghginv))
print("[g,h]       =", tuple(comm))
print("z-comp [g,h] =", sp.expand(comm[2]))
print("equals 1/2*(x*yp - xp*y)?", sp.simplify(comm[2] - sp.Rational(1,2)*(x*yp - xp*y)) == 0)
print("equals   (x*yp - xp*y) ? ", sp.simplify(comm[2] - (x*yp - xp*y)) == 0)
