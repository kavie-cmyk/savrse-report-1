from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
index_path = ROOT / "index.html"
css_path = ROOT / "styles.css"
js_path = ROOT / "app.js"
readme_path = ROOT / "README.md"

NEW_SECTION = r'''<section id="kinetic" class="section kinetic-section kinetic-explainer-v2" data-section="10">
  <div class="section-head kinetic-head-simple">
    <span class="section-no">10</span>
    <div>
      <div class="eyebrow">WHAT KINETIC ACTUALLY IS · PLAIN-LANGUAGE VERSION</div>
      <h2>KINETIC SWITCHYARD LÀ <span>GAME GÌ?</span></h2>
      <p class="kinetic-one-liner"><b>Bạn đứng trong một nhà máy tự động đang chạy liên tục và dùng hai tay trong VR để chuyển các kiện hàng tới đúng máy trước khi dây chuyền bị rối hoặc quá tải.</b></p>
      <p class="kinetic-subline">Ban đầu chỉ có vài kiện hàng và vài điểm chuyển hướng. Sau đó mọi thứ nhanh hơn, nhiều luồng xuất hiện cùng lúc và bạn phải nhìn trước, đổi đường, cứu lỗi và phối hợp hai tay để giữ cả hệ thống chạy trơn tru.</p>
    </div>
  </div>

  <div class="theme-disclosure">
    <span class="theme-pill">THEME MINH HỌA ĐỀ XUẤT</span>
    <div><b>Nhà máy tự động / sorting plant tương lai</b><small>Theme này được bổ sung để giúp người đọc hình dung gameplay. Đây <b>chưa phải</b> art direction hay theme cuối cùng đã được research chứng minh.</small></div>
  </div>

  <div class="kinetic-simple-grid" data-visual="kinetic-explained-simple">
    <article class="simple-card"><span class="simple-no">01</span><h3>Bạn nhìn thấy gì?</h3><p>Một dây chuyền nhỏ trước mặt: <b>đầu vào → băng chuyền → điểm chuyển hướng → các máy đích.</b> Kiện hàng liên tục chạy vào và mỗi kiện cần đi tới đúng nơi.</p></article>
    <article class="simple-card"><span class="simple-no">02</span><h3>Bạn làm gì?</h3><p><b>Nhìn → với tay → cầm/xoay/gạt switch → đổi đường → nhìn kết quả → xử lý việc tiếp theo.</b> Bạn thao tác trực tiếp bằng hai tay, không chỉ chọn menu.</p></article>
    <article class="simple-card"><span class="simple-no">03</span><h3>Mục tiêu là gì?</h3><p>Giữ dòng hàng chạy <b>đúng, nhanh và ít tắc</b> khi tình hình liên tục thay đổi. Đây không phải puzzle chỉ có một đáp án rồi chơi xong.</p></article>
    <article class="simple-card"><span class="simple-no">04</span><h3>Vì sao chơi lại?</h3><p>Lần sau bạn có thể <b>đọc tình hình sớm hơn, phối hợp hai tay tốt hơn, ít thao tác thừa hơn và đạt personal best cao hơn.</b></p></article>
  </div>

  <div class="factory-snapshot" data-visual="factory-gameplay-snapshot">
    <div class="snapshot-copy">
      <span class="snapshot-kicker">HÃY TƯỞNG TƯỢNG 30 GIÂY CHƠI</span>
      <h3>Một kiện BLUE đang đi sai đường.</h3>
      <ol class="thirty-seconds">
        <li><b>0–5s</b><span>Một kiện BLUE đi vào dây chuyền. Đích của nó là <b>Machine B</b>.</span></li>
        <li><b>5–10s</b><span>Switch đang để hướng A. Nếu bạn không làm gì, kiện hàng sẽ đi sai máy.</span></li>
        <li><b>10–15s</b><span>Bạn đưa tay ra và <b>gạt switch sang B</b> trước khi kiện hàng tới junction.</span></li>
        <li><b>15–20s</b><span>Kiện BLUE vào đúng Machine B. Flow tiếp tục, điểm/throughput tăng.</span></li>
        <li><b>20–30s</b><span>Một kiện khác xuất hiện, Machine B sắp quá tải và bạn phải xử lý <b>hai việc gần như cùng lúc</b>.</span></li>
      </ol>
    </div>

    <div class="factory-demo" id="factory-demo" aria-label="Minh họa tương tác Kinetic trong theme nhà máy">
      <div class="factory-hud"><span>FACTORY CELL 01</span><b id="factory-hud-state">MỤC TIÊU: đưa kiện BLUE → MACHINE B</b></div>
      <svg class="factory-svg" viewBox="0 0 760 390" role="img" aria-label="Sơ đồ nhà máy với băng chuyền, switch và hai máy đích">
        <defs>
          <marker id="factoryArrow" markerWidth="10" markerHeight="10" refX="8" refY="4" orient="auto"><path d="M0,0 L0,8 L9,4 z" fill="currentColor"/></marker>
          <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="8" flood-opacity=".18"/></filter>
        </defs>
        <rect class="factory-floor" x="15" y="18" width="730" height="350" rx="24"/>
        <g class="machine infeed" transform="translate(42 140)"><rect width="130" height="100" rx="14"/><text x="65" y="39" text-anchor="middle">INFEED</text><text x="65" y="66" text-anchor="middle">KIỆN HÀNG</text></g>
        <path class="belt belt-main" d="M172 190 H350"/>
        <circle class="junction-ring" cx="380" cy="190" r="34"/>
        <path class="belt route-to-a" d="M410 180 C490 145 510 105 585 105"/>
        <path class="belt route-to-b active" d="M410 200 C490 235 510 285 585 285"/>
        <g class="machine machine-a" transform="translate(585 55)"><rect width="135" height="100" rx="14"/><text x="68" y="40" text-anchor="middle">MACHINE A</text><text x="68" y="67" text-anchor="middle">RED</text></g>
        <g class="machine machine-b target" transform="translate(585 235)"><rect width="135" height="100" rx="14"/><text x="68" y="40" text-anchor="middle">MACHINE B</text><text x="68" y="67" text-anchor="middle">BLUE ✓</text></g>
        <g class="switch-handle" id="factory-switch-handle" transform="translate(380 190)"><circle r="25"/><line x1="0" y1="0" x2="18" y2="-18"/><circle cx="21" cy="-21" r="7"/></g>
        <g class="package package-blue" id="factory-package" transform="translate(205 190)"><rect x="-19" y="-16" width="38" height="32" rx="6"/><text x="0" y="5" text-anchor="middle">B</text></g>
        <text class="belt-label" x="258" y="169">BĂNG CHUYỀN</text>
        <text class="belt-label" x="347" y="244">SWITCH</text>
      </svg>
      <div class="factory-controls">
        <div class="factory-instruction"><span>BƯỚC 1</span><b id="factory-instruction">Switch hiện đang ở A. Hãy chuyển sang B trước khi kiện hàng tới junction.</b></div>
        <button type="button" class="factory-action" id="factory-switch">GẠT SWITCH → B</button>
        <button type="button" class="factory-reset" id="factory-reset">Chơi lại minh họa</button>
      </div>
      <div class="factory-result" id="factory-result"><span>LIVE FEEDBACK</span><b>Kiện BLUE đang tới junction…</b></div>
    </div>
  </div>

  <div class="mastery-explainer" data-visual="kinetic-mastery-explainer">
    <div class="mastery-copy"><span>ĐIỀU LÀM NÓ THÀNH GAME</span><h3>Không phải “tìm đáp án”. Là <span>ngày càng vận hành giỏi hơn.</span></h3><p>Lần đầu bạn chỉ cố không làm sai. Sau nhiều lần chơi, bạn bắt đầu dự đoán congestion trước khi nó xảy ra, dùng hai tay song song, chọn việc ưu tiên tốt hơn và phục hồi lỗi nhanh hơn.</p></div>
    <div class="difficulty-ladder">
      <div><b>LEVEL 1</b><span>1 luồng · 1 switch</span><small>Hiểu thao tác</small></div><i>→</i>
      <div><b>LEVEL 2</b><span>Nhiều luồng</span><small>Chọn đúng route</small></div><i>→</i>
      <div><b>LEVEL 3</b><span>Xung đột / quá tải</span><small>Ưu tiên & recovery</small></div><i>→</i>
      <div><b>MASTERY</b><span>Dự đoán + hai tay</span><small>Personal best</small></div>
    </div>
  </div>

  <div class="kinetic-plain-loop" data-visual="kinetic-core-loop-plain">
    <h3>Core loop — dịch sang ngôn ngữ người chơi</h3>
    <div class="plain-loop-row"><span>NHÌN TÌNH HÌNH</span><i>→</i><span>ĐỔI ĐƯỜNG BẰNG TAY</span><i>→</i><span>XEM KẾT QUẢ</span><i>→</i><span>XỬ LÝ TÌNH HUỐNG MỚI</span><i>→</i><strong>CHƠI LẠI TỐT HƠN</strong></div>
    <small>Research terminology phía sau: read changing state → physically reroute → observe result → score/throughput feedback → demand changes → recover/optimize → retry/personal best.</small>
  </div>

  <div class="kinetic-evidence-boundary">
    <article><span class="boundary-label supported">RESEARCH-SUPPORTED CORE</span><p>Routing trong live system; reach/grab/rotate/redirect/switch; changing state; recovery/optimization; mastery/retry hypothesis; VR-vs-flat falsification.</p></article>
    <article><span class="boundary-label proposed">PRODUCT VISUALIZATION ADDED HERE</span><p>Nhà máy tự động, băng chuyền, kiện hàng và Machine A/B là <b>theme minh họa đề xuất</b> để làm concept dễ hình dung hơn — chưa khóa final theme.</p></article>
    <article><span class="boundary-label unproven">VẪN CHƯA ĐƯỢC CHỨNG MINH</span><p>PMF, WTP, retention, commercial success và việc factory theme có hấp dẫn người chơi hay không.</p></article>
  </div>

  <div class="kinetic-research-details">
    <div class="hypothesis-grid" data-visual="kinetic-hypotheses">
      <article><span>WHY‑VR</span><b>MEDIUM–HIGH</b><small>hypothesis</small></article>
      <article><span>REPLAY</span><b>HIGH</b><small>hypothesis</small></article>
      <article><span>PROTOTYPE FEASIBILITY</span><b>HIGH</b><small>hypothesis</small></article>
      <article><span>COMMERCIAL CONFIDENCE</span><b>NOT PROVEN</b><small>no PMF/WTP/retention proof</small></article>
    </div>
    <div class="mvp-boundary" data-visual="mvp-boundary">
      <div class="mvp-in"><h3>PROTOTYPE — IN</h3><span>compact factory workcell</span><span>routing & live state</span><span>grab / rotate / switch</span><span>feedback / scoring</span><span>replay / skill</span><span>VR vs flat test</span></div>
      <div class="mvp-out"><h3>NOT IN THIS PROTOTYPE</h3><span>large world</span><span>social graph</span><span>creator economy</span><span>marketplace</span><span>broad multiplayer</span><span>live-service complexity</span></div>
    </div>
  </div>

  <div class="kinetic-bottom-line"><span>NÓI GỌN TRONG 1 CÂU</span><b>Kinetic = “giữ một nhà máy đang chạy khỏi rối tung bằng cách dùng hai tay để định tuyến, ưu tiên và cứu lỗi — rồi chơi lại để vận hành giỏi hơn chính lần trước.”</b></div>
</section>'''

