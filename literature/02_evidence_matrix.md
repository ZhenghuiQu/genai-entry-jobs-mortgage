---
project: genai-entry-jobs-mortgage
document: evidence_matrix
model: claude-opus-5-5 (Claude Opus 5.5, Claude Code desktop)
date: 2026-10-08
status: independent_review
research_cutoff: 2026-10-08
---

# 02 — Paper-Level Evidence Matrix and Bibliography

## 0. Scope and legend

This file is the canonical registry of paper IDs (P001–P042) and methods references (M01–M25) used across the package. Each paper has a YAML block with the 21 required fields. Fields that could not be verified are marked `n.v.`; "n.v." means not verified, **not** "not done".

**Verification labels**

| Label | Meaning |
|---|---|
| `FULL_TEXT_VERIFIED` | Relevant claims checked against an accessible full text, typically the working-paper version, which is named |
| `METHODS_VERIFIED` | Methodological details checked against the paper, appendix or slides |
| `ABSTRACT_ONLY` | Only the abstract was available. It was obtained from OpenAlex, the publisher, arXiv or a search-engine summary of the abstract (the source is stated). |
| `UNVERIFIED` | Bibliographic or substantive information could not be independently confirmed |
| `INFERENCE` | An interpretation by this review, not stated in the source |

Bibliographic metadata (authors, title, venue, volume, pages, DOI) were checked against **Crossref** for every DOI-bearing item. Page numbers in "location" refer to the version read, which is named in the block.

## 1. Summary table

| ID | Short citation | Stream | Status | Relevance | Verification |
|---|---|---|---|---|---|
| P001 | Eloundou et al. 2024 | A | Published (*Science*) | High (exposure measure) | FULL_TEXT_VERIFIED (arXiv) |
| P002 | Felten, Raj & Seamans 2021 | A | Published (*SMJ*) | Medium | ABSTRACT_ONLY |
| P003 | Handa et al. 2025 | A | Preprint (arXiv) | Medium (heterogeneity) | ABSTRACT_ONLY |
| P004 | Brynjolfsson, Chandar & Chen 2026 | A | Working paper (Aug 2026) | **Very high** | FULL_TEXT_VERIFIED |
| P005 | Tucker 2026 | A | Slides (Census CES) | **Very high** (public-data template) | METHODS_VERIFIED |
| P006 | Hosseini & Lichtinger 2026 | A | Working paper (SSRN) | High | ABSTRACT_ONLY |
| P007 | Atkinson & Yamco 2026 | A | Fed article | Medium | FULL_TEXT_VERIFIED |
| P008 | Frank et al. 2026 | A | Preprint (arXiv) | High (timing threat) | ABSTRACT_ONLY |
| P009 | Iscenko & Curto Millet 2026 | A | Policy paper (EIG) | High (rate threat) | FULL_TEXT_VERIFIED |
| P010 | Humlum & Vestergaard 2025 | A | NBER WP | Medium | ABSTRACT_ONLY |
| P011 | Acemoglu et al. 2022 | A | Published (*JOLE*) | Low–medium | ABSTRACT_ONLY |
| P012 | Brynjolfsson, Li & Raymond 2025 | A | Published (*QJE*) | Low–medium | ABSTRACT_ONLY |
| P013 | Haurin 1991 | B | Published | Low | UNVERIFIED (title-level only) |
| P014 | Robst, Deitz & McGoldrick 1999 | B | Published | Low | UNVERIFIED (title-level only) |
| P015 | Diaz-Serrano 2005 | B | Published | Low | UNVERIFIED (title-level only) |
| P016 | Fisher & Gervais 2011 | B | Published (*IER*) | Medium | ABSTRACT_ONLY |
| P017 | Ortalo-Magné & Rady 2006 | B | Published (*REStud*) | Medium | ABSTRACT_ONLY |
| P018 | Kaplan 2012 | B | Published (*JPE*) | Medium | ABSTRACT_ONLY |
| P019 | Mezza et al. 2020 | B | Published (*JOLE*) | Medium | ABSTRACT_ONLY |
| P020 | Schwandt & von Wachter 2019 | B | Published (*JOLE*) | Low–medium | ABSTRACT_ONLY |
| P021 | Kuchler & Zafar 2019 | B | Published (*JF*) | Low–medium | ABSTRACT_ONLY |
| P022 | Ringo 2026 | B/C | Published (*REStat*) | High | METHODS_VERIFIED (FEDS) |
| P023 | Bhutta & Ringo 2021 | B/C | Published (*JME*) | High | METHODS_VERIFIED (FEDS) |
| P024 | Barrot et al. 2022 | B/C | Published (*JF*) | **Very high** (labor shock → HMDA, CZ) | METHODS_VERIFIED (FRBNY SR) |
| P025 | Mian & Sufi 2009 | C | Published (*QJE*) | High | METHODS_VERIFIED (NBER WP) |
| P026 | Avery, Brevoort & Canner 2007 | C | Published (*JRER*) | Medium | ABSTRACT_ONLY |
| P027 | Fuster et al. 2019 | C | Published (*RFS*) | High | METHODS_VERIFIED (NBER WP) |
| P028 | Bhutta, Hizmo & Ringo 2025 | C | Published (*JF*) | High | METHODS_VERIFIED (FEDS) |
| P029 | Buchak et al. 2018 | C | Published (*JFE*) | Medium | METHODS_VERIFIED (partial, NBER WP) |
| P030 | Gilje, Loutskina & Strahan 2016 | C | Published (*JF*) | Medium | METHODS_VERIFIED (NBER WP) |
| P031 | CFPB 2024 | C | Official report | High | METHODS_VERIFIED |
| P032 | Gete & Reher 2018 | C | Published (*RFS*) | Medium | ABSTRACT_ONLY |
| P033 | Ouazad & Kahn 2022 | C | **RETRACTED** (per Crossref) | — (excluded) | METHODS_VERIFIED (NBER WP), not used |
| P034 | Chu et al. 2026 | C/D | Working paper (SSRN) | Medium | ABSTRACT_ONLY |
| P035 | Li & Guo 2026 | D | Published (*FRL*) | **Very high** (competitor) | ABSTRACT_ONLY |
| P036 | Seagraves & Sirmans 2026 | D | Working paper (SSRN) | **Very high** (competitor) | ABSTRACT_ONLY (secondary) |
| P037 | Mondragon & Wieland 2022 | D | NBER WP | Medium | ABSTRACT_ONLY |
| P038 | Eisfeldt, Schubert & Zhang 2023 | D | NBER WP | Medium | ABSTRACT_ONLY |
| P039 | Fonseca & Liu 2024 | D | Published (*JF*) | Medium | ABSTRACT_ONLY |
| P040 | Dettling & Hsu 2018 | B | Published (*Labour Econ*) | Low | UNVERIFIED (title-level only) |
| P041 | Bleemer et al. 2021 | B | Published (*JUE*) | Low | UNVERIFIED (title-level only) |
| P042 | Oreopoulos, von Wachter & Heisz 2012 | B | Published (*AEJ: Applied*) | Low–medium | ABSTRACT_ONLY |

---

## 2. Paper-level blocks

### Stream A — GenAI exposure and labor outcomes

