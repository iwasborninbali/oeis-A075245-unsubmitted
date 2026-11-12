# Verification certificate

## Claim

At n=409 the unique maximum-z solution is (105,3906,7987770), contradicting the stated formula.

With least-x tie-breaking, there are ten formula failures in 3<=n<=2000, listed in the README.

At n=17 and n=73 the maximum z has solutions with different x.

## Evidence

| What | Program | Author and date | Coverage | Result |
|---|---|---|---|---|
| Human-checkable proof | `proof.md` | Adapted by OpenAI Codex from ChatGPT, 2026-11-12 | Formula refutation at 409; search bounds | Not machine-checked |
| Producer | `programs/divisor_search.py` | OpenAI Codex, 2026-11-13 | 3..2000 via divisors | Ten failures |
| Independent check | `verification/check.py` | OpenAI Codex, 2026-11-13 | Direct x,y search at 17,73,409 | Passed |

The two programs were separately written and share no code or tables; they share mathematical definitions and finite bounds. Guide review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6: `python3 programs/divisor_search.py` produced the ten indices and unique 409 winner; `python3 verification/check.py` produced the displayed winners and `PASS`. Full outputs in `verification/logs/`.

## Not covered

The ten-index count has not been separately recomputed over the entire range here. The source review reports that the guide checked the published b-file; this repository did not retrieve it. The proof is not formally machine-checked. A tie convention requires editorial decision; existence for all n is not proved.

## Guide's independent check

pending

## Verdict

partial — the central counterexample and ties were independently replayed, but the full 3..2000 count has only one replayed search.
