/* Skill switch, balloon target-zone painter, Buck's Secret settings (calculator side). */
(()=>{'use strict';
const TICKET_URL='__TICKET_URL__';
const $=id=>document.getElementById(id);
let S=lbLoadSkill(),brush='G',brushSize=1,zoom=1,moveMode=false;
const persist=()=>{lbSaveSkill(S)};
/* ---------- markup ---------- */
const bar=document.createElement('section');bar.className='skill-bar';bar.id='skillBar';
bar.innerHTML='<button type="button" id="skillToggle" class="skill-toggle" aria-pressed="false"><span class="sk-knob"></span><span class="sk-text">🎯 Skill mode: <b>OFF</b></span></button>'+
 '<a class="skill-play" id="skillPlay" href="'+TICKET_URL+'">🎟️ Play ticket</a>'+
 '<p class="skill-explain" id="skillExplain"></p>';
const card=document.createElement('section');card.className='card skill-card';card.id='skillCard';
card.innerHTML='<div class="card-top"><h3>🎯 Balloon target zones</h3><span class="muted tiny">One grid · all 3 balloons</span></div>'+
 '<p class="skill-help">Pick a color, then tap or drag on the balloon. Each square is one real pixel of the balloon. Where the crosshair’s centre pixel lands decides that balloon’s number. <b>Your worst shot sets the prize:</b> 5, 5, 1 pays $1; any $0 shot means no prize.</p>'+
 '<div class="sk-palette" id="skPalette">'+LB_ZONES.map(z=>'<div class="sk-zone" data-zone="'+z+'"><button type="button" class="sk-swatch" data-zone="'+z+'" aria-label="Paint '+LB_ZONE_INFO[z].name+'"><i style="background:'+LB_ZONE_INFO[z].col+'"></i>'+LB_ZONE_INFO[z].name+(z==='G'?' <small>Buck’s Secret</small>':'')+'</button><label class="sk-val"><span>$</span><input type="number" inputmode="decimal" min="0" step="1" data-val="'+z+'" aria-label="'+LB_ZONE_INFO[z].name+' prize in dollars"></label></div>').join('')+'</div>'+
 '<div class="sk-tools"><div class="sk-seg" role="group" aria-label="Brush size"><span>Brush</span><button type="button" data-brush="1" aria-pressed="true">1</button><button type="button" data-brush="3" aria-pressed="false">3×3</button><button type="button" data-brush="5" aria-pressed="false">5×5</button></div>'+
 '<div class="sk-seg" role="group" aria-label="Zoom"><button type="button" id="skZoomOut" aria-label="Zoom out">−</button><span id="skZoomLabel">1×</span><button type="button" id="skZoomIn" aria-label="Zoom in">+</button><button type="button" id="skMove" aria-pressed="false">✋ Move</button></div></div>'+
 '<div class="sk-shells"><label for="skShells">Shells per ticket</label><input type="number" id="skShells" inputmode="numeric" min="1" max="20" step="1"><small class="tiny muted">Each shot uses one, hit or miss. Balloons left when you run out count as $0.</small></div>'+
 '<div class="sk-gridwrap" id="skWrap"><canvas id="skGrid" aria-label="Balloon target zone grid. Tap squares to paint."></canvas></div>'+
 '<p class="tiny muted sk-legend">White dot = dead-centre pixel. Gold squares = Buck’s Secret.</p>'+
 '<details class="sk-rings"><summary>Quick rings (bullseye range)</summary>'+
 [['gold','Gold (Buck’s Secret) size',0,10],['green','Green ring size',0,18],['yellow','Yellow ring size',0,18]].map(([k,l,lo,hi])=>'<div class="sk-ring"><label for="skR_'+k+'">'+l+'</label><input type="range" id="skR_'+k+'" min="'+lo+'" max="'+hi+'" step="0.5"><output id="skO_'+k+'"></output></div>').join('')+
 '<button type="button" id="skRepaint" class="sk-btn">Repaint as rings</button><small class="tiny muted">Repainting replaces hand-painted squares. Sizes are in pixels from the centre; gold 0 = dead-centre pixel only.</small></details>'+
 '<div class="sk-stats" id="skStats"></div>';
const secret=document.createElement('section');secret.className='card secret-card';secret.id='secretCard';
secret.innerHTML='<div class="card-top"><h3>🦌 Buck’s Secret</h3><span class="muted tiny">Skill ON or OFF</span></div>'+
 '<p class="skill-help">The <b>gold</b> squares on the balloon grid are Buck’s Secret (default: the dead-centre pixel only). <b>Skill ON:</b> a gold hit shows the gold prize. <b>Skill OFF:</b> a gold hit pays extra on top of the ticket, even on a losing ticket.</p><p class="tiny muted" id="secGoldInfo"></p>'+
 '<label class="sk-check"><input type="checkbox" id="secOn"> Buck’s Secret on</label>'+
 '<div class="sec-grid">'+
 '<label for="secAmount">Skill OFF: extra per gold hit</label><span class="sk-money">$<input type="number" id="secAmount" inputmode="decimal" min="0" step="1"></span>'+
 '<label for="secMax">Skill OFF: most extra per ticket</label><span class="sk-money">$<input type="number" id="secMax" inputmode="decimal" min="0" step="1"></span></div>';
/* place: bar under the header; zone card first in the ticket column; secret card after modifiers */
const header=document.querySelector('.header');
const anchor=document.querySelector('.v3-switch')||header;anchor.insertAdjacentElement('afterend',bar);
const col=$('v3TicketCol');if(col)col.prepend(card);else bar.insertAdjacentElement('afterend',card);
const mod=$('modifierEditor');if(mod)mod.insertAdjacentElement('afterend',secret);else card.insertAdjacentElement('afterend',secret);
/* odds-driven cards get a note in Skill mode */
const oddsCard=[...document.querySelectorAll('.card h3')].find(h=>/Prize odds editor/.test(h.textContent))?.closest('.card');
for(const c of [oddsCard,mod].filter(Boolean)){c.classList.add('skill-odds');const n=document.createElement('div');n.className='skill-note';n.textContent='🎯 Skill mode is on: the ticket ignores these odds. Switch Skill off to use them.';c.prepend(n);}

/* ---------- big playable ticket + play sliders (Skill mode) ---------- */
const play=document.createElement('section');play.className='card skill-play-card';play.id='skillPlayCard';
const SL=[['speed','Balloon movement speed',0.3,2.2,0.1,v=>Number(v).toFixed(1)+'×'],['movement','Balloon movement distance',30,120,5,v=>v+'%'],['size','Balloon size',70,130,5,v=>v+'%'],['wobble','Crosshair pattern size (∞ then 8)',0,40,1,v=>v+'px'],['lift','Crosshair height above finger',0,220,10,v=>v+'px']];
play.innerHTML='<div class="card-top"><h3>🎟️ Play Lucky Buck (Skill)</h3><a class="tiny sk-open" href="'+TICKET_URL+'">Open full screen ↗</a></div>'+
 '<iframe id="skFrame" title="Playable Lucky Buck ticket" scrolling="no"></iframe>'+
 '<details class="sk-playset" open><summary>🎛️ Play settings</summary>'+SL.map(([k,l,lo,hi,st])=>'<div class="sk-slider"><label for="skP_'+k+'">'+l+'</label><output id="skPO_'+k+'"></output><input type="range" id="skP_'+k+'" min="'+lo+'" max="'+hi+'" step="'+st+'"></div>').join('')+
 '<label class="sk-check"><input type="checkbox" id="skP_sound"> Sound effects</label>'+
 '<button type="button" class="sk-btn" id="skPReset">Reset play settings</button></details>';
const scratchCard=document.querySelector('.showcase-center > .card');
/* Ticket goes first in Skill mode so it is easy to play; the zone grid follows. */card.insertAdjacentElement('beforebegin',play);scratchCard?.classList.add('skill-hide');
document.getElementById('shotCalculator')?.classList.add('skill-hide');
const frame=$('skFrame');
function fitFrame(){try{const d=frame.contentDocument,pg=d&&d.querySelector('.page');if(pg)frame.style.height=Math.ceil(pg.getBoundingClientRect().height)+2+'px';}catch(e){}}
frame.addEventListener('load',()=>{fitFrame();try{const W=frame.contentWindow;new W.ResizeObserver(fitFrame).observe(frame.contentDocument.querySelector('.page'));}catch(e){}});
function loadFrame(){if(!frame.getAttribute('src'))frame.src=TICKET_URL+(TICKET_URL.includes('?')?'&':'?')+'embed=1';}
function syncPlay(){for(const [k,,,,,f] of SL){const i=$('skP_'+k);if(document.activeElement!==i)i.value=S.play[k];$('skPO_'+k).textContent=f(i.value);}$('skP_sound').checked=S.play.sound;}
for(const [k,,,,,f] of SL)$('skP_'+k).addEventListener('input',e=>{S.play[k]=Number(e.target.value);$('skPO_'+k).textContent=f(e.target.value);persist();});
$('skP_sound').addEventListener('change',e=>{S.play.sound=e.target.checked;persist();});
$('skPReset').addEventListener('click',()=>{S.play={...LB_PLAY_DEFAULTS};persist();syncPlay();});
/* ---------- grid drawing ---------- */
const cv=$('skGrid'),ctx=cv.getContext('2d'),wrap=$('skWrap');
let cell=10;
function size(){const w=Math.max(200,wrap.clientWidth-2);cell=Math.max(6,Math.floor(w*zoom/LB_GW));cv.width=cell*LB_GW;cv.height=cell*LB_GH;cv.style.width=cv.width+'px';cv.style.height=cv.height+'px';draw();}
function draw(){ctx.clearRect(0,0,cv.width,cv.height);const g=Math.max(1,Math.round(cell/9));
 for(let j=0;j<LB_GH;j++)for(let i=0;i<LB_GW;i++){const k=j*LB_GW+i,z=S.grid[k];if(z==='.')continue;ctx.fillStyle=LB_ZONE_INFO[z].col;ctx.fillRect(i*cell,j*cell,cell-g,cell-g);
  if(LB_MASK[k]==='#'){ctx.fillStyle='#0006';ctx.fillRect(i*cell,j*cell,cell-g,cell-g);}}
 ctx.fillStyle='#fff';ctx.beginPath();ctx.arc((LB_CX+.5)*cell-g/2,(LB_CY+.5)*cell-g/2,Math.max(2,cell*.22),0,Math.PI*2);ctx.fill();
 ctx.strokeStyle='#000';ctx.lineWidth=Math.max(1,cell*.08);ctx.beginPath();ctx.arc((LB_CX+.5)*cell-g/2,(LB_CY+.5)*cell-g/2,Math.max(2,cell*.22),0,Math.PI*2);ctx.stroke();}
function paintAt(e){const r=cv.getBoundingClientRect();const i=Math.floor((e.clientX-r.left)/r.width*LB_GW),j=Math.floor((e.clientY-r.top)/r.height*LB_GH);const h=(brushSize-1)/2;let changed=false;const a=S.grid.split('');
 for(let y=j-h;y<=j+h;y++)for(let x=i-h;x<=i+h;x++){if(x<0||y<0||x>=LB_GW||y>=LB_GH)continue;const k=y*LB_GW+x;if(a[k]==='.'||a[k]===brush)continue;a[k]=brush;changed=true;}
 if(changed){S.grid=a.join('');draw();}return changed;}
let painting=false,dirty=false;
cv.addEventListener('pointerdown',e=>{if(moveMode)return;painting=true;dirty=paintAt(e)||dirty;cv.setPointerCapture?.(e.pointerId);e.preventDefault();});
cv.addEventListener('pointermove',e=>{if(!painting)return;dirty=paintAt(e)||dirty;e.preventDefault();});
const endPaint=()=>{if(!painting)return;painting=false;if(dirty){persist();stats();}dirty=false;};
cv.addEventListener('pointerup',endPaint);cv.addEventListener('pointercancel',endPaint);
/* ---------- stats ---------- */
function stats(){const cnt={G:0,N:0,Y:0,R:0};let tot=0;for(const c of S.grid)if(c!=='.'){cnt[c]++;tot++;}
 /* worst-shot rule: prize = lowest of the three balloon values */let win=0,ev=0;for(const a of LB_ZONES)for(const b of LB_ZONES)for(const c of LB_ZONES){const p=cnt[a]*cnt[b]*cnt[c]/tot**3,v=Math.min(S.values[a],S.values[b],S.values[c]);if(v>0){win+=p;ev+=p*v;}}
 const gi=$('secGoldInfo');if(gi)gi.textContent='Gold area now: '+cnt.G+' square'+(cnt.G===1?'':'s')+(cnt.G===1&&S.grid[LB_CY*LB_GW+LB_CX]==='G'?' (dead-centre pixel)':'')+'. Turn Skill on to paint it bigger or smaller.';
 $('skStats').innerHTML='<table class="sk-table"><tr><th>Zone</th><th>Prize</th><th>Squares</th><th>Balloon</th></tr>'+LB_ZONES.map(z=>'<tr><td><i style="background:'+LB_ZONE_INFO[z].col+'"></i>'+LB_ZONE_INFO[z].name+'</td><td>$'+S.values[z]+'</td><td>'+cnt[z]+'</td><td>'+(cnt[z]/tot*100).toFixed(1)+'%</td></tr>').join('')+'</table>'+
  '<p class="tiny muted">If all 3 shots hit random spots on the balloon (no misses): win '+(win*100).toFixed(2)+'% of tickets, average prize $'+ev.toFixed(3)+' per ticket (Buck’s Secret not included). Better aim = better results.</p>';}
/* ---------- controls ---------- */
function syncUI(){const on=S.skillOn;document.body.classList.toggle('skill-on',on);$('skillToggle').setAttribute('aria-pressed',String(on));$('skillToggle').querySelector('b').textContent=on?'ON':'OFF';
 $('skillExplain').textContent=on?'ON: where you hit each balloon decides its number (the grid below). Prize odds are not used.':'OFF: the ticket uses the prize odds and Luck settings in this calculator.';
 card.classList.toggle('hidden',!on);play.classList.toggle('hidden',!on);if(on)loadFrame();syncPlay();
 for(const b of card.querySelectorAll('.sk-swatch'))b.setAttribute('aria-pressed',String(b.dataset.zone===brush));
 for(const z of card.querySelectorAll('.sk-zone'))z.classList.toggle('active',z.dataset.zone===brush);
 for(const i of card.querySelectorAll('[data-val]'))if(document.activeElement!==i)i.value=S.values[i.dataset.val];
 if(document.activeElement!==$('skShells'))$('skShells').value=S.shells;
 for(const k of ['gold','green','yellow']){$('skR_'+k).value=S.rings[k];$('skO_'+k).textContent=S.rings[k]+' px';}
 $('secOn').checked=S.secret.on;$('secAmount').value=S.secret.amount;$('secMax').value=S.secret.max;
 for(const id of ['secAmount','secMax'])$(id).disabled=!S.secret.on;
 $('skZoomLabel').textContent=zoom+'×';$('skMove').setAttribute('aria-pressed',String(moveMode));cv.style.touchAction=moveMode?'auto':'none';wrap.classList.toggle('zoomed',zoom>1);}
$('skillToggle').addEventListener('click',()=>{S.skillOn=!S.skillOn;persist();syncUI();if(S.skillOn)size();});
card.addEventListener('click',e=>{const sw=e.target.closest('.sk-swatch');if(sw){brush=sw.dataset.zone;moveMode=false;syncUI();}
 const br=e.target.closest('[data-brush]');if(br){brushSize=Number(br.dataset.brush);for(const b of card.querySelectorAll('[data-brush]'))b.setAttribute('aria-pressed',String(b===br));}});
card.addEventListener('input',e=>{const z=e.target.dataset?.val;if(z){const v=Number(e.target.value);if(Number.isFinite(v)&&v>=0){S.values[z]=v;persist();stats();}}
 const m=/^skR_(\w+)$/.exec(e.target.id||'');if(m){S.rings[m[1]]=Number(e.target.value);$('skO_'+m[1]).textContent=S.rings[m[1]]+' px';persist();}});
$('skShells').addEventListener('input',e=>{const v=Math.round(Number(e.target.value));if(v>=1&&v<=20){S.shells=v;persist();}});
$('skRepaint').addEventListener('click',()=>{const r=S.rings;const g=r.gold,n=Math.max(g,r.green),y=Math.max(n,r.yellow);S.grid=lbRingGrid(g,n,y);persist();draw();stats();});
$('skZoomIn').addEventListener('click',()=>{zoom=Math.min(3,zoom+1);syncUI();size();});
$('skZoomOut').addEventListener('click',()=>{zoom=Math.max(1,zoom-1);if(zoom===1)moveMode=false;syncUI();size();});
$('skMove').addEventListener('click',()=>{moveMode=!moveMode;syncUI();});
$('secOn').addEventListener('change',e=>{S.secret.on=e.target.checked;persist();syncUI();});
for(const id of ['secAmount','secMax'])$(id).addEventListener('input',e=>{const v=Number(e.target.value);if(Number.isFinite(v)&&v>=0){S.secret[id==='secAmount'?'amount':'max']=v;persist();}});
window.addEventListener('resize',()=>{if(S.skillOn)size();});
window.addEventListener('storage',e=>{if(e.key===LB_SKILL_KEY){S=lbLoadSkill();syncUI();if(S.skillOn)size();stats();}});
syncUI();stats();if(S.skillOn)requestAnimationFrame(size);
window.__luckyBuckSkill={get:()=>S};
})();
