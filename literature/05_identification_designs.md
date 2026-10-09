---
project: genai-entry-jobs-mortgage
document: identification_designs
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 05 — Identification Strategy Comparison

## 0. Scope

This document formalizes and compares seven candidate designs (D-A to D-G), using common notation. For each design it states the estimand, the estimating equation, the identifying assumptions and the diagnostics. It also treats four cross-cutting problems:

- age-group alignment (§3);
- what a triple difference with CZ × year fixed effects does and does not absorb (§4);
- PPML vs log-linear count models (§5);
- cell sizes (§6), inference (§7) and multiple testing (§8).

Data facts are documented in `04_data_feasibility.md`; HMDA processing rules in `03_hmda_methods_audit.md`; mechanisms in `06_mechanisms_and_contribution.md`.

Every design here is an **exposure design**. Coefficients measure how outcomes changed differentially across places with different *pre-determined* occupational exposure to LLM capabilities. They are **not** effects of AI adoption, and **not** effects on individual workers. Under the stated assumptions they are intention-to-treat-style *local-market exposure effects*. Without those assumptions they are *observational associations*. Labels used: `[ESTABLISHED: source]`, `[ADAPTED: source]`, `[NEW]`, `[INFERENCE]`.

---

## 1. Notation and common elements

| Symbol | Definition |
|---|---|
| $c$ | 1990 commuting zone (CZ) (DEC-H40) |
| $a$ | HMDA applicant-age bin: `<25`, `25-34`, `35-44`, `45-54` |
| $t$ | HMDA activity year, 2018–2025; $q$ = calendar quarter (QWI) |
| $Y_a$ | $\mathbb{1}[a=\text{25-34}]$ (primary "young" group) |
| $Y^{aux}_a$ | $\mathbb{1}[a=\text{<25}]$ (auxiliary young group) |
| $\text{Post}_t$ | $\mathbb{1}[t\ge 2023]$. ChatGPT was released on 30 Nov 2022, so 2022 is the last pre year. |
| $\beta_o$ | Eloundou et al. GPT-4 β exposure of SOC occupation $o$ (P001; D06) |
| $\omega^{g}_{co}$ | Pre-period (ACS 2015–2019) employment share of occupation $o$ among civilian employed residents of CZ $c$ in age band $g$ |
| $E^{g}_c$ | $\sum_o \omega^{g}_{co}\,\beta_o$ |
| $z_c$ | $(E^{22\text{–}34}_c-\bar E)/\mathrm{sd}(E)$, standardized across CZs in the estimation sample (unweighted). Main exposure. |
| $N_{cat}$ | HMDA home-purchase applications (actions 1–5; DEC-H20) |
| $X_c$ | Pre-determined CZ covariates (§4.3) |
| $s(c)$ | State of CZ $c$ (largest-population state for multi-state CZs) |

**Why the exposure is age-specific (22–34).** The labor-market evidence locates the shock in *young workers within exposed occupations*. For ages 22–25, the Q5-vs-Q1 long difference is −0.179 (SE 0.036); for 35–40 it is 0.001 (SE 0.031) (P004 Table 1 Panel A, p. 13). The exposure relevant to a place's young residents is therefore the occupational mix of its *young* workers, not of its whole workforce `[NEW, motivated by P004]`. The all-age measure $E^{16+}_c$ is a robustness check.

**Why 2015–2019.** It is pre-COVID and pre-ChatGPT, and the PUMS file uses a single PUMA vintage (2010) `[NEW]`. Tucker (P005) also uses ACS 2015–2019 to map occupations to industry-states `[ESTABLISHED: P005]`.

---

## 2. Candidate designs

### D-A — Geographic continuous-exposure DiD (single age group)

