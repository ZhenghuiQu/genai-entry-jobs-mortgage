---
project: genai-entry-jobs-mortgage
document: literature_review
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 01 — Literature Review

## 1. Scope

This document reviews four research streams relevant to *Generative AI, Entry-Level Employment, and the US Mortgage Market*:

- (A) GenAI exposure and labor outcomes;
- (B) employment shocks, income risk and housing decisions;
- (C) HMDA-based empirical research;
- (D) AI, housing markets and household finance.

It reports what each stream establishes, where findings conflict, and how each relates to this project. Paper-level details (all 21 extraction fields) are in `02_evidence_matrix.md`. HMDA processing conventions are in `03_hmda_methods_audit.md`. Mechanisms and the contribution assessment are in `06_mechanisms_and_contribution.md`. This file does not repeat them.

Verification labels follow the project convention:
- `FULL_TEXT_VERIFIED`, `METHODS_VERIFIED`, `ABSTRACT_ONLY`, `UNVERIFIED`;
- `INFERENCE` for our interpretation.

Paper IDs `P0xx` and methods IDs `M0xx` are defined in `02`.

---

## 2. Methodology of this review

### 2.1 Tools and skills actually used

| Tool / skill | Used? | What for |
|---|---|---|
| Skill `econ-lit-search` (local NBER/JEL full-text index) | **Invoked; unavailable.** The helper script has a placeholder endpoint and no API key, so every query failed. | — |
| Other installed skills (`literature-review`, `citation-management`, `openalex-api`, `lit-review-assistant`, `deep-research`) | Not invoked | Their methods (database search, DOI verification) were applied directly through the APIs below |
| `WebSearch` (standard and extended modes) | Yes | Discovery of recent working papers, competitors, policy facts |
| `WebFetch` | Yes | arXiv abstracts, Dallas Fed article, Tucker slides, FFIEC documentation. SSRN and ScienceDirect returned HTTP 403. |
| Crossref REST API (via `curl`/Python) | Yes | DOI, title, author, volume and page verification for every journal citation; retraction flag |
| OpenAlex API | Yes | Abstracts (inverted index) for papers not read in full |
| Local PDF text extraction (Python `pypdf`, in an isolated scratch directory) | Yes | Full-text and methods extraction for 20 PDFs: NBER/FEDS/FRBNY/EIG/Stanford/arXiv/CFPB versions |
| Official data endpoints (FFIEC HMDA Data Browser API and static files; LEHD QWI; Census; BLS; FHFA; GitHub) | Yes | Data-feasibility probes (`04`) |
| Consensus / Exa search connectors | Available, **not used** | — |
| GitHub repository `ZhenghuiQu/genai-entry-jobs-mortgage` | **Not consulted** | To keep this review independent of earlier proposals or other models' reviews |

### 2.2 Search strategy

- **Seed papers** were named in the brief: Eloundou et al., Felten et al., Brynjolfsson and coauthors.
- **Forward search** looked for papers citing or responding to Brynjolfsson, Chandar & Chen ("Canaries"). This led to Tucker (2026), Iscenko & Curto Millet (2026), Frank et al. (2026) and Hosseini & Lichtinger (2026).
- **Backward search** used the reference lists of Canaries (Aug 2026), Bhutta & Ringo, and Barrot et al.
- **Keyword searches** combined "AI exposure" or "generative AI" with "mortgage", "HMDA", "homeownership", "housing", "house prices", "household debt" and "credit". HMDA searches combined it with "applicant age", "denial", "local labor shock" and "first-time buyers".
- **Policy facts** covered HMDA reporting thresholds, the FHA MIP cut in 2023, and the student-loan restart in 2023.

### 2.3 Inclusion criteria

- Relevance to at least one stream.
- Verifiable existence: DOI, official repository, or the author's or institution's site.
- For empirical claims used in the design: full text or methods verified where possible; otherwise labelled `ABSTRACT_ONLY`.
- Working papers are included but labelled as such.
- Retracted work is excluded from evidence (P033).

### 2.4 Coverage limitations

- SSRN abstract pages and ScienceDirect returned HTTP 403. SSRN-only and Elsevier-only papers were verified through Crossref metadata and search-engine abstracts, so they are `ABSTRACT_ONLY`.
- Google Scholar and Semantic Scholar were not queried directly.
- Very recent working papers (2026) may exist that the search did not surface. The "no direct competitor" statement (§7) is conditional on this coverage.

---