CSS_PATCH = r'''

/* === KINETIC EXPLAINER V2 · factory-theme communication layer === */
#kinetic.kinetic-explainer-v2{background:#f6f3ec;color:#151515;position:relative;overflow:hidden}
#kinetic.kinetic-explainer-v2:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(15,23,42,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(15,23,42,.035) 1px,transparent 1px);background-size:36px 36px;pointer-events:none}
#kinetic.kinetic-explainer-v2>*{position:relative;z-index:1}
#kinetic .kinetic-head-simple{align-items:flex-start}
#kinetic .kinetic-head-simple h2{color:#111827;margin-bottom:18px}
#kinetic .kinetic-head-simple h2 span{color:#d55b2d}
#kinetic .kinetic-one-liner{font-size:clamp(1.35rem,2.4vw,2.15rem);line-height:1.32;max-width:1050px;margin:0 0 14px;color:#111827;letter-spacing:-.025em}
#kinetic .kinetic-subline{font-size:1.05rem;line-height:1.72;max-width:960px;color:#4b5563;margin:0}
.theme-disclosure{display:flex;gap:18px;align-items:center;margin:30px 0 26px;padding:18px 22px;background:#fff;border:1px solid #d9d4c8;border-left:5px solid #d55b2d;border-radius:14px;box-shadow:0 8px 28px rgba(31,41,55,.06)}
.theme-disclosure .theme-pill{flex:0 0 auto;background:#111827;color:#fff;padding:8px 10px;border-radius:7px;font-size:.69rem;font-weight:800;letter-spacing:.09em}
.theme-disclosure div{display:grid;gap:4px}.theme-disclosure b{font-size:1rem}.theme-disclosure small{color:#6b7280;line-height:1.5}
.kinetic-simple-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:28px 0 42px}
.simple-card{background:#fff;border:1px solid #ded9ce;border-radius:16px;padding:22px;min-height:225px;box-shadow:0 8px 25px rgba(31,41,55,.045)}
.simple-card .simple-no{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#111827;color:#fff;font-size:.72rem;font-weight:800;margin-bottom:20px}
.simple-card h3{font-size:1.08rem;margin:0 0 10px;color:#111827}.simple-card p{margin:0;color:#4b5563;line-height:1.62;font-size:.92rem}
.factory-snapshot{display:grid;grid-template-columns:minmax(300px,.82fr) minmax(500px,1.38fr);gap:24px;align-items:stretch;margin:18px 0 46px}
.snapshot-copy{padding:28px;background:#171b20;color:#fff;border-radius:20px;display:flex;flex-direction:column}
.snapshot-kicker{font-size:.7rem;letter-spacing:.12em;font-weight:800;color:#f3a66f}.snapshot-copy h3{font-size:1.55rem;line-height:1.25;margin:10px 0 20px;color:#fff}
.thirty-seconds{list-style:none;margin:0;padding:0;display:grid;gap:0}.thirty-seconds li{display:grid;grid-template-columns:62px 1fr;gap:12px;padding:13px 0;border-top:1px solid rgba(255,255,255,.11)}.thirty-seconds li>b{color:#f3a66f;font-size:.79rem}.thirty-seconds li span{color:#d6d9dd;line-height:1.5;font-size:.88rem}
.factory-demo{background:#fff;border:1px solid #d7d2c7;border-radius:20px;padding:18px;box-shadow:0 14px 42px rgba(31,41,55,.08);overflow:hidden}
.factory-hud{display:flex;justify-content:space-between;gap:16px;align-items:center;padding:8px 4px 14px}.factory-hud span{font-size:.66rem;font-weight:800;letter-spacing:.11em;color:#6b7280}.factory-hud b{font-size:.78rem;color:#0f5d73;text-align:right}
.factory-svg{display:block;width:100%;height:auto;color:#6b7280}.factory-floor{fill:#eae6dc;stroke:#d3cec2;stroke-width:2}.machine rect{fill:#252a31;stroke:#111827;stroke-width:2;filter:url(#softShadow)}.machine text{fill:#fff;font-size:13px;font-weight:800;letter-spacing:.04em}.machine-a rect{fill:#6e3c36}.machine-b rect{fill:#17677b}.machine-b.target rect{stroke:#6cc6d8;stroke-width:4}.belt{fill:none;stroke:#9aa0a6;stroke-width:18;stroke-linecap:round}.belt-main{stroke:#7e858d}.route-to-a,.route-to-b{opacity:.3;transition:opacity .25s,stroke .25s}.route-to-b.active,.route-to-a.active{opacity:1;stroke:#2d879d}.junction-ring{fill:#f5f2ea;stroke:#333b45;stroke-width:8}.switch-handle{transition:transform .35s ease;transform-origin:380px 190px}.switch-handle circle:first-child{fill:#f0a057;stroke:#9a4d1e;stroke-width:3}.switch-handle line{stroke:#6f3514;stroke-width:7;stroke-linecap:round}.switch-handle circle:last-child{fill:#fff;stroke:#6f3514;stroke-width:3}.package-blue rect{fill:#2d8da5;stroke:#0c4d5e;stroke-width:3;filter:url(#softShadow)}.package-blue text{fill:#fff;font-size:14px;font-weight:900}.belt-label{font-size:11px;font-weight:800;fill:#6b7280;letter-spacing:.08em}.package-blue.running{animation:factoryPackageToB 2.5s cubic-bezier(.45,.05,.3,1) forwards}.package-blue.miss{animation:factoryPackageToA 2.5s cubic-bezier(.45,.05,.3,1) forwards}
@keyframes factoryPackageToB{0%{transform:translate(205px,190px)}45%{transform:translate(365px,190px)}70%{transform:translate(470px,235px)}100%{transform:translate(635px,285px)}}
@keyframes factoryPackageToA{0%{transform:translate(205px,190px)}45%{transform:translate(365px,190px)}70%{transform:translate(470px,145px)}100%{transform:translate(635px,105px)}}
.factory-controls{display:grid;grid-template-columns:1fr auto auto;gap:10px;align-items:center;margin-top:10px}.factory-instruction{display:grid;gap:3px}.factory-instruction span{font-size:.63rem;font-weight:800;letter-spacing:.1em;color:#d55b2d}.factory-instruction b{font-size:.78rem;line-height:1.35;color:#374151}.factory-action,.factory-reset{border:0;border-radius:10px;padding:12px 14px;font-weight:800;cursor:pointer}.factory-action{background:#d55b2d;color:#fff}.factory-action:disabled{background:#a7adb4;cursor:default}.factory-reset{background:#ebe8df;color:#333b45}.factory-result{margin-top:12px;padding:12px 14px;border-radius:10px;background:#eef6f7;display:flex;justify-content:space-between;gap:12px;align-items:center}.factory-result span{font-size:.62rem;font-weight:800;letter-spacing:.1em;color:#47747d}.factory-result b{font-size:.78rem;color:#174b58;text-align:right}.factory-result.success{background:#e9f5ed}.factory-result.success b{color:#236338}
.mastery-explainer{display:grid;grid-template-columns:.72fr 1.28fr;gap:28px;align-items:center;padding:30px;border:1px solid #d9d4c8;border-radius:20px;background:#fff;margin-bottom:28px}.mastery-copy>span{font-size:.67rem;font-weight:800;letter-spacing:.11em;color:#d55b2d}.mastery-copy h3{font-size:1.55rem;line-height:1.25;margin:9px 0 12px;color:#111827}.mastery-copy h3 span{color:#d55b2d}.mastery-copy p{color:#5b6470;line-height:1.62;margin:0}.difficulty-ladder{display:grid;grid-template-columns:1fr auto 1fr auto 1fr auto 1fr;align-items:center;gap:8px}.difficulty-ladder>div{min-height:128px;border-radius:13px;background:#f1eee6;padding:16px;display:flex;flex-direction:column;justify-content:center;gap:5px}.difficulty-ladder>div:last-child{background:#1f2933;color:#fff}.difficulty-ladder b{font-size:.68rem;letter-spacing:.09em;color:#d55b2d}.difficulty-ladder>div:last-child b{color:#f3a66f}.difficulty-ladder span{font-weight:800;font-size:.86rem}.difficulty-ladder small{font-size:.72rem;color:#707782}.difficulty-ladder>div:last-child small{color:#cbd1d8}.difficulty-ladder i{font-style:normal;color:#9aa0a6;font-weight:800}
.kinetic-plain-loop{padding:24px;border-radius:18px;background:#171b20;color:#fff;margin-bottom:28px}.kinetic-plain-loop h3{margin:0 0 16px;color:#fff;font-size:1.1rem}.plain-loop-row{display:flex;gap:9px;align-items:center;flex-wrap:wrap}.plain-loop-row span,.plain-loop-row strong{padding:10px 12px;border:1px solid rgba(255,255,255,.18);border-radius:9px;font-size:.72rem;letter-spacing:.05em}.plain-loop-row strong{background:#d55b2d;border-color:#d55b2d}.plain-loop-row i{font-style:normal;color:#f3a66f}.kinetic-plain-loop>small{display:block;margin-top:14px;color:#aeb6bf;line-height:1.5}
.kinetic-evidence-boundary{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:28px}.kinetic-evidence-boundary article{background:#fff;border:1px solid #ded9ce;border-radius:14px;padding:18px}.kinetic-evidence-boundary p{margin:10px 0 0;color:#5b6470;font-size:.83rem;line-height:1.55}.boundary-label{font-size:.62rem;font-weight:900;letter-spacing:.09em}.boundary-label.supported{color:#1b6a55}.boundary-label.proposed{color:#b14d24}.boundary-label.unproven{color:#8c3c3c}
.kinetic-research-details{border-top:1px solid #d8d3c7;padding-top:26px}.kinetic-bottom-line{margin-top:28px;padding:22px 24px;background:#d55b2d;color:#fff;border-radius:16px;display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:center}.kinetic-bottom-line span{font-size:.65rem;font-weight:900;letter-spacing:.11em;white-space:nowrap}.kinetic-bottom-line b{font-size:1.04rem;line-height:1.5}
@media(max-width:1050px){.kinetic-simple-grid{grid-template-columns:repeat(2,1fr)}.factory-snapshot{grid-template-columns:1fr}.mastery-explainer{grid-template-columns:1fr}.difficulty-ladder{grid-template-columns:1fr 1fr;gap:10px}.difficulty-ladder i{display:none}.kinetic-evidence-boundary{grid-template-columns:1fr}.factory-controls{grid-template-columns:1fr 1fr}.factory-instruction{grid-column:1/-1}}
@media(max-width:640px){.theme-disclosure{align-items:flex-start;flex-direction:column}.kinetic-simple-grid{grid-template-columns:1fr}.simple-card{min-height:0}.snapshot-copy{padding:22px}.factory-demo{padding:10px}.factory-hud{align-items:flex-start;flex-direction:column}.factory-hud b{text-align:left}.factory-controls{grid-template-columns:1fr}.factory-action,.factory-reset{width:100%}.factory-result{align-items:flex-start;flex-direction:column}.factory-result b{text-align:left}.difficulty-ladder{grid-template-columns:1fr}.kinetic-bottom-line{grid-template-columns:1fr;gap:7px}.plain-loop-row{align-items:flex-start;flex-direction:column}.plain-loop-row i{transform:rotate(90deg);margin-left:20px}}
'''