- **Hypothesis.** CZs with higher young-worker exposure saw relative declines in young applicants' purchase applications after 2022.
- **Unit.** CZ × year, separately for each age bin $a$.
- **Equation (PPML).**
$$
\mathbb{E}[N_{cat}\mid\cdot]=\exp\Big(\mu_{c}+\lambda_{s(c),t}+\sum_{k\neq 2022}\beta^{A}_{a,k}\,z_c\,\mathbb{1}[t=k]+\sum_{k\neq 2022}X_c'\theta_{a,k}\mathbb{1}[t=k]\Big)
$$
- **Estimand.** $\beta^A_{a,k}$ is the differential log change, relative to 2022, in age-$a$ applications per 1 SD of $z_c$, within state. Under *strong* parallel trends this is an average causal response to exposure (M01). Under ordinary parallel trends only level comparisons are identified, and differences across exposure levels mix in selection bias (M01, abstract).
- **FE.** CZ; state × year.
- **SE.** Clustered by state.
- **Identifying assumption.** Absent GenAI, age-$a$ application growth would be unrelated to $z_c$ conditional on state × year and $X_c$ × year.
- **Main biases.** Every CZ-level shock correlated with $z_c$: house-price growth in exposed places (P035, P036), rate sensitivity of high-price markets (P022, P023), tech correction (P009), remote work (P037), and AI-related wealth (P038).
- **Testable implications.** $\beta^A_{a,k}\approx 0$ for $k\le 2021$. Declines for $a\in\{\text{<25},\text{25-34}\}$ after 2022. Older groups unaffected or positive.
- **Diagnostics.** Pre-trends 2018–2021; HonestDiD bounds (M03).
- **Data.** HMDA, PUMS, crosswalks.
- **Difficulty.** Low.
- **Causal limits.** Weakest of the designs. **Role:** descriptive, and essential for the *level decomposition* of D-B (do young applications fall, or do older ones rise?).

### D-B — Age-based triple difference (PRIMARY)

- **Hypothesis.** After 2022, the young-to-prime-age ratio of purchase applications fell more in CZs with higher young-worker exposure.
- **Unit.** CZ × age ($a\in\{\text{25-34},\text{35-44}\}$) × year.
- **Equation (pooled; PPML).**
$$
\mathbb{E}[N_{cat}\mid\cdot]=\exp\Big(\beta^{B}\,z_c\,Y_a\,\text{Post}_t+\alpha_{ct}+\gamma_{at}+\delta_{ca}+\sum_{k\neq 2022}(X_c Y_a\mathbb{1}[t=k])'\theta_k\Big)
$$
- **Estimand.** $\beta^B$ is the change (post-2022 vs 2018–2022) in the log ratio of young to prime-age applications per 1 SD of $z_c$. The corresponding percentage effect on the young/old application ratio is $100(e^{\beta^B}-1)$. Under the DDD parallel-trends assumption, this is a **local-market exposure effect on the age composition of mortgage demand**. It is not the effect of AI on any individual, nor of AI adoption.
- **Exposure.** $z_c$ (§1).
- **Timing.** Post = 2023–2025. Event-study variant in D-C.
- **Outcome.** $N_{cat}$ (primary). Secondary outcomes use the same structure with OLS on cell means, weighted by $N_{cat}$ (`07` REQ-EST-04).
- **FE.** $\alpha_{ct}$ (CZ × year) absorbs every shock common to both age groups within a CZ-year. $\gamma_{at}$ (age × year) absorbs national age-specific shocks, such as the national rate path's differential effect on young buyers, national student-loan policy, and national FHA policy. $\delta_{ca}$ (CZ × age) absorbs permanent local age gaps.
- **SE.** Clustered by state (main); CZ and AKM in robustness (§7).
- **Identifying assumption (DDD parallel trends; M04).** Absent the GenAI shock, the *young–old gap* in log application growth would not depend on $z_c$, conditional on $X_c Y_a$ × year. Only this single "difference-in-trends" assumption is required, not two separate parallel-trends assumptions (M04).
- **Main biases.** Age-specific incidence of shocks correlated with $z_c$ (§4). This is the central threat.
- **Testable implications (pre-specified, see `06` §4).**
  1. Pre-trends: $\beta^B_k=0$ for $k\in\{2018,\dots,2021\}$.
  2. Age gradient: the effect for `<25` vs `35-44` is larger in absolute value than for `25-34` vs `35-44`.
  3. Placebo ages: `45-54` vs `35-44` shows no effect.
  4. Timing: the effect grows from 2023 to 2025 as affected cohorts age into the 25–34 bin.
  5. The QWI first stage (D-C) shows a relative decline of young employment/hiring in high-$z$ CZs in the same window.
- **Robustness.** See `07` REQ-ROB list.
- **Data.** HMDA (D01), PUMS (D05), Eloundou (D06), crosswalks (D13), controls (D05, D11, D12, D16).
- **Difficulty.** Medium.
- **Causal limits.** Credible only for age-specific changes *not* explained by the controlled age-specific incidence channels. Cannot isolate the labor channel from an AI-driven house-price channel (§4, `06`).

`[ADAPTED]`: the area-level HMDA demand outcomes follow P024 and P025. The age contrast parallels the experienced-worker "placebo" comparison in P004 and the triple difference of P005. Applying an age DDD to HMDA is `[NEW]`.

### D-C — Dynamic event study (for D-B, D-A, and the QWI first stage)

**Mortgage event study.**
$$
\mathbb{E}[N_{cat}\mid\cdot]=\exp\Big(\sum_{k\in\{2018,\dots,2025\}\setminus\{2022\}}\beta^{C}_k\,z_c\,Y_a\,\mathbb{1}[t=k]+\alpha_{ct}+\gamma_{at}+\delta_{ca}+\sum_{k\neq 2022}(X_c Y_a\mathbb{1}[t=k])'\theta_k\Big)
$$

**Labor first stage (QWI).** Outcomes are employment `Emp`, hires `HirA`, and earnings `EarnS`. CZ $c$, QWI age group $g\in\{\text{A04 (25–34)},\text{A05 (35–44)}\}$ (main, aligned with HMDA), plus $\{\text{A03 (22–24)}\}$ vs A05 (aligned with P004/P005); quarters 2016Q1–2025Q4:
$$
\mathbb{E}[L_{cgq}\mid\cdot]=\exp\Big(\sum_{k\neq q^*}\pi_k\,z_c\,Y_g\,\mathbb{1}[q=k]+\alpha_{cq}+\gamma_{gq}+\delta_{cg}\Big)
$$
The reference quarter is $q^*=$ 2022Q4 for beginning-of-quarter stocks (`Emp`) and 2022Q3 for within-quarter flows (`HirA`). This follows Tucker's convention `[ESTABLISHED: P005]`. Earnings use OLS on $\ln$ `EarnS`, weighted by `EmpS`.

- **Purpose.** Pre-trend diagnostics, dynamic shape, and the existence and timing of the labor channel.
- **Diagnostics.** Joint Wald test of pre-period coefficients. Rambachan–Roth relative-magnitude bounds with $\bar M\in\{0.5,1,2\}$ (M03). Visual check for the early-2022 break documented by P008 and P009. A break that starts in 2022Q1–Q2 (before ChatGPT) is evidence for the rates/tech explanation.
- **Caveat.** Pre-tests have low power and conditioning on passing them distorts inference (M02; M03). The plan reports bounds regardless of the pre-test outcome.
- **Difficulty.** Low once D-B is built.

### D-D — Industry shift-share exposure (alternative exposure; fallback)

- **Exposure.**
$$
E^{IND}_c=\sum_i s^{Y,2019}_{ci}\,X_i,\qquad X_i=\sum_o e_{io}\,\beta_o
$$
$s^{Y,2019}_{ci}$ is the 2019 QWI employment share of NAICS industry $i$ (sector or 3-digit) among workers aged 22–34 (A03 + A04) working in CZ $c$. $e_{io}$ is the OEWS May 2022 national staffing pattern (D10). Then standardize to $z^{IND}_c$.
- **Equation.** As D-B/D-C with $z^{IND}_c$ in place of $z_c$.
- **Estimand.** As D-B, but exposure reflects the *industry* mix of young local jobs.
- **Identification.** Shift-share logic.
  - Exogenous *shares* (GPSS, M05): the young-worker industry mix would be as good as random with respect to differential trends. This is implausible, because finance, information and professional services are rate-sensitive (P009).
  - Or exogenous *shifts* (BHJ, M06): industry exposures $X_i$ as-good-as-randomly assigned across industries. This is also implausible, for the same reason.
- **So D-D is not more credible than D-B.** Its value is (i) workplace-based exposure consistent with the QWI first stage and with P005; (ii) established exposure-robust inference (M07); (iii) Rotemberg-weight diagnostics (M05) that show *which industries* drive identification.
- **SE.** AKM with industry-level shocks (M07); state clusters.
- **Difficulty.** Medium (OEWS Excel parsing; NAICS aggregation).
- **Known cost.** Crosswalking occupations to industries loses most of the variance. In P005's appendix, the variance falls from about 0.045 (ACS person level) to about 0.015 (industry-state level).

### D-E — IV / "Wald scaling" of mortgage effects by labor effects (REJECTED as causal)

$$
\Delta\ln\!\frac{N_{cY}}{N_{cO}}=\theta\,\Delta\ln\!\frac{L_{cY}}{L_{cO}}+X_c'\phi+\mu_{s(c)}+u_c,\qquad \text{instrument: } z_c
$$

$\hat\theta=\hat\beta^B/\hat\pi$ would be the elasticity of young-relative mortgage demand to young-relative employment. **The exclusion restriction fails on current evidence.** Exposure also moves mortgage demand through house prices (P035, P036), firm-value and wealth effects (P038), and expectations without employment change (mechanism M2 in `06`). **Decision: REJECTED** as a causal design. The ratio $\hat\beta^B/\hat\pi$ may be reported **only** as a descriptive scaling ("mortgage response per unit of first-stage response"), explicitly labelled non-causal.

### D-F — Application-level conditional outcomes and within-lender DDD (MECHANISM MODULE)

For application $i$ (actions 1–3) by an applicant of age $a$ in CZ $c$, lender $\ell$, year $t$:
$$
\text{Denied}_i=\beta^{F}z_cY_a\text{Post}_t+\alpha_{ct}+\gamma_{at}+\delta_{ca}+\lambda_{\ell t}+W_i'\phi+\varepsilon_i
$$

- $W_i$: bins of income, DTI (public bins), CLTV, loan amount; loan type; co-applicant indicator.
- **Three variants.**
  - (F1) no $W_i$ and no $\lambda_{\ell t}$: the unconditional change, which includes composition.
  - (F2) with $W_i$ and $\lambda_{\ell t}$.
  - (F3) adds $\lambda_{\ell ct}$ (lender × CZ × year): young vs old applicants *at the same lender in the same market-year*.
- **Same structure for** rate spread among originations (DEC-H32) and for denial-reason indicators (DEC-H33).
- **Estimand.** The differential change in denial probability for young applicants in high-exposure CZs, *conditional on public-HMDA observables*. It is **not** a credit-supply effect: credit scores are unobserved, and P028 shows unobserved risk factors matter (P028 abstract).
- `[ADAPTED: P027 (LPM, lender FE), P028 (actions 1–3, risk bins, clustering)]`.
- **SE.** State clusters (main); two-way lender and CZ (adapted from P028's lender × county).
- **Difficulty.** Medium–high (memory, F6).

### D-G — Long-difference cross-section (FALLBACK-LITE; transparency check)

$$
\Delta_c\equiv\Big[\ln N_{cY}-\ln N_{cO}\Big]_{2023\text{–}25}-\Big[\ln N_{cY}-\ln N_{cO}\Big]_{2018\text{–}19}=b\,z_c+X_c'g+\mu_{s(c)}+e_c
$$

Weights are 2018–2019 total applications; SE clustered by state. This is the two-period, linear analogue of D-B (one observation per CZ), and it mirrors P024's CZ long differences `[ESTABLISHED: P024]`. It is robust to PPML convergence issues and is easy for a reader to replicate. 2020–2022 are excluded from the baseline to avoid the pandemic boom.

---

## 3. Age-group alignment (treatment and comparison groups)

### 3.1 Verified age categories

| Source | Age categories | Provenance |
|---|---|---|
| HMDA public LAR (2018–2025) | `<25`, `25-34`, `35-44`, `45-54`, `55-64`, `65-74`, `>74`, `8888` (n/a); exact age is collected but binned for privacy | `[DOC]` FIG 2024 field 55; LAR data-field page |
| QWI | 14–18, 19–21, **22–24**, **25–34**, 35–44, 45–54, 55–64, 65–99 | `[DOC]` LEHD `label_agegrp.csv` |
| PEP county | 5-year bands, plus 18–24 | `[SCHEMA]` V2025 header |
| ACS PUMS | Single years (`AGEP`) | `[SCHEMA]` |
| Canaries (P004) | 22–25, 26–30, 31–34, 35–40, 41–49, 50+ | P004 Table 1 |

### 3.2 Is 25–34 an adequate proxy for early-career exposure?

**Only partially.** In P004 Table 1 Panel A (Q5 vs Q1, Nov 2022 → Jun 2026):

| Ages | Coefficient (SE) |
|---|---|
| 22–25 | −0.179 (0.036) |
| 26–30 | −0.048 (0.033) |
| 31–34 | −0.014 (0.030) |
| 35–40 | 0.001 (0.031) |

So most of HMDA's 25–34 bin is, on current evidence, weakly affected. The HMDA 25–34 contrast is therefore a **diluted** measure of the labor shock `[INFERENCE from P004]`. Two features soften this.

1. **Cohort accumulation.** Workers aged 22–24 in 2023 are 24–26 in 2025. Affected entry cohorts move into the 25–34 bin over the post period, so the HMDA 25–34 effect should *grow* over 2023–2025 (a testable prediction).
2. **Expectations (M2 in `06`).** Workers aged 25–34 in exposed occupations may revise expected earnings and earnings risk even without current job loss. This cannot be directly verified with HMDA.

### 3.3 Is under-25 informative despite low participation?

**Yes, as an auxiliary test.** It is the bin where the labor shock is concentrated (QWI A03 ⊂ HMDA `<25`). The Kent County probe shows `<25` is about 6.8% of purchase applications (263/3,862), so CZ aggregation is required.

There is a selection caveat: under-25 applicants are a selected group, and unobserved family wealth support is likely `[INFERENCE]`. The prediction is a **larger proportional decline** for `<25` than for `25-34` (age gradient). A reversed gradient would count against the labor channel.

### 3.4 Comparison group: 35–44 or 45–54?

- **35–44 (primary).** This group is the closest in life-cycle housing behaviour: first-time and early move-up buyers, similar product mix (FHA usage) `[INFERENCE]`. In P004, workers aged 35–40 (0.001) and 41–49 (0.031) show no relative employment decline in exposed occupations.
- **45–54 (robustness).** Further in life cycle and wealth; more move-up and lock-in exposure (P039). It is also more likely to benefit from AI complementarity and equity wealth (P004 Fact 5; P038).
- **Both comparison groups are themselves exposed to AI**, in the sense of working in exposed occupations. The evidence (P004) suggests their *employment* was not reduced, and complementarity may *raise* their labor income. A positive effect on the comparison group biases $\beta^B$ toward a more negative value. Therefore D-A level estimates by age must be reported alongside D-B.

### 3.5 Cohort vs life-cycle effects

$\delta_{ca}$ absorbs permanent local age gaps (life-cycle differences). $\gamma_{at}$ absorbs national cohort shifts in each bin. Remaining cohort composition differences *across CZs* that interact with time are not absorbed: for example, CZs with growing in-migration of young graduates. Mitigation: X5 (teleworkability), PEP-population offsets (REQ-ROB-11), and the 2018–2021 pre-trends.

### 3.6 Alternatives that reduce the labor–mortgage population mismatch

1. Use the **QWI 25–34 group as the first stage for the HMDA 25–34 outcome** (same bin), in addition to 22–24 (literature-aligned).
2. **Age-specific exposure** $E^{22\text{–}34}_c$ rather than all-age exposure.
3. **Optional residence-based first stage** from ACS 1-year PUMS 2018–2024 (employment rate and wages of residents aged 25–34 by CZ), deferred (D05 note).
4. **Not feasible:** individual linkage of mortgage applicants to occupation (HMDA has none).

### 3.7 Recommendation

| Role | Specification | Status |
|---|---|---|
| Primary | Young = `25-34`, comparison = `35-44`; first stage QWI A04 vs A05 | DECIDED |
| Auxiliary young | `<25` vs `35-44`; first stage QWI A03 vs A05 | DECIDED |
| Alternative comparison | `45-54` | DECIDED (robustness) |
| Placebo | `45-54` vs `35-44` | DECIDED |

---

## 4. What does the triple difference with CZ × year FE absorb?

### 4.1 Formal decomposition

Suppose the true conditional mean is
$$
\ln\mathbb{E}[N_{cat}]=\alpha_{ct}+\gamma_{at}+\delta_{ca}+\beta\,z_cY_a\text{Post}_t+\sum_{j}h_{jc}\,\kappa_{jat},
$$
where $h_{jc}$ is CZ $c$'s exposure to a common shock $j$ and $\kappa_{jat}$ is its time path, which may differ by age. Write $\kappa_{jat}=\bar\kappa_{jt}+\tilde\kappa_{jat}$, where $\bar\kappa_{jt}$ is the age-invariant part.

- $\alpha_{ct}$ absorbs $h_{jc}\bar\kappa_{jt}$ for **all** $j$.
- $\gamma_{at}$ absorbs the *national* component of $\tilde\kappa_{jat}$.

What remains is $h_{jc}\tilde\kappa_{jat}$ (de-meaned), so in the two-period, two-age case:
$$
\operatorname{plim}\hat\beta-\beta=\sum_j\frac{\operatorname{Cov}(z_c,h_{jc}\mid X_c)}{\operatorname{Var}(z_c\mid X_c)}\Big[(\tilde\kappa_{jY,\text{post}}-\tilde\kappa_{jO,\text{post}})-(\tilde\kappa_{jY,\text{pre}}-\tilde\kappa_{jO,\text{pre}})\Big].
$$

**Conclusion.** The DDD removes bias from any shock with (i) **age-invariant incidence**, or (ii) local intensity **uncorrelated with exposure** given $X_c$. It does **not** remove bias from shocks that are common but hit young and old buyers differently in places where the shock is stronger, when those places are also high-exposure. A shock to *local house prices* is the canonical example. It is age-neutral as a price change, but its *incidence* on applications is age-specific, because first-time buyers face down-payment and DTI constraints (P017, P023). So $\alpha_{ct}$ absorbs the price change but not its differential effect on young applications. `[INFERENCE, derived]`

### 4.2 Confounder assessment

| # | Shock $j$ | Local intensity $h_{jc}$ | Correlated with $z_c$? | Age-specific incidence $\tilde\kappa$? | Absorbed by $\alpha_{ct}$? | Mitigation in the plan |
|---|---|---|---|---|---|---|
| 1 | AI-related local house-price growth | price growth | **Yes, positive**: P035 (county), P036 (metro, +3.6% ZHVI per SD) | **Yes**: constrained first-time buyers (P017, P023) | Only the age-invariant part | Pre-period price-to-income × $Y$ × year (X1). FHFA HPI event study on $z_c$ (mechanism). Level decomposition by age (D-A). Mediation framed as a channel, not a control. |
| 2 | 2022–23 mortgage-rate shock | affordability (price-to-income), FHA reliance | Likely positive with affordability `[INFERENCE]`. Exposed occupations concentrate in rate-sensitive sectors (P009). | **Yes**: LMI and first-time buyers more rate-sensitive (P022 abstract); DTI constraints bind (P023) | No | X1, X2 (pre-period FHA share among 25–34 applicants) × $Y$ × year. Pre-period event study covering the 2020–21 rate *decline* (a "reverse" episode). |
| 3 | Tech-sector correction 2022–23 | tech employment share | **Strong positive** | Plausibly: junior hiring freezes (P009) | No | X4 (young tech share) × $Y$ × year. Exclude top tech CZs. Exposure excluding computer occupations (as in P004 robustness). |
| 4 | Federal student-loan repayment restart (interest from 1 Sept 2023; payments due Oct 2023) | young college share | **Positive** (exposure ↔ college; P004 attenuation with college share) | **Yes** (young borrowers' DTI) | No | X3 (college share 22–34) × $Y$ × year. Read DTI outcomes with care. |
| 5 | FHA annual MIP cut, 0.85% → 0.55% for most borrowers, endorsements from 20 Mar 2023 (HUD ML 2023-05) | FHA reliance | Likely negative `[INFERENCE]` | **Yes** ("about eight-in-ten FHA loans going to first-time homebuyers" in 2014; P023 FEDS p. 4) | No | X2 × $Y$ × year. Split conventional vs FHA outcomes. |
| 6 | Remote work and young migration | teleworkability | Positive (both white-collar) | **Yes** (the young are more mobile) | No | X5 × $Y$ × year. PEP offsets. P037 shows remote work raised house prices 2019–2023. |
| 7 | Mortgage-rate lock-in (fewer listings, fewer move-up buyers) | share of low-rate mortgagors | Unknown | **Yes**, mainly older move-up buyers (P039; Liebersohn–Rothstein) | No | Biases young *share* upward. Report levels; 45–54 comparison. |
| 8 | AI equity/wealth gains for incumbents | high-income, equity-holding residents | Positive (P038) | **Yes**: older and wealthier buyers | No | Level decomposition. Interpret as part of the total AI exposure effect but **not** the labor channel. |
| 9 | HMDA reporting-threshold episode (2020–22; P031) | small-lender market share | Likely negative `[INFERENCE]` | Possibly | Partly | Consistent-reporter sample (DEC-H52) |
| 10 | 2020–21 pandemic housing boom | remote-work amenability | Positive | Yes | No | Alternative baselines: 2018–19 only; 2022 only |

**Overall assessment.** The DDD is **necessary but not sufficient**. The most important threats (rows 1–4) are exactly of the "age-specific incidence" type that CZ × year FE cannot absorb. Credibility therefore rests on:

- (a) explicit $X_c\times Y_a\times$year controls for the leading channels;
- (b) pre-trends over 2018–2021, which include both a rate *increase* (2018) and a rate *decrease* (2020–21);
- (c) the age-gradient and cohort-timing predictions, which rate and price stories do not obviously generate `[INFERENCE]`;
- (d) the QWI first stage;
- (e) HonestDiD sensitivity bounds.

### 4.3 Pre-specified control set $X_c$ (all measured before 2020)

| ID | Control | Source | Enters main spec? |
|---|---|---|---|
| X1 | ln(median home value / median household income), 2015–2019 | ACS 5-yr county API (D16), aggregated to CZ | **Yes** |
| X2 | FHA share of 25–34 purchase applications, 2018–2019 | HMDA | **Yes** |
| X3 | Bachelor's+ share among employed 22–34 | PUMS | Horse-race spec only |
| X4 | Tech-industry share among employed 22–34 (NAICS 5112, 518, 519, 5415; exact `NAICSP` codes per F5) | PUMS | Horse-race spec only |
| X5 | Teleworkable share among employed 22–34 (M21) | PUMS + D14 | Horse-race spec only |

X3–X5 are strongly correlated with $z_c$ and partly lie on the causal path: education is a channel through which AI affects workers (P004 §4). Including them in the main specification would absorb part of the treatment. Hence the pre-specified main specification is {X1, X2}, and {X1–X5} is a reported horse race `[NEW]`.

---

## 5. PPML vs log-linear count models

| Issue | PPML | OLS on $\ln N$ | OLS on $\ln(1+N)$ / IHS |
|---|---|---|---|
| Zeros | Kept | Dropped (sample selection on outcome) | Kept, but the estimate depends on units (M09) |
| Consistency | Requires only a correct conditional mean $\exp(\cdot)$ (M08) | Under heteroskedasticity, $\mathbb{E}[\ln N]\neq\ln\mathbb{E}[N]$, so estimates are inconsistent for the semi-elasticity (M08) | Not a percentage effect (M09) |
| Interpretation | $100(e^{\beta}-1)$% change in expected count | % change in geometric mean | Ambiguous |
| FE | Two-way FE consistent. Three-way FE consistent but with asymptotic bias; a bias correction is available (M11). | Standard | Standard |
| DiD | Natural for ratio/parallel-trends-in-logs (M12) | — | — |
| Software | `fixest::fepois`, `ppmlhdfe` (M10), `pyfixest.fepois` | — | — |

**Decision DEC-E01: PPML for all count outcomes** `[ESTABLISHED for counts: M08–M12; used for employment counts with zeros in P004 App. C.6]`.

**Robustness.**
- (i) D-G linear long differences.
- (ii) Share-form linear DDD: $s_{ct}=N_{cYt}/(N_{cYt}+N_{cOt})$ on $z_c\,\text{Post}_t$ with CZ and year FE, weighted by $N_{cYt}+N_{cOt}$.
- (iii) Three-way-FE bias check: compare with a specification replacing $\alpha_{ct}$ by $\alpha_c+\alpha_{s(c)t}$ (M11).

PPML coefficients are semi-elasticities of the *expected* count. In D-B, $\beta^B$ is the change in the log ratio of expected young to prime-age applications.

---

## 6. Cell sizes, zeros and suppression

- **HMDA.** Kent County, DE (one mid-sized county) has 263 `<25` and 941 `25-34` purchase applications in 2025 `[PROBE]`. CZ aggregation pools about 3 counties per CZ on average (≈3,100 counties / ≈720 CZs) `[INFERENCE]`. `25-34` and `35-44` cells should be non-zero in nearly all CZ-years. `<25` cells may be small in rural CZs. Cell rates (denial, shares) need minimum-size rules: estimate cell-mean outcomes with weights equal to $N$; flag cells with $N^{dec}<20$. Distribution checked in F4.
- **HMDA has no suppression**, but there are privacy bins and partial-exemption `Exempt` values (DEC-H50, H51).
- **QWI suppression.** Status flag 5 (suppressed) and flag 9 (fuzzed, significantly distorted). Tucker (P005) reports about 1% of early-career employment and hires censored at state × industry level. At county × all-industry level the share should be lower `[INFERENCE]`. Rule: treat flags −2, −1, 5 and 11 as missing. Keep all other released values (1, 6, 7, 9, 10, 12) in the main spec, and set the distorted flags 7, 9 and 12 to missing in robustness (`07` REQ-QWI-02). Report the share of young employment in missing cells by CZ (REQ-VAL-06).

---

## 7. Inference

| Choice | Rationale | Status |
|---|---|---|
| Cluster by **state** (≈47 clusters) | Exposure is spatially correlated; neighbouring CZs share labor and housing shocks; conservative (M14, M15) | DECIDED (main) |
| Cluster by CZ | Level of treatment assignment (M15) | DECIDED (robustness) |
| AKM shift-share SEs with occupation-level "shocks" $\beta_o$ | $z_c$ is a share-weighted sum of occupation characteristics, so residuals may correlate across CZs with similar occupational mix (M07) | PROVISIONAL (implementation effort) |
| Conley spatial HAC (e.g. 250 km) | Spatial correlation beyond state borders (M13) | OPEN (needs CZ centroids) |
| Wild cluster bootstrap for linear specs (D-G, share-form) | Moderate number of clusters (M14) | PROVISIONAL |
| Generated regressor | $z_c$ is estimated from PUMS samples. Measurement error attenuates toward zero. Not corrected; disclosed. | DECIDED (disclose) |

---

## 8. Multiple-hypothesis testing

- **Primary hypothesis (one test).** $H_1$: $\beta^B<0$ (pooled, D-B, `25-34` vs `35-44`, main controls). Report the two-sided p-value.
- **Secondary families**, with Anderson (2008) sharpened FDR q-values (M17) computed within family:
  - **F-LAB** (first stage): `Emp`, `HirA`, `EarnS` for A04 vs A05 and A03 vs A05.
  - **F-COMP** (composition): mean ln income, LMI share, DTI>43 share, ln loan amount, FHA share, CLTV≥95 share.
  - **F-COND** (conditional): denial (F1), denial (F2), DTI-reason share, employment-history-reason share, rate spread.
- Romano–Wolf (M18) as robustness, if time permits.
- Specification choices are pre-specified in `07`. Results from non-pre-specified specifications are labelled exploratory.

---

## 9. Threats checklist (prompt items → where handled)

| Threat | Where handled |
|---|---|
| Endogenous occupational composition | Pre-period (2015–19) shares; Design D-D comparison; exposure is fixed over time |
| Heterogeneous pre-trends | D-C event studies; HonestDiD (M03); alternative baselines |
| Tech-sector correction | X4; exclusion of tech CZs; exposure without computer occupations |
| Interest-rate increases | X1, X2; pre-period 2018 rise and 2020–21 fall as diagnostic episodes; P022/P023 mechanisms |
| Housing affordability | X1; FHFA HPI mechanism event study; level decomposition |
| Migration and sorting | X5; PEP offsets; D-A level effects; CZ geography |
| Differential shocks to young households | Student loans (X3), FHA MIP (X2); placebo ages |
| Complementarity vs displacement | Comparison-group levels; Anthropic automation/augmentation heterogeneity (D08, post-treatment caveat) |
| Labor-market spillovers | CZ aggregation internalizes within-CZ spillovers; cross-CZ spillovers are unaddressed (disclosed) |
| Nonrandom application | `06` §3; counts as primary outcome; composition outcomes |
| Selection into origination | Denial uses actions 1–3; origination counts separately; conditional vs unconditional comparison |
| Lender composition | Lender × year FE (D-F); consistent reporters; nonbank share outcome `[OPEN: lender type]` |
| Staggered/heterogeneous AI adoption | Exposure is a continuous *potential* measure. No staggered-adoption estimator is needed, because treatment timing is common. Heterogeneous responses are interpreted with M01 caveats. |

---

## 10. Design ranking

| Rank | Design | Credibility | Feasibility (1 week) | Role |
|---|---|---|---|---|
| 1 | **D-B + D-C** (age DDD + event studies, incl. QWI first stage) | Medium (central threat: §4 rows 1–4) | High | **Primary** |
| 2 | D-F (application-level conditional / within-lender) | Low–medium as causal; high as a selection diagnostic | Medium (memory) | Mechanism module |
| 3 | D-G (long-difference cross-section) | Same assumptions as D-B, fewer moving parts | Very high | Transparency check; fallback-lite |
| 4 | D-D (industry shift-share exposure) | Not higher than D-B; established inference | Medium | Alternative exposure; **fallback** if PUMS/crosswalks fail |
| 5 | D-A (single-age DiD) | Low | Very high | Descriptive; level decomposition |
| — | D-E (IV) | Exclusion fails | — | **REJECTED** as causal; descriptive scaling only |
| — | Regression discontinuity / sharp-date designs | No exogenous cutoff in borrower or place characteristics | — | REJECTED |
| — | Individual-level design | HMDA lacks occupation | — | REJECTED (infeasible) |
| — | Synthetic control on binarized exposure | Treatment is continuous and spatially diffuse; many treated units | — | Not selected |

**Rationale.** D-B is preferred over D-A because it removes all age-invariant local shocks, including local credit-supply shocks and general demand. It is preferred over D-D because occupation-based, age-specific exposure is closer to the mechanism documented by P004/P006, and D-D's identifying assumptions are no weaker. It is preferred over D-E because the exclusion restriction is contradicted by P035/P036. The ranking is made on credibility and feasibility, **not** on expected statistical significance.