## 3. Stream A — Generative AI exposure and labor-market outcomes

### 3.1 How exposure is measured

| Approach | Paper | What it measures | Verification |
|---|---|---|---|
| Task capability (LLM rubric) | P001 Eloundou, Manning, Mishkin & Rock (2024, *Science*) | Share of an occupation's O*NET tasks for which an LLM (E1), or LLM-powered software (E2), could cut completion time by ≥50%. α = E1; β = E1 + 0.5·E2; ζ = E1 + E2. Human and GPT-4 annotations. | FULL_TEXT_VERIFIED (arXiv version, §3; Table 2) |
| Ability-to-application mapping | P002 Felten, Raj & Seamans (2021, *SMJ*) | AI Occupational Exposure (AIOE), aggregated to industry (AIIE) and county (AIGE). A language-modeling variant is in the authors' data repository. | ABSTRACT_ONLY; data repository verified |
| Observed usage | P003 Handa et al. (2025, arXiv) | Distribution of more than four million Claude conversations over O*NET tasks; "automative" vs "augmentative" use | ABSTRACT_ONLY (first page read) |
| Vacancy-based AI exposure (pre-LLM AI) | P011 Acemoglu, Autor, Hazell & Restrepo (2022, *JOLE*) | Establishment exposure to AI-compatible tasks | ABSTRACT_ONLY |

Two points shape the design. First, P001's β is a **capability** measure fixed at 2023. It is not a measure of adoption or displacement. Second, usage-based measures (P003) are **post-treatment** objects, because usage is itself shaped by the shock. P004 uses P003's automation/augmentation split for heterogeneity, and so do we (`07` DEC-X03).

### 3.2 From exposure to realized outcomes: the entry-level evidence

- **P004 Brynjolfsson, Chandar & Chen** (Aug 2026 version; FULL_TEXT_VERIFIED). ADP payroll, millions of workers, through June 2026.
  - Employment of 22–25-year-olds in exposed occupations "now stands 19% below where it would be had it kept pace with that of their less-exposed peers" (abstract).
  - In levels, it fell about 11% in the top two exposure quintiles while growing about 10% in the bottom three (p. 3).
  - Occupation-level long differences (Table 1, p. 13), Q5 vs Q1: 22–25: −0.179 (0.036); 26–30: −0.048 (0.033); 31–34: −0.014 (0.030); 35–40: 0.001 (0.031).
  - Adjustment runs through hiring, not separations (Fact 4), and not through base pay (Fact 6, §2.6).
  - The gap is concentrated where AI use is automative (Fact 5).
  - The authors' own caveats: estimates attenuate with an occupational college-share control (Panel C: −0.091; Panel F all controls: −0.080, SE 0.057); some divergence predates ChatGPT, especially around COVID (§2.3); the ACS shows a much smaller gap, −0.022 [−0.055, +0.011] for 2022–2024 versus −0.132 in ADP, although the two agree within professional, information and financial services (§5, p. 28).
  - They describe the results as "descriptive indicators … rather than causal estimates".
- **P005 Tucker** (Apr 2026, U.S. Census Bureau CES slides; METHODS_VERIFIED). Public QWI, industry × state, ages 22–24.
  - −15% employment (−159k jobs) over 10 quarters after ChatGPT in the most-exposed quintile; an immediate 9% drop in hires; no similar decline at ages 25+.
  - A triple difference against older ages suggests substitution away from early-career workers may have begun with the COVID recession.
  - Local projections on monetary-policy shocks explain about a quarter of the 2025q2 gap, but not the discontinuous drop in hires.
  - Exposure is P001 β crosswalked to industry-states through ACS 2015–2019, which loses much of the variance.
- **P006 Hosseini & Lichtinger** (May 2026; ABSTRACT_ONLY). Résumé data for 65 million workers at more than 280,000 firms. After firms post "GenAI integrator" roles, junior employment declines relative to non-adopters, mainly through slower hiring; senior employment is largely unchanged.
- **P007 Atkinson & Yamco** (Dallas Fed, Jan 2026; FULL_TEXT_VERIFIED). CPS data.
  - The most-exposed tertile's share of young (20–24) employment fell from 16.4% (Nov 2022) to 15.5% (Sep 2025).
  - There is no rise in layoffs. Job-finding rates of young labor-market entrants into exposed occupations fell by more than 3 percentage points from their Nov 2023 peak.
  - The aggregate unemployment effect is about 0.1 percentage point.

