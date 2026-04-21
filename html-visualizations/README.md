# html-visualizations

Single-file, browser-only ports of the Moderne visualization notebooks. Each tool:

- Runs entirely in the browser &mdash; no Python, no server, no build step.
- Loads a CSV via drag-and-drop (or file picker).
- Renders an interactive Plotly chart.
- Lets you download a single-chart, self-contained HTML you can email.

## Quick start

1. Clone or download this directory (`html-visualizations/`) as a whole &mdash; the tools share `_shared/styles.css` and `_shared/common.js`.
2. Open `index.html` in any modern browser (Chrome, Safari, Firefox, Edge).
3. Click any implemented tool, drop a CSV, set options, click **Generate chart**.
4. Use the **Download HTML** button next to each chart to export a standalone file for sharing.

> Opening the HTML files via `file://` works for most tools. The `dependency_vulnerabilities` tool calls `api.first.org` for EPSS scores; that works from `file://` in Chrome/Safari but some browsers may block it &mdash; serve the folder via `python -m http.server` or any static server if you hit CORS issues.

## Which CSV does each tool expect?

| Tool | Source data table (Python notebook input) |
| --- | --- |
| `dependency_vulnerabilities.html` | `DependencyVulnerabilities` (expects `cve, version, fixedVersion, repositoryPath, severity, depth`) |
| `technical_debt_treemap.html` | `MethodQualityMetrics` |
| `code_smell_severity_stacked_bar.html` | `CodeSmells` |
| `language_composition.html` | `FindSourceFiles` (expects `language, sourcePath, linesOfText, hasParseFailures`) |
| `cyclomatic_complexity_heatmap.html` | `CyclomaticComplexity` |
| `dependency_usage_violin.html` | `DependenciesInUse` (expects `artifactId, version, count`; `groupId` optional) |
| `portfolio_health_sunburst.html` | `ClassQualityMetrics` |
| `repository_release_order.html` | `DependenciesInUse` (expects `repositoryOrigin, repositoryPath, projectName, groupId, artifactId`) |
| `composite_recipe_results_sankey.html` | `CompositeRecipeResults` |
| `lst_provenance.html` | `LstProvenance` |
| `complexity_vs_test_gaps_bubble.html` | `ClassQualityMetrics` + `TestGaps` (two CSVs) |
| `spring_component_relationships.html` | `SpringComponentRelationships` |
| `architectural_stability_scatter.html` | `PackageQualityMetrics` |
| `method_risk_radar.html` | `MethodQualityMetrics` |
| `coupling_cohesion_quadrant.html` | `ClassQualityMetrics` |
| `cyclomatic_complexity_risk_matrix.html` | `CyclomaticComplexity` |
| `test_quality_issue_heatmap.html` | `TestQualityIssues` |
| `test_quality_treemap.html` | `TestQualityIssues` |
| `dependency_usage_violin_nodejs.html` | NPM `DependenciesInUse` (all 12 insight recipes) |
| `dependency_vulnerabilities_npm.html` | npm or NuGet `DependencyVulnerabilityCheck` (identical schema, one tool) |
| `parse_failure_stacktraces.html` | `ParseFailures` |
| `release_metro_map.html` | `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` |
| `release_metro_plan.html` | `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` |
| `release_metro_waves.html` | `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` |
| `test_gap_risk_heatmap.html` | `TestGaps` |
| `test_quality_by_language.html` | `TestQualityIssues` |
| `test_quality_language_sunburst.html` | `TestQualityIssues` |
| `test_quality_risk_matrix.html` | `TestQualityIssues` |
| `test_quality_executive_dashboard.html` | `TestQualityIssues` |
| `code_quality_executive_dashboard.html` | `ClassQualityMetrics` (only the primary table is required; omit the optional helper tables from the Python notebook) |
| `portfolio_quality_comparison_violin.html` | `MethodQualityMetrics` |
| `dependency_cycle_network.html` | `PackageQualityMetrics` |
| `eslint_problems.html`, `eslint_problems_by_repo.html` | `ESLintProblems` |
| `ui5lint_rule_treemap.html`, `ui5lint_violations_heatmap.html` | `UI5Lint` |
| `comment_language_distribution.html` | `CommentsLanguage` |
| `find_source_files.html` | `FindSourceFiles` |
| `java_versions_in_use.html` | `JavaVersionsInUse` |
| `java_versions_by_sourceset.html` | `JavaVersionsBySourceSet` |
| `gradle_wrappers.html` | `GradleWrappers` |
| `maven_parent_poms.html` | `MavenParentPOMs` |
| `recipe_performance.html` | `RecipePerformance` |
| `language_composition_by_folder.html` | `LanguageCompositionByFolder` |
| `language_composition_by_repo.html` | `FindSourceFiles` (language + sourcePath) |
| `cobol_relationships.html` | `CobolRelationships` |
| `cobol_find_copybook.html` | `CobolFindCopybook` |

