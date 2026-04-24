# html-visualizations

Single-file, browser-only ports of the Moderne visualization notebooks. Each tool:

- Runs entirely in the browser &mdash; no Python, no server, no build step.
- Loads a CSV via drag-and-drop (or file picker).
- Renders an interactive Plotly chart.
- Lets you download a single-chart, self-contained HTML you can email.

## Quick start

1. Download `moderne-visualizations.html` &mdash; it is fully self-contained (each tool inlines its own CSS + helpers), so no other files are needed.
2. Open it in any modern browser (Chrome, Safari, Firefox, Edge).
3. Click any tool in the sidebar, drop a CSV, set options, click **Generate chart**.
4. Use the **Download HTML** button next to each chart to export a standalone file for sharing.

> Opening the HTML files via `file://` works for most tools. The `dependency_vulnerabilities` tool calls `api.first.org` for EPSS scores; that works from `file://` in Chrome/Safari but some browsers may block it &mdash; serve the folder via `python -m http.server` or any static server if you hit CORS issues.

## Aggregator tools

Two starred entries in the sidebar render multiple visualizations on one scrolling page from a single multi-file (or folder) drop:

- **⭐ All Prethink files** (`#prethink_all`, under *Prethink quality*) — drop any mix of Prethink CSVs (`ClassQualityMetrics`, `MethodQualityMetrics`, `PackageQualityMetrics`, `CodeSmells`, `TestGaps`, `TestQualityIssues`, `CyclomaticComplexity`, …) and it renders every applicable Prethink visualization. Empty-state placeholders show which inputs are still missing.
- **⭐ All release files** (`#release_all`, under *Release*) — drop `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` together (all three are required) to render metro map, metro plan, metro waves, and repository release order in one view.

Both aggregators accept folder drops, keep cumulative state across successive drops (with a **Clear all** button), show a per-file detection log, auto-skip `.moderne/run/` historical snapshots, and tag rows with their project folder so multi-project drops stay distinguishable.

## Which CSV does each tool expect?

Every entry below is a hash-routed view inside `moderne-visualizations.html` — e.g. `…/moderne-visualizations.html#technical_debt_treemap`. The groupings match the sidebar.

**Prethink quality**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| ⭐ All Prethink files | `prethink_all` | Any mix of the Prethink data tables listed below — folder drops work, missing inputs show placeholders |
| Architectural stability scatter | `architectural_stability_scatter` | `PackageQualityMetrics` |
| Code quality executive dashboard | `code_quality_executive_dashboard` | `ClassQualityMetrics` (only the primary table is required; omit the optional helper tables from the Python notebook) |
| Code smell severity | `code_smell_severity_stacked_bar` | `CodeSmells` |
| Complexity vs test gaps bubble | `complexity_vs_test_gaps_bubble` | `ClassQualityMetrics` + `TestGaps` (two CSVs) |
| Coupling vs cohesion quadrant | `coupling_cohesion_quadrant` | `ClassQualityMetrics` |
| Dependency cycle network | `dependency_cycle_network` | `PackageQualityMetrics` |
| Method risk radar | `method_risk_radar` | `MethodQualityMetrics` |
| Portfolio health sunburst | `portfolio_health_sunburst` | `ClassQualityMetrics` |
| Portfolio quality comparison violin | `portfolio_quality_comparison_violin` | `MethodQualityMetrics` |
| Technical debt hotspots | `technical_debt_treemap` | `MethodQualityMetrics` or `ClassQualityMetrics` (auto-detected) |
| Test gap risk heatmap | `test_gap_risk_heatmap` | `TestGaps` |
| Test quality by language | `test_quality_by_language` | `TestQualityIssues` |
| Test quality executive dashboard | `test_quality_executive_dashboard` | `TestQualityIssues` |
| Test quality issue heatmap | `test_quality_issue_heatmap` | `TestQualityIssues` |
| Test quality language sunburst | `test_quality_language_sunburst` | `TestQualityIssues` |
| Test quality risk matrix | `test_quality_risk_matrix` | `TestQualityIssues` |
| Test quality treemap | `test_quality_treemap` | `TestQualityIssues` |

**Static analysis**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| Cyclomatic complexity heatmap | `cyclomatic_complexity_heatmap` | `CyclomaticComplexity` |
| Cyclomatic complexity risk matrix | `cyclomatic_complexity_risk_matrix` | `CyclomaticComplexity` |
| Repository category heatmap | `repository_category_heatmap` | Static-analysis findings (top-N repos × impact categories) |

**Dependencies**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| Dependency usage violin (Maven / Gradle / Jackson / NuGet) | `dependency_usage_violin` | `DependenciesInUse` (expects `artifactId, version, count`; `groupId` optional) |
| Dependency vulnerabilities | `dependency_vulnerabilities` | `DependencyVulnerabilities` (expects `cve, version, fixedVersion, repositoryPath, severity, depth`) |
| NPM / NuGet dependency vulnerabilities | `dependency_vulnerabilities_npm` | npm or NuGet `DependencyVulnerabilityCheck` (identical schema, one tool) |
| NPM package usage violin | `dependency_usage_violin_nodejs` | NPM `DependenciesInUse` (all 12 insight recipes) |