### 3.3 Skeptical and conflicting evidence

- **P008 Frank et al.** (Jan 2026, arXiv; ABSTRACT_ONLY). In unemployment-insurance records, unemployment risk in AI-exposed occupations rose "beginning in early 2022, months before ChatGPT". In LinkedIn data, graduate cohorts from 2021 onward entered exposed jobs at lower rates. Graduates with AI-exposed coursework did *better* after ChatGPT.
- **P009 Iscenko & Curto Millet** (EIG, Jan 2026; FULL_TEXT_VERIFIED; both authors at Google, disclosed). Using Lightcast postings, they argue the entry-level decline is better explained by the March 2022 monetary tightening. About 38% of workers in the top exposure quintile work in information, finance and insurance, or professional and technical services, versus under 2% in the bottom quintile. Exposed postings also fell more in the early-2020 slowdown.
- **P010 Humlum & Vestergaard** (2025, NBER WP 33777; ABSTRACT_ONLY). Denmark, linking adoption surveys to administrative data. "Precise zeros" on earnings and hours, with confidence intervals ruling out effects above 1%.
- **Resolution so far.** P004 controls for occupational interest-rate exposure (Zens et al. 2020, M22) and finds little attenuation (Table 1 Panel B). P005 attributes about one quarter of the gap to monetary policy. Neither paper settles causality.

### 3.4 Substitution vs complementarity

- In P004 (Fact 5), employment declines concentrate where AI usage is automative; where usage is complementary, employment is flat or rising, especially for experienced workers.
- P012 Brynjolfsson, Li & Raymond (2025, *QJE*; ABSTRACT_ONLY): AI assistance raised customer-support productivity by 15% on average, with the largest gains for less experienced workers.
- P011 (ABSTRACT_ONLY, pre-LLM AI): AI-exposed establishments reduce non-AI hiring, but aggregate effects are "too small to be detectable".
- `INFERENCE`: complementarity can *raise* older workers' earnings in exposed places. This matters for the choice of comparison group (`05` §3.4).

### 3.5 Heterogeneity and causal status

- **Heterogeneity.** Age is the dominant dimension (P004, P005, P006, P007). Education matters too: P004's estimates attenuate with a college-share control, and P006 finds a U-shape by graduate institution tier. By industry, P004 §5 finds that ADP and ACS agree within professional, information and finance sectors. Geographic heterogeneity has **not** been studied in this literature at the local labor-market level (`INFERENCE` from the search).
- **Causal status.** None of the US studies claims clean causal identification. P004 is explicitly descriptive. P006's firm-adoption DiD is the closest to a causal design and relies on adoption timing. The evidence is best summarized as a robust *association* for young workers in exposed occupations, of disputed magnitude and timing.

### 3.6 Synthesis

| Claim | Status | Sources |
|---|---|---|
| Young (22–25) workers in exposed occupations saw relative employment declines after late 2022 | Supported in ADP, QWI, résumé and CPS data; weak in the ACS | P004, P005, P006, P007; P004 §5 |
| Adjustment is via hiring, not layoffs or base pay | Consistent across sources | P004, P005, P006, P007 |
| Effects for workers aged 26+ | Small or none | P004 Table 1; P005 |
| The decline is caused by GenAI rather than by rates or the tech cycle | **Contested** | P008, P009 vs P004, P005 |
| Earnings effects | Small | P004 Fact 6; P010 |

---

## 4. Stream B — Employment shocks, income risk and housing decisions

### 4.1 Theory

- **Tenure choice under income risk.** Higher earnings risk lowers ownership through irreversibility and transaction costs (Dixit & Pindyck 1994, M23). In a calibrated life-cycle model, the post-1980 rise in earnings risk "can easily account for" the decline in young homeownership beyond delayed marriage (P016 Fisher & Gervais 2011, *IER*; ABSTRACT_ONLY). Riskier and more unequal earnings for later cohorts explain much of the cross-generation fall in homeownership (Paz-Pardo 2024, *AEJ: Macro*; ABSTRACT_ONLY). Earlier empirical work on income variability and tenure choice: P013 Haurin (1991), P014 Robst, Deitz & McGoldrick (1999), P015 Diaz-Serrano (2005). These were verified at title level only, so they are cited for topic only.
- **Counter-force: rent hedging.** Ownership hedges rent risk, and this matters more for households with longer expected stays (Sinai & Souleles 2005, *QJE*; ABSTRACT_ONLY).
- **Credit constraints.** The ability of young households to afford a starter-home down payment is "a powerful driver" of housing-market dynamics (P017 Ortalo-Magné & Rady 2006, *REStud*; ABSTRACT_ONLY). DTI limits bind and amplify rate shocks (P023 Bhutta & Ringo 2021, *JME*; METHODS_VERIFIED, FEDS version pp. 4–5, 22).
- **Precaution.** Precautionary wealth responds to unemployment risk for moderate- and higher-income households, but not in wealth subaggregates that exclude home equity (Carroll, Dynan & Krane 2003, *REStat*; ABSTRACT_ONLY).

