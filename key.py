import random
i=raw_input ("Please enter a key, major or minor (e.g. E minor)")


ni=input ("Please enter number of chords you'd like :)")
n=int(ni)

al=['Amaj','Bmin','C#min','Dmaj','Emaj','F#min','G#Dim']
aml=['Amin','Bdim','Cmaj','Dmin','Emin','Fmaj','Gmaj']
abl=['Abmaj','Bbmin','Cmin','Dbmaj','Ebmaj','Fmin','Gdim']
abml=['Abmin','Bbdim','Cbmaj','Dbmin','Ebmin','Fbmaj','GbDmaj']
ashl=['A#maj','B#min','C##min','D#maj','E#maj','F##min','G##dim']
ashml=['A#min','B#dim','C#maj','D#min','E#min','F#maj','G#maj']
bbl=['Bbmaj','Cmin','Dmin','Ebmaj','Fmaj','Gmin','Adim']
bbml=['Bbmin','Cdim','Dbmaj','Ebmin','Fmin','Gbmaj','Abmaj']
bl=['Bmaj','C#min','D#min','Emaj','F#maj','G#min','A#dim']
bml=['Bmin','C#dim','Dmaj','Emin','F#min','Gmaj','Amaj']
bshl=['B#maj','C##min','D##min','E#maj','F##maj','G##min','A##dim']
bshml=['B#min','C##dim','D#maj','E#min','F##min','G#maj','A#maj']
cbl=['Cbmaj','Dbmin','Ebmin','Fbmaj','Gbmaj','Abmin','Bbdim']
cbml=['Cbmin','Dbdim','Ebbmaj','Fbmin','Gbmin','Abbmaj','Bbbmaj']
cl=['Cmaj','Dmin','Emin','Fmaj','Gmaj','Amin','Bdim']
cml=['Cmin','Ddim','Ebmaj','Fmin','Gmin','Abmaj','Bbmaj']
cshl=['C#maj','D#min','E#min','F#maj','G#maj','A#min','B#dim']
cshml=['C#min','D#dim','Emaj','F#min','G#min','Amaj','Bmaj']
dbl=['Dbmaj','Ebmin','Fmin','Gbmaj','Abmaj','Bbmin','Cdim']
dbml=['Dbmin','Ebdim','Fbmaj','Gbmin','Abmin','Bbbmaj','Cbmaj']
dl=['Dmaj','Emin','F#min','Gmaj','Amaj','Bmin','C#dim']
dml=['Dmin','Edim','Fmaj','Gmin','Amin','Bbmaj','Cmaj']
dshl=['D#maj','E#min','F##min','G#maj','A#maj','B#min','C##dim']
dshml=['D#min','E#dim','F#maj','G#min','A#min','Bmaj','C#maj']
ebl=['Ebmaj','Fmin','Gmin','Abmaj','Bbmaj','Cmin','Ddim']
ebml=['Ebmin','Fdim','Gbmaj','Abmin','Bbmin','Cbmaj','Dbmaj']
el=['Emaj','F#min','G#min','Amaj','Bmaj','C#min','D#dim']
eml=['Emin','F#dim','Gmaj','Amin','Bmin','Cmaj','Dmaj']
eshl=['E#maj','F##min','G##min','A#maj','B#maj','C##min','D##dim']
eshml=['E#min','F##dim','G#maj','A#min','B#min','C#maj','D#maj']
fbl=['Fbmaj','Gbmin','Abmin','Bbbmaj','Cbmaj','Dbmin','Ebdim']
fbml=['Fbmin','Gbdim','Abbmaj','Bbbmin','Cbmin','Dbbmaj','Ebbmaj']
fl=['Fmaj','Gmin','Amin','Bbmaj','Cmaj','Dmin','Edim']
fml=['Fmin','Gdim','Abmaj','Bbmin','Cmin','Dbmaj','Ebmaj']
fshl=['F#maj','G#min','A#min','Bmaj','C#maj','D#min','E#dim']
fshml=['F#min','G#dim','Amaj','Bmin','C#min','Dmaj','Emaj']
gbl=['Gbmaj','Abmin','Bbmin','Cbmaj','Dbmaj','Ebmin','Fdim']
gbml=['Gbmin','Abdim','Bbbmaj','Cbmin','Dbmin','Ebbmaj','Fbmaj']
gl=['Gmaj','Amin','Bmin','Cmaj','Dmaj','Emin','F#dim']
gml=['Gmin','Adim','Bbmaj','Cmin','Dmin','Ebmaj','Fmaj']
gshl=['G#maj','A#min','B#min','C#maj','D#maj','E#min','F##dim']
gshml=['G#min','A#dim','Bmaj','C#min','D#min','Emaj','F#maj']
a= ("A major")
am=("A minor")
ab=("Ab major")
abm=("Ab minor")
ash=("A# major")
ashm=("A# minor")
bb=("Bb major")
bbm=("Bb minor")
b=("B major")
bm=("B minor")
bsh=("B# major")
bshm=("B# minor")
cb=("Cb major")
cbm=("Cb minor")
c=("C major")
cm=("C minor")
csh=("C# major")
cshm=("C# minor")
db=("Db major")
dbm=("Db minor")
d=("D major")
dm=("D minor")
dsh=("D# major")
dshm=("D# minor")
eb=("Eb major")
ebm=("Eb minor")
e=("E major")
em=("E minor")
esh=("E# major")
eshm=("E# minor")
fb=("Fb major")
fbm=("Fb minor")
f=("F major")
fm=("F minor")
fsh=("F# major")
fshm=("F# minor")
gb=("Gb major")
gbm=("Gb minor")
g=("G major")
gm=("G minor")
gsh=("G# major")
gshm=("G# minor")

