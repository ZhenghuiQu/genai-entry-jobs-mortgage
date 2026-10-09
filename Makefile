PYTHON ?= .venv/bin/python

.PHONY: feasibility feasibility-acquire feasibility-analyze feasibility-validate

# Feasibility only: this is not a national regression or paper pipeline.
feasibility: feasibility-acquire feasibility-analyze

feasibility-acquire:
	$(PYTHON) scripts/feasibility/acquire_small_sources.py
	$(PYTHON) scripts/feasibility/acquire_followup_sources.py
	FEASIBILITY_HTTP_BACKEND=curl_cffi_chrome $(PYTHON) scripts/feasibility/final_source_probe.py
	FEASIBILITY_HTTP_BACKEND=curl_cffi_chrome $(PYTHON) scripts/feasibility/hmda_probe.py
	$(PYTHON) scripts/feasibility/qwi_probe.py
	$(PYTHON) scripts/feasibility/acs_bulk_probe.py
	$(PYTHON) scripts/feasibility/pums_resource_probe.py

feasibility-analyze:
	$(PYTHON) scripts/feasibility/hmda_analyze.py > data/feasibility/hmda_analysis_console.log
	$(PYTHON) scripts/feasibility/geography_audit.py > data/feasibility/geography_analysis_console.log
	$(PYTHON) scripts/feasibility/occupation_audit.py > data/feasibility/occupation_analysis_console.log
	$(PYTHON) scripts/feasibility/qwi_probe.py --analyze-only > data/feasibility/qwi_analysis_console.log
	$(PYTHON) scripts/feasibility/auxiliary_audit.py > data/feasibility/auxiliary_analysis_console.log
	$(PYTHON) scripts/feasibility/compute_probe.py > data/feasibility/compute_analysis_console.log
	$(PYTHON) scripts/feasibility/render_reports.py
	$(MAKE) feasibility-validate

feasibility-validate:
	$(PYTHON) scripts/feasibility/test_zip_helpers.py
	$(PYTHON) scripts/feasibility/validate_artifacts.py

# Phase 2: offline diagnostics only; public acquisition is a separate explicit target.
.PHONY: phase2-analyze phase2-acquire phase2-validate
phase2-acquire:
	$(PYTHON) scripts/phase2/acquire_sources.py --national
phase2-analyze:
	$(PYTHON) scripts/phase2/exposure_coverage.py
	$(PYTHON) scripts/phase2/geographic_resolution.py
	$(PYTHON) scripts/phase2/render_phase2_reports.py
phase2-validate:
	$(PYTHON) scripts/phase2/validate_phase2.py
