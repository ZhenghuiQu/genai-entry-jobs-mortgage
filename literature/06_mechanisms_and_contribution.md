---
project: genai-entry-jobs-mortgage
document: mechanisms_and_contribution
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 06 — Economic Mechanisms, Selection, and Contribution

## 0. Scope

This document develops the economic framework linking GenAI exposure to HMDA outcomes. It separates four mechanisms (M1–M4) from alternative explanations (A1–A8), derives testable implications, analyses borrower and lender selection, and assesses the contribution relative to existing research.

The model is **illustrative**. It organizes predictions and is not estimated. Statements are tagged `[THEORY: source]`, `[EVIDENCE: Pxxx]`, `[INFERENCE]` or `[REC]`.

---

## 1. Transmission framework

### 1.1 Households

A potential buyer $h$ of age $a$ lives in CZ $c$. Labor income is
$$
y_{h t}=\exp(p_{ht}+\varepsilon_{ht}),\qquad p_{h,t+1}=p_{ht}+g_{a,o}+\eta_{h,t+1},\quad \eta\sim(0,\sigma^2_{\eta,o}),
$$
where $o$ is the worker's occupation (or the occupation the worker would enter). GenAI exposure can act through three parameters:

1. **Entry probability** $\pi_{a,o}$: the probability that a young entrant obtains a job in occupation $o$ in a given period. P004 Fact 4 and P006 find that adjustment runs mainly through reduced *hiring* of young workers `[EVIDENCE]`.
2. **Expected growth** $g_{a,o}$: career-ladder returns. If entry-level tasks are automated, the expected return to entering exposed occupations may fall `[INFERENCE]`.
3. **Risk** $\sigma^2_{\eta,o}$: uncertainty about career paths in exposed occupations `[INFERENCE]`.

### 1.2 Tenure choice and feasibility

Following the life-cycle tenure-choice tradition `[THEORY: P016, P017, Sinai & Souleles 2005]`, household $h$ applies to buy at $t$ if
$$
\underbrace{V^{O}(W_{ht},p_{ht};\,g,\sigma^2,P_{ct},r_t)-V^{R}(W_{ht},p_{ht};\,g,\sigma^2,R_{ct})}_{\text{ownership premium}}\;\ge\;\kappa_h
$$
and expects to satisfy the underwriting constraints
$$
W_{ht}\ \ge\ (1-\overline{LTV})\,P_{ct}\quad\text{(down payment)},\qquad
\frac{m(r_t)\,L_{ht}+\text{other debt}_{ht}}{y_{ht}}\ \le\ \overline{DTI}\quad\text{(DTI)}.
$$
Here $W$ is liquid wealth, $P_{ct}$ the house price, $R_{ct}$ rent, $m(r)$ the payment factor, $L$ the loan, and $\kappa_h$ includes transaction costs. Three established forces shape the response to an income shock.

- **Irreversibility.** With transaction costs, the option value of waiting rises with $\sigma^2$, raising the ownership threshold `[THEORY: Dixit & Pindyck 1994]`. Higher earnings risk lowers young homeownership in calibrated life-cycle models `[EVIDENCE: P016 abstract; Paz-Pardo 2024 abstract]`.
- **Down payment.** Young households' ability to afford a starter-home down payment is "a powerful driver" of housing markets `[EVIDENCE: P017 abstract]`.
- **DTI constraints.** These bind for lower-income buyers and amplify rate shocks `[EVIDENCE: P023 FEDS pp. 4–5, 22; P022 abstract]`.

**Offsetting force.** Ownership hedges rent risk, and that motive strengthens with expected tenure length `[EVIDENCE: Sinai & Souleles 2005 abstract]`. If GenAI raises local rents (P037 for remote work; P035/P036 for prices), the hedging motive could *raise* ownership demand among those who can afford it.

### 1.3 Application and approval

Let $q_h$ be latent creditworthiness: income stability, credit score, DTI headroom. Applying costs $c_A$. The lender approves if $q_h+\nu_h\ge\bar s_{\ell}$, where $\nu$ is unobserved to the econometrician and $\bar s_\ell$ is lender $\ell$'s standard. A household applies if $\Pr(\text{approve}\mid q_h)\cdot S_h\ge c_A$, where $S_h$ is the surplus. This gives an application threshold $q^*$.

**HMDA observes** only applicants ($q_h\ge q^*$), their reported characteristics (income, DTI bin, loan amount, CLTV, loan type), the lender's decision, and price.

### 1.4 Mapping to HMDA observables

