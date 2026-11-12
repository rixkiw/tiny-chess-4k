import json,os,urllib.request as R
U=os.environ.get("MAKEFUN_ENV_URL","http://127.0.0.1:9")
S=[i for i in range(21,99)if i%10 not in(0,9)]
N=(-21,-19,-12,-8,8,12,19,21)
BI=(-11,-9,9,11)
R4=(-10,-1,1,10)
V={"p":100,"n":320,"b":330,"r":500,"q":900,"k":0}
O={"n":N,"b":BI,"r":R4,"q":BI+R4,"k":BI+R4}
M=99999
nodes=0
budget=260000
SC=0
KL=[None]*80
def ps(q,r,c):
 ce=7-abs(c-3.5)-abs(r-3.5)
 if q=="p":return(8*(6-r)if r<7 else 70)+(8 if c in(3,4)else 0)-(10 if c in(0,7)else 0)
 if q=="n":return 12*ce
 if q=="b":return 7*ce
 if q=="r":return 4*ce+(22 if r==1 else 0)
 if q=="q":return 3*ce
 return 24 if r==7 and c in(0,1,2,6,7)else -12*ce
P={q:[ps(q,r,c)for r in range(8)for c in range(8)]for q in "pnbrqk"}
def vl(p,i):
 q=p.lower()
 r=i//10-2
 if p.isupper():return V[q]+P[q][r*8+i%10-1]
 return-(V[q]+P[q][(7-r)*8+i%10-1])
def parse(f):
 global SC
 b=["x"]*120
 for i in S:b[i]="."
 r=2;c=1
 for h in f.split()[0]:
  if h=="/":r+=1;c=1
  elif h.isdigit():c+=int(h)
  else:b[r*10+c]=h;c+=1
 SC=sum(vl(b[i],i)for i in S if b[i]!=".")
 return b,f.split()[1]=="w"
def gen(b,w,c=0):
 m=[]
 for i in S:
  p=b[i]
  if p=="."or p.isupper()!=w:continue
  q=p.lower()
  if q=="p":
   d=-10 if w else 10
   t=i+d
   if b[t]==".":
    if t<30 or t>88:m.append((i,t,"q"))
    elif not c:
     m.append((i,t,""))
     if(i<40 or i>80)and b[i+2*d]==".":m.append((i,i+2*d,""))
   for e in(d-1,d+1):
    t=i+e;v=b[t]
    if v not in("x",".")and v.isupper()!=w:m.append((i,t,"q"if t<30 or t>88 else""))
  else:
   for o in O[q]:
    t=i+o
    while b[t]!="x":
     v=b[t]
     if v==".":
      if not c:m.append((i,t,""))
     else:
      if v.isupper()!=w:m.append((i,t,""))
      break
     if q=="n"or q=="k":break
     t+=o
 return m
def mv(b,m):
 global SC
 f,t,pr=m
 c=b[t];p=b[f]
 if c!=".":SC-=vl(c,t)
 SC-=vl(p,f)
 np=(pr.upper()if p.isupper()else pr)if pr else p
 b[t]=np
 b[f]="."
 SC+=vl(np,t)
 return c
def un(b,m,c):
 global SC
 f,t,pr=m
 p=b[t]
 SC-=vl(p,t)
 p=("P"if p.isupper()else"p")if pr else p
 b[f]=p
 b[t]=c
 SC+=vl(p,f)
 if c!=".":SC+=vl(c,t)
def qs(b,w,a,e,d):
 global nodes
 nodes+=1
 s=SC if w else-SC
 if s>=e or d>4:return s
 if s>a:a=s
 for m in gen(b,w,1):
  if b[m[1]].lower()=="k":return M-d
  c=mv(b,m)
  v=-qs(b,not w,-e,-a,d+1)
  un(b,m,c)
  if v>=e:return v
  if v>a:a=v
 return a
def srch(b,w,dep,a,e,pl):
 global nodes
 nodes+=1
 if nodes>budget:raise StopIteration
 if dep<1:return qs(b,w,a,e,0)
 ms=gen(b,w)
 if not ms:return-pl-M
 ms.sort(key=lambda m:-V.get(b[m[1]].lower(),0)*9+V[b[m[0]].lower()]-(400 if m==KL[pl]else 0))
 i=0
 for m in ms:
  if b[m[1]].lower()=="k":return M-pl
  q=b[m[1]]=="."and not m[2]
  c=mv(b,m)
  if i>3 and dep>2 and q:
   v=-srch(b,not w,dep-2,-e,-a,pl+1)
   if v>a:v=-srch(b,not w,dep-1,-e,-a,pl+1)
  else:v=-srch(b,not w,dep-1,-e,-a,pl+1)
  un(b,m,c)
  i+=1
  if v>=e:
   if q:KL[pl]=m
   return v
  if v>a:a=v
 return a
def sq(s):return(10-int(s[1]))*10+"abcdefgh".index(s[0])+1
def best(f,l):
 global nodes
 nodes=0
 b,w=parse(f)
 t=l[0]
 sc=[0]*len(l)
 for dep in range(1,12):
  try:
   bs=-M*2
   u0=None
   for i in sorted(range(len(l)),key=lambda j:-sc[j]):
    u=l[i]
    m=(sq(u[0:2]),sq(u[2:4]),u[4:5])
    c=mv(b,m)
    v=-srch(b,not w,dep-1,-M*2,M*2,1)
    un(b,m,c)
    sc[i]=v
    if v>bs:bs,u0=v,u
   t=u0
  except StopIteration:break
 return t
def post(p,d):
 return json.load(R.urlopen(R.Request(U+p,json.dumps(d).encode(),{"content-type":"application/json"})))
g=post("/game",{})
while g["status"]!="done":
 while g["status"]=="your_move":
  nodes=0
  g=post("/move",{"game":g["game"],"move":best(g["fen"],g["legal_moves"])})
 g=post("/game",{})
