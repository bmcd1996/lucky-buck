/* Lucky Buck shared skill settings (used by calculator AND ticket). One grid applies to all three balloons. */
const LB_SKILL_KEY='lucky-buck-skill-v1',LB_CALC_KEY='quill-lucky-buck-v2';
const LB_GW=37,LB_GH=45,LB_CX=18,LB_CY=22;
const LB_MASK='__MASK__';
const LB_ZONES=['G','N','Y','R'];
const LB_ZONE_INFO={G:{name:'Gold',col:'#f5b81c'},N:{name:'Green',col:'#35c759'},Y:{name:'Yellow',col:'#fff06a'},R:{name:'Red',col:'#ef3b3b'}};
function lbRingGrid(g,n,y){let s='';for(let j=0;j<LB_GH;j++)for(let i=0;i<LB_GW;i++){if(LB_MASK[j*LB_GW+i]==='.'){s+='.';continue}const d=Math.hypot(i-LB_CX,j-LB_CY);s+=d<=g?'G':d<=n?'N':d<=y?'Y':'R'}return s}
/* Gold = Buck's Secret spot. Default: the single dead-centre pixel. */
/* Play settings shared by the calculator sliders and the ticket. */
const LB_PLAY_DEFAULTS={speed:1.6,movement:100,wobble:20,lift:130,size:100,sound:true};
const LB_PLAY_RANGES={speed:[0.3,2.2],movement:[30,120],wobble:[0,40],lift:[0,220],size:[70,130]};
function lbCleanPlay(p){p=p||{};const o={};for(const k in LB_PLAY_RANGES){const x=Number(p[k]),[lo,hi]=LB_PLAY_RANGES[k];o[k]=Number.isFinite(x)?Math.min(hi,Math.max(lo,x)):LB_PLAY_DEFAULTS[k];}o.sound=p.sound!==false;return o}
function lbSkillDefaults(){return {version:2,skillOn:false,rings:{gold:0,green:6.5,yellow:11.5},grid:lbRingGrid(0,6.5,11.5),values:{G:25,N:5,Y:1,R:0},shells:5,play:{...LB_PLAY_DEFAULTS},secret:{on:true,amount:1,max:2}}}
function lbLoadSkill(){const d=lbSkillDefaults();try{const v=JSON.parse(localStorage.getItem(LB_SKILL_KEY)||'null');if(!v||typeof v!=='object'||v.version!==2)return d;
 let grid=d.grid;if(typeof v.grid==='string'&&v.grid.length===LB_GW*LB_GH){grid='';for(let k=0;k<v.grid.length;k++){const m=LB_MASK[k]==='.',c=v.grid[k];grid+=m?'.':(LB_ZONES.includes(c)?c:'R')}}
 const num=(x,f,lo,hi)=>{x=Number(x);return Number.isFinite(x)?Math.min(hi,Math.max(lo,x)):f};
 const values={};for(const z of LB_ZONES)values[z]=num(v.values?.[z],d.values[z],0,100000);
 const s=v.secret||{};
 return {version:2,skillOn:v.skillOn===true,rings:{gold:num(v.rings?.gold,0,0,20),green:num(v.rings?.green,6.5,0,25),yellow:num(v.rings?.yellow,11.5,0,25)},grid,values,play:lbCleanPlay(v.play),shells:Math.round(num(v.shells,5,1,20)),
  secret:{on:s.on!==false,amount:num(s.amount,1,0,1000),max:num(s.max,2,0,10000)}};
 }catch(e){return d}}
function lbSaveSkill(v){try{localStorage.setItem(LB_SKILL_KEY,JSON.stringify(v));return true}catch(e){return false}}
function lbIsGold(S,c){return c.cx>=0&&c.cx<LB_GW&&c.cy>=0&&c.cy<LB_GH&&S.grid[c.cy*LB_GW+c.cx]==='G'}