$$
N^{app}_{cat}=\text{Pop}_{cat}\cdot\Pr(\text{want to buy}\mid\cdot)\cdot\Pr(q\ge q^*\mid\cdot),\qquad
D_{cat}=\Pr(q+\nu<\bar s\mid q\ge q^*).
$$

---

## 2. Mechanisms

### M1 — Employment and realized earnings

- **Intuition.** Fewer young workers obtain entry-level jobs in exposed occupations, or they obtain them later or in lower-paying occupations. They have lower current income, shorter employment histories, and slower savings for the down payment.
- **Representation.** $\pi_{a,o}\downarrow$ for $a\in$ {22–25} and exposed $o$. This lowers $\mathbb{E}[y]$ and $W$, and causes failures of the down-payment and DTI constraints.
- **Assumptions.** The labor shock is local enough to differ across CZs (place-based incidence). Affected individuals would otherwise have bought in the same CZ within the window.
- **Observable predictions.**
  - QWI young employment and hires fall in high-$z$ CZs (first stage).
  - Young applications fall, more for `<25` than `25-34` (age gradient).
  - The effect grows over 2023–2025.
  - Denial reason "employment history" rises among young denials.
  - Applicant composition shifts in an *ambiguous* direction (§3).
- **Data.** QWI (D04); HMDA (D01).
- **Confounders.** A2 (rates), A3 (tech correction), A5 (student loans).
- **What the data can identify.** Whether places with high young-worker exposure saw relative declines in young employment *and* young mortgage applications at the same time.
- **What they cannot identify.** That the *same individuals* are involved (no linkage). Whether employment declines are *caused by* AI rather than correlated shocks (P008, P009). Occupational displacement locally (QWI has no occupation).

### M2 — Expected future income and income uncertainty

- **Intuition.** Even employed young workers in exposed occupations may expect flatter career ladders or face higher uncertainty. They delay irreversible purchases.
- **Representation.** $g_{a,o}\downarrow$ and/or $\sigma^2_{\eta,o}\uparrow$. The ownership premium falls and the threshold rises (option value) `[THEORY]`.
- **Supporting evidence (indirect).** Personal labor-market experiences shift expectations (P021 abstract). Precautionary wealth responds to job-loss risk for moderate- and higher-income households (Carroll, Dynan & Krane 2003 abstract).
- **Assumptions.** Young workers perceive exposure-specific risk, for example from news, peers or employer signals.
- **Observable predictions.**
  - Young applications fall *without* a commensurate QWI employment decline.
  - Remaining young applicants are *positively* selected: higher income, lower DTI, lower denial.
  - Possibly immediate timing (an information shock in 2023).
- **Data.** HMDA. No local expectations data is available: the NY Fed SCE is not public at CZ level `[INFERENCE]`.
- **Confounders.** Any shock that lowers young demand without a labor effect (A1, A2).
- **Can identify.** Only *residually*: a demand decline without a first stage is *consistent with* M2, but also with A1 and A2.
- **Cannot identify.** Expectations or risk directly. **M2 is not separately identifiable from A1/A2 with this data** `[REC: state explicitly]`.

### M3 — Mortgage demand and endogenous applicant selection

- **Intuition.** M1 and M2 operate on the *extensive margin of application*. Applicants who drop out are those closest to the threshold, so the observed applicant pool changes composition.
- **Representation.** $q^*\uparrow$ and/or $F(q)$ shifts left (§3.1).
- **Observable predictions.**
  - $N^{app}\downarrow$ (unambiguous under M1/M2).
  - Composition (income, DTI, LMI share) and *unconditional* denial: **ambiguous sign**.
- **Can identify.** Changes in volume and composition of applicants.
- **Cannot identify.** Potential buyers who chose not to apply. HMDA contains no record of non-applicants `[DOC]`.

### M4 — Conditional lender decisions and pricing

- **Intuition.** Lenders may perceive higher employment risk for young applicants in exposed local markets and tighten underwriting overlays. Or they may price risk via rate spreads. Discouraged borrowers would then reduce applications.
- **Representation.** $\bar s_{\ell}\uparrow$ for young applicants in high-$z$ CZs.
- **Assumptions.** Lenders have discretion beyond agency AUS rules. GSE loan-level price adjustments depend on credit score and LTV, not on local AI exposure `[INFERENCE]`, so effects would arise from overlays, portfolio lending or non-agency pricing.
- **Observable predictions.**
  - Conditional denial (D-F, F2/F3) rises for young applicants in high-$z$ CZs, *within lender*.
  - The employment-history denial reason rises.
  - Conditional rate spread rises.
