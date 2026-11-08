"""Pixel-art crosshairs on the SAME cell grid as the balloons (4 px per cell at
native art scale). 17 x 17 cells, so cell (8,8) is the single exact centre."""
from PIL import Image, ImageDraw, ImageFont
import math, sys
OUT=sys.argv[1]; CELL=4; N=17; C=8
O=(16,10,20)          # dark outline
def blank(): return [[None]*N for _ in range(N)]
def outline(g):
    add=[]
    for y in range(N):
        for x in range(N):
            if g[y][x] is None and any(0<=x+dx<N and 0<=y+dy<N and g[y+dy][x+dx] not in (None,O) for dx,dy in((1,0),(-1,0),(0,1),(0,-1))):
                add.append((x,y))
    for x,y in add: g[y][x]=O
    return g
def ring(g,r0,r1,col,skip=lambda x,y:False):
    for y in range(N):
        for x in range(N):
            d=math.hypot(x-C,y-C)
            if r0<=d<=r1 and not skip(x,y): g[y][x]=col
def designs():
    D={}
    # 1 Classic red scope: ring, four ticks with a gap, single red centre pixel
    g=blank(); R=(236,40,48); W=(255,255,255)
    ring(g,6.5,7.4,R,skip=lambda x,y:abs(x-C)<=0 or abs(y-C)<=0)
    for k in range(3,8):
        for x,y in((C,C-k),(C,C+k),(C-k,C),(C+k,C)): g[y][x]=R
    g[C][C]=W; D['1  Red scope']=outline(g)
    # 2 Hunter orange: chunky plus with a gap and blaze-orange centre pixel
    g=blank(); Q=(255,122,24); Y=(255,214,90)
    for k in range(2,8):
        for x,y in((C,C-k),(C,C+k),(C-k,C),(C+k,C)): g[y][x]=Q if k>2 else Y
    g[C][C]=Q; D['2  Hunter orange']=outline(g)
    # 3 Buck sight: four inward chevrons (antler-tip arrows) + gold centre pixel
    g=blank(); G=(255,206,64)
    for s in range(4):
        for k in range(0,3):
            pts=[(C-k,C-5+k),(C+k,C-5+k)] if s==0 else [(C-k,C+5-k),(C+k,C+5-k)] if s==1 else [(C-5+k,C-k),(C-5+k,C+k)] if s==2 else [(C+5-k,C-k),(C+5-k,C+k)]
            for x,y in pts: g[y][x]=G
    g[C][C]=G; D['3  Buck sight']=outline(g)
    # 4 Bullseye target: red/white rings with dark edges, see-through middle, red centre pixel
    g=blank()
    ring(g,7.5,8.3,O); ring(g,6.6,7.5,(236,40,48)); ring(g,5.6,6.6,(255,255,255)); ring(g,4.9,5.6,O)
    for x,y in((C,C-1),(C,C+1),(C-1,C),(C+1,C),(C-1,C-1),(C+1,C+1),(C-1,C+1),(C+1,C-1)): g[y][x]=O
    g[C][C]=(236,40,48); D['4  Bullseye']=g
    # 5 Neon green sniper: thin long plus to the edges, corner brackets, centre pixel
    g=blank(); L=(110,255,120)
    for k in range(2,9):
        for x,y in((C,C-k),(C,C+k),(C-k,C),(C+k,C)):
            if 0<=x<N and 0<=y<N: g[y][x]=L
    for sx in(-1,1):
        for sy in(-1,1):
            for x,y in((C+sx*5,C+sy*5),(C+sx*4,C+sy*5),(C+sx*5,C+sy*4)): g[y][x]=L
    g[C][C]=(255,255,255); D['5  Neon sniper']=outline(g)
    # 6 Lucky clover: four leaf-shaped dots around a single centre pixel
    g=blank(); K=(70,210,90); KL=(150,255,150)
    for dx,dy in((0,-1),(0,1),(-1,0),(1,0)):
        cx,cy=C+dx*4,C+dy*4
        for y in range(N):
            for x in range(N):
                if math.hypot(x-cx,y-cy)<=1.6: g[y][x]=K
        g[cy-1 if dy<=0 else cy][cx-1 if dx<=0 else cx]=KL
    g[C][C]=(255,255,255); D['6  Lucky clover']=outline(g)
    # 7 Hunter red (owner pick: Hunter orange shape, in red)
    g=blank(); Q=(232,34,44); Y=(255,128,116)
    for k in range(2,8):
        for x,y in((C,C-k),(C,C+k),(C-k,C),(C+k,C)): g[y][x]=Q if k>2 else Y
    g[C][C]=Q; D['7  Hunter red']=outline(g)
    return D
def render(g):
    im=Image.new('RGBA',(N*CELL,N*CELL),(0,0,0,0)); px=im.load()
    for y in range(N):
        for x in range(N):
            if g[y][x]:
                for j in range(CELL):
                    for i in range(CELL): px[x*CELL+i,y*CELL+j]=g[y][x]+(255,)
    return im
D=designs()
bal=Image.open(f'{OUT}/balloon_D_blue.png')   # 148x180, centre cell spans 72-76 x 88-92
cw=N*CELL; tile_w,tile_h=bal.width+cw+40,bal.height+40
sheet=Image.new('RGBA',(tile_w*2+20,(tile_h+30)*4+10),(118,58,148,255)); d=ImageDraw.Draw(sheet)
try: font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf',16)
except Exception: font=None
for i,(name,g) in enumerate(D.items()):
    im=render(g); im.save(f'{OUT}/crosshair_{i+1}.png',optimize=True)
    col,row=i%2,i//2; ox,oy=10+col*(tile_w+10),10+row*(tile_h+30)
    d.text((ox,oy),name,fill=(255,240,180),font=font)
    # crosshair alone
    sheet.alpha_composite(im,(ox,oy+30+(bal.height-cw)//2))
    # crosshair centred on the balloon's centre cell
    bx,by=ox+cw+20,oy+30
    sheet.alpha_composite(bal,(bx,by))
    sheet.alpha_composite(im,(bx+74-cw//2,by+90-cw//2))
sheet.resize((sheet.width*2,sheet.height*2),Image.NEAREST).save(f'{OUT}/crosshair_options.png'); print(sheet.size, 'crosshair', cw,'px; centre cell', C*CELL,(C+1)*CELL)
