---
project: genai-entry-jobs-mortgage
document: executive_summary
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 00 — Executive Summary

## 0. Scope

This package is an independent, source-verified literature review and methodological audit for the assignment *Generative AI, Entry-Level Employment, and the US Mortgage Market* (`研究任务说明.pdf`). It recommends a research design. It does **not** implement the analysis: no estimates were produced.

Three kinds of statement are kept separate:

- **`[ASSIGNMENT]`** — requirements from the assignment;
- **`[EVIDENCE]`** — findings from the literature, with a verification label and paper ID;
- **`[REC]`** — our own recommendations.

Paper IDs (P0xx) and methods IDs (M0xx) are defined in `02_evidence_matrix.md`.

**Assignment requirements that bind the design `[ASSIGNMENT]`**
- HMDA (ffiec.cfpb.gov) is the mortgage data source.
- All data are downloaded by code, and the whole replication runs with one command.
- Deliverables: an AER-style English LaTeX paper, a research plan that cites literature and motivation for every setting, the code, the GitHub history, and the AI interaction logs.
- Bonus: a two-layer plan (economic logic, then a numbered execution spec with formulas, boundary cases and acceptance counts) that another AI could reproduce from the plan alone.

## 1. Main findings

1. **The entry-level labor shock is documented but contested `[EVIDENCE]`.**
   - In ADP payroll data, employment of 22–25-year-olds in the most LLM-exposed occupations stands 19% below its "kept-pace" counterfactual as of June 2026. The adjustment runs through hiring, not layoffs or base pay (P004, FULL_TEXT_VERIFIED). The authors call this descriptive, not causal.
   - The effect is concentrated at 22–25. In P004 Table 1, Q5 vs Q1: 22–25 −0.179 (SE 0.036); 26–30 −0.048 (0.033); 31–34 −0.014 (0.030).
   - It shrinks to −0.080 (0.057) with education, rate and WFH controls, and to −0.022 [−0.055, 0.011] in the ACS (P004 §5).
   - Public QWI data show −15% employment for ages 22–24 in exposed industries (P005).
   - But deterioration began before ChatGPT (P008), coincides with the March 2022 tightening (P009), and Danish administrative data show precise null effects on earnings (P010).
2. **No study links GenAI exposure to mortgage outcomes by age** (search as of 2026-10-08; `01` §2.4 lists the coverage limits).
   - The closest competitors study *house prices*. They find that AI exposure **raises** local home values: Li & Guo 2026, FRL, county level (P035), and Seagraves & Sirmans 2026, SSRN, +3.6% ZHVI per SD across 211 metros (P036). Both are ABSTRACT_ONLY.
   - This contradicts the naive "hit regions weaken" expectation and creates a competing price channel.
3. **HMDA can support an age × local-market × year panel for 2018–2025, but only through loan-level files `[EVIDENCE: probes]`.**
   - Applicant age is public only in bins (`<25`, `25-34`, …).
   - The official Data Browser API ignores age filters.
   - The 2025 snapshot (frozen June 2, 2026; 737 MB zipped) is available.
4. **The panel has three integrity hazards.**
   - The 2020–2022 reporting-threshold episode: 2023 is the first year since 2019 in which lenders with fewer than 100 loans reported (P031 fn. 7).
   - EGRRCPA partial exemptions (`Exempt` values).
   - Connecticut switched to planning-region county codes in HMDA 2024 (our tabulation).
5. **Selection makes denial and pricing outcomes ambiguous `[REC, derived]`.**
   - Application counts are the only HMDA outcome with an unambiguous predicted sign under a labor-demand shock.
   - Screening out marginal applicants *lowers* observed denial rates even when lender standards are unchanged (`06` §3.1).
   - Public HMDA lacks credit scores, which explain most conditional denial gaps (P028).
6. **A triple difference with CZ × year fixed effects is necessary but not sufficient `[REC]`.** It absorbs age-invariant local shocks. It does **not** absorb shocks with age-specific incidence that correlate with exposure. Examples: the 2022 rate shock, which hits first-time and LMI buyers hardest (P022, P023); AI-linked price growth; the student-loan repayment restart (Oct 2023); and the FHA premium cut (Mar 2023) (`05` §4).

## 2. Most relevant literature

| Rank | ID | Why it matters |
|---|---|---|
| 1 | P004 Brynjolfsson, Chandar & Chen (2026) | Defines the affected age group, the exposure measure and the comparison logic; shows dilution beyond age 25 and weak ACS replication |
| 2 | P005 Tucker (2026, Census CES) | Public-data (QWI) template for the labor first stage and reference-quarter conventions |
| 3 | P035 Li & Guo (2026); P036 Seagraves & Sirmans (2026) | Closest competitors; AI exposure → higher house prices (channel A1) |
| 4 | P024 Barrot et al. (2022, JF) | Labor shock → HMDA applications and denials at CZ level; shows denial ≠ supply and that labor shocks can *raise* borrowing |
| 5 | P008 Frank et al. (2026); P009 Iscenko & Curto Millet (2026) | Timing and interest-rate threats |
| 6 | P022 Ringo (2026, REStat); P023 Bhutta & Ringo (2021, JME) | Rate and DTI sensitivity of first-time and lower-income buyers; HMDA sample conventions |
| 7 | P028 Bhutta, Hizmo & Ringo (2025, JF); P027 Fuster et al. (2019, RFS); P031 CFPB (2024) | HMDA processing conventions; limits of public-data denial models |
| 8 | P001 Eloundou et al. (2024, Science) | Exposure measure (GPT-4 β) |

