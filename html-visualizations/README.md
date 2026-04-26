# html-visualizations

Single-file, browser-only ports of the Moderne visualization notebooks. Each tool:

- Runs entirely in the browser, no Python, no server, no build step.
- Loads a CSV via drag-and-drop (or file picker).
- Renders an interactive Plotly chart.
- Lets you download each chart as a standalone HTML you can email, or as a static PNG / SVG.

## Quick start

1. Download or send `moderne-visualizations.html`. It is fully self-contained (each tool inlines its own CSS + helpers), so no other files are needed. If you are unable to download the file, email tips are provided below.
2. Open it in any modern browser (Chrome, Safari, Firefox, Edge).
3. Click any tool in the sidebar, drop a CSV, set options, click **Generate chart**.
4. Next to each chart, pick **Download HTML** (interactive), **PNG** (raster), or **SVG** (vector) to export it.

> Opening the HTML files via `file://` works for most tools. 
- The `moderne-visualizations.html` inlines Plotly and PapaParse, so every tool works with zero network access. 
- The only runtime network call is the optional EPSS fetch in `dependency_vulnerabilities`. That tool still renders the fix-type bar and quick-wins heatmap offline, only the EPSS heatmap needs `api.first.org`. 
- The **PNG** and **SVG** export buttons are also fully offline (Plotly renders them locally).

**Download HTML** exports still reference Plotly from a CDN. Edit the saved file, or use PNG/SVG instead, if you need the exported chart to work offline too.

### Emailing the tool file

The inlined Plotly/PapaParse blobs push `moderne-visualizations.html` to ~5.9 MB of minified JavaScript, which some email scanners flag or drop. You can strip those two blobs before sending and have the recipient paste them back. The file drops to ~1.3 MB and is much more likely to make it through.

**Sender:** open `moderne-visualizations.html` in a text editor and delete these two elements (each is one opening tag, the minified library source, and a closing `</script>`):

```html
<script type="text/plain" id="_plotly_src">…plotly source…</script>
<script type="text/plain" id="_papaparse_src">…papaparse source…</script>
```

Leave everything else alone, and in particular keep the small `<script type="text/plain" id="_exporter_src">` block (it only contains the PNG/SVG export helper) and all the regular `<script>` tags. Send the stripped file.

