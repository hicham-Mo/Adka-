const experts = [
  { icon: '📖', name: 'حكيم القرآن', desc: 'تفسير وتأمل، وليس فتوى' },
  { icon: '⚖️', name: 'عمر السيادي', desc: 'الامتثال تحت القانون 42.25' },
  { icon: '💰', name: 'طارق المالي', desc: 'تحليل مالي عام' },
  { icon: '📈', name: 'خبير الاستثمار', desc: 'قراءة سوقية عامة' },
  { icon: '💻', name: 'أمين البرمجة', desc: 'مراجعة كود ومعمارية' },
  { icon: '☁️', name: 'خبير السحاب', desc: 'نشر وبنية تحتية' },
  { icon: '🔐', name: 'خبير التشفير', desc: 'أمان وحماية بيانات' },
  { icon: '🇲🇦', name: 'مستشار SARL', desc: 'تأسيس شركات بالمغرب' },
  { icon: '📣', name: 'ليلى الاتصالية', desc: 'محتوى تسويقي دقيق' },
  { icon: '🔍', name: 'موثق الحقيقة', desc: 'تدقيق ومراجعة معلومات' },
  { icon: '🧠', name: 'فيلسوف المنطق', desc: 'تحليل منطقي للمقترحات' },
  { icon: '📊', name: 'محلل البيانات', desc: 'قراءة وتلخيص بيانات' },
  { icon: '🗂️', name: 'حارس الذاكرة', desc: 'تنظيم السجلات والأرشيف' },
  { icon: '🎬', name: 'استوديو المحتوى', desc: 'مقالات وسكريبتات' }
];

const models = [
  { id: 'groq', name: 'Groq', enabled: true },
  { id: 'gemini', name: 'Gemini', enabled: true },
  { id: 'claude', name: 'Claude', enabled: true }
];

let selectedExpert = null;
let stats = { calls: 0, ok: 0, fail: 0 };
let logEntries = [];
let GATEWAY_BASE_URL = 'http://127.0.0.1:8000';
let GATEWAY_PATH = '/api/query';

const activeView = () => document.querySelector('.view.active')?.id;

function renderExperts(filter = '') {
  const grid = document.getElementById('expertsGrid');
  const list = experts.filter(e => e.name.includes(filter) || e.desc.includes(filter));

  grid.innerHTML = list.map((expert, index) => {
    const realIdx = experts.indexOf(expert);
    return `
      <div class="expert-card ${selectedExpert === realIdx ? 'selected' : ''}" data-idx="${realIdx}">
        <span class="expert-icon">${expert.icon}</span>
        <div class="expert-name">${expert.name}</div>
        <div class="expert-desc">${expert.desc}</div>
      </div>
    `;
  }).join('') || '<div class="empty-note">لا نتائج مطابقة</div>';

  grid.querySelectorAll('.expert-card').forEach(card => {
    card.addEventListener('click', () => {
      const idx = Number(card.dataset.idx);
      selectedExpert = selectedExpert === idx ? null : idx;
      renderExperts(document.getElementById('expertSearch').value);
      updateSelectedLabel();
    });
  });
}

function updateSelectedLabel() {
  const label = document.getElementById('selectedLabel');
  label.textContent = selectedExpert !== null
    ? `الخبير المختار: ${experts[selectedExpert].icon} ${experts[selectedExpert].name}`
    : 'اختر خبيرًا أو اترك الاختيار فارغًا';
}

function renderLog() {
  const content = document.getElementById('logContent');
  if (!logEntries.length) {
    content.innerHTML = 'لا توجد استدعاءات مسجلة.';
    return;
  }

  content.innerHTML = `
    <table class="log-table">
      <thead>
        <tr>
          <th>الوقت</th>
          <th>النموذج</th>
          <th>الخبير</th>
          <th>الحالة</th>
        </tr>
      </thead>
      <tbody>
        ${logEntries.map(entry => `
          <tr>
            <td>${entry.time}</td>
            <td>${entry.model}</td>
            <td>${entry.expert}</td>
            <td><span class="status-pill ${entry.ok ? 'ok' : 'fail'}">${entry.ok ? 'نجح' : 'فشل'}</span></td>
          </tr>
        `).join('')}
      </tbody>
    </table>
  `;
}

function updateStatChips() {
  document.getElementById('statCalls').textContent = stats.calls;
  document.getElementById('statOk').textContent = stats.ok;
  document.getElementById('statFail').textContent = stats.fail;
}

