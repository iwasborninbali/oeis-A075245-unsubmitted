# Independent verification: 2026-11-15

Reference: supplied repository archive, commit f0fae5fccd471ffd2578a460fa1b40c7086e46a5. This review is independent of the producer and certificate authors.

## Claim

For positive integers x<y<z solving 4/n=1/x+1/y+1/z, the unique maximum-z triple at n=409 is (105,3906,7987770), refuting the OEIS conjecture; using least-x tie-breaking exactly ten n in 3..2000 violate it (409,769,1129,1201,1249,1321,1369,1609,1721,1849); at n=17 and 73 the maximum z is attained at distinct x values.

## Proof check

**Proof verdict: correct with fixable explanatory gaps.** Line-by-line assessment of proof.md:

- **Lines 3-5:** The strict inequalities n/4<x<3n/4 follow from x<y<z and positivity. With A=4x-n and B=nx, the identity (Ay-B)(Az-B)=B^2 follows on clearing denominators. Correct. The assertion that the conjecture allows only x=103 or 104 at n=409 uses its implicit d in {1,2}; cite the precise conjecture. **Fixable, not fatal.**
- **Line 7:** d=Ay-B=By/z gives 0<d<B, d divides B^2 and d=-B modulo A. Also z=B/A+B^2/(A*d) strictly decreases as d increases. Correct. **Omitted sufficiency condition:** divisor/congruence tests alone do not ensure integer z. For n=6,x=3,y=5, A=6,B=18,d=12 divides B^2 and satisfies d=-B mod A and 0<d<B, but z=15/2. Explicitly check A divides B+B^2/d, equivalently z is integral. The repository code actually checks this. **Fixable, not fatal.**
- **Line 9:** 103 and 409 are primes, each 1 modulo 3; hence divisors of B^2 are 1 modulo 3, whereas d must be 2 modulo 3. Correct. Primality is asserted without showing elementary trial division. **Fixable, not fatal.**
- **Line 11:** B=42536=2^3*13*409; x=104 gives A=7 and d=3 mod 7. The positive values d<52 are 3,10,17,24,31,38,45, none dividing B^2. d=52 gives (y,z)=(6084,4976712), with proper integrality and ordering. Monotonicity makes it optimal for this x. Correct; show the factorization/substitution if expanding the proof. **Expository only.**
- **Line 13:** (105,3906,7987770) is an exact ordered solution whose z exceeds the best for x=104, and x=103 is impossible. This rigorously **refutes the conjecture without assuming that the witness is globally maximal**. Correct. The witness alone does **not** establish uniqueness of the global maximum. **Computational check needed for uniqueness, not a gap in the refutation.**
- **Line 15:** The finite x,y search intervals are correct. z=B*y/(A*y-B) decreases strictly with y; the divisor search's upper bound B(B+1)/A follows from d>=1. Strict comparison is needed to retain ties, as implemented. The first valid d is optimal only for that fixed x, as intended. **The uniqueness, ties, and exact ten-index count depend on correct exhaustive code, not on the preceding human algebra.** The repository independent check covered only 17,73,409; our independent full-range scan below closes this coverage gap for n<=2000. **Fixable and now independently checked.**
- **Definition/scope:** Least-x selection among maximum-z ties is an editorial convention, not fixed by the OEIS wording. Only finite-range existence is checked; the general Erdos-Straus existence conjecture is not used. **Not fatal.**

No substantive algebraic error or unproved conjectural premise was found in the finite refutation.

## Independent computation

New program: [independent_scan.py](independent_scan.py); log: [output.log](output.log). No factorization, divisor enumeration, original source code, or original result tables were used. It enumerates x strictly between n/4 and 3n/4, and integer y in the exact interval max(x+1,floor(B/A)+1)..floor((2B-1)/A). It tests integer z=B*y/(A*y-B) and z>y by integer division. Since z(y) is strictly decreasing, it abandons remaining y (or an entire x) only if their best possible z is **strictly** smaller than the incumbent; this preserves ties. Every winner is independently checked with exact rational fractions. At n=17,73,409, separate unpruned x,y searches were run.

Run: python3 verification/agent-2026-11-15/independent_scan.py --end 5000