### 4.2 Empirical evidence on young households

- **Debt.** A $1,000 increase in student debt lowers homeownership by about 1.8 percentage points in the mid-20s (P019 Mezza et al. 2020, *JOLE*; ABSTRACT_ONLY). Related: rising tuition and homeownership (P041 Bleemer et al. 2021; title only); debt and parental co-residence (P040 Dettling & Hsu 2018; title only).
- **Insurance through family.** Moving back home insures young workers against labor-market risk (P018 Kaplan 2012, *JPE*; ABSTRACT_ONLY). This is a mechanism through which entry-level shocks delay household formation.
- **Entry conditions.** Entering the labor market in a downturn causes persistent earnings losses (P020 Schwandt & von Wachter 2019, *JOLE*; P042 Oreopoulos, von Wachter & Heisz 2012, *AEJ: Applied*; both ABSTRACT_ONLY). This motivates "cohort scarring" predictions: affected 2023–2025 entrants should carry lower earnings and housing demand into their late twenties (`INFERENCE`).
- **Expectations.** Personal unemployment experience makes people more pessimistic about aggregate unemployment (P021 Kuchler & Zafar 2019, *JF*; ABSTRACT_ONLY). This is indirect support for mechanism M2.
- **Rate sensitivity.** A 1-percentage-point policy-induced rise in mortgage rates lowers lower-income households' presence among home buyers by 1–2 percentage points, with stronger effects for first-time buyers (P022 Ringo 2026, *REStat*; METHODS_VERIFIED, FEDS version). After 2008, young homeownership declined most in high-price regions (Mabille 2023, *RFS*; ABSTRACT_ONLY). Both papers show that **financing shocks have age- and place-specific incidence**, which is central to the confounding analysis (`05` §4).

### 4.3 Labor shocks and mortgage borrowing: a competing prediction

**P024 Barrot, Loualiche, Plosser & Sauvagnat** (2022, *JF*; METHODS_VERIFIED, FRBNY SR 821) find that import-competition shocks *raised* household debt, mainly through home-equity extraction where house prices grew. In their data, HMDA denial rates were higher in exposed commuting zones, which they read as higher demand (SR 821 p. 19; Table A.4).

So a negative local labor shock does **not** necessarily reduce mortgage activity. Incumbent owners may borrow to smooth consumption. For *young prospective buyers*, who are mostly renters, the prediction differs (`INFERENCE`). This is one reason the design focuses on home-purchase applications by age.

---

## 5. Stream C — HMDA-based empirical research (summary)

The detailed reconstruction of samples, outcomes, fixed effects and standard errors is in `03_hmda_methods_audit.md` §2. In brief:

- **Area-level demand and denial outcomes:** P025 (ZIP level), P024 (CZ level).
- **Application-level denial models:** P027, P028.
- **Credit-supply designs using lender heterogeneity:** P027, P029, P030, P032.
- **Official descriptive conventions:** P031 (CFPB).

The established population for housing-demand questions is first-lien, owner-occupied, site-built 1–4 family, home-purchase loans. P028 shows that, with confidential credit scores and AUS results, observable risk explains most denial disparities. Public-HMDA conditional denial regressions therefore omit key risk variables.

No audited academic paper uses public HMDA **applicant age** as a primary dimension. P033 (Ouazad & Kahn 2022) is flagged **retracted** in Crossref metadata and is not used as evidence.

---

## 6. Stream D — AI, housing markets and household finance