```yaml
P001:
  citation: "Eloundou, Tyna, Sam Manning, Pamela Mishkin, and Daniel Rock. 2024. 'GPTs Are GPTs: Labor Market Impact Potential of LLMs.' Science 384 (6702): 1306-1308."
  doi_url: "https://doi.org/10.1126/science.adj0998 ; arXiv:2303.10130 ; data https://github.com/openai/GPTs-are-GPTs"
  status: "Published"
  question: "Which occupations' tasks could LLMs (and LLM-powered software) materially speed up?"
  mechanism: "Task-level technological capability (potential exposure), not adoption"
  data: "O*NET task statements and detailed work activities; human annotators and GPT-4 ratings; BLS employment for aggregation"
  geography: "US (occupation level)"
  period: "Ratings produced 2023"
  unit: "O*NET-SOC occupation (8-digit), task"
  exposure: "E1 direct (LLM cuts time >=50%), E2 with LLM-powered tools; alpha=E1, beta=E1+0.5*E2, zeta=E1+E2"
  outcomes: "Exposure scores"
  identification: "Not causal; measurement"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "About 80% of US workers could have at least 10% of tasks affected; about 19% at least 50% (arXiv abstract). GPT-4 and human ratings agree moderately (Table 2)."
  causal_interpretation: "Capability exposure; says nothing about realized displacement"
  limitations: "Rubric- and model-dependent; static (2023 capabilities); task-to-occupation aggregation"
  relevance: "Primary exposure measure (dv_rating_beta), as in P004 and P005"
  location: "arXiv v. Sec. 3 (rubric, E0/E1/E2), Table 2 (agreement); occ_level.csv columns verified"
  verification: "FULL_TEXT_VERIFIED (arXiv version); data schema verified"
P002:
  citation: "Felten, Edward, Manav Raj, and Robert Seamans. 2021. 'Occupational, Industry, and Geographic Exposure to Artificial Intelligence: A Novel Dataset and Its Potential Uses.' Strategic Management Journal 42 (12): 2195-2217."
  doi_url: "https://doi.org/10.1002/smj.3286 ; data https://github.com/AIOE-Data/AIOE"
  status: "Published"
  question: "Construct and validate occupational (AIOE), industry (AIIE) and county (AIGE) AI exposure"
  mechanism: "AI abilities mapped to occupational abilities"
  data: "n.v. (EFF AI progress metrics; O*NET abilities per authors' description, not verified)"
  geography: "US; county for AIGE (abstract)"
  period: "n.v."
  unit: "Occupation; industry; county"
  exposure: "AIOE; later language-modeling variant (repository file 'Language Modeling AIOE and AIIE.xlsx')"
  outcomes: "Exposure indices"
  identification: "Measurement"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "Abstract: creates and validates AIOE, AIIE, AIGE"
  causal_interpretation: "n/a"
  limitations: "Pre-LLM AI abilities in the original index"
  relevance: "Robustness exposure (LM-AIOE)"
  location: "Repository file list verified via GitHub API"
  verification: "ABSTRACT_ONLY (OpenAlex)"
P003:
  citation: "Handa, Kunal, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah Heck, Jared Mueller, Jerry Hong, Stuart Ritchie, Tim Belonax, Kevin K. Troy, Dario Amodei, Jared Kaplan, Jack Clark, and Deep Ganguli. 2025. 'Which Economic Tasks Are Performed with AI? Evidence from Millions of Claude Conversations.' arXiv:2503.04761."
  doi_url: "https://arxiv.org/abs/2503.04761 ; data https://huggingface.co/datasets/Anthropic/EconomicIndex"
  status: "Preprint"
  question: "Which O*NET tasks and occupations is AI actually used for?"
  mechanism: "Observed usage; automation vs augmentation"
  data: "Over four million Claude.ai conversations (privacy-preserving analysis) mapped to O*NET tasks"
  geography: "Usage (not geographic)"
  period: "Usage data from about 2024-2025 releases"
  unit: "Task / occupation"
  exposure: "Usage shares; automative vs augmentative"
  outcomes: "Usage distribution"
  identification: "Descriptive"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "Usage concentrates in particular task families (abstract)"
  causal_interpretation: "n/a"
  limitations: "One platform; usage is post-treatment"
  relevance: "Heterogeneity only (automation vs augmentation), as in P004 Fact 5"
  location: "p. 1 (abstract, authors)"
  verification: "ABSTRACT_ONLY"
P004:
  citation: "Brynjolfsson, Erik, Bharat Chandar, and Ruyu Chen. 2026. 'Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence.' Working paper, Stanford Digital Economy Lab, August 2026 version."
  doi_url: "https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf"
  status: "Working paper (earlier versions Aug 2025, Nov 2025)"
  question: "Has GenAI affected employment, especially for early-career workers in exposed occupations?"
  mechanism: "Automation of codified entry-level tasks; reduced hiring of young workers"
  data: "ADP administrative payroll (millions of workers, through June 2026); benchmarks CPS, ACS; Tucker QWI"
  geography: "US (ADP client firms)"
  period: "Jan 2018 - Jun 2026 (balanced-firm samples since 2018 or 2021)"
  unit: "Occupation x age group x month; firm x quintile x month (Poisson)"
  exposure: "Eloundou GPT-4 beta quintiles (main); Anthropic Economic Index automation/augmentation; alternatives in App. E"
  outcomes: "Employment headcount; hires vs separations; base compensation"
  identification: "Descriptive long differences Nov 2022 -> Jun 2026; within-firm Poisson event studies with firm-time and firm-quintile FE"
  fixed_effects: "Firm x time, firm x quintile (App. C.6)"
  standard_errors: "Heteroskedasticity-robust (long differences); clustered by firm (Poisson); SOC3 clustering similar (fn. 16)"
  findings: "Ages 22-25 in exposed occupations 19% below kept-pace counterfactual. Table 1 Panel A Q5 vs Q1: 22-25 -0.179 (0.036); 26-30 -0.048 (0.033); 31-34 -0.014 (0.030); 35-40 0.001 (0.031). Panel F (all controls): 22-25 -0.080 (0.057). Via hiring; no base-pay adjustment. ACS gap 2022-24 -0.022 [-0.055, 0.011] vs ADP -0.132."
  causal_interpretation: "Authors: 'early, descriptive indicators ... rather than causal estimates'"
  limitations: "ADP sample representativeness; pre-trends around COVID; attenuation with education; larger than national survey benchmarks"
  relevance: "Defines the affected age group, the exposure measure and the comparison group; key evidence on dilution in 26-34"
  location: "Abstract p. 1; Sec. 1.2 (exposure aggregation to 6-digit SOC); Table 1 p. 13; Sec. 2.6 (pay); Sec. 5 pp. 28-29 (ACS); App. C.6 eq. C.1 (Poisson, citing Chen & Roth)"
  verification: "FULL_TEXT_VERIFIED"
P005:
  citation: "Tucker, Lee. 2026. 'You're (Not) Hired: Artificial Intelligence and Early Career Hiring in the Quarterly Workforce Indicators.' Presentation slides, U.S. Census Bureau, Center for Economic Studies, April 17, 2026."
  doi_url: "https://leetucker.net/docs/ai_sge_2026/"
  status: "Slides (no paper version found); author disclaimer that views are not the Census Bureau's"
  question: "Do public QWI data show early-career employment declines in AI-exposed industries after ChatGPT?"
  mechanism: "Reduced early-career hiring"
  data: "QWI (45 states, through 2025q2, private, excl. NAICS 92); ACS 2015-2019 PUMS crosswalk; BTOS validation; Bauer-Swanson monetary shocks"
  geography: "Industry x state"
  period: "Through 2025q2; reference 2022q4 (stocks) / 2022q3 (flows)"
  unit: "Industry x state x age x quarter"
  exposure: "Eloundou GPT-4 exposure aggregated to industry-states via ACS; top quintile indicator"
  outcomes: "Log employment, hires, separations, earnings growth, job gains/losses"
  identification: "Event study (industry-state and time FE); triple difference vs older ages; local projections for monetary sensitivity"
  fixed_effects: "Industry x state; time"
  standard_errors: "n.v. (not stated in slides)"
  findings: "Ages 22-24 employment -15% (-159k) over 10 quarters; hires -9% immediately; no similar decline at 25+; monetary policy explains about 1/4 of the gap; early-career substitution possibly began with COVID"
  causal_interpretation: "Descriptive / event-study; monetary confound partially addressed"
  limitations: "Crosswalk loses variance (0.045 -> 0.015); about 1% cell censoring; establishment imputation; no SEs reported in text"
  relevance: "Template for the QWI first stage; reference-quarter convention"
  location: "Slides: data, equations, results, limitations sections"
  verification: "METHODS_VERIFIED"
P006:
  citation: "Hosseini Maasoum, Seyed M., and Guy Lichtinger. 2026. 'Generative AI as Seniority-Biased Technological Change: Evidence from U.S. Resume and Job Posting Data.' Working paper, May 6, 2026 version (first version August 31, 2025). SSRN 5425555."
  doi_url: "https://doi.org/10.2139/ssrn.5425555"
  status: "Working paper"
  question: "Does GenAI adoption reduce demand for junior relative to senior workers?"
  mechanism: "Task displacement and labor-saving productivity gains for junior roles"
  data: "Resume data (65 million workers, more than 280,000 firms, 2015-2025); job postings (GenAI integrator roles)"
  geography: "US firms"
  period: "2015-2025"
  unit: "Firm x seniority x time"
  exposure: "Firm adoption (GenAI integrator postings); occupational exposure for heterogeneity"
  outcomes: "Junior/senior employment; hires; separations"
  identification: "DiD adopters vs non-adopters (per abstract)"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Junior employment declines sharply at adopters; senior trends largely unchanged; via slower hiring; concentrated in exposed occupations"
  causal_interpretation: "Relies on adoption timing being exogenous to junior-demand trends"
  limitations: "Adoption proxy; resume-data coverage"
  relevance: "Corroborates the hiring margin for juniors"
  location: "PDF p. 1 abstract"
  verification: "ABSTRACT_ONLY (abstract read from full-text PDF)"
P007:
  citation: "Atkinson, Tyler, and Shane Yamco. 2026. 'Young Workers' Employment Drops in Occupations with High AI Exposure.' Dallas Fed Economics, Federal Reserve Bank of Dallas, January 6, 2026."
  doi_url: "https://www.dallasfed.org/research/economics/2026/0106"
  status: "Federal Reserve article"
  question: "Does CPS show young-worker employment drops in AI-exposed occupations?"
  mechanism: "Reduced job finding for entrants"
  data: "CPS public microdata"
  geography: "US"
  period: "to Sep 2025"
  unit: "Age x exposure tertile x month (12-month moving averages)"
  exposure: "Eloundou scores, tertiles fixed on 2024 employment weights"
  outcomes: "Employment shares; layoffs; job-finding rates"
  identification: "Descriptive"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "Young most-exposed employment share 16.4% -> 15.5% (Nov 2022 -> Sep 2025); no rise in layoffs; entrants' job finding down >3 pp from Nov 2023 peak; about 0.1 pp aggregate unemployment"
  causal_interpretation: "Not causal (authors note education as a possible confounder)"
  limitations: "Small CPS cells"
  relevance: "Independent public-data corroboration of the hiring margin"
  location: "Web article"
  verification: "FULL_TEXT_VERIFIED"
P008:
  citation: "Frank, Morgan R., Alireza Javadian Sabet, Lisa Simon, Sarah H. Bana, and Renzhe Yu. 2026. 'AI-Exposed Jobs Deteriorated before ChatGPT.' arXiv:2601.02554."
  doi_url: "https://arxiv.org/abs/2601.02554"
  status: "Preprint (v1, Jan 5, 2026)"
  question: "Did AI-exposed jobs deteriorate only after ChatGPT?"
  mechanism: "Pre-existing forces (timing test)"
  data: "Monthly US unemployment insurance records; LinkedIn profiles; university syllabi"
  geography: "US; occupation x location"
  period: "Around 2021-2024"
  unit: "Occupation x location x month; graduate cohorts"
  exposure: "AI-exposed occupations and curricula (measure n.v.)"
  outcomes: "Unemployment risk; entry into exposed jobs; first-job pay; search duration"
  identification: "Descriptive timing"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Risk rose in AI-exposed occupations from early 2022, before ChatGPT; 2021+ cohorts entered exposed jobs at lower rates; AI-exposed coursework associated with better outcomes after ChatGPT"
  causal_interpretation: "Challenges the attribution of the decline to ChatGPT"
  limitations: "n.v."
  relevance: "Key timing threat; motivates the 2022-break diagnostic"
  location: "PDF p. 1 abstract"
  verification: "ABSTRACT_ONLY"
P009:
  citation: "Iscenko, Zanna, and Fabien Curto Millet. 2026. 'Looking for the Ladder: Is AI Impacting Entry-Level Jobs?' Economic Innovation Group, January 2026."
  doi_url: "https://eig.org/wp-content/uploads/2026/01/TAWP-Iscenko-Millet.pdf"
  status: "Policy paper (authors employed by Google, disclosed)"
  question: "Is the entry-level decline due to AI or to monetary policy?"
  mechanism: "Interest-rate sensitivity of exposed sectors"
  data: "Lightcast job postings (238 million, per secondary coverage); Census BTOS; LinkedIn hiring statistics"
  geography: "US"
  period: "2019-2025"
  unit: "Occupation x month (postings)"
  exposure: "AI exposure quintiles"
  outcomes: "Job postings; entry-level hiring"
  identification: "Timing comparison; descriptive"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "Decline starts March 2022 with tightening; about 38% of top-quintile workers in Information, Finance & Insurance, Prof./Tech. services vs <2% in bottom quintile; exposed postings also fell more in the early-2020 slowdown"
  causal_interpretation: "Argues against AI attribution; not a formal design"
  limitations: "Postings are not employment; descriptive"
  relevance: "Main rate confound (A2) for both labor and housing outcomes"
  location: "pp. 1, 5-6"
  verification: "FULL_TEXT_VERIFIED"
P010:
  citation: "Humlum, Anders, and Emilie Vestergaard. 2025. 'Large Language Models, Small Labor Market Effects.' NBER Working Paper 33777. (Crossref lists the current title as 'Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI'.)"
  doi_url: "https://doi.org/10.3386/w33777"
  status: "NBER WP"
  question: "Labor-market effects of AI chatbots"
  mechanism: "Adoption -> productivity -> wages and hours"
  data: "Two adoption surveys (late 2023, 2024; 25,000 workers, 7,000 workplaces) linked to Danish matched employer-employee data"
  geography: "Denmark"
  period: "2023-2024"
  unit: "Worker; workplace"
  exposure: "11 exposed occupations; adoption; employer policies"
  outcomes: "Earnings; recorded hours"
  identification: "DiD; employer policies as quasi-experimental variation"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Precise zeros; CIs rule out effects >1% (OpenAlex abstract)"
  causal_interpretation: "Quasi-experimental"
  limitations: "Denmark; incumbents rather than entrants"
  relevance: "Counter-evidence on realized earnings effects"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P011:
  citation: "Acemoglu, Daron, David Autor, Jonathon Hazell, and Pascual Restrepo. 2022. 'Artificial Intelligence and Jobs: Evidence from Online Vacancies.' Journal of Labor Economics 40 (S1): S293-S340."
  doi_url: "https://doi.org/10.1086/718327"
  status: "Published"
  question: "Effect of (pre-LLM) AI on labor markets"
  mechanism: "AI-labor substitution at the establishment level"
  data: "Near-universe of US online vacancies, 2010 onward"
  geography: "US"
  period: "2010-2018"
  unit: "Establishment"
  exposure: "Task compatibility with AI"
  outcomes: "AI and non-AI hiring; skill requirements"
  identification: "Exposure-based"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Exposed establishments reduce non-AI hiring; aggregate occupation/industry effects too small to detect"
  causal_interpretation: "Exposure design"
  limitations: "Pre-LLM"
  relevance: "Historical precedent: establishment-level effects can be invisible in aggregates"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P012:
  citation: "Brynjolfsson, Erik, Danielle Li, and Lindsey Raymond. 2025. 'Generative AI at Work.' Quarterly Journal of Economics 140 (2): 889-942."
  doi_url: "https://doi.org/10.1093/qje/qjae044"
  status: "Published"
  question: "Productivity effects of a GenAI assistant"
  mechanism: "Complementarity; diffusion of best practices"
  data: "5,172 customer-support agents"
  geography: "Firm"
  period: "n.v."
  unit: "Agent"
  exposure: "Staggered access to AI assistant"
  outcomes: "Issues resolved per hour; quality"
  identification: "Staggered rollout"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "+15% productivity on average; largest gains for less experienced/lower-skilled agents"
  causal_interpretation: "Within-firm quasi-experiment"
  limitations: "One firm and occupation"
  relevance: "Complementarity channel; productivity gains for novices do not imply more junior hiring"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
```

