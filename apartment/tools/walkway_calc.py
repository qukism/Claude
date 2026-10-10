"""Walkway calculator for the Allston living room (units: inches).

Measures the narrowest gap between the couch (x 0-45, y 35.5-148.5) and a counter table plus
its stools (circles, radius 8), and flags collisions with the radiator, TV stand, kitchen-door
path and ottoman. Same geometry as the 3D model. Run: python3 walkway_calc.py
"""
import math
COUCH=(0,45,35.5,148.5); R=8
OBS={'radiator':(128,137,0,41.5),'stand':(122,137,55,125),'kitchen':(3,35.5,0,32.5),'ottoman':(45,73,92.5,148.5)}
def rgap(a,b):
    dx=max(0,b[0]-a[1],a[0]-b[1]); dy=max(0,b[2]-a[3],a[2]-b[3]); return math.hypot(dx,dy)
def cgap(r,c):
    px=min(max(c[0],r[0]),r[1]); py=min(max(c[1],r[2]),r[3]); return math.hypot(c[0]-px,c[1]-py)-R
def hits(rect,st):
    h=[]
    for n,o in OBS.items():
        if rect[0]<o[1]-.01 and rect[1]>o[0]+.01 and rect[2]<o[3]-.01 and rect[3]>o[2]+.01: h.append(n)
        elif any(cgap(o,c)<-.01 for c in st): h.append(n+'(stool)')
    return h
def evaluate(rect,st):
    w=min([rgap(COUCH,rect)]+[cgap(COUCH,c) for c in st]); return round(w,1),hits(rect,st)
def wall(L,D,n,tuck=False):
    x0=128-L; rect=(x0,128,0,D); d=4 if tuck else 10
    st=[(x0+L/(2*n)*(2*i+1),D+d) for i in range(n)]
    return evaluate(rect,st)
def pen(L,D,nr,nl,tuck=False):
    # short end on wall; right-side stools must clear radiator (y<49.5) and TV stand (47<y<133)
    d=4  # stools pushed in, for the second walkway figure
    best=None
    for x0 in [x/2 for x in range(90,260)]:
        x1=x0+D; rect=(x0,x1,0,L)
        st=[(x1+10,L/(2*nr)*(2*i+1)) for i in range(nr)]+[(x0-10,L/(2*nl)*(2*i+1)) for i in range(nl)] if nl else [(x1+10,L/(2*nr)*(2*i+1)) for i in range(nr)]
        if evaluate(rect,st)[1]: continue
        best=(x0,)+evaluate(rect,st)
    if not best: return None
    x0=best[0]; x1=x0+D; rect=(x0,x1,0,L)
    stt=[(x1+d,L/(2*nr)*(2*i+1)) for i in range(nr)]+([(x0-d,L/(2*nl)*(2*i+1)) for i in range(nl)] if nl else [])
    return x0, best[1], evaluate(rect,stt)[0]
print("LONG SIDE ON WALL (right end x=128), walkway in-use / pushed-in")
for L,n in [(48,2),(54,2),(60,3),(66,3),(72,3)]:
    for D in [15,16,18,20]:
        print(f" {L}x{D} seats {n}:", wall(L,D,n), wall(L,D,n,True)[0])
print("PENINSULA (short end on wall), x0, walkway in-use, pushed-in")
for L in [36,40,42,45,48,54,60]:
    for D in [16,18,20,24]:
        for nr,nl in [(2,2),(2,1),(3,2)]:
            r=pen(L,D,nr,nl)
            if r: print(f" {L}x{D} seats {nr}+{nl}={nr+nl}: x0 {r[0]} walk {r[1]} / {r[2]}")
print("PENINSULA pushed-in check")
for L,D in [(48,18),(48,20),(48,24),(42,24),(54,24)]:
    r=pen(L,D,2,2); x0=r[0]; x1=x0+D; rect=(x0,x1,0,L)
    st=[(x1+4,L/4),(x1+4,3*L/4),(x0-4,L/4),(x0-4,3*L/4)]
    end=[(x0+D/2, L+10)]
    print(f" {L}x{D}: x0 {x0} in-use {r[1]} pushed-in {evaluate(rect,st)[0]} ; 5th stool at end hits: {hits(rect,end)}")
