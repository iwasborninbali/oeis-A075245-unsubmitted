"""Direct bounded x,y search, independent of divisor search; OpenAI Codex, 2026-11-13."""
def maximum(n):
    best=0; winners=[]
    for x in range(n//4+1,(3*n-1)//4+1):
        a,b=4*x-n,n*x
        for y in range(max(x+1,b//a+1),(2*b-1)//a+1):
            d=a*y-b
            if (b*y)%d: continue
            z=b*y//d
            if z<=y: continue
            if z>best: best=z; winners=[]
            if z==best: winners.append((x,y,z))
    return winners
for n in (17,73,409):
    print(n,maximum(n))
assert maximum(409)==[(105,3906,7987770)]
assert maximum(73)==[(20,210,30660),(21,140,30660)]
print('PASS')