### Stream B — Income risk, constraints and housing

```yaml
P013:
  citation: "Haurin, Donald R. 1991. 'Income Variability, Homeownership, and Housing Demand.' Journal of Housing Economics 1 (1): 60-74."
  doi_url: "https://doi.org/10.1016/S1051-1377(05)80025-7"
  status: "Published"
  question: "Income variability and tenure/housing demand (from title)"
  mechanism: "Income risk"
  data: "n.v."
  geography: "n.v."
  period: "n.v."
  unit: "n.v."
  exposure: "n.v."
  outcomes: "n.v."
  identification: "n.v."
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "n.v."
  causal_interpretation: "n.v."
  limitations: "n.v."
  relevance: "Background citation on income variability and tenure"
  location: "n.v."
  verification: "UNVERIFIED (bibliographic metadata via Crossref only; no abstract)"
P014:
  citation: "Robst, John, Richard Deitz, and KimMarie McGoldrick. 1999. 'Income Variability, Uncertainty and Housing Tenure Choice.' Regional Science and Urban Economics 29 (2): 219-229."
  doi_url: "https://doi.org/10.1016/S0166-0462(98)00031-3"
  status: "Published"
  question: "Income variability and tenure choice (from title)"
  mechanism: "Income risk"
  data: "n.v."
  geography: "n.v."
  period: "n.v."
  unit: "n.v."
  exposure: "n.v."
  outcomes: "n.v."
  identification: "n.v."
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "n.v."
  causal_interpretation: "n.v."
  limitations: "n.v."
  relevance: "Background"
  location: "n.v."
  verification: "UNVERIFIED (Crossref metadata only)"
P015:
  citation: "Diaz-Serrano, Luis. 2005. 'Labor Income Uncertainty, Skewness and Homeownership: A Panel Data Study for Germany and Spain.' Journal of Urban Economics 58 (1): 156-176."
  doi_url: "https://doi.org/10.1016/j.jue.2005.03.003"
  status: "Published"
  question: "Labor income uncertainty and homeownership (from title)"
  mechanism: "Income risk"
  data: "Panel data, Germany and Spain (from title)"
  geography: "Germany, Spain"
  period: "n.v."
  unit: "n.v."
  exposure: "n.v."
  outcomes: "n.v."
  identification: "n.v."
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "n.v."
  causal_interpretation: "n.v."
  limitations: "Non-US"
  relevance: "Background"
  location: "n.v."
  verification: "UNVERIFIED (Crossref metadata only)"
P016:
  citation: "Fisher, Jonas D. M., and Martin Gervais. 2011. 'Why Has Home Ownership Fallen among the Young?' International Economic Review 52 (3): 883-912."
  doi_url: "https://doi.org/10.1111/j.1468-2354.2011.00653.x"
  status: "Published"
  question: "Why did homeownership of households headed by 25-44-year-olds fall 1980-2000?"
  mechanism: "Later marriage; rising earnings risk"
  data: "Micro and macro evidence for calibration"
  geography: "US"
  period: "1980-2005"
  unit: "Model households"
  exposure: "Earnings risk"
  outcomes: "Young homeownership"
  identification: "Calibrated equilibrium life-cycle model"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "Rising earnings risk 'can easily account for' the decline beyond delayed marriage"
  causal_interpretation: "Model-based"
  limitations: "Structural assumptions"
  relevance: "Theory for mechanism M2 (risk delays ownership)"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P017:
  citation: "Ortalo-Magné, François, and Sven Rady. 2006. 'Housing Market Dynamics: On the Contribution of Income Shocks and Credit Constraints.' Review of Economic Studies 73 (2): 459-485."
  doi_url: "https://doi.org/10.1111/j.1467-937X.2006.383_1.x"
  status: "Published"
  question: "How do income shocks and credit constraints drive housing dynamics?"
  mechanism: "Down-payment constraint for young first-time buyers; property ladder"
  data: "UK and US evidence"
  geography: "UK, US"
  period: "n.v."
  unit: "Model"
  exposure: "Young households' income"
  outcomes: "Prices; transactions"
  identification: "Theory with empirical support"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "Young households' ability to afford the down payment is a powerful driver of the housing market"
  causal_interpretation: "Theory"
  limitations: "n.v."
  relevance: "Mechanism M1 (down payment); age-specific incidence of price shocks (05 Sec. 4)"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P018:
  citation: "Kaplan, Greg. 2012. 'Moving Back Home: Insurance against Labor Market Risk.' Journal of Political Economy 120 (3): 446-512."
  doi_url: "https://doi.org/10.1086/666588"
  status: "Published"
  question: "Is co-residence with parents insurance against labor-market risk?"
  mechanism: "Moving home after adverse labor events"
  data: "Monthly panel data"
  geography: "US"
  period: "n.v."
  unit: "Youth"
  exposure: "Labor-market events"
  outcomes: "Co-residence; earnings growth"
  identification: "Estimated dynamic game"
  fixed_effects: "n/a"
  standard_errors: "n.v."
  findings: "The option to live at home is valuable insurance, especially for low-skilled youth"
  causal_interpretation: "Structural"
  limitations: "n.v."
  relevance: "Channel by which entry-level shocks delay household formation and purchases"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P019:
  citation: "Mezza, Alvaro, Daniel Ringo, Shane Sherlund, and Kamila Sommer. 2020. 'Student Loans and Homeownership.' Journal of Labor Economics 38 (1): 215-260."
  doi_url: "https://doi.org/10.1086/704609"
  status: "Published"
  question: "Effect of student debt on homeownership"
  mechanism: "Debt burden, DTI, down payment"
  data: "Administrative data for a nationally representative cohort"
  geography: "US"
  period: "n.v."
  unit: "Individual"
  exposure: "Student debt instrumented by in-state tuition changes"
  outcomes: "Homeownership"
  identification: "IV"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "+$1,000 debt lowers homeownership by about 1.8 pp in the mid-20s (about 4 months delay)"
  causal_interpretation: "IV"
  limitations: "n.v."
  relevance: "Confounder A5 (student-loan restart) and the DTI channel for the young"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P020:
  citation: "Schwandt, Hannes, and Till von Wachter. 2019. 'Unlucky Cohorts: Estimating the Long-Term Effects of Entering the Labor Market in a Recession in Large Cross-Sectional Data Sets.' Journal of Labor Economics 37 (S1): S161-S198."
  doi_url: "https://doi.org/10.1086/701046"
  status: "Published"
  question: "Persistent effects of entry conditions"
  mechanism: "Scarring"
  data: "US labor force surveys 1976-2015"
  geography: "US (state x cohort)"
  period: "1976-2015"
  unit: "Cohort x state"
  exposure: "Unemployment at entry"
  outcomes: "Earnings; wages"
  identification: "Entry-condition variation"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Persistent earnings and wage reductions, especially for less advantaged entrants"
  causal_interpretation: "Quasi-experimental"
  limitations: "n.v."
  relevance: "Cohort-scarring prediction for 2023-25 entrants"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P021:
  citation: "Kuchler, Theresa, and Basit Zafar. 2019. 'Personal Experiences and Expectations about Aggregate Outcomes.' Journal of Finance 74 (5): 2491-2542."
  doi_url: "https://doi.org/10.1111/jofi.12819"
  status: "Published"
  question: "Do personal experiences shape expectations?"
  mechanism: "Extrapolation from personal and local experience"
  data: "Survey data"
  geography: "US"
  period: "n.v."
  unit: "Individual"
  exposure: "Local house prices; own unemployment"
  outcomes: "Expectations"
  identification: "Within-individual variation"
  fixed_effects: "Individual (implied by within-individual design)"
  standard_errors: "n.v."
  findings: "Personal unemployment makes individuals more pessimistic about national unemployment"
  causal_interpretation: "Within-person"
  limitations: "n.v."
  relevance: "Indirect support for M2 (expectations)"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P022:
  citation: "Ringo, Daniel. 2026. 'Monetary Policy and Home Buying Inequality.' Review of Economics and Statistics 108: 1052-1066. (FEDS 2023-006.)"
  doi_url: "https://doi.org/10.1162/rest_a_01445 ; https://doi.org/10.17016/FEDS.2023.006"
  status: "Published"
  question: "Does monetary policy change who buys homes?"
  mechanism: "Payment-to-income constraints bind more for lower-income and first-time buyers"
  data: "Optimal Blue rate locks merged to confidential HMDA (application and origination dates)"
  geography: "US"
  period: "Through 2019; 212 monetary-policy shocks (Swanson 2021); >90M purchase loans"
  unit: "Loan / rate lock"
  exposure: "High-frequency monetary-policy shocks"
  outcomes: "LMI share of buyers; first-time-buyer heterogeneity"
  identification: "Rate-lock timing around policy shocks"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "+1 pp policy-induced mortgage-rate rise lowers lower-income households' presence among buyers by 1-2 pp; stronger for first-time buyers; persists about one year"
  causal_interpretation: "High-frequency identification"
  limitations: "Pre-2020 sample"
  relevance: "Age/first-time-specific incidence of the 2022 rate shock (confounder A2); HMDA sample definition"
  location: "FEDS p. 13 (data); Table notes p. 31 (HMDA sample: first-lien, purchase, owner-occupied, income 0-1M)"
  verification: "METHODS_VERIFIED (FEDS version); abstract of published version (OpenAlex)"
P023:
  citation: "Bhutta, Neil, and Daniel Ringo. 2021. 'The Effect of Interest Rates on Home Buying: Evidence from a Shock to Mortgage Insurance Premiums.' Journal of Monetary Economics 118: 195-211. (FEDS 2017-086.)"
  doi_url: "https://doi.org/10.1016/j.jmoneco.2020.10.001"
  status: "Published"
  question: "Effect of interest rates on home buying"
  mechanism: "DTI limits amplify rate effects"
  data: "Confidential HMDA with application dates; Optimal Blue; McDash"
  geography: "US"
  period: "2014-2015 (FHA MIP cut, Jan 2015)"
  unit: "Application / loan (weekly)"
  exposure: "FHA-likely borrowers; 50 bp MIP cut"
  outcomes: "Purchase originations; denial; DTI denial reasons; house prices (area FHA share x post)"
  identification: "RD in application week; application-level denial comparisons"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "About +14% purchase originations among FHA-likely borrowers; no response among high-income; DTI cited in 31% of denied FHA purchase applications with a reason (2014)"
  causal_interpretation: "RD"
  limitations: "Short window"
  relevance: "DTI channel; FHA-reliant first-time buyers (about 80% of FHA loans to first-time buyers, 2014) -> confounder A6"
  location: "FEDS pp. 4-5 (FHA/first-time; DTI amplification), 13-14 (data), 22-24 (denial), 28 (FHA share x post)"
  verification: "METHODS_VERIFIED (FEDS version)"
P024:
  citation: "Barrot, Jean-Noël, Erik Loualiche, Matthew Plosser, and Julien Sauvagnat. 2022. 'Import Competition and Household Debt.' Journal of Finance 77 (6): 3037-3091. (FRBNY Staff Report 821, 2017.)"
  doi_url: "https://doi.org/10.1111/jofi.13185 ; https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr821.pdf"
  status: "Published"
  question: "How do local labor-market (trade) shocks affect household balance sheets?"
  mechanism: "Income shock -> borrowing to smooth consumption via home-equity extraction"
  data: "FRBNY CCP/Equifax; HMDA; PSID; Census"
  geography: "US commuting zones"
  period: "2000-2007"
  unit: "CZ; individual (CCP)"
  exposure: "Industry shipping costs x initial CZ industry mix"
  outcomes: "Household debt; HMDA log applications and originations (purchase, refi); HMDA denial rates"
  identification: "Shift-share exposure; cross-sectional long differences"
  fixed_effects: "CZ controls (1998), Census controls"
  standard_errors: "n.v."
  findings: "Household debt rises more in exposed regions, via equity extraction where prices grew; HMDA denial rates higher in exposed CZs, read as higher demand"
  causal_interpretation: "Shift-share exogeneity of shipping costs"
  limitations: "Pre-2018 HMDA (no age)"
  relevance: "Closest labor-shock -> HMDA template at CZ level; competing prediction (labor shock can raise borrowing)"
  location: "SR 821: p. 19 (denial interpretation); Table A.4 p. 54 (CZ, 733 obs., population weights); tables pp. 46, 53"
  verification: "METHODS_VERIFIED (SR version); published abstract via OpenAlex"
P040:
  citation: "Dettling, Lisa J., and Joanne W. Hsu. 2018. 'Returning to the Nest: Debt and Parental Co-residence among Young Adults.' Labour Economics 54: 225-236."
  doi_url: "https://doi.org/10.1016/j.labeco.2017.12.006"
  status: "Published"
  question: "Debt and parental co-residence (from title)"
  mechanism: "Debt -> co-residence"
  data: "n.v."
  geography: "n.v."
  period: "n.v."
  unit: "n.v."
  exposure: "n.v."
  outcomes: "n.v."
  identification: "n.v."
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "n.v."
  causal_interpretation: "n.v."
  limitations: "n.v."
  relevance: "Background (household formation)"
  location: "n.v."
  verification: "UNVERIFIED (Crossref metadata only)"
P041:
  citation: "Bleemer, Zachary, Meta Brown, Donghoon Lee, Katherine Strair, and Wilbert van der Klaauw. 2021. 'Echoes of Rising Tuition in Students' Borrowing, Educational Attainment, and Homeownership in Post-Recession America.' Journal of Urban Economics 122: 103298."
  doi_url: "https://doi.org/10.1016/j.jue.2020.103298"
  status: "Published"
  question: "Tuition, borrowing and homeownership (from title)"
  mechanism: "Debt"
  data: "n.v."
  geography: "US"
  period: "Post-recession"
  unit: "n.v."
  exposure: "Tuition changes"
  outcomes: "Borrowing; attainment; homeownership"
  identification: "n.v."
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "n.v."
  causal_interpretation: "n.v."
  limitations: "n.v."
  relevance: "Background (A5)"
  location: "n.v."
  verification: "UNVERIFIED (Crossref metadata only)"
P042:
  citation: "Oreopoulos, Philip, Till von Wachter, and Andrew Heisz. 2012. 'The Short- and Long-Term Career Effects of Graduating in a Recession.' American Economic Journal: Applied Economics 4 (1): 1-29."
  doi_url: "https://doi.org/10.1257/app.4.1.1"
  status: "Published"
  question: "Earnings costs of graduating in a recession"
  mechanism: "Cyclical downgrading; slow mobility to better firms"
  data: "Longitudinal university-employer-employee data"
  geography: "n.v. (Canada, per the authors' data; not verified here)"
  period: "n.v."
  unit: "Graduate"
  exposure: "Unemployment at graduation"
  outcomes: "Earnings; employer quality"
  identification: "Entry-condition variation"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Persistent earnings declines lasting about ten years; larger for less advantaged graduates"
  causal_interpretation: "Quasi-experimental"
  limitations: "n.v."
  relevance: "Cohort scarring for affected entrants"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
```

