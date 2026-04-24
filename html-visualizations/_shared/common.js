/* Shared helpers for html-visualizations tools.
   Expects Plotly + Papa Parse to be loaded in the host page. */

// --- Dropzone wiring ---

function wireFileDrop({ dropId, inputId, dropTextId, onRows }) {
  const drop = document.getElementById(dropId);
  const input = document.getElementById(inputId);
  const dropText = document.getElementById(dropTextId);

  drop.addEventListener('click', () => input.click());
  drop.addEventListener('dragover', e => { e.preventDefault(); drop.classList.add('drag'); });
  drop.addEventListener('dragleave', () => drop.classList.remove('drag'));
  drop.addEventListener('drop', e => {
    e.preventDefault();
    drop.classList.remove('drag');
    if (e.dataTransfer.files && e.dataTransfer.files[0]) parse(e.dataTransfer.files[0]);
  });
  input.addEventListener('change', e => {
    if (e.target.files[0]) parse(e.target.files[0]);
  });

  function parse(file) {
    Papa.parse(file, {
      header: true,
      dynamicTyping: false,
      skipEmptyLines: true,
      complete: (results) => {
        dropText.innerHTML = `<strong>${escapeHtml(file.name)}</strong> loaded (${results.data.length.toLocaleString()} rows). Click to choose a different file.`;
        onRows(results.data, file.name);
      },
      error: (err) => {
        dropText.innerHTML = `<span class="error">Parse error: ${escapeHtml(err.message)}</span>`;
      }
    });
  }
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({
    '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
  }[c]));
}

// --- Download a rendered chart as a single, self-contained HTML file. ---

function downloadStandaloneChart(chartDivId, filename) {
  const gd = document.getElementById(chartDivId);
  if (!gd || !gd.data) return;
  const payload = JSON.stringify({ data: gd.data, layout: gd.layout });
  const title = (gd.layout && gd.layout.title)
    ? (typeof gd.layout.title === 'string' ? gd.layout.title : (gd.layout.title.text || 'Chart'))
    : 'Chart';
  const safeTitle = String(title).replace(/<[^>]+>/g, ' ').trim();
  const html =
`<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>${escapeHtml(safeTitle)}</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"><\/script>
<style>body{margin:0;font-family:sans-serif;} #c{width:100vw;height:100vh;}</style>
</head><body><div id="c"></div>
<script>const p=${payload};Plotly.newPlot('c',p.data,p.layout,{responsive:true});<\/script>
</body></html>`;
  const blob = new Blob([html], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename || 'chart.html';
  a.click();
  URL.revokeObjectURL(url);
}

// --- Utility helpers used across tools ---

function parseNum(v) {
  if (v === null || v === undefined || v === '') return 0;
  const n = parseFloat(v);
  return isFinite(n) ? n : 0;
}

// Header normalization for Moderne data-table CSVs. The platform emits two
// shapes of the same tables: raw camelCase (used by the Python notebooks
// and `samples/*.csv` in this repo), and the human-readable title-case
// shape that `.moderne/context/*.csv` files on disk use. Normalize both
// to camelCase so every tool reads one schema.
const HEADER_MAP = {
  // project / repository
  'repository origin': 'repositoryOrigin',
  'repository path': 'repositoryPath',
  'repository branch': 'repositoryBranch',
  'source path': 'sourcePath',
  'source file': 'sourceFile',
  'project name': 'projectName',
  'project artifact id': 'projectArtifactId',
  'source set': 'sourceSet',
  'source set name': 'sourceSetName',
  // class- / method-level quality
  'class name': 'className',
  'method name': 'methodName',
  'method signature': 'methodSignature',
  'line count': 'lineCount',
  'method count': 'methodCount',
  'field count': 'fieldCount',
  // metric abbreviations: all-caps in the human-readable export, lowercase everywhere else
  'wmc': 'wmc', 'lcom4': 'lcom4', 'tcc': 'tcc', 'cbo': 'cbo',
  'maintainability index': 'maintainabilityIndex',
  'cyclomatic complexity': 'cyclomaticComplexity',
  'cognitive complexity': 'cognitiveComplexity',
  'max nesting depth': 'maxNestingDepth',
  'parameter count': 'parameterCount',
  'abc score': 'abcScore',
  'halstead volume': 'halsteadVolume',
  'halstead difficulty': 'halsteadDifficulty',
  'halstead estimated bugs': 'halsteadEstimatedBugs',
  // single-word capitalized headers that still need case normalization
  'language': 'language',
  'version': 'version',
  'description': 'description',
  'name': 'name',
  // code smells
  'smell type': 'smellType',
  'severity': 'severity',
  'evidence': 'evidence',
  // test quality / gaps
  'issue type': 'issueType',
  'risk score': 'riskScore',
  'gap reason': 'gapReason',
  'suggested test class': 'suggestedTestClass',
  // architectural
  'afferent coupling': 'afferentCoupling',
  'efferent coupling': 'efferentCoupling',
  'instability': 'instability',
  'abstractness': 'abstractness',
  'distance from main sequence': 'distanceFromMainSequence',
  'in cycle': 'inCycle',
  'cycle members': 'cycleMembers',
  'package name': 'packageName',
  // dependencies
  'group id': 'groupId',
  'artifact id': 'artifactId',
  'requested version': 'requestedVersion',
  'fixed version': 'fixedVersion',
  'parent group id': 'parentGroupId',
  'parent artifact id': 'parentArtifactId',
  'parent version': 'parentVersion',
  // misc
  'rule id': 'ruleId',
  'parent recipe': 'parentRecipe',
  'build tool type': 'buildToolType',
  'build tool version': 'buildToolVersion'
};

function normalizeHeaders(row) {
  const out = {};
  for (const k of Object.keys(row)) {
    const low = k.toLowerCase();
    // Try the raw lowercased header first, then retry after stripping a
    // trailing "(abbrev)" note (e.g. "Afferent coupling (Ca)" → "afferent coupling").
    const stripped = low.replace(/\s*\([^)]*\)\s*$/, '').trim();
    const mapped = HEADER_MAP[low] || HEADER_MAP[stripped] || k;
    out[mapped] = row[k];
  }
  return out;
}