**Recipient without internet accesss:** paste the two blocks back in just before `</head>`, using the minified source of [plotly 2.35.2](https://cdn.plot.ly/plotly-2.35.2.min.js) and [PapaParse 5.x](https://cdn.jsdelivr.net/npm/papaparse) (obtained once on any machine with internet and carried across the gap):

```html
<script type="text/plain" id="_plotly_src">/* paste plotly-2.35.2.min.js here */</script>
<script type="text/plain" id="_papaparse_src">/* paste papaparse.min.js here */</script>
```

**Recipient with internet access:** just open the stripped file. If the embed blocks are missing, the shell falls back to loading Plotly and PapaParse from their CDNs, so no re-insertion is required.

Note that the `TOOLS` object near the bottom of the file also contains script tags (one per tool) and can itself trigger heuristic scanners. There's no clean way to strip it, so if the email is rejected despite removing the lib blobs, use a shared drive, USB transfer, or a password-protected zip instead.

### Sending results by email

Charts exported with **Download HTML** contain two `<script>` tags (one CDN include for Plotly, one inline `Plotly.newPlot(...)` call with the chart JSON). Many outbound email DLP/sanitizers drop any HTML attachment that contains scripts at all, regardless of size, so the interactive HTML format is not email friendly.

**Preferred: export as PNG or SVG instead.** The **PNG** and **SVG** buttons next to every chart produce plain image attachments with no scripts, no external references, and no executable code. They can usually be sent by email cleanly and are usually smaller than the equivalent Download HTML. Pick:

- **SVG** for reports, slides, Confluence/Word, etc. Vector format, stays crisp at any zoom, editable in Illustrator/Inkscape.
- **PNG** for quick previews, Slack/Teams messages, screenshots.

The PNG/SVG output is rendered from the same figure the interactive chart uses, so axes, legend, colorbar, and annotations all appear exactly as on screen.

**If you truly need to email the interactive HTML**, try these in order:

1. **Rename the file's extension**: `chart.html` → `chart.htm.txt` or `chart.html.bin`. Write the original name in the email body so it's obvious.
2. **Password-protect a zip**: most mail gateways will let a password-protected `.zip` through. Provide the password through a separate channel or communication.


## Caveats

- All data stays in your browser. The only network calls are to CDN (`cdn.plot.ly`, `cdn.jsdelivr.net`) for Plotly + Papa Parse, and optionally `api.first.org` for EPSS scores in the vulnerability tool.
- The JS ports reproduce the notebook logic as closely as practical but are not a bit-for-bit clone. In particular, `dependency_usage_violin` uses a simpler natural-compare version ordering instead of Moderne's `code_data_science.versions.index`; the resulting axis order can differ for pre-release / build-metadata versions.
- Large CSVs (hundreds of thousands of rows) will work but the in-browser aggregation is single-threaded; expect multi-second waits past ~100k rows.
- Dropping multi-selected files on an aggregator tool has been more reliable than the built in folder picker, or folder drop, at times.

## Aggregator tools

Three starred entries in the sidebar accept a single multi-file (or folder) drop and surface every visualization whose inputs are present:

- **⭐ All POV visualizations** drop the entire output folder produced by `pov_recipes_cli_bash.sh` (the `$MODERNE_POV_DATATABLES` directory). 
  - Auto-detects every POV data table the script produces and renders every applicable or available visualization inline on one scrolling page. 
  - The Download HTML / PNG / SVG header buttons download every rendered chart at once.
- **⭐ All Prethink files** drop any mix of Prethink CSVs and it renders every applicable or available Prethink visualization inline.
- **⭐ All release files** drop `ProjectCoordinates` + `DependenciesInUse` + `ParentRelationships` together (all three are required) to render metro map, metro plan, metro waves, and repository release order in one view.

All three aggregators accept folder and multi-file drops, keep cumulative state across successive drops, show a per-file detection log, auto-skip `.moderne/run/` historical snapshots, and tag rows with their project folder so multi-project drops stay distinguishable.

## Which CSV does each tool expect?

Every entry below is a hash-routed view inside `moderne-visualizations.html` — e.g. `…/moderne-visualizations.html#technical_debt_treemap`. The groupings match the sidebar.

**POV recipes**

| Sidebar label | Slug | Source data table |
| --- | --- | --- |
| ⭐ All POV visualizations | `pov_all` | Drop the whole `$MODERNE_POV_DATATABLES` folder produced by `pov_recipes_cli_bash.sh`; auto-detects every POV data table and routes you to the right individual tool or aggregator |

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
- Sidebar: `<a class="nav-item" data-slug="…" href="#…">Label</a>` inside one of the `<div class="nav-group">` blocks (POV recipes, Prethink quality, Release, Static analysis, Dependencies, Lint, Inventory, Structure).

To add a new tool:

1. Pick any existing TOOLS entry as a template (`code_smell_severity_stacked_bar` is the simplest) and author a complete standalone HTML document with inline `<style>` and `<script>`. Load Plotly + PapaParse from CDN and inline the helper block you need — copy from the template:
   - `wireFileDrop({ dropId, inputId, dropTextId, onRows })`, `downloadStandaloneChart(chartDivId, filename)`
   - `normalizeHeaders(rows)` + `HEADER_MAP` — fold platform CSV header variants to canonical names
   - `repoOrModule(row)` — prefer when you previously would have used `shortRepo(row.repositoryPath)`
   - `parseNum(v)`, `shortRepo`, `shortClass`, `extractPackage`, `matchesRepoFilter`, `compareVersions`, `groupBy`
2. Add the document as a new string value in the `TOOLS` object, keyed by a unique snake_case slug.
3. Add a matching `<a class="nav-item" data-slug="your_slug" href="#your_slug">Display name</a>` inside the appropriate `<div class="nav-group">`.
4. If the tool belongs in an aggregator, wire it into the render loop in `prethink_all` or `release_all` (detection → section render with empty-state placeholder), and add an entry to the `POV_VIZ` catalog in `pov_all` if the source recipe is part of the POV bash script.
5. Add a row to the table above and run through the Quick start to sanity-check.

The Python notebooks in `../moderne_visualizations_misc/` remain the source of truth for the data transformations; translate the pandas + plotly operations cell-by-cell into vanilla JS.

There is no build step or checked-in bundler — `moderne-visualizations.html` is edited directly.

## What's in this folder

```
html-visualizations/
├── README.md                              ← this file
└── moderne-visualizations.html            ← self-contained bundle (sidebar + iframe viewer + TOOLS map)
```

