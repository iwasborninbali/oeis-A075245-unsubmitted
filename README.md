# OEIS A075245: maximum-denominator formula fails (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 14 Nov 2026).

- [A075245](https://oeis.org/A075245), conjectured formula fails at n = 409 (10 failures up to 2000): **candidate** (2026-11-13: repository built (core c5)). Certificate: partial.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

For n>=3 with a solution, consider positive integers x<y<z satisfying 4/n=1/x+1/y+1/z and maximize z; the sequence records x, with offset 3. The entry does not specify how to choose x when different maximizers tie. For numerical enumeration here, choose the least x among maximizers, matching the entry's Maple program's first-maximum rule. Existence for every n is not assumed.

The snapshot `context/A075245.seq` and live [entry](https://oeis.org/A075245), read 2026-11-13, give M. F. Hasler's July 2, 2022 conjecture: “Conjecture: a(n) = floor(n/4) + d, with d = 1 except for some n = 8k+1 (k = 6, 9, 11, 14, 20, 21, 24, 29, 30, 35, 39, ...) where d = 2 .” The live entry still states it and also reports the pattern through 2000.

## Terms / result

At n=409 the unique maximizing triple is (105,3906,7987770); its x=105 is floor(409/4)+3. Exact enumeration finds ten failures through 2000: 409, 769, 1129, 1201, 1249, 1321, 1369, 1609, 1721, 1849. The guide reported these values were already in the linked OEIS b-file; this repository has not independently retrieved that third-party file.

| n | maximizing triples |
|---:|---|
| 17 | (5,30,510), (6,15,510) |
| 73 | (20,210,30660), (21,140,30660) |
| 409 | (105,3906,7987770) |

## How it was obtained

A divisibility argument excludes both allowed x values at n=409, and a valid triple has a larger z. Exhaustive integer searches establish the displayed maxima. Full details are in [proof.md](proof.md).

## Verification

Two separately written exact searches agree at n=409 and the ties at 17 and 73. The divisor search covers n=3..2000; the direct checker covers only the three displayed indices. The proof is human-checkable, not machine-checked. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

The formula and linked table are due to Hasler; the guide reported the ten exceptions already present in the b-file. ChatGPT gave the refutation and Claude Code reviewed it. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 programs/divisor_search.py` and `python3 verification/check.py`; the former reports ten failures and the latter ends `PASS`. Both take under a few seconds on the recorded machine. Outputs are in `verification/logs/`.

## Provenance

Source `projects/science/athanor-oeis`, commit `7662d9a678c6d414685a899a631c63ac320f6840`, paths `tasks/2026-11-12-A075245-egyptian-floor-formula/answers/2026-11-12-chatgpt.md`, `context/A075245.seq`, and `TASK.md`. The guide's review is recorded in `tasks/README.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
