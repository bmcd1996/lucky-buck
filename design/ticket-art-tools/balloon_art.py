"""Hand-built pixel-art balloons on a cell grid, several style options.
Grid 37 x 45 cells, 4 px per cell -> 148 x 180 px. The body's centre cell (18,22)
is the exact centre of the image = the game's hit/bullseye point. The marker X
is symmetric around that one cell."""
from PIL import Image, ImageDraw, ImageFont
import math, sys
OUT=sys.argv[1]; CELL=4; GW,GH=37,45; CX,CY=18,22
PAL={
 'red':   dict(dark=(98,12,30), shade=(170,26,40), base=(224,48,48), light=(252,110,90), rim=(255,160,130)),
 'blue':  dict(dark=(18,28,100), shade=(30,66,176), base=(48,112,232), light=(104,166,255), rim=(160,206,255)),
 'yellow':dict(dark=(136,76,10), shade=(208,136,18), base=(248,192,40), light=(255,228,104), rim=(255,242,168)),
}
OUTLINE=(24,12,24); WHITE=(255,255,255); SHINE2=(255,244,226); MARKER=(18,14,24)
STYLES={
 'A':dict(R=15.4, bands=4, outline=1, shine='classic', x='thick', knot='tie'),
 'B':dict(R=15.4, bands=3, outline=2, shine='big',     x='thick', knot='tie'),
 'C':dict(R=15.4, bands=4, outline=1, shine='double',  x='marker',knot='tie'),
 'D':dict(R=15.4, bands=5, outline=1, shine='classic', x='dot',   knot='round'),
}
def build(name,st):
    p=PAL[name]; R=st['R']; g=[[None]*GW for _ in range(GH)]
    inside=lambda x,y:(x-CX)**2+(y-CY)**2<=R*R
    lx,ly,lz=-0.55,-0.65,0.52; n=math.sqrt(lx*lx+ly*ly+lz*lz); lx,ly,lz=lx/n,ly/n,lz/n
    tones={3:[p['light'],p['base'],p['shade']],4:[p['light'],p['base'],p['shade'],p['dark']],5:[p['rim'],p['light'],p['base'],p['shade'],p['dark']]}[st['bands']]
    cuts={3:[0.72,0.25],4:[0.80,0.42,0.08],5:[0.93,0.78,0.42,0.08]}[st['bands']]
    for y in range(GH):
        for x in range(GW):
            if not inside(x,y): continue
            nx,ny=(x-CX)/R,(y-CY)/R; nz=math.sqrt(max(0,1-nx*nx-ny*ny)); d=nx*lx+ny*ly+nz*lz
            col=tones[-1]
            for c,t in zip(cuts,tones):
                if d>c: col=t; break
            r=math.hypot(x-CX,y-CY)
            if R-2.0<r<=R-0.6 and nx>0.3 and ny>0.3: col=p['rim']   # squeaky reflected rim
            g[y][x]=col
    body=[[c is not None for c in row] for row in g]
    # knot under the body (pinched tie or round nub)
    by=max(y for y in range(GH) if any(body[y]))
    if st['knot']=='tie':
        rows=[(0,0),(-1,1),(-2,2)]
    else:
        rows=[(-1,1),(-1,1)]
    for i,(a,b) in enumerate(rows):
        for x in range(CX+a,CX+b+1): g[by+1+i][x]=p['base'] if x<=CX else p['shade']; body[by+1+i][x]=True
    # outline around body+knot
    for w in range(st['outline']):
        add=[]
        for y in range(GH):
            for x in range(GW):
                if g[y][x] is None and any(0<=x+dx<GW and 0<=y+dy<GH and g[y+dy][x+dx] is not None for dx,dy in((1,0),(-1,0),(0,1),(0,-1))):
                    add.append((x,y))
        for x,y in add: g[y][x]=OUTLINE
    # shiny corner
    S={'classic':[(10,12),(11,12),(12,12),(9,13),(10,13),(11,13),(9,14),(10,14),(13,11),(14,11),(8,16)],
       'big':[(10,11),(11,11),(12,11),(13,11),(9,12),(10,12),(11,12),(12,12),(8,13),(9,13),(10,13),(11,13),(8,14),(9,14),(10,14),(8,15),(9,15),(14,10),(15,10)],
       'double':[(10,12),(11,12),(12,12),(9,13),(10,13),(11,13),(9,14),(10,14),(13,11),(14,11),(25,30),(26,29),(24,31)]}[st['shine']]
    for i,(x,y) in enumerate(S): g[y][x]=WHITE if i<8 else SHINE2
    centre_col=g[CY][CX]
    # marker X (always symmetric about the centre cell)
    arm=6
    for k in range(-arm,arm+1):
        for x,y in ((CX+k,CY+k),(CX+k,CY-k)): g[y][x]=MARKER
    if st['x'] in ('thick','marker','dot'):
        for k in range(1,arm):
            for sx in (1,-1):
                for sy in (1,-1):
                    g[CY+sy*k][CX+sx*(k+1)]=MARKER       # widen each arm outward, mirrored 4 ways
    if st['x']=='marker':
        for sx in (1,-1):
            for sy in (1,-1):
                g[CY+sy*arm][CX+sx*(arm+1)]=MARKER; g[CY+sy*(arm+1)][CX+sx*(arm+1)]=MARKER  # blobby marker ends
    if st['x']=='dot':
        for x,y in ((CX,CY),(CX-1,CY),(CX+1,CY),(CX,CY-1),(CX,CY+1)): g[y][x]=MARKER
        g[CY][CX]=centre_col                                                                 # centre pixel shows the balloon colour
    img=Image.new('RGBA',(GW*CELL,GH*CELL),(0,0,0,0)); px=img.load()
    for y in range(GH):
        for x in range(GW):
            if g[y][x]:
                for j in range(CELL):
                    for i in range(CELL): px[x*CELL+i,y*CELL+j]=g[y][x]+(255,)
    return img
W,H=GW*CELL,GH*CELL
sheet=Image.new('RGBA',(W*3+60,(H+40)*len(STYLES)+10),(118,58,148,255)); d=ImageDraw.Draw(sheet)
try: font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',22)
except Exception: font=None
for r,(k,st) in enumerate(STYLES.items()):
    d.text((10,r*(H+40)+8),f'Option {k}',fill=(255,240,180),font=font)
    for i,nm in enumerate(('red','blue','yellow')):
        im=build(nm,st); im.save(f'{OUT}/balloon_{k}_{nm}.png',optimize=True)
        sheet.alpha_composite(im,(20+i*(W+10),r*(H+40)+36))
sheet.save(f'{OUT}/balloon_options.png'); print(sheet.size)
