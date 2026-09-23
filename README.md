
# Adka-
🏗️ النظام العملي: شبكة الخبراء الذكيين دعني أبني لك نموذج فعلي لنظام وكلاء متعاونين:<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>نور الاستخلاف 2026 — لوحة التحكم المتطورة</title>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  :root {
    --bg1:#05070a; --bg2:#0f1419;
    --accent:#34d399; --accent2:#60a5fa; --accent3:#a78bfa;
    --card: rgba(255,255,255,0.04); --border: rgba(255,255,255,0.09);
  }
  body {
    font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
    background: radial-gradient(ellipse at top, var(--bg2) 0%, var(--bg1) 65%);
    color:#e8ecef; min-height:100vh; padding-bottom:40px;
  }
  ::-webkit-scrollbar { width:6px; }
  ::-webkit-scrollbar-thumb { background:rgba(255,255,255,0.15); border-radius:4px; }

  /* ===== Header ===== */
  .topbar {
    display:flex; align-items:center; justify-content:space-between;
    padding:16px 20px; background:rgba(255,255,255,0.03);
    border-bottom:1px solid var(--border); position:sticky; top:0; z-index:50;
    backdrop-filter: blur(12px);
  }
  .brand { display:flex; align-items:center; gap:10px; }
  .brand .logo { font-size:1.6rem; }
  .brand h1 {
    font-size:1.05rem;
    background:linear-gradient(90deg,var(--accent),var(--accent2),var(--accent3));
    -webkit-background-clip:text; background-clip:text; color:transparent;
  }
  .conn-status { display:flex; align-items:center; gap:6px; font-size:0.72rem; color:#9ca3af; }
  .conn-dot { width:8px; height:8px; border-radius:50%; background:#6b7280; transition:.3s; }
  .conn-dot.ok { background:#22c55e; box-shadow:0 0 8px #22c55e; }
  .conn-dot.bad { background:#ef4444; box-shadow:0 0 8px #ef4444; }
  .conn-dot.checking { background:#f59e0b; animation:pulse 1s infinite; }
  @keyframes pulse { 50%{opacity:.4;} }

  /* ===== Tabs ===== */
  .tabs {
    display:flex; gap:6px; padding:12px 16px; overflow-x:auto;
  }
  .tab-btn {
    padding:9px 16px; border-radius:10px; border:1px solid var(--border);
    background:var(--card); color:#9ca3af; font-size:0.82rem; cursor:pointer;
    white-space:nowrap; transition:.2s;
  }
  .tab-btn.active { background:rgba(52,211,153,0.12); border-color:var(--accent); color:var(--accent); font-weight:700; }

  .container { padding:0 16px; max-width:900px; margin:0 auto; }
  .view { display:none; animation:fadeIn .25s; }
  .view.active { display:block; }
  @keyframes fadeIn { from{opacity:0; transform:translateY(6px);} to{opacity:1; transform:translateY(0);} }

  /* ===== Cards / general ===== */
  .card {
    background:var(--card); border:1px solid var(--border); border-radius:16px;
    padding:16px; margin-bottom:16px;
  }
  .card h3 { font-size:0.9rem; margin-bottom:10px; color:#e8ecef; }
  label { font-size:0.75rem; color:#9ca3af; display:block; margin-bottom:6px; }
  input[type=text], input[type=url], textarea {
    width:100%; background:rgba(0,0,0,0.3); border:1px solid var(--border);
    border-radius:10px; color:#e8ecef; padding:11px; font-size:0.87rem;
    font-family:inherit; margin-bottom:10px;
  }
  textarea { min-height:80px; resize:vertical; }
  input:focus, textarea:focus { outline:none; border-color:var(--accent); }

  .btn {
    padding:11px 18px; border:none; border-radius:10px; font-size:0.86rem; font-weight:700;
    cursor:pointer; transition:.2s; color:#fff;
  }
  .btn-primary { background:linear-gradient(90deg,#059669,#3b82f6); width:100%; }
  .btn-primary:hover { filter:brightness(1.1); }
  .btn-secondary { background:rgba(255,255,255,0.08); border:1px solid var(--border); }
  .btn:disabled { opacity:.5; cursor:not-allowed; }
  .row { display:flex; gap:8px; }
  .row .btn { flex:1; }

  .stat-strip { display:flex; gap:10px; margin-bottom:16px; flex-wrap:wrap; }
  .stat-chip { flex:1; min-width:100px; background:var(--card); border:1px solid var(--border);
    border-radius:12px; padding:12px; text-align:center; }
  .stat-chip .num { font-size:1.3rem; font-weight:800; color:var(--accent); }
  .stat-chip .lbl { font-size:0.68rem; color:#8b95a1; margin-top:2px; }

  /* ===== Experts ===== */
  .search-box { margin-bottom:12px; }
  .experts-grid {
    display:grid; grid-template-columns:repeat(auto-fill,minmax(140px,1fr));
    gap:9px; margin-bottom:14px;
  }
  .expert-card {
    background:var(--card); border:1px solid var(--border); border-radius:13px;
    padding:12px 8px; text-align:center; cursor:pointer; transition:.2s; user-select:none;
  }
  .expert-card:hover { background:rgba(255,255,255,0.07); transform:translateY(-2px); }
  .expert-card.selected {
    border-color:var(--accent); background:rgba(52,211,153,0.1);
    box-shadow:0 0 0 1px var(--accent), 0 0 18px rgba(52,211,153,.15);
  }
  .expert-icon { font-size:1.5rem; display:block; margin-bottom:5px; }
  .expert-name { font-size:0.74rem; font-weight:700; }
  .expert-desc { font-size:0.62rem; color:#8b95a1; margin-top:2px; line-height:1.25; }

  .selected-label { font-size:0.78rem; color:var(--accent); margin-bottom:10px; font-weight:700; }

  /* ===== Models row ===== */
  .models-row { display:flex; gap:8px; flex-wrap:wrap; margin-bottom:14px; }
  .model-chip {
    padding:7px 14px; border-radius:20px; font-size:0.76rem; font-weight:700;
    display:flex; align-items:center; gap:6px; border:1px solid var(--border);
    background:rgba(255,255,255,0.04); cursor:pointer; transition:.2s;
  }
  .model-chip.disabled { opacity:.35; }
  .model-chip .dot { width:7px; height:7px; border-radius:50%; background:#22c55e; }

  /* ===== Results ===== */
  .results { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:10px; }
  .result-card { background:var(--card); border:1px solid var(--border); border-radius:14px; padding:13px; min-height:90px; }
  .result-header { display:flex; align-items:center; gap:7px; margin-bottom:8px; font-weight:700; font-size:0.8rem; }
  .badge { width:9px; height:9px; border-radius:50%; }
  .badge.groq { background:#f97316; } .badge.gemini { background:#3b82f6; } .badge.claude { background:#a855f7; }
  .result-text { font-size:0.8rem; color:#c7ccd1; line-height:1.55; white-space:pre-wrap; }
  .loading { color:#6b7280; font-size:0.78rem; display:flex; align-items:center; gap:6px; }
  .spinner { width:12px; height:12px; border:2px solid rgba(255,255,255,0.2); border-top-color:var(--accent); border-radius:50%; animation:spin .8s linear infinite; }
  @keyframes spin { to{transform:rotate(360deg);} }
  .error-text { color:#f87171; font-size:0.78rem; }

  /* ===== Log table ===== */
  .log-table { width:100%; font-size:0.76rem; border-collapse:collapse; }
  .log-table th { text-align:right; color:#8b95a1; padding:8px 6px; border-bottom:1px solid var(--border); font-weight:600; }
  .log-table td { padding:8px 6px; border-bottom:1px solid rgba(255,255,255,0.05); }
  .status-pill { padding:2px 8px; border-radius:10px; font-size:0.68rem; }
  .status-pill.ok { background:rgba(34,197,94,.15); color:#4ade80; }
  .status-pill.fail { background:rgba(239,68,68,.15); color:#f87171; }
  .empty-note { text-align:center; color:#6b7280; font-size:0.8rem; padding:24px 0; }

  .hint { font-size:0.68rem; color:#6b7280; margin-top:4px; line-height:1.5; }
  code { background:rgba(255,255,255,0.08); padding:2px 6px; border-radius:5px; font-size:0.75rem; }
</style>
</head>
<body>

<div class="topbar">
  <div class="brand">
    <span class="logo">🏛️</span>
    <div>
      <h1>نور الاستخلاف 2026</h1>
    </div>
  </div>
  <div class="conn-status">
    <span class="conn-dot" id="connDot"></span>
    <span id="connLabel">غير متصل</span>
  </div>
</div>

<div class="tabs">
  <button class="tab-btn active" data-view="dashboard">🧭 لوحة القيادة</button>
  <button class="tab-btn" data-view="settings">⚙️ الإعدادات</button>
  <button class="tab-btn" data-view="log">🗂️ السجل</button>
</div>

<div class="container">

  <!-- ===== Dashboard View ===== -->
  <div class="view active" id="view-dashboard">
    <div class="stat-strip">
      <div class="stat-chip"><div class="num" id="statCalls">0</div><div class="lbl">استدعاءات الجلسة</div></div>
      <div class="stat-chip"><div class="num" id="statOk">0</div><div class="lbl">نجحت</div></div>
      <div class="stat-chip"><div class="num" id="statFail">0</div><div class="lbl">فشلت</div></div>
    </div>

    <div class="models-row" id="modelsRow"></div>

    <div class="card">
      <input type="text" class="search-box" id="expertSearch" placeholder="🔍 بحث عن خبير...">
      <div class="experts-grid" id="expertsGrid"></div>
      <div class="selected-label" id="selectedLabel">اختر خبيرًا، أو اترك الاختيار فارغًا لأمر عام</div>
      <textarea id="promptInput" placeholder="اكتب أمرك أو سؤالك هنا..."></textarea>
      <button class="btn btn-primary" id="launchBtn">🚀 إطلاق الأمر على النماذج المفعّلة</button>
    </div>

    <div class="results" id="resultsArea"></div>
  </div>

  <!-- ===== Settings View ===== -->
  <div class="view" id="view-settings">
    <div class="card">
      <h3>🔌 عنوان الخادم (Gateway)</h3>
      <label>رابط الخادم الأساسي</label>
      <input type="url" id="gatewayUrlInput" value="http://127.0.0.1:8000" placeholder="http://127.0.0.1:8000">
      <label>مسار نقطة النهاية</label>
      <input type="text" id="gatewayPathInput" value="/api/query" placeholder="/api/query">
      <div class="row">
        <button class="btn btn-secondary" id="testConnBtn">📡 فحص الاتصال</button>
        <button class="btn btn-primary" id="saveConnBtn">💾 حفظ</button>
      </div>
      <div class="hint" id="settingsHint">
        الإعدادات تُحفظ فقط لهذه الجلسة الحالية في المتصفح. لو حمّلت هذا الملف من جديد ستحتاج إدخالها مرة أخرى.
        شكل الطلب المُرسل للخادم: <code>{model, expert, prompt}</code> ويُتوقع رد بصيغة <code>{response: "..."}</code>.
      </div>
    </div>
    <div class="card">
      <h3>🧩 تفعيل/تعطيل النماذج</h3>
      <div class="models-row" id="modelsToggleRow"></div>
      <div class="hint">النماذج المعطّلة لن تُستدعى عند الإطلاق الموحد — مفيد إن كان لديك مفتاح واحد فقط فعّالًا حاليًا.</div>
    </div>
  </div>

  <!-- ===== Log View ===== -->
  <div class="view" id="view-log">
    <div class="card">
      <h3>سجل استدعاءات هذه الجلسة</h3>
      <div id="logContent"><div class="empty-note">لا توجد استدعاءات مسجّلة بعد</div></div>
    </div>
  </div>

</div>

<script>
const experts = [
  {icon:"📖", name:"حكيم القرآن", desc:"تفسير وتأمل، وليس فتوى"},
  {icon:"⚖️", name:"عمر السيادي", desc:"الامتثال تحت القانون 42.25"},
  {icon:"💰", name:"طارق المالي", desc:"تحليل مالي عام"},
  {icon:"📈", name:"خبير الاستثمار", desc:"قراءة سوقية عامة"},
  {icon:"💻", name:"أمين البرمجة", desc:"مراجعة كود ومعمارية"},
  {icon:"☁️", name:"خبير السحاب", desc:"نشر وبنية تحتية"},
  {icon:"🔐", name:"خبير التشفير", desc:"أمان وحماية بيانات"},
  {icon:"🇲🇦", name:"مستشار SARL", desc:"تأسيس شركات بالمغرب"},
  {icon:"📣", name:"ليلى الاتصالية", desc:"محتوى تسويقي دقيق"},
  {icon:"🔍", name:"موثق الحقيقة", desc:"تدقيق ومراجعة معلومات"},
  {icon:"🧠", name:"فيلسوف المنطق", desc:"تحليل منطقي للمقترحات"},
  {icon:"📊", name:"محلل البيانات", desc:"قراءة وتلخيص بيانات"},
  {icon:"🗂️", name:"حارس الذاكرة", desc:"تنظيم السجلات والأرشيف"},
  {icon:"🎬", name:"استوديو المحتوى", desc:"مقالات وسكريبتات"},
];

const models = [
  {id:"groq", name:"Groq", enabled:true},
  {id:"gemini", name:"Gemini", enabled:true},
  {id:"claude", name:"Claude", enabled:true},
];

let selectedExpert = null;
let stats = { calls:0, ok:0, fail:0 };
let logEntries = [];
let GATEWAY_BASE_URL = "http://127.0.0.1:8000";
let GATEWAY_PATH = "/api/query";

// ===== Tabs =====
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('view-' + btn.dataset.view).classList.add('active');
  });
});

// ===== Render models (dashboard row, read-only display) =====
function renderModelsRow() {
  const row = document.getElementById('modelsRow');
  row.innerHTML = models.map(m => `
    <div class="model-chip ${m.enabled ? '' : 'disabled'}">
      <span class="dot" style="background:${m.enabled ? '#22c55e' : '#6b7280'}"></span>${m.name}
    </div>`).join('');
}

// ===== Render models toggle (settings) =====
function renderModelsToggle() {
  const row = document.getElementById('modelsToggleRow');
  row.innerHTML = models.map(m => `
    <div class="model-chip" data-id="${m.id}" style="cursor:pointer;">
      <span class="dot" style="background:${m.enabled ? '#22c55e' : '#6b7280'}"></span>${m.name} ${m.enabled ? '✓' : '✕'}
    </div>`).join('');
  row.querySelectorAll('.model-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const m = models.find(x => x.id === chip.dataset.id);
      m.enabled = !m.enabled;
      renderModelsToggle();
      renderModelsRow();
    });
  });
}

// ===== Render experts =====
function renderExperts(filter="") {
  const grid = document.getElementById('expertsGrid');
  const list = experts.filter(e => e.name.includes(filter) || e.desc.includes(filter));
  grid.innerHTML = list.map((e) => {
    const idx = experts.indexOf(e);
    return `
    <div class="expert-card ${selectedExpert===idx?'selected':''}" data-idx="${idx}">
      <span class="expert-icon">${e.icon}</span>
      <div class="expert-name">${e.name}</div>
      <div class="expert-desc">${e.desc}</div>
    </div>`;
  }).join('') || `<div class="empty-note">لا نتائج مطابقة</div>`;
  grid.querySelectorAll('.expert-card').forEach(card => {
    card.addEventListener('click', () => {
      const idx = parseInt(card.dataset.idx);
      selectedExpert = (selectedExpert === idx) ? null : idx;
      renderExperts(document.getElementById('expertSearch').value);
      updateSelectedLabel();
    });
  });
}

function updateSelectedLabel() {
  const label = document.getElementById('selectedLabel');
  label.textContent = selectedExpert !== null
    ? `الخبير المختار: ${experts[selectedExpert].icon} ${experts[selectedExpert].name}`
    : "اختر خبيرًا، أو اترك الاختيار فارغًا لأمر عام";
}

document.getElementById('expertSearch').addEventListener('input', (e) => renderExperts(e.target.value));

// ===== Connection check =====
async function checkConnection() {
  const dot = document.getElementById('connDot');
  const label = document.getElementById('connLabel');
  dot.className = 'conn-dot checking';
  label.textContent = 'جارٍ الفحص...';
  try {
    const res = await fetch(GATEWAY_BASE_URL + GATEWAY_PATH, {
      method: "OPTIONS"
    }).catch(() => null);
    // بعض الخوادم لا تدعم OPTIONS — أي استجابة (حتى خطأ HTTP) تعني أن الاتصال بالشبكة نجح
    if (res) {
      dot.className = 'conn-dot ok'; label.textContent = 'متصل بالخادم';
    } else {
      throw new Error('no response');
    }
  } catch (e) {
    dot.className = 'conn-dot bad'; label.textContent = 'غير متصل';
  }
}

document.getElementById('testConnBtn').addEventListener('click', checkConnection);
document.getElementById('saveConnBtn').addEventListener('click', () => {
  GATEWAY_BASE_URL = document.getElementById('gatewayUrlInput').value.trim() || GATEWAY_BASE_URL;
  GATEWAY_PATH = document.getElementById('gatewayPathInput').value.trim() || GATEWAY_PATH;
  document.getElementById('settingsHint').innerHTML =
    `✅ تم الحفظ لهذه الجلسة. نقطة النهاية الحالية: <code>${GATEWAY_BASE_URL}${GATEWAY_PATH}</code>`;
  checkConnection();
});

// ===== Real fetch calls to gateway =====
async function callModel(modelId, prompt, expertLabel) {
  const res = await fetch(GATEWAY_BASE_URL + GATEWAY_PATH, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ model: modelId, expert: expertLabel, prompt: prompt })
  });
  if (!res.ok) {
    const errText = await res.text().catch(() => res.statusText);
    throw new Error(`HTTP ${res.status}: ${errText}`);
  }
  const data = await res.json();
  return data.response ?? JSON.stringify(data);
}

function resultCardTemplate(id, badgeClass, name) {
  return `
    <div class="result-card" id="card-${id}">
      <div class="result-header"><span class="badge ${badgeClass}"></span>${name}</div>
      <div class="loading"><span class="spinner"></span> جارٍ الاستدعاء...</div>
    </div>`;
}

function addLogEntry(model, expertLabel, ok, detail) {
  logEntries.unshift({
    time: new Date().toLocaleTimeString('ar-MA'),
    model, expert: expertLabel, ok, detail: detail?.slice(0,60) || ''
  });
  renderLog();
}

function renderLog() {
  const content = document.getElementById('logContent');
  if (logEntries.length === 0) {
    content.innerHTML = `<div class="empty-note">لا توجد استدعاءات مسجّلة بعد</div>`;
    return;
  }
  content.innerHTML = `
    <table class="log-table">
      <thead><tr><th>الوقت</th><th>النموذج</th><th>الخبير</th><th>الحالة</th></tr></thead>
      <tbody>
        ${logEntries.map(l => `
          <tr>
            <td>${l.time}</td>
            <td>${l.model}</td>
            <td>${l.expert}</td>
            <td><span class="status-pill ${l.ok?'ok':'fail'}">${l.ok?'نجح':'فشل'}</span></td>
          </tr>`).join('')}
      </tbody>
    </table>`;
}

function updateStatChips() {
  document.getElementById('statCalls').textContent = stats.calls;
  document.getElementById('statOk').textContent = stats.ok;
  document.getElementById('statFail').textContent = stats.fail;
}

async function launch() {
  const prompt = document.getElementById('promptInput').value.trim();
  if (!prompt) return;
  const activeModels = models.filter(m => m.enabled);
  if (activeModels.length === 0) { alert('فعّل نموذجًا واحدًا على الأقل من الإعدادات'); return; }

  const btn = document.getElementById('launchBtn');
  btn.disabled = true;
  btn.textContent = "⏳ جارٍ التنفيذ...";

  const expertLabel = selectedExpert !== null ? experts[selectedExpert].name : "أمر عام";
  const resultsArea = document.getElementById('resultsArea');
  const badgeMap = {groq:'groq', gemini:'gemini', claude:'claude'};
  resultsArea.innerHTML = activeModels.map(m => resultCardTemplate(m.id, badgeMap[m.id], m.name)).join('');

  await Promise.allSettled(activeModels.map(async m => {
    try {
      const text = await callModel(m.id, prompt, expertLabel);
      document.querySelector(`#card-${m.id} .loading`)?.remove();
      const div = document.createElement('div');
      div.className = 'result-text';
      div.textContent = text;
      document.getElementById(`card-${m.id}`).appendChild(div);
      stats.ok++; addLogEntry(m.name, expertLabel, true, text);
    } catch (err) {
      document.querySelector(`#card-${m.id} .loading`)?.remove();
      const div = document.createElement('div');
      div.className = 'error-text';
      div.textContent = 'فشل الاستدعاء: ' + err.message;
      document.getElementById(`card-${m.id}`).appendChild(div);
      stats.fail++; addLogEntry(m.name, expertLabel, false, err.message);
    }
  }));

  stats.calls++;
  updateStatChips();
  btn.disabled = false;
  btn.textContent = "🚀 إطلاق الأمر على النماذج المفعّلة";
}

document.getElementById('launchBtn').addEventListener('click', launch);

renderModelsRow();
renderModelsToggle();
renderExperts();
updateSelectedLabel();
updateStatChips();
renderLog();
</script>

</body>
</html>
