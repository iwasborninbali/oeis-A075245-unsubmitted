"""Divisor-based exhaustive maximization, OpenAI Codex, 2026-11-13."""
import signal
signal.alarm(500)
from math import isqrt

def divisors_square(v):
    fs=[]
    p=2
    while p*p<=v:
        if v%p==0:
            e=0
            while v%p==0:
                e+=1; v//=p
            fs.append((p,2*e))
        p += 1 if p==2 else 2
    if v>1: fs.append((v,2))
    ds=[1]
    for p,e in fs:
        old=ds[:]; q=1
        for _ in range(e):
            q*=p
            ds.extend(d*q for d in old)
    return sorted(ds)

def maximum(n):
    best=0; wins=[]
    for x in range(n//4+1,(3*n-1)//4+1):
        a,b=4*x-n,n*x
        if b*(b+1)<best*a: continue
        for d in divisors_square(b):
            if d>=b: break
            if (b+d)%a: continue
            y=(b+d)//a
            if y<=x: continue
            if (b*y)%d: continue
            z=b*y//d
            if z<=y: continue
            if z>best: best=z; wins=[]
            if z==best: wins.append((x,y,z))
            break
    return wins

bad=[]
for n in range(3,2001):
    wins=maximum(n)
    if not wins:
        raise ValueError(('no solution',n))
    x=min(w[0] for w in wins)
    if x not in ({n//4+1,n//4+2} if n%8==1 else {n//4+1}):
        bad.append((n,x))
print('range: 3..2000')
print('formula failures:',bad)
print('409 winners:',maximum(409))
print('73 winners:',maximum(73))
