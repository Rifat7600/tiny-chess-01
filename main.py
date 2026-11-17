import json,os,urllib.request as j
g=os.environ["MAKEFUN_ENV_URL"]
P,N,B,R,Q,K=1,2,3,4,5,6
V=(0,100,320,330,500,900,0)
S=100000;Z=1000000;I=128;O=6400;U=25000
ns=(14,18,31,33,-14,-18,-31,-33)
ks=(1,-1,15,16,17,-15,-16,-17)
bd=(15,17,-15,-17)
rd=(1,-1,16,-16)
Mt=[0,0,ns,bd,rd,bd+rd,ks]
T=["KKKKUUUUMMOQLLMPKKKOLJIKLMMGKKKK","ACEECGKKEKMNELNOEKNOELMNCGKLACEE","GIIIIKKKIKLMILLMIKMMIMMMILKKGIII","KKKKLMMMJKKKJKKKJKKKJKKKJKKKKKKL","GIIJIKKKIKLLJKLLKKLLILLLIKLKGIIJ","ECCAECCAECCAECCAGEECIGGGOOKKOQMK","ACEGEGIKEIOQEIQSEIQSEIOQEEKKAEEE"]
T=["".join(s[x*4+min(y,7-y)]for x in range(8)for y in range(8))for s in T]
b=[0]*128;t=c=f=0;e=-1;Y=[4,116];u=[];h={}
n=o=0
D={}
F=set()
def su():
 global t,c,e,f
 b[:]=[0]*128
 for i,g in enumerate((R,N,B,Q,K,B,N,R)):b[i]=g;b[i+112]=-g;b[i+16]=P;b[i+96]=-P
 t=0;c=15;e=-1;f=0;Y[0]=4;Y[1]=116;h.clear();h[(tuple(b),t,c,e)]=1
def at(q,w):
 for d in(-15,-17)if w else(15,17):
  a=q+d
  if not(a&0x88)and b[a]==(P if w else-P):return 1
 for s2,p2 in((ns,N),(ks,K)):
  for d in s2:
   a=q+d
   if not(a&0x88)and b[a]==(p2 if w else-p2):return 1
 for ds,ps in((bd,(B,Q)),(rd,(R,Q))):
  for d in ds:
   a=q+d
   while not(a&0x88):
    p=b[a]
    if p:
     if(p>0)==w and abs(p)in ps:return 1
     break
    a+=d
 return 0
def mk(v):
 global t,c,e,f
 u.append((b[:],t,c,e,f,Y[:]))
 a=v&127;d=(v>>7)&127;p=(v>>14)&7
 pc=b[a];cap=b[d]!=0 or v&(1<<18)
 b[a]=0
 if v&(1<<18):b[d-16 if t==0 else d+16]=0
 if v&(1<<19):
  rf,rt=(d+1,d-1)if d in(6,118)else(d-2,d+1)
  b[rt]=b[rf];b[rf]=0
 b[d]=(p if pc>0 else-p)if p else pc
 if abs(pc)==K:Y[t]=d
 nc=c
 for sq,ms in((4,3),(0,2),(7,1),(116,12),(112,8),(119,4)):
  if a==sq or d==sq:nc&=~ms
 c=nc;e=-1
 if v&(1<<20):e=(a+d)//2
 f=0 if abs(pc)==P or cap else f+1
 t^=1
def um():
 global t,c,e,f
 b[:],t,c,e,f,Y[:]=u.pop()
def gm(co=False):
 vs=[];us=1 if t==0 else-1
 for a in range(128):
  if a&0x88:continue
  pc=b[a]
  if pc*us<=0:continue
  q=abs(pc)
  if q==P:
   d=16 if t==0 else-16
   for dd in(d,d-1,d+1):
    to=a+dd
    if to&0x88:continue
    if dd==d:
     if b[to]:continue
    elif b[to]*us>=0 and not(to==e and e!=-1):continue
    if(to>>4)==(7 if t==0 else 0):
     for p in(Q,R,B,N):vs.append(a|(to<<7)|(p<<14)|((1<<18)if to==e and dd!=d else 0))
    elif dd!=d or not co:
     vs.append(a|(to<<7)|((1<<18)if to==e and dd!=d else 0))
     if dd==d and(a>>4)==(1 if t==0 else 6)and b[a+2*d]==0:vs.append(a|((a+2*d)<<7)|(1<<20))
  else:
   for d in Mt[q]:
    to=a+d
    while not(to&0x88):
     x=b[to]
     if x:
      if x*us<0:vs.append(a|(to<<7))
      break
     if not co:vs.append(a|(to<<7))
     if q in(2,6):break
     to+=d
 if not co:
  for ks2,ds,bit in((4,1,1),(4,-1,2),(116,1,4),(116,-1,8)):
   if c&bit and b[ks2+ds]==0 and b[ks2+2*ds]==0 and(ds>0 or b[ks2-3]==0)and not at(ks2,t==1)and not at(ks2+ds,t==1)and not at(ks2+2*ds,t==1):vs.append(ks2|((ks2+2*ds)<<7)|(1<<19))
 return vs
def om(vs,tm):
 sc=[]
 for v in vs:
  s=0
  if v==tm:s=1000000
  else:
   d=(v>>7)&127
   cap=P if v&(1<<18)else abs(b[d])
   if cap:
    s=100000+10*V[cap]-V[abs(b[v&127])]
    if(v>>14)&7:s+=200000+V[(v>>14)&7]
   elif(v>>14)&7:s=90000+V[(v>>14)&7]
  sc.append((-s,v))
 sc.sort()
 return[v for _,v in sc]
