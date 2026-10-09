# Unmatched occupational root causes — Phase A

Date: 2026-10-09 (Asia/Shanghai). Primary exposure data unchanged. All proposed score rules remain unapproved.

## Reproduced evidence

Run `.venv/bin/python scripts/phase3/audit_cached_occupations.py`. It uses only standard-library CSV/XML readers and 3,243 cached Delaware occupation aggregates, not person microdata. Every used input has a SHA-256 receipt in `results/feasibility/phase3_cached_audit.json`. The script independently reconstructs the 529 Census memberships and O*NET rating joins from cached workbooks, reconciles their scores to the existing mapping, checks the official 93-title non-data-level set, and recalculates both age denominators.

| Age | PWGTP employment weight | Initial scored weight | Phase 2 scored weight | Initial coverage | Phase 2 coverage |
| --- | ---: | ---: | ---: | ---: | ---: |
| 22–34 | 123,656 | 88,016 | 102,627 | 71.178107% | 82.993951% |
| 25–34 | 100,473 | 71,868 | 83,381 | 71.529665% | 82.988465% |

Universe: civilian employed ESR 1/2, stated age band, Delaware, 2015–2019 five-year PUMS. PWGTP is the released five-year weight: do not divide it again by five. Age bands overlap and must not be added. These are estimated employment weights, not 123,656 observed records. Cached young-worker person count is 4,898. OCCP–SOCP inconsistency weight is zero here; national consistency remains unknown.

The original 107 unmatched groups and current 62 both reproduce. The change is not 45 simple repairs: 57 originally unmatched groups (weight 19,779) become covered, while 12 formerly covered groups (weight 5,168) fail the stricter all-title rule. Net improvement: 14,611 weight, 45 groups. Original diagnostics and ambiguous-group files describe the older rule; do not treat them as current unresolved lists.

## Root-cause classification

Tags overlap; rows cannot be added across categories.

| Requested class | Current groups | Weight, 22–34 | Finding |
| --- | ---: | ---: | --- |
| A: broad/minor SOC | 18 | 7,425 | Official hierarchy already expanded; missing terminal scores block completion |
| B: ACS composites | 32 | 10,652 | Explicit membership already read; composite is not a wildcard matching failure |
| C: terminal All Other | 62 | 21,029 | Every unresolved group includes an unscored residual title |
| D: no valid rating for a member/title | 62 | 21,029 | Structurally unrepresented titles, not failed data-level joins |
| E: historical mismatch | 0 confirmed | 0 confirmed | Reconstructed cached memberships match; annual-file extensions still need vintage review |
| F: official-source inconsistency | 1 | 72 | Census 7640 includes invalid 40-9095 |
| G: restrictive score policy | 21 candidates | 6,801 | Non-data-level residual plus rated specialties; one also has F; not a confirmed coding bug |

Official evidence: [Census PUMS list](https://www2.census.gov/programs-surveys/demo/guidance/industry-occupation/2018-ACS-PUMS-and-2018-SIPP-Public-Use-Occupation-Code-List.xlsx), [BLS hierarchy](https://www.bls.gov/soc/2018/soc_structure_2018.pdf), [O*NET crosswalk](https://www.onetcenter.org/taxonomy/2019/soc/2019_to_SOC_Crosswalk.xlsx), and [official non-data-level list](https://www.onetcenter.org/taxonomy/2019/no_data_coll.html). Sources remain pinned by cached hashes. No code/title similarity or uncontrolled prefixes were used.

The 93 unscored titles comprise 74 civilian titles and 19 military titles. Their exact code set equals the official non-data-level set, leaving no missing data-level beta rating. Military groups remain in the master taxonomy but do not appear in this civilian sample.

## Which groups are potentially resolvable?

Twenty groups have all documented SOC members represented by at least one rated specialty. They total 6,729 weight (5.441709 percentage points of all young employment):
`0440, 1530, 1108, 1760, 3090, 1240, 2330, 3545, 1555, 1970, 3245, 0750, 1610, 1825, 0960, 6765, 3550, 3960, 3655, 8630`.

A mean of available data-level specialties within SOC, then an equal mean of documented SOC members, reproduces the existing diagnostic coverage of 88.435660% / 88.842774%. It does not establish that unspecified residual workers have the same exposure. [O*NET's computer residual page](https://www.onetonline.org/link/summary/15-1299.00) explicitly distinguishes this broad residual population from named specialties. Reclassifying these groups requires a scoring-policy decision, not a new exact join. No such decision is implemented here.

Forty-one groups total 14,228 weight and include at least one SOC with no rated specialty. Nine are standalone wholly unrated occupations:
`2006, 2014, 9150, 7855, 4655, 4965, 2180, 2865, 5040`.
The other 32 contain fully missing SOC members within broader/composite occupations. Retain missing scores and bounds. Neither a hierarchy expansion nor a NEM relabeling creates a rating for these members. They may receive proxy/aggregate scores only under explicit additional assumptions.

Group `7640` (72 weight) has both a source error and a residual-policy problem. Cached ACS worksheet: group row 703, invalid component row 707; separate official Census occupation worksheet: row 547, Census identifier 7550 explicitly maps to 49-9095. This supports a versioned correction candidate, not a discovered PUMS erratum. Correcting it alone leaves unscored 49-9099. If both correction and specialty policy were approved, illustrative 22–34 coverage would be 88.493886%, still below 95%.

No exact, assumption-free score repair for these remaining groups was confirmed. G denotes review priority, not permission to silently relax the primary rule.

## Employment priorities

| Rank | OCCP | Description | Weight | Blocking component |
| --- | --- | --- | ---: | --- |
| 1 | 4020 | Cooks | 2,186 | 35-2019 wholly unrated |
| 2 | 0440 | Other managers | 2,005 | 11-9179 and 11-9199 residual/specialty policy |
| 3 | 2205 | Postsecondary teachers | 1,592 | 25-1069 and 25-1199 wholly unrated |
| 4 | 4220 | Janitors and building cleaners | 1,462 | 37-2019 wholly unrated |
| 5 | 2545 | Teaching assistants | 1,371 | 25-9049 wholly unrated |

These five account for 8,616 weight (40.972% of unresolved employment); top ten: 12,207 (58.048%). Whole-group weights are not estimates of employment in the missing internal member.

The complete 62-row registry is `results/feasibility/occupation_resolution_priorities.csv`, descending employment weight with code tie-breaks. It records both age weights, every missing/partial component, source row, proposed rule, exact-versus-aggregation status, uncertainty and approval gate. It is the authoritative per-occupation handoff; no blank score means zero.