function addLogEntry(model, expert, ok) {
  logEntries.unshift({
    time: new Date().toLocaleTimeString('ar-MA'),
    model,
    expert,
    ok
  });
  renderLog();
}

function resultCardTemplate(id, badgeClass, name) {
  return `
    <div class="result-card" id="card-${id}">
      <div class="result-header"><span class="badge ${badgeClass}"></span>${name}</div>
      <div class="loading"><span class="spinner"></span> جارٍ الاستدعاء...</div>
    </div>
  `;
}

async function checkConnection() {
  const dot = document.getElementById('connDot');
  const label = document.getElementById('connLabel');
  dot.className = 'dot checking';
  label.textContent = 'جارٍ الفحص...';

  try {
    const res = await fetch(`${GATEWAY_BASE_URL}/health`, { method: 'GET' });
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}`);
    }
    dot.className = 'dot online';
    label.textContent = 'متصل بالخادم';
  } catch (err) {
    dot.className = 'dot offline';
    label.textContent = 'غير متصل';
  }
}

async function callModel(modelId, prompt, expertLabel) {
  const res = await fetch(`${GATEWAY_BASE_URL}${GATEWAY_PATH}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ model: modelId, expert: expertLabel, prompt })
  });

  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`HTTP ${res.status}: ${detail || 'خطأ غير معروف'}`);
  }

  const data = await res.json();
  return data.response || JSON.stringify(data);
}

async function launch() {
  const prompt = document.getElementById('promptInput').value.trim();
  if (!prompt) return;

  const activeModels = models.filter(m => m.enabled);
  if (!activeModels.length) {
    alert('فعّل نموذجًا واحدًا على الأقل في الإعدادات.');
    return;
  }

  const expertLabel = selectedExpert !== null ? experts[selectedExpert].name : 'أمر عام';
  const resultsArea = document.getElementById('resultsArea');

  const cardMap = {
    groq: 'groq',
    gemini: 'gemini',
    claude: 'claude'
  };

  resultsArea.innerHTML = activeModels.map(m => resultCardTemplate(m.id, cardMap[m.id], m.name)).join('');

  const button = document.getElementById('launchBtn');
  button.disabled = true;
  button.textContent = '⏳ جارٍ التنفيذ...';

  try {
    const outcomes = await Promise.allSettled(activeModels.map(async model => {
      const text = await callModel(model.id, prompt, expertLabel);
      const loading = document.querySelector(`#card-${model.id} .loading`);
      if (loading) loading.remove();

      const div = document.createElement('div');
      div.className = 'result-text';
      div.textContent = text;
      document.getElementById(`card-${model.id}`).appendChild(div);

      stats.ok += 1;
      addLogEntry(model.name, expertLabel, true);
    }));

    const failed = outcomes.filter(o => o.status === 'rejected').length;
    stats.fail += failed;
    stats.calls += activeModels.length;

    for (const outcome of outcomes) {
      if (outcome.status === 'rejected') {
        const modelId = outcome.reason?.modelId || 'unknown';
        const card = document.getElementById(`card-${modelId}`);
        if (card) {
          const loading = card.querySelector('.loading');
          if (loading) loading.remove();
          const err = document.createElement('div');
          err.className = 'error-text';
          err.textContent = `فشل الاستدعاء: ${outcome.reason.message}`;
          card.appendChild(err);
        }
      }
    }
  } catch (err) {
    // no-op here
  } finally {
    updateStatChips();
    button.disabled = false;
    button.textContent = '🚀 إطلاق الأمر';
  }
}

document.getElementById('expertSearch').addEventListener('input', (e) => renderExperts(e.target.value));

document.getElementById('launchBtn').addEventListener('click', launch);

document.getElementById('testConnBtn').addEventListener('click', checkConnection);

document.getElementById('saveConnBtn').addEventListener('click', () => {
  const url = document.getElementById('gatewayUrlInput').value.trim() || GATEWAY_BASE_URL;
  const path = document.getElementById('gatewayPathInput').value.trim() || GATEWAY_PATH;

  GATEWAY_BASE_URL = url;
  GATEWAY_PATH = path;

  document.getElementById('settingsHint').textContent = `✅ تم الحفظ. نقطة النهاية الحالية: ${GATEWAY_BASE_URL}${GATEWAY_PATH}`;
  checkConnection();
});

document.querySelectorAll('.tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.view).classList.add('active');
  });
});

renderExperts();
updateSelectedLabel();
updateStatChips();
renderLog();
checkConnection();