JS_PATCH = r'''

// === KINETIC EXPLAINER V2 · factory micro-demo ===
(() => {
  const demo = document.getElementById('factory-demo');
  if (!demo) return;
  const pkg = document.getElementById('factory-package');
  const switchBtn = document.getElementById('factory-switch');
  const resetBtn = document.getElementById('factory-reset');
  const result = document.getElementById('factory-result');
  const instruction = document.getElementById('factory-instruction');
  const hud = document.getElementById('factory-hud-state');
  const handle = document.getElementById('factory-switch-handle');
  const routeA = demo.querySelector('.route-to-a');
  const routeB = demo.querySelector('.route-to-b');
  let routedToB = false;
  let timer = null;

  const reset = () => {
    if (timer) window.clearTimeout(timer);
    routedToB = false;
    pkg.classList.remove('running','miss');
    void pkg.getBoundingClientRect();
    routeA.classList.add('active');
    routeB.classList.remove('active');
    handle.style.transform = 'translate(380px,190px) rotate(-42deg)';
    switchBtn.disabled = false;
    switchBtn.textContent = 'GẠT SWITCH → B';
    instruction.textContent = 'Switch hiện đang ở A. Hãy chuyển sang B trước khi kiện hàng tới junction.';
    hud.textContent = 'MỤC TIÊU: đưa kiện BLUE → MACHINE B';
    result.classList.remove('success');
    result.querySelector('b').textContent = 'Kiện BLUE đang tới junction…';
  };

  switchBtn.addEventListener('click', () => {
    if (routedToB) return;
    routedToB = true;
    routeA.classList.remove('active');
    routeB.classList.add('active');
    handle.style.transform = 'translate(380px,190px) rotate(42deg)';
    switchBtn.disabled = true;
    switchBtn.textContent = 'SWITCH ĐÃ Ở B ✓';
    instruction.textContent = 'Đúng. Bây giờ nhìn kiện hàng đi qua junction và tới Machine B.';
    pkg.classList.remove('miss');
    pkg.classList.add('running');
    result.querySelector('b').textContent = 'Đã đổi route → theo dõi kết quả…';
    timer = window.setTimeout(() => {
      result.classList.add('success');
      result.querySelector('b').textContent = '✓ ĐÚNG TUYẾN — Machine B nhận hàng. Flow tiếp tục.';
      hud.textContent = 'ROUND 1 CLEAR · tiếp theo: nhiều luồng + quá tải';
    }, 2550);
  });

  resetBtn.addEventListener('click', reset);
  reset();
})();
'''

