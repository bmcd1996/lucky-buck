"""Build the Skill-mode preview: calculator (index.html) + ticket (ticket.html) in this folder.
Reads ~/lucky-buck/index.html and ticket-1.0.0.html; never writes to the repo."""
import re, base64, io, os, sys
from PIL import Image
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.expanduser('~/lucky-buck')
OUT = sys.argv[1] if len(sys.argv) > 1 else HERE
TICKET_URL = sys.argv[2] if len(sys.argv) > 2 else 'ticket.html'
CALC_URL = sys.argv[3] if len(sys.argv) > 3 else 'index.html'
VERSION = sys.argv[4] if len(sys.argv) > 4 else 'v3.4.0 preview'

calc = open(f'{REPO}/index.html').read()
tick = open(f'{REPO}/ticket-1.0.0.html').read()

def once(s, old, new):
    n = s.count(old)
    assert n == 1, (n, old[:80])
    return s.replace(old, new)

# ---- balloon mask from the ticket's own red balloon (4 px per cell) ----
i = tick.find('id="balloon0"')
m = re.search(r'src="data:image/png;base64,([^"]+)"', tick[i:])
a = np.array(Image.open(io.BytesIO(base64.b64decode(m.group(1)))).convert('RGBA'))
mask = ''
for y in range(a.shape[0] // 4):
    for x in range(a.shape[1] // 4):
        c = a[y * 4 + 2, x * 4 + 2]
        mask += '.' if c[3] < 128 else ('#' if int(c[:3].sum()) < 120 else 'o')
assert len(mask) == 37 * 45 and mask[22 * 37 + 18] != '.'
shared = open(f'{HERE}/shared.js').read().replace('__MASK__', mask)

# ================= calculator =================
css = open(f'{HERE}/calc_skill.css').read()
js = open(f'{HERE}/calc_skill.js').read().replace('__TICKET_URL__', TICKET_URL)
calc = once(calc, '</style>\n</head>', css + '</style>\n</head>')
calc = calc.replace('>v3.3.3</span>', '>' + VERSION + '</span>')
k = calc.rfind('</body>')
calc = calc[:k] + '<script>\n' + shared + '\n' + js + '\n</script>\n' + calc[k:]
open(f'{OUT}/index.html' if OUT == HERE else f'{OUT}/calc.html', 'w').write(calc)

# ================= ticket =================
T = tick
T = once(T, "const nfmt=n=>Number(n).toLocaleString('en-US');",
 "const nfmt=n=>Number(n).toLocaleString('en-US');\n" + shared + r"""
/* Calculator odds for Skill OFF: the lucky-buck ticket's prize rows plus its Luck level (Hot Streak, Double Down, Rescue Bonus and special items are not applied on this ticket yet). */
function calcOdds(){const fb={p:[75,17,6.5,1.5],src:'built-in odds (no calculator save found)'};
 try{const st=JSON.parse(localStorage.getItem(LB_CALC_KEY)||'null');const t=st&&Array.isArray(st.tickets)&&st.tickets.find(x=>x.id==='lucky-buck');if(!t)return fb;
  const rows=t.rows.filter(r=>r.kind!=='jackpot');const L=rows.find(r=>r.kind==='lose'),c=a=>rows.find(r=>r.kind==='cash'&&Number(r.amount)===a);
  if(rows.length!==4||!L||!c(1)||!c(5)||!c(25))return {...fb,src:'built-in odds (calculator ticket has a different prize set)'};
  let p=[L.chance,c(1).chance,c(5).chance,c(25).chance].map(Number);const lv=Number(t.luck)||0;
  if(lv>0&&t.luckMode==='luckyBuck'){const cu=t.rates?.luck?.mode==='edit'?t.rates.luck.levels?.[lv]:null;p=cu&&cu.length===4?cu.map(Number):[p[0]-(11/3)*lv,p[1]+lv,p[2]+2*lv,p[3]+(2/3)*lv];}
  const sum=p.reduce((x,y)=>x+y,0);if(!p.every(v=>Number.isFinite(v)&&v>=0)||Math.abs(sum-100)>1e-6)return {...fb,src:'built-in odds (calculator odds invalid)'};
  return {p,src:'calculator'+(lv>0?' + Luck '+lv:'')};}catch(e){return fb}}
let S=lbLoadSkill(),bonus=0,shells=0;
const bsz=()=>S.play.size/100;
/* Play settings: shared with the calculator's sliders (same saved settings). */
const PLAY_IDS=[['speed','speed'],['movement','movement'],['wobble','wobble'],['lift','lift'],['bsize','size']];
function outText(id){const i=$(id),o=$(id+'Out');if(o)o.textContent=(id==='speed'?Number(i.value).toFixed(1)+'×':id==='movement'||id==='bsize'?i.value+'%':i.value+'px');}
function applyPlay(){for(const [id,k] of PLAY_IDS){$(id).value=S.play[k];outText(id);}$('sound').checked=S.play.sound;front.style.setProperty('--bs',bsz());}
function savePlay(k,v){const cur=lbLoadSkill();cur.play[k]=v;lbSaveSkill(cur);S.play=cur.play;front.style.setProperty('--bs',bsz());}
if(new URLSearchParams(location.search).get('embed')==='1')document.documentElement.classList.add('embed');
function showShells(){const box=$('shellBox');if(!box)return;box.style.display=S.skillOn?'':'none';$('shells').textContent=shells+'/'+S.shells;}
function cellFor(b,spot,r){const cs=r.width*0.228*bsz()/LB_GW;return{cx:Math.floor(LB_CX+.5+(spot.x-b.x)*r.width/cs),cy:Math.floor(LB_CY+.5+(spot.y-b.y)*r.height/cs)}}
function inMask(c){return c.cx>=0&&c.cx<LB_GW&&c.cy>=0&&c.cy<LB_GH&&LB_MASK[c.cy*LB_GW+c.cx]!=='.'}
function showMode(){const o=calcOdds();$('modeNote').innerHTML=S.skillOn?'<b>🎯 Skill mode ON</b> (set in the calculator): where you hit each balloon decides its number, and your worst shot sets the prize. Gold $'+S.values.G+', green $'+S.values.N+', yellow $'+S.values.Y+', red $'+S.values.R+'. '+S.shells+' shells per ticket; balloons left when you run out count as $0.':'<b>Skill mode OFF</b>: odds from '+o.src+': lose '+o.p[0].toFixed(2).replace(/\.?0+$/,'')+'%, $1 '+o.p[1].toFixed(2).replace(/\.?0+$/,'')+'%, $5 '+o.p[2].toFixed(2).replace(/\.?0+$/,'')+'%, $25 '+o.p[3].toFixed(2).replace(/\.?0+$/,'')+'%.';
 const gold=[...S.grid].filter(c=>c==='G').length;
 $('modeNote').innerHTML+=S.secret.on?' Buck’s Secret = the gold spot ('+gold+' pixel'+(gold===1?'':'s')+')'+(S.skillOn?': it shows the gold prize.':': each gold hit pays +$'+S.secret.amount+', up to +$'+S.secret.max+' per ticket.'):' Buck’s Secret is off.';
 $('force').disabled=S.skillOn;showShells();}
window.addEventListener('storage',e=>{if(e.key===LB_SKILL_KEY||e.key===LB_CALC_KEY){const f=lbLoadSkill();if(!purchased||completed)S=f;else S.play=f.play;showMode();applyPlay();}});
""")
T = once(T, "if(forced==='normal'){const r=Math.random()*100;forced=r<75?'lose':r<92?'1':r<98.5?'5':'25'}",
 "if(forced==='normal'){const p=calcOdds().p,r=Math.random()*100;forced=r<p[0]?'lose':r<p[0]+p[1]?'1':r<p[0]+p[1]+p[2]?'5':'25'}")
T = once(T, "ticketResult=baseOutcome();purchased=true;",
 "S=lbLoadSkill();bonus=0;shells=S.shells;showMode();showShells();ticketResult=S.skillOn?{numbers:[null,null,null],winning:0,skill:true}:baseOutcome();purchased=true;")
T = once(T, "<span class=\"glyph\">?</span>';}",
 "<span class=\"glyph\">?</span>';}front.style.setProperty('--bs',bsz());")
# --- shooting: replace hit detection + reveal + payout ---
old_start = "const hitRadius=width*.106,"
s0 = T.index(old_start); s1 = T.index("function loop(now)")
new_shoot = r"""const hitRadius=width*.106*bsz(),accFor=d=>Math.round(clamp(100*(1-Math.pow(d/(width*.28),2)),0,100));let b,accuracy,cell,label='';
if(ticketResult.skill){shells--;showShells();const h=remaining.map(o=>({o,c:cellFor(o,spot,r)})).find(q=>inMask(q.c));
 if(!h){$('accuracy').textContent='miss';playSound('miss');effect(spot.x,spot.y,'MISS!',false);if(shells<=0){outOfShells();return;}updateLabel('Miss! '+shells+' shell'+(shells===1?'':'s')+' left. Hold, follow a balloon, release.');return;}
 b=h.o;cell=h.c;const z=S.grid[cell.cy*LB_GW+cell.cx];b.amount=Number(S.values[z])||0;b.zone=z;ticketResult.numbers[balloons.indexOf(b)]=b.amount;accuracy=accFor(Math.hypot((b.x-spot.x)*width,(b.y-spot.y)*height));label=LB_ZONE_INFO[z].name;$('accuracy').textContent=label;
}else{accuracy=accFor(closest.d);$('accuracy').textContent=accuracy+'%';
 if(closest.d>hitRadius){playSound('miss');effect(spot.x,spot.y,'MISS!',false);updateLabel('Miss! Try again. Hold, follow a balloon, release.');return;}
 b=closest.b;cell=cellFor(b,spot,r);}
/* Buck's Secret = the gold squares of the grid. Skill ON: gold shows the gold prize. Skill OFF: gold pays an extra bonus. */
const perfect=S.secret.on&&lbIsGold(S,cell);let add=0;if(perfect&&!ticketResult.skill){add=Math.max(0,Math.min(S.secret.amount,S.secret.max-bonus));bonus+=add;}
b.popped=true;b.accuracy=accuracy;playSound(perfect||(ticketResult.skill?b.zone==='G':accuracy>=95)?'bull':'pop');b.node.classList.add('popped');b.node.style.opacity='0';const n=document.createElement('span');n.className='revealed p'+b.amount;starBurst(b.x,b.y,n);n.textContent=b.amount===0?'$0':'$'+b.amount;n.style.left=(b.x*100)+'%';n.style.top=(b.y*100)+'%';front.append(n);
const popped=balloons.filter(o=>o.popped).length;$('hits').textContent=popped+'/3';
if(perfect)effect(b.x,b.y-.075,add>0?'BUCK’S SECRET +$'+add:'BUCK’S SECRET!',true);else if(ticketResult.skill)effect(b.x,b.y-.075,b.zone==='G'?'BULLSEYE!':label.toUpperCase(),true);else if(accuracy<95)effect(b.x,b.y,accuracy+'% HIT',true);
if(popped<3&&ticketResult.skill&&shells<=0){outOfShells();return;}
updateLabel(popped===3?'Checking your numbers…':`${popped}/3 balloons popped — keep going!`+(ticketResult.skill?' '+shells+' shell'+(shells===1?'':'s')+' left.':'')+(bonus>0?' Secret bonus +$'+bonus:''));
if(popped===3)finishTicket();
}
/* Out of shells (Skill mode): every balloon still floating counts as $0. */
function outOfShells(){for(const o of balloons){if(o.popped)continue;o.popped=true;o.amount=0;ticketResult.numbers[balloons.indexOf(o)]=0;o.node.classList.add('popped');o.node.style.opacity='0';const n=document.createElement('span');n.className='revealed p0';n.textContent='$0';n.style.left=(o.x*100)+'%';n.style.top=(o.y*100)+'%';front.append(n);}
 $('hits').textContent='3/3';effect(.5,.55,'OUT OF SHELLS!',false);updateLabel('Out of shells! Leftover balloons count as $0.');finishTicket();}
function finishTicket(){completed=true;setTimeout(()=>{const nums=ticketResult.numbers;/* Skill mode: your worst shot sets the prize (5,5,1 pays $1; any $0 = no prize). */const win=ticketResult.skill?Math.min(...nums):ticketResult.winning;const pay=win+bonus;
 if(pay>0){total+=pay;$('wallet').textContent='Test $'+nfmt(total);updateLabel(win>0?(ticketResult.skill?'🎯 Worst shot $'+win+': YOU WON $'+win+'!':'🎉 MATCH THREE! YOU WON $'+win+'!')+(bonus>0?' + Buck’s Secret $'+bonus+' = $'+pay:''):'🦌 No match, but Buck’s Secret pays $'+bonus+'!');playSound('win')}
 else{updateLabel(ticketResult.skill?'A $0 shot means no prize. Try another $1 ticket!':'No match this time. Try another $1 ticket!')}btn.textContent='🎟️ Buy next test ticket · $1'},570)}
"""
T = T[:s0] + new_shoot + T[s1:]
# remove the old duplicate accuracy line that preceded hitRadius? (it was part of the replaced span) -- check
assert T.count('const hitRadius') == 1
T = once(T, '<span>Hits <b id="hits">0/3</b></span>', '<span>Hits <b id="hits">0/3</b></span><span id="shellBox" style="display:none">Shells <b id="shells">—</b></span>')
T = once(T, "['lift','px']]", "['lift','px'],['bsize','%']]")
T = once(T, '<div class="field"><label for="force">', '<div class="field"><div><label for="bsize">Balloon size</label><output id="bsizeOut">100%</output></div><input id="bsize" type="range" min="70" max="130" step="5" value="100"></div>\n<div class="field"><label for="force">')
# --- testing controls: mode note + zone overlay toggle + calculator link ---
T = once(T, '<label class="field" style="display:flex;align-items:center;gap:7px"><input type="checkbox" id="sound" checked>',
  '<label class="field" style="display:flex;align-items:center;gap:7px"><input type="checkbox" id="sound" checked>')
T = re.sub(r'<p class="small">Ticket odds are currently 75% lose.*?</p>',
 '<p class="small" id="modeNote"></p><p class="small"><a href="' + CALC_URL + '" style="color:inherit;font-weight:800">⚙️ Open the calculator</a> to switch Skill mode, paint the balloon zones, set Buck’s Secret, or change the odds. Rescue Bonus, Hot Streak, Double Down and special items are not applied on this ticket yet. All money is imaginary.</p>', T, flags=re.S)
T = once(T, '.balloon img{image-rendering:pixelated}', '.balloon img{image-rendering:pixelated}#front .balloon{width:calc(22.8% * var(--bs,1))}#front .crosshair{width:calc(10.476% * var(--bs,1));height:auto}.embed body{background:transparent;min-height:0}.embed .page{min-height:0}.embed .page{width:100%;padding:0;gap:8px}.embed .gameShell{width:100%}.embed .topbar,.embed .lead,.embed .tune,.embed .page>p.small:last-child{display:none}')
T = once(T, "for(const [id,suffix] of [['speed'", "showMode();$('sound').addEventListener('change',e=>savePlay('sound',e.target.checked));\nfor(const [id,k] of PLAY_IDS)$(id).addEventListener('input',e=>savePlay(k,Number(e.target.value)));\napplyPlay();\nfor(const [id,suffix] of [['speed'")
T = once(T, "window.__luckyBuckPlaytest={getState:()=>({", "window.__luckyBuckPlaytest={skill:()=>S,calcOdds,cellFor,getState:()=>({bonus,numbers:ticketResult&&ticketResult.numbers,")
T = once(T, 'Original Lucky Buck Ticket 1.0.0 · Standalone playtest · Simulator and saved tickets unchanged', 'Original Lucky Buck Ticket 1.0.0 · Linked to the Cardboard to Cash calculator (Skill mode, odds, Buck’s Secret)')
open(f'{OUT}/ticket.html', 'w').write(T)
print('ok', len(calc), len(T))