// For single-repo `.moderne/context/*.csv` exports that drop the repository
// columns: use the first path segment of sourcePath (typically the
// Gradle / Maven submodule) as a grouping label.
function moduleOf(sourcePath) {
  if (!sourcePath) return '(unknown)';
  const parts = String(sourcePath).split('/').filter(Boolean);
  return parts.length ? parts[0] : '(root)';
}

// Universal "which repo or module does this row belong to" helper. Prefer
// the last segment of repositoryPath (matches the platform's display name);
// fall back to the sourcePath submodule when no repo column is present.
function repoOrModule(row) {
  const r = row || {};
  return r.repositoryPath ? shortRepo(r.repositoryPath) : moduleOf(r.sourcePath);
}

function shortRepo(path) {
  if (!path) return '';
  const parts = String(path).split('/');
  return parts[parts.length - 1];
}

function shortClass(fqn) {
  if (!fqn) return '';
  const parts = String(fqn).split('.');
  return parts[parts.length - 1];
}

function extractPackage(fqn) {
  if (!fqn) return '';
  const s = String(fqn);
  const i = s.lastIndexOf('.');
  return i < 0 ? '' : s.slice(0, i);
}

function matchesRepoFilter(value, filterStr) {
  const terms = (filterStr || '').split(',').map(s => s.trim()).filter(Boolean);
  if (terms.length === 0) return true;
  const lower = String(value || '').toLowerCase();
  return terms.some(t => lower.includes(t.toLowerCase()));
}

function groupBy(rows, keyFn) {
  const map = new Map();
  for (const r of rows) {
    const k = keyFn(r);
    if (!map.has(k)) map.set(k, []);
    map.get(k).push(r);
  }
  return map;
}