### Stream C — HMDA-based empirical research

```yaml
P025:
  citation: "Mian, Atif, and Amir Sufi. 2009. 'The Consequences of Mortgage Credit Expansion: Evidence from the U.S. Mortgage Default Crisis.' Quarterly Journal of Economics 124 (4): 1449-1496. (NBER WP 13936.)"
  doi_url: "https://doi.org/10.1162/qjec.2009.124.4.1449"
  status: "Published"
  question: "Origins of the mortgage default crisis; credit supply vs income"
  mechanism: "Credit-supply expansion to subprime ZIP codes"
  data: "Public HMDA 1996-2006; Equifax; IRS ZIP income"
  geography: "US ZIP codes (major metros)"
  period: "1996-2007"
  unit: "ZIP code (within county)"
  exposure: "1996 share of subprime borrowers / HMDA denial rate (latent demand)"
  outcomes: "Mortgage originations for home purchase; mortgage debt-to-income; defaults"
  identification: "Within-county comparisons of ZIPs"
  fixed_effects: "County"
  standard_errors: "n.v."
  findings: "Credit expanded to subprime ZIPs 2002-2005 despite declining relative income growth"
  causal_interpretation: "Supply interpretation via the negative income-credit correlation"
  limitations: "Pre-2018 HMDA"
  relevance: "Area-level HMDA outcome construction; denial rate as an area characteristic"
  location: "NBER WP pp. 10, 13-14, 20, 23; Table p. 47"
  verification: "METHODS_VERIFIED (NBER WP)"
P026:
  citation: "Avery, Robert B., Kenneth P. Brevoort, and Glenn B. Canner. 2007. 'Opportunities and Issues in Using HMDA Data.' Journal of Real Estate Research 29 (4): 351-380."
  doi_url: "https://doi.org/10.1080/10835547.2007.12091206"
  status: "Published"
  question: "Practical issues researchers face with HMDA"
  mechanism: "n/a (methodology)"
  data: "HMDA"
  geography: "US"
  period: "Pre-2007 HMDA"
  unit: "n/a"
  exposure: "n/a"
  outcomes: "n/a"
  identification: "n/a"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "Comprehensive enumeration of HMDA data issues (abstract)"
  causal_interpretation: "n/a"
  limitations: "Pre-2018 schema; details not read"
  relevance: "General methodological reference; specific claims not used"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P027:
  citation: "Fuster, Andreas, Matthew Plosser, Philipp Schnabl, and James Vickery. 2019. 'The Role of Technology in Mortgage Lending.' Review of Financial Studies 32 (5): 1854-1899. (NBER WP 24500.)"
  doi_url: "https://doi.org/10.1093/rfs/hhz018"
  status: "Published"
  question: "Do FinTech lenders differ in processing, supply elasticity, defaults?"
  mechanism: "Technology-based lending"
  data: "HMDA incl. restricted version (application and action dates); Ginnie Mae; CRISM"
  geography: "US; tract; county (top 500)"
  period: "2010-2016"
  unit: "Loan application; lender-month; county"
  exposure: "FinTech lender indicator; demand shocks"
  outcomes: "Processing time; denial; refinancing; market share"
  identification: "Within-tract comparisons; demand-shock elasticities"
  fixed_effects: "Lender, census tract, calendar month"
  standard_errors: "Tract-clustered (loan level); county-clustered (county regs); White-Huber (lender-month)"
  findings: "FinTech processes 20% faster without higher defaults; more elastic supply"
  causal_interpretation: "Conditional comparisons"
  limitations: "Pre-2018 coverage outside MSAs (robust to MSA-only)"
  relevance: "Application-level LPM template with lender FE; samples by action code"
  location: "NBER WP pp. 12 fn. 15, 33, 45, 53, 56-61"
  verification: "METHODS_VERIFIED (NBER WP)"
P028:
  citation: "Bhutta, Neil, Aurel Hizmo, and Daniel Ringo. 2025. 'How Much Does Racial Bias Affect Mortgage Lending? Evidence from Human and Algorithmic Credit Decisions.' Journal of Finance 80: 1463-1496. (FEDS 2022-067.)"
  doi_url: "https://doi.org/10.1111/jofi.13444"
  status: "Published"
  question: "How much do observable risk factors explain racial denial gaps?"
  mechanism: "Underwriting on credit score, leverage, AUS"
  data: "Confidential HMDA 2018-2019 incl. credit score, AUS results; Ginnie Mae"
  geography: "US"
  period: "2018-2019"
  unit: "Application"
  exposure: "Applicant race/ethnicity"
  outcomes: "Denial; denial reasons"
  identification: "Conditional comparisons with fine risk bins; AUS recommendations"
  fixed_effects: "Risk-bin indicators; lender/program controls (n.v. in full)"
  standard_errors: "Clustered by lender and county"
  findings: "Observable risk factors explain most denial disparities; residual 1-2 pp partly due to unobserved risk"
  causal_interpretation: "Conditional"
  limitations: "Confidential data"
  relevance: "Shows public-HMDA conditional denial omits key risk variables; sample conventions (actions 1-3, full reporters, first-lien, site-built single-unit)"
  location: "FEDS pp. 10, 21, 25-27, 35; Table A.2 p. 37"
  verification: "METHODS_VERIFIED (FEDS version)"
P029:
  citation: "Buchak, Greg, Gregor Matvos, Tomasz Piskorski, and Amit Seru. 2018. 'Fintech, Regulatory Arbitrage, and the Rise of Shadow Banks.' Journal of Financial Economics 130 (3): 453-483. (NBER WP 23288.)"
  doi_url: "https://doi.org/10.1016/j.jfineco.2018.03.011"
  status: "Published"
  question: "Why did shadow banks grow?"
  mechanism: "Regulatory burden; technology"
  data: "HMDA; Fannie/Freddie loan-level"
  geography: "US counties"
  period: "2007-2015"
  unit: "Loan; county-time"
  exposure: "Regulatory shocks"
  outcomes: "Market shares; pricing"
  identification: "DiD with geographic exposure"
  fixed_effects: "County x time"
  standard_errors: "Clustered at county-year"
  findings: "Banks contracted where regulatory burden rose; shadow banks filled gaps"
  causal_interpretation: "DiD"
  limitations: "n.v."
  relevance: "Lender composition as a confounder; county x time FE practice"
  location: "NBER WP pp. 16, 38, 46"
  verification: "METHODS_VERIFIED (partial)"
P030:
  citation: "Gilje, Erik P., Elena Loutskina, and Philip E. Strahan. 2016. 'Exporting Liquidity: Branch Banking and Financial Integration.' Journal of Finance 71 (3): 1159-1184. (NBER WP 19403.)"
  doi_url: "https://doi.org/10.1111/jofi.12387"
  status: "Published"
  question: "Do branch networks integrate lending markets?"
  mechanism: "Liquidity windfalls (shale) -> lending in non-boom counties"
  data: "HMDA; Call Reports"
  geography: "US counties"
  period: "Shale-boom era"
  unit: "Bank x county x year"
  exposure: "Bank exposure to shale booms"
  outcomes: "Growth in mortgage originations; approval rates"
  identification: "Bank liquidity shocks with county x year FE"
  fixed_effects: "County x year"
  standard_errors: "Clustered by bank"
  findings: "Exposed banks increase hard-to-securitize lending in non-boom counties with branches"
  causal_interpretation: "Within-county across banks"
  limitations: "HMDA misses small/rural lenders (p. 13)"
  relevance: "Location x time FE practice; coverage caveat"
  location: "NBER WP pp. 13-14, 27, 36-41"
  verification: "METHODS_VERIFIED (NBER WP)"
P031:
  citation: "Consumer Financial Protection Bureau. 2024. '2023 Mortgage Market Activity and Trends.' December 2024."
  doi_url: "https://files.consumerfinance.gov/f/documents/cfpb_2023-mortgage-market-activity-and-trends_2024-12.pdf"
  status: "Official report"
  question: "Descriptive overview of 2023 HMDA"
  mechanism: "n/a"
  data: "2023 HMDA snapshot (as of May 1, 2024) and 2018-2022"
  geography: "US"
  period: "2018-2023"
  unit: "Records; tabulations"
  exposure: "n/a"
  outcomes: "Applications, originations, denial rates, characteristics by income/race"
  identification: "Descriptive"
  fixed_effects: "n/a"
  standard_errors: "n/a"
  findings: "2023 first year since 2019 with sub-100-loan reporters (fn. 7); reporters +14.6% vs 2022; IMCs originated 61.9% of closed-end purchase loans"
  causal_interpretation: "n/a"
  limitations: "No age tabulations found"
  relevance: "Official population conventions; threshold-change documentation"
  location: "pp. 4, 6, 7 (fn. 7), 8, 18-20"
  verification: "METHODS_VERIFIED"
P032:
  citation: "Gete, Pedro, and Michael Reher. 2018. 'Mortgage Supply and Housing Rents.' Review of Financial Studies 31 (12): 4884-4911."
  doi_url: "https://doi.org/10.1093/rfs/hhx145"
  status: "Published"
  question: "Did the post-2008 mortgage-supply contraction raise rents?"
  mechanism: "Tighter lending -> rental demand"
  data: "n.v. (HMDA use not verified)"
  geography: "MSAs"
  period: "2010-2014"
  unit: "MSA"
  exposure: "MSA exposure to lender regulatory shocks"
  outcomes: "Rents; homeownership; rental supply"
  identification: "Shift-share-type exposure"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Tighter standards raised rents and depressed homeownership"
  causal_interpretation: "Exposure design"
  limitations: "n.v."
  relevance: "Credit-supply shock design at MSA level"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P033:
  citation: "Ouazad, Amine, and Matthew E. Kahn. 2022. 'Mortgage Finance and Climate Change: Securitization Dynamics in the Aftermath of Natural Disasters.' Review of Financial Studies 35 (8): 3617-3665."
  doi_url: "https://doi.org/10.1093/rfs/hhab124"
  status: "RETRACTED (Crossref title carries 'RETRACTED:')"
  question: "n/a"
  mechanism: "n/a"
  data: "HMDA (NBER WP 26322)"
  geography: "n/a"
  period: "n/a"
  unit: "n/a"
  exposure: "n/a"
  outcomes: "n/a"
  identification: "n/a"
  fixed_effects: "n/a"
  standard_errors: "WP: double-clustered by ZIP and year"
  findings: "NOT USED"
  causal_interpretation: "NOT USED"
  limitations: "Retracted"
  relevance: "Excluded from evidence; listed for transparency"
  location: "NBER WP pp. 11-12, 23"
  verification: "Bibliographic + retraction flag verified"
P034:
  citation: "Chu, Yongqiang, Jing (Jade) He, Leiju Qiu, and Daxuan Zhao. 2026. 'Artificial Intelligence and the Racial Gap in Mortgage Lending.' SSRN Working Paper 6342658."
  doi_url: "https://doi.org/10.2139/ssrn.6342658"
  status: "Working paper"
  question: "Does bank AI adoption change racial gaps in lending?"
  mechanism: "Algorithmic underwriting"
  data: "HMDA 2022-2024; bank AI adoption from job postings"
  geography: "US"
  period: "2022-2024"
  unit: "Application / bank-year"
  exposure: "Bank AI-skill intensity; IV with AI-graduate supply"
  outcomes: "Denial and interest-rate gaps"
  identification: "IV"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "+1 SD adoption widens denial gap by 0.75 pp and rate gap by about 4 bp; concentrated in purchase loans"
  causal_interpretation: "IV"
  limitations: "n.v."
  relevance: "Lender-side AI is a distinct channel that could move denial outcomes"
  location: "Abstract (search-engine summary)"
  verification: "ABSTRACT_ONLY"
```

