# Review of “Measure and Integration: From Riemann to the Present”

Verdict: The essay contains several substantive mathematical errors and misleading statements. I would not use it as teaching material in its current form. It has a strong conceptual ambition and covers many important topics, but some central theorems are misstated, certain examples are invalid as written, and several analogies are presented as if they were mathematical equivalences.

The most important issue is that the essay explicitly promises exact theorem hypotheses and verified constants, signs, and statements. The mathematical precision does not consistently meet that standard. This is more than a copy-editing problem: students could learn incorrect versions of foundational results.

I reviewed the supplied essay across its measure-theoretic, functional-analytic, topological, vector-valued, numerical, and modern-analysis sections. The findings below distinguish definite mathematical errors, incorrect or incomplete hypotheses, and pedagogical problems.

## 1. Definite mathematical errors

These are the corrections I would prioritize before distributing the essay to students.

## 1.1 The Riemann integral and null sets

§1.1–1.3, especially lines 35–53

The essay says that the Riemann integral is sensitive to changes on sets of measure zero and that this is a central defect of the integral.&#x20;

measure-integration-essay.md



This is incorrect as stated. A bounded Riemann-integrable function remains Riemann-integrable if its values are changed on a set of Lebesgue measure zero, and the integral is unchanged.

For example, the zero function and the function that equals \\(1\\) on \\(\mathbb Q\cap[0,1]\\) and \\(0\\) elsewhere differ on a null set, but the latter is not Riemann-integrable. This does not establish that the integral assigns different values to the two functions: one of those integrals does not exist.

Suggested correction: Explain that the Riemann integral is limited because some bounded functions with null sets of discontinuities excluded—more precisely, functions discontinuous on a set of positive measure—fail its integrability criterion. The Lebesgue integral extends the class of integrable functions and provides powerful convergence theorems.

## 1.2 The Baire category theorem

§1.2, line 45

The essay says that the discontinuity set of a Baire class one function is “a meagre \\(G\_\delta\\).”&#x20;

measure-integration-essay.md



The standard theorem is that the set of discontinuities of a real-valued Baire class one function on a suitable metric space is an \\(F\_\sigma\\) meagre set. The set of continuity points is a dense \\(G\_\delta\\) on a nonempty complete metric space.

Suggested correction: Distinguish the discontinuity set from the continuity set. The fat Cantor set example can still illustrate the failure of Riemann integrability of \\(\mathbf 1_C\\).

## 1.3 The \\(L^\infty\\) dual space

§4.2, lines 263–265

The essay identifies \\((L^\infty)^\*\\) with the entire space \\(ba(X,\mathcal A,\mu)\\) of bounded finitely additive measures.&#x20;

measure-integration-essay.md



This omits an important qualification. For a given measure space, the dual of \\(L^\infty(\mu)\\) corresponds to bounded finitely additive measures that are absolutely continuous with respect to \\(\mu\\), with the appropriate identification of measures that agree on \\(\mu\\)-null sets. It is not generally the entire space of finitely additive measures on \\(\mathcal A\\).

Suggested correction: State the duality using the appropriate absolutely continuous finitely additive measures, or give a standard example such as \\(L^\infty(\mathbb N)\\), whose dual can be identified with \\(ba(\mathbb N)\\).

## 1.4 The Peano kernel theorem

§7.2

The stated theorem assumes only that \\(E\\) is a linear functional on \\(C^k[a,b]\\) and annihilates polynomials of degree less than \\(k\\). It then asserts an \\(L^1\\) Peano kernel representation.&#x20;

measure-integration-essay.md



The continuity or boundedness hypothesis is missing. Polynomial exactness alone does not guarantee that a linear functional admits the asserted integral representation.

Suggested correction: Include the standard continuity hypothesis on \\(E\\), state the regularity assumptions on \\(f\\), and define the Peano kernel explicitly. Also, Gaussian quadrature's exactness through degree \\(2n-1\\) does not mean that its Peano kernel vanishes as a function; rather, the error functional annihilates those polynomials.

## 1.5 Weak convergence and the finite-element method

§7.4

The essay claims that every bounded sequence in a dual space has a weak-\* convergent subsequence by Banach–Alaoglu.&#x20;

measure-integration-essay.md



This is false in general. Banach–Alaoglu gives compactness of the dual unit ball in the weak-\* topology, not sequential compactness in arbitrary dual spaces. Compactness does not always imply sequential compactness.

