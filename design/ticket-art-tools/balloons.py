"""Remove leftover sunset background baked around each balloon image.
The balloon is enclosed by its own dark outline; everything reachable from the
transparent area without crossing that outline is leftover background."""
from PIL import Image
import numpy as np, sys
from collections import deque
from scipy import ndimage
src,dst,T=sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 150
a=np.asarray(Image.open(src).convert('RGBA')).copy()
H,W=a.shape[:2]; rgb=a[...,:3].astype(int); s=rgb.sum(2); al=a[...,3]
wall=(s<T)&(al>0)
def flood(seed):
    m=np.zeros((H,W),bool); q=deque([seed]); m[seed]=True
    while q:
        y,x=q.popleft()
        for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
            yy,xx=y+dy,x+dx
            if 0<=yy<H and 0<=xx<W and not m[yy,xx] and al[yy,xx]>0 and not wall[yy,xx]:
                m[yy,xx]=True; q.append((yy,xx))
    return m
ys,xs=np.nonzero(al>0); cx=int((xs.min()+xs.max())/2)
# body: flood from the upper-middle of the balloon (left of the ? glyph)
body=flood((int(H*0.45),int(W*0.25)))
# knot: the small enclosed blob just under the body, centred horizontally
by=np.nonzero(body.any(1))[0].max()
knot=np.zeros((H,W),bool)
for y in range(by+1,min(H,by+30)):
    if al[y,cx]>0 and not wall[y,cx] and not body[y,cx]:
        k=flood((y,cx))
        if k.sum()<1500: knot|=k; break
core=body|knot
dist=ndimage.distance_transform_edt(~core)
keep=ndimage.binary_fill_holes(core|(wall&(dist<=6)))
print('body',int(body.sum()),'knot',int(knot.sum()))
a[...,3]=np.where(keep,255,0).astype(np.uint8)
Image.fromarray(a).save(dst,optimize=True)
print(src,'removed px',int(((al>0)&~keep).sum()))