**Lint**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| ESLint problems (repo → rule) | `eslint_problems_by_repo` | `ESLintProblems` |
| ESLint problems (rule → repo) | `eslint_problems` | `ESLintProblems` |
| UI5Lint rule treemap | `ui5lint_rule_treemap` | `UI5Lint` |
| UI5Lint violations heatmap | `ui5lint_violations_heatmap` | `UI5Lint` |

**Inventory**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| Comment language distribution | `comment_language_distribution` | `CommentsLanguage` |
| Find source files | `find_source_files` | `FindSourceFiles` |
| Gradle wrappers | `gradle_wrappers` | `GradleWrappers` |
| Java versions by source set | `java_versions_by_sourceset` | `JavaVersionsBySourceSet` |
| Java versions in use | `java_versions_in_use` | `JavaVersionsInUse` |
| Language composition | `language_composition` | `FindSourceFiles` (expects `language, sourcePath, linesOfText, hasParseFailures`) |
| Language composition by folder | `language_composition_by_folder` | `LanguageCompositionByFolder` |
| Language composition by repo | `language_composition_by_repo` | `FindSourceFiles` (language + sourcePath) |
| LST provenance | `lst_provenance` | `LstProvenance` |
| Maven parent POMs | `maven_parent_poms` | `MavenParentPOMs` |
| Parse failure stacktraces | `parse_failure_stacktraces` | `ParseFailures` |

**Structure**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| COBOL find copybook | `cobol_find_copybook` | `CobolFindCopybook` |
| COBOL relationships | `cobol_relationships` | `CobolRelationships` |
| Composite recipe results sankey | `composite_recipe_results_sankey` | `CompositeRecipeResults` |
| Recipe performance | `recipe_performance` | `RecipePerformance` |
| Spring component relationships | `spring_component_relationships` | `SpringComponentRelationships` |

**Release**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| ⭐ All release files | `release_all` | `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` (all three required) |
| Release metro map | `release_metro_map` | `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` |
| Release metro plan | `release_metro_plan` | `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` |
| Release metro waves | `release_metro_waves` | `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` |
| Repository release order | `repository_release_order` | `DependenciesInUse` (expects `repositoryOrigin, repositoryPath, projectName, groupId, artifactId`) |

Sample CSVs matching each schema live in `../samples/`.

## Porting an additional notebook

Everything lives inside `moderne-visualizations.html`. The main page is a sidebar + an `<iframe id="viewer">` with hash routing: clicking a sidebar entry (or landing on `#slug`) looks up `TOOLS[slug]` — a fully self-contained HTML document stored as a string — and loads it into the iframe. The same string is what **Download HTML** writes to disk, which is why each tool inlines its own helpers and CSS.

Structurally, inside `moderne-visualizations.html`:

- `const TOOLS = { … }` (~line 134) — one entry per tool, keyed by slug.
- Sidebar: `<a class="nav-item" data-slug="…" href="#…">Label</a>` inside one of the `<div class="nav-group">` blocks (Prethink quality, Static analysis, Dependencies, Lint, Inventory, Structure, Release).

To add a new tool:

1. Pick any existing TOOLS entry as a template (`code_smell_severity_stacked_bar` is the simplest) and author a complete standalone HTML document with inline `<style>` and `<script>`. Load Plotly + PapaParse from CDN and inline the helper block you need — copy from the template:
   - `wireFileDrop({ dropId, inputId, dropTextId, onRows })`, `downloadStandaloneChart(chartDivId, filename)`
   - `normalizeHeaders(rows)` + `HEADER_MAP` — fold platform CSV header variants to canonical names
   - `repoOrModule(row)` — prefer when you previously would have used `shortRepo(row.repositoryPath)`
   - `parseNum(v)`, `shortRepo`, `shortClass`, `extractPackage`, `matchesRepoFilter`, `compareVersions`, `groupBy`
2. Add the document as a new string value in the `TOOLS` object, keyed by a unique snake_case slug.
3. Add a matching `<a class="nav-item" data-slug="your_slug" href="#your_slug">Display name</a>` inside the appropriate `<div class="nav-group">`.
4. If the tool belongs in an aggregator, wire it into the render loop in `prethink_all` or `release_all` (detection → section render with empty-state placeholder).
5. Add a row to the table above and run through the Quick start to sanity-check.

The Python notebooks in `../moderne_visualizations_misc/` remain the source of truth for the data transformations; translate the pandas + plotly operations cell-by-cell into vanilla JS.

There is no build step or checked-in bundler — `moderne-visualizations.html` is edited directly.

## What's in this folder

```
html-visualizations/
├── README.md                              ← this file
└── moderne-visualizations.html            ← self-contained bundle (sidebar + iframe viewer + TOOLS map)
```

## Caveats

- All data stays in your browser. The only network calls are to CDN (`cdn.plot.ly`, `cdn.jsdelivr.net`) for Plotly + Papa Parse, and optionally `api.first.org` for EPSS scores in the vulnerability tool.
- The JS ports reproduce the notebook logic as closely as practical but are not a bit-for-bit clone. In particular, `dependency_usage_violin` uses a simpler natural-compare version ordering instead of Moderne's `code_data_science.versions.index`; the resulting axis order can differ for pre-release / build-metadata versions.
- Large CSVs (hundreds of thousands of rows) will work but the in-browser aggregation is single-threaded; expect multi-second waits past ~100k rows.