- **Data.** HMDA application-level file.
- **Confounders.** Unobserved credit scores and AUS results. Public HMDA lacks both, and P028 shows they explain most conditional denial gaps.
- **Can identify.** Changes in conditional denial *given public observables*, within lender.
- **Cannot identify.** Credit-supply changes as distinct from unobserved applicant risk. Any D-F estimate is therefore an **upper bound on supply-side explanations only under the assumption that unobserved risk did not change differentially** `[INFERENCE]`.

---

## 3. Borrower and lender selection

### 3.1 Why denial rates are not credit-supply measures here

With threshold $q^*$, the denial rate is
$$
D=\frac{\int_{q^*}^{\infty}G(\bar s-q)\,dF(q)}{1-F(q^*)},\qquad G=\text{CDF of }\nu .
$$
Differentiating with respect to the application threshold:
$$
\frac{\partial D}{\partial q^*}=\frac{f(q^*)}{1-F(q^*)}\Big[D-G(\bar s-q^*)\Big]<0,
$$
because the marginal applicant at $q^*$ has the *highest* denial probability, $G(\bar s-q^*)>D$.

So:

- **Pure screening-out** of marginal applicants (M2/M3 raising $q^*$) **lowers** the observed denial rate, with lender standards $\bar s$ unchanged.
- **A leftward shift of $F$** among those who still apply (M1 lowering incomes) **raises** it.
- **A rise in $\bar s$** (M4) **raises** it.

The sign of $\Delta D$ is therefore uninformative about credit supply without further structure `[INFERENCE, derived]`. P024 reads *higher* denial rates in import-exposed CZs as evidence of *higher* demand (FRBNY SR 821, p. 19). The same logic of reading denial through demand applies here, with the opposite sign possible.

### 3.2 Same logic for pricing

Rate spreads are observed only for originations (and some action-2 records), after **two** selections: into application, then into approval and acceptance. A change in the mean spread mixes the risk composition of originated borrowers with lender pricing `[INFERENCE]`.

### 3.3 What HMDA regressions identify, and how the plan uses them

| Quantity | Identified? | Plan |
|---|---|---|
| Change in the number of applications by age | Yes (reduced-form exposure effect) | Primary outcome (D-B) |
| Change in observable composition of applicants | Yes (descriptive) | F-COMP family |
| Change in unconditional denial / spread | Yes (descriptive), but mixes selection and supply | Reported, labelled as mixed |
| Change in denial / spread *conditional on public observables*, within lender | Yes, under the stated assumption | D-F; labelled "conditional on public HMDA observables" |
| Credit supply to equally risky young applicants | **No** (unobserved credit score, AUS) | Not claimed |
| Behaviour of potential buyers who did not apply | **No** | Not claimed |
| Workers who lost jobs because of AI | **No** (no occupation in HMDA) | Not claimed |

**Composition decomposition `[REC]`.** For each conditional outcome, report (i) the unconditional change and (ii) the change conditional on the pre-specified observable bins. Optionally add (iii) the change after reweighting post-period applicants to the pre-period distribution of observables within CZ × age. The difference (i) − (ii) is the part attributable to changes in *observable* composition.

### 3.4 Lender selection and lender composition

The lender mix differs by age. Non-banks and FinTech lenders have different processing and pricing (P027, P029), and their market shares changed after 2022 (P031 p. 6: independent mortgage companies originated 61.9% of closed-end purchase loans in 2023). Changes in which lenders young applicants use can move denial and spread outcomes. Mitigations:

- lender × year FE (F2);
- lender × CZ × year FE (F3);
- report the change in lender-type share by age as an outcome `[OPEN: lender type from TS agency code]`;
- the consistent-reporter sample (DEC-H52).

---

## 4. Testable-implications matrix

Signs refer to the young (`25-34`, and `<25` where noted) **relative to** `35-44`, in high-$z$ vs low-$z$ CZs, after 2022.

- "±" means ambiguous; "0" means no prediction or no effect.
- "early" means the effect starts in 2022.
- "rising" means the effect grows over 2023–2025.

