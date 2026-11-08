# Hand-drawn pixel arrow (clockwise "turn over" arrow) on a cell grid.
RING=[
"....####....",
"..########..",
".####..####.",
"####....####",
"###......###",
"###......###",
"###......###",
"###......###",
"####....####",
".####..####.",
"..########..",
"....####....",
]
def arrow():
    w=12; g=[[0]*w for _ in range(14)]
    for y,row in enumerate(RING):
        for x,ch in enumerate(row):
            if ch=='#': g[y+2][x]=1
    # open the upper-right of the ring
    for y in range(0,8):
        for x in range(6,w):
            g[y][x]=0
    # arrowhead at the end of the top band, pointing right/down along the ring
    head={6:range(0,8),7:range(1,7),8:range(2,6),9:range(3,5)}
    for x,ys in head.items():
        for y in ys: g[y][x]=1
    return g
if __name__=='__main__':
    for r in arrow(): print(''.join('#' if v else '.' for v in r))