if i==a:
	print random.sample((al),n)

if i==am:
	print random.sample((aml),n)

if i==ab:
	print random.sample((abl),n)

if i==abm:
	print random.sample((abml),n)

if i==ash:
	print random.sample((ashl),n)

if i==ashm:
	print random.sample((ashml),n)

if i==bb:
	print random.sample((bbl),n)

if i==bbm:
	print random.sample((bbml),n)

if i==b:
	print random.sample((bl),n)

if i==bm:
	print random.sample((bml),n)

if i==bsh:
	print random.sample((bshl),n)

if i==bshm:
	print random.sample((bshml),n)

if i==cb:
	print random.sample((cbl),n)

if i==cbm:
	print random.sample((cbml),n)

if i==c:
	print random.sample((cl),n)

if i==cm:
	print random.sample((cml),n)

if i==csh:
	print random.sample((cshl),n)

if i==cshm:
	print random.sample((cshml),n)

if i==db:
	print random.sample((dbl),n)

if i==dbm:
	print random.sample((dbml),n)

if i==d:
	print random.sample((dl),n)

if i==dm:
	print random.sample((dml),n)

if i==dsh:
	print random.sample((dshl),n)

if i==dshm:
	print random.sample((dshml),n)

if i==eb:
	print random.sample((ebl),n)

if i==ebm:
	print random.sample((ebml),n)

if i==e:
	print random.sample((el),n)

if i==em:
	print random.sample((eml),n)

if i==esh:
	print random.sample((eshl),n)

if i==eshm:
	print random.sample((eshml),n)

if i==fb:
	print random.sample((fbl),n)

if i==fbm:
	print random.sample((fbml),n)

if i==f:
	print random.sample((fl),n)

if i==fm:
	print random.sample((fml),n)

if i==fsh:
	print random.sample((fshl),n)

if i==fshm:
	print random.sample((fshml),n)

if i==gb:
	print random.sample((gbl),n)

if i==gbm:
	print random.sample((gbml),n)

if i==g:
	print random.sample((gl),n)

if i==gm:
	print random.sample((gml),n)

if i==gsh:
	print random.sample((gshl),n)

if i==gshm:
	print random.sample((gshml),n)


	