### Stream D — AI, housing and household finance

```yaml
P035:
  citation: "Li, Sen, and Chunyu Guo. 2026. 'Impact of Generative AI on Local Housing Values through AI Exposure.' Finance Research Letters 108: 110442."
  doi_url: "https://doi.org/10.1016/j.frl.2026.110442"
  status: "Published (October 2026 issue)"
  question: "Does GenAI affect local housing markets through occupational AI exposure?"
  mechanism: "Supply-side (fewer new listings); labor-market uncertainty discussed"
  data: "Zillow; Redfin"
  geography: "US counties"
  period: "July 2021 - June 2024"
  unit: "County x month (n.v.)"
  exposure: "County occupational AI exposure"
  outcomes: "Home values; new listings; sale-to-list ratios"
  identification: "Continuous DiD around ChatGPT release"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Higher home-value growth and fewer new listings in exposed counties; no comparable buyer-side increase"
  causal_interpretation: "Continuous DiD"
  limitations: "Short post window; full text not accessed"
  relevance: "Closest competitor (housing); price channel A1"
  location: "Abstract (search-engine summary; ScienceDirect 403)"
  verification: "ABSTRACT_ONLY"
P036:
  citation: "Seagraves, Cayman, and Stace Sirmans. 2026. 'AI Exposure and Housing Markets.' SSRN Working Paper 6749481."
  doi_url: "https://doi.org/10.2139/ssrn.6749481"
  status: "Working paper (2 SSRN versions)"
  question: "Did AI exposure affect metro house prices?"
  mechanism: "Demand from AI-complement workers; reduced outmigration"
  data: "Zillow ZHVI; FHFA; IRS migration; Revelio LinkedIn"
  geography: "211 US metros"
  period: "2017Q1-2025Q4"
  unit: "Metro x quarter"
  exposure: "Population-weighted (2019) AI exposure; LLM task-suitability index"
  outcomes: "House-price growth; migration; AI hiring"
  identification: "Exposure x post; placebo (WFH)"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "+1 SD exposure -> +3.6% cumulative ZHVI growth (about $9,400); concentrated in supply-inelastic metros; WFH placebo opposite sign"
  causal_interpretation: "Exposure design"
  limitations: "Abstract seen only through secondary summary (SSRN 403)"
  relevance: "Closest competitor; price channel A1"
  location: "Abstract"
  verification: "ABSTRACT_ONLY (secondary; Crossref confirms title and authors)"
P037:
  citation: "Mondragon, John, and Johannes Wieland. 2022. 'Housing Demand and Remote Work.' NBER Working Paper 30041."
  doi_url: "https://doi.org/10.3386/w30041"
  status: "NBER WP"
  question: "Did remote work raise housing demand and prices?"
  mechanism: "Home-space demand"
  data: "n.v. (metro remote-work exposure; prices; rents)"
  geography: "US metros"
  period: "2019-2023"
  unit: "Metro"
  exposure: "Remote-work exposure"
  outcomes: "House prices; rents"
  identification: "Cross-metro exposure with migration-spillover controls"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "Remote work explains over half of the 18.9% real house-price increase 2019-2023"
  causal_interpretation: "Exposure design + model-based aggregation"
  limitations: "n.v."
  relevance: "Template for exposure -> housing; confounder A4"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P038:
  citation: "Eisfeldt, Andrea L., Gregor Schubert, and Miao Ben Zhang. 2023. 'Generative AI and Firm Values.' NBER Working Paper 31222."
  doi_url: "https://doi.org/10.3386/w31222"
  status: "NBER WP"
  question: "Effect of GenAI on firm values"
  mechanism: "Workforce exposure -> expected productivity"
  data: "US public firms; earnings calls"
  geography: "US"
  period: "Around ChatGPT release"
  unit: "Firm"
  exposure: "Firm workforce GenAI exposure"
  outcomes: "Stock returns"
  identification: "Event-time portfolio returns"
  fixed_effects: "n/a"
  standard_errors: "n.v."
  findings: "Higher-exposure firms earned 0.4% higher daily excess returns after ChatGPT"
  causal_interpretation: "Event study"
  limitations: "n.v."
  relevance: "Wealth channel for equity-holding incumbents (A1/A8)"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
P039:
  citation: "Fonseca, Julia, and Lu Liu. 2024. 'Mortgage Lock-In, Mobility, and Labor Reallocation.' Journal of Finance 79 (6): 3729-3772."
  doi_url: "https://doi.org/10.1111/jofi.13398"
  status: "Published"
  question: "Do rising rates lock in mortgagors?"
  mechanism: "Locked-in low rates reduce moving"
  data: "Individual credit records"
  geography: "US"
  period: "Including 2022-2024"
  unit: "Individual"
  exposure: "Locked rate vs current rate"
  outcomes: "Moving; labor reallocation"
  identification: "Timing of origination"
  fixed_effects: "n.v."
  standard_errors: "n.v."
  findings: "1 pp smaller rate gap reduces moving by 9% overall and 16% in 2022-2024"
  causal_interpretation: "Quasi-experimental"
  limitations: "n.v."
  relevance: "Confounder A7 (fewer listings, fewer move-up buyers)"
  location: "Abstract"
  verification: "ABSTRACT_ONLY"
```

