## Plan: Demonstrate Data Feasibility

Build a reproducible single-video experiment that proves whether YouTube retention samples can be mapped to timestamped transcript intervals under SEM’s actual access conditions.

### Phase 1: Reproducible Environment

**Tasks**

1. Add runtime dependencies to [pyproject.toml](pyproject.toml).
2. Add testing support and regenerate `uv.lock`.
3. Resolve `client_secret.json` relative to the project/script location.
4. Define safe locations for OAuth tokens, raw API responses, and generated datasets.
5. Add `.gitignore` rules for credentials, tokens, and sensitive raw data.
6. Keep the experiment limited to one configured video and documented date range.

**What this fixes**

- Unresolved imports.
- Working-directory-dependent credential failures.
- Non-reproducible setup.
- Accidental exposure of secrets.

**Verification gate**

- `uv sync` succeeds.
- All imports load successfully.
- Pylance reports no unresolved dependencies.
- Running from the repository root finds the credential file and reaches OAuth.

---

### Phase 2: Verify Identity and API Access

**Tasks**

1. Run OAuth using the intended account and read-only scopes.
2. Confirm the Data API returns the requested video.
3. Confirm the authenticated account/channel relationship.
4. Run the Analytics query against the real video.
5. Record whether `channel==MINE` works.
6. Determine whether SEM requires Content Owner or CMS access.
7. Treat permission errors and empty results as documented evidence.

**What this covers**

- OAuth requirements.
- Channel ownership and access.
- Whether retention data is actually available to SEM.
- Whether historical data can be retrieved.

**Verification gate**

A real run must produce either:

- retention rows, or
- a reproducible access limitation classified as `CONFIRMED`, `CONDITIONAL`, `UNKNOWN`, or `UNAVAILABLE`.

No alignment conclusion is made before this gate passes.

---

### Phase 3: Capture Raw Source Evidence

**Tasks**

1. Update transcript retrieval to the current instance-based API.
2. Save inspectable artifacts for:
   - video metadata,
   - transcript response,
   - Analytics response,
   - query parameters,
   - run timestamp.
3. Log critical boundary information:
   - response keys,
   - column headers,
   - record counts,
   - first and last samples,
   - query dates and filters.
4. Do not log OAuth tokens or client secrets.
5. Normalize transcript snippets into:
   - `text`,
   - `start`,
   - `duration`.

**What this fixes**

- The current script does not inspect raw response structure.
- Analytics columns are assumed rather than verified.
- Transcript API output shape is not documented.

**Verification gate**

Raw artifacts can be opened after a real run, and the console output shows:

- actual response schemas,
- transcript shape,
- Analytics `columnHeaders`,
- sample values,
- source record counts.

---

### Phase 4: Validate Data and Transformations

**Tasks**

1. Validate exactly one matching video and a positive duration.
2. Validate transcript fields, numeric timestamps, positive durations, ordering, gaps, and end time.
3. Validate Analytics row width against `columnHeaders`.
4. Convert values to numeric types explicitly.
5. Check retention ratio range, ordering, duplicates, and missing values.
6. Make this transformation explicit:

   `calculated_seconds = elapsedVideoTimeRatio * total_seconds`

7. Log:
   - ratio range,
   - calculated time range,
   - retention value range,
   - number of rows,
   - retention sample spacing.

**What this covers**

- Whether the API data has the expected shape.
- Whether the ratio-to-seconds conversion is defensible.
- Whether retention data represents point samples or actual intervals.
- Whether retention resolution is sufficient.

**Verification gate**

A normalized retention table passes schema and invariant checks, and every transformation from source field to derived field is logged or saved with its assumptions.

---

### Phase 5: Implement and Test Alignment

**Tasks**

1. Define alignment semantics explicitly:
   - a retention sample at time `t` belongs to `[start, end)`;
   - transcript gaps remain unmatched;
   - exact boundaries cannot match two segments.
2. Add stable transcript segment IDs.
3. Return normalized text strings instead of NumPy arrays.
4. Produce an aligned dataset containing:
   - video ID,
   - retention ratio,
   - retention value,
   - calculated seconds,
   - transcript segment ID,
   - transcript start/end,
   - transcript text,
   - match status.
5. Calculate:
   - total retention samples,
   - matched samples,
   - unmatched samples,
   - alignment coverage,
   - transcript time coverage,
   - sample spacing.
6. Add deterministic tests in `tests/test_alignment.py` for:
   - ordinary matches,
   - exact boundaries,
   - transcript gaps,
   - first and last positions,
   - invalid input,
   - duplicate or unsorted rows.

**What this fixes**

- The current script only prints sampled output.
- It does not measure alignment coverage.
- It silently represents unmatched points.
- It does not test boundary behavior.

**Verification gate**

- Fixture tests pass with `uv run pytest`.
- A real video produces a reusable aligned artifact.
- Coverage and resolution are printed.
- Matched and unmatched rows are distinguishable.
- No retention point is silently discarded.

---

### Phase 6: Make the Feasibility Decision

**Tasks**

1. Compare the observed results with [data-feasibility-spec.md](docs/03-research/data-feasibility-spec.md).
2. Record whether:
   - real API access worked,
   - raw responses were inspected,
   - transformations were explained,
   - alignment coverage was measurable,
   - resolution was useful.
3. Update [current-state.md](docs/00-project-control/current-state.md).
4. Update [assumptions-risks.md](docs/00-project-control/assumptions-risks.md).
5. Update [open-questions.md](docs/00-project-control/open-questions.md).
6. Classify findings as:
   - `CONFIRMED`
   - `CONDITIONAL`
   - `UNKNOWN`
   - `UNAVAILABLE`
7. Assign the final feasibility result:
   - **GREEN:** required evidence is obtainable;
   - **YELLOW:** a modified experiment is still credible;
   - **RED:** the hypothesis cannot be meaningfully tested with available data.

**Verification gate**

A reviewer can reproduce the run, inspect the raw and aligned artifacts, and answer:

> Given SEM’s actual access, what data can we reliably obtain for the experiment?

## Scope Boundaries

Included:

- One real authorized video.
- OAuth and API access testing.
- Transcript retrieval.
- Retention retrieval.
- Raw response inspection.
- Validation and alignment.
- Coverage and resolution measurement.
- Feasibility documentation.

Excluded:

- Production architecture.
- Multi-channel ingestion.
- Machine learning.
- Visual analysis.
- Recommendations.
- Broader MVP development.

## Key Decisions

- Retention values are initially treated as sampled positions, not intervals.
- Alignment means timestamp association, not causal attribution.
- Raw evidence must be preserved for audit.
- Secrets and sensitive API data must not be committed.
- No arbitrary coverage threshold should be invented before observing real retention spacing and transcript coverage.
- If SEM cannot retrieve retention data, that becomes a documented feasibility result rather than an alignment success.
