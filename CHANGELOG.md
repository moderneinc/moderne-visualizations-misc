# CHANGELOG


## v0.69.0 (2024-10-22)

### Bug Fixes

* fix: check column existance before dropping ([`c4ed15d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c4ed15d1a4d225c6f9f9a03a6fc81f96dbc7051f))

### Chores

* chore: update formatting ([`2a0e4c4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2a0e4c4a846349727b58261f74dc1a17f1635b1e))


## v0.68.0 (2024-09-10)

### Unknown

* run experimental on regular FindMethods recipe ([`d5d37ba`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d5d37ba45a3545d5918fcac529e85504ab7a3921))


## v0.67.0 (2024-09-09)

### Unknown

* fix ellipses ([`52d63ed`](https://github.com/moderneinc/moderne-visualizations-misc/commit/52d63ed89f0c658a0fd8bb0557c458a1b2872639))


## v0.66.0 (2024-09-09)

### Unknown

* tsne for dimension reduc and gmm for clustering ([`9916d14`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9916d14ad19d52e6124f97faac431b2c68bdcbf4))


## v0.65.0 (2024-09-05)

### Unknown

* remove n_jobs from kmeans and add n_jobs to umap ([`2772ae3`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2772ae3d1786076fd80ae7accb8675148c88f207))


## v0.64.0 (2024-09-05)

### Unknown

* add visualization to test onnx embeddings latency and deployment (#64)

* add visualization to test onnx embeddings latency and deployment

* fix new line issue in description ([`59d1f69`](https://github.com/moderneinc/moderne-visualizations-misc/commit/59d1f69a4692dcd8fccfb4da41f346cf8ba6095e))


## v0.63.0 (2024-09-04)

### Unknown

* No longer map plain text `.py` to Python (#63)

We now use the Python parser for `.py` sources and no longer want to map the plain text `.py` files (of projects which haven't been ingested recently) to the Python group. ([`1c2868f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/1c2868f2649a5f0e845bf1622486118143f463f4))


## v0.62.0 (2024-08-27)

### Bug Fixes

* fix: need `fetch-depth: 0` for fetching tags to find what version to rev (#62) ([`e913a63`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e913a6346155b54949aa9bfdee9492b6208ba35d))


## v0.1.0 (2024-08-27)

### Bug Fixes

* fix: sentence casing fix (#61)

* fix: sentence casing fix

* chore: update actions to run on PRs

* chore: update publish workflow to use check workflow

* chore: add concurrency check ([`ea3c3cf`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ea3c3cfe7025e1a8f20742b20f30744699e7d4f2))

### Features

* feat: dependency violin chart support for nuget (#60) ([`d61b833`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d61b833fb36243bf27b685d9fff8e8587f4c4be1))


## v0.61.0 (2024-08-26)

### Bug Fixes

* fix: treat `version` as `string` and not `float` (#58)

Avoid truncation of `8.10` to `8.10` when rendering plot

fix https://github.com/moderneinc/moderne-visualizations-misc/issues/54 ([`bcf5ae5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bcf5ae5ffa77072173221d3e610547b2f1bfc454))

### Features

* feat: nuget dependency vulnerability visualization (#59)

modeled after java and npm variant ([`0d3a19f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0d3a19fed3be2d32a0bb7c40a4436edbf22ae6d2))


## v0.60.0 (2024-08-22)

### Chores

* chore: update github actions (#57) ([`fd1076a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fd1076af1817689620eec468a09a017578ed20d5))

* chore: update thumbnails for `find methods` visualizations (#56)

these are now data grids and custom yaml recipes

re: https://github.com/moderneinc/moderne-ui/issues/4671 ([`ae5ffbb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ae5ffbb9c60fb9be2b565a6b0d31fea81ab6ad72))

### Refactoring

* refactor(sankey): update color palette for sankey diagram (composite recipe results) (#55)

important to have length of `colors` array match number of nodes

fix https://github.com/moderneinc/moderne-ui/issues/4670 ([`2a30506`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2a30506d2eeb049932819d409d1b857c76bb9d1f))


## v0.59.0 (2024-08-14)

### Unknown

* Visualize Java versions in use as well (#53) ([`4b2e11c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4b2e11c71838dad0c9cb94e960fc7a89c16c5bef))

* remove legend ([`764fb6f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/764fb6fbb8d5ae4f94da9e7ff8a570140089f31f))


## v0.58.0 (2024-08-12)

### Chores

* chore: cleanup ([`63fcea6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/63fcea6000a786d38b2ade58280e4bef2b18ac33))

### Unknown

* spelling ([`9e48a2b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9e48a2bb102f3f6c87be335786b9d8afff74a4de))

* Change name for clustering embeddings viz to include classes ([`eb5a349`](https://github.com/moderneinc/moderne-visualizations-misc/commit/eb5a3497e513051ffe19d7151f9f56518fad885d))


## v0.57.0 (2024-08-07)

### Unknown

* Cleanup ai code search next steps (#52)

* change arguments from * to ..

* change arguments to .. and rename columns + cleanup unused df columns ([`89360ca`](https://github.com/moderneinc/moderne-visualizations-misc/commit/89360ca863881aea1396af7a3e473ece828d5bf3))


## v0.56.1 (2024-08-07)

### Bug Fixes

* fix(generate_yaml): add custom mime type ([`de23dbb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/de23dbb0e7f5aaf9ce2a38ea2676048c53954aa3))


## v0.56.0 (2024-08-06)

### Unknown

* Feat next steps method search (#51)

* datagrid for method patterns and generate yaml recipe

* typo

* add quotes around query for recipe description

* temporary ipython code display ([`188df06`](https://github.com/moderneinc/moderne-visualizations-misc/commit/188df0629e4aa11bf17ee923cfea6ce68ad9de7e))


## v0.55.0 (2024-08-06)

### Chores

* chore: update violin nodejs images ([`ae93ce4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ae93ce4e176c04e3b7fc8d701c6f2f701b517f5f))

### Features

* feat: add dependency_tree_view for insights ([`572880d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/572880d1ce85b25adad9c1b7f2a19669236a4f00))


## v0.54.1 (2024-08-05)

### Bug Fixes

* fix: update MANIFEST.in ([`5c3796b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5c3796bd71101d1d485d30df1954378d77904f3a))


## v0.54.0 (2024-08-05)

### Features

* feat: add violins for nodejs recipes ([`22e88ba`](https://github.com/moderneinc/moderne-visualizations-misc/commit/22e88ba80d5bd6d7796535ea85443cc884f9699a))

### Refactoring

* refactor: add resuable module ([`9be1981`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9be19818409035c6e1e4016fc7ab920c03a836c5))


## v0.53.1 (2024-08-05)

### Bug Fixes

* fix(dependency_tree_view_javascript): remove link ([`ce1953d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ce1953d3ac899dbdbb8ff75f5552a22b55d3809a))


## v0.53.0 (2024-08-05)

### Unknown

* Add a separate visualization for NPM vulnerabilities (#50) ([`d8648c5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d8648c59df5cfe174e76f5c02a330ac18c8d2aaf))


## v0.52.0 (2024-08-04)

### Chores

* chore: style cleanup ([`a249460`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a2494608f0a8c26227c102816033e638d214ce81))


## v0.51.0 (2024-08-04)

### Features

* feat: add dependency_tree_view_javascript ([`ae10f74`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ae10f74d441a3f7e918a747c2c19568b2f8f4aca))


## v0.50.2 (2024-07-12)

### Chores

* chore(text matches): limit to org.openrewrite.text.Find for now ([`b9c022e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b9c022e551d3981c162d9bf41d3e0442e035d5cb))


## v0.50.1 (2024-07-12)

### Bug Fixes

* fix(text matches): use better default ([`239e3fc`](https://github.com/moderneinc/moderne-visualizations-misc/commit/239e3fc9255f3c11be76c25aad7ac9737960d7b4))


## v0.50.0 (2024-07-12)

### Features

* feat: add text matches (#49) ([`a1f9524`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1f95248e3bcb85d0520701d888a43024be599d6))


## v0.49.1 (2024-07-11)

### Chores

* chore(github_secrets): updated image ([`a422fde`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a422fde77706a9ede292f35cb94c6012fac0e6f1))


## v0.49.0 (2024-07-11)

### Features

* feat: add GitHub secrets in use ([`92cc34d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/92cc34d8b3a4925cad7e7bc421182b21197b45ac))


## v0.48.0 (2024-06-20)

### Bug Fixes

* fix: use `1.24.4` instead (#47) ([`bdb0e29`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bdb0e29869f0e188bf6592d77ccab14131d49633))

* fix: lock numpy down to 1.x to avoid v2 incompat (#46) ([`0946862`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0946862327d19c991b4003a96a5ade858f4ffffc))


## v0.47.0 (2024-05-14)

### Unknown

* Feat visualization for recommendations (#45)

* use gradio client to search + display using moderne datagrid

* add yml for recommendatinos

* clean up ([`29cf70f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/29cf70fd561cb2e314966cd822c36ad915bfb5fa))


## v0.46.0 (2024-05-06)

### Refactoring

* refactor: update maven parent pom color scheme (#44)

utilize the `color_by_weight(500)` ([`7e3223d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7e3223d63ad06dba818323a02df83a86cd3ca474))

* refactor: update cont. color scale for recipe performance (#43)

use new palette

fix https://github.com/moderneinc/moderne-ui/issues/4273 ([`1112c02`](https://github.com/moderneinc/moderne-visualizations-misc/commit/1112c02122a5aad65b2ae7f64710bbd9f80901ac))

### Unknown

* changes to accept both methods and classes for clustering embeddings (#42) ([`8e80d75`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8e80d75d1b95fc6ebe64fc8a71474957e9152191))


## v0.45.2 (2024-04-30)

### Unknown

* Add defaults to Maven parent poms (#41)

Such that it produces meaningful visualizations directly from DevCenter ([`ff6c21d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ff6c21d952c88cf0c587f6f00c018876f6664a70))


## v0.45.1 (2024-04-25)

### Bug Fixes

* fix(embeddings): revert to previous color ([`d157dd4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d157dd4529f719cd8ed9d49b256eadd43de69f2d))


## v0.45.0 (2024-04-23)

### Unknown

* feat/updated colors (#40)

* feat: update to latest visualization colors

* refactor: update screenshots

* refactor: remove padding from screenshots

* chore: bump version of code science

* style: reformat ([`7827d26`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7827d268760d63143193805f465b835570d7a198))


## v0.44.0 (2024-04-16)

### Unknown

* empty datatable fail safe (#39) ([`06a860b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/06a860b575df4cb8c5eb9803a5b775863dde113a))


## v0.43.3 (2024-04-12)

### Bug Fixes

* fix(sql_crud): handle missing data ([`98387b9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/98387b980ff17a93907383d729be1f08d5b1dada))


## v0.43.2 (2024-04-12)

### Bug Fixes

* fix(sql_crud): scm types ([`be9553d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/be9553db21682e0ffc05cf5196d103fc788252ab))


## v0.43.1 (2024-04-12)

### Bug Fixes

* fix(sql_crud): link column ([`7e4de81`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7e4de818c54f5d723da1844f6f195a8df73be096))


## v0.43.0 (2024-04-12)


## v0.42.0 (2024-04-12)

### Features

* feat(sql_crud): add link column ([`30f6c43`](https://github.com/moderneinc/moderne-visualizations-misc/commit/30f6c434e370902b9535a27876ff0258c39c6541))


## v0.41.0 (2024-03-26)

### Features

* feat: Add named visualization specifically for Jackson ([`2601075`](https://github.com/moderneinc/moderne-visualizations-misc/commit/26010753963a0577c1fdb6dcf49c822337d4bc91))

### Unknown

* Jackson ([`aacb54b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/aacb54b8e7e617a546e39b2babc286a43367c1c2))


## v0.40.1 (2024-03-19)

### Bug Fixes

* fix(nodejs): update image ([`cacae7b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/cacae7bacaac6d791672ebaae783b44b3f3adf57))


## v0.40.0 (2024-03-09)

### Unknown

* Node.js dependency violin ([`d92ae6b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d92ae6b00007685f48d269e3f250732febf1140a))


## v0.39.1 (2024-03-08)

### Bug Fixes

* fix(violin): use correct recipes ([`0375921`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0375921957d6219140e6930b2099031624c36485))


## v0.39.0 (2024-02-29)

### Bug Fixes

* fix: Fix yaml for real ([`7eb7868`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7eb7868146fa7f2ef543754ddbc3dd8a9b4b12a2))

* fix: fix yaml ([`bff7957`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bff795729c1602970fcf55da6cb390fa594ed832))

### Unknown

* Use jackson for dependency insight (#37)

* Use jackson for dependency insight

* Update dependency_usage_violin.yml

* Update dependency_usage_violin_gradle.yml

* Update dependency_usage_violin_maven.yml ([`02c1906`](https://github.com/moderneinc/moderne-visualizations-misc/commit/02c19060e0e91bdd1af80ad9efdf6bf37e8e7a30))


## v0.38.0 (2024-02-23)

### Unknown

* change recipe path after reorganising ml recipes (#36) ([`a747f4c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a747f4c48d3abb4b13c3751543fec57f11a03e75))


## v0.37.0 (2024-02-12)

### Features

* feat(violin): add hover counts and improve legibility (#35) ([`207b04a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/207b04ac9b3b8f9cb464c22b412719bdab34c213))


## v0.36.5 (2024-01-23)

### Bug Fixes

* fix(violin): ensure version column isnt read as float ([`ce8eec6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ce8eec64ffb77d7e9ef7f1b0234d13a03d3e3f37))


## v0.36.4 (2024-01-18)

### Bug Fixes

* fix(spring_relations): scaling issue ([`fd3af6a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fd3af6a1f933d40ad5bf8c54a9e8519d0f2601b2))


## v0.36.3 (2024-01-18)

### Bug Fixes

* fix(spring_components): remove link due to issue ([`19ee5e5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/19ee5e540aa3be4790464949e20a4169234775e1))


## v0.36.2 (2024-01-18)

### Bug Fixes

* fix: link type issue ([`9a2c92a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9a2c92a3fa87fe5fcc440993dc4e7673716f2f87))


## v0.36.1 (2024-01-18)

### Bug Fixes

* fix: various fixes ([`f7057b8`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f7057b874102017d3e56d94d161ecee7f00ae5c8))


## v0.36.0 (2024-01-18)

### Chores

* chore: file name typos ([`9874e07`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9874e0722b540e92458c7839ea4cd3b5d326a9d5))

### Continuous Integration

* ci: add ignore words to sentence casing check ([`3b1fa91`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3b1fa91e06ec3858d8c21af07dd7db7c5ffa38e4))

### Features

* feat: add spring component visualizations ([`8f51080`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8f5108078379a5b83312bf0e28ca5fd46a9e3f19))


## v0.35.1 (2024-01-17)

### Bug Fixes

* fix(eslint): update data table name ([`ef16017`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ef1601778277a65c936d994747e10d05f495c98e))


## v0.35.0 (2024-01-17)

### Chores

* chore: more clean up ([`10b516d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/10b516d320ceb394a0d3845e5a1c204e1b53c760))

* chore: clean up and format ([`8583d87`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8583d87c142743f97f0f50e3a22e69ad2e86f420))

### Features

* feat(language-comp): improve simple text mapping based on file extensions ([`32d6235`](https://github.com/moderneinc/moderne-visualizations-misc/commit/32d6235c9c5a3c617e18f69c8868da3231415ddb))

### Unknown

* Add visualization for ESLint (#31)

* Add visualization for ESLint

* Update notebook

* Update notebook

* Clear cell outputs

* "Correct" case of `Eslint`

* Fix some more minor issues

* Polish ([`456ce3c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/456ce3cb70e3066a11d5511a99d54daf60688261))


## v0.34.0 (2024-01-09)

### Unknown

* Changed from TSNE to UMAP for 2D projection (#30)

* Changed from TSNE to UMAP for 2D projection

* added umap dependency

* fix umap dependency

---------

Co-authored-by: juju <justine.gehring@gmail.com> ([`4811028`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4811028916bc125bd2acb5ad8dff7fb7a9e69e40))


## v0.33.3 (2024-01-08)

### Bug Fixes

* fix(violin): add a min height to figure for readability ([`a22b3bb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a22b3bb23bf6cd09d140e105f5c17c04540ea4a4))

### Chores

* chore: clear outputs ([`13ac74a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/13ac74a97a70e879342ea772416d5d8a157931d6))

* chore: formatting ([`e75d91e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e75d91ec6c1d35cc59a2afb69abb9be8c5210a3f))


## v0.33.2 (2024-01-08)

### Unknown

* Lower timeout, reorder legend, change embds (#29)

* reorder legend, change embeddings, and fix perplexity for small datatable

* lower perplexity

---------

Co-authored-by: juju <justine.gehring@gmail.com> ([`0193da9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0193da90f9f903154e582da6c8eeef922b62628e))


## v0.33.1 (2024-01-08)

### Unknown

* typo ([`894c2c0`](https://github.com/moderneinc/moderne-visualizations-misc/commit/894c2c0dd4454d344e0bd6813c8944da70dadd7b))

* Update embeddings_clustering.yml (#27) ([`e178fff`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e178fffb81db675333afd455d5b17c75829aef78))


## v0.33.0 (2024-01-08)

### Unknown

* fix yml ([`d81a36f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d81a36fca42a9a14137ddb80abec13e24d7b5b03))

* more moderne colors + fix name yml ([`8597485`](https://github.com/moderneinc/moderne-visualizations-misc/commit/859748562b228931d960353a7d9ef3daf3649290))

* adding embedding clustering yml file ([`8e31c8d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8e31c8df1694c073c35f2d52e2d5560aedf939f7))

* clustering methods or classes ([`f7ac8da`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f7ac8da527819c7bb011ac2baac29eadbf67af62))


## v0.32.3 (2023-12-06)

### Unknown

* Fix copy & paste error ([`13cd075`](https://github.com/moderneinc/moderne-visualizations-misc/commit/13cd07570f3c8d615b664b103ce10c6a21227fc4))


## v0.32.2 (2023-12-06)

### Unknown

* Duplicate violin chart for the other recipes which use it ([`4296c89`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4296c89ea0ac1f77376fce5d6628da709eddba59))


## v0.32.1 (2023-11-30)

### Chores

* chore: bumping code-data-science version for bug fix ([`160c237`](https://github.com/moderneinc/moderne-visualizations-misc/commit/160c2375db8778389b9aa5dfad85e8739a0d8308))

* chore(dependency_usage_violin): sentence casing ([`bc879d7`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bc879d7d62cf51594349b2b88976166a6249a57d))


## v0.32.0 (2023-11-30)

### Chores

* chore: formatting and polish ([`9125462`](https://github.com/moderneinc/moderne-visualizations-misc/commit/91254625d05a057dc4eeca8e730c17bc5581b8b6))

### Features

* feat: add dependency usage violin ([`5234f14`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5234f1410333fb300b7f1c79149cede465b57f16))

### Unknown

* Improve descriptions ([`e020857`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e02085772cccea24d314de50d34f65d218d5fe72))

* Fix up some thumbnails ([`80ea73e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/80ea73e1d54cb2e2af26d88915e18fa6d0196ba2))


## v0.31.1 (2023-11-18)

### Chores

* chore(sankey): update scaling and description ([`aad3949`](https://github.com/moderneinc/moderne-visualizations-misc/commit/aad3949c58a0fa1460a19d76a7209f8fcffbd912))

* chore(sankey): remove unused import ([`faddce2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/faddce2e9e190ababe1942def3c3b6c0ffa268c4))


## v0.31.0 (2023-11-18)

### Bug Fixes

* fix(sankey): add count threshold to spec ([`00469f2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/00469f25855dcbbf1a23b8087cfe5eb009f890af))

### Chores

* chore: fix formatting ([`e00bdcf`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e00bdcfe17e6c75faf40097f16f9b1e2e4ec4359))

### Features

* feat: add composite recipe results sankey ([`c5f9ec7`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c5f9ec70b6a59b37b00c166440c3a4fe1efb978d))


## v0.30.3 (2023-11-11)

### Documentation

* docs(recipe_performance): correction regarding default ([`a1c9924`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1c992433ad43369f2714c9b1a37bdf5384c2acf))


## v0.30.2 (2023-11-11)

### Bug Fixes

* fix(recipe_performance): add minimum plot height ([`208978d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/208978d4d9e4f74afd066211e68ecf7fd65749b1))


## v0.30.1 (2023-11-10)

### Chores

* chore: update recipe performance spec to all recipes ([`6c1e15c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/6c1e15c8c6f6ab7fcddaa89ca096df9cdc2ae6ce))


## v0.30.0 (2023-11-10)

### Chores

* chore: update pyproject.toml ([`c2895bc`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c2895bc15f0d43c154ee9a5aebc4f5070a4a8790))

### Features

* feat: Add unit measurement to language composition notebooks (#25) ([`f8ee8ac`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f8ee8acdd01d267597e258d5f8f1e90f5f364dff))

### Unknown

* Adding image for comment language distribution viz ([`a6cebe5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a6cebe547f6d1de96521fd0f758e496b9aa869df))


## v0.29.1 (2023-10-26)

### Chores

* chore(recipe_performance): convert to seconds ([`3025838`](https://github.com/moderneinc/moderne-visualizations-misc/commit/30258386fc9b57c9f8112fb4315b2beefb84340c))


## v0.29.0 (2023-10-26)

### Bug Fixes

* fix(recipe_performance): parameter top_n int conversion ([`34718e4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/34718e4c9705157a67627c5b3d2e8c56a3898525))


## v0.28.1 (2023-10-26)

### Chores

* chore: specify recipe for recipe_performance ([`82840dc`](https://github.com/moderneinc/moderne-visualizations-misc/commit/82840dcf6ed38b3043b4c4de305f59430de87228))

* chore: formatting ([`f54ad25`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f54ad2561a1cf93ea17a5258545027887821658f))


## v0.28.0 (2023-10-26)

### Features

* feat: add recipe_performance ([`b13106c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b13106c74bb78b8b9e2cfca7ac1d1cf6354543de))


## v0.27.1 (2023-10-03)

### Bug Fixes

* fix(language_comp): support column rename sourceFileType ([`9ac123c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9ac123c8fb0770f8a6e0bfb088a2d3c24539f728))

### Unknown

* Add preview image for maven parent poms ([`7142ed4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7142ed4c04a6c601595823c38870ba3c7672b0ff))

* Add explicit legend ([`640b2f4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/640b2f4a53139a0ea7dbdc9d78458abf821b70e6))

* Update README to include running locally ([`51bd92b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/51bd92bf676304fd6f382f6d803550148a6ea127))

* Add samples after rename projectArtifactId & drop datedSnapshotVersion ([`c1eb9b3`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c1eb9b335833d9ad98aad78a0ad469334526efcf))


## v0.27.0 (2023-09-30)

### Unknown

* Visualize Maven parent POM artifactIds & versions in use (#24) ([`f223ef4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f223ef427dd31ed255d2689e40ee3ef9f96c66b3))


## v0.26.1 (2023-09-26)

### Chores

* chore(dependency_vulnerabilities): update description ([`e6b49c6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e6b49c62730e693d439232ec25ccc97cea7650c7))


## v0.26.0 (2023-09-26)

### Features

* feat(dependency_vulnerabilities): add repo filter option ([`f518777`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f518777ced2a23ec3991f53e8537f03d4fa0bcab))


## v0.25.0 (2023-09-25)

### Unknown

* Java versions by source set ([`9353b3c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9353b3c8ea691378d4becef0fed122e9dd6524d8))


## v0.24.0 (2023-09-21)

### Unknown

* adding other category ([`1bd710d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/1bd710db10df0f30e8b6c53834581a543f9f2de2))

* Merge branch 'main' of https://github.com/moderneinc/moderne-visualizations-misc ([`2bcf996`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2bcf99607a934f5f9d5a4c87aca83610bcb344bc))


## v0.23.0 (2023-09-21)


## v0.22.0 (2023-09-19)

### Bug Fixes

* fix(comment_lang): update recipe and dataTable ([`0a44876`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0a4487676d6e15b0dfadcbf5bc66e929b52649b2))


## v0.21.0 (2023-09-19)

### Unknown

* adding unknown to dict of languages ([`6623df2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/6623df2a50a1670caf362dd15b18975468d4ec3e))

* fixing sentence case ([`992ef06`](https://github.com/moderneinc/moderne-visualizations-misc/commit/992ef06a0c6019469b02437fa0a64f0d95623e39))

* typo ([`27645f9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/27645f97dbaaf60808e5d138bef329511b89dbd3))

* typo ([`e51aa30`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e51aa305850641e81dc855b14370ab082acb1802))

* visualization added for language comment distribution ([`d12ab12`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d12ab12969c6955f995281458ef519c523fb867a))


## v0.20.1 (2023-09-13)

### Chores

* chore(dependency_tree_view): add image ([`420897c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/420897c2c4a10996a70b418a62169fa5eef09ffe))


## v0.20.0 (2023-09-13)

### Features

* feat: add dependency_tree_view ([`06d16b1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/06d16b10ed5fa3c8a413d871ca8b0004893ab472))


## v0.19.4 (2023-09-05)

### Chores

* chore: sentence casing ([`fad64f0`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fad64f0060afa5b20f43bf9e3c4ce15af3814753))

### Unknown

* Update displayName of ParseFailureStacktraces ([`8822467`](https://github.com/moderneinc/moderne-visualizations-misc/commit/88224678ce271fe0863a6629421e8af118574270))


## v0.19.3 (2023-09-05)

### Bug Fixes

* fix(call_graph_uml): address backward link creation ([`f4f8738`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f4f8738898ce152b2414fa26900fcbc605cfaccf))

### Chores

* chore: run formatting ([`cc24328`](https://github.com/moderneinc/moderne-visualizations-misc/commit/cc24328631ca74fcb674c628de257a5ae42e6f57))


## v0.19.2 (2023-09-05)

### Bug Fixes

* fix(call_graph_uml): addres bad hierarchy with inner classes ([`5a6559d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5a6559def1815c2354abcdb4f4766bd29214b676))

### Chores

* chore: update plantuml jar ([`db92036`](https://github.com/moderneinc/moderne-visualizations-misc/commit/db920361d4956984a0475fa4efa1444e5626ae5c))


## v0.19.1 (2023-09-01)

### Chores

* chore(parse_failure_stacktraces): update image ([`2523496`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2523496788889be382066dd6716496008d735796))


## v0.19.0 (2023-09-01)

### Chores

* chore(parse_failure_stacktraces): clean outputs ([`4866f3d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4866f3de47ed73bbcce0c5ffa4bc463bed4a7a42))

* chore(parse_failure_stacktraces): trying as data grid ([`3ee1458`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3ee14583402c6c354e31d285a3c6ae8cb5d6b3c4))

### Unknown

* add parse-failure-stacktraces image ([`e07ff30`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e07ff301b06ca9e266f88cef19c275b936f9c786))

* add parse_failure_stacktraces.yml ([`83a8294`](https://github.com/moderneinc/moderne-visualizations-misc/commit/83a82940cc68b65553acbfebfea12bd19af03dfc))

* Add parse failure stack trace grouping and top10 failures display ([`f913a19`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f913a197b7d5469a952b3cbda52fffe42daea28e))


## v0.18.2 (2023-09-01)

### Continuous Integration

* ci: cleanup local things ([`f28f587`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f28f587d91d646842d49ada9846a46e5db099ee8))

* ci: prevent publish unless checks pass ([`d2d5d8e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d2d5d8ee3c0bd9623f22648ed72bf0e4f2cbaa70))

* ci: add tasks to check options and casing ([`f1c6883`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f1c68837cc83a0414a7efdabdfecfac8aa7f09ab))

### Documentation

* docs: update README ([`18d75df`](https://github.com/moderneinc/moderne-visualizations-misc/commit/18d75df9c3147df05939bf6c07a0a4bf90520d87))


## v0.18.1 (2023-08-31)

### Unknown

* Render inner classes in the call_graph_uml. ([`e3be531`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e3be531de20d611025858445675c561186464d34))


## v0.18.0 (2023-08-30)

### Features

* feat: call_graph_data_grid ([`3cd1321`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3cd132104e5c30fc193351c71d87311c1f748cc3))


## v0.17.4 (2023-08-30)

### Chores

* chore(call_graph_uml): raise exception if df empty ([`a1edefb`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1edefbfe73f13ef3a6bf611c1a5e5172ee7d903))


## v0.17.3 (2023-08-30)

### Chores

* chore: update manifest to include resources ([`037c28d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/037c28d909e43757f389631ab1b71a7e674f6e6f))


## v0.17.2 (2023-08-30)

### Chores

* chore(call_graph_uml): more cleanup ([`6ee728f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/6ee728ff6d00383c24b369a8cbb3e4ead4608b42))

* chore(call_graph_uml): cleanup ([`4385818`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4385818fb106bc559afb1150581ed0162ad349e9))


## v0.17.1 (2023-08-30)

### Chores

* chore(call_graph_uml): use local plantuml ([`cc87e3f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/cc87e3fa9e6e09352bd5c78a40f6c1433f89b357))


## v0.17.0 (2023-08-30)

### Bug Fixes

* fix: Typos in call graph yaml ([`997b4d2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/997b4d2314efa3bf1522a3ea028c2ada3b8bb751))

### Unknown

* Filter df if filter_by_fqn is provided. (#22)

Prevent inner classes relationships, since it causes an issue in UML (requires creating inner classes in the template). ([`a64544f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a64544fca60ba66eab9c8c70cd193478a086602c))


## v0.16.2 (2023-08-29)

### Chores

* chore: move older yml to dev mode ([`9eb1499`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9eb14996f4fe876cbca09295e0d9ab6435c9d524))


## v0.16.1 (2023-08-29)

### Chores

* chore(call_graph_uml): add parameters tag ([`7946989`](https://github.com/moderneinc/moderne-visualizations-misc/commit/794698937df80796ec8de6fe744fc25815296ac1))


## v0.16.0 (2023-08-29)

### Features

* feat: add call_graph_uml ([`c81fc11`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c81fc110862db1c61ebbfa57d8710b1c15edbd5f))

### Unknown

* Call graph (#21)

* Call graph vis WIP

* chore: add uml notebook

* chore: update dependency

* Renamed uml variant to call_graph_uml.
Added filtering by FQN and method name.
Started update for call_graph with graphviz.

* poe format

* Updated call_graph_uml name with UML.

---------

Co-authored-by: Sam Snyder <sam@moderne.io>
Co-authored-by: Kyle Scully <scullykns@gmail.com> ([`2895601`](https://github.com/moderneinc/moderne-visualizations-misc/commit/289560176e54a454bd682528b31d3da6ef40befb))


## v0.15.0 (2023-08-29)

### Bug Fixes

* fix: Add node_shape for io.moderne.FindCallGraph ([`f3f55ae`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f3f55aed98eaffc80125e79d992afc95ee95caa8))


## v0.14.0 (2023-08-29)

### Unknown

* Basic call graph ([`7a7af62`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7a7af62bbd67fd004f6912a1aa76b5a518dd59aa))

* Call graph vis WIP (#18)

Co-authored-by: Sam Snyder <sam@moderne.io> ([`d4be066`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d4be06651311e1cedb223d848fdcfb39d6bcc79d))

* Added nodesep and removed minLen. ([`393455b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/393455b26b3144734f48cccd87c34727cff9c571))


## v0.13.1 (2023-08-25)

### Bug Fixes

* fix(cobol_relationships): escape html annotation ([`e42b14d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e42b14dabf2ed5cbe674cca511e8b237574fc9f2))


## v0.13.0 (2023-08-25)

### Features

* feat(maven): Add effective maven settings data grid (#17) ([`34cf41a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/34cf41a441d01096012276405ec8574af7cb06e1))


## v0.12.1 (2023-08-24)

### Bug Fixes

* fix(cobol_relationships): update size ([`3c4a4a6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3c4a4a60cd87ec4f1bfe1d06db02b9f7e401d3a6))


## v0.12.0 (2023-08-24)

### Features

* feat: Add language composition by repository (#16) ([`ab0c328`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ab0c328ea4e5c3a6668ff76131cb41cb9f1fc5e1))


## v0.11.0 (2023-08-24)

### Unknown

* Change engine back to sfdp ([`e873023`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e87302361b84874274c4d1b017bd27ab02b6085d))


## v0.10.0 (2023-08-24)

### Unknown

* Set overlap_scaling to 30.
Updated engine to neato. ([`c96dc47`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c96dc47e69fa626f19b4f09c5e99843eefa4f07c))


## v0.9.0 (2023-08-24)

### Unknown

* Expanded viewable relationships through filter. (#15)

Added option to view exclude relationships.
Create a unique shape for filtered node. ([`d5d339b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d5d339bd7c16e4d5c3b5a7a7339d70766680d671))


## v0.8.0 (2023-08-23)

### Unknown

* Added normalization graph config. Added beautify for filtered graphs for easy readability. ([`1e13558`](https://github.com/moderneinc/moderne-visualizations-misc/commit/1e1355878bdf9cdc0cd8ee05bc5383f388d7b321))


## v0.7.0 (2023-08-23)

### Unknown

* Removed graph layout option settings. (#14)

Set engine to "sfdp" and added configurations for clearer clustering. ([`44534d5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/44534d57b2b47632e80266e485e95f02df0ff48a))


## v0.6.0 (2023-08-23)

### Features

* feat: add parameter for defining graphviz layout engine (#13) ([`9ee166e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9ee166ef585e29626dc344bb7ecd75fb61391a1a))


## v0.5.0 (2023-08-22)

### Unknown

* Fix relationships for copybooks that to refer to more than 1 copybook. ([`13efd0c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/13efd0c8bd7010f0daed817559dee7972e84f26b))


## v0.4.0 (2023-08-22)

### Unknown

* Prevent redundant copybook relationships. (#12) ([`1ada2b3`](https://github.com/moderneinc/moderne-visualizations-misc/commit/1ada2b3b26c145b92b20b633c4923c11b692cf73))


## v0.3.1 (2023-08-22)

### Chores

* chore: move parse_failure_analysis to dev ([`4213578`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4213578172bc4edbd83b05307d241330a19dbd23))


## v0.3.0 (2023-08-22)


## v0.2.1 (2023-08-21)

### Unknown

* Updated SQL relationship colors for visibility (#11) ([`788945e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/788945ee6126bb9756621324482ae7cf7f40b2af))


## v0.2.0 (2023-08-21)

### Features

* feat(sql_crud): add option to filter operations ([`4527362`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4527362492dab1b35e2ced37e634db774a3af1c5))


## v0.1.38 (2023-08-18)

### Continuous Integration

* ci: update ([`f09411f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f09411fb9c3dd4e548bce569da7e30f078a8545d))

* ci: add version bumping to release ([`ca7ba04`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ca7ba048426387a25beb271185953ed1ab29ebf3))


## v0.1.37 (2023-08-17)

### Chores

* chore: update project stuff ([`2769aef`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2769aef1bcc8a05093c3ca8122482c805d59ed65))

* chore: seperate ci only deps ([`8b7afd1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8b7afd17f69e7b7f656f4cb3b3007a4e12d2a9a2))


## v0.1.36 (2023-08-17)

### Bug Fixes

* fix(cobol_relationships): remove unused option ([`a671671`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a671671c25250b09695ef650553576bf1ef22b1f))

* fix: remove extra empty cell and clean outputs ([`43a9d3a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/43a9d3a6353969d84570dbdf7fcb0f1f923c35fa))

* fix(language_comp): clear cells ([`0ed34d9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0ed34d9f83044441690e4a3eed05e2cf84b5a3d7))

* fix(language_comp): seperate plot into its own cell ([`6f1a52c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/6f1a52ce624fed7c04dc1b9fa0d64125648850ce))

* fix(language_comp): remove extra cell ([`27854c4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/27854c403bb987e6522780ce5f95a850ba8cf8fb))

* fix(language_comp): update dependencies ([`b9ea3ad`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b9ea3ad4bcdd5767f92cfc03ff2ed00eaee55f93))

* fix: dependency vulnerabilities imports ([`c2f42b6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c2f42b6ef1b5a9e46f735f8ceb24b4d9d72fdeed))

### Chores

* chore: clean up ([`5dcbe30`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5dcbe30e4311f3f8a0b46a08b2e12e46364fac6e))

* chore: update dev deps ([`3d3bbc2`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3d3bbc251b274e686c5fe2310c02340f39635871))

* chore: bump version ([`a1fa7a6`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a1fa7a6cd8146117176b792b07bbb48252853871))

* chore: bump version ([`e7d7f0d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e7d7f0d7e2144f122207a4554e1b7ebc284d5032))

* chore: update images ([`d3a901f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/d3a901fa61cf240f19c77392be13eab4b2ed768f))

* chore: bump version ([`04d4932`](https://github.com/moderneinc/moderne-visualizations-misc/commit/04d4932d40ee7bc4ad7b1fc984675fc4466f1597))

* chore: bump version ([`c1e08e1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c1e08e19dd0a1fe8fe0c7f48a1c881c3d8e23cdc))

* chore: bump version ([`500f5e1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/500f5e1cefb751f82e29c5fa613e4e646b48fb76))

* chore: bump version ([`fcff20c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fcff20c85078fc703dfefae5a2002a0c0e1d2014))

* chore: run formatting ([`735b031`](https://github.com/moderneinc/moderne-visualizations-misc/commit/735b031eb90065bc8fb13b862623c8b448e81f0c))

* chore: add type checking ([`8c59f57`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8c59f574f73745b89948032cebbf4668fd504409))

* chore: more option support ([`e97331b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e97331b0d61406177d1883364401dc4a34f62a92))

* chore: bump version ([`b90933c`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b90933c98fce38cac04ffae75a32cbfee8477251))

* chore: clean up ([`f0d861b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f0d861b4ae25b316aa7dd4af9a25c2df1c0fcf94))

* chore: update code_data_science ([`27a01f9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/27a01f98d38d3ac7476bcf7c3a6cb8f23ff8972f))

* chore: bump version ([`b63c1d3`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b63c1d35274cfec317ffd4e283d00dce5e895232))

* chore: bump version ([`90c7513`](https://github.com/moderneinc/moderne-visualizations-misc/commit/90c75135ee342d35f527e2a4aced0d53098c34d4))

* chore: update dependencies ([`2a6d2ac`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2a6d2ac6314401eada3574b4e0afceadb929aa19))

* chore: bump version ([`43672ed`](https://github.com/moderneinc/moderne-visualizations-misc/commit/43672eddaab8c8eca231f881cec67737d6e83f12))

* chore: bump version ([`8bbb49b`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8bbb49b91666b032aa019025e528afa0de1efad9))

* chore: bump version ([`0f29dab`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0f29dabed88c70fd8e4bf14ef95fadb9b4c47837))

* chore: add plotly dependency ([`b2d735d`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b2d735def13791930bf298fb230b585aa2f9beba))

* chore: bump version ([`e8ab9a1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e8ab9a18e87488d49a8ace0be7c5238f5a09dcbd))

* chore(dependency_vulnerabilities): remove height restraint ([`e5320d9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e5320d96802957fe4524187a55567087c8d6f68e))

* chore: bump version ([`f560495`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f56049578714a05585cfd20dba75bf83d2a9fd51))

* chore: update gitignore ([`970e3f5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/970e3f53f25b35280988fe5ab08d500d3da6520e))

* chore: add more samples ([`77952b1`](https://github.com/moderneinc/moderne-visualizations-misc/commit/77952b119e2c179280013b52689066ff450111ac))

* chore: exlude samples directory in publishing ([`dc60d3a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/dc60d3a486eca22af797c28edbfaba373629b7a7))

* chore: changing version for initial publish ([`2ec9b59`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2ec9b59f59598474bd5d52cd35b0f9846081d3ea))

* chore: add preview images ([`93b2dd0`](https://github.com/moderneinc/moderne-visualizations-misc/commit/93b2dd0f4e8998f6f0c003e1e0e08a1860bd25bc))

### Features

* feat: add language comp by folder (#8)

Co-authored-by: Sam Snyder <sam@moderne.io> ([`dd66434`](https://github.com/moderneinc/moderne-visualizations-misc/commit/dd66434ef89584910c6f7e1898cd3f3fe8f8d1c1))

* feat: add cobol relationships data grid ([`7f4d2e8`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7f4d2e8b179af4dc594ae7311bdbe45ff58e076b))

* feat(cobol_relationships): add new option to filter to resource ([`0af3dec`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0af3dec43d49b1f09c162fad4e4ef4dbddc6f071))

* feat: add colors to cobol ([`96cfd4f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/96cfd4fdfc0718cb6067f33ebb592fef104ce06d))

* feat(gradle_wrappers): update colors ([`e619282`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e619282a5a90d618deea463694627fc5195532b9))

* feat: add github action ([`f65fbd9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f65fbd961c675c3ed958b1ef7b7aee0c499b98e5))

### Unknown

* Added SQL_CURSOR (#9) ([`e52c150`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e52c1505ea9c759a946b30a7827cdd99481613d3))

* Bump version ([`4ce2674`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4ce2674af7fa86f023fde9060cccceb663f57c0d))

* Separate relationships by node and type. (#7) ([`9de0927`](https://github.com/moderneinc/moderne-visualizations-misc/commit/9de09277a50ce2227aa37f8ac8195edfd9fa243b))

* Update cobol relationships. (#5) ([`a684629`](https://github.com/moderneinc/moderne-visualizations-misc/commit/a684629af024c08eebbddca96503af9c321fa54f))

* Add arguments to cobol_relationships (#4) ([`bf532ac`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bf532aca8903cc84230122e488affc7642d47e02))

* Add lst_provenance viz ([`2ae3683`](https://github.com/moderneinc/moderne-visualizations-misc/commit/2ae3683e1c107810a8c23b81ad5570792326db32))

* Better preview ([`0a3eb80`](https://github.com/moderneinc/moderne-visualizations-misc/commit/0a3eb807b574655ff2f9ef1a47b8ccb805fd40a1))

* Bump version and add preview image ([`df12dd4`](https://github.com/moderneinc/moderne-visualizations-misc/commit/df12dd4f66c4f83ee4cc564b4bec3bdadc7cd328))

* Merge branch 'main' of https://github.com/moderneinc/moderne-visualizations-misc ([`f9ea0c9`](https://github.com/moderneinc/moderne-visualizations-misc/commit/f9ea0c9fe05cbf571c008dcaff753024dcfbde35))

* Merge pull request #3 from shanman190/feature/gradle-wrappers-image

Add preview image for gradle wrapper visualization ([`8cb35e3`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8cb35e3f9cdc697a8daf419f7552ee08655e35d2))

* Add preview image for gradle wrapper visualization ([`5b74d35`](https://github.com/moderneinc/moderne-visualizations-misc/commit/5b74d35469c0c34d34cc1cb296ba2389a3931227))

* Merge pull request #2 from shanman190/main

Add gradle wrapper visualization ([`3693164`](https://github.com/moderneinc/moderne-visualizations-misc/commit/3693164d34fb136367ae212cbcdac584edd851f8))

* Add gradle wrapper visualization ([`b3243bc`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b3243bcc76ef9f14aac2e93441a28cc51e4223f3))

* Update samples to include bindcard bindplan linkedit ([`c6430b3`](https://github.com/moderneinc/moderne-visualizations-misc/commit/c6430b317e62f6d474b8fed572977389591b998c))

* Clear outputs ([`62b79d5`](https://github.com/moderneinc/moderne-visualizations-misc/commit/62b79d53d584504df8417f2512b55dedaf84ad1b))

* cobol relationships ([`fbf8e7e`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fbf8e7e1ee1dd4c1a5efb22a3a5092e176af9883))

* Back to svg ([`219e756`](https://github.com/moderneinc/moderne-visualizations-misc/commit/219e756f1a0a76edacf4b94e2514df3202bcc307))

* Copybook output as png for now ([`4bb6a56`](https://github.com/moderneinc/moderne-visualizations-misc/commit/4bb6a564528c07478ec13c30dd53a07f7483e5aa))

* Remove outputs ([`ec5ced0`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ec5ced03556bfb2578c3d4869bec843e67f43e90))

* Fix copybook viz ([`8861ead`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8861eade6577a5664501bf6faddc19eb9e80bae3))

* Add sdfp layout for copybook viz ([`bdc96fe`](https://github.com/moderneinc/moderne-visualizations-misc/commit/bdc96fe0632bb3959d61449e1dfa2da3cbfc3e7f))

* Update copybook viz ([`13afedd`](https://github.com/moderneinc/moderne-visualizations-misc/commit/13afedd35b91a5af465d2efa976e20ed7379def3))

* Fix copybook viz ([`7ad4b09`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7ad4b09db1b97ddaa72c84fc433bb776645bd74e))

* Copybook not copy book ([`b035799`](https://github.com/moderneinc/moderne-visualizations-misc/commit/b035799e942b8a3370c8edf7427f3435ca9cb292))

* Add SourceFileModelTypes ([`53e975a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/53e975ad9c7ffb0525d03d0180498a1f19cd9155))

* FindMethods ([`e82501a`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e82501a9150798e69e72472f546b758ab7f0170c))

* First COBOL graph visualization ([`8027d66`](https://github.com/moderneinc/moderne-visualizations-misc/commit/8027d66d75fded677c457fc1f55b20b4f7c2977c))

* Add ipynb ([`7cfc289`](https://github.com/moderneinc/moderne-visualizations-misc/commit/7cfc289246ec0b4797408f96db4c3962f2122501))

* MANIFEST.in ([`fadd64f`](https://github.com/moderneinc/moderne-visualizations-misc/commit/fadd64f960eb166075ba6a74f8df87b4ed9c921f))

* Bump version ([`e8f6d39`](https://github.com/moderneinc/moderne-visualizations-misc/commit/e8f6d3911d9157f85dfb6732642cc030a6b8dc0f))

* code_data_science==1.1.4 ([`ab6b4e8`](https://github.com/moderneinc/moderne-visualizations-misc/commit/ab6b4e81cadcd89d1422089b93e2f5b9b5ea9884))

* Sample ([`cb94749`](https://github.com/moderneinc/moderne-visualizations-misc/commit/cb94749f3379acf27df1f9b148fef23bfa3ad11f))

* Initial import ([`43cf672`](https://github.com/moderneinc/moderne-visualizations-misc/commit/43cf672a9cba9f10d20d7459f20a3df7ac4d11c7))