| Paper | Finding | Verification | Relation to this project |
|---|---|---|---|
| P035 Li & Guo (2026, *Finance Research Letters* 108: 110442) | Counties with higher occupational AI exposure saw larger increases in home values after ChatGPT's release, a relative decline in new listings, and no comparable rise in buyer-side indicators (Zillow/Redfin, Jul 2021–Jun 2024, continuous DiD) | ABSTRACT_ONLY (search-engine abstract; ScienceDirect 403) | **Closest competitor** on housing. No mortgage, age or labor first stage. |
| P036 Seagraves & Sirmans (2026, SSRN 6749481) | 211 metros, 2017Q1–2025Q4: +1 SD exposure ↔ +3.6% cumulative ZHVI growth (about $9,400 at the median); concentrated in supply-inelastic metros; WFH placebo has the opposite sign; reduced outmigration (IRS) and rising AI hiring (Revelio) | ABSTRACT_ONLY (secondary summary of the SSRN abstract) | Price channel A1; supports the "exposure raises prices" finding |
| Li & Guo (2026, SSRN 6987090) "Generative AI Infrastructure and Local Housing Markets" | Exists (Crossref) | UNVERIFIED content | Data-center channel; not used |
| P034 Chu, He, Qiu & Zhao (2026, SSRN 6342658) | Bank AI adoption (job postings) widens racial gaps in denial (+0.75 pp per SD) and interest rate (+4 bp); HMDA 2022–2024; IV using AI-graduate supply | ABSTRACT_ONLY | Supply-side AI in lending. Shows lender AI adoption is a separate channel that could affect denial outcomes. |
| P037 Mondragon & Wieland (2022, NBER WP 30041) | Remote work explains more than half of the 18.9% real house-price increase from 2019 to 2023 | ABSTRACT_ONLY | Template for exposure → housing demand; confounder A4 |
| P038 Eisfeldt, Schubert & Zhang (2023, NBER WP 31222) | Firms with higher GenAI workforce exposure earned 0.4% higher daily excess returns after ChatGPT | ABSTRACT_ONLY | Wealth channel (A1) for equity-holding incumbents |
| P039 Fonseca & Liu (2024, *JF*) | Mortgage lock-in reduced mobility, by 16% per 1 pp rate gap in 2022–2024 | ABSTRACT_ONLY | Confounder A7 (listings, move-up buyers) |

**Automation and household debt (pre-GenAI).** The searches did not surface a verified paper on robot or automation exposure and US mortgage applications. P024 (trade) is the closest labor-shock analogue.

---

## 7. Closest competing studies and differences

| Dimension | This project | P035 Li & Guo | P036 Seagraves & Sirmans | P005 Tucker | P024 Barrot et al. |
|---|---|---|---|---|---|
| Outcome | HMDA purchase applications, composition, denial and pricing **by age** | House values, listings | House-price growth, migration | Young employment and hires | Household debt; HMDA applications and denials |
| Geography | CZ | County | Metro | Industry × state | CZ |
| Period | 2018–2025 | Jul 2021–Jun 2024 | 2017Q1–2025Q4 | to 2025q2 | 2000–2007 |
| Exposure | Young-worker occupational β (P001), pre-period | Occupational AI exposure (county) | Population-weighted AI exposure; LLM task suitability | P001 β to industry | Shipping costs × industry mix |
| Identification | Age DDD with CZ × year FE; event study; first stage | Continuous DiD | Exposure × post; placebo | Event study; DDD by age | Cross-sectional long differences |
| Mechanism | Labor (M1/M2) vs price (A1) vs rates (A2) | Supply-side (listings) | Demand from AI-complement workers | Entry-level hiring | Equity extraction |

**Is the question already answered?** No (`06` §6.2). The closest housing papers study prices rather than mortgage credit by age. The closest labor paper studies employment only.

**Overlap risk.** Medium. The same public data (HMDA 2025, released mid-2026) are available to anyone, and the competitor papers are recent. The contribution should be framed around the *age composition of mortgage demand* and *channel discrimination*, not around "AI affects housing" in general.

---

## 8. Relationship to this project (summary)

1. The labor evidence justifies an **age-specific** exposure focus (22–34) and an age comparison. It also warns that the 25–34 HMDA bin is only partly treated and that the first stage is contested (`05` §3).
2. The housing-finance evidence identifies down payments, DTI constraints, rate sensitivity and debt as the channels through which young households' labor shocks would reach mortgage demand. The same channels are confounders, because rates and prices have age-specific incidence.
3. The HMDA literature supplies the population definition, the action-code conventions and the reading of denial rates as demand-contaminated.
4. The AI-housing papers imply that exposure **raises** prices. The naive expectation ("hit regions → fewer applications, more denials") must therefore be tested against a price channel that predicts the same decline in young applications but larger loans and higher DTI.
