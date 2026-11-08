"""Apply the approved-for-preview visual changes to a Lucky Buck ticket HTML file.
Artwork/layout only: no changes to odds, shooting, balloons or sounds."""
import re,base64,sys
path,assets=sys.argv[1],sys.argv[2]
t=open(path).read()
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
PANEL=b64(f'{assets}/back_panel.png'); FLIP=b64(f'{assets}/flip_badge.png')
def sub1(pat,rep,s,flags=re.S):
    n=re.subn(pat,lambda m:rep,s,count=1,flags=flags)
    assert n[1]==1,pat; return n[0]
# fonts
t=sub1(r'<link href="https://fonts.googleapis.com/css2\?family=Handjet[^"]*" rel="stylesheet">',
 '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Annie+Use+Your+Telescope&family=Lilita+One&family=Roboto+Condensed:wght@700&display=swap" rel="stylesheet">',t)
# replace old reverse CSS (mini-update 1.1 + visual polish) with the new reverse styles
NEWCSS=r'''/* Lucky Buck ticket art restore: original front art untouched; the back reuses the
   SAME image (so the outer frame and logo are identical pixels) under a printed panel. */
.ticket{container-type:inline-size}
.ticket .back{border:0;background:#3b1e54;box-shadow:none;padding:0;transform:none;display:none}
.ticket.flipped .back{display:block}
.back .base,.back .panelArt{position:absolute;inset:0;width:100%;height:100%;object-fit:fill;pointer-events:none}
.flipBadge{position:absolute;left:79.118%;top:2.655%;width:15.588%;height:7.571%;pointer-events:none;z-index:25;image-rendering:auto}
.ticket .flipHotspot,.ticket .back button.flipHotspot{position:absolute;left:76%;right:auto;top:1.2%;width:22.5%;height:11%;z-index:30;margin:0;padding:0;border:0;border-radius:0;background:transparent;box-shadow:none;clip-path:none;color:transparent;font-size:0;cursor:pointer;touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.ticket .flipHotspot:focus-visible{outline:3px solid #fff3b0;outline-offset:-4px}
.back .rules{position:absolute;left:10.000%;top:25.369%;width:80.000%;height:68.633%;padding:3cqw 4cqw 2.6cqw;display:flex;flex-direction:column;color:#1d1018;text-align:left;z-index:2}
.back .rules .price{display:flex;align-items:center;justify-content:center;gap:2cqw;font-family:'Lilita One','Arial Black',Impact,sans-serif;font-size:5.6cqw;line-height:1.05;color:#4a1d6e;letter-spacing:.015em;text-align:center}
.back .rules .price b{font-weight:400;background:#1c0a1a;color:#fff;font-size:7.4cqw;line-height:1;padding:.7cqw 2.2cqw .9cqw;border-radius:2cqw}
.back .rules ol{list-style:none;margin:3cqw 0 0;padding:0;display:flex;flex-direction:column;gap:2.2cqw}
.back .rules li{display:grid;grid-template-columns:8.6cqw 1fr;column-gap:2.8cqw;align-items:start}
.back .rules .num{box-sizing:border-box;width:8.6cqw;height:8.6cqw;border-radius:50%;background:#ec9a33;border:.7cqw solid #1c0a1a;color:#1c0a1a;font-family:'Lilita One','Arial Black',sans-serif;font-size:5.4cqw;line-height:1;display:grid;place-items:center}
.back .rules h3{margin:.3cqw 0 0;font-family:'Lilita One','Arial Black',Impact,sans-serif;font-weight:400;font-size:5.3cqw;line-height:1;letter-spacing:.03em;color:#1c0a1a}
.back .rules li p{margin:.8cqw 0 0;font-family:'Roboto Condensed','Arial Narrow','Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:4.6cqw;line-height:1.16;color:#1d1018}
.back .rules .secret{margin-top:auto;padding-top:2cqw;padding:0 1cqw .4cqw;color:#c4232b;font-family:'Annie Use Your Telescope','Bradley Hand','Segoe Print','Comic Sans MS',cursive;transform:rotate(-2deg);transform-origin:left center}
.back .rules .secret .t{font-size:6.6cqw;line-height:1;text-decoration:underline;text-decoration-thickness:.3cqw;text-underline-offset:1cqw}
.back .rules .secret p{margin:1.2cqw 0 0;font-family:inherit;font-size:5.7cqw;line-height:1.08;color:inherit;-webkit-text-stroke:.08cqw #c4232b}
</style>'''
t=sub1(r'/\* Mini-update 1\.1:.*?</style>',NEWCSS,t)
# front: baked-look flip badge image + invisible tap target
t=sub1(r'<button id="flip" class="flipHotspot" type="button" aria-label="Flip ticket to read instructions">.*?</button>',
 f'<img class="flipBadge" alt="" draggable="false" src="data:image/png;base64,{FLIP}">\n    <button id="flip" class="flipHotspot" type="button" aria-label="Flip ticket to read instructions"></button>',t)
# back face
BACK=f'''<div class="face back" aria-label="Ticket rules on the reverse">
    <img class="base" id="backBase" alt="" draggable="false">
    <img class="panelArt" alt="" draggable="false" src="data:image/png;base64,{PANEL}">
    <img class="flipBadge" alt="" draggable="false" src="data:image/png;base64,{FLIP}">
    <div class="rules">
     <div class="price"><b>$1</b><span>MATCH 3 AMOUNTS<br>TO WIN!</span></div>
     <ol>
      <li><span class="num">1</span><div><h3>SHOOT</h3><p>Hold to aim at the moving balloons. Release to fire.</p></div></li>
      <li><span class="num">2</span><div><h3>REVEAL</h3><p>Pop all three balloons to show the amounts.</p></div></li>
      <li><span class="num">3</span><div><h3>WIN</h3><p>Match all three amounts to win that prize.</p></div></li>
     </ol>
     <div class="secret" aria-label="Buck’s Secret, handwritten on the ticket"><div class="t">Buck’s Secret</div><p>Word around the woods is hittin’ a perfect bullseye can earn ya an extra buck or two...</p></div>
    </div>
    <button id="flipBack" class="flipHotspot" type="button" aria-label="Flip ticket to game side"></button>
   </div>'''
t=sub1(r'<div class="face back".*?<button id="flipBack"[^>]*>.*?</button>\s*</div>',BACK,t)
# JS: drop the runtime sky/logo "polish"; show the same original image on the back
t=sub1(r'/\* Preserve the real logo while clearing.*?else originalArtForPolish\.addEventListener\(\'load\',polishLuckyBuckArtwork,\{once:true\}\);\n\}\n',
 "/* The back shows the very same original artwork image as the front (frame + logo). */\n{const bb=document.getElementById('backBase'),fb=front.querySelector('img.base');if(bb&&fb)bb.src=fb.getAttribute('src');}\n",t)
open(path,'w').write(t); print('patched',path,len(t))