## 3. Major research gap

Unanswered:
- whether GenAI exposure shifted the **age composition of mortgage demand** across local markets;
- whether any shift reflects a **young-worker labor channel** or an **AI-driven price and wealth channel**;
- how **applicant selection** shapes measured denial and pricing for young borrowers.

The original question is not already answered. But the labor first stage it presupposes is contested, so we recommend the narrower framing in `07` §I.1.

## 4. Recommended design

**Primary: age-differential local exposure design (D-B with D-C event studies).**
- **Unit:** 1990 commuting zone × HMDA age bin × year, 2018–2025.
- **Outcome:** home-purchase applications (first-lien, principal residence, site-built 1–4 unit, closed-end, actions 1–5).
- **Exposure:** pre-period (ACS 2015–2019) employment-weighted GPT-4 β of employed residents aged 22–34 (P001), standardized.
- **Contrast:** 25–34 vs 35–44 applicants, before (2018–2022) vs after (2023–2025).
- **Estimator:** PPML with CZ × year, age × year and CZ × age fixed effects, plus pre-period affordability and FHA-share controls interacted with young × year.
- **Inference:** state-clustered SEs.
- **Paired analyses:**
  - a QWI first stage of identical structure (A04 vs A05; A03 vs A05);
  - an auxiliary `<25` contrast and placebo `45-54` vs `35-44`;
  - an application-level selection and within-lender module;
  - a price-channel event study.
- **Estimand:** a local-market exposure effect on the age composition of mortgage demand. It is not an adoption effect, an individual effect, or a credit-supply effect.

**Fallback (DEC-D02).** Industry-based young-worker exposure (QWI shares × OEWS staffing patterns, as in P005), with a linear share-form DDD. It is triggered only by data failures (`07` §O), never by results.

## 5. Most serious identification threat

Shocks with age-specific incidence whose local intensity correlates with young-worker exposure: rate sensitivity of first-time buyers in expensive markets; AI-linked house-price growth; tech-cycle hiring freezes; the student-loan restart. These survive the CZ × year fixed effects. Mitigations are partial:
- pre-specified controls × young × year;
- pre-trends over 2018–2021, which include both a rate rise and a rate fall;
- timing and age-gradient tests;
- HonestDiD bounds.

## 6. Most serious data-feasibility concern

**No public dataset measures local employment by age and occupation after 2022.**
- QWI has age and industry but no occupation.
- OEWS has occupation but no age.
- The CPS is too thin.

So the labor first stage is place × age × industry. It may be weak at the 25–34 bin that dominates mortgage applications. Operationally:
- the ACS PUMS 2015–2019 occupation-code harmonization (F5) and the Dorn crosswalk formats (F3) must be confirmed;
- application-level regressions may exceed 16 GB of RAM (F6).

## 7. Immediate next steps

1. Run feasibility checks **F1–F8** (`07` §J) before writing analysis code. Freeze acceptance counts from the F-run; do not guess them.
2. Commit this package to the repository (requires the user's authorization; nothing has been pushed).
3. Implement `make all` in the stage order of `07` §L.
4. Estimate the pre-specified primary specification first, then the pre-specified robustness list. Report all results whatever their significance. The assignment notes reviewers' preference for significant results `[ASSIGNMENT]`; pre-specification is the credible response.

## 8. Manifest

| File | Content |
|---|---|
| `00_executive_summary.md` | This summary |
| `01_literature_review.md` | Review by stream; tools and skills used; competing findings; closest competitors |
| `02_evidence_matrix.md` | P001–P042 blocks (21 fields each); M01–M25; screened list; full bibliography |
| `03_hmda_methods_audit.md` | Verified HMDA facts, probes, paper-level practices, recommended processing decisions (DEC-H##) |
| `04_data_feasibility.md` | Dataset registry D01–D16; joint-breakdown verdicts; concordances; alignment; compute budget |
| `05_identification_designs.md` | Designs D-A to D-G with equations; age alignment; DDD absorption analysis; PPML vs logs; inference; ranking |
| `06_mechanisms_and_contribution.md` | Model; M1–M4; selection algebra; prediction matrix; alternatives A1–A8; contribution |
| `07_recommended_research_plan.md` | Part I (economics), Part II (REQ-numbered spec, validation, decision register, open items, fallback, schedule), QC audit, **Critical Weaknesses** |