Sample CSVs matching each schema live in `../samples/`.

## Porting an additional notebook

Use `code_smell_severity_stacked_bar.html` as the simplest template:

1. Copy it to a new filename.
2. Update the `<title>`, `<header>`, and CSV-column hint in the dropzone.
3. Adjust the `<div class="controls">` inputs to match the notebook's parameter cell.
4. In the `runBtn.addEventListener(...)` block, replace the transform + Plotly call with the JS equivalent of the notebook's pandas + plotly code. Shared helpers available from `_shared/common.js`:
   - `wireFileDrop({ dropId, inputId, dropTextId, onRows })`
   - `downloadStandaloneChart(chartDivId, filename)`
   - `parseNum(v)`, `shortRepo(path)`, `shortClass(fqn)`, `extractPackage(fqn)`
   - `matchesRepoFilter(value, commaSeparatedTerms)`
   - `compareVersions(a, b)` (natural, for version axes)
5. Add a new `<div class="cat-card">` entry in `index.html`.

The Python notebooks are the source of truth for the data transformations; open the matching `.ipynb` in `../moderne_visualizations_misc/` and translate the pandas operations one by one.

## What's in this folder

```
html-visualizations/
├── README.md                              ← this file
├── index.html                             ← catalog / launcher
├── _shared/
│   ├── styles.css                         ← shared look & feel
│   └── common.js                          ← CSV load, download, helpers
├── dependency_vulnerabilities.html
├── technical_debt_treemap.html
├── code_smell_severity_stacked_bar.html
├── language_composition.html
├── cyclomatic_complexity_heatmap.html
├── dependency_usage_violin.html
├── portfolio_health_sunburst.html
├── repository_release_order.html
├── composite_recipe_results_sankey.html
├── lst_provenance.html
├── complexity_vs_test_gaps_bubble.html
├── spring_component_relationships.html
├── architectural_stability_scatter.html
├── method_risk_radar.html
├── coupling_cohesion_quadrant.html
├── cyclomatic_complexity_risk_matrix.html
├── test_quality_issue_heatmap.html
├── test_quality_treemap.html
├── dependency_usage_violin_nodejs.html
├── dependency_vulnerabilities_npm.html
├── parse_failure_stacktraces.html
├── release_metro_map.html
├── release_metro_plan.html
├── release_metro_waves.html
├── test_gap_risk_heatmap.html
├── test_quality_by_language.html
├── test_quality_language_sunburst.html
├── test_quality_risk_matrix.html
├── test_quality_executive_dashboard.html
├── code_quality_executive_dashboard.html
├── portfolio_quality_comparison_violin.html
├── dependency_cycle_network.html
├── eslint_problems.html
├── eslint_problems_by_repo.html
├── ui5lint_rule_treemap.html
├── ui5lint_violations_heatmap.html
├── comment_language_distribution.html
├── find_source_files.html
├── java_versions_in_use.html
├── java_versions_by_sourceset.html
├── gradle_wrappers.html
├── maven_parent_poms.html
├── recipe_performance.html
├── language_composition_by_folder.html
├── language_composition_by_repo.html
├── cobol_relationships.html
└── cobol_find_copybook.html
```

## Caveats

- All data stays in your browser. The only network calls are to CDN (`cdn.plot.ly`, `cdn.jsdelivr.net`) for Plotly + Papa Parse, and optionally `api.first.org` for EPSS scores in the vulnerability tool.
- The JS ports reproduce the notebook logic as closely as practical but are not a bit-for-bit clone. In particular, `dependency_usage_violin` uses a simpler natural-compare version ordering instead of Moderne's `code_data_science.versions.index`; the resulting axis order can differ for pre-release / build-metadata versions.
- Large CSVs (hundreds of thousands of rows) will work but the in-browser aggregation is single-threaded; expect multi-second waits past ~100k rows.
