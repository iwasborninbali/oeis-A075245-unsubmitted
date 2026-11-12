# Refutation and exhaustive-search bounds

For n=409, x>n/4 since 1/x<4/n. The conjecture permits x=103 or 104. Put A=4x-n and B=nx. Clearing denominators gives

    (Ay-B)(Az-B)=B².

For a valid triple let d=Ay-B. Both factors are positive, d divides B², d≡-B (mod A), and y<z implies 0<d<B. Also y=(B+d)/A and z=B(B+d)/(A d), strictly decreasing in d for fixed x.

For x=103, A=3 and B=42127=103·409. Both factors are primes congruent to 1 modulo 3; hence every divisor d of B² is 1 modulo 3. But d≡-B≡2 modulo 3, impossible.

For x=104, A=7 and B=42536=2³·13·409. We require d≡3 modulo 7. The positive candidates below 52 are 3,10,17,24,31,38,45; none divides B², since its only prime factors are 2, 13, and 409. At d=52, y=6084 and z=4976712, giving a valid triple. Since z decreases in d, this is the maximum with x=104.

For x=105, the triple (105,3906,7987770) satisfies 4/409=1/105+1/3906+1/7987770 and 105<3906<7987770, as can be checked by clearing denominators. Its z exceeds 4976712. Thus neither permitted x can occur in a global maximizing triple, refuting the conjecture independently of the search.

The exact search additionally establishes that this is the unique maximizing triple at 409. The search is exhaustive: x>n/4 and 4/n<3/x give x<3n/4. For each x, A,B>0, and positivity plus y<z imply B/A<y<2B/A, with y>x. The direct checker enumerates these finite integer intervals and tests whether z=By/(Ay-B) is integral and exceeds y. The divisor search enumerates divisors d of B², applies the congruence and ordering tests, and uses z=B(B+d)/(Ad); once a valid d is reached, larger d cannot improve it. Its skipped x satisfy B(B+1)/A<the best z already found, an upper bound since d>=1. These arguments are human-checkable, not formally machine-checked.