def ev():
 s=0;ph=0
 for q,p in enumerate(b):
  if p and not(q&0x88):
   a=abs(p)
   if a!=K:
    if a!=P:ph+=V[a]
    if p>0:s+=V[a]+(ord(T[a-1][(7-(q>>4))*8+(q&7)])-75)*5
    else:s-=V[a]+(ord(T[a-1][(q>>4)*8+(q&7)])-75)*5
 if ph>O:ph=O
 re=O-ph
 a=(7-(Y[0]>>4))*8+(Y[0]&7);d=(Y[1]>>4)*8+(Y[1]&7)
 s+=((ord(T[5][a])-75)*ph+(ord(T[6][a])-75)*re-(ord(T[5][d])-75)*ph-(ord(T[6][d])-75)*re)*5//O
 return s if t==0 else-s
def qs(al,be,pl):
 global n,o
 n+=1
 if n>=U:o=1;return 0
 if pl>=I:return ev()
 ch=at(Y[t],t==1)
 if not ch:
  st=ev()
  if st>=be:return st
  if st>al:al=st
  bs=st
 else:bs=-S-1
 vs=om(gm(not ch),0)
 lg=0
 for v in vs:
  if not ch:
   d=(v>>7)&127;cp=P if v&(1<<18)else abs(b[d]);pr=(v>>14)&7
   if bs+V[cp]+(V[pr]if pr else 0)+200<al:continue
  mk(v)
  if at(Y[t^1],t==0):um();continue
  lg+=1;sc=-qs(-be,-al,pl+1);um()
  if o:return 0
  if sc>bs:bs=sc
  if sc>=be:return sc
  if sc>al:al=sc
 if ch and lg==0:return-S+pl
 return bs
def nm(de,al,be,pl):
 global n,o
 k=(tuple(b),t,c,e)
 if pl>0 and(f>=100 or k in h or k in F):return 0
 if de<=0 or pl>=I:return qs(al,be,pl)
 n+=1
 if n>=U:o=1;return 0
 ch=at(Y[t],t==1);tm=0;x=D.get(k)
 if x:
  tm=x[3]
  if x[0]>=de:
   s=x[2]
   if s>99000:s-=pl
   elif s<-99000:s+=pl
   if x[1]==1:return s
   if x[1]==2 and s>=be:return s
   if x[1]==3 and s<=al:return s
 a0=al;vs=om(gm(),tm);bs=-S-1;bm=0;lg=0;F.add(k)
 for v in vs:
  mk(v)
  if at(Y[t^1],t==0):um();continue
  lg+=1;sc=-nm(de-1,-be,-al,pl+1);um()
  if o:F.discard(k);return 0
  if sc>bs:bs=sc;bm=v
  if sc>al:al=sc
  if al>=be:break
 F.discard(k)
 if lg==0:return-S+pl if ch else 0
 s=bs
 if s>99000:s+=pl
 elif s<-99000:s-=pl
 if len(D)<200000:D[k]=(de,3 if bs<=a0 else 2 if bs>=be else 1,s,bm)
 return bs
def rs(de,al,be):
 k=(tuple(b),t,c,e);x=D.get(k);vs=om(gm(),x[3]if x else 0)
 bs=-S-1;bm=0;lg=0
 for v in vs:
  mk(v)
  if at(Y[t^1],t==0):um();continue
  lg+=1;sc=-nm(de-1,-be,-al,1);um()
  if o:return(bs,bm,0)
  if sc>bs:bs=sc;bm=v
  if sc>al:al=sc
 if lg==0:return(0,0,1)
 return(bs,bm,1)
def th():
 global n,o
 vs=[]
 for v in gm():
  mk(v)
  if not at(Y[t^1],t==0):vs.append(v)
  um()
 if not vs:return 0
 if len(vs)==1:return vs[0]
 n=0;o=0;bm=vs[0];de=1
 while de<=64:
  s,v,dn=rs(de,-Z,Z)
  if not dn:break
  bm=v
  if s>99000 or s<-99000:break
  if n>U//4:break
  de+=1
 return bm
def mu(v):
 s=chr(97+(v&7))+str(((v&127)>>4)+1)+chr(97+(((v>>7)&127)&7))+str((((v>>7)&127)>>4)+1);pr=(v>>14)&7
 if pr:s+="nbrq"[pr-2]
 return s
def ut(z):
 a=(ord(z[0])-97)+(int(z[1])-1)*16;d=(ord(z[2])-97)+(int(z[3])-1)*16;pr=0
 if len(z)==5:pr="nbrq".index(z[4])+2
 pc=b[a];v=a|(d<<7)|(pr<<14)
 if abs(pc)==K and abs(d-a)==2:v|=1<<19
 if abs(pc)==P and d==e and e!=-1:v|=(1<<18)
 if abs(pc)==P and abs(d-a)==32:v|=1<<20
 return v
def au(z):
 v=ut(z);mk(v);k=(tuple(b),t,c,e);h[k]=h.get(k,0)+1
def po(p,bo):return json.load(j.urlopen(j.Request(g+p,data=json.dumps(bo).encode(),headers={"content-type":"application/json"})))
def mn():
 cu=None;ap=0
 while 1:
  gg=po("/game",{})
  if gg["status"]=="done":break
  if gg["game"]!=cu:cu=gg["game"];su();ap=0
  vs=gg.get("moves",[])
  for z in vs[ap:]:au(z)
  ap=len(vs)
  while gg["status"]=="your_move":
   v=th();z=mu(v);gg=po("/move",{"game":gg["game"],"move":z})
   vs=gg.get("moves",[])
   for z in vs[ap:]:au(z)
   ap=len(vs)
mn()
