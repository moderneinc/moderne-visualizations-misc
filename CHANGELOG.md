# CHANGELOG


## v0.71.2 (2025-06-16)

### Bug Fixes

- **sankey**: Better fix for collision
  ([`858b4ad`](https://github.com/moderneinc/moderne-visualizations-misc/commit/858b4ad0689f6f58072495256a64ca41e752651c))


## v0.71.1 (2025-06-16)

### Bug Fixes

- **sankey**: Handle recipe name collisions
  ([#70](https://github.com/moderneinc/moderne-visualizations-misc/pull/70),
  [`7e1f2c2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7e1f2c2a75fa4abad8c5c715340ea832f909044d))


## v0.71.0 (2025-05-22)

### Bug Fixes

- **recipe_performance**: Handle new header names
  ([`174eaea`](https://github.com/moderneinc/moderne-visualizations-misc/commit/174eaea2db655bc0860777f7f8449d706c366ca8))

### Chores

- Add papermill to dev group
  ([`c749ce7`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c749ce7b3fab54333971094e34b24effa34d344b))

- Add vscode recommended extensions
  ([`622b9d1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/622b9d1ebae56500947fce579dc2fcf7ce6fad0f))


## v0.70.0 (2025-02-08)

### Chores

- Add ipykernel to dev dependencies
  ([`a905b2c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a905b2cf7e3a5dc12d4904d4e9f10288626998e4))

### Continuous Integration

- Address action errors
  ([`e52e80a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e52e80aa31fa1cf6212e5586606625dcf221c93f))

- Address even more action errors
  ([`c215d1e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c215d1eea7b8975b667b78a13c2ade5357ea0c0b))

- Address more action errors
  ([`27a5767`](https://github.com/moderneinc/moderne-visualizations-misc/commit/27a5767b03abdf8c844367c7a40625249e764441))

- Switch to uv and ruff
  ([`81a3012`](https://github.com/moderneinc/moderne-visualizations-misc/commit/81a3012bb2ac34e96be0841390e22d4f192ea7c6))

- Update checks
  ([`2b680b5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2b680b503914ae58df73da211837abe664351beb))

### Features

- Add ui5lint visualizations
  ([`4de20d8`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4de20d868654553eb0f8b442d94267c4d31d9d95))


## v0.69.0 (2024-10-22)

### Bug Fixes

- Check column existance before dropping
  ([`c4ed15d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c4ed15d1a4d225c6f9f9a03a6fc81f96dbc7051f))

### Chores

- Update formatting
  ([`2a0e4c4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2a0e4c4a846349727b58261f74dc1a17f1635b1e))


## v0.68.0 (2024-09-10)


## v0.67.0 (2024-09-09)


## v0.66.0 (2024-09-09)


## v0.65.0 (2024-09-05)


## v0.64.0 (2024-09-05)


## v0.63.0 (2024-09-04)


## v0.62.0 (2024-08-27)

### Bug Fixes

- Need `fetch-depth: 0` for fetching tags to find what version to rev
  ([#62](https://github.com/moderneinc/moderne-visualizations-misc/pull/62),
  [`e913a63`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e913a6346155b54949aa9bfdee9492b6208ba35d))


## v0.1.0 (2024-08-27)

### Bug Fixes

- Sentence casing fix ([#61](https://github.com/moderneinc/moderne-visualizations-misc/pull/61),
  [`ea3c3cf`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ea3c3cfe7025e1a8f20742b20f30744699e7d4f2))

* fix: sentence casing fix

* chore: update actions to run on PRs

* chore: update publish workflow to use check workflow

* chore: add concurrency check

### Features

- Dependency violin chart support for nuget
  ([#60](https://github.com/moderneinc/moderne-visualizations-misc/pull/60),
  [`d61b833`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d61b833fb36243bf27b685d9fff8e8587f4c4be1))


## v0.61.0 (2024-08-26)

### Bug Fixes

- Treat `version` as `string` and not `float`
  ([#58](https://github.com/moderneinc/moderne-visualizations-misc/pull/58),
  [`bcf5ae5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bcf5ae5ffa77072173221d3e610547b2f1bfc454))

Avoid truncation of `8.10` to `8.10` when rendering plot

fix https://github.com/moderneinc/moderne-visualizations-misc/issues/54

### Features

- Nuget dependency vulnerability visualization
  ([#59](https://github.com/moderneinc/moderne-visualizations-misc/pull/59),
  [`0d3a19f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0d3a19fed3be2d32a0bb7c40a4436edbf22ae6d2))

modeled after java and npm variant


## v0.60.0 (2024-08-22)

### Chores

- Update github actions ([#57](https://github.com/moderneinc/moderne-visualizations-misc/pull/57),
  [`fd1076a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fd1076af1817689620eec468a09a017578ed20d5))

- Update thumbnails for `find methods` visualizations
  ([#56](https://github.com/moderneinc/moderne-visualizations-misc/pull/56),
  [`ae5ffbb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ae5ffbb9c60fb9be2b565a6b0d31fea81ab6ad72))

these are now data grids and custom yaml recipes

re: https://github.com/moderneinc/moderne-ui/issues/4671

### Refactoring

- **sankey**: Update color palette for sankey diagram (composite recipe results)
  ([#55](https://github.com/moderneinc/moderne-visualizations-misc/pull/55),
  [`2a30506`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2a30506d2eeb049932819d409d1b857c76bb9d1f))

important to have length of `colors` array match number of nodes

fix https://github.com/moderneinc/moderne-ui/issues/4670


## v0.59.0 (2024-08-14)


## v0.58.0 (2024-08-12)

### Chores

- Cleanup
  ([`63fcea6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/63fcea6000a786d38b2ade58280e4bef2b18ac33))


## v0.57.0 (2024-08-07)


## v0.56.1 (2024-08-07)

### Bug Fixes

- **generate_yaml**: Add custom mime type
  ([`de23dbb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/de23dbb0e7f5aaf9ce2a38ea2676048c53954aa3))


## v0.56.0 (2024-08-06)


## v0.55.0 (2024-08-06)

### Chores

- Update violin nodejs images
  ([`ae93ce4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ae93ce4e176c04e3b7fc8d701c6f2f701b517f5f))

### Features

- Add dependency_tree_view for insights
  ([`572880d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/572880d1ce85b25adad9c1b7f2a19669236a4f00))


## v0.54.1 (2024-08-05)

### Bug Fixes

- Update MANIFEST.in
  ([`5c3796b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5c3796bd71101d1d485d30df1954378d77904f3a))


## v0.54.0 (2024-08-05)

### Features

- Add violins for nodejs recipes
  ([`22e88ba`](https://github.com/moderneinc/moderne-visualizations-misc/commit/22e88ba80d5bd6d7796535ea85443cc884f9699a))

### Refactoring

- Add resuable module
  ([`9be1981`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9be19818409035c6e1e4016fc7ab920c03a836c5))


## v0.53.1 (2024-08-05)

### Bug Fixes

- **dependency_tree_view_javascript**: Remove link
  ([`ce1953d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ce1953d3ac899dbdbb8ff75f5552a22b55d3809a))


## v0.53.0 (2024-08-05)


## v0.52.0 (2024-08-04)

### Chores

- Style cleanup
  ([`a249460`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a2494608f0a8c26227c102816033e638d214ce81))


## v0.51.0 (2024-08-04)

### Features

- Add dependency_tree_view_javascript
  ([`ae10f74`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ae10f74d441a3f7e918a747c2c19568b2f8f4aca))


## v0.50.2 (2024-07-12)

### Chores

- **text matches**: Limit to org.openrewrite.text.Find for now
  ([`b9c022e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b9c022e551d3981c162d9bf41d3e0442e035d5cb))


## v0.50.1 (2024-07-12)

### Bug Fixes

- **text matches**: Use better default
  ([`239e3fc`](https://github.com/moderneinc/moderne-visualizations-misc/commit/239e3fc9255f3c11be76c25aad7ac9737960d7b4))


## v0.50.0 (2024-07-12)

### Features

- Add text matches ([#49](https://github.com/moderneinc/moderne-visualizations-misc/pull/49),
  [`a1f9524`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1f95248e3bcb85d0520701d888a43024be599d6))


## v0.49.1 (2024-07-11)

### Chores

- **github_secrets**: Updated image
  ([`a422fde`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a422fde77706a9ede292f35cb94c6012fac0e6f1))


## v0.49.0 (2024-07-11)

### Features

- Add GitHub secrets in use
  ([`92cc34d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/92cc34d8b3a4925cad7e7bc421182b21197b45ac))


## v0.48.0 (2024-06-20)

### Bug Fixes

- Lock numpy down to 1.x to avoid v2 incompat
  ([#46](https://github.com/moderneinc/moderne-visualizations-misc/pull/46),
  [`0946862`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0946862327d19c991b4003a96a5ade858f4ffffc))

- Use `1.24.4` instead ([#47](https://github.com/moderneinc/moderne-visualizations-misc/pull/47),
  [`bdb0e29`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bdb0e29869f0e188bf6592d77ccab14131d49633))


## v0.47.0 (2024-05-14)


## v0.46.0 (2024-05-06)

### Refactoring

- Update cont. color scale for recipe performance
  ([#43](https://github.com/moderneinc/moderne-visualizations-misc/pull/43),
  [`1112c02`](https://github.com/moderneinc/moderne-visualizations-misc/commit/1112c02122a5aad65b2ae7f64710bbd9f80901ac))

use new palette

fix https://github.com/moderneinc/moderne-ui/issues/4273

- Update maven parent pom color scheme
  ([#44](https://github.com/moderneinc/moderne-visualizations-misc/pull/44),
  [`7e3223d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7e3223d63ad06dba818323a02df83a86cd3ca474))

utilize the `color_by_weight(500)`


## v0.45.2 (2024-04-30)


## v0.45.1 (2024-04-25)

### Bug Fixes

- **embeddings**: Revert to previous color
  ([`d157dd4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d157dd4529f719cd8ed9d49b256eadd43de69f2d))


## v0.45.0 (2024-04-23)


## v0.44.0 (2024-04-16)


## v0.43.3 (2024-04-12)

### Bug Fixes

- **sql_crud**: Handle missing data
  ([`98387b9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/98387b980ff17a93907383d729be1f08d5b1dada))


## v0.43.2 (2024-04-12)

### Bug Fixes

- **sql_crud**: Scm types
  ([`be9553d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/be9553db21682e0ffc05cf5196d103fc788252ab))


## v0.43.1 (2024-04-12)

### Bug Fixes

- **sql_crud**: Link column
  ([`7e4de81`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7e4de818c54f5d723da1844f6f195a8df73be096))


## v0.43.0 (2024-04-12)


## v0.42.0 (2024-04-12)

### Features

- **sql_crud**: Add link column
  ([`30f6c43`](https://github.com/moderneinc/moderne-visualizations-misc/commit/30f6c434e370902b9535a27876ff0258c39c6541))


## v0.41.0 (2024-03-26)

### Features

- Add named visualization specifically for Jackson
  ([`2601075`](https://github.com/moderneinc/moderne-visualizations-misc/commit/26010753963a0577c1fdb6dcf49c822337d4bc91))


## v0.40.1 (2024-03-19)

### Bug Fixes

- **nodejs**: Update image
  ([`cacae7b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/cacae7bacaac6d791672ebaae783b44b3f3adf57))


## v0.40.0 (2024-03-09)


## v0.39.1 (2024-03-08)

### Bug Fixes

- **violin**: Use correct recipes
  ([`0375921`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0375921957d6219140e6930b2099031624c36485))


## v0.39.0 (2024-02-29)

### Bug Fixes

- Fix yaml
  ([`bff7957`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bff795729c1602970fcf55da6cb390fa594ed832))

- Fix yaml for real
  ([`7eb7868`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7eb7868146fa7f2ef543754ddbc3dd8a9b4b12a2))


## v0.38.0 (2024-02-23)


## v0.37.0 (2024-02-12)

### Features

- **violin**: Add hover counts and improve legibility
  ([#35](https://github.com/moderneinc/moderne-visualizations-misc/pull/35),
  [`207b04a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/207b04ac9b3b8f9cb464c22b412719bdab34c213))


## v0.36.5 (2024-01-23)

### Bug Fixes

- **violin**: Ensure version column isnt read as float
  ([`ce8eec6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ce8eec64ffb77d7e9ef7f1b0234d13a03d3e3f37))


## v0.36.4 (2024-01-18)

### Bug Fixes

- **spring_relations**: Scaling issue
  ([`fd3af6a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fd3af6a1f933d40ad5bf8c54a9e8519d0f2601b2))


## v0.36.3 (2024-01-18)

### Bug Fixes

- **spring_components**: Remove link due to issue
  ([`19ee5e5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/19ee5e540aa3be4790464949e20a4169234775e1))


## v0.36.2 (2024-01-18)

### Bug Fixes

- Link type issue
  ([`9a2c92a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9a2c92a3fa87fe5fcc440993dc4e7673716f2f87))


## v0.36.1 (2024-01-18)

### Bug Fixes

- Various fixes
  ([`f7057b8`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f7057b874102017d3e56d94d161ecee7f00ae5c8))


## v0.36.0 (2024-01-18)

### Chores

- File name typos
  ([`9874e07`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9874e0722b540e92458c7839ea4cd3b5d326a9d5))

### Continuous Integration

- Add ignore words to sentence casing check
  ([`3b1fa91`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3b1fa91e06ec3858d8c21af07dd7db7c5ffa38e4))

### Features

- Add spring component visualizations
  ([`8f51080`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8f5108078379a5b83312bf0e28ca5fd46a9e3f19))


## v0.35.1 (2024-01-17)

### Bug Fixes

- **eslint**: Update data table name
  ([`ef16017`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ef1601778277a65c936d994747e10d05f495c98e))


## v0.35.0 (2024-01-17)

### Chores

- Clean up and format
  ([`8583d87`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8583d87c142743f97f0f50e3a22e69ad2e86f420))

- More clean up
  ([`10b516d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/10b516d320ceb394a0d3845e5a1c204e1b53c760))

### Features

- **language-comp**: Improve simple text mapping based on file extensions
  ([`32d6235`](https://github.com/moderneinc/moderne-visualizations-misc/commit/32d6235c9c5a3c617e18f69c8868da3231415ddb))


## v0.34.0 (2024-01-09)


## v0.33.3 (2024-01-08)

### Bug Fixes

- **violin**: Add a min height to figure for readability
  ([`a22b3bb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a22b3bb23bf6cd09d140e105f5c17c04540ea4a4))

### Chores

- Clear outputs
  ([`13ac74a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/13ac74a97a70e879342ea772416d5d8a157931d6))

- Formatting
  ([`e75d91e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e75d91ec6c1d35cc59a2afb69abb9be8c5210a3f))


## v0.33.2 (2024-01-08)


## v0.33.1 (2024-01-08)


## v0.33.0 (2024-01-08)


## v0.32.3 (2023-12-06)


## v0.32.2 (2023-12-06)


## v0.32.1 (2023-11-30)

### Chores

- Bumping code-data-science version for bug fix
  ([`160c237`](https://github.com/moderneinc/moderne-visualizations-misc/commit/160c2375db8778389b9aa5dfad85e8739a0d8308))

- **dependency_usage_violin**: Sentence casing
  ([`bc879d7`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bc879d7d62cf51594349b2b88976166a6249a57d))


## v0.32.0 (2023-11-30)

### Chores

- Formatting and polish
  ([`9125462`](https://github.com/moderneinc/moderne-visualizations-misc/commit/91254625d05a057dc4eeca8e730c17bc5581b8b6))

### Features

- Add dependency usage violin
  ([`5234f14`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5234f1410333fb300b7f1c79149cede465b57f16))


## v0.31.1 (2023-11-18)

### Chores

- **sankey**: Remove unused import
  ([`faddce2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/faddce2e9e190ababe1942def3c3b6c0ffa268c4))

- **sankey**: Update scaling and description
  ([`aad3949`](https://github.com/moderneinc/moderne-visualizations-misc/commit/aad3949c58a0fa1460a19d76a7209f8fcffbd912))


## v0.31.0 (2023-11-18)

### Bug Fixes

- **sankey**: Add count threshold to spec
  ([`00469f2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/00469f25855dcbbf1a23b8087cfe5eb009f890af))

### Chores

- Fix formatting
  ([`e00bdcf`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e00bdcfe17e6c75faf40097f16f9b1e2e4ec4359))

### Features

- Add composite recipe results sankey
  ([`c5f9ec7`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c5f9ec70b6a59b37b00c166440c3a4fe1efb978d))


## v0.30.3 (2023-11-11)

### Documentation

- **recipe_performance**: Correction regarding default
  ([`a1c9924`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1c992433ad43369f2714c9b1a37bdf5384c2acf))


## v0.30.2 (2023-11-11)

### Bug Fixes

- **recipe_performance**: Add minimum plot height
  ([`208978d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/208978d4d9e4f74afd066211e68ecf7fd65749b1))


## v0.30.1 (2023-11-10)

### Chores

- Update recipe performance spec to all recipes
  ([`6c1e15c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/6c1e15c8c6f6ab7fcddaa89ca096df9cdc2ae6ce))


## v0.30.0 (2023-11-10)

### Chores

- Update pyproject.toml
  ([`c2895bc`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c2895bc15f0d43c154ee9a5aebc4f5070a4a8790))

### Features

- Add unit measurement to language composition notebooks
  ([#25](https://github.com/moderneinc/moderne-visualizations-misc/pull/25),
  [`f8ee8ac`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f8ee8acdd01d267597e258d5f8f1e90f5f364dff))


## v0.29.1 (2023-10-26)

### Chores

- **recipe_performance**: Convert to seconds
  ([`3025838`](https://github.com/moderneinc/moderne-visualizations-misc/commit/30258386fc9b57c9f8112fb4315b2beefb84340c))


## v0.29.0 (2023-10-26)

### Bug Fixes

- **recipe_performance**: Parameter top_n int conversion
  ([`34718e4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/34718e4c9705157a67627c5b3d2e8c56a3898525))


## v0.28.1 (2023-10-26)

### Chores

- Formatting
  ([`f54ad25`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f54ad2561a1cf93ea17a5258545027887821658f))

- Specify recipe for recipe_performance
  ([`82840dc`](https://github.com/moderneinc/moderne-visualizations-misc/commit/82840dcf6ed38b3043b4c4de305f59430de87228))


## v0.28.0 (2023-10-26)

### Features

- Add recipe_performance
  ([`b13106c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b13106c74bb78b8b9e2cfca7ac1d1cf6354543de))


## v0.27.1 (2023-10-03)

### Bug Fixes

- **language_comp**: Support column rename sourceFileType
  ([`9ac123c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9ac123c8fb0770f8a6e0bfb088a2d3c24539f728))


## v0.27.0 (2023-09-30)


## v0.26.1 (2023-09-26)

### Chores

- **dependency_vulnerabilities**: Update description
  ([`e6b49c6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e6b49c62730e693d439232ec25ccc97cea7650c7))


## v0.26.0 (2023-09-26)

### Features

- **dependency_vulnerabilities**: Add repo filter option
  ([`f518777`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f518777ced2a23ec3991f53e8537f03d4fa0bcab))


## v0.25.0 (2023-09-25)


## v0.24.0 (2023-09-21)


## v0.23.0 (2023-09-21)


## v0.22.0 (2023-09-19)

### Bug Fixes

- **comment_lang**: Update recipe and dataTable
  ([`0a44876`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0a4487676d6e15b0dfadcbf5bc66e929b52649b2))


## v0.21.0 (2023-09-19)


## v0.20.1 (2023-09-13)

### Chores

- **dependency_tree_view**: Add image
  ([`420897c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/420897c2c4a10996a70b418a62169fa5eef09ffe))


## v0.20.0 (2023-09-13)

### Features

- Add dependency_tree_view
  ([`06d16b1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/06d16b10ed5fa3c8a413d871ca8b0004893ab472))


## v0.19.4 (2023-09-05)

### Chores

- Sentence casing
  ([`fad64f0`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fad64f0060afa5b20f43bf9e3c4ce15af3814753))


## v0.19.3 (2023-09-05)

### Bug Fixes

- **call_graph_uml**: Address backward link creation
  ([`f4f8738`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f4f8738898ce152b2414fa26900fcbc605cfaccf))

### Chores

- Run formatting
  ([`cc24328`](https://github.com/moderneinc/moderne-visualizations-misc/commit/cc24328631ca74fcb674c628de257a5ae42e6f57))


## v0.19.2 (2023-09-05)

### Bug Fixes

- **call_graph_uml**: Addres bad hierarchy with inner classes
  ([`5a6559d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5a6559def1815c2354abcdb4f4766bd29214b676))

### Chores

- Update plantuml jar
  ([`db92036`](https://github.com/moderneinc/moderne-visualizations-misc/commit/db920361d4956984a0475fa4efa1444e5626ae5c))


## v0.19.1 (2023-09-01)

### Chores

- **parse_failure_stacktraces**: Update image
  ([`2523496`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2523496788889be382066dd6716496008d735796))


## v0.19.0 (2023-09-01)

### Chores

- **parse_failure_stacktraces**: Clean outputs
  ([`4866f3d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4866f3de47ed73bbcce0c5ffa4bc463bed4a7a42))

- **parse_failure_stacktraces**: Trying as data grid
  ([`3ee1458`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3ee14583402c6c354e31d285a3c6ae8cb5d6b3c4))


## v0.18.2 (2023-09-01)

### Continuous Integration

- Add tasks to check options and casing
  ([`f1c6883`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f1c68837cc83a0414a7efdabdfecfac8aa7f09ab))

- Cleanup local things
  ([`f28f587`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f28f587d91d646842d49ada9846a46e5db099ee8))

- Prevent publish unless checks pass
  ([`d2d5d8e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d2d5d8ee3c0bd9623f22648ed72bf0e4f2cbaa70))

### Documentation

- Update README
  ([`18d75df`](https://github.com/moderneinc/moderne-visualizations-misc/commit/18d75df9c3147df05939bf6c07a0a4bf90520d87))


## v0.18.1 (2023-08-31)


## v0.18.0 (2023-08-30)

### Features

- Call_graph_data_grid
  ([`3cd1321`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3cd132104e5c30fc193351c71d87311c1f748cc3))


## v0.17.4 (2023-08-30)

### Chores

- **call_graph_uml**: Raise exception if df empty
  ([`a1edefb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1edefbfe73f13ef3a6bf611c1a5e5172ee7d903))


## v0.17.3 (2023-08-30)

### Chores

- Update manifest to include resources
  ([`037c28d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/037c28d909e43757f389631ab1b71a7e674f6e6f))


## v0.17.2 (2023-08-30)

### Chores

- **call_graph_uml**: Cleanup
  ([`4385818`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4385818fb106bc559afb1150581ed0162ad349e9))

- **call_graph_uml**: More cleanup
  ([`6ee728f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/6ee728ff6d00383c24b369a8cbb3e4ead4608b42))


## v0.17.1 (2023-08-30)

### Chores

- **call_graph_uml**: Use local plantuml
  ([`cc87e3f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/cc87e3fa9e6e09352bd5c78a40f6c1433f89b357))


## v0.17.0 (2023-08-30)

### Bug Fixes

- Typos in call graph yaml
  ([`997b4d2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/997b4d2314efa3bf1522a3ea028c2ada3b8bb751))


## v0.16.2 (2023-08-29)

### Chores

- Move older yml to dev mode
  ([`9eb1499`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9eb14996f4fe876cbca09295e0d9ab6435c9d524))


## v0.16.1 (2023-08-29)

### Chores

- **call_graph_uml**: Add parameters tag
  ([`7946989`](https://github.com/moderneinc/moderne-visualizations-misc/commit/794698937df80796ec8de6fe744fc25815296ac1))


## v0.16.0 (2023-08-29)

### Features

- Add call_graph_uml
  ([`c81fc11`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c81fc110862db1c61ebbfa57d8710b1c15edbd5f))


## v0.15.0 (2023-08-29)

### Bug Fixes

- Add node_shape for io.moderne.FindCallGraph
  ([`f3f55ae`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f3f55aed98eaffc80125e79d992afc95ee95caa8))


## v0.14.0 (2023-08-29)


## v0.13.1 (2023-08-25)

### Bug Fixes

- **cobol_relationships**: Escape html annotation
  ([`e42b14d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e42b14dabf2ed5cbe674cca511e8b237574fc9f2))


## v0.13.0 (2023-08-25)

### Features

- **maven**: Add effective maven settings data grid
  ([#17](https://github.com/moderneinc/moderne-visualizations-misc/pull/17),
  [`34cf41a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/34cf41a441d01096012276405ec8574af7cb06e1))


## v0.12.1 (2023-08-24)

### Bug Fixes

- **cobol_relationships**: Update size
  ([`3c4a4a6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3c4a4a60cd87ec4f1bfe1d06db02b9f7e401d3a6))


## v0.12.0 (2023-08-24)

### Features

- Add language composition by repository
  ([#16](https://github.com/moderneinc/moderne-visualizations-misc/pull/16),
  [`ab0c328`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ab0c328ea4e5c3a6668ff76131cb41cb9f1fc5e1))


## v0.11.0 (2023-08-24)


## v0.10.0 (2023-08-24)


## v0.9.0 (2023-08-24)


## v0.8.0 (2023-08-23)


## v0.7.0 (2023-08-23)


## v0.6.0 (2023-08-23)

### Features

- Add parameter for defining graphviz layout engine
  ([#13](https://github.com/moderneinc/moderne-visualizations-misc/pull/13),
  [`9ee166e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9ee166ef585e29626dc344bb7ecd75fb61391a1a))


## v0.5.0 (2023-08-22)


## v0.4.0 (2023-08-22)


## v0.3.1 (2023-08-22)

### Chores

- Move parse_failure_analysis to dev
  ([`4213578`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4213578172bc4edbd83b05307d241330a19dbd23))


## v0.3.0 (2023-08-22)


## v0.2.1 (2023-08-21)


## v0.2.0 (2023-08-21)

### Features

- **sql_crud**: Add option to filter operations
  ([`4527362`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4527362492dab1b35e2ced37e634db774a3af1c5))


## v0.1.38 (2023-08-18)

### Continuous Integration

- Add version bumping to release
  ([`ca7ba04`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ca7ba048426387a25beb271185953ed1ab29ebf3))

- Update
  ([`f09411f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f09411fb9c3dd4e548bce569da7e30f078a8545d))


## v0.1.37 (2023-08-17)

### Chores

- Seperate ci only deps
  ([`8b7afd1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8b7afd17f69e7b7f656f4cb3b3007a4e12d2a9a2))

- Update project stuff
  ([`2769aef`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2769aef1bcc8a05093c3ca8122482c805d59ed65))


## v0.1.36 (2023-08-17)

### Bug Fixes

- Dependency vulnerabilities imports
  ([`c2f42b6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c2f42b6ef1b5a9e46f735f8ceb24b4d9d72fdeed))

- Remove extra empty cell and clean outputs
  ([`43a9d3a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/43a9d3a6353969d84570dbdf7fcb0f1f923c35fa))

- **cobol_relationships**: Remove unused option
  ([`a671671`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a671671c25250b09695ef650553576bf1ef22b1f))

- **language_comp**: Clear cells
  ([`0ed34d9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0ed34d9f83044441690e4a3eed05e2cf84b5a3d7))

- **language_comp**: Remove extra cell
  ([`27854c4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/27854c403bb987e6522780ce5f95a850ba8cf8fb))

- **language_comp**: Seperate plot into its own cell
  ([`6f1a52c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/6f1a52ce624fed7c04dc1b9fa0d64125648850ce))

- **language_comp**: Update dependencies
  ([`b9ea3ad`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b9ea3ad4bcdd5767f92cfc03ff2ed00eaee55f93))

### Chores

- Add more samples
  ([`77952b1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/77952b119e2c179280013b52689066ff450111ac))

- Add plotly dependency
  ([`b2d735d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b2d735def13791930bf298fb230b585aa2f9beba))

- Add preview images
  ([`93b2dd0`](https://github.com/moderneinc/moderne-visualizations-misc/commit/93b2dd0f4e8998f6f0c003e1e0e08a1860bd25bc))

- Add type checking
  ([`8c59f57`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8c59f574f73745b89948032cebbf4668fd504409))

- Bump version
  ([`a1fa7a6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1fa7a6cd8146117176b792b07bbb48252853871))

- Bump version
  ([`e7d7f0d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e7d7f0d7e2144f122207a4554e1b7ebc284d5032))

- Bump version
  ([`04d4932`](https://github.com/moderneinc/moderne-visualizations-misc/commit/04d4932d40ee7bc4ad7b1fc984675fc4466f1597))

- Bump version
  ([`c1e08e1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c1e08e19dd0a1fe8fe0c7f48a1c881c3d8e23cdc))

- Bump version
  ([`500f5e1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/500f5e1cefb751f82e29c5fa613e4e646b48fb76))

- Bump version
  ([`fcff20c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fcff20c85078fc703dfefae5a2002a0c0e1d2014))

- Bump version
  ([`b90933c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b90933c98fce38cac04ffae75a32cbfee8477251))

- Bump version
  ([`b63c1d3`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b63c1d35274cfec317ffd4e283d00dce5e895232))

- Bump version
  ([`90c7513`](https://github.com/moderneinc/moderne-visualizations-misc/commit/90c75135ee342d35f527e2a4aced0d53098c34d4))

- Bump version
  ([`43672ed`](https://github.com/moderneinc/moderne-visualizations-misc/commit/43672eddaab8c8eca231f881cec67737d6e83f12))

- Bump version
  ([`8bbb49b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8bbb49b91666b032aa019025e528afa0de1efad9))

- Bump version
  ([`0f29dab`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0f29dabed88c70fd8e4bf14ef95fadb9b4c47837))

- Bump version
  ([`e8ab9a1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e8ab9a18e87488d49a8ace0be7c5238f5a09dcbd))

- Bump version
  ([`f560495`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f56049578714a05585cfd20dba75bf83d2a9fd51))

- Changing version for initial publish
  ([`2ec9b59`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2ec9b59f59598474bd5d52cd35b0f9846081d3ea))

- Clean up
  ([`5dcbe30`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5dcbe30e4311f3f8a0b46a08b2e12e46364fac6e))

- Clean up
  ([`f0d861b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f0d861b4ae25b316aa7dd4af9a25c2df1c0fcf94))

- Exlude samples directory in publishing
  ([`dc60d3a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/dc60d3a486eca22af797c28edbfaba373629b7a7))

- More option support
  ([`e97331b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e97331b0d61406177d1883364401dc4a34f62a92))

- Run formatting
  ([`735b031`](https://github.com/moderneinc/moderne-visualizations-misc/commit/735b031eb90065bc8fb13b862623c8b448e81f0c))

- Update code_data_science
  ([`27a01f9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/27a01f98d38d3ac7476bcf7c3a6cb8f23ff8972f))

- Update dependencies
  ([`2a6d2ac`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2a6d2ac6314401eada3574b4e0afceadb929aa19))

- Update dev deps
  ([`3d3bbc2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3d3bbc251b274e686c5fe2310c02340f39635871))

- Update gitignore
  ([`970e3f5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/970e3f53f25b35280988fe5ab08d500d3da6520e))

- Update images
  ([`d3a901f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d3a901fa61cf240f19c77392be13eab4b2ed768f))

- **dependency_vulnerabilities**: Remove height restraint
  ([`e5320d9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e5320d96802957fe4524187a55567087c8d6f68e))

### Features

- Add cobol relationships data grid
  ([`7f4d2e8`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7f4d2e8b179af4dc594ae7311bdbe45ff58e076b))

- Add colors to cobol
  ([`96cfd4f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/96cfd4fdfc0718cb6067f33ebb592fef104ce06d))

- Add github action
  ([`f65fbd9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f65fbd961c675c3ed958b1ef7b7aee0c499b98e5))

- Add language comp by folder
  ([#8](https://github.com/moderneinc/moderne-visualizations-misc/pull/8),
  [`dd66434`](https://github.com/moderneinc/moderne-visualizations-misc/commit/dd66434ef89584910c6f7e1898cd3f3fe8f8d1c1))

Co-authored-by: Sam Snyder <sam@moderne.io>

- **cobol_relationships**: Add new option to filter to resource
  ([`0af3dec`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0af3dec43d49b1f09c162fad4e4ef4dbddc6f071))

- **gradle_wrappers**: Update colors
  ([`e619282`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e619282a5a90d618deea463694627fc5195532b9))
