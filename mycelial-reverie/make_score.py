"""Reproduce the original seeded 30-second electronic ambient score (no samples)."""
import numpy as np,wave
sr=48000;dur=30;n=sr*dur;t=np.arange(n)/sr;rng=np.random.default_rng(8217);a=np.zeros((n,2))
def put(start,signal,gain=1,pan=0):
 i=int(start*sr);j=min(n,i+len(signal));s=signal[:j-i]*gain
 if i<0 or j<=i:return
 a[i:j,0]+=s*np.sqrt((1-pan)/2);a[i:j,1]+=s*np.sqrt((1+pan)/2)
def tone(f,d,bright=.3):
 u=np.arange(int(d*sr))/sr;return (np.sin(2*np.pi*f*u)+bright*np.sin(2*np.pi*2*f*u)+.12*np.sin(2*np.pi*3*f*u))*np.exp(-u*2.3)*(1-np.exp(-u*50))
for st,notes in [(0,[55,82.4069,110]),(4,[73.416,110,146.832]),(8,[65.406,98,130.813]),(12.5,[87.307,130.813,174.614]),(18,[73.416,110,146.832,220]),(24,[55,82.4069,110,164.814,220])]:
 d=7 if st<24 else 6;u=np.arange(int(d*sr))/sr;env=np.minimum(u/1.2,1)*np.minimum((d-u)/1.5,1)
 for k,f in enumerate(notes):
  sig=(np.sin(2*np.pi*f*u+.008*np.sin(u*.7))+.2*np.sin(2*np.pi*f*2*u))*env*.055;put(st,sig,1,(k%3-1)*.45)
for st in np.arange(.25,24,.535714):
 d=.32;u=np.arange(int(d*sr))/sr;sig=np.sin(2*np.pi*(47*u+4*(1-np.exp(-u*20))))*np.exp(-u*17);put(st,sig,.23 if st<4 else .16)
 if st>8:
  noise=rng.normal(0,1,len(u));noise=np.r_[0,np.diff(noise)];put(st+.27,noise*np.exp(-u*95),.015,.45)
notes=[220,329.6276,440,493.8833,659.255,440,329.6276,293.6648]
for k,st in enumerate(np.arange(4,27,.535714)):
 sig=tone(notes[k%8],1.5,.4);pan=np.sin(k*1.4)*.65;put(st,sig,.065,pan);put(st+.268,sig,.025,-pan);put(st+.536,sig,.012,pan)
for st in [3.5,7.5,12,17.5,23.5]:
 d=1.1;u=np.arange(int(d*sr))/sr;env=np.sin(np.pi*u/d)**2;freq=180+2000*(u/d)**3;sig=np.sin(2*np.pi*np.cumsum(freq)/sr)*env;put(st,sig,.055,-.25);put(st+.06,sig,.04,.35);put(st+.5,tone(880,2),.1,.1)
for st,f in [(5,1320),(9.2,1760),(10.4,1320),(14,1174.66),(16,1567.98),(19,1760),(21,1320),(24.3,880),(25,1320),(25.7,1760)]:
 sig=tone(f,3,.1);put(st,sig,.045,-.4);put(st+.35,sig,.022,.6)
env=np.minimum(t/.6,1)*np.minimum((dur-t)/1.3,1);a*=env[:,None];a=np.tanh(a*1.5);a*=.85/max(np.max(np.abs(a)),.85)
with wave.open('assets/score.wav','wb') as w:w.setnchannels(2);w.setsampwidth(2);w.setframerate(sr);w.writeframes((a*32767).astype('<i2').tobytes())