---

## 3. Methods references (M-IDs)

| ID | Reference | Used for | Verification |
|---|---|---|---|
| M01 | Callaway, Goodman-Bacon & Sant'Anna (2024), NBER WP 32117 | Continuous-treatment DiD interpretation | ABSTRACT_ONLY |
| M02 | Roth, Sant'Anna, Bilinski & Poe (2023), *J. Econometrics* 235 (2) | DiD practice; pre-testing issues | Bibliographic |
| M03 | Rambachan & Roth (2023), *REStud* 90 (5) | HonestDiD sensitivity | Bibliographic |
| M04 | Olden & Møen (2022), *Econometrics J.* 25 (3) | DDD requires one parallel-trend assumption | Bibliographic |
| M05 | Goldsmith-Pinkham, Sorkin & Swift (2020), *AER* 110 (8) | Shift-share via shares; Rotemberg weights | Bibliographic |
| M06 | Borusyak, Hull & Jaravel (2022), *REStud* 89 (1) | Shift-share via shocks | Bibliographic |
| M07 | Adão, Kolesár & Morales (2019), *QJE* 134 (4) | Shift-share inference | Bibliographic |
| M08 | Santos Silva & Tenreyro (2006), *REStat* 88 (4) | PPML | Bibliographic |
| M09 | Chen & Roth (2024), *QJE* 139 (2) | Logs with zeros | Bibliographic; cited by P004 for Poisson |
| M10 | Correia, Guimarães & Zylkin (2020), *Stata J.* 20 (1) | PPML with HD FE | Bibliographic |
| M11 | Weidner & Zylkin (2021), *J. Int. Econ.* 132: 103513 | Three-way-FE PPML bias | Bibliographic |
| M12 | Wooldridge (2023), *Econometrics J.* 26 (3) | Nonlinear (Poisson) DiD | Bibliographic |
| M13 | Conley (1999), *J. Econometrics* 92 (1) | Spatial HAC | Bibliographic |
| M14 | Cameron & Miller (2015), *JHR* 50 (2) | Cluster-robust inference | Bibliographic |
| M15 | Abadie, Athey, Imbens & Wooldridge (2023), *QJE* 138 (1) | Clustering level | Bibliographic |
| M16 | Freyaldenhoven, Hansen & Shapiro (2019), *AER* 109 (9) | Pre-event trends | Bibliographic |
| M17 | Anderson (2008), *JASA* 103 (484) | Sharpened FDR q-values | Bibliographic |
| M18 | Romano & Wolf (2005), *Econometrica* 73 (4) | Stepwise multiple testing | Bibliographic |
| M19 | Autor, Dorn & Hanson (2013), *AER* 103 (6) | CZ-level exposure designs | Bibliographic |
| M20 | Autor & Dorn (2013), *AER* 103 (5) | CZ geography / crosswalk lineage | Bibliographic |
| M21 | Dingel & Neiman (2020), *J. Public Econ.* 189: 104235 | Teleworkability | Bibliographic; data file verified |
| M22 | Zens, Böck & Zörner (2020), *JEDC* 119: 103989 | Occupational monetary-policy sensitivity (used by P004) | Bibliographic |
| M23 | Dixit & Pindyck (1994), Princeton UP | Irreversible investment | Bibliographic |
| M24 | Sinai & Souleles (2005), *QJE* 120 (2) | Rent-risk hedging | ABSTRACT_ONLY |
| M25 | Carroll, Dynan & Krane (2003), *REStat* 85 (3) | Precautionary wealth | ABSTRACT_ONLY |

"Bibliographic" = existence and metadata verified via Crossref. Statements about these methods papers in this package describe their well-known contributions at the level of their titles and abstracts.

Additional abstract-verified background (not given P-IDs): Paz-Pardo (2024), Mabille (2023), Liebersohn & Rothstein (2024); see the bibliography.

## 4. Screened but not included as evidence