html = index_path.read_text(encoding="utf-8-sig")
pattern = re.compile(r'<section id="kinetic" class="section kinetic-section dark-section" data-section="10">.*?</section>\s*(?=<section id="falsification")', re.S)
if not pattern.search(html):
    # Allow rerun/idempotence if the class was already changed.
    pattern = re.compile(r'<section id="kinetic" class="section kinetic-section kinetic-explainer-v2" data-section="10">.*?</section>\s*(?=<section id="falsification")', re.S)
if not pattern.search(html):
    raise SystemExit("Could not locate Kinetic section; aborting without modifying report.")
html = pattern.sub(NEW_SECTION + "\n\n", html, count=1)
index_path.write_text(html, encoding="utf-8")

css = css_path.read_text(encoding="utf-8-sig")
marker = "/* === KINETIC EXPLAINER V2 · factory-theme communication layer === */"
if marker in css:
    css = css.split(marker, 1)[0].rstrip() + "\n"
css_path.write_text(css + CSS_PATCH, encoding="utf-8")

js = js_path.read_text(encoding="utf-8-sig")
js_marker = "// === KINETIC EXPLAINER V2 · factory micro-demo ==="
if js_marker in js:
    js = js.split(js_marker, 1)[0].rstrip() + "\n"
js_path.write_text(js + JS_PATCH, encoding="utf-8")

if readme_path.exists():
    readme = readme_path.read_text(encoding="utf-8-sig")
    note = "\n## Kinetic explainer v2\nThe Kinetic section uses an automated-factory/sorting-plant theme as a communication visualization. The factory theme is proposed/illustrative, not a research-proven final theme. Research-supported interaction and decision boundaries remain unchanged.\n"
    if "## Kinetic explainer v2" not in readme:
        readme_path.write_text(readme.rstrip() + "\n" + note, encoding="utf-8")

print("Kinetic explainer v2 patch applied successfully.")
