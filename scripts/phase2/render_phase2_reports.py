"""Render authoritative Phase 2 updates while preserving Day 1-2 evidence."""
import datetime as dt,hashlib,json,shutil,sys
from pathlib import Path
import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'feasibility'))
from common import ROOT,DATA,OUT,save
BASE='3f363bca62b6d8938ee8f95696465361d2092476'
DATE='2026-10-09 (Asia/Shanghai)'
def table(d,cols=None):
 if cols:d=d[cols]
 d=d.copy().fillna('OPEN / not observed')
 return '| '+' | '.join(d.columns)+' |\n| '+' | '.join(['---']*len(d.columns))+' |\n'+'\n'.join('| '+' | '.join(f'{v:.6f}' if isinstance(v,float) else str(v).replace('|','/') for v in row)+' |' for row in d.itertuples(index=False,name=None))
def write(name,text):
 (ROOT/'docs'/name).write_text(text.rstrip()+'\n')
def run():
 o=json.loads((OUT/'phase2_occupation_summary.json').read_text());g=json.loads((OUT/'phase2_geography_summary.json').read_text());p=json.loads((OUT/'phase2_processing_log.json').read_text())
 cov=pd.read_csv(OUT/'exposure_coverage_by_geography.csv',dtype={'geography_id':str});de=cov[(cov.scope=='State')&cov.survey_year.eq('pooled')]
 old=pd.read_csv(OUT/'occupation_weighted_coverage.csv');old=old[old.survey_year.eq('pooled')];comp=de[['age_group','employment_weight','covered_weight','weighted_coverage_percent','available_soc_diagnostic_coverage_percent','exposure_lower','exposure_upper']].merge(old[['age_group','weighted_coverage_percent']],on='age_group',suffixes=('_after','_before'))
 scopes=[dict(document='Research assignment PDF',availability='MISSING in scoped local search; remote inaccessible'),dict(document='Independent GPT review',availability='MISSING'),dict(document='Independent Claude review',availability='AVAILABLE: eight literature/*.md files, original hashes revalidated'),dict(document='Complete GPT–Claude cross-review',availability='MISSING; treatment-window recommendation known only from current user instruction'),dict(document='Separate Claude-only State audit',availability='MISSING; distinct from available independent Claude review')]
 save('phase2_research_document_status.json',scopes)
 resources=dict(measured_at_utc=dt.datetime.now(dt.timezone.utc).isoformat(),disk_free_bytes=shutil.disk_usage(ROOT).free,ram_bytes=17179869184,ram_measurement='sysctl -n hw.memsize, current Phase 2 run',raw_retention='Existing 118 MB feasibility data retained; no expanded national person CSV or full HMDA downloaded',national_acquisition_status='HTTP 403; archive absent',processing_memory_limit='DuckDB 2 GB, 2 threads, pandas chunks 100000',national_expected_compressed_bytes=2238752642,national_size_basis='Prior pinned ZIP metadata, re-download failed; not a current successful HEAD')
 save('phase2_resource_audit.json',resources)
 gates=[]
 def gate(id,status,source,version,procedure,evidence,uncertainty,implication):gates.append(dict(gate_id=id,status=status,source=source,version=version,test_procedure=procedure,evidence_observed=evidence,validation_statistics=evidence,remaining_uncertainty=uncertainty,primary_design_implication=implication))
 gate('R01','OPEN','Git/connected GitHub account and requested repository',BASE,'Inspect clean status, branches/remotes/log; connector metadata/profile/repository listing; network-enabled git ls-remote',{'local_branch':'codex/phase2-exposure-repair','local_base':BASE,'connector_account':'EHeroLibertyMan','requested_repository_status':404,'owner_repo_list_count':0,'git_https_auth':'unavailable','gh_cli':'not installed'},'Remote contents/default branch/AGENTS.md/history unavailable; comparison and integration cannot be verified','Local additive changes only; preserve original commit, no remote push or cherry-pick claim')
 gate('R02','OPEN','Original research documents',BASE,'Scoped workspace/Desktop and attachment filename search; revalidate available document hashes',scopes,'Assignment, GPT review, full cross-review, separate State audit missing','Primary pre-period/reference and final geographic policy require author reconciliation')
 gate('O01','PASS','BLS SOC 2018 structure PDF; official coding guide; Census ACS workbook; O*NET 2019 crosswalk','BLS November 2017 / reference January 2018; Census September 26 2019; Eloundou 0471612fef3cc22b74fb884d27bff9dbd3770582','Parse ordered published hierarchy; explicit Census component rows only; assert published level counts and exact O*NET identifiers',o,'Web extracts are complete text representations, not original-byte downloads; internal shares remain unknown','Official hierarchy expansion is reproducible; numeric broad/minor groups no longer unresolved solely for missing hierarchy')
 gate('O02','OPEN','Census PUMS ACS row 707 and general occupation list row 547','Pinned original downloaded workbooks','Compare explicit Census component 7550 and title to the separate official Census list and exact O*NET SOC',{'original':'40-9095','supported_candidate':'49-9095','primary_policy':'retain anomaly; keep group 7640 unscored','other_unresolved_special_code':'55-9830 Census military unspecified, not assumed official SOC'},'No PUMS-specific erratum observed; group 7640 also includes unrated 49-9099','Candidate correction is auditable, not silently adopted; military unspecified remains explicit special category')
 gate('O03','OPEN','O*NET-SOC 2019 crosswalk and pinned exposure ratings','1016 official O*NET occupations; 923 ratings','Count unrated detailed SOCs and children; primary requires every official child/member rated; compare alternative equal O*NET-child rule',{'rated_detailed_SOC':798,'fully_rated_detailed_SOC':774,'unrated_detailed_SOC':69,'partially_rated_detailed_SOC':24,'unrated_ONET_children':93,'internal_employment_weights':'not available in inspected ACS/O*NET files'},'Equal internal shares are assumptions; OEWS has no age demographics or O*NET-child employment and 2019 uses hybrid SOC categories','Occupation scores are provisional; employment weighting only occurs with PWGTP and fractional afactor')
 gate('O04','FAIL','Delaware ACS 2015-2019 five-year PUMS','Original archive pinned by source_manifest; 45217 rows','Re-run original script, verify outputs; stream all person records, ESR 1/2; retain every employed PWGTP denominator; evaluate 98% target',comp.to_dict('records'),'Delaware is not national validation; unscored employment can affect rankings','Technical repair improves coverage but neither age band achieves prespecified 98%; target is project-specific, not statistical law')
 gate('O05','OPEN','National ACS person PUMS https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip','ACS 2015-2019 five-year baseline','Recheck resources, attempt bounded streaming download with default and existing validated HTTP clients',{'download_status':403,'national_rows_observed':0,'national_geography_coverage':'not computed','available_processing_validation':'complete Delaware archive'},'Cloudflare response blocks download; no national state/CZ/major-group/ranking validation','Do not use DE rates as national estimates; National CSV rows have observed=False and blank numeric values')
 gate('G01','PASS','Dorn cw_cty_czone and cw_puma2010_czone archives','Pinned source-manifest hashes; county1990/PUMA2010','Unique keys/pairs; published factor sums at tolerance 1e-6; PWGTP*afactor conservation',{'county_rows':3141,'CZs':741,'PUMAs':2351,'split_PUMAs':553,'fractional_allocation_error_DE':p['geographic_allocation_error']},'Population allocation factors do not reveal true young-worker residence within PUMA','Retain fractional mass; geographic arithmetic passes for observed DE sample only')
 gate('G02','PASS','Official Census ACS22 COUSUB22-BLKGRP20 and COUSUB22-TRACT22 relationships; Dorn county map','2022 CT official relationships, complete web extracts retrieved Phase 2','Use all positive-area relationships; map old county to CZ only if unique; check region and tract join keys and sample inconsistencies',{'towns':g['towns'],'tracts':g['official_tracts'],'ambiguous_tracts':g['ambiguous_CZ_tracts'],'old_CT_counties':8,'new_CT_regions':9,'CT_CZ':20901,'samples':g['CT_samples']},'Coverage observed only for four existing CT purchase-origination extracts, all ages; missing identifiers remain','Option A is technically validated at CZ level; recommend retain CT via documented unique-CZ bridge provisionally')
 gate('G03','OPEN','Dorn county-code changes September 2021; Census 2019 county population','Pinned source-manifest hashes','Compare genuine renames, Broomfield approximation, state exclusion and all county-state memberships',{'cross_state_CZs':g['cross_state_CZs'],'CT_affected_CZs':g['CT_affected_CZs'],'CT_cross_state_CZs':g['CT_cross_state_CZs'],'population_inventory':g['population_inventory']},'Broomfield approximation needs acceptance; complete national application missing/mismatch shares unavailable; MI employment losses not computed','CT exclusion removes one whole CZ, not a partial cross-state CZ; other state exclusions require full-component audits')
 gate('D01','OPEN','Available Claude identification/research-plan files and current Phase 2 user request',BASE,'Document competing primary windows/reference-year implications, preserve PPML DDD/dynamic companion and descriptive interpretation',{'current_provisional_window':'2018-2025; pre2018-2022/post2023-2025; reference2022','requested_crossreview_comparison':'2018-2019 vs2023-2025, attributed only to user instruction','regressions_run':0},'Full cross-review absent; restricted comparison cannot use omitted 2022 as its within-sample reference','No primary pre-period/reference switch without author approval; no coefficients/significance tests produced')
 gate('V01','PASS','Current system resource measurements and scripts','Phase 2 runtime', 'Check disk/RAM; stream ZIP chunks; pin derived schemas and no-regression scope',resources,'National throughput unmeasured because download failed; no current author deadline','Storage/RAM permit streaming architecture; access is the active technical dependency')
 payload=dict(phase='Phase 2',recommendation='C',recommendation_text='Critical exposure or provenance dependencies remain unresolved',release_status='PROVISIONAL_AUDIT_NOT_FINAL',original_commit=BASE,regressions_run=0,national_validation_complete=False,remote_integration_complete=False,gates=gates)
 save('phase2_gate_status.json',payload);save('phase2_test_register.json',gates)
 common=f'Date: {DATE}. This document is a Phase 2 audit, not an implementation or treatment-effect report. Mapping release: **PROVISIONAL_AUDIT_NOT_FINAL**. Recommendation **C**.\n\n'
 write('occupation_mapping_resolution.md','# Occupational Mapping Resolution\n\n'+common+f'''## Official membership and schemas

The complete [BLS 2018 hierarchy](https://www.bls.gov/soc/2018/soc_structure_2018.pdf) has 23 major, 98 minor, 459 broad and 867 detailed occupations. The parser reads ordered published parent/child rows, with level rules and three exceptional minor codes from the [official coding guide](https://www.bls.gov/soc/2018/soc_2018_class_and_coding_structure.pdf). It does not expand Census composites by a shared prefix. All 1,556 extracted BLS source lines are retained; this is a web text representation, not a byte-identical PDF.

The Census ACS worksheet supplies 529 PUMS groups. Explicit `Combines` rows, including nested composite leaf rows, supply component membership; numeric broad/minor members are then expanded through the BLS tree. Original OCCP, SOCP, description, source components, detailed/rated/unrated members, Excel rows, source links, status, ambiguity, terminal All Other members and the aggregation rule appear in `occupation_mapping_final.csv`. The filename is contractual; its metadata explicitly says the mapping is provisional. `soc2018_official_hierarchy.csv` preserves hierarchy levels and source line numbers.

Revalidated ratings: 923 unique O*NET-SOC ratings, linked exactly to the official 2019 crosswalk. There are 1,016 official children, 798 detailed SOCs with at least one rating, 774 with every official child rated, 69 entirely unrated SOCs and 24 partly rated SOCs. The 93 unrated children are exported separately. Source commit: `0471612fef3cc22b74fb884d27bff9dbd3770582`; original local source hashes are rechecked.

## Aggregation and employment weights

Primary audit rule: mean over official O*NET children within detailed SOC, then equal mean over detailed members within PUMS group, only when every child/member is rated and memberships are valid. An equal member mean is not employment-weighted. The geographic index applies ACS PWGTP afterward; CZ allocation uses PWGTP × published afactor.

The inspected ACS/O*NET inputs cannot identify internal detailed-SOC employment shares inside a Census composite or O*NET-child shares inside SOC. [OEWS](https://www.bls.gov/oes/oes_ques.htm) has no age demographics and excludes self-employed workers; its May 2019/2020 categories combine 2010/2018 SOC definitions. National OEWS employment could supply an all-age external sensitivity weighting after explicit concordance, not observed age-specific internal shares. It cannot resolve O*NET-child weights. No employment-weighted internal score is claimed or implemented.

Prespecified alternatives: (1) equal mean across all rated O*NET children of a fully rated PUMS group; (2) an envelope from minimum to maximum child rating for fully rated groups; (3) an explicitly diagnostic equal-SOC mean allowing a SOC with some unrated children. Alternative 3 assumes observed children represent missing children and has a different coverage definition; it is not an accepted primary repair. National OEWS weights remain an unimplemented optional sensitivity because compatible shares have not been validated.

## Unmatched categories and source anomaly

A — official broad/minor expansion: resolved through the BLS tree; original-to-repaired coverage is recomputed, not presumed.

B — 74 PUMS groups contain an unrated detailed SOC or an unrated O*NET child. Terminal All Other occupations remain real detailed occupations and are never expanded to neighbors.

C — Census military rank-not-specified `55-9830` is a special aggregate outside the regular BLS hierarchy; membership stays unresolved. Military groups are preserved even though ESR 1/2 defines the civilian coverage universe.

D — blank/unknown OCCP or OCCP/SOCP inconsistency is flagged at the person-aggregate join. Observed DE young-worker missing/inconsistent weight is zero; national values are unknown.

E — group 7640 contains original `40-9095` at ACS worksheet Excel row 707. The text explicitly calls it Census 7550, manufactured building/mobile home installers. The separate official Census list, Excel row 547, maps that exact Census identifier and title to `49-9095`; the O*NET crosswalk corroborates that SOC. This is authoritative support for a correction candidate, not an observed PUMS erratum. Both codes and the basis are preserved; the primary audit leaves group 7640 unscored. Even correcting this typo does not rate its `49-9099` All Other component.

## Weighted coverage and bounded uncertainty

{table(comp)}

The before column independently reproduces Day 1–2. The after column applies the stronger every-child rule, so the change reflects both official hierarchy repair and tighter missing-child accounting. Available-SOC diagnostic coverage is 88.436% / 88.843%; those higher values assume missing children can be represented by rated ones. Neither rule meets the original 98% target.

For total employment W, known-score numerator S and unresolved employment U, the conservative conditional bounds are [S/W, (S+U)/W]. Unmatched employment is retained in W; the lower bound is not zero imputation. These bounds condition on the equal-share primary scores of covered groups. The separate child-min/max envelope permits unknown internal composition among rated children as well. They do not bound uncertainty in the original AI ratings themselves.

There are 62 unresolved DE occupation groups among ages 22–34 (versus 107 in the original audit). Both DE-allocated CZ intervals overlap in every observed age/year comparison; their exposure ranking is not robust to unscored employment. No national ranking claim is made. Coverage describes availability, not identification, AI adoption, or precision; replicate-weight uncertainty has not been estimated.

Gate details: O01–O05 in `phase2_gate_status.json`. The hierarchy procedure passes; rating/aggregation/source policy remains OPEN, and the observed 98% coverage test FAILS.
''')
 write('national_exposure_coverage.md','# National Exposure Coverage\n\n'+common+f'''## Observed scope and download dependency

The national [ACS 2015–2019 person archive](https://www2.census.gov/programs-surveys/acs/data/pums/2019/5-Year/csv_pus.zip) could not be downloaded: default and Chrome-compatible TLS clients return HTTP 403. The response identifies Cloudflare; no credentials or challenge circumvention was attempted. Metadata listing remains accessible through the web tool. `phase2_national_acquisition.json` and append-only source logs preserve the attempts. This is an access failure, not evidence about occupational coverage.

Current RAM is 16 GiB. Current free storage is {resources['disk_free_bytes']/1024**3:.2f} GiB at report rendering. Prior ZIP directory metadata records a 2,238,752,642-byte national archive and about 10.38 GB of expanded person CSVs; these are historical metadata, not a successful current HEAD. The downloader caps compressed storage at 3 GB and requires 8 GiB free. Processing reads ZIP entries to EOF in 100,000-row chunks, stores only occupation × PUMA × age segment × survey-year aggregates, and uses a 2 GB DuckDB memory cap. It never expands all CSVs or downloads HMDA snapshots.

The complete DE archive was reprocessed: 45,217 person rows, 4,898 civilian employed residents aged 22–34. Reusable national code exists, but it has only been exercised on DE. The national branch is not represented as validated. National, all-state, all-CZ, major-group, high-exposure and unresolved-weight distribution requests remain OPEN until acquisition succeeds.

## Recomputed Delaware results by survey year

{table(cov[(cov.scope=='State')],['geography_id','age_group','survey_year','employment_weight','covered_weight','weighted_coverage_percent','exposure_lower','exposure_upper','known_high_exposure_weight','possible_high_exposure_weight'])}

These use five-year PWGTP as supplied. Pooled weights are not multiplied by five; individual-year rows describe components of the same five-year file, not separate annual-weight population estimates. ESR 1/2 and exact age bands are used. Unmatched occupations remain in every denominator.

The 12 `National` rows in `exposure_coverage_by_geography.csv` have `observed=False`, OPEN status and blank numerical metrics. State rows contain DE only; CZ rows represent two partially observed zones allocated from DE PUMAs, not whole CZs. No other-state or complete-CZ coverage is imputed.

## Major groups, unresolved employment and sensitivity

`phase2_coverage_by_major_group.csv` reports observed DE major-SOC coverage by age/year. `unmatched_employment_by_group.csv` preserves unresolved group labels, reason, members, weights, denominators and shares. `exposure_sensitivity.csv` reports four methods and intervals, not outcome coefficients. `phase2_exposure_rank_checks.csv` records interval overlap for the two sample-allocated CZs.

High exposure is explicitly diagnostic: primary group beta ≥ 0.5, chosen without mortgage coefficient inspection. The output separately shows fully scored high-exposure weight and potentially high weight (known high plus all unresolved weight). Coverage among potentially high employment is a conservative availability ratio, not an observed classification of unscored workers. High-exposure coverage nationally cannot be reported.

No spatial ranking is defensible solely from the observed coverage percentages: all 12 pairwise DE CZ interval checks overlap. Bounds are conditional on scoring/allocation assumptions and do not include rating error, ACS sampling error or unknown within-PUMA employment patterns. Gate O05 remains OPEN; the 98% project target has not been relaxed.

## Reproduction

Run `.venv/bin/python scripts/phase2/acquire_sources.py --national` with public network access. Then run `.venv/bin/python scripts/phase2/exposure_coverage.py`. The latter verifies a completed national archive against its acquisition hash before processing; if the file is absent it explicitly produces DE-only diagnostics. Use `make phase2-analyze` to reproduce currently observed local evidence. A 403 response cannot be treated as a completed national audit.
''')
 write('geographic_design_resolution.md','# Geographic Design Resolution\n\n'+common+f'''## Option A: official Connecticut bridge

Use the [official Census 2022 relationship files](https://www.census.gov/geographies/reference-files/2022/geo/relationship-files.html), linking new-region county subdivisions to legacy 2020 block groups (which preserve old county FIPS) and to 2022 tracts. Keep every positive land/water area relationship. Map a region or tract only if all documented old-county members have a single Dorn CZ. Do not choose a largest-area county or assign population proportions absent from the source.

Observed: 169 towns; 884 unique tracts, none ambiguous at CZ level; nine planning regions. All eight legacy Connecticut counties map to Dorn CZ 20901, and that CZ contains only Connecticut counties. Every documented new-region component therefore has the same CZ. This exact CZ result does not imply an exact new-region-to-old-county assignment: several regions span multiple old counties. Machine memberships and source records are archived in `phase2_ct_region_membership.csv`, `phase2_ct_tract_bridge.csv`, and complete web-text extracts. Byte download attempts failed 403; extract hashes identify the text representation only.

## Empirical comparison of A and B

{table(pd.DataFrame(g['CT_samples']),['year','rows','option_A_mapped_rows','option_A_coverage_percent','missing_county_rows','county_state_inconsistent_rows','option_B_consistent_CT_exclusion_rows','option_B_CT_retention_percent'])}

These are existing CT-filtered recorded home-purchase **originations**, all ages, for four years. They are not the primary national home-purchase application sample or all 2018–2025 years. The denominator includes missing/inconsistent records. Option A recovers every consistent nonmissing CT county in 2024/2025. It flags two out-of-state county rows in the 2018 CT extract; no tract/county inconsistencies occur in these four extracts. Remaining counts are 138, 244, 359 and 336 missing-county rows; no supported geographic information recovers them.

Option B consistently excludes CT across every HMDA/ACS/control/labor year: 100% loss of these CT-originations and 0% CT retention. In the 2019 population inventory that removes 3,565,287 residents and eight counties. Because the observed Dorn CT CZ is entirely within CT, exclusion removes one whole CZ and creates no partial CZ. The earlier concern that CT exclusion necessarily fragments a cross-border CZ is not supported by this crosswalk.

## Remaining geography policies

- Genuine renames 12086→12025 and 46102→46113 are supported by Dorn’s September 2021 county-change notes; audit original/repaired keys separately.
- Broomfield 08014→28900 is Dorn’s approximation. Its four source counties include Weld in another CZ. Do not call it an exact bridge. Report its affected HMDA weight before author acceptance; a sensitivity may exclude Broomfield consistently. No such complete national application count is currently observed.
- Missing counties, missing states and state/county/tract disagreements remain separate flagged categories. Do not pick a preferred identifier silently. An officially validated known tract can only recover a missing county when its state and mapping are consistent; no such recovery is observed here.
- There are 137 cross-state CZs in the complete Dorn county inventory. The dominant-state map is a label, not a membership restriction. `phase2_partial_cz_population.csv` measures population consequences of CT and CT+MI exclusions. A MI exclusion can fragment other CZs; preserve all components consistently across exposure and outcomes or drop the whole affected CZ with explicit approval. National young-worker losses are not yet measured.
- Dorn PUMA2010 allocations retain fractional afactor, including 553 split PUMAs. All 2,351 PUMA sums pass tolerance 1e-6; DE allocation mass error is zero. Young-worker spatial composition inside a PUMA remains an assumption.

{table(pd.DataFrame(g['population_inventory']),['policy','county_rows','mapped_rows','population','coverage_percent'])}

Inventory rates above are 2019 population/county coverage for contiguous states plus DC, with documented rename candidates and the Broomfield approximation. They do not establish national HMDA coverage. Alaska/Hawaii remain visible in the original inventory, and any primary contiguous-sample restriction still requires author confirmation.

## Recommendation and gate implications

Prefer Option A and retain Connecticut provisionally: it has a documented exact CZ bridge and avoids needless sample loss. Option B is technically coherent but sacrifices an entire CZ. No outcome estimates were used to choose. G02 passes the bridge and bounded-sample test; G03 remains OPEN for the full national application universe, Broomfield policy and state-exclusion employment losses. CZ remains provisional; State remains the geographic fallback and does not resolve missing occupation ratings.
''')
 write('research_provenance_integration.md','# Research Provenance Integration\n\n'+common+f'''## Repository reconciliation

The initial local Git tree was clean at `{BASE}` on `feasibility-handoff`, with origin pointing to the requested [existing repository](https://github.com/ZhenghuiQu/genai-entry-jobs-mortgage). It contains 61 tracked files and a root handoff commit; there is no observed original remote history locally. The new review branch is `codex/phase2-exposure-repair`, descended from the handoff commit. Original feasibility scripts, five reports, 23 structured test records and all manifests are preserved; reports receive explicit current Phase 2 updates and their Day 1–2 contents remain labeled as archived evidence.

GitHub connector authentication succeeds for account EHeroLibertyMan. The requested repository metadata request returns 404; the connector lists no accessible repositories for owner ZhenghuiQu. `gh` is not installed. Sandboxed Git initially fails DNS; network-enabled `git ls-remote` reaches GitHub but cannot read an HTTPS username in noninteractive mode. These tests establish current inaccessibility, not repository nonexistence. Remote branches, AGENTS.md, documents and commit history cannot be compared. No clone, remote integration, cherry-pick, force push, history rewrite or deletion of unrelated files is claimed.

Local implementation can be committed after diff/credential review to preserve work, but that is not a commit on the inaccessible existing remote. R01 remains OPEN. `audit/phase2_integration_plan.md` gives a concrete additive integration sequence for an authenticated checkout; if remote histories are unrelated, copy only inspected changes and record this original base hash rather than replacing the remote tree.

## Document availability

{table(pd.DataFrame(scopes))}

The scoped search examined the workspace, Desktop filenames and attachments; it did not inspect unrelated research contents. No missing document is fabricated. All eight available literature files must match their original stored hashes. The available Claude literature package recommends CZ and an industry-exposure fallback; this does not establish the contents of the missing separate State audit or full cross-review. The current user request controls the continuation.

## Source/version and interaction record

`audit/phase2_request.txt` preserves the supplied Phase 2 instruction. Current source attempts append to `source_manifest.jsonl`; historical entries are not edited. New BLS/CT evidence is explicitly labeled complete web-text extraction, with URL, line coverage and representation hashes. Existing official Census/O*NET/DE/Dorn data retain the original manifests and SHA-256 checks. Phase 2 source hashes and derived-file hashes live in `phase2_artifact_manifest.json`; this supplements, not replaces, Day 1–2 manifests. Test records and gate outputs preserve failures and unresolved choices as well as passes.

Skills actually used: `data-analytics:analyze-data-quality` for hierarchy/completeness/join/missingness checks; `validate-data` for denominators, independent arithmetic and limits on conclusions; `query` for bounded ad-hoc DuckDB aggregations, using the installed Python DuckDB API because the CLI is absent. `panel-data-rules` was inspected but its CRSP/Compustat rules were not applicable or invoked. No occupation-taxonomy-specific, Git-history-specific, or research-provenance-specific skill was available in the inspected catalog; those tasks use official sources, normal Git tools and explicit audit manifests. No subagents were requested or used.

## Overall judgment

Methodological validity: official membership and CT bridging improve, but scores still require unknown internal-share and missing-rating assumptions; source documents cannot authenticate the primary treatment window. Technical feasibility: local streaming/DuckDB and exact CT CZ linkage work; national acquisition and original-repository access remain unavailable. Research-time constraints: no current author deadline is supplied, so C is not justified by an invented one-week limit. These unresolved exposure/provenance dependencies require recommendation C even though CT linkage now passes its bounded validation.
''')
 write('phase2_decision_register.md','# Phase 2 Decision Register\n\n'+common+'''## Competing specifications and required author approval

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
''')
 # Update original five documents in place, preserving their entire previous audit as history.
 updates={
 'occupation_crosswalk_audit.md':f'Revalidated DE primary coverage is now **82.994% (22–34)** and **82.988% (25–34)**, with 62 unresolved 22–34 groups. The complete official hierarchy is audited. Missing child/member scores still fail the 98% project target. See [occupation resolution](occupation_mapping_resolution.md) and [national coverage](national_exposure_coverage.md).',
 'geography_audit.md':'The official CT bridge now passes a bounded CZ validation: all old CT counties and all nine new regions have unique Dorn CZ 20901. 2024/2025 existing CT-originations linkage is 98.979%/99.058%; missing codes remain. CT exclusion removes a whole CT-only CZ. See [geographic resolution](geographic_design_resolution.md).',
 'data_source_registry.md':'Phase 2 adds the complete BLS SOC hierarchy and complete official CT town/block-group and town/tract relationship web extracts. Original downloaded sources and hashes remain preserved. New byte-download attempts and national ACS access fail 403. Resources are remeasured at 16 GiB RAM and roughly 75 GiB free; see [provenance integration](research_provenance_integration.md) and `phase2_resource_audit.json`.',
 'design_decisions_pending.md':'The proposed cross-review primary 2018–2019 versus 2023–2025 window is not silently adopted. The full source document is missing; available Claude PPML uses 2018–2022 pre/reference2022 and has a separate 2018–2019 companion. See [Phase 2 decisions](phase2_decision_register.md) for source-specific competing specifications and author approvals.',
 'feasibility_gate_report.md':'Current recommendation remains **C**, now supported by Phase 2 evidence: official hierarchy and CT bridge pass, DE coverage improves but fails the retained project target, national acquisition returns 403, and original repository/document access remains unresolved. The authoritative gate records are `phase2_gate_status.json`; see [decisions](phase2_decision_register.md), [occupation](occupation_mapping_resolution.md), [geography](geographic_design_resolution.md), [provenance](research_provenance_integration.md).'
 }
 for name,body in updates.items():
  path=ROOT/'docs'/name;text=path.read_text();title,rest=text.split('\n',1)
  if '<!-- PHASE2 BEGIN -->' in rest:rest=rest.split('<!-- PHASE2 END -->',1)[1]
  block=f'\n\n<!-- PHASE2 BEGIN -->\n## Current Phase 2 update — {DATE}\n\n{body}\n\nThe Day 1–2 evidence below is preserved historically; current Phase 2 findings supersede its occupation/CT/provenance conclusions where explicitly stated. No outcome estimation was authorized.\n\n<!-- PHASE2 END -->'
  path.write_text(title+block+rest)
 ctrl=f'''# Phase 2 Controller Report

Date: {DATE}. Recommendation **C — Critical exposure or provenance dependencies remain unresolved.**

1. **Repository:** Clean handoff base `{BASE}` preserved on local review branch `codex/phase2-exposure-repair`. Original remote is inaccessible (connector404; Git HTTPS authentication unavailable). No remote comparison/integration/push is claimed. Local implementation and audit records are prepared for additive integration.
2. **Occupation:** Revalidated DE coverage 71.178%→82.994% (22–34), 71.530%→82.988% (25–34), using complete-child primary scoring. Unresolved 22–34 groups fall 107→62. The available-child diagnostic reaches 88.436%/88.843% but assumes missing-child representativeness. National coverage remains unobserved after403; no 98% acceptance claim.
3. **Geography:** Official CT relationships yield exact unique CZ20901 for all nine planning regions; existing2024/2025 CT-originations coverage is98.979%/99.058%. Missing county counts359/336 remain. Broomfield approximation and complete national application linkage remain OPEN. CT exclusion removes one whole CZ; other state exclusions can fragment137 cross-state CZs.
4. **Primary design:** Keep CZ provisional and State fallback; prefer documented CT bridge provisionally. Preserve HMDA2018–2025, mortgage ages25–34 versus35–44, descriptive PPML DDD/dynamic companion. No primary pre-period or reference change is approved.
5. **Dependencies:** National ACS acquisition; unrated exposure and internal-weight policy; original repository access; assignment/GPT/full cross-review/separate State audit; author window/reference and Broomfield/missingness choices. Methodological, access and deadline constraints are distinguished in the five new reports. No current deadline was invented.
6. **Next step:** Restore authenticated original-repository and public national-ACS access, run `scripts/phase2/exposure_coverage.py` on its validated national ZIP, reconcile source documents and freeze author decisions. Stop before HMDA regressions/paper writing. Zero outcome coefficients, significance tests or treatment-effect regressions were produced.
'''
 # Normalize prose number spacing for readability.
 for a,b in [('connector404','connector 404'),('after403','after 403'),('CZ20901','CZ 20901'),('existing2024','existing 2024'),('is98','is 98'),('counts359','counts 359'),('fragment137','fragment 137'),('HMDA2018','HMDA 2018'),('ages25','ages 25'),('versus35','versus 35')]:ctrl=ctrl.replace(a,b)
 (ROOT/'audit/phase2_controller_report.md').write_text(ctrl)
 print('Rendered 5 new English reports, updated original 5 reports, gate/test/resource registers; recommendation C')
if __name__=='__main__':run()