| Item | Reason |
|---|---|
| Hampole, Papanikolaou, Schmidt & Seegmiller (2025), NBER WP 33509, "Artificial Intelligence and the Labor Market" | Exists (Crossref); content not extracted |
| Li & Guo (2026), SSRN 6987090, "Generative AI Infrastructure and Local Housing Markets" | Exists (Crossref); content not verified |
| Boston College CRR brief "Are Older Mortgage Applicants More Likely to Be Rejected?" (HMDA 2018–2020) | Seen in search only; UNVERIFIED |
| Richmond Fed Regional Matters (2019) on young adults' denials | Seen in search only; UNVERIFIED |
| Yin, Vu & Persico (NBER), "How (Un)Stable Are LLM Occupational Exposure Scores?" | Title seen in a reference list only; UNVERIFIED |
| Webb (2019), SSRN 3482150 | Pre-LLM AI exposure; not used |
| Noy & Zhang (2023), *Science* | Experimental productivity; peripheral |
| Hui, Reshef & Zhou (2024), *Organization Science* | Freelance platform; peripheral |
| Bick, Blandin & Deming (2024), NBER WP 32966 | Adoption rates; peripheral |

---

## 5. Full bibliography (AER style)

Abadie, Alberto, Susan Athey, Guido W. Imbens, and Jeffrey M. Wooldridge. 2023. "When Should You Adjust Standard Errors for Clustering?" *Quarterly Journal of Economics* 138 (1): 1–35. https://doi.org/10.1093/qje/qjac038.

Acemoglu, Daron, David Autor, Jonathon Hazell, and Pascual Restrepo. 2022. "Artificial Intelligence and Jobs: Evidence from Online Vacancies." *Journal of Labor Economics* 40 (S1): S293–S340. https://doi.org/10.1086/718327.

Adão, Rodrigo, Michal Kolesár, and Eduardo Morales. 2019. "Shift-Share Designs: Theory and Inference." *Quarterly Journal of Economics* 134 (4): 1949–2010. https://doi.org/10.1093/qje/qjz025.

Anderson, Michael L. 2008. "Multiple Inference and Gender Differences in the Effects of Early Intervention: A Reevaluation of the Abecedarian, Perry Preschool, and Early Training Projects." *Journal of the American Statistical Association* 103 (484): 1481–1495. https://doi.org/10.1198/016214508000000841.

Atkinson, Tyler, and Shane Yamco. 2026. "Young Workers' Employment Drops in Occupations with High AI Exposure." *Dallas Fed Economics*, Federal Reserve Bank of Dallas, January 6. https://www.dallasfed.org/research/economics/2026/0106.

Autor, David H., and David Dorn. 2013. "The Growth of Low-Skill Service Jobs and the Polarization of the US Labor Market." *American Economic Review* 103 (5): 1553–1597. https://doi.org/10.1257/aer.103.5.1553.

Autor, David H., David Dorn, and Gordon H. Hanson. 2013. "The China Syndrome: Local Labor Market Effects of Import Competition in the United States." *American Economic Review* 103 (6): 2121–2168. https://doi.org/10.1257/aer.103.6.2121.

Avery, Robert B., Kenneth P. Brevoort, and Glenn B. Canner. 2007. "Opportunities and Issues in Using HMDA Data." *Journal of Real Estate Research* 29 (4): 351–380. https://doi.org/10.1080/10835547.2007.12091206.

Barrot, Jean-Noël, Erik Loualiche, Matthew Plosser, and Julien Sauvagnat. 2022. "Import Competition and Household Debt." *Journal of Finance* 77 (6): 3037–3091. https://doi.org/10.1111/jofi.13185.

Bhutta, Neil, Aurel Hizmo, and Daniel Ringo. 2025. "How Much Does Racial Bias Affect Mortgage Lending? Evidence from Human and Algorithmic Credit Decisions." *Journal of Finance* 80: 1463–1496. https://doi.org/10.1111/jofi.13444.

Bhutta, Neil, and Daniel Ringo. 2021. "The Effect of Interest Rates on Home Buying: Evidence from a Shock to Mortgage Insurance Premiums." *Journal of Monetary Economics* 118: 195–211. https://doi.org/10.1016/j.jmoneco.2020.10.001.

Bleemer, Zachary, Meta Brown, Donghoon Lee, Katherine Strair, and Wilbert van der Klaauw. 2021. "Echoes of Rising Tuition in Students' Borrowing, Educational Attainment, and Homeownership in Post-Recession America." *Journal of Urban Economics* 122: 103298. https://doi.org/10.1016/j.jue.2020.103298.

Borusyak, Kirill, Peter Hull, and Xavier Jaravel. 2022. "Quasi-Experimental Shift-Share Research Designs." *Review of Economic Studies* 89 (1): 181–213. https://doi.org/10.1093/restud/rdab030.

Brynjolfsson, Erik, Bharat Chandar, and Ruyu Chen. 2026. "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence." Working paper, Stanford Digital Economy Lab, August. https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf.

Brynjolfsson, Erik, Danielle Li, and Lindsey Raymond. 2025. "Generative AI at Work." *Quarterly Journal of Economics* 140 (2): 889–942. https://doi.org/10.1093/qje/qjae044.

Buchak, Greg, Gregor Matvos, Tomasz Piskorski, and Amit Seru. 2018. "Fintech, Regulatory Arbitrage, and the Rise of Shadow Banks." *Journal of Financial Economics* 130 (3): 453–483. https://doi.org/10.1016/j.jfineco.2018.03.011.

Callaway, Brantly, Andrew Goodman-Bacon, and Pedro H. C. Sant'Anna. 2024. "Difference-in-Differences with a Continuous Treatment." NBER Working Paper 32117. https://doi.org/10.3386/w32117.

Cameron, A. Colin, and Douglas L. Miller. 2015. "A Practitioner's Guide to Cluster-Robust Inference." *Journal of Human Resources* 50 (2): 317–372. https://doi.org/10.3368/jhr.50.2.317.

Carroll, Christopher D., Karen E. Dynan, and Spencer D. Krane. 2003. "Unemployment Risk and Precautionary Wealth: Evidence from Households' Balance Sheets." *Review of Economics and Statistics* 85 (3): 586–604. https://doi.org/10.1162/003465303322369740.

Chen, Jiafeng, and Jonathan Roth. 2024. "Logs with Zeros? Some Problems and Solutions." *Quarterly Journal of Economics* 139 (2): 891–936. https://doi.org/10.1093/qje/qjad054.

Chu, Yongqiang, Jing (Jade) He, Leiju Qiu, and Daxuan Zhao. 2026. "Artificial Intelligence and the Racial Gap in Mortgage Lending." SSRN Working Paper 6342658. https://doi.org/10.2139/ssrn.6342658.

Conley, T. G. 1999. "GMM Estimation with Cross Sectional Dependence." *Journal of Econometrics* 92 (1): 1–45. https://doi.org/10.1016/S0304-4076(98)00084-0.

Consumer Financial Protection Bureau. 2024. "2023 Mortgage Market Activity and Trends." December. https://files.consumerfinance.gov/f/documents/cfpb_2023-mortgage-market-activity-and-trends_2024-12.pdf.

Correia, Sergio, Paulo Guimarães, and Tom Zylkin. 2020. "Fast Poisson Estimation with High-Dimensional Fixed Effects." *Stata Journal* 20 (1): 95–115. https://doi.org/10.1177/1536867X20909691.

Dettling, Lisa J., and Joanne W. Hsu. 2018. "Returning to the Nest: Debt and Parental Co-residence among Young Adults." *Labour Economics* 54: 225–236. https://doi.org/10.1016/j.labeco.2017.12.006.

Diaz-Serrano, Luis. 2005. "Labor Income Uncertainty, Skewness and Homeownership: A Panel Data Study for Germany and Spain." *Journal of Urban Economics* 58 (1): 156–176. https://doi.org/10.1016/j.jue.2005.03.003.

Dingel, Jonathan I., and Brent Neiman. 2020. "How Many Jobs Can Be Done at Home?" *Journal of Public Economics* 189: 104235. https://doi.org/10.1016/j.jpubeco.2020.104235.

Dixit, Avinash K., and Robert S. Pindyck. 1994. *Investment under Uncertainty*. Princeton, NJ: Princeton University Press. https://doi.org/10.1515/9781400830176.

Eisfeldt, Andrea L., Gregor Schubert, and Miao Ben Zhang. 2023. "Generative AI and Firm Values." NBER Working Paper 31222. https://doi.org/10.3386/w31222.

Eloundou, Tyna, Sam Manning, Pamela Mishkin, and Daniel Rock. 2024. "GPTs Are GPTs: Labor Market Impact Potential of LLMs." *Science* 384 (6702): 1306–1308. https://doi.org/10.1126/science.adj0998.

Felten, Edward, Manav Raj, and Robert Seamans. 2021. "Occupational, Industry, and Geographic Exposure to Artificial Intelligence: A Novel Dataset and Its Potential Uses." *Strategic Management Journal* 42 (12): 2195–2217. https://doi.org/10.1002/smj.3286.

Fisher, Jonas D. M., and Martin Gervais. 2011. "Why Has Home Ownership Fallen among the Young?" *International Economic Review* 52 (3): 883–912. https://doi.org/10.1111/j.1468-2354.2011.00653.x.

Fonseca, Julia, and Lu Liu. 2024. "Mortgage Lock-In, Mobility, and Labor Reallocation." *Journal of Finance* 79 (6): 3729–3772. https://doi.org/10.1111/jofi.13398.

Frank, Morgan R., Alireza Javadian Sabet, Lisa Simon, Sarah H. Bana, and Renzhe Yu. 2026. "AI-Exposed Jobs Deteriorated before ChatGPT." arXiv:2601.02554. https://arxiv.org/abs/2601.02554.

Freyaldenhoven, Simon, Christian Hansen, and Jesse M. Shapiro. 2019. "Pre-Event Trends in the Panel Event-Study Design." *American Economic Review* 109 (9): 3307–3338. https://doi.org/10.1257/aer.20180609.

Fuster, Andreas, Matthew Plosser, Philipp Schnabl, and James Vickery. 2019. "The Role of Technology in Mortgage Lending." *Review of Financial Studies* 32 (5): 1854–1899. https://doi.org/10.1093/rfs/hhz018.