For standard finite-element convergence arguments, a bounded sequence in a reflexive space such as \\(H^1\\) has a weakly convergent subsequence. That conclusion follows from reflexivity and weak compactness, not from the stated general version of Banach–Alaoglu.

Suggested correction: State the actual compactness theorem appropriate to the function space and the convergence argument being made.

## 2. Other important theorem and hypothesis problems

| Section                          | Problem                                                                                                                                                                                                                                    | Required correction                                                                                                                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| §3.1, Daniell–Stone              | The theorem claims that the extended integral applies precisely to all measurable functions for which the integral exists. This is too broad without specifying the generated \\(\sigma\\)-algebra and the precise extension construction. | State the exact version of Daniell–Stone being used, including its continuity and uniqueness hypotheses.                                                                                   |
| §3.2, linear functionals         | The discussion of idempotents as characteristic functions of points confuses point indicators with general measurable-set indicators.                                                                                                      | Explain that idempotents in a function algebra represent measurable sets when the algebra contains the corresponding indicator functions; point indicators need not belong to the algebra. |
| §4.2, Hölder's inequality        | Equality is described as linear dependence of \\(\|f\|^p\\) and \\(\|g\|^q\\) without addressing zero cases and endpoint exponents.                                                                                                        | Give the equality condition for \\(1\<p,q<\infty\\) separately from the endpoint cases.                                                                                                    |
| §4.3, reflexivity                | “\\(L^p\\) is reflexive iff \\(1\<p<\infty\\)” is presented without the usual assumptions on the measure space.                                                                                                                            | State the measure-space hypotheses and distinguish the general theorem from degenerate or exceptional cases.                                                                               |
| §5.3, Haar measure               | The modular-function formula depends on the convention used to define the modular function and the right Haar measure.                                                                                                                     | Declare the convention explicitly and verify the sign or reciprocal in the formula.                                                                                                        |
| §5.5, Kolmogorov extension       | The existence and uniqueness statement for arbitrary families of measurable spaces is insufficiently qualified.                                                                                                                            | Specify the assumptions under which the consistent family extends to a probability measure and the exact \\(\sigma\\)-algebra on which uniqueness holds.                                   |
| §6.2, Pettis integral            | The essay suggests the converse to Bochner integrability holds for separable Banach spaces. Separability alone is not sufficient.                                                                                                          | Require the appropriate strong measurability and integrability conditions; Pettis integrability alone does not imply Bochner integrability.                                                |
| §8.1, Birkhoff theorem           | Almost-everywhere convergence and \\(L^1\\) convergence are conflated.                                                                                                                                                                     | State the general almost-everywhere convergence result separately; \\(L^1\\) convergence requires additional conditions.                                                                   |
| §8.2, martingale convergence     | The theorem groups almost-sure convergence with \\(L^1\\) convergence under a uniform \\(L^1\\) bound.                                                                                                                                     | Uniform \\(L^1\\) boundedness gives almost-sure convergence under the standard martingale hypotheses, but \\(L^1\\) convergence requires uniform integrability.                            |
| §8.5, noncommutative integration | The operator trace, Dixmier trace, and normal trace are presented as though they were interchangeable examples of the same functional on a von Neumann algebra.                                                                            | Distinguish normal semifinite traces from singular traces such as Dixmier traces, which have different domains and properties.                                                             |

These are not all equally severe, but they matter in a text aimed at functional analysts. In particular, the hypotheses of a theorem are part of the theorem, not optional technical details.

## 3. Errors in examples and applications

Several examples are useful in principle but are not valid demonstrations of the claims made around them.

3.1 Monte Carlo convergence rates — §7.3

The essay states that the Monte Carlo error is \\(O(N^{-1/2})\\) and Gaussian by the central limit theorem. Neither statement holds without qualifications.

- The \\(N^{-1/2}\\) rate is a typical statistical rate, not an unconditional error bound.
- The central limit theorem requires appropriate assumptions, usually finite variance for the ordinary i.i.d. sample-mean version.
- Almost-sure weak convergence of empirical measures does not itself provide a convergence rate.

Fix: Separate the strong law of large numbers, the central limit theorem, and non-asymptotic error estimates. Explain the role of dimension and regularity when comparing Monte Carlo with deterministic quadrature.

3.2 Young measures — §6.4

