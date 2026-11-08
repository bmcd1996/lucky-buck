"""Build the flip-arrow badge as a mirror of the original $1 badge shell.
Deterministic: reads front_orig.png, writes badge_flip.png (RGBA, placed at its
top-right position on a 680x1017 transparent canvas) and badge_dollar.png."""
from PIL import Image, ImageDraw
import numpy as np, math, sys
ART=sys.argv[1]
src=Image.open(f'{ART}/front_orig.png').convert('RGB'); a=np.asarray(src).astype(int)
W,H=src.size
FILL=np.array([27,8,18]); WHITE=np.array([252,250,252])
X0,X1,Y0,Y1=34,142,24,104           # search box around the $1 badge
s=a.sum(2)
mask=np.zeros((H,W),bool)
box=np.zeros((H,W),bool); box[Y0:Y1,X0:X1]=True
dark=(s<170)&box
glyph=(s>330)&box; glyph[:, :54]=False; glyph[:, 122:]=False; glyph[:36]=False; glyph[90:]=False
# badge = dark region + glyph, flood-filled from badge centre
from collections import deque
cand=dark|glyph
seen=np.zeros_like(cand); q=deque([(60,90)]); seen[60,90]=True
while q:
    y,x=q.popleft()
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
        yy,xx=y+dy,x+dx
        if box[yy,xx] and cand[yy,xx] and not seen[yy,xx]:
            seen[yy,xx]=True; q.append((yy,xx))
mask=seen
# fill interior holes (anti-aliased glyph pixels between the dark/white thresholds)
inv=~mask; lab=np.zeros_like(mask); q=deque()
for yy in range(Y0,Y1):
    for xx in (X0,X1-1):
        if inv[yy,xx]: lab[yy,xx]=True; q.append((yy,xx))
for xx in range(X0,X1):
    for yy in (Y0,Y1-1):
        if inv[yy,xx] and not lab[yy,xx]: lab[yy,xx]=True; q.append((yy,xx))
while q:
    y,x=q.popleft()
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
        yy,xx=y+dy,x+dx
        if Y0<=yy<Y1 and X0<=xx<X1 and inv[yy,xx] and not lab[yy,xx]:
            lab[yy,xx]=True; q.append((yy,xx))
mask=box&~lab
mask[:27,:]=False                     # top dark line belongs to the border
mask[:, :36]=False                    # left of inner edge belongs to the border
ys,xs=np.nonzero(mask)
print('badge mask bbox x',xs.min(),xs.max(),'y',ys.min(),ys.max(),'px',mask.sum())
# $1 badge alone (for reference/measurement)
d=np.zeros((H,W,4),np.uint8); d[mask,:3]=a[mask]; d[mask,3]=255
Image.fromarray(d).save(f'{ART}/badge_dollar.png')
# empty shell: fill everything inside the badge that is not its soft outer edge
shell=a.copy()
inner=mask.copy()
gl=np.zeros_like(mask); gl[34:92,52:124]=True
shell[gl&mask]=FILL
# erode the mask 3px: everything that is not the badge's soft outer rim becomes clean fill
from PIL import ImageFilter
er=np.asarray(Image.fromarray((mask*255).astype(np.uint8)).filter(ImageFilter.MinFilter(7)))>0
shell[er]=FILL
# mirror about the ticket's vertical centre line
mx=np.zeros((H,W,4),np.uint8)
for y,x in zip(ys,xs):
    nx=W-1-x
    mx[y,nx,:3]=shell[y,x]; mx[y,nx,3]=255
# arrow glyph: mirrored glyph box centre
gys,gxs=np.nonzero(glyph&mask)
cx=W-1-(gxs.min()+gxs.max())/2; cy=(gys.min()+gys.max())/2
gh=gys.max()-gys.min()+1
print('glyph box h',gh,'w',gxs.max()-gxs.min()+1,'centre',cx,cy)
sys.path.insert(0,__file__.rsplit('/',1)[0]); from arrow_cells import arrow
cells=arrow(); CELL=4
gw,gh2=len(cells[0])*CELL,len(cells)*CELL
ox=int(round(cx-gw/2)); oy=int(round(cy-gh2/2))
hard=np.zeros((H,W))
for j,row in enumerate(cells):
    for i,v in enumerate(row):
        if v: hard[oy+j*CELL:oy+(j+1)*CELL, ox+i*CELL:ox+(i+1)*CELL]=1
soft=np.asarray(Image.fromarray((hard*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.45))).astype(float)/255
amask=mx[...,3]>0
for c in range(3):
    ch=mx[...,c].astype(float)
    ch=np.where(amask, ch*(1-soft)+WHITE[c]*soft, ch)
    mx[...,c]=ch.clip(0,255).astype(np.uint8)
Image.fromarray(mx).save(f'{ART}/badge_flip.png')
ays,axs=np.nonzero(hard>0); print('arrow bbox w',axs.max()-axs.min()+1,'h',ays.max()-ays.min()+1)