// Simple Fruchterman-Reingold spring layout. Returns Map<nodeId, {x,y}>
// with positions roughly normalized to [-1, 1]. Deterministic given `seed`.
function computeSpringLayout(nodeIds, edges, options = {}) {
  const iterations = options.iterations || 80;
  const k = options.k || 0.15;
  let s = options.seed || 42;
  function rand() { s = (s * 9301 + 49297) % 233280; return s / 233280; }

  const n = nodeIds.length;
  if (n === 0) return new Map();
  const nodes = new Map();
  nodeIds.forEach(id => nodes.set(id, { x: rand() - 0.5, y: rand() - 0.5, vx: 0, vy: 0 }));
  const kRepulse = Math.sqrt(1 / n) * k;
  const kAttract = kRepulse;

  for (let iter = 0; iter < iterations; iter++) {
    for (const an of nodes.values()) { an.vx = 0; an.vy = 0; }
    const ids = [...nodes.keys()];
    for (let i = 0; i < ids.length; i++) {
      const an = nodes.get(ids[i]);
      for (let j = i + 1; j < ids.length; j++) {
        const bn = nodes.get(ids[j]);
        const dx = an.x - bn.x, dy = an.y - bn.y;
        const dist = Math.sqrt(dx * dx + dy * dy) + 0.01;
        const force = (kRepulse * kRepulse) / dist;
        an.vx += (dx / dist) * force; an.vy += (dy / dist) * force;
        bn.vx -= (dx / dist) * force; bn.vy -= (dy / dist) * force;
      }
    }
    for (const [src, tgt] of edges) {
      const sn = nodes.get(src), tn = nodes.get(tgt);
      if (!sn || !tn) continue;
      const dx = sn.x - tn.x, dy = sn.y - tn.y;
      const dist = Math.sqrt(dx * dx + dy * dy) + 0.01;
      const force = (dist * dist) / kAttract;
      const fx = (dx / dist) * force, fy = (dy / dist) * force;
      sn.vx -= fx; sn.vy -= fy;
      tn.vx += fx; tn.vy += fy;
    }
    const temp = 0.1 * (1 - iter / iterations);
    for (const node of nodes.values()) {
      const vmag = Math.sqrt(node.vx * node.vx + node.vy * node.vy) + 0.001;
      node.x += (node.vx / vmag) * Math.min(vmag, temp);
      node.y += (node.vy / vmag) * Math.min(vmag, temp);
    }
  }
  // Normalize positions to [-1, 1]
  let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
  for (const node of nodes.values()) {
    if (node.x < minX) minX = node.x; if (node.x > maxX) maxX = node.x;
    if (node.y < minY) minY = node.y; if (node.y > maxY) maxY = node.y;
  }
  const sx = maxX - minX || 1, sy = maxY - minY || 1;
  for (const node of nodes.values()) {
    node.x = ((node.x - minX) / sx) * 2 - 1;
    node.y = ((node.y - minY) / sy) * 2 - 1;
  }
  return nodes;
}

// Topological sort (Kahn's algorithm). Returns `{ order, cycles }`.
// If the graph has cycles, `order` still drains all acyclic parts and
// `cycles` lists the nodes that couldn't be ordered (participating in a cycle).
function topologicalSort(nodeIds, edges) {
  const inDeg = new Map(nodeIds.map(id => [id, 0]));
  const outEdges = new Map(nodeIds.map(id => [id, []]));
  for (const [u, v] of edges) {
    if (!inDeg.has(u) || !inDeg.has(v)) continue;
    inDeg.set(v, inDeg.get(v) + 1);
    outEdges.get(u).push(v);
  }
  const order = [];
  const queue = [...nodeIds].filter(id => inDeg.get(id) === 0);
  while (queue.length) {
    const u = queue.shift();
    order.push(u);
    for (const v of outEdges.get(u)) {
      inDeg.set(v, inDeg.get(v) - 1);
      if (inDeg.get(v) === 0) queue.push(v);
    }
  }
  const cycles = nodeIds.filter(id => !order.includes(id));
  // Append cycle nodes at the end so we still produce a full order
  return { order: [...order, ...cycles], cycles };
}

// Build a repo-level DiGraph from the three ReleaseMetroPlan tables.
// Returns { nodes: string[], edges: [[u, v, {edge_type}], ...] } where the
// edge direction is producer -> consumer.
function buildReleaseGraph(coordsRows, depsRows, parentsRows) {
  const artifactToRepo = new Map();
  for (const c of coordsRows) {
    const key = `${c.groupId}:${c.artifactId}`;
    if (!artifactToRepo.has(key)) artifactToRepo.set(key, String(c.repositoryPath));
  }
  const edges = new Map();
  for (const d of depsRows || []) {
    const key = `${d.groupId}:${d.artifactId}`;
    const producer = artifactToRepo.get(key);
    const consumer = String(d.repositoryPath || '');
    if (!producer || !consumer || producer === consumer) continue;
    const k = `${producer}\u0001${consumer}`;
    if (!edges.has(k)) edges.set(k, 'dependency');
  }
  for (const p of parentsRows || []) {
    const key = `${p.parentGroupId}:${p.parentArtifactId}`;
    const parent = artifactToRepo.get(key);
    const child = String(p.repositoryPath || '');
    if (!parent || !child || parent === child) continue;
    edges.set(`${parent}\u0001${child}`, 'parent');
  }
  const nodeSet = new Set(coordsRows.map(c => String(c.repositoryPath)));
  const edgeList = [...edges.entries()].map(([k, etype]) => {
    const [u, v] = k.split('\u0001');
    nodeSet.add(u); nodeSet.add(v);
    return [u, v, { edge_type: etype }];
  });
  return { nodes: [...nodeSet], edges: edgeList };
}

// Compute release waves via Kahn-style topological grouping.
// Returns { waves: string[][], circular: string[] }.
function computeReleaseWaves(nodes, edges) {
  const inEdgesByNode = new Map(nodes.map(n => [n, []]));
  const outEdgesByNode = new Map(nodes.map(n => [n, []]));
  for (const [u, v] of edges) {
    if (!inEdgesByNode.has(u) || !inEdgesByNode.has(v)) continue;
    outEdgesByNode.get(u).push(v);
    inEdgesByNode.get(v).push(u);
  }
  const remaining = new Set(nodes);
  const waves = [];
  while (remaining.size) {
    const wave = [];
    for (const n of remaining) {
      if (inEdgesByNode.get(n).every(p => !remaining.has(p))) wave.push(n);
    }
    if (wave.length === 0) break;
    wave.sort();
    waves.push(wave);
    for (const n of wave) remaining.delete(n);
  }
  const circular = [...remaining].sort();
  return { waves, circular };
}

// Sample n+1 points on a cubic Bézier.
function cubicBezier(p0, p1, p2, p3, n = 30) {
  const pts = [];
  for (let i = 0; i <= n; i++) {
    const t = i / n, u = 1 - t;
    const x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0];
    const y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1];
    pts.push([x, y]);
  }
  return pts;
}

// Version comparator: natural compare of dot-separated components,
// numeric where possible, lexicographic fallback. Good enough for
// version axes when semver parsing is ambiguous.
function compareVersions(a, b) {
  const as = String(a).split(/[.\-+]/);
  const bs = String(b).split(/[.\-+]/);
  const n = Math.max(as.length, bs.length);
  for (let i = 0; i < n; i++) {
    const ai = as[i] === undefined ? '' : as[i];
    const bi = bs[i] === undefined ? '' : bs[i];
    const an = Number(ai);
    const bn = Number(bi);
    if (!isNaN(an) && !isNaN(bn)) {
      if (an !== bn) return an - bn;
    } else {
      if (ai !== bi) return ai < bi ? -1 : 1;
    }
  }
  return 0;
}