The essay claims that the pushforwards \\((u_n)\_\\#\lambda\\) converge to a Young measure \\(\nu\\).&#x20;

measure-integration-essay.md



This confuses two different objects. A Young measure is generally a parameterized family \\(\nu_x\\) of probability measures. The pushforward measures describe the distribution of the values of \\(u_n\\), but do not in general capture where oscillations occur in the domain.

Fix: Distinguish the spatially parameterized Young measure from the global value-distribution measure. State the compactness, tightness, and integrability assumptions required by the particular Young-measure theorem.

3.3 Finite-element convergence — §7.4

The text suggests that weak convergence of the discrete solutions is the general outcome of finite-element discretization. This is not a universal description of FEM convergence.

Depending on the problem, one may prove weak convergence, strong convergence in an energy norm, \\(L^2\\) convergence, or other estimates. The result depends on coercivity, stability, approximation properties, mesh assumptions, and regularity.

Fix: Present one clearly specified variational problem and prove or cite its convergence theorem, rather than suggesting one generic argument covers FEM.

3.4 The Lebesgue differentiation theorem — §8.2

The essay's basic theorem is sound for \\(f\in L^1\_{\mathrm{loc}}(\mathbb R^n)\\). However, its explanatory language says the Lebesgue integral is “differentiable,” which can mislead students.

Fix: Say that local averages of \\(f\\) converge to \\(f(x)\\) at almost every Lebesgue point. This is a differentiation theorem for averages, not a claim that the integral operator itself is differentiable.

3.5 Metric Sobolev spaces — §8.4

The essay states that several definitions of metric Sobolev spaces coincide on doubling spaces. This is too broad: the equivalence of different definitions generally depends on the precise definitions, assumptions on the measure, and often a Poincaré inequality.

Fix: Name the spaces precisely and state the hypotheses of the equivalence theorem. Do not present doubling alone as sufficient for every equivalence and embedding claimed.

## 4. Conceptual claims that should not be taught as theorems

The essay repeatedly uses the phrase “the integral is the primitive object, and the measure is its shadow.” This is an effective philosophical theme, but it is not a universally valid mathematical conclusion.

The Daniell–Stone construction can recover a measure from a suitably regular positive linear functional. The Riesz–Markov–Kakutani theorem represents continuous linear functionals on \\(C_0(X)\\) by appropriate Radon measures. But these are representation theorems with specific domains and hypotheses, not proof that integration must always be the primitive object.

Three particular claims need revision:

- “The measure is not primitive.” Measure theory can begin with a measure and construct the integral. The Daniell construction offers an alternative starting point, not a refutation of the measure-first construction.
- “The measure is the state space of the algebra.” For a unital commutative \\(C^\*\\)-algebra, states correspond to probability measures on its compact spectrum. The full dual includes much more than states; in the non-unital case, the formulation also requires care.
- “The Radon–Nikodym theorem is the measure-theoretic analogue of the fundamental theorem of calculus.” This is a useful analogy, but it is not an equivalence. The Radon–Nikodym theorem represents absolutely continuous measures using densities, whereas the fundamental theorem of calculus relates derivatives and integrals under particular analytic hypotheses.

The same caution applies to the essay's comparisons between the Jordan and spectral decompositions, Gaussian quadrature and Rayleigh–Ritz, and the Banach–Tarski paradox and finitely additive functionals. These comparisons can be insightful, but each needs a clearly identified scope and a statement of what the analogy does not imply.

## 5. Additional corrections needed for advanced teaching

The following issues are particularly important if the intended audience includes graduate students.

| Location                     | Issue                                                                                                                                                                                                              | Recommended change                                                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| §1.2, Volterra function      | The construction is described too loosely to establish the claimed properties. A uniform limit of smooth bump functions does not, by itself, guarantee all the stated differentiability and derivative properties. | Supply a rigorous construction or cite a source that establishes the existence of the required function.                                                                  |
| §2.3, Lebesgue integral      | The definition for general signed functions is imprecise. If both \\(\int f^+\\) and \\(\int f^-\\) are infinite, their difference is undefined.                                                                   | Explicitly distinguish nonnegative extended integrals, integrable signed functions, and extended integrals with a defined value.                                          |
| §3.4, Radon–Nikodym property | The definition of the Banach-space Radon–Nikodym property omits absolute continuity of the vector measure with respect to the scalar reference measure.                                                            | State that the relevant vector measure must be absolutely continuous with respect to the reference measure, in addition to the appropriate bounded-variation assumptions. |
| §4.1, \\(L^p\\) completeness | The proof sketch needs more care around the subsequence converging almost everywhere and the use of Fatou's lemma.                                                                                                 | Give the standard subsequence argument and distinguish convergence almost everywhere from convergence in \\(L^p\\).                                                       |
| §5.4, Banach–Tarski          | The explanation that pieces can be reassembled because they lack measurable volumes is broadly right, but it risks suggesting that nonmeasurability alone causes the paradox.                                      | Explain the role of the group action, paradoxical decomposition, and the axiom of choice.                                                                                 |
| §6.3, Nikodým boundedness    | The vector-valued theorem and its proof sketch are compressed enough to conceal significant hypotheses and distinctions.                                                                                           | State the scalar theorem and the vector-measure version separately, with their precise assumptions.                                                                       |
| §6.4, weak PDE formulations  | Distributional derivatives are described as though integration were necessarily vector-valued integration. Distribution theory and Bochner/Pettis integration are distinct frameworks.                             | Separate distributional integration by parts, vector measures, and Banach-space-valued integration.                                                                       |
| §8.6, Girsanov theorem       | The density and drift signs are consistent with one common convention, but the theorem omits the filtration, integrability, and measure-change details needed for a complete statement.                            | State the stochastic basis, adaptedness conditions, Novikov condition, and the resulting Brownian motion under the new measure explicitly.                                |

## 6. Pedagogical problems

Even after correcting the mathematics, I would revise the presentation before using this as a teaching text.

First, the scope is too broad. The essay moves from elementary Riemann sums to the Radon–Nikodym property, noncommutative \\(L^p\\) spaces, RCD spaces, stochastic calculus, and descriptive set theory. These topics require substantially different prerequisites. A reader who has just learned measure theory is unlikely to benefit from seeing them all treated at similar levels of compression.

Second, the same central metaphor is repeated excessively. Phrases such as “the measure is the dual object,” “the linear-algebraic content,” and “the measure connects the topology to the geometry” recur throughout. The repetition crowds out proofs, counterexamples, and explanations of why each hypothesis matters.

Third, the text often asserts results where it should demonstrate them. Examples include the moment problem, vector-valued integration, Young measures, and finite-element convergence. These are not topics where a paragraph of analogies can substitute for a precise theorem and an illustrative calculation.

Fourth, the references are not sufficient to support the stated level of verification. The bibliography contains useful standard works, but several historical entries lack complete publication details. More importantly, a bibliography does not establish that every theorem has been stated correctly. The manuscript should link technical claims to the precise theorem or section in a reliable reference.

## 7. Recommended revision plan

I would revise the essay in this order:

1. Correct the mathematical statements first. Fix the null-set discussion, Baire category terminology, \\(L^\infty\\) duality, Peano kernel hypotheses, compactness arguments, and convergence theorem statements.
2. Audit every theorem independently. For each theorem, list the assumptions, conclusion, relevant function spaces, and any exceptional cases. Verify these against a standard reference such as Rudin's Real and Complex Analysis or Bogachev's Measure Theory, as appropriate.
3. Separate established results from analogies. Keep the unifying conceptual theme, but label interpretive comparisons explicitly and avoid treating them as equivalences.
4. Reorganize by prerequisite level. Build a core text around Riemann integration, Lebesgue measure and integration, convergence theorems, \\(L^p\\) spaces, and representation theorems. Move advanced applications into optional chapters or appendices.
5. Add worked examples and exercises. Include explicit proofs of representative results, counterexamples illustrating failed hypotheses, and exercises that test whether students understand the differences between pointwise, almost-everywhere, norm, weak, and weak-\* convergence.
6. Recheck the final manuscript after editing. In particular, verify all equations, historical attributions, cross-references, and bibliography entries. A corrected individual paragraph does not guarantee that its later applications remain consistent.

## Final assessment

The essay is a promising conceptual survey, but it is not yet reliable enough to serve as authoritative teaching material. Its strongest feature is the attempt to connect integration, measure theory, functional analysis, topology, and numerical analysis. Its main weakness is the gap between the confidence of its mathematical assertions and the precision with which those assertions are stated.

I recommend retaining the broad conceptual structure while substantially revising the theorem statements, examples, and applications. The most serious errors should be corrected before students encounter the text; stylistic improvements can follow.

I can also produce a line-by-line correction report for the entire manuscript, with corrected theorem statements, replacement passages, and a severity rating for every identified issue.