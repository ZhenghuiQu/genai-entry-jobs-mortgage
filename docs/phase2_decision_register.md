# Phase 2 Decision Register

Date: 2026-10-09 (Asia/Shanghai). This document is a Phase 2 audit, not an implementation or treatment-effect report. Mapping release: **PROVISIONAL_AUDIT_NOT_FINAL**. Recommendation **C**.

## Competing specifications and required author approval

| ID | Competing specification | Verified source | Argument and limitation | Required author approval / current status |
| --- | --- | --- | --- | --- |
| D01 | Provisional primary: 2018–2022 pre vs 2023–2025 post; event-study reference 2022 | Available Claude `05_identification_designs.md`, lines 36, 59–105; local Day 1–2 decision report | Retains all pre-years and last pre-year reference; includes COVID boom and rate/tech shocks | Remains preserved; changing it requires approval |
| D02 | Requested cross-review primary: 2018–2019 vs 2023–2025, omitting 2020–2022 | Current user Phase 2 instruction; full cross-review MISSING | Cleaner pre-pandemic comparison but only two pre-years and longer secular gap | Obtain cross-review; approve promoting this comparison to primary |
| D03 | 2018–2019 vs 2023–2025 long-difference companion | Available Claude `05_identification_designs.md` lines 165–168; `07_recommended_research_plan.md` REQ-EST-09 | This comparison already exists as a proposed companion; it is not evidence that Claude primary PPML used that window | Any promotion/change in role requires approval; no estimation here |
| D04 | Dynamic full 2018–2025 panel with 2022 reference; alternatively restricted panel with 2019 reference | Available Claude dynamic formula; reference consequence is algebraic design assessment | 2022 can be reference only if included in dynamic estimation sample; a 2018/2019-only pre comparison cannot use an absent 2022 observation as its normalization | Freeze primary versus companion windows and each reference explicitly; no silent switch |
| E01 | Exposure ages 22–34 versus 25–34 | Available review uses 22–34 ACS; user primary mortgage ages 25–34 | Both audited; 25–34 aligns mortgage cohort but changes original labor-exposure definition | Author chooses; retain both outputs |
| E02 | Every-child equal-SOC primary audit versus equal-O*NET-child alternative versus available-child diagnostic | Official memberships plus Phase 2 assumptions | Internal shares unavailable; diagnostic missing-child representativeness is stronger than complete-child scoring | Author approves scoring/missing policy before a final index; no zero fill |
| E03 | Retain source typo group unscored versus documented 40-9095→49-9095 correction candidate | Two official Census workbooks and O*NET corroboration | Candidate correction supported, no PUMS-specific erratum; unrated All Other remains | Record explicit acceptance and residual policy; primary audit remains conservative |
| G01 | CZ provisional primary; State geographic fallback | Current instruction; available independent Claude package | State bypasses county/PUMA linkage but shares the missing occupation exposure dependency | Neither is released for implementation yet |
| G02 | CT A: documented unique-CZ bridge; B: all-year exclusion | Official Census relationships and Dorn observed members | A preserves ≥98.979%/99.058% of 2024/2025 CT sample originations; B loses one whole CT-only CZ | Recommend A provisionally; author accepts primary geographic/missing policy |
| G03 | Broomfield→28900 approximation versus consistent exclusion | Dorn September 2021 county-change notes | Source counties span two CZs; approximation is not a genuine rename | Require explicit acceptance and affected application counts |
| G04 | Retain full cross-state CZs versus drop whole CZs affected by state exclusion | Complete Dorn member states; population exclusion diagnostics | Dominant-state labels do not define membership; partial exposures/outcomes must have the same support | Freeze consistent exposure/outcome support; measure national employment losses first |
| V01 | Original 98% project target | Day 1–2 audit and current Phase 2 instruction | Neither observed repaired DE age band passes; high coverage cannot establish measurement validity | No lowering after outcome inspection; no universal statistical rule claimed |

## Preserved empirical design

HMDA activity years remain 2018–2025. Mortgage comparison remains recorded home-purchase applications for ages 25–34 versus 35–44. The provisional proposal is age-based PPML triple differences with market×year, age×year and market×age fixed effects and a dynamic companion, with pre/post timing around 2023. Interpretation is explicitly descriptive unless parallel-trend and other identification assumptions are defended. No estimator, coefficient, significance test or treatment-effect regression has been run.

Recorded applications refer to observed HMDA reporting, not all latent mortgage demand. Preserve the existing provisional action 1–5/product filters and partial-exemption policy while author decisions remain pending. CT validation uses originations and does not silently redefine the primary application outcome. Exposure coverage/geo checks are not proof of causal identification, and surviving two-age contrasts remain vulnerable to differential rate shocks, tech correction, reporting changes and cohort composition.

## Single stopping recommendation

**C — Critical exposure or provenance dependencies remain unresolved.** The SOC hierarchy is complete and the CT CZ bridge is technically validated on available samples. Unrated exposure, internal aggregation validity, national coverage, original repository access and missing authoritative review documents remain unresolved. State fallback has not independently validated those common exposure/provenance dependencies, so B is not justified. Full national exposure/geographic validation has not passed, so A is not justified.

Exact next implementation step: restore authenticated access to the named original repository and a download-capable route for the pinned national ACS person archive; run the existing Phase 2 aggregate pipeline nationally, then reconcile the missing full cross-review and approve the primary pre-period/reference and missing-score/geographic policies. Do not begin HMDA regressions or paper writing at this stopping point.