| Outcome | M1 employment | M2 expectations | M4 lender tightening | A1 AI-driven house prices | A2 rate shock × affordability | A3 tech correction |
|---|---|---|---|---|---|---|
| QWI young employment / hires (first stage) | − (rising) | 0 | 0 | 0 | − (early) | − (early) |
| HMDA young applications $N^{app}$ | − (rising) | − | − (discouraged) | − | − (early, fading) | − (early) |
| Age gradient (`<25` more negative than `25-34`) | Yes | Unclear | Unclear | Not predicted `[INFERENCE]` | Not predicted | Unclear |
| `35-44` applications in levels (D-A) | 0 | 0 | 0 | 0 or + | − | − |
| Mean ln income of young applicants | ± | + | + (only strong approved) | + | + | ± |
| High-DTI share | ± | − | − | + (stretching) | + | ± |
| ln loan amount | − or ± | − | ± | **+** | ± | ± |
| FHA share | + | ± | ± | ± | − (after the MIP cut, +) | ± |
| Unconditional denial | ± | − | + | + | + | ± |
| Conditional denial (within lender) | + (employment history) | 0 | **+** | + (DTI) | + (DTI) | ± |
| Employment-history denial reason | **+** | 0 | + | 0 | 0 | + |
| Local HPI (FHFA) | − or 0 | − or 0 | 0 | **+** | − | − |
| Timing | rising after 2023 | 2023 onward | 2023 onward | follows prices | **2022 onward** | **2022 onward** |

**Discriminating tests (pre-specified) `[REC]`**

1. **Timing.** A break in 2022 (pre-ChatGPT) in the HMDA or QWI event study favours A2/A3. A break that starts in 2023 and grows favours M1/M2.
2. **House prices.** If high-$z$ CZs show *rising* relative house prices (as P035/P036 report), then A1 is present. Young applicants should then show *higher* loan amounts and DTI. M1 predicts the opposite for loan amounts.
3. **Age gradient.** M1 uniquely predicts `<25` > `25-34` in absolute effect.
4. **Employment-history denial reason.** Specific to M1/M4.
5. **First stage.** Without a QWI first stage, M1 has no support. Remaining effects are then attributable to M2, A1 or A2, which cannot be separated.

---

## 5. Alternative explanations

| ID | Alternative | Evidence | How it would mimic the main pattern | Plan |
|---|---|---|---|---|
| A1 | AI-driven local price growth (wealth of incumbents, AI-complement high earners) | P035 abstract: higher home values and fewer listings in high-exposure counties after ChatGPT; P036 abstract: +3.6% ZHVI growth per SD exposure in 211 metros, 2017Q1–2025Q4; reduced outmigration | Prices up → young first-time buyers priced out → young applications down | HPI event study; loan-amount/DTI composition; X1 |
| A2 | Monetary tightening × local affordability | P022: rate hikes reduce LMI and first-time buyers' share; P023: DTI constraints amplify; P009: exposure concentrated in rate-sensitive sectors | Larger young declines in expensive (high-$z$) places | X1, X2; timing |
| A3 | Tech/finance labor correction 2022–23 | P008: AI-exposed unemployment risk rose from early 2022; P009: hiring declines from March 2022 | Young labor and young demand fall in tech-heavy CZs | X4; timing; exclude tech CZs |
| A4 | Remote work and migration of the young | P037: remote work explains over half of 2019–2023 real house price growth | Young out-migration from expensive white-collar CZs | X5; PEP denominators |
| A5 | Student-loan repayment restart (Oct 2023) | Policy fact (secondary sources); P019: student debt lowers homeownership | Young DTI ↑ and applications ↓ where college share is high | X3; DTI outcomes |
| A6 | FHA MIP cut (Mar 2023) | HUD ML 2023-05 (secondary sources) | Boosts young FHA-reliant buyers in low-$z$ CZs → spurious negative | X2; FHA vs conventional split |
| A7 | Lock-in reducing move-up purchases (older) | P039; Liebersohn & Rothstein 2024 | Shifts the age mix *toward* young (opposite sign) | Levels; 45–54 comparison |
| A8 | HMDA coverage changes | P031 fn. 7 | Artificial counts changes where small lenders matter | Consistent reporters |

---

## 6. Contribution relative to existing research

### 6.1 What is established (with verification status)

**AI labor literature (Stream A)**

- LLM *exposure* is widespread across occupations, measured as task capability (P001, full text).
- In ADP payroll data, employment of 22–25-year-olds in the most exposed occupations is 19% below where it would be had it kept pace with less-exposed peers (June 2026). The gap works through hiring; experienced workers show no comparable gap; base pay barely adjusts (P004, full text). The authors call these "descriptive indicators … rather than causal estimates" (P004 abstract).
- QWI shows a 15% employment decline for 22–24 in the most exposed industry-states over 10 quarters after ChatGPT. Hires dropped 9% immediately. About a quarter of the gap may be monetary policy, and early-career substitution may have begun with COVID (P005, slides).
- Firm-level résumé data show junior declines at GenAI-adopting firms, via hiring (P006, abstract).
- **Contested.** Deterioration began before ChatGPT (P008, abstract), and the interest-rate confound is serious (P009, full text). In the representative ACS the overall young-worker gap is small and insignificant (−0.022 [−0.055, 0.011]), while it agrees with ADP within professional, information and financial services (P004 §5). Danish administrative data show precise null effects on earnings and hours (P010, abstract).