- Range: **3..5000** (larger than the original 3-index independent check and 3..2000 producer).
- 3..2000: **exactly 10 failures**, with (n,x): (409,105), (769,196), (1129,286), (1201,306), (1249,315), (1321,336), (1369,352), (1609,408), (1721,435), (1849,468).
- 2001..5000: **18 more failures** at n=2041,2089,2161,2449,2521,2641,2689,2801,3001,3049,3169,3721,3889,4201,4489,4561,4729,4801; **28 total** through 5000. This extension is outside the stated ten-index count.
- At n=409, the **unique maximum** is (105,3906,7987770). Unpruned search tested 79377 y candidates and checked the same winner.
- Exactly two ties at n<=2000: 17 has (5,30,510) and (6,15,510); 73 has (20,210,30660) and (21,140,30660). Another tie by 5000 occurs at 2521 with (636,69748,131876031) and (658,14946,131876031).
- 55,453,365 candidate y values tested; 6,247,500 x intervals; observed elapsed **9.973019 seconds** (Python 3, perf_counter, same run as output.log); STATUS=PASS.
- SHA-256 of independent_scan.py: **296e151c73fae9782e3dddc3125a0d4ef527c9ccd1f30ff55bde692102a7f2bd**.
- SHA-256 of output.log: **3dc546153ac5fd962029a84988e51e6de29726abd89a053d5e5facb6a4d772a0**.

This computes no infinite classification and proves no existence for all n.

## Prior art

- [OEIS A075245](https://oeis.org/A075245) and its [internal format](https://oeis.org/A075245/internal) retain M. F. Hasler's **July 2, 2022 conjecture** and advertise [Hasler's table of x-coordinates for n=3..2000](https://oeis.org/A075245/b075245.txt). **The table itself returned HTTP 403**: individual entries at 409 and the ten indices were *not* read. The [OEIS history](https://oeis.org/history?seq=A075245) likewise returned HTTP 403; revision timing was not independently established. Internal format shows revision #31 and Sep 10 2025 metadata, but this is not an adequate history check. The repository's assertion that the b-file already includes the exceptional values remains unverified here.
- [OEIS A075246](https://oeis.org/A075246) and [A075247](https://oeis.org/A075247) tabulate the corresponding y and maximal z; [A073101](https://oeis.org/A073101) counts representations; [A192787](https://oeis.org/A192787) covers a related ordering convention.
- [OEIS A257843](https://oeis.org/A257843) **already lists 409, 769, 1129, 1249, 1321, 1369, 1609, 1721** among inputs where lexicographically earliest and maximal-z decompositions differ; [A257839](https://oeis.org/A257839) defines the lexicographically first x. A257843 is credited to Hasler (May 2015) but individual terms cannot be securely dated without history. This is earlier relevant tabulation, **not itself an explicit proof of the formula's failure**.
- OEIS links [Erdos Problems, problem 242](https://www.erdosproblems.com/242), on the broader existence question, distinct from maximizing z. [MathOverflow: relative size of Egyptian denominators](https://mathoverflow.net/questions/142991/relative-size-of-egyptian-fraction-denominators) and [an arXiv paper on Egyptian-fraction counts](https://arxiv.org/abs/2509.10030) are related but do not give this 409 result in the available descriptions.
- Focused searches: exact phrases "A075245" "409", "A075245" "counterexample", "4/409" "1/105" "1/3906", and combinations of A075245, Erdos-Straus, largest z / maximal denominator on **arxiv.org, mathoverflow.net, math.stackexchange.com, zbmath.org, and journal publisher sites**. No independently published exact proof/refutation surfaced in indexed results. This is not a proof of absence; direct zbMATH/journal catalog and OEIS-history searches remain incomplete.

**Novelty: not established.** An older OEIS table of this precise coordinate and an older related-index sequence make a novelty claim especially unsafe. Direct inspection and dating of the table and a broader scholarly-priority audit would be needed.

## Verdict

**PARTIAL overall (archival/novelty uncertainty, not mathematical failure).** Every **finite** assertion in the certificate is independently confirmed by a distinct exact method through n=5000, and the counterexample proof is valid subject to the fixable clarifications above. Missing: direct verification of the published OEIS b-file's contents and its dated revision history, and an exhaustive literature priority check. Do **not** claim the numerical exceptions as new on this evidence. The open general existence problem is explicitly out of scope.