Gete, Pedro, and Michael Reher. 2018. "Mortgage Supply and Housing Rents." *Review of Financial Studies* 31 (12): 4884–4911. https://doi.org/10.1093/rfs/hhx145.

Gilje, Erik P., Elena Loutskina, and Philip E. Strahan. 2016. "Exporting Liquidity: Branch Banking and Financial Integration." *Journal of Finance* 71 (3): 1159–1184. https://doi.org/10.1111/jofi.12387.

Goldsmith-Pinkham, Paul, Isaac Sorkin, and Henry Swift. 2020. "Bartik Instruments: What, When, Why, and How." *American Economic Review* 110 (8): 2586–2624. https://doi.org/10.1257/aer.20181047.

Handa, Kunal, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah Heck, Jared Mueller, Jerry Hong, Stuart Ritchie, Tim Belonax, Kevin K. Troy, Dario Amodei, Jared Kaplan, Jack Clark, and Deep Ganguli. 2025. "Which Economic Tasks Are Performed with AI? Evidence from Millions of Claude Conversations." arXiv:2503.04761. https://arxiv.org/abs/2503.04761.

Haurin, Donald R. 1991. "Income Variability, Homeownership, and Housing Demand." *Journal of Housing Economics* 1 (1): 60–74. https://doi.org/10.1016/S1051-1377(05)80025-7.

Hosseini Maasoum, Seyed M., and Guy Lichtinger. 2026. "Generative AI as Seniority-Biased Technological Change: Evidence from U.S. Résumé and Job Posting Data." Working paper, May 6 version. SSRN 5425555. https://doi.org/10.2139/ssrn.5425555.

Humlum, Anders, and Emilie Vestergaard. 2025. "Large Language Models, Small Labor Market Effects." NBER Working Paper 33777. https://doi.org/10.3386/w33777.

Iscenko, Zanna, and Fabien Curto Millet. 2026. "Looking for the Ladder: Is AI Impacting Entry-Level Jobs?" Economic Innovation Group, January. https://eig.org/wp-content/uploads/2026/01/TAWP-Iscenko-Millet.pdf.

Kaplan, Greg. 2012. "Moving Back Home: Insurance against Labor Market Risk." *Journal of Political Economy* 120 (3): 446–512. https://doi.org/10.1086/666588.

Kuchler, Theresa, and Basit Zafar. 2019. "Personal Experiences and Expectations about Aggregate Outcomes." *Journal of Finance* 74 (5): 2491–2542. https://doi.org/10.1111/jofi.12819.

Li, Sen, and Chunyu Guo. 2026. "Impact of Generative AI on Local Housing Values through AI Exposure." *Finance Research Letters* 108: 110442. https://doi.org/10.1016/j.frl.2026.110442.

Liebersohn, Jack, and Jesse Rothstein. 2024. "Household Mobility and Mortgage Rate Lock." NBER Working Paper 32781. https://doi.org/10.3386/w32781.

Mabille, Pierre. 2023. "The Missing Homebuyers: Regional Heterogeneity and Credit Contractions." *Review of Financial Studies* 36 (7): 2756–2796. https://doi.org/10.1093/rfs/hhac077.

Mezza, Alvaro, Daniel Ringo, Shane Sherlund, and Kamila Sommer. 2020. "Student Loans and Homeownership." *Journal of Labor Economics* 38 (1): 215–260. https://doi.org/10.1086/704609.

Mian, Atif, and Amir Sufi. 2009. "The Consequences of Mortgage Credit Expansion: Evidence from the U.S. Mortgage Default Crisis." *Quarterly Journal of Economics* 124 (4): 1449–1496. https://doi.org/10.1162/qjec.2009.124.4.1449.

Mondragon, John, and Johannes Wieland. 2022. "Housing Demand and Remote Work." NBER Working Paper 30041. https://doi.org/10.3386/w30041.

Olden, Andreas, and Jarle Møen. 2022. "The Triple Difference Estimator." *Econometrics Journal* 25 (3): 531–553. https://doi.org/10.1093/ectj/utac010.

Oreopoulos, Philip, Till von Wachter, and Andrew Heisz. 2012. "The Short- and Long-Term Career Effects of Graduating in a Recession." *American Economic Journal: Applied Economics* 4 (1): 1–29. https://doi.org/10.1257/app.4.1.1.

Ortalo-Magné, François, and Sven Rady. 2006. "Housing Market Dynamics: On the Contribution of Income Shocks and Credit Constraints." *Review of Economic Studies* 73 (2): 459–485. https://doi.org/10.1111/j.1467-937X.2006.383_1.x.

Ouazad, Amine, and Matthew E. Kahn. 2022. "Mortgage Finance and Climate Change: Securitization Dynamics in the Aftermath of Natural Disasters." *Review of Financial Studies* 35 (8): 3617–3665. https://doi.org/10.1093/rfs/hhab124. **[Retracted; not used as evidence.]**

Paz-Pardo, Gonzalo. 2024. "Homeownership and Portfolio Choice over the Generations." *American Economic Journal: Macroeconomics* 16 (1): 207–237. https://doi.org/10.1257/mac.20200473.

Rambachan, Ashesh, and Jonathan Roth. 2023. "A More Credible Approach to Parallel Trends." *Review of Economic Studies* 90 (5): 2555–2591. https://doi.org/10.1093/restud/rdad018.

Ringo, Daniel. 2026. "Monetary Policy and Home Buying Inequality." *Review of Economics and Statistics* 108: 1052–1066. https://doi.org/10.1162/rest_a_01445.

Robst, John, Richard Deitz, and KimMarie McGoldrick. 1999. "Income Variability, Uncertainty and Housing Tenure Choice." *Regional Science and Urban Economics* 29 (2): 219–229. https://doi.org/10.1016/S0166-0462(98)00031-3.

Romano, Joseph P., and Michael Wolf. 2005. "Stepwise Multiple Testing as Formalized Data Snooping." *Econometrica* 73 (4): 1237–1282. https://doi.org/10.1111/j.1468-0262.2005.00615.x.

Roth, Jonathan, Pedro H. C. Sant'Anna, Alyssa Bilinski, and John Poe. 2023. "What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature." *Journal of Econometrics* 235 (2): 2218–2244. https://doi.org/10.1016/j.jeconom.2023.03.008.

Santos Silva, J. M. C., and Silvana Tenreyro. 2006. "The Log of Gravity." *Review of Economics and Statistics* 88 (4): 641–658. https://doi.org/10.1162/rest.88.4.641.

Schwandt, Hannes, and Till von Wachter. 2019. "Unlucky Cohorts: Estimating the Long-Term Effects of Entering the Labor Market in a Recession in Large Cross-Sectional Data Sets." *Journal of Labor Economics* 37 (S1): S161–S198. https://doi.org/10.1086/701046.

Seagraves, Cayman, and Stace Sirmans. 2026. "AI Exposure and Housing Markets." SSRN Working Paper 6749481. https://doi.org/10.2139/ssrn.6749481.

Sinai, Todd, and Nicholas S. Souleles. 2005. "Owner-Occupied Housing as a Hedge Against Rent Risk." *Quarterly Journal of Economics* 120 (2): 763–789. https://doi.org/10.1093/qje/120.2.763.

Tucker, Lee. 2026. "You're (Not) Hired: Artificial Intelligence and Early Career Hiring in the Quarterly Workforce Indicators." Presentation slides, U.S. Census Bureau, Center for Economic Studies, April 17. https://leetucker.net/docs/ai_sge_2026/.

Weidner, Martin, and Thomas Zylkin. 2021. "Bias and Consistency in Three-Way Gravity Models." *Journal of International Economics* 132: 103513. https://doi.org/10.1016/j.jinteco.2021.103513.

Wooldridge, Jeffrey M. 2023. "Simple Approaches to Nonlinear Difference-in-Differences with Panel Data." *Econometrics Journal* 26 (3): C31–C66. https://doi.org/10.1093/ectj/utad016.

Zens, Gregor, Maximilian Böck, and Thomas O. Zörner. 2020. "The Heterogeneous Impact of Monetary Policy on the US Labor Market." *Journal of Economic Dynamics and Control* 119: 103989. https://doi.org/10.1016/j.jedc.2020.103989.

### Data and policy sources

- FFIEC / CFPB. *HMDA Snapshot National Loan-Level Dataset*, 2018–2025. https://ffiec.cfpb.gov/data-publication/snapshot-national-loan-level-dataset ; files at `https://files.ffiec.cfpb.gov/static-data/snapshot/`.
- FFIEC / CFPB. *Filing Instructions Guide for HMDA Data Collected in 2024*. https://files.ffiec.cfpb.gov/documentation/2024-hmda-fig.pdf.
- FFIEC / CFPB. *Public HMDA — LAR Data Fields*. https://ffiec.cfpb.gov/documentation/publications/loan-level-datasets/lar-data-fields.
- U.S. Census Bureau, LEHD. *Quarterly Workforce Indicators*, release R2026Q3. https://lehd.ces.census.gov/data/qwi/latest_release/.
- U.S. Census Bureau. *American Community Survey 2015–2019 5-Year PUMS*. https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/.
- U.S. Census Bureau. *County Population by Characteristics*, Vintage 2025 and 2010–2020 Intercensal. https://www2.census.gov/programs-surveys/popest/datasets/.
- U.S. Bureau of Labor Statistics. *Occupational Employment and Wage Statistics*, May 2022. https://www.bls.gov/oes/.
- Federal Housing Finance Agency. *House Price Index, county annual*. https://www.fhfa.gov/hpi/download/annual/hpi_at_county.csv.
- Dorn, David. *Crosswalk files* (county → CZ; PUMA 2010 → CZ). https://www.ddorn.net/data.htm.
- U.S. Department of Housing and Urban Development. 2023. *Mortgagee Letter 2023-05* (FHA annual MIP reduction). https://archives.hud.gov/news/2024/2023-05hsgml.pdf (verified via secondary sources only).