**Income risk and housing (Stream B)**
- Earnings risk and credit constraints are leading explanations for lower and delayed young homeownership (P016, P017, Paz-Pardo 2024; all abstract).
- Student debt delays ownership (P019, abstract).
- First-time and LMI buyers are the most rate-sensitive (P022, P023).
- Young-homeownership declines after 2008 were concentrated in high-price regions (Mabille 2023, abstract).

**HMDA research (Stream C)**
- A mature toolkit for area-level demand and denial outcomes (P024, P025), application-level denial models (P027, P028), and lender heterogeneity (P027, P029).
- Applicant age has been in public HMDA since 2018 but is barely used in academic work.

**AI and housing (Stream D)**
- AI exposure is associated with *higher* local house prices (P035, P036, both abstract-only).
- One paper studies *lender* AI adoption and racial gaps (P034, abstract).

### 6.2 What remains unanswered

1. Whether GenAI exposure changed the **age composition of mortgage demand** across local markets.
2. Whether any such change runs through **young workers' labor outcomes** (M1/M2) or through **AI-driven house prices and wealth** (A1). The two predict opposite signs for young applicants' loan sizes and for local prices.
3. How **applicant selection** shapes measured denial and pricing for young borrowers in exposed markets.

No paper found as of 2026-10-08 addresses (1)–(3). This search-based statement is limited by the coverage of the search tools; SSRN direct search was blocked (`01` §2.4).

### 6.3 Closest competitors and differences

| Paper | Data | Outcome | Identification | Mechanism | Difference from this project |
|---|---|---|---|---|---|
| P035 Li & Guo (2026, FRL) | Zillow, Redfin; county; Jul 2021–Jun 2024 | Home values, listings, sale-to-list | Continuous DiD around ChatGPT release | Supply-side (fewer listings) | No mortgage, no age, no labor first stage; ends mid-2024 |
| P036 Seagraves & Sirmans (2026, SSRN) | ZHVI, FHFA; 211 metros; 2017Q1–2025Q4 | House-price growth; migration (IRS); AI hiring (Revelio) | Exposure × post; LLM task-suitability alternative; WFH placebo | Demand from AI-complement workers; reduced outmigration | No mortgage applications by age; prices, not credit |
| P004 Canaries (2026) | ADP | Employment by age × occupation | Descriptive long differences, firm × time FE | Entry-level substitution | Labor only; no housing |
| P005 Tucker (2026) | QWI, industry × state | Employment, hires, earnings by age | Event study and DDD across ages | Entry-level hiring | Labor only. Closest **public-data template for our first stage.** |
| P024 Barrot et al. (2022, JF) | CCP, HMDA; CZ; 2000–07 | Household debt, HMDA applications and denials | Shift-share exposure (shipping costs) | Trade shock → equity extraction by owners | A labor shock raised borrowing among *owners*. Our population is *young prospective buyers*, where the sign may differ. |

### 6.4 Nature and size of the likely contribution (honest assessment)

| Type | Assessment |
|---|---|
| New empirical fact | **Yes, primary.** Age-specific mortgage-demand responses to GenAI exposure, measured with a complete public dataset (HMDA 2018–2025). |
| Reconciliation | **Plausible, secondary.** It could reconcile *rising* prices in exposed markets (P035, P036) with *weaker* young demand, through a reallocation of mortgage credit across ages. This depends on results. |
| Measurement | **Modest.** Age-specific, residence-based CZ exposure; a reusable age × CZ HMDA panel. |
| New transmission mechanism | **Partially testable only.** M1 can be supported or undermined (first stage, gradient, timing). M2 is not separately identifiable from A1/A2. |
| New identification approach | **No.** The design adapts standard exposure-DDD logic. |

**Bottom line.** The original question ("does GenAI exposure affect the mortgage market through early-career labor outcomes?") is **not already answered** in the literature. But the labor first stage it presupposes is *contested* (P008, P009, P004 §5, P010). The project should therefore be framed more narrowly:

> *Did places where young workers were more exposed to LLMs see a relative decline in young households' mortgage demand after 2022, and is the pattern consistent with an entry-level labor channel rather than with house-price, interest-rate, or tech-cycle channels?*

This framing promises an empirical fact plus a set of *discriminating* tests. It does not promise a cleanly identified causal labor-to-mortgage elasticity, which current data cannot deliver.
