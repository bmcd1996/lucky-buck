"""Back-of-ticket overlay (680x1017 RGBA). Transparent over the outer border and
the top logo band, so the back shows the SAME original image underneath there
(identical pixels by construction). Below the logo: sunset backdrop + a cream
printed panel with stepped pixel corners. Also writes the flip badge crop."""
from PIL import Image
import numpy as np, sys
ART,OUT=sys.argv[1],sys.argv[2]
a=np.asarray(Image.open(f'{ART}/front_orig.png').convert('RGB')).astype(float)
H,W=a.shape[:2]
IX0,IX1,IY1=36,644,977          # inner edge of the original frame
TOP=232                          # overlay starts just under the logo
ov=np.zeros((H,W,4),np.uint8)
# backdrop: continue the painted sky downward, in 4px bands, warming toward sunset orange
start=a[TOP:TOP+8,IX0+8:IX1-8].reshape(-1,3).mean(0)
warm=np.array([226,128,96]); mid=np.array([150,62,150])
for y in range(TOP,IY1):
    t=(y-TOP)/(IY1-TOP); band=(y-TOP)//4*4/(IY1-TOP)
    c=start*(1-band)+mid*band if band<0.55 else mid*(1-(band-0.55)/0.45)+warm*((band-0.55)/0.45)
    ov[y,IX0:IX1,:3]=c.clip(0,255); ov[y,IX0:IX1,3]=255
# blend the first 16 rows into the real sky so there is no seam under the logo
for i in range(16):
    y=TOP+i; al=i/16
    ov[y,IX0:IX1,:3]=(a[y,IX0:IX1]*(1-al)+ov[y,IX0:IX1,:3]*al).clip(0,255)
# cream panel with stepped corners, dark outline, gold inner rule
PX0,PX1,PY0,PY1=56,624,246,968
DARK=(28,10,26); GOLD=(236,160,58); CREAM=(252,243,222)
def stepped(x0,y0,x1,y1,step,col):
    for y in range(y0,y1):
        k=min(y-y0,y1-1-y)
        inset=step*max(0,3-k//step) if k<3*step else 0
        ov[y,x0+inset:x1-inset,:3]=col; ov[y,x0+inset:x1-inset,3]=255
stepped(PX0,PY0,PX1,PY1,4,DARK)
stepped(PX0+4,PY0+4,PX1-4,PY1-4,4,GOLD)
stepped(PX0+10,PY0+10,PX1-10,PY1-10,4,DARK)
stepped(PX0+12,PY0+12,PX1-12,PY1-12,4,CREAM)
Image.fromarray(ov).save(f'{OUT}/back_panel.png',optimize=True)
# flip badge crop (positioned by CSS at the same native coordinates)
fb=Image.open(f'{ART}/badge_flip.png'); bb=fb.getbbox(); print('flip badge bbox',bb)
fb.crop(bb).save(f'{OUT}/flip_badge.png',optimize=True)
print('panel inner',PX0+12,PY0+12,PX1-12,PY1-12)
