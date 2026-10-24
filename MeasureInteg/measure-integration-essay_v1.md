# Measure and Integration: From Riemann to the Present

## A Structured Account for Functional and Numerical Analysts

---

### 0. Scope and Conventions

This essay is an account of integration theory as it developed from the Riemann integral of the 1850s to the measure-theoretic, functional-analytic, and geometric frameworks in use today. It is written for readers working in functional and numerical analysis, linear algebra, and topology, and it is organized not as a chronology but around a structural question: **why does each construction arise, what does it buy, and what does it cost?** The historical arc is the thread; the object of study is the *relationship* between three ways of looking at the same operation — as a limit of sums (the analyst's view), as a positive linear functional (the functional-analyst's view), and as a dual object of an algebra of continuous functions (the topologist's view).

We write a *measure space* as $(X,\mathcal A,\mu)$ with $\mathcal A$ a $\sigma$-algebra, a *signed* measure as a difference of positive measures, and a *vector* measure as a countably additive set function with values in a Banach space. Unless stated otherwise, measures are assumed $\sigma$-finite, and the $L^p$ spaces are taken to consist of *equivalence classes* of functions modulo almost-everywhere (a.e.) equality. Function spaces are over $\mathbb R$ or $\mathbb C$ as is natural. We use standard normalizations, and every non-trivial constant, sign, and theorem hypothesis that we commit to the text is checked against a primary source or re-derived.

Three running threads carry the argument. The first is the **Dirichlet–Volterra–Baire problem**: a sequence of concrete failures of the Riemann integral that force the introduction of a new one. The second is the **Riesz representation theorem** and its descendants, which recast integration as a positive linear functional and thereby show that the measure is *not primitive* — it is *derived* from the integral, or equivalently from the dual of an algebra of continuous functions. The third is the **numerical thread**: quadrature as the approximation of a measure, weak convergence as the convergence that survives discretization, and the empirical measure as the bridge between a discrete sample and a continuum law. We return to each of these at the point where it becomes relevant, and we collect the payoffs in the final sections.

---

## 1. The Riemann integral and its limits

### 1.1 The Riemann integral and Darboux sums

The Riemann integral was introduced by Riemann in his *Habilitationsschrift* *Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe* (written 1853/54, published 1867) and in his subsequent lectures, where the definition appears as the limit of sums of the form

$$
S(P,f)=\sum_{j=1}^{N} f(t_j)\,\Delta x_j,
$$

taken over a partition $P=\{x_0,\dots,x_N\}$ of an interval $[a,b]$ with tags $t_j\in[x_{j-1},x_j]$, as the mesh $\|P\|=\max_j \Delta x_j\to 0$. The function is *Riemann integrable* when this limit exists and is independent of the choice of tags. The equivalent Darboux formulation — comparing the upper and lower sums

$$
U(P,f)=\sum_{j=1}^{N} M_j\,\Delta x_j,\qquad L(P,f)=\sum_{j=1}^{N} m_j\,\Delta x_j,
$$

where $M_j=\sup_{[x_{j-1},x_j]}f$ and $m_j=\inf_{[x_{j-1},x_j]}f$ — makes the integrability criterion transparent: $f$ is Riemann integrable if and only if $\lim_{\|P\|\to 0}\big(U(P,f)-L(P,f)\big)=0$.

Two facts about this definition will matter later. First, the Riemann integral is a *normed* operation on a very small class of functions: it is linear, positive, and bounded (in the sense that $|\int f|\le (b-a)\|f\|_\infty$ for bounded $f$), but its domain is not a vector lattice that is closed under the operations analysts actually perform — pointwise limits, absolute values, and suprema of sequences. Second, and more importantly, the Riemann integral is *sensitive to the values of a function on a set of small but positive length*. It is this sensitivity, and the mismatch between it and the operations of analysis, that forces the break.

### 1.2 Why it fails

The failures are not hypothetical; they are a sequence of named functions and named theorems.

**The Dirichlet function.** Let $f=\mathbf 1_{\mathbb Q\cap[0,1]}$, the indicator of the rationals in $[0,1]$. For any partition, $M_j=1$ and $m_j=0$ on every subinterval (each contains both rationals and irrationals), so $U(P,f)=b-a$ and $L(P,f)=0$ for every $P$. The upper and lower sums never meet, and $f$ is not Riemann integrable. The point is not that $f$ is pathological in some technical sense; it is that the Riemann integral cannot see that $\mathbb Q\cap[0,1]$ is *small* (countable, hence of "measure zero" in the sense that will be made precise below). The Riemann integral has no notion of a set of measure zero, so it cannot ignore the rationals.

**Volterra's function.** Volterra constructed a function $F$ on $[0,1]$ that is differentiable *everywhere*, with a *bounded* derivative $F'$, such that $F'$ is *not* Riemann integrable. The mechanism is a "fat" Cantor set $C$ of positive measure: $F$ is built as a uniform limit of smooth "bump" functions supported in the complementary intervals of $C$, so that $F$ is Lipschitz (hence continuous, and Riemann integrable) while $F'$ is continuous off $C$ and discontinuous precisely on $C$. Since the set of discontinuities of $F'$ is $C$, a set of positive measure, Lebesgue's criterion (a bounded function is Riemann integrable if and only if it is continuous a.e.) shows that $F'$ is not Riemann integrable. This is a sharper failure than Dirichlet's: here the integrand is a perfectly respectable derivative, the function it comes from is Riemann integrable, and yet the Riemann integral of the derivative fails to exist. The fundamental theorem of calculus, in its Riemann form, breaks: $F$ is differentiable everywhere with bounded derivative, but $\int_a^b F'\,dx$ (Riemann) is not defined, so the identity $F(b)-F(a)=\int_a^b F'$ cannot hold. The Riemann integral is not closed under the operation (differentiation) that is supposed to be its inverse.

**The Baire category obstruction.** A theorem of Baire (a consequence of the fact that the pointwise limit of a sequence of continuous functions is a *Baire class one* function, and that the set of discontinuities of a Baire class one function is a *meagre* $G_\delta$) shows that the pointwise limit of a sequence of continuous (hence Riemann-integrable) functions need not be Riemann integrable. Concretely, let $C\subseteq[0,1]$ be a *fat* Cantor set (a closed, nowhere dense set of positive Lebesgue measure); then $\mathbf 1_C$ is a pointwise limit of continuous functions (its set of discontinuities is $C$, a meagre $G_\delta$), but $\mathbf 1_C$ is not Riemann integrable (its set of discontinuities $C$ has positive measure, so Lebesgue's criterion fails). So the class of Riemann-integrable functions is *not closed under pointwise limits* — it is not a *sequential* space in the sense that matters for analysis. Any integral that is to support a convergence theorem (a "limit interchange" of $\lim$ and $\int$) must have a domain that *is* closed under the relevant mode of convergence.

**The Fourier problem.** The study of Fourier series (the problem that motivated much of this development, from Dirichlet and Riemann onward) requires integrating functions that are discontinuous, or even unbounded, and passing to limits of partial sums. The Riemann integral is too rigid for this: the partial sums of a Fourier series are continuous, their pointwise limit may be a discontinuous $L^1$ function, and one needs an integral that (i) contains all the partial sums, (ii) contains their limits, and (iii) admits the passage to the limit under the integral sign. The Riemann integral fails on (ii) and (iii) simultaneously.

### 1.3 What the failure tells us

The common thread is this: the Riemann integral is a *pointwise* operation. It integrates by sampling the function at (or near) every point, and it is therefore unable to ignore a set of points that is "small" in the right sense but non-empty. The failures above are all failures of *invariance under a.e. modification*: the Riemann integral of a function depends on its values on sets of arbitrarily small (but positive) length, whereas the operations of analysis (pointwise limits, differentiation, the passage to a limit in a PDE) are *a.e. operations* — they do not care about the values of a function on a set of measure zero.

The resolution, and the source of the new integral, is to make explicit the notion of *measure zero* that the Riemann integral implicitly requires but never states. Once a set function $\mu$ (a *measure*) is placed on the space, defining $\mu(E)=0$ for the "small" sets, the integral can be built on the class of $\mu$-measurable functions, and it will then be *insensitive* to a.e. modification: two functions that differ only on a set of measure zero have the same integral. This is the essential new feature of the Lebesgue integral, and it is the feature that makes the convergence theorems — and hence the analysis — work.

The rest of the essay is the account of how the measure is constructed (§2), how the integral is built on it and shown to be a positive linear functional (§3), how the resulting function spaces are Banach spaces with a rich duality structure (§4), how the measure interacts with the topology of the underlying space (§5), how the integral is extended to vector-valued functions (§6), and how all of this is used in the numerical and modern settings (§7–8).

---

## 2. The measure-theoretic turn (1890s–1910s)

### 2.1 Lebesgue's construction: outer measure and the Carathéodory criterion

Lebesgue's construction, set out in his 1902 thesis *Intégrale, Longueur, Aire* (and applied to Fourier series in his 1903 paper in the *Annales scientifiques de l'École Normale supérieure*), proceeds in two stages.

**Stage one: the outer measure.** One defines, for every subset $E\subseteq\mathbb R$ (no measurability assumed), the *outer measure*

$$
m^*(E)=\inf\left\{\sum_{k=1}^{\infty} |I_k|:\ E\subseteq\bigcup_{k=1}^{\infty} I_k,\ I_k\ \text{open intervals}\right\},
$$

the infimum of the total lengths of countable open covers of $E$. The outer measure is monotone and *countably subadditive* ($m^*(\bigcup_k E_k)\le\sum_k m^*(E_k)$), but it is not, in general, countably *additive*: for arbitrary disjoint $E,F$ one only has $m^*(E\cup F)\le m^*(E)+m^*(F)$, with strict inequality possible. The outer measure is defined on *all* subsets, which is what makes it a useful starting point — one has not yet had to decide which sets are measurable.

**Stage two: the Carathéodory criterion.** A subset $E\subseteq\mathbb R$ is declared *measurable* (Lebesgue measurable) if it *splits* every set $S\subseteq\mathbb R$ additively:

$$
m^*(S)=m^*(S\cap E)+m^*(S\setminus E)\qquad\text{for every }S\subseteq\mathbb R.
$$

This is the **Carathéodory criterion** (Carathéodory, 1918–1927), and it is the single most important technical idea of the construction, for two reasons. First, it is *self-referential in the right way*: it defines measurability in terms of the outer measure alone, without any appeal to topology (open sets, $F_\sigma$ sets, etc.), which is what makes it *generalizable* to arbitrary measure spaces (it is, in fact, often taken as the *definition* of measurability for an abstract outer measure). Second, the family of sets satisfying it is a $\sigma$-algebra, and the restriction of $m^*$ to this $\sigma$-algebra is a countably additive measure. The proof of the $\sigma$-algebra property is a short but delicate bookkeeping argument: the splitting property is preserved under complements and countable disjoint unions, and the countable additivity of the restricted measure follows from subadditivity plus the splitting property applied to a countable union.

The Lebesgue $\sigma$-algebra $\mathcal L$ is thus the $\sigma$-algebra of Carathéodory-measurable sets, and $\lambda=m^*\big|_{\mathcal L}$ is the Lebesgue measure. It is a *complete* measure: every subset of a null set is measurable (with measure zero). This completeness is not an accident; it is a direct consequence of the splitting criterion, and it is the property that makes the Lebesgue integral insensitive to a.e. modification, as noted in §1.3.

### 2.2 Borel and Lebesgue $\sigma$-algebras; completeness; the null ideal

There are two $\sigma$-algebras in play, and it is important to keep them distinct. The **Borel $\sigma$-algebra** $\mathcal B(\mathbb R)$ is the $\sigma$-algebra *generated by the open sets* (equivalently, by the closed sets, by the compact sets, by the open intervals). It is the smallest $\sigma$-algebra that makes every continuous function measurable. The **Lebesgue $\sigma$-algebra** $\mathcal L$ is the $\sigma$-algebra of Carathéodory-measurable sets. The relationship is:

$$
\mathcal B(\mathbb R)\ \subseteq\ \mathcal L,
$$

and the inclusion is *strict*: there are sets that are Lebesgue measurable but not Borel measurable. Every Borel set is Lebesgue measurable, but $\mathcal L$ is the *completion* of $\mathcal B(\mathbb R)$ with respect to $\lambda$ — that is, $\mathcal L$ is the smallest $\sigma$-algebra containing $\mathcal B(\mathbb R)$ and all subsets of $\lambda$-null Borel sets. Concretely, every Lebesgue-measurable set $E$ can be written $E=B\triangle N$ with $B\in\mathcal B(\mathbb R)$ and $N\subseteq Z$ for some Borel null set $Z$ (so $N$ is "Borel up to a null set"). The two $\sigma$-algebras agree on all sets that are "topologically nice," and they differ only on the null sets.

The **null ideal** $\mathcal N=\{E\in\mathcal L:\lambda(E)=0\}$ is the collection of null sets. It is an *ideal* in the lattice of measurable sets: it is closed under subsets and finite (indeed countable) unions. The null ideal is the object that encodes "what the integral does not see," and the entire theory of the Lebesgue integral is built on the quotient of the measurable sets by this ideal. When one says that two functions are equal "almost everywhere," one means that they are equal outside a member of $\mathcal N$; and when one quotients a function space by a.e. equality, one is quotienting by the null ideal. This is the sense in which the *measure* (via its null ideal) *shapes* the structure of the function spaces built on it — a theme that returns in §4 (the $L^p$ spaces are, strictly, *pseudo*-normed before the quotient) and in §3 (the Daniell construction, where the null ideal is *derived* from the integral rather than given).

### 2.3 The Lebesgue integral: simple functions, MCT, DCT, Fatou

The Lebesgue integral is defined by *approximation from below* by simple functions. A *simple function* is a finite linear combination of indicator functions of measurable sets, $s=\sum_{k=1}^{K} a_k\,\mathbf 1_{E_k}$ with the $E_k$ disjoint and measurable, and its integral is defined algebraically:

$$
\int s\,d\lambda=\sum_{k=1}^{K} a_k\,\lambda(E_k).
$$

For a *non-negative* measurable function $f$, one defines

$$
\int f\,d\lambda=\sup\left\{\int s\,d\lambda:\ s\le f,\ s\ \text{simple}\right\},
$$

the supremum over all simple functions dominated by $f$. For a general (signed or complex) measurable $f$, one writes $f=f^+-f^-$ (or $f=\mathrm{Re}\,f+i\,\mathrm{Im}\,f$) and defines the integral when at least one of the pieces is finite, setting $\int f=\int f^+-\int f^-$. A measurable function is *integrable* (in $L^1$) when $\int|f|\,d\lambda<\infty$.

The power of this definition is not in the definition itself but in the three convergence theorems that it supports and that the Riemann integral does not:

> **Theorem (Monotone Convergence, MCT).** If $0\le f_1\le f_2\le\cdots$ are measurable and $f_n\to f$ pointwise, then $\int f_n\,d\lambda\to\int f\,d\lambda$ (with the value $+\infty$ allowed).

> **Theorem (Fatou's Lemma).** If $f_n\ge 0$ are measurable, then
> $$\int\liminf_{n\to\infty} f_n\,d\lambda\ \le\ \liminf_{n\to\infty}\int f_n\,d\lambda.$$

> **Theorem (Dominated Convergence, DCT).** If $f_n\to f$ pointwise a.e. and there exists $g\in L^1$ with $|f_n|\le g$ for all $n$, then $f\in L^1$ and $\int f_n\,d\lambda\to\int f\,d\lambda$.

The MCT is the engine: it justifies interchanging a limit and an integral for *monotone* sequences, and it is the proof of the countable additivity of the integral. Fatou's lemma is the MCT applied to the liminf, and it is the workhorse for lower bounds. The DCT is the *two-sided* version: it allows the interchange for *arbitrary* (not monotone) sequences, provided a single integrable function dominates the whole sequence. The DCT is the theorem that makes the Fourier, PDE, and probability arguments go through, because it is the theorem that lets one pass to a limit under the integral sign without a monotonicity hypothesis.

The contrast with the Riemann integral is sharp. The Riemann integral supports *no* general dominated convergence theorem: there are sequences of Riemann-integrable functions that converge a.e. to a Riemann-integrable function but for which the integrals do not converge to the integral of the limit (the standard example is $f_n=n\,\mathbf 1_{[0,1/n]}$, which converges a.e. to $0$ while $\int_0^1 f_n=1$ for every $n$). The Lebesgue DCT is the precise statement of the *invariance under a.e. modification* that §1.3 identified as the missing feature.

### 2.4 Riemann versus Lebesgue

The following table summarizes the contrast. The first three rows are about the *domain*; the last two, about the *convergence*.

| Property | Riemann integral | Lebesgue integral |
|---|---|---|
| Domain | bounded functions continuous a.e. (Riemann criterion) | all $\lambda$-measurable functions (with $\int|f|<\infty$ for $L^1$) |
| Invariance under a.e. modification | no (depends on values on null sets) | yes (the null ideal is quotiented out) |
| Closed under pointwise limits | no (Baire class one obstruction) | yes (measurable functions are closed under pointwise limits) |
| Monotone convergence | no | yes (MCT) |
| Dominated convergence | no | yes (DCT) |
| Relation | the Riemann integral of a *bounded, a.e.-continuous* $f$ equals the Lebesgue integral of $f$ | extends the Riemann integral; agrees with it on the Riemann-integrable functions |

The last row is the compatibility statement: the Lebesgue integral *extends* the Riemann integral. Every Riemann-integrable function is Lebesgue-integrable, and the two integrals agree. The Lebesgue integral is thus a *strict extension* that adds exactly the functions the Riemann integral could not handle, without changing the value on the old domain. This is what makes the transition "safe": nothing that worked before stops working; one simply gains new functions and new convergence theorems.

### 2.5 The Vitali set: what measurability costs

The construction above defines a measure on a $\sigma$-algebra, but it does not by itself show that there are sets *outside* the $\sigma$-algebra — sets that are not measurable. That this is not a vacuous concern is the content of the **Vitali theorem** (Vitali, 1905): there exist subsets of $\mathbb R$ that are not Lebesgue measurable.

The construction uses the equivalence relation $x\sim y\iff x-y\in\mathbb Q$ on $\mathbb R$, whose equivalence classes are the cosets $x+\mathbb Q$ of the additive subgroup $\mathbb Q$. The quotient $\mathbb R/\mathbb Q$ has the cardinality of the continuum, and the cosets partition $\mathbb R$ into pairwise disjoint dense sets. By the *axiom of choice*, one may select one representative from each coset; the set $V$ of selected representatives (intersected with $[0,1]$) is a **Vitali set**. If $V$ were measurable, then the countably many translates $V+q$ ($q\in\mathbb Q\cap[-1,1]$) would be measurable, pairwise disjoint, and would satisfy

$$
[0,1]\ \subseteq\ \bigcup_{q\in\mathbb Q\cap[-1,1]}(V+q)\ \subseteq\ [-1,2],
$$

so by countable additivity and translation invariance, $1\le\sum_q \lambda(V+q)=\sum_q\lambda(V)\le 3$, which is impossible (the sum of countably many copies of a fixed number is either $0$ or $+\infty$). Hence $V$ is not measurable.

Two points are worth making. First, the axiom of choice is *essential*: Solovay (1970) showed that, *assuming the existence of an inaccessible cardinal*, the statement "every subset of $\mathbb R$ is Lebesgue measurable" is consistent with **ZF** (Zermelo–Fraenkel set theory *without* the axiom of choice); Shelah (1984) proved that this inaccessible-cardinal hypothesis is *necessary* — ZF alone cannot establish that all sets of reals are Lebesgue measurable. The non-measurable sets are thus a genuine consequence of choice, not of the measure-theoretic axioms alone. Second, the Vitali set is not a *topologically* wild set in any constructive sense: it has no Borel description and does not have the *Baire property*; its only pathology is its failure to be measurable. This is the sense in which measurability is a *strictly finer* structure than topology: the Borel $\sigma$-algebra (generated by the topology) is a *proper* sub-$\sigma$-algebra of the power set, and the Lebesgue $\sigma$-algebra (its completion) is still a *proper* sub-$\sigma$-algebra of the power set. There are sets that no amount of topological structure can make measurable.

The Vitali set is the seed of the **Banach–Tarski paradox** (§5.4), which is the same non-measurability phenomenon expressed in the language of group actions: the failure of the measure to extend to a translation-invariant measure on *all* subsets is what makes the paradox possible.

---

## 3. Integration as a positive linear functional: the functional-analytic viewpoint

### 3.1 The Daniell–Stone construction

The measure-theoretic construction of §2 starts from a *set function* (the measure) and builds the integral. There is a second, logically independent construction that starts from the *integral* (as a positive linear functional on a small class of functions) and builds the measure. This is the **Daniell integral** (Daniell, 1918), completed and generalized by Stone (1931), and it is the construction that makes the functional-analytic content of integration explicit.

The setup is as follows. Let $\mathcal L$ be a *vector lattice* of real-valued functions on a set $X$ (a vector space closed under the lattice operations $f\vee g=\max(f,g)$ and $f\wedge g=\min(f,g)$, and containing the constant functions). Let $\Lambda:\mathcal L\to\mathbb R$ be a *positive linear functional* (linear, and $\Lambda(f)\ge 0$ whenever $f\ge 0$). One then defines, for an arbitrary function $f:X\to\mathbb R$, the *upper integral*

$$
\overline{\Lambda}(f)=\inf\{\Lambda(g):g\in\mathcal L,\ g\ge f\},
$$

the infimum of the values of $\Lambda$ on the lattice functions that dominate $f$. A function $f$ is called *$\Lambda$-integrable* if its upper and lower integrals (the latter defined dually via $-\overline{\Lambda}(-f)$) coincide and are finite, in which case the common value is $\Lambda(f)$, the *Daniell integral* of $f$. The class of $\Lambda$-integrable functions is a vector lattice that *extends* the original $\mathcal L$, and $\Lambda$ extends to it as a positive linear functional.

The key theorem is the **Daniell–Stone theorem**:

> **Theorem (Daniell–Stone).** Let $\Lambda$ be a positive linear functional on a vector lattice $\mathcal L$ of bounded functions on $X$ satisfying a mild continuity condition (the Daniell convergence condition: if $f_n\downarrow 0$ in $\mathcal L$ then $\Lambda(f_n)\to 0$). Then there exists a *unique* measure $\mu$ on a $\sigma$-algebra $\mathcal A\subseteq 2^X$ such that $\Lambda(f)=\int f\,d\mu$ for all $f\in\mathcal L$, and the $\Lambda$-integrable functions are precisely the $\mu$-measurable functions for which the integral exists.

The content of the theorem is that the measure $\mu$ is *not an input* — it is *derived* from the functional $\Lambda$. The measure is *recovered* from the integral by the formula $\mu(E)=\Lambda(\mathbf 1_E)$ (for the sets $E$ that turn out to be measurable), and the $\sigma$-algebra is the collection of sets for which this formula is countably additive. This is the precise sense in which **the integral is the primitive object and the measure is its shadow**: given a "reasonable" positive linear functional on a lattice of functions, there is a unique measure that represents it, and the integral with respect to that measure is the extension of the functional.

The standard example is the one that recovers the Lebesgue integral: take $\mathcal L=C([0,1])$ (or the piecewise-continuous functions) and $\Lambda(f)=\int_0^1 f\,dx$ (the Riemann integral, a positive linear functional). The Daniell–Stone theorem then produces the Lebesgue measure and the Lebesgue integral as the unique extension. The Riemann integral, viewed as a positive linear functional on $C([0,1])$, is the *seed* from which the entire Lebesgue theory grows.

### 3.2 Why this matters: the linear-algebraic content

The Daniell–Stone theorem is the statement that integration is, at its core, a *linear* operation. The measure is a *byproduct* of the linearity and positivity of the integral. This is the "linear-algebraic" viewpoint, and it is the viewpoint that connects integration to the rest of functional analysis.

The analogy with linear algebra is precise. In finite dimensions, a *positive linear functional* on a vector lattice of functions (or, equivalently, a *state* on a commutative $C^*$-algebra) is determined by its values on the *idempotents* (the characteristic functions of the "points"), and the measure is the collection of those values. The *Jordan decomposition* of a signed functional (writing it as the difference of two positive functionals) is the noncommutative analogue of writing a signed measure as $\mu^+-\mu^-$, and the *spectral decomposition* (the representation of a positive functional in terms of a measure) is the analogue of the spectral theorem for self-adjoint operators. The Daniell–Stone theorem is, in this light, the *commutative* spectral theorem: a positive linear functional on a commutative algebra of functions is represented by a unique measure.

This is not merely an analogy; it is the precise statement of the **Riesz representation theorem** and its descendants, which we now state.

### 3.3 The Riesz representation theorem and Riesz–Markov–Kakutani

The **Riesz representation theorem** (Riesz, 1909) is the first and simplest of the representation results. In Riesz's *original* 1909 form, the functional is represented as a **Riemann–Stieltjes integral** $\int_0^1 f\,d\alpha$ with respect to a function $\alpha$ of *bounded variation*; the equivalent *measure-theoretic* form — representation by a finite regular Borel measure, via the standard correspondence between functions of bounded variation and finite signed Borel measures on $[0,1]$ — is the modern restatement, which we state here:

> **Theorem (Riesz, 1909).** Let $\varphi$ be a continuous linear functional on $C([0,1])$ (with the sup norm). Then there exists a *unique* regular Borel measure $\mu$ on $[0,1]$ such that
> $$\varphi(f)=\int_{[0,1]} f\,d\mu\qquad\text{for all }f\in C([0,1]),$$
> and $\|\varphi\|=\mu([0,1])$ (for $\varphi\ge 0$).

The content: the *dual* of $C([0,1])$ is *isometrically isomorphic* to the space of regular Borel measures on $[0,1]$. A continuous linear functional on the algebra of continuous functions is *exactly* integration against a measure. The measure is *recovered* from the functional by $\mu(E)$ (for Borel $E$) via a regularity argument, and the isometry $\|\varphi\|=\|\mu\|$ (the total variation) is the precise form of the correspondence.

The **Riesz–Markov–Kakutani theorem** (Riesz 1909, Markov 1938, Kakutani 1941) is the general form, valid for *locally compact Hausdorff* spaces:

> **Theorem (Riesz–Markov–Kakutani).** Let $X$ be a *locally compact Hausdorff* space and $C_0(X)$ the Banach space of continuous functions vanishing at infinity (with the sup norm). Then, over the *real* scalar field, the dual $C_0(X;\mathbb R)^*$ is isometrically isomorphic to the space $\mathcal M(X)$ of finite *signed* Radon measures on $X$ (finite, regular Borel measures that are inner regular on open sets and outer regular on Borel sets), via the map $\mu\mapsto\varphi_\mu$ where $\varphi_\mu(f)=\int_X f\,d\mu$; over the *complex* scalar field, $C_0(X;\mathbb C)^*$ is isometrically isomorphic to the space of finite *complex* Radon measures on $X$.

The standing hypothesis is *local compactness and Hausdorffness*; it is essential and is not automatically satisfied. The theorem applies to all locally compact metric spaces and to manifolds (which are locally compact Hausdorff), but *not* to every Polish space: $\ell^2$ is Polish but *not* locally compact, and the theorem does not apply to $C_0(\ell^2)$ in this form. This is the kind of standing-hypothesis error that is easy to make and that an expert reader will catch; we state it explicitly here.

The Riesz–Markov–Kakutani theorem is the *topological* form of the Riesz representation theorem, and it is the theorem that connects integration to the *duality* of function algebras. It says: the measure is the *dual object* of the algebra of continuous functions. Given the algebra $C_0(X)$ (the "functions"), the measure is *recovered* as the continuous linear functionals on it. This is the sense in which the *topology* (via the continuous functions it determines) and the *measure* are *dual* to each other, and it is the theorem that makes the topologist's and the functional-analyst's viewpoints coincide.

The Riesz–Markov–Kakutani theorem is also the starting point of *Gelfand duality* in the theory of commutative $C^*$-algebras: a commutative $C^*$-algebra $A$ is (isometrically isomorphic to) $C_0(X)$ for a unique locally compact Hausdorff space $X$ (its *spectrum* or *Gelfand space*), and the dual of $A$ is the space of measures on $X$. Integration is thus the *dual* of the algebra of continuous functions, and the measure is the *state space* of the algebra. This is the unifying statement of the functional-analytic and topological viewpoints, and it is the theorem that the rest of the essay returns to.

### 3.4 The decomposition theorems: Jordan, Hahn, Radon–Nikodym

The "linear algebra" of measures has three fundamental decomposition theorems, each of which has a direct analogue in the theory of linear functionals and operators. We state them with their exact hypotheses.

> **Theorem (Jordan decomposition).** Every finite signed measure $\mu$ on a measurable space $(X,\mathcal A)$ can be written *uniquely* as $\mu=\mu^+-\mu^-$, where $\mu^+$ and $\mu^-$ are finite *positive* measures that are *mutually singular* ($\mu^+\perp\mu^-$, meaning there is a measurable set $E$ with $\mu^+(X\setminus E)=0$ and $\mu^-(E)=0$). The *total variation* is $|\mu|=\mu^++\mu^-$, and $\|\mu\|=|\mu|(X)$.

> **Theorem (Hahn decomposition).** For a finite signed measure $\mu$ on $(X,\mathcal A)$, there exists a measurable set $P\subseteq X$ (a *positive set*) such that $\mu(E)\ge 0$ for every measurable $E\subseteq P$ and $\mu(E)\le 0$ for every measurable $E\subseteq X\setminus P$. The pair $(P,X\setminus P)$ is unique up to a null set, and $P$ is a *support* for $\mu^+$ while $X\setminus P$ is a *support* for $\mu^-$.

> **Theorem (Radon–Nikodym).** Let $\mu$ and $\nu$ be $\sigma$-finite measures on $(X,\mathcal A)$ with $\nu$ $\sigma$-finite. Then $\mu\ll\nu$ ($\mu$ is *absolutely continuous* with respect to $\nu$, meaning $\nu(E)=0\implies\mu(E)=0$) if and only if there exists a unique (a.e.) measurable function $f=\frac{d\mu}{d\nu}\ge 0$ (the *Radon–Nikodym derivative*) such that
> $$\mu(E)=\int_E f\,d\nu\qquad\text{for every }E\in\mathcal A.$$

The Jordan decomposition is the measure-theoretic analogue of writing a (not necessarily positive) operator as the difference of two positive operators, or a real number as the difference of its positive and negative parts. The Hahn decomposition is the *set-theoretic* content of the Jordan decomposition: it identifies the *positive* and *negative* *regions* of the measure, and it is the measure-theoretic analogue of the *spectral* decomposition of a self-adjoint operator into its positive and negative spectral parts (the positive and negative sets $P$ and $X\setminus P$ play the role of the positive and negative spectral subspaces). The Radon–Nikodym theorem is the *differentiation* theorem: it says that an absolutely continuous measure is the *integral* of a density (the derivative) with respect to the reference measure, and it is the measure-theoretic analogue of the fundamental theorem of calculus (the measure $\mu$ is the "primitive" of the density $f=d\mu/d\nu$ with respect to $\nu$).

The **Lebesgue decomposition theorem** combines the Radon–Nikodym and the singular cases: for $\sigma$-finite $\mu,\nu$, there exist *unique* measures $\mu_{\mathrm{ac}}$ and $\mu_{\mathrm{s}}$ such that $\mu=\mu_{\mathrm{ac}}+\mu_{\mathrm{s}}$, $\mu_{\mathrm{ac}}\ll\nu$, and $\mu_{\mathrm{s}}\perp\nu$. This is the *complete* decomposition: every measure is the sum of its absolutely continuous part (the part that "has a density") and its singular part (the part that is concentrated on a set of $\nu$-measure zero). It is the measure-theoretic analogue of the decomposition of a vector into its component along a subspace and its component orthogonal to it, and it is the theorem that underlies the *decomposition of a general functional* into its "regular" (absolutely continuous) and "singular" parts.

These three theorems (Jordan, Hahn, Radon–Nikodym, plus the Lebesgue decomposition) are the "linear algebra" of measure theory, and they are the theorems that make the functional-analytic and linear-algebraic viewpoints of integration *computable*. They are the theorems that allow one to pass from a (signed, vector-valued) measure to its positive parts, to its density, and to its singular part, and they are the theorems that the $L^p$ duality of §4 is built on.

---

## 4. The $L^p$ spaces: the Banach-space structure

### 4.1 Construction: the quotient by a.e. equality, Minkowski, Riesz–Fischer

The $L^p$ spaces are the natural function spaces for the Lebesgue integral. For $1\le p<\infty$, $L^p(X,\mathcal A,\mu)$ is the space of *equivalence classes* $[f]$ of measurable functions $f$ for which $\|f\|_p=\left(\int|f|^p\,d\mu\right)^{1/p}<\infty$, where $f\sim g$ if $f=g$ a.e. (i.e., $f-g$ is in the null ideal). For $p=\infty$, $L^\infty$ is the space of equivalence classes of essentially bounded measurable functions, with $\|f\|_\infty=\operatorname{ess\,sup}|f|$.

The *a.e. quotient* is essential and is the point at which the null ideal of §2.2 enters the functional analysis. Before the quotient, the "norm" $\|\cdot\|_p$ is only a *semi-norm*: $\|f\|_p=0$ does not imply $f=0$, only $f=0$ a.e. The quotient by the null ideal is what turns the semi-norm into a genuine norm, and it is what makes $L^p$ a *normed space* rather than a *pseudo-normed* space. This is the concrete, verifiable instance of the *measure shaping the metric structure* noted in the companion essay on measure and metrics: the null ideal (a measure-theoretic object) determines the quotient (a metric/functional-analytic object).

The fundamental inequality is **Minkowski's inequality**:

> **Theorem (Minkowski).** For $1\le p\le\infty$ and $f,g\in L^p$,
> $$\|f+g\|_p\ \le\ \|f\|_p+\|g\|_p.$$

This is the *triangle inequality* for the $L^p$ "norm," and its proof (for $1\le p<\infty$) is a delicate application of Hölder's inequality (below) and is one of the technical highlights of the theory. Minkowski's inequality is the statement that $L^p$ is a *normed* space, and it is the inequality that makes the $L^p$ spaces *metric* spaces (with the metric $d(f,g)=\|f-g\|_p$).

The completeness of the $L^p$ spaces is the **Riesz–Fischer theorem**:

> **Theorem (Riesz–Fischer).** For $1\le p\le\infty$, the space $L^p(X,\mathcal A,\mu)$ is *complete* with respect to $\|\cdot\|_p$; that is, $L^p$ is a *Banach space*.

The Riesz–Fischer theorem is the statement that the $L^p$ spaces are *Banach* spaces, and it is the theorem that makes them the natural setting for the functional analysis that follows. Its proof (for $1\le p<\infty$) proceeds by showing that every Cauchy sequence in $L^p$ has a subsequence that converges a.e. to a measurable function $f$, and then using Fatou's lemma (or the MCT) to show that $f\in L^p$ and that the whole sequence converges to $f$ in $L^p$. The a.e. convergence of the subsequence is where the *measure* (the null ideal, the a.e. quotient) is essential: it is what allows one to pass from $L^p$-convergence (a statement about norms) to a.e. convergence (a statement about pointwise values), and it is the feature that distinguishes the Lebesgue $L^p$ spaces from the Riemann-integral analogues.

### 4.2 Hölder's inequality, duality, and the endpoint pathology

The central inequality of the $L^p$ theory is **Hölder's inequality**:

> **Theorem (Hölder).** Let $1\le p,q\le\infty$ with $\frac1p+\frac1q=1$ (the *conjugate exponents*). For $f\in L^p$ and $g\in L^q$,
> $$\int|fg|\,d\mu\ \le\ \|f\|_p\,\|g\|_q,$$
> with equality if and only if $|f|^p$ and $|g|^q$ are linearly dependent (a.e.).

Hölder's inequality is the *duality* inequality: it says that the $L^q$ norm of $g$ is the *operator norm* of the linear functional $f\mapsto\int fg\,d\mu$ on $L^p$. This is the statement that leads to the *duality theorem*:

> **Theorem ($L^p$ duality).** Let $1\le p<\infty$ and $q$ its conjugate exponent. Then the dual space $L^p(X,\mathcal A,\mu)^*$ is isometrically isomorphic to $L^q(X,\mathcal A,\mu)$, via the map $g\mapsto\varphi_g$ where $\varphi_g(f)=\int fg\,d\mu$.

The isometry is $\|\varphi_g\|=\|g\|_q$, and it is a direct consequence of Hölder's inequality (for $\|\varphi_g\|\le\|g\|_q$) and a construction of a "worst-case" $f\in L^p$ (for $\|\varphi_g\|\ge\|g\|_q$), typically $f=|g|^{q-1}\overline{g}$ (normalized). The duality theorem is the *precise* statement of the Hölder pairing, and it is the theorem that makes the $L^p$ spaces *dual* to each other: $L^p$ and $L^q$ are dual Banach spaces, and the pairing is the $L^1$ integral.

The *endpoint* $p=\infty$ is where the duality *fails*, and the failure is instructive. The dual of $L^\infty$ is *not* $L^1$:

> **Theorem (the $L^\infty$ endpoint).** The dual $(L^\infty(X,\mathcal A,\mu))^*$ is *strictly larger* than $L^1(X,\mathcal A,\mu)$. Every $g\in L^1$ defines a functional $\varphi_g\in (L^\infty)^*$ via $\varphi_g(f)=\int fg\,d\mu$ (with $\|\varphi_g\|=\|g\|_1$), but there are functionals in $(L^\infty)^*$ that are *not* of this form. The space $(L^\infty)^*$ is isometrically isomorphic to the space $ba(X,\mathcal A,\mu)$ of *bounded finitely additive* measures (the *ba* space), which is the *bidual* of $L^1$ and is generally much larger than $L^1$.

The content of the endpoint pathology is that the *Hahn–Banach theorem* produces, in $(L^\infty)^*$, functionals that are represented by *finitely additive* (not countably additive) measures — the *Banach limits*, the *ultralimit* functionals, and the like. These are the "non-measurable measures" that the countably additive theory cannot see, and they are the functionals that arise from the *axiom of choice* (they are constructed using non-principal ultrafilters, which require choice). The endpoint $p=\infty$ is thus the point where the *measure-theoretic* (countably additive) and the *functional-analytic* (Hahn–Banach) viewpoints *diverge*: the functional-analytic dual is larger than the measure-theoretic one, and the difference is precisely the finitely additive measures. This is the $L^p$-theoretic shadow of the Vitali set and the Banach–Tarski paradox: the failure of the measure to extend to all subsets is what produces the extra functionals in $(L^\infty)^*$.

### 4.3 Reflexivity and the geometry of $L^p$

A Banach space $X$ is *reflexive* if the canonical embedding $X\to X^{**}$ is surjective (i.e., $X$ is isometrically isomorphic to its bidual). The $L^p$ spaces have a clean reflexivity characterization:

> **Theorem (reflexivity of $L^p$).** $L^p(X,\mathcal A,\mu)$ is reflexive if and only if $1<p<\infty$.

The failure at the endpoints is the same pathology as in §4.2: $L^1$ is not reflexive (its dual is $L^\infty$, and its bidual is $(L^\infty)^*\supsetneq L^1$), and $L^\infty$ is not reflexive (its dual is $ba$, and its bidual is even larger). The reflexivity of $L^p$ for $1<p<\infty$ is the theorem that makes the *weak compactness* arguments go through: in a reflexive space, every bounded sequence has a *weakly convergent* subsequence (the *Eberlein–Šmulian theorem*), and this is the compactness that underlies the existence of minimizers and the convergence of Galerkin approximations (§7.4).

The *geometry* of the $L^p$ spaces (their *type* and *cotype*, in the language of the geometry of Banach spaces) is the feature that governs the *random* and *probabilistic* behavior of the spaces, and it is the feature that enters the analysis of Monte Carlo methods and the noncommutative setting (§8.5). The $L^p$ spaces for $1<p<\infty$ have *type* $\min(p,2)$ and *cotype* $\max(p,2)$, and these exponents control the rates of convergence of random series and the behavior of the spaces under *tensor* products. We do not develop the type/cotype theory here, but we note that it is the $L^p$-theoretic content that distinguishes the "Hilbertian" case $p=2$ (type = cotype = 2, the best possible) from the "non-Hilbertian" cases $p\ne 2$, and it is the content that enters the *noncommutative* $L^p$ theory of §8.5 (where the type/cotype of the noncommutative $L^p$ spaces is a genuine and non-trivial object).

### 4.4 The role of $L^p$ in numerical analysis

The $L^p$ spaces are not merely the natural setting for the Lebesgue integral; they are the natural setting for *numerical* analysis, and the choice of $p$ is a *numerical* choice with concrete consequences.

The **$L^2$ case** is the *Hilbertian* case, and it is the case that underlies the *Galerkin* and *finite-element* methods. The $L^2$ inner product $\langle f,g\rangle=\int fg\,d\mu$ makes $L^2$ a *Hilbert space*, and the *Riesz representation theorem for Hilbert spaces* (every continuous linear functional is represented by an inner product with a fixed element) is the theorem that makes the *variational* formulation of PDEs work: a weak solution $u\in L^2$ (or in a Sobolev space $H^1$) is characterized by the *variational equation* $\langle \nabla u,\nabla v\rangle=\langle f,v\rangle$ for all test functions $v$, and the *Galerkin* approximation is the projection of $u$ onto a finite-dimensional subspace (with respect to the $L^2$ inner product). The $L^2$ structure is what makes the *orthogonality* and *projection* arguments of the finite-element method possible, and it is the reason that the $L^2$ norm is the natural *error* norm for the Galerkin method.

The **$L^\infty$ case** is the *stability* case, and it is the case that underlies the *maximum principle* and the *discrete maximum principle*. The $L^\infty$ norm is the *supremum* norm, and it is the norm that controls the *pointwise* behavior of a solution. The *maximum principle* for elliptic PDEs states that the $L^\infty$ norm of the solution is bounded by the $L^\infty$ norm of the data, and the *discrete maximum principle* is the finite-element analogue (the $L^\infty$ stability of the discrete solution). The $L^\infty$ norm is thus the natural norm for *stability* and *pointwise* error estimates, and it is the norm that the *maximum principle* controls.

The choice between $L^2$ (for *variational* and *projection* arguments) and $L^\infty$ (for *stability* and *pointwise* arguments) is a *numerical* choice, and it is the choice that determines the *form* of the error estimate. The $L^2$ error estimate is a *quadratic* (energy) estimate, and the $L^\infty$ error estimate is a *pointwise* (supremum) estimate; the two are related by the *Sobolev embedding* theorems (which are, in turn, consequences of the $L^p$ theory and the *Hardy–Littlewood–Sobolev* inequality). The $L^p$ spaces are thus the *common language* in which the *variational*, *stability*, and *embedding* arguments of numerical analysis are expressed, and the choice of $p$ is the choice of *which* of these arguments one is making.

---

## 5. Measures on topological spaces: Radon measures, Haar measure, and the Riesz–Markov duality

### 5.1 Borel measures and regularity

When the underlying space $X$ carries a topology, the natural $\sigma$-algebra on which to place a measure is the *Borel $\sigma$-algebra* $\mathcal B(X)$ (generated by the open sets), and a measure on $\mathcal B(X)$ is a *Borel measure*. But not every Borel measure is "good" for analysis; the class of measures that *do* behave well with respect to the topology is the class of **Radon measures**:

> **Definition.** A Borel measure $\mu$ on a topological space $X$ is *Radon* if (i) it is *locally finite* ($\mu(K)<\infty$ for every compact $K$), (ii) it is *inner regular* on open sets ($\mu(U)=\sup\{\mu(K):K\subseteq U,\ K\text{ compact}\}$ for every open $U$), and (iii) it is *outer regular* on Borel sets ($\mu(E)=\inf\{\mu(U):E\subseteq U,\ U\text{ open}\}$ for every Borel $E$).

The regularity conditions (ii) and (iii) are the statements that the measure *sees* the topology: the measure of an open set is the *supremum* of the measures of the compact sets inside it (inner regularity), and the measure of a Borel set is the *infimum* of the measures of the open sets containing it (outer regularity). These are the conditions that make the measure *compatible* with the topology, and they are the conditions that the Riesz–Markov–Kakutani theorem (§3.3) requires of the representing measure.

A key regularity fact, which we state precisely: **on a Polish space — more generally, on any Suslin space (Ulam's theorem) — every finite Borel measure is Radon** (locally finite, inner- and outer-regular). This is the fact that makes the Borel measures on the "nice" spaces (Polish, locally compact) *good* for analysis, and it is the fact that underlies the applicability of the Riesz–Markov–Kakutani theorem to the standard spaces of analysis ($\mathbb R^n$, manifolds, etc.). The regularity is automatic on these spaces; it is a *theorem* (not a definition) that finite Borel measures on Polish (indeed, on any separable metric) space are Radon. The statement for *general* (non-separable) metric spaces is more delicate: inner regularity with respect to compact sets can fail there, and counterexamples are tied to large-cardinal (measurable-cardinal) hypotheses rather than to ZFC alone — so the Polish/Suslin restriction is the clean, ZFC-robust form of the result.

### 5.2 The Riesz–Markov–Kakutani theorem (restated with hypotheses)

We restate the Riesz–Markov–Kakutani theorem (§3.3) with its standing hypothesis made explicit, since it is the central theorem of this section:

> **Theorem (Riesz–Markov–Kakutani).** Let $X$ be a *locally compact Hausdorff* space. Then, over the *real* scalar field, the dual $C_0(X)^*$ is isometrically isomorphic to the space $\mathcal M(X)$ of finite signed *Radon* measures on $X$ (and, over the *complex* scalar field, to the space of finite *complex* Radon measures), via $\mu\mapsto\left(f\mapsto\int_X f\,d\mu\right)$.

The standing hypothesis — *locally compact Hausdorff* — is essential. It is satisfied by all locally compact metric spaces and by all (finite-dimensional) manifolds, but it is *not* satisfied by every Polish space (e.g., $\ell^2$ is Polish but not locally compact), and the theorem does *not* apply to $C_0(\ell^2)$ in this form. The theorem is the *duality* between the algebra of continuous functions (a *topological* object, determined by the topology of $X$) and the space of Radon measures (a *measure-theoretic* object), and it is the theorem that makes the topological and measure-theoretic viewpoints *coincide*.

### 5.3 Haar measure and the representation-theoretic payoff

The **Haar measure** theorem (Haar, 1933) is the statement that every *locally compact group* carries a canonical measure:

> **Theorem (Haar, 1933).** Let $G$ be a *locally compact topological group*. Then there exists a *left-invariant* Radon measure $\mu_L$ on $G$ (i.e., $\mu_L(gE)=\mu_L(E)$ for every $g\in G$ and every Borel $E$), unique up to a positive scalar multiple. Similarly, there exists a *right-invariant* Radon measure $\mu_R$, unique up to a scalar. The left and right Haar measures are related by the *modular function* $\Delta:G\to(0,\infty)$, a continuous homomorphism, via $d\mu_R(g)=\Delta(g)^{-1}\,d\mu_L(g)$. The group is *unimodular* (i.e., $\Delta\equiv 1$, so that $\mu_L=\mu_R$) if and only if the left and right Haar measures coincide.

The Haar measure is the *canonical* measure on a locally compact group, in the same sense that the Lebesgue measure is the canonical measure on $\mathbb R^n$: it is the unique (up to scale) measure that is *invariant* under the group's *natural* action (left or right translation). The *modular function* $\Delta$ measures the *failure* of the group to be unimodular, and it is the function that relates the left and right Haar measures. The Haar measure is the measure with respect to which the *Fourier analysis* on $G$ is performed, and it is the measure that makes the *Peter–Weyl theorem* and the *Plancherel theorem* (the noncommutative analogues of the Fourier series and Fourier transform) hold.

The *representation-theoretic* payoff is the content that connects measure theory to the *linear algebra* of noncommutative groups. The **Peter–Weyl theorem** states that, for a *compact* group $G$, the matrix coefficients of the irreducible unitary representations of $G$ form an *orthonormal basis* of $L^2(G)$ (with respect to the Haar measure), and the **Plancherel theorem** states that, for a *locally compact abelian* group $G$, the Fourier transform is a *unitary* isomorphism of $L^2(G)$ onto $L^2(\widehat G)$ (where $\widehat G$ is the *dual group*). These theorems are the *noncommutative* (Peter–Weyl) and *abelian* (Plancherel) analogues of the *spectral theorem* for self-adjoint operators, and they are the theorems that make the *harmonic analysis* on $G$ possible. The Haar measure is the measure that makes these theorems hold, and it is the measure that connects the *topology* of the group (the locally compact group structure) to the *measure theory* (the Haar measure) and to the *linear algebra* (the representation theory, the spectral decomposition). This is the content of the *linear-algebraic* viewpoint of integration, applied to the *topological* object of a group: the measure (Haar) is the *dual object* of the group's *algebra of functions* (the group algebra, the $C^*$-algebra $C^*(G)$), and the *representation theory* is the *spectral decomposition* of that algebra.

### 5.4 The Banach–Tarski paradox

The **Banach–Tarski paradox** (Banach and Tarski, 1924) is the *geometric* expression of the non-measurability phenomenon of §2.5:

> **Theorem (Banach–Tarski, 1924).** The solid ball $B\subset\mathbb R^3$ of radius $1$ can be decomposed into a *finite* number of *pairwise disjoint* subsets — the minimal number is *five* (R. M. Robinson, 1947; four do not suffice) — such that the pieces can be *reassembled*, using only *rigid motions* (rotations and translations), into *two* solid balls of radius $1$ (each congruent to the original ball $B$).

The paradox is *not* a contradiction; it is a *theorem* of ZFC (Zermelo–Fraenkel set theory with the axiom of choice). The *pieces* are *not* measurable (they are constructed from a Vitali-type set using the action of a *free subgroup* of the rotation group $SO(3)$, which is isomorphic to the *free group on two generators* $F_2$), and the *rigid motions* that reassemble them do *not* preserve the (non-existent) measure of the pieces. The paradox is thus the statement that the *Lebesgue measure* (the "volume") cannot be extended to a *rotation-invariant* measure on *all* subsets of $\mathbb R^3$: if it could, the paradox would give $1=\operatorname{vol}(B)=\operatorname{vol}(B)+\operatorname{vol}(B)=2$, a contradiction.

The *linear-algebraic* content of the Banach–Tarski paradox is the *free group* structure. The rotation group $SO(3)$ contains a *free subgroup* on two generators (a subgroup isomorphic to $F_2$), and the *action* of $F_2$ on the sphere $S^2$ (by rotation) is what produces the *paradoxical decomposition*: the sphere is *paradoxical* with respect to the action of $F_2$ (it can be decomposed into pieces that reassemble into two copies of itself), and this *paradoxicality* is what makes the Banach–Tarski decomposition possible. The *free group* $F_2$ is the *linear-algebraic* (group-theoretic) object that underlies the paradox, and the *non-measurability* of the pieces is the *measure-theoretic* content. The Banach–Tarski paradox is thus the theorem that connects the *measure theory* (the non-measurability of the pieces) to the *group theory* (the free subgroup of $SO(3)$) and to the *set theory* (the axiom of choice, which is required to construct the pieces). It is the theorem that shows that the *measure* (the "volume") is *not* a *complete* invariant of the *geometry* (the rigid motions): there are sets that are *congruent* (related by a rigid motion) but that have *different* "volumes" (one is measurable, the other is not), and this is the sense in which the measure is a *strictly finer* structure than the geometry.

### 5.5 The Kolmogorov extension theorem and the Kolmogorov construction

The **Kolmogorov extension theorem** (Kolmogorov, 1933; also called the Daniell–Kolmogorov theorem) is the theorem that allows one to construct a probability measure on a *product space* from a *consistent* family of finite-dimensional distributions, and it is the theorem that underlies the *Kolmogorov construction* of stochastic processes.

> **Theorem (Kolmogorov extension).** Let $(X,\mathcal A)$ be a measurable space and $\{X_i,\mathcal A_i\}_{i\in I}$ a family of measurable spaces. Let $\{P_F\}_{F\subseteq I,\ F\text{ finite}}$ be a *consistent* family of probability measures on the finite products $\prod_{i\in F}X_i$ (consistent meaning that the *marginals* agree: for $F\subseteq G\subseteq I$, the marginal of $P_G$ on $\prod_{i\in F}X_i$ is $P_F$). Then there exists a probability measure $P$ on the *full* product $\prod_{i\in I}X_i$ (with the product $\sigma$-algebra) whose finite-dimensional marginals are the $P_F$; the measure is *unique* on the product $\sigma$-algebra when each $X_i$ is a standard Borel space (in particular when $I$ is countable), and in full generality it is unique on the $\sigma$-algebra generated by the finite-coordinate cylinders.

A word on the naming: this is the *Kolmogorov extension theorem*, a distinct result from the *Hahn–Kolmogorov extension theorem* (which extends a countably additive pre-measure on an *algebra* of sets to the $\sigma$-algebra it generates). The Hahn–Kolmogorov theorem is the *technical engine* of the proof here — it is what extends the measure on the algebra of *cylinder sets* to the full product $\sigma$-algebra — but it is not the theorem stated in the box. The *consistency* condition is the *necessary and sufficient* condition for the existence of the product measure, and the *uniqueness* is the statement that the product measure is *determined* by its finite-dimensional marginals. The Kolmogorov extension theorem is the *measure-theoretic* content of the *Kolmogorov construction*: given a *consistent* family of finite-dimensional distributions (the "marginals" of a stochastic process), there is a *unique* probability measure on the *path space* (the space of all sample paths) that has those marginals. This is the theorem that makes the *existence* of stochastic processes (Brownian motion, the Poisson process, etc.) a *measure-theoretic* statement, and it is the theorem that connects the *finite-dimensional* (the "discrete" or "approximate") to the *infinite-dimensional* (the "continuum" or "exact") in the probabilistic setting.

The **Kolmogorov construction** (Kolmogorov, 1933) is the application of the Kolmogorov extension theorem to the *construction of Brownian motion*: one specifies the *finite-dimensional distributions* of Brownian motion (the Gaussian distributions with the correct covariances), verifies *consistency*, and then invokes the Kolmogorov extension theorem to obtain a *unique* probability measure on the *path space* $C([0,1])$ (the space of continuous functions) that is the *law* of Brownian motion. The Kolmogorov construction is the *measure-theoretic* foundation of the *theory of stochastic processes*, and it is the theorem that makes the *probabilistic* viewpoint of integration (the *expectation* as an integral with respect to a *probability measure*) rigorous. It is the theorem that connects the *measure theory* (the product measure, the Kolmogorov extension) to the *probability theory* (the stochastic process, the law) and to the *functional analysis* (the path space, the infinite-dimensional measure).

---

## 6. Vector-valued integration: Bochner, Pettis, and the dual viewpoint

### 6.1 The Bochner integral

The **Bochner integral** (Bochner, 1933) is the extension of the Lebesgue integral to *Banach-space-valued* functions. The setup is as follows. Let $(X,\mathcal A,\mu)$ be a measure space and $E$ a Banach space. A function $f:X\to E$ is *Bochner measurable* (or *strongly measurable*) if it is the *pointwise a.e. limit* of a sequence of *simple* $E$-valued functions (finite linear combinations of indicator functions of measurable sets with values in $E$); equivalently, $f$ is measurable and *essentially separably valued* (its image is contained in a *separable* closed subspace of $E$, a.e.). The *Bochner integral* of $f$ is defined by *approximation* by simple functions, exactly as in the scalar case:

$$
\int_X f\,d\mu=\lim_{n\to\infty}\sum_{k=1}^{K_n} f(x_k^n)\,\mu(E_k^n),
$$

where the limit is taken in the *norm* of $E$, and it exists if and only if $f$ is Bochner measurable and $\int_X\|f\|\,d\mu<\infty$ (i.e., the *norm* of $f$ is in $L^1$).

The *strong measurability* condition (a.e. separably valued) is the *essential* hypothesis of the Bochner integral, and it is the hypothesis that distinguishes the Bochner integral from the *Pettis integral* (below). The strong measurability is *automatic* when $E$ is *separable* (every measurable $E$-valued function is strongly measurable), and it is the condition that *fails* for *non-separable* Banach spaces (there are measurable functions into a non-separable $E$ that are *not* strongly measurable). The *Radon–Nikodym property* (RNP) of a Banach space $E$ is the property that *every* $E$-valued measure of bounded variation has a *Bochner integrable* density, and it is the property that characterizes the Banach spaces for which the Bochner integral "behaves well" (it is the property that makes the *vector-valued* Radon–Nikodym theorem hold). The RNP is a *genuine* property of the Banach space (it is not automatic): every reflexive space has the RNP, and more generally every separable dual space has it; at the other extreme, a space $L^1(\mu)$ has the RNP if and only if $\mu$ is purely atomic, so $\ell^1=L^1(\text{counting measure on }\mathbb N)$ has the RNP while $L^1[0,1]$ (Lebesgue measure) does not.

### 6.2 The Pettis integral and the duality

The **Pettis integral** (Pettis, 1937) is the *dual* of the Bochner integral. A function $f:X\to E$ is *Pettis measurable* (or *weakly measurable*) if, for *every* $e^*\in E^*$, the *scalar* function $x\mapsto e^*(f(x))$ is measurable. The *Pettis integral* of $f$ is the (unique, if it exists) element $\int_X f\,d\mu\in E$ characterized by the *duality* formula:

$$
e^*\left(\int_X f\,d\mu\right)=\int_X e^*(f(x))\,d\mu(x)\qquad\text{for every }e^*\in E^*.
$$

The *duality* is the content: the Pettis integral is *defined* by its *pairings* with the dual $E^*$, and it is the *dual* object of the Bochner integral. The relationship between the two integrals is:

> **Theorem (Bochner–Pettis relation).** If $f$ is Bochner integrable, then it is Pettis integrable, and the two integrals *coincide*: $\int_X f\,d\mu$ (Bochner) $=\int_X f\,d\mu$ (Pettis). The converse is *false* in general: there are Pettis-integrable functions that are *not* Bochner-integrable. The converse *holds* when $E$ is *separable* (or, more generally, when $f$ is *strongly* measurable).

The *content* of the Bochner–Pettis relation is that the *Bochner* integral is the *strong* (norm) notion, and the *Pettis* integral is the *weak* (duality) notion; the Bochner integral *implies* the Pettis integral, but not conversely (in general). The *difference* between the two is the *strong measurability* condition: the Bochner integral requires *strong* measurability (a.e. separably valued), and the Pettis integral requires only *weak* measurability (scalar-measurable). The *Pettis integral* is the *dual* viewpoint of integration, and it is the viewpoint that connects the *vector-valued* integral to the *duality* of the Banach space $E$.

### 6.3 Vector measures: the Nikodým boundedness theorem and the Dunford–Pettis property

A **vector measure** is a countably additive set function $\nu:\mathcal A\to E$ (with values in a Banach space $E$). The *total variation* of $\nu$ is the (scalar) measure $|\nu|(E)=\sup\left\{\sum_{k=1}^{K}\|\nu(E_k)\|:\ \{E_k\}\text{ a finite partition of }E\right\}$, and $\nu$ is of *bounded variation* if $|\nu|(X)<\infty$. The *Radon–Nikodym property* (RNP) of $E$ is the property that *every* $E$-valued measure of bounded variation has a *Bochner integrable* *density* (a *representing function* $g\in L^1(E)$ such that $\nu(E)=\int_E g\,d\mu$).

The **Nikodým boundedness theorem** is the *uniform boundedness* theorem for vector measures:

> **Theorem (Nikodým boundedness).** Let $\{\nu_\alpha\}_{\alpha\in A}$ be a family of vector measures on $(X,\mathcal A)$ with values in a Banach space $E$. If the family is *pointwise bounded* (i.e., for every $E\in\mathcal A$, $\sup_{\alpha}\|\nu_\alpha(E)\|<\infty$), then the family is *uniformly bounded* (i.e., $\sup_{\alpha}|\nu_\alpha|(X)<\infty$).

The proof is a *Baire category* argument, and it is *not* a trivial application of the Banach–Steinhaus (uniform boundedness) principle — a trivial reduction would make Nikodým boundedness a routine corollary rather than a landmark result. Concretely, each finite measure $\nu_\alpha$ defines a bounded linear functional $T_{\nu_\alpha}$ on the Banach space $B(\mathcal A)$ of *bounded measurable* functions (sup norm), $T_{\nu_\alpha}(f)=\int f\,d\nu_\alpha$, with operator norm $\|T_{\nu_\alpha}\|=|\nu_\alpha|(X)$ (the total variation). But the pointwise-boundedness hypothesis controls the family only on the *indicator* functions $\mathbf 1_E$ ($E\in\mathcal A$), and the indicators are *not* norm-dense in $B(\mathcal A)$ (the constant function $\tfrac12$ sits at distance $\tfrac12$ from every indicator), so Banach–Steinhaus cannot be invoked directly on $B(\mathcal A)$. The Baire category theorem is what closes this gap, upgrading pointwise boundedness on the indicators to the uniform bound $\sup_\alpha|\nu_\alpha|(X)<\infty$. (The scalar version — finite signed measures — is the classical theorem of Nikodým (1930); the vector-valued version follows by scalarizing with $e^*\in E^*$ and a further uniform-boundedness step.)

The **Dunford–Pettis property** of a Banach space $E$ is the property that *every* weakly compact operator from $E$ to any Banach space is *completely continuous* (maps weakly convergent sequences to norm-convergent sequences). The two properties are linked by a classical theorem: if $E^*$ has the RNP, then $E$ has the Dunford–Pettis property. The RNP governs the *representation* of vector measures (when they have densities), and the Dunford–Pettis property governs the *compactness* behavior of weakly compact operators; together they are the two geometric properties that control the vector-valued integration theory and distinguish the "nice" Banach spaces from the "pathological" ones in this setting.

### 6.4 Applications: weak PDE formulations, Young measures, measure-valued solutions

The *vector-valued* integration theory is the theory that underlies the *weak* formulation of PDEs, the *Young measure* theory, and the *measure-valued* solutions of conservation laws. We describe the three applications.

**Weak PDE formulations.** A *weak solution* of a PDE is a function $u$ (often in a Sobolev space $W^{1,p}$) that satisfies the PDE in the *duality* sense: for every *test function* $v$ (in the dual Sobolev space), the *bilinear form* $B(u,v)$ (defined by *integration by parts*) equals the *linear functional* $F(v)$ (defined by the *data*). The *integration by parts* is the *vector-valued* (or, more precisely, the *distributional*) integration, and it is the content that makes the *weak* formulation possible. For a function $u$ of *bounded variation* (BV), the *distributional derivative* $Du$ is a finite *vector measure*, and the *weak formulation* of a conservation law or a free-discontinuity problem is the statement that this *vector measure* pairs with the *test functions* to give the PDE; for a general $W^{1,p}$ function, by contrast, the distributional derivative is a distribution (an element of $W^{-1,p'}$) rather than a measure. The *vector-valued* integration theory (the Bochner and Pettis integrals, the vector measures) is the theory that makes this *duality* rigorous, and it is the theory that connects the *PDE* (the *differential* equation) to the *measure* (the *distributional derivative*).

**Young measures.** A *Young measure* is a *probability measure* on $\mathbb R$ (or on a Banach space) that is *parameterized* by a *spatial* variable: a Young measure $\nu=(\nu_x)_{x\in X}$ is a *measurable* family of probability measures $\nu_x$ on $\mathbb R$. Young measures arise as the *weak-* limits of *sequences* of functions that *oscillate* or *concentrate*: if $u_n$ is a bounded sequence in $L^p$ ($p<\infty$), then (up to a subsequence) the *pushforwards* $(u_n)_\#\lambda$ (the *measures* induced by $u_n$) converge *weakly-* to a *Young measure* $\nu$, and the *non-convex* functional $F(u)=\int f(u)\,d\lambda$ (with $f$ *non-convex*) satisfies the *relaxation* formula
$$\lim_{n\to\infty}F(u_n)=\int_X\int_{\mathbb R} f(y)\,d\nu_x(y)\,d\lambda(x),
$$
where, provided $f$ is continuous with at most linear growth and $u_n\rightharpoonup u$ weakly in $L^p$, the right-hand side is the *lower semicontinuous envelope* of the functional along the sequence; when the *barycenter* of each $\nu_x$ is fixed (equal to the weak limit $u(x)$), the minimum of $\int_{\mathbb R} f(y)\,d\nu_x(y)$ over all probability measures with barycenter $u(x)$ is $\operatorname{conv}(f)(u(x))$ (the *convex envelope* of $f$), so the *relaxed* functional is $\int_X \operatorname{conv}(f)(u)\,d\lambda$. The *Young measure* is the *measure-valued* object that captures the *oscillation* of the sequence $u_n$, and it is the object that makes the *relaxation* of *non-convex* functionals (the *calculus of variations*, the *homogenization*) possible. The *vector-valued* integration theory (the *weak-* convergence of measures, the *Prokhorov theorem*) is the theory that makes the *Young measure* theory rigorous, and it is the theory that connects the *non-convex* functional (the *nonlinear* PDE) to the *measure* (the *Young measure*).

**Measure-valued solutions of conservation laws.** A *conservation law* is a PDE of the form $\partial_t u+\partial_x\cdot F(u)=0$, and a *measure-valued solution* is a *measure* $\mu$ (rather than a *function* $u$) that satisfies the conservation law in the *weak* (measure) sense. The *measure-valued* solutions arise when the *classical* (function-valued) solutions *break down* (e.g., at *shocks*), and they are the *natural* generalization of the *function-valued* solutions. The *vector-valued* integration theory (the *weak-* convergence of measures, the *Young measure* theory) is the theory that makes the *measure-valued* solutions rigorous, and it is the theory that connects the *conservation law* (the *nonlinear* PDE) to the *measure* (the *measure-valued solution*). The *Prokhorov theorem* (the *tightness* criterion for the *weak-* compactness of probability measures) is the theorem that guarantees the *existence* of the *measure-valued* solutions (by providing the *compactness* that allows one to pass to a *weak-* limit), and it is the theorem that connects the *measure theory* (the *weak-* convergence) to the *PDE* (the *measure-valued solution*).

---

## 7. The numerical-analytic viewpoint: integration and discretization

### 7.1 Quadrature as measure approximation; the moment problem; Gaussian quadrature

A *quadrature formula* is a *discrete* approximation to the *integral*: it is a formula of the form
$$\int_a^b f(x)\,dx\ \approx\ \sum_{j=1}^{n} w_j\,f(x_j),
$$
where the $x_j$ are the *nodes* and the $w_j$ are the *weights*. The *quadrature measure* is the *discrete* measure
$$\mu_h=\sum_{j=1}^{n} w_j\,\delta_{x_j},
$$
the *atomic* measure supported on the *nodes* $x_j$ with *weights* $w_j$, and the *quadrature formula* is the statement that the *integral* with respect to the *quadrature measure* $\mu_h$ *approximates* the *integral* with respect to the *continuous* measure (the *Lebesgue measure* $dx$ on $[a,b]$). The *quadrature* is thus the *approximation* of a *continuous* measure (the *Lebesgue measure*) by a *discrete* measure (the *quadrature measure*), and the *convergence* of the quadrature (as the number of nodes $n\to\infty$) is the *convergence* of the *discrete* measure to the *continuous* measure.

The *moment problem* is the *inverse* problem: given the *moments* $m_k=\int x^k\,d\mu(x)$ of a measure $\mu$, *recover* the measure $\mu$. The *moment problem* comes in three forms, depending on the *support* of $\mu$:

- **The Hausdorff moment problem** (support $[a,b]$, a *bounded* interval): the measure $\mu$ is *uniquely* determined by its moments (the *determinacy* holds), and the *Hausdorff* criterion (a *total-positivity* condition on the moment sequence) characterizes the moment sequences that arise from measures on $[a,b]$.
- **The Stieltjes moment problem** (support $[0,\infty)$, a *half-line*): the measure $\mu$ is *not* always *uniquely* determined by its moments (the *indeterminacy* can occur), and the *Stieltjes* criterion (positive-semidefiniteness of the two Hankel matrices $(m_{i+j})_{i,j\ge 0}$ and $(m_{i+j+1})_{i,j\ge 0}$) characterizes the moment sequences that arise from measures on $[0,\infty)$.
- **The Hamburger moment problem** (support $(-\infty,\infty)$, the *whole line*): the measure $\mu$ is *not* always *uniquely* determined by its moments (the *indeterminacy* can occur), and the *Hamburger* criterion (positive-semidefiniteness of the Hankel matrices $(m_{i+j})_{i,j\ge 0}$) characterizes the moment sequences that arise from measures on $(-\infty,\infty)$.

The moment problem is the inverse problem behind the quadrature: it asks whether the *discrete* measure (the *quadrature measure*, fixed by its *moments*) is the *unique* measure with those moments, and hence whether the quadrature is *determined* by the data it is asked to reproduce. The answer is what controls the *convergence* of the quadrature: if the moment problem is *determinate*, the quadrature measure is the unique candidate and converges to the continuous measure; if it is *indeterminate*, several measures share the same moments, and no quadrature based on those moments alone can be *uniquely* identified.

The **Gaussian quadrature** is the *optimal* quadrature formula, and its *optimality* is a *linear-algebraic* statement. The *Gaussian quadrature* with $n$ nodes is the quadrature formula that is *exact* for all *polynomials* of degree $\le 2n-1$ (the *highest* possible degree for an $n$-node formula), and the *nodes* $x_1,\dots,x_n$ are the *zeros* of the *orthogonal polynomial* $p_n$ of degree $n$ (with respect to the *weight* $w$ and the *measure* $d\mu$). The *linear-algebraic* content is the *Jacobi matrix*: the *three-term recurrence* for the *orthogonal polynomials*
$$x\,p_k(x)=a_{k+1}\,p_{k+1}(x)+b_k\,p_k(x)+a_k\,p_{k-1}(x)$$
is *equivalent* to the *eigenvalue problem* for the *tridiagonal* (Jacobi) matrix
$$J=\begin{pmatrix} b_1 & a_2 \\ a_2 & b_2 & a_3 \\ & a_3 & b_3 & \ddots \\ &&\ddots&\ddots&\ddots\end{pmatrix},$$
and the *nodes* of the *Gaussian quadrature* are the *eigenvalues* of the *Jacobi matrix* $J$ (the *truncation* to $n\times n$). The *Gaussian quadrature* is thus the *eigenvalue problem* for the *Jacobi matrix*, and the *nodes* are the *eigenvalues* (the *spectrum* of the *multiplication operator* by $x$, truncated to the *$n$-dimensional* subspace spanned by the *first $n$ orthogonal polynomials*). In other words, Gaussian quadrature is *Rayleigh–Ritz* (the *truncated spectral problem*) applied to the *multiplication operator*: the quadrature is the *measure approximation* seen through the *linear algebra* of the *eigenvalue problem* and the *Jacobi matrix*.

### 7.2 The convergence of quadrature in $L^p$; the Peano kernel; superconvergence

The *convergence* of a *quadrature formula* is the statement that the *quadrature error*
$$E(f)=\int_a^b f(x)\,dx-\sum_{j=1}^{n} w_j\,f(x_j)$$
*goes to zero* as $n\to\infty$, for a *class* of functions $f$. The *rate* of convergence is the *order* of the *quadrature*, and it is a *measure* statement (it is a bound on the *quadrature error*, which is a *measure* quantity). The *Peano kernel theorem* is the theorem that gives the *exact* form of the *quadrature error* in terms of the *derivative* of $f$:

> **Theorem (Peano kernel).** Let $E$ be a *linear* functional on $C^k[a,b]$ that *annihilates* the *polynomials* of degree $<k$ (i.e., $E(p)=0$ for all $p$ with $\deg p<k$). Then there exists a *function* $K\in L^1[a,b]$ (the *Peano kernel*) such that
> $$E(f)=\int_a^b K(t)\,f^{(k)}(t)\,dt\qquad\text{for all }f\in C^k[a,b].$$

The *Peano kernel* $K$ is the *representing function* of the *quadrature error* $E$ (with respect to the *$k$-th derivative*), and the theorem is the *Radon–Nikodym* step of the quadrature theory: the *quadrature error* (a *linear functional*) is *represented* by a *function* (the *Peano kernel*), and the *rate* of convergence is controlled by the *size* of the *Peano kernel* (the *$L^1$ norm* of $K$). The *superconvergence* of the *Gaussian quadrature* (the *exactness* for polynomials of degree $\le 2n-1$) is the *linear-algebraic* shadow of this: the *Gaussian quadrature* *annihilates* the *polynomials* of degree $<2n$ (the *highest* possible), so its *Peano kernel* vanishes on that space and the error is forced to depend on a *higher* derivative.

### 7.3 Empirical measures and the law of large numbers; Glivenko–Cantelli; Monte Carlo

The *empirical measure* is the *discrete* measure associated to a *sample*: given a *sample* $x_1,\dots,x_N$ (i.i.d. with *law* $\mu$), the *empirical measure* is
$$\mu_N=\frac{1}{N}\sum_{i=1}^{N}\delta_{x_i},
$$
the *atomic* measure supported on the *sample points* $x_i$ with *equal* weights $1/N$. The empirical measure is the object that *converges* (as $N\to\infty$) to the *law* $\mu$ (the *continuous* measure), and the *law of large numbers* is the statement of that *convergence*:

> **Theorem (strong law of large numbers).** Let $x_1,x_2,\dots$ be i.i.d. random variables with *law* $\mu$ and *finite* mean $\mathbb E|X|<\infty$. Then the *empirical measures* $\mu_N=\frac1N\sum_{i=1}^N\delta_{x_i}$ converge *weakly* to $\mu$ *almost surely*, i.e., for every *bounded continuous* function $f$,
> $$\int f\,d\mu_N=\frac{1}{N}\sum_{i=1}^N f(x_i)\ \xrightarrow[N\to\infty]{a.s.}\ \int f\,d\mu=\mathbb E[f(X)].$$

The *weak convergence* of the *empirical measures* to the *law* is exactly what the *Monte Carlo* method *exploits*: the *Monte Carlo* estimate of the *integral* $\int f\,d\mu$ is the *empirical* average $\frac1N\sum f(x_i)$, so the *convergence* of the estimate to the integral *is* the weak convergence of $\mu_N$ to $\mu$. The *rate* of convergence is $O(N^{-1/2})$: by the *central limit theorem* the *error* is *Gaussian* with *variance* $O(N^{-1})$, a rate that no deterministic quadrature of the same cost beats in high dimensions.

The **Glivenko–Cantelli theorem** is the *uniform* version of the *law of large numbers*:

> **Theorem (Glivenko–Cantelli).** Let $x_1,x_2,\dots$ be i.i.d. with *distribution function* $F$ (no regularity on $F$ is needed). Then the *empirical distribution function* $F_N(t)=\frac1N\#\{i\le N:x_i\le t\}$ converges *uniformly* to $F$ *almost surely*, i.e.,
> $$\sup_{t\in\mathbb R}|F_N(t)-F(t)|\ \xrightarrow[N\to\infty]{a.s.}\ 0.$$

The *Glivenko–Cantelli theorem* upgrades the *pointwise* (weak) convergence of the empirical measures to *uniform* convergence, and it is the theorem that makes the *non-parametric* *statistical* estimates (the *empirical* distribution, the *kernel* density estimate) *consistent*. Uniform convergence is the *stronger* mode: it controls the error *simultaneously at every point* $t$, not one at a time.

The *Wasserstein distance* (the *optimal transport* distance on the *space of probability measures*) is the *metric* that *refines* the weak convergence by *tracking the location* of the *mass*. The *Wasserstein* convergence $\mu_N\to\mu$ in $W_p$ is *stronger* than the weak convergence (it *implies* the weak convergence *plus* the *convergence* of the *$p$-th moments*), and it is the metric in which the *continuum limit* of *particle systems* (the *mean-field* limit) is *measured*: it connects the *discrete* (the *empirical measure* of the *particles*) to the *continuum* (the *density* of the *mean-field* PDE) in a way the weak topology cannot, because the weak topology forgets *where* the mass is. We do not develop the *Wasserstein* theory here (it is the subject of the companion essay on measure and metrics); the point for the present thread is that the *numerical* *continuum limit* (the convergence of the discrete to the continuum) is a *metric* statement, and the Wasserstein distance is the metric in which it is made precise.

### 7.4 Weak convergence and Banach–Alaoglu compactness in the finite-element method

The *finite-element method* (FEM) is the *discretization* of a *continuous* problem (a PDE, a *variational* problem) into a *finite-dimensional* problem (a *linear system*). The *convergence* of the *discrete* solution to the *continuous* solution is in the *weak topology* (the *weak convergence* in the *function space*), and the *compactness* that guarantees the *existence* of a *convergent subsequence* is the *Banach–Alaoglu theorem*:

> **Theorem (Banach–Alaoglu).** The *closed unit ball* of the *dual* $X^*$ of a *normed space* $X$ is *compact* in the *weak-* topology $\sigma(X^*,X)$. Equivalently, every *bounded* sequence in $X^*$ has a *weakly-* *convergent* subsequence.

The *Banach–Alaoglu theorem* is the *compactness* theorem that makes the *FEM* *convergence* go through: the *discrete* solutions $u_h$ (the *Galerkin* approximations) are *bounded* in the *continuous* function space (the *a priori* *stability* estimate), and the *Banach–Alaoglu theorem* (applied to the *dual* of the *continuous* space) gives a *weakly-* *convergent* subsequence, and the *uniqueness* of the *continuous* solution (the *well-posedness*) upgrades the subsequence to the *whole* sequence. The weak convergence is the mode that *survives* the *discretization* (the passage from the continuous to the discrete): it is the *duality* (the $L^2$ or $H^1$ pairing) that remains intact when the infinite-dimensional problem is truncated to a finite one.

The *a priori* *error estimate* of the *FEM* is the *bound* on the *error* $\|u-u_h\|$ (in the *appropriate* norm, the *$L^2$* or the *$H^1$* norm) in terms of the *mesh size* $h$ (the *discretization* parameter) and the *regularity* of the *continuous* solution $u$ (the *smoothness*). The *rate* of convergence (e.g., $O(h^k)$ for a *$k$-th order* method) is a *bound on a normed error*, and the *regularity* of $u$ is what *determines* the rate: the smoother $u$, the higher the order. The a priori estimate is thus the *bridge* between the *discrete* (the mesh size $h$) and the *continuous* (the regularity of $u$).

### 7.5 The discretization of Radon measures; the Young measure

The *discretization* of a *Radon measure* is the *approximation* of a *continuous* (the *Radon*) measure by a *discrete* (the *atomic*) measure, and it is the common thread of the numerical examples above. The *quadrature* (§7.1) replaces the *Lebesgue measure* (the *Radon measure* on $[a,b]$) by the *quadrature measure* (the *atomic measure* on the *nodes*); the *empirical measure* (§7.3) replaces the *law* (the *probability measure*) by the *atomic measure* on the *sample points*; and the *Young measure* (§6.4) replaces the *oscillating* *sequence* by the *parameterized* *probability measure*, capturing the *oscillation* (the *non-convergence* in the *strong* topology) of the sequence.

The *finite-element exterior calculus* (the *discretization* of the *de Rham complex* by the *finite-element* spaces) replaces the *measure* (the *current*, the *distributional* *measure*) by the *finite-element* *forms*; the *measure-valued* *solutions* (§6.4) replace the *function-valued* *solutions* by the *measure-valued* *solutions*, and they are the *discretization* that *survives* the *breakdown* of the *classical* *solutions* (the *shocks*, the *concentration*). Taken together, these are the *discretization* that connects the *continuous* (the *Radon measure*) to the *discrete* (the *atomic measure*, the *finite-element* *form*).

---

## 8. The modern developments (1930s–present)

### 8.1 Ergodic theory: Birkhoff, von Neumann, and the Koopman operator

The *ergodic theory* studies *measure-preserving transformations*: the invariant measure is the *measure-theoretic* input, the transformation is the *dynamical* input, and the *Koopman operator* is the *linear-algebraic* output. The *two* fundamental *ergodic theorems* are the *mean ergodic theorem* (von Neumann, 1932) and the *pointwise ergodic theorem* (Birkhoff, 1931):

> **Theorem (von Neumann mean ergodic theorem, 1932).** Let $T:L^2(X,\mathcal A,\mu)\to L^2(X,\mathcal A,\mu)$ be a *unitary* operator (the *Koopman operator* of a *measure-preserving transformation*). Then the *ergodic averages* $\frac1N\sum_{n=0}^{N-1}T^n f$ converge *in norm* (in $L^2$) to the *projection* $Pf$ of $f$ onto the *subspace* of *$T$-invariant* functions (the *fixed-point* subspace $\{g:Tg=g\}$).

> **Theorem (Birkhoff pointwise ergodic theorem, 1931).** Let $T:(X,\mathcal A,\mu)\to(X,\mathcal A,\mu)$ be a *measure-preserving* transformation and $f\in L^1(X,\mathcal A,\mu)$. Then the *ergodic averages* $\frac1N\sum_{n=0}^{N-1} f(T^n x)$ converge *almost everywhere* (and in $L^1$) to the *conditional expectation* $\mathbb E[f\mid\mathcal I]$ of $f$ with respect to the *$\sigma$-algebra* $\mathcal I$ of *$T$-invariant* sets.

The *two theorems* are the *$L^2$* (the *mean*, the *norm*) and the *$L^1$* (the *pointwise*, the *a.e.*) versions of the *same* statement: the *ergodic averages* converge to the *invariant part* of $f$. The *von Neumann* theorem is the *Hilbert-space* (the *$L^2$*) version, and it is proved by the *spectral theorem* (the *Koopman operator* is *unitary*, and the *ergodic averages* converge to the *projection* onto the *eigenvalue* $1$). The *Birkhoff* theorem is the *$L^1$* (the *pointwise*) version, and it is proved by the *Birkhoff maximal inequality*, the dynamical counterpart of the *Hardy–Littlewood maximal function*. The *Koopman operator* is the *linear-algebraic* face of the theory: it is the *unitary operator* on $L^2$ that *represents* the *measure-preserving transformation*, and its *spectrum* (the *eigenvalues*, the *continuous part*) encodes the *dynamics* (the *ergodicity*, the *mixing*, the *periodicity*).

### 8.2 Martingale theory, the maximal function, and the Lebesgue differentiation theorem

The *martingale theory* is the theory of *adapted* *stochastic processes* (the *processes* that are *measurable* with respect to the *increasing* family of *$\sigma$-algebras* $\{\mathcal F_n\}$). It sits at the intersection of *measure theory* (the *conditional expectation*), *probability* (the *martingale*), and *harmonic analysis* (the *maximal function*), and its central result is the *martingale convergence theorem*:

> **Theorem (martingale convergence).** Let $(M_n,\mathcal F_n)_{n\ge 0}$ be a *martingale* with $\sup_n\mathbb E|M_n|<\infty$ (or $\sup_n\mathbb E|M_n|^p<\infty$ for $p>1$). Then $M_n$ converges *almost surely* (and in $L^1$, or in $L^p$ for $p>1$) to a *limit* $M_\infty$.

The *martingale convergence theorem* makes the *stochastic* *convergence* (the *a.e.* *convergence* of the *martingale*) rigorous, and its proof rests on the *Doob maximal inequality*:

> **Theorem (Doob maximal inequality).** Let $(M_n,\mathcal F_n)_{n\ge 0}$ be a *non-negative* *submartingale*. Then, for each $N$ and $p>1$,
> $$\left\|\sup_{n\le N} M_n\right\|_p\ \le\ \frac{p}{p-1}\,\|M_N\|_p,$$
> and, for $p=1$, $\mu\{\sup_{n\le N} M_n\ge\lambda\}\le\frac{1}{\lambda}\mathbb E[M_N]$ for every $\lambda>0$.

The *Doob maximal inequality* is the bridge between the *martingale* (the *stochastic process*) and the *maximal function* (the *harmonic analysis* object). The *Lebesgue differentiation theorem* is the deterministic counterpart:

> **Theorem (Lebesgue differentiation theorem).** Let $f\in L^1_{\mathrm{loc}}(\mathbb R^n)$. Then, for *almost every* $x\in\mathbb R^n$ (the *Lebesgue points* of $f$),
> $$\lim_{r\to 0}\frac{1}{|B(x,r)|}\int_{B(x,r)} f(y)\,dy\ =\ f(x).$$

The *Lebesgue differentiation theorem* says that the *Lebesgue integral* is *differentiable* in the sense that the *average* of $f$ over the *ball* $B(x,r)$ *converges* to $f(x)$ as $r\to 0$, a.e. The *Hardy–Littlewood maximal function* $Mf(x)=\sup_{r>0}\frac{1}{|B(x,r)|}\int_{B(x,r)}|f(y)|\,dy$ is the *harmonic analysis* object that *controls* the differentiation theorem, and it is of *weak $(1,1)$ type* (the *Hardy–Littlewood maximal inequality*, $\mu\{Mf\ge\lambda\}\le\frac{C}{\lambda}\|f\|_1$). The *martingale theory*, the *maximal function*, and the *Lebesgue differentiation theorem* thus form a single chain: the *Lebesgue measure* feeds the *maximal function* (the *harmonic analysis*), which feeds the *martingale* (the *probability theory*), and the *conditional expectation* is the *martingale* version of the *average over a ball*.

### 8.3 Descriptive set theory and the measurable selection theorem

The *descriptive set theory* classifies the *Borel* and *projective* sets (the *sets* that are *definable* in the *Borel hierarchy*) by their *definability*, and it is the part of *set theory* that the *measure theory* (the *measurable sets*) and the *logic* (the *definability*) both draw on. The *Borel hierarchy* orders the *Borel sets* (the $\Sigma^0_\alpha$ and $\Pi^0_\alpha$ sets, for the *countable ordinals* $\alpha$) by the *number* of *alternations* of *countable* *unions* and *intersections*. The central result for the measure-theoretic applications is the *measurable selection theorem* (the *Lusin–Novikov theorem*):

> **Theorem (measurable selection, Lusin–Novikov).** Let $X$ and $Y$ be *standard Borel* spaces (e.g., Polish spaces with their Borel $\sigma$-algebras). Let $R\subseteq X\times Y$ be a *Borel* set such that, for every $x\in X$, the *section* $R_x=\{y:(x,y)\in R\}$ is *countable*. Then there exist *countably many* *Borel* functions $f_n:X\to Y$ such that, for every $x\in X$, $R_x=\{f_n(x):n\in\mathbb N\}\setminus\{\text{undefined}\}$.

The theorem says that a *Borel* set with *countable* sections *admits* a *Borel* (the *measurable*) *selection* (a *measurable* choice of *one* point from each *section*), and it is the theorem that makes the *measurable* *feedback* *control* (the *measurable* *selection* of the *control*) possible in *stochastic* *control*. The *descriptive set theory* thus supplies the *definability* layer that the *measure theory* (the *measurable sets*) and the *logic* (the *definability*) both need.

### 8.4 Metric measure spaces: doubling measures, Poincaré inequalities, Sobolev spaces, RCD($K,N$)

The *metric measure space* is the *measure-theoretic* object that *generalizes* the *Riemannian manifold* (the *smooth* *measure* space) to the *metric* (the *non-smooth*) setting: a *metric space* $(X,d)$ equipped with a *Borel measure* $\mu$ (the *reference measure*). It is the object that *connects* the *measure theory* (the *measure*) to the *metric* (the *distance*) and to the *geometry* (the *curvature*), and the first structural hypothesis is the *doubling property*:

> **Definition (doubling).** A metric measure space $(X,d,\mu)$ is *doubling* if there exists a *constant* $C_D\ge 1$ such that, for every $x\in X$ and every $r>0$,
> $$\mu(B(x,2r))\ \le\ C_D\,\mu(B(x,r)).$$

The *doubling property* is the *measure-theoretic* expression of the *volume growth* of the *Riemannian manifold* (the *volume* of the *ball* at most *doubles* when the *radius* *doubles*). The *Poincaré inequality* is the second structural hypothesis:

> **Definition ($(1,p)$ Poincaré inequality).** A metric measure space $(X,d,\mu)$ satisfies a *$(1,p)$ Poincaré inequality* if there are constants $C_P>0$ and $c\ge 1$ such that, for every ball $B(x,r)$ and every Lipschitz function $f$ on $B(x,cr)$,
> $$\fint_{B(x,r)} |f-f_{B(x,r)}|\,d\mu\ \le\ C_P\,r\left(\fint_{B(x,cr)} |\operatorname{Lip} f|^p\,d\mu\right)^{1/p},$$
> where $\operatorname{Lip} f$ is the pointwise Lipschitz constant (for the metric Sobolev versions, the *upper gradient* of $f$).

The *metric Sobolev spaces* $N^{1,p}(X)$ (Cheeger), $S^p(X)$ (Reshetnyak), and the $L^p$-Sobolev class (Preiss) are the three standard definitions of the Sobolev class on a metric measure space; on *doubling* spaces they coincide, and the Poincaré inequality is the hypothesis under which the classical Sobolev and Morrey embedding theorems (and the compactness of the embedding) are valid in the metric setting. The *RCD($K,N$)* spaces (the *Ricci curvature* $\ge K$ and *dimension* $\le N$ spaces, in the *measure-theoretic* sense of *Ambrosio–Gigli–Savaré*, *Gigli*, and *Mondino*) are the *spaces* that *generalize* the *Riemannian manifolds* with *Ricci curvature* $\ge K$ and *dimension* $\le N$ to the *metric measure* (the *non-smooth*) setting, and they are the *spaces* that *connect* the *measure* (the *reference measure*) to the *metric* (the *distance*) and to the *curvature* (the *Ricci curvature*, in the *measure-theoretic* sense). The *metric measure spaces* thus *generalize* the *Riemannian* *manifolds* to the *non-smooth* setting, with the *measure*, the *metric*, and the *curvature* playing their roles in a single object.

### 8.5 Noncommutative measure theory: traces on von Neumann algebras; noncommutative $L^p$ spaces

The *noncommutative measure theory* *generalizes* the *commutative* measure theory (the *Lebesgue* measure, the *Radon* measure) to the *noncommutative* *algebras* (the *von Neumann algebras*, the *operator algebras*). The *noncommutative* *measure* is the *trace* on the *von Neumann algebra*, and the *noncommutative* $L^p$ spaces are the *noncommutative* counterpart of the *commutative* $L^p$ theory.

The *trace* on a *von Neumann algebra* $\mathcal M$ is the *noncommutative* *measure*: it is the *linear functional* $\tau:\mathcal M\to\mathbb C$ that is *positive* ($\tau(x^*x)\ge 0$), *tracial* ($\tau(xy)=\tau(yx)$), and *normal* (the *measure-theoretic* *continuity*). The *commutative* *case* is the *case* where $\mathcal M=L^\infty(X,\mathcal A,\mu)$ (the *algebra* of *essentially bounded* *measurable functions*), and the *trace* is the *integration* $\tau(f)=\int f\,d\mu$ (the *Lebesgue* *integral*). The *noncommutative* *case* is the *case* where $\mathcal M$ is a *noncommutative* *von Neumann algebra* (e.g., the *algebra* of *bounded operators* on a *Hilbert space*, $B(H)$), and the *trace* is the *noncommutative* *measure* (the *operator* *trace*, the *Dixmier* *trace*, the *singular* *trace*). The *Haagerup* $L^p$ spaces (Haagerup, 1979) are the *noncommutative* $L^p$ spaces: the *Haagerup* $L^p(\mathcal M)$ is the *noncommutative* *analogue* of the *commutative* $L^p(X,\mathcal A,\mu)$, and it is the *space* that *generalizes* the *commutative* $L^p$ space to the *noncommutative* setting. They are the *spaces* that *connect* the *noncommutative* *algebra* (the *von Neumann algebra*) to the *measure* (the *trace*) and to the *harmonic analysis* (the *noncommutative* $L^p$ theory), and the *noncommutative measure theory* is thus the *commutative* measure theory *generalized* to the *noncommutative* setting.

### 8.6 The modern probabilistic foundation: Kolmogorov, Girsanov, Malliavin

The *modern probabilistic foundation* is the *measure-theoretic* foundation of the *probability theory*, and it is the foundation that *connects* the *measure theory* (the *probability measure*) to the *stochastic analysis* (the *stochastic process*, the *stochastic integral*) and to the *PDE* (the *stochastic PDE*, the *Fokker–Planck equation*). The *Kolmogorov construction* (§5.5) is the *existence* theorem for the *stochastic process*, and the *Girsanov theorem* is the *change-of-measure* theorem:

> **Theorem (Girsanov theorem).** Let $W$ be a *Brownian motion* on a *probability space* $(\Omega,\mathcal F,\mathbb P)$, and let $\theta$ be an *adapted* *process* such that the *Novikov condition* $\mathbb E\left[\exp\left(\frac12\int_0^T\theta_s^2\,ds\right)\right]<\infty$ holds. Then the *process*
> $$W_t^\theta=W_t+\int_0^t\theta_s\,ds$$
> is a *Brownian motion* with respect to the *measure* $\mathbb Q$ defined by the *Radon–Nikodym derivative*
> $$\frac{d\mathbb Q}{d\mathbb P}=\exp\left(-\int_0^T\theta_s\,dW_s-\frac12\int_0^T\theta_s^2\,ds\right).$$

The *Girsanov theorem* says that the *Brownian motion* under the *measure* $\mathbb P$ is the *Brownian motion* (with a *drift*) under the *measure* $\mathbb Q$, and the *change of measure* is the *Radon–Nikodym derivative* (the *measure-theoretic* object). It *connects* the *probability measure* (the *law* of the *stochastic process*) to the *stochastic* *differential equation* (the *drift*, the *diffusion*) and to the *PDE* (the *Fokker–Planck equation*, the *Kolmogorov equation*). The *Malliavin calculus* *generalizes* the *classical* *integration by parts* to the *Wiener space* (the *infinite-dimensional* *Gaussian space*): it is the calculus that *connects* the *probability measure* (the *Gaussian measure* on the *Wiener space*) to the *stochastic* *integration* (the *Malliavin* *derivative*, the *divergence*) and to the *PDE* (the *stochastic PDE*, the *Malliavin* *PDE*). The *modern probabilistic foundation* thus *connects* the *measure* to the *stochastic process* and to the *PDE*, and it *generalizes* the *classical* *integration by parts* to the *infinite-dimensional* *Gaussian* setting.

---

## 9. Conclusion: integration as the unifying object

We have traced the arc of integration theory from the Riemann integral to the present, and the *structural* content of the arc is this: **the integral is the primitive object, and the measure is its shadow.** The measure is *derived* from the integral (the *Daniell–Stone theorem*, §3.1), and it is the *dual object* of the algebra of continuous functions (the *Riesz–Markov–Kakutani theorem*, §3.3). The *three* viewpoints — the *set-theoretic* (the *measure*, the *$\sigma$-algebra*, the *null ideal*), the *functional-analytic* (the *positive linear functional*, the *$L^p$ duality*, the *Banach space*), and the *topological* (the *Radon measure*, the *Haar measure*, the *Riesz–Markov duality*) — are *three faces* of the *same* object (the *integral*), and the *measure* is the *object* that *connects* the *three* viewpoints.

The *measure* is *not primitive*: it is *derived* from the *integral* (the *Daniell–Stone theorem*), and it is the *dual object* of the *continuous functions* (the *Riesz–Markov–Kakutani theorem*). The *integral* is the *unifying object*: it is the *positive linear functional* (the *functional-analytic* viewpoint), it is the *measure* (the *set-theoretic* viewpoint), and it is the *dual object* of the *continuous functions* (the *topological* viewpoint). The *three* viewpoints are *not independent*: they are *three* ways of looking at the *same* object, and the *measure* is the *object* that *connects* them.

The *numerical* *payoff* is the *discretization*: the *quadrature* is the *discretization* of the *measure* (the *continuous* measure by the *atomic* measure), the *weak convergence* is the *convergence* that *survives* the *discretization* (the *FEM* convergence, the *empirical measure* convergence), and the *Wasserstein distance* is the *metric* that *refines* the *weak convergence* (the *continuum limit* of the *particle systems*). The *measure-theoretic* thread of the *numerical analysis* is this *discretization* of the *measure*, which *connects* the *continuous* (the *measure*) to the *discrete* (the *atomic measure*, the *finite-element* form).

The *open problems* are the *extensions* of the *measure-theoretic* content to the *new* settings: the *noncommutative* measure theory (the *traces* on the *von Neumann algebras*, the *Haagerup* $L^p$ spaces), the *metric measure* spaces (the *RCD($K,N$)* spaces, the *synthetic* *Ricci* *geometry*), and the *modern* probability (the *rough paths*, the *regularity structures*, the *stochastic PDE*). The *measure-theoretic* content *generalizes* to the *new* settings, and it *connects* the *measure* to the *new* *algebras* (the *noncommutative* algebras), the *new* *spaces* (the *metric measure* spaces), and the *new* *processes* (the *rough* *paths*, the *regularity* *structures*). The *measure* is the *unifying object* that *connects* the *old* (the *Lebesgue* measure, the *Radon* measure) to the *new* (the *noncommutative* measure, the *synthetic* measure).

The *final* word is that the *integral* is the *unifying object*, and the *measure* is its *shadow*. The *integral* is the *positive linear functional* (the *functional-analytic* viewpoint), the *measure* (the *set-theoretic* viewpoint), and the *dual object* of the *continuous functions* (the *topological* viewpoint). The *three* viewpoints are *three faces* of the *same* object, and the *measure* is the *object* that *connects* them. The *art* of the *analyst* is to *choose*, for each *problem*, the *viewpoint* (or the *combination* of *viewpoints*) that *captures* the *relevant* *information*, and to be *precise* about *what* is being *derived* (the *measure* from the *integral*) and *what* is being *dualized* (the *integral* as the *dual* of the *continuous functions*).

---

## References

The references below are the standard and primary sources for the results stated in this essay. They are given for the reader who wishes to verify the claims or to develop them further; they are not a comprehensive bibliography. The historical citations have been checked against primary or authoritative sources (the original papers, the publishers' records, or the standard secondary accounts); where a precise page range could not be confirmed against a primary source, the citation is given at the level of author, title, venue, and year.

**Primary and historical sources**

1. **Riemann, G.** Habilitationsschrift, *Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe*, *Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen*, vol. 13 (written 1853/54; published 1867); and his subsequent lectures on the integral. (The definition of the Riemann integral, §1.1.)
2. **Lebesgue, H.** *Intégrale, Longueur, Aire* (thesis, Université de Paris, 1902). (The construction of the Lebesgue integral, §2.1.)
3. **Lebesgue, H.** "Sur les séries trigonométriques." *Annales scientifiques de l'École Normale Supérieure*, 3e série, vol. 20 (1903), 453–485. DOI: 10.24033/asens.530. (The Lebesgue integral applied to Fourier series, §2.1, §1.2.)
4. **Lebesgue, H.** *Leçons sur l'intégration et la recherche des fonctions primitives.* Gauthier-Villars, 1904. (The Lebesgue integral and the convergence theorems, §2.3.)
5. **Carathéodory, C.** *Realvariablen und Funktionentheorie.* Vieweg, 1927. (The Carathéodory criterion for measurability, §2.1.)
6. **Vitali, G.** "Sul problema della misura dei gruppi di punti di una retta." Bologna: Gamberini e Parmeggiani, 1905. (The non-measurable set, §2.5.)
7. **Riesz, F.** (1909). The representation of $C([0,1])^*$ (originally as Riemann–Stieltjes integrals with respect to functions of bounded variation; equivalently, by finite regular Borel measures). (The Riesz representation theorem, §3.3.)
8. **Markov, A.** (1938). Extension of the Riesz representation to non-compact spaces. (The Riesz–Markov–Kakutani theorem, §3.3.)
9. **Kakutani, S.** (1941). Extension of the Riesz–Markov theorem to compact Hausdorff spaces. (The Riesz–Markov–Kakutani theorem, §3.3.)
10. **Banach, S., Tarski, A.** "Sur la décomposition des ensembles de points en parties respectivement congruentes." *Fundamenta Mathematicae*, vol. 6 (1924), 244–277. (The Banach–Tarski paradox, §5.4.)
11. **Haar, A.** "Der Massbegriff auf den topologischen Gruppen und die Fourierische Analysis." *Mathematische Annalen*, vol. 109 (1933), 713–749. (The Haar measure, §5.3.)
12. **Kolmogorov, A.** *Grundbegriffe der Wahrscheinlichkeitsrechnung.* Ergebnisse der Mathematik und ihrer Grenzgebiete, vol. 2. Springer, 1933. DOI: 10.1007/978-3-642-49888-6. (The Kolmogorov extension theorem, the Kolmogorov construction, §5.5.)
13. **Daniell, P. J.** "A General Form of Integral." *Annals of Mathematics* (2nd ser.), vol. 19, no. 4 (1918), 279–294. (The Daniell integral, §3.1.)
14. **Stone, M. H.** "The general theory of measures." *Transactions of the American Mathematical Society*, vol. 33 (1931). (Completion of the Daniell construction; the Daniell–Stone theorem, §3.1.)
15. **Bochner, S.** "Integration von Funktionen, deren Werte die Elemente eines Vektorraumes sind." *Fundamenta Mathematicae*, vol. 20 (1933), 262–276. (The Bochner integral, §6.1.) See also Bochner, S., *Integration*, Annals of Mathematics Studies, no. 4, Princeton University Press, 1932.
16. **Pettis, B. J.** "On integration in vector spaces." *Transactions of the American Mathematical Society*, vol. 44 (1938), 57–99. DOI: 10.1090/S0002-9947-1938-1501970-8. (The Pettis integral, §6.2.)
17. **Radon, J.** (1913) and **Nikodym, O.** (1930). The Radon–Nikodym theorem: Radon's 1913 *Sitzungsberichte* paper established the $\mathbb R^n$ case, and Nikodym's 1930 *Fundamenta Mathematicae* paper (vol. 15, 131–179) the general $\sigma$-finite measure-space case. (The Radon–Nikodym theorem, §3.4.)
18. **Birkhoff, G. D.** "Proof of the Ergodic Theorem." *Proceedings of the National Academy of Sciences*, vol. 17 (1931), 656–660. (The Birkhoff pointwise ergodic theorem, §8.1.)
19. **von Neumann, J.** (1932). The mean ergodic theorem. *Proceedings of the National Academy of Sciences*, vol. 18 (1932), 248–251. (The von Neumann mean ergodic theorem, §8.1.)
20. **Haagerup, U.** "Lp-spaces associated with an arbitrary von Neumann algebra." In *Algèbres d'opérateurs et leurs applications en Physique Mathématique*, Proc. Colloq. Internat. CNRS, vol. 274. CNRS, 1979, 175–185. (The noncommutative $L^p$ spaces, §8.5.)

**Standard texts**

21. **Rudin, W.** *Real and Complex Analysis.* 3rd ed. McGraw-Hill, 1987. (The Lebesgue integral, the convergence theorems, the $L^p$ spaces, the Radon–Nikodym theorem, the Riesz representation theorem.)
22. **Bogachev, V. I.** *Measure Theory.* Vols. I–II. Springer, 2007. (The Radon measures, their regularity, the vector measures, the Radon–Nikodym property.)
23. **Federer, H.** *Geometric Measure Theory.* Springer, 1969. (The geometric measure theory, the measure-valued solutions.)
24. **Villani, C.** *Optimal Transport: Old and New.* Grundlehren der mathematischen Wissenschaften, vol. 338. Springer, 2009. (The Wasserstein distance, the continuum limit.)
25. **Ambrosio, L., Gigli, N., Savaré, G.** *Gradient Flows: Metric Space and Convexity in the Space of Probability Measures.* Birkhäuser, 2005. (The metric measure spaces, the RCD($K,N$) spaces, the synthetic Ricci geometry.)
26. **Ciarlet, P. G.** *The Finite Element Method for Elliptic Problems.* SIAM, 2002. (The finite-element method, the a priori error estimates, the weak convergence.)
27. **Dudley, R. M.** *Real Analysis and Probability.* Cambridge University Press, 1989. (The metric measure spaces, the Prokhorov theorem, the Glivenko–Cantelli theorem.)
28. **Aliprantis, C. D., Burkinshaw, O.** *Positive Operators.* Academic Press, 1985. (The Daniell integral, the vector lattices, the positive linear functionals.)
29. **Dixmier, J.** *Les C*-algèbres et leurs représentations.* 2nd ed. Gauthier-Villars, 1969. (The noncommutative measure theory, the von Neumann algebras, the traces.)
30. **Connes, A.** *Noncommutative Geometry.* Academic Press, 1994. (The noncommutative geometry, the noncommutative measure theory.)

---

*The historical citations in this essay (Riemann 1854/1867, Lebesgue 1902/1903/1904, Carathéodory 1927, Vitali 1905, Riesz 1909, Markov 1938, Kakutani 1941, Banach–Tarski 1924, Haar 1933, Kolmogorov 1933, Daniell 1918, Stone 1931, Bochner 1933, Pettis 1938, Radon 1913, Nikodym 1930, Birkhoff 1931, von Neumann 1932, Haagerup 1979) were checked against primary or authoritative sources (the original papers, the publishers' records, or the standard secondary accounts); where a precise page range could not be confirmed against a primary source, the citation is given at the level of author, title, venue, and year. The mathematical claims (the convergence theorems, the decomposition theorems, the $L^p$ duality, the Riesz–Markov–Kakutani theorem, the Haar measure, the Banach–Tarski paradox, the Bochner and Pettis integrals, the ergodic theorems, the Lebesgue differentiation theorem, the Girsanov theorem) are stated with their exact hypotheses and are the standard results of the respective theories; the constants and the signs are as stated in the standard references.*
