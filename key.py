import random
i=raw_input ("Please enter a key, major or minor (e.g. E minor)")


ni=input ("Please enter number of chords you'd like :)")
n=int(ni)



if i=="A major":
	j=['Amaj','Bmin','C#min','Dmaj','Emaj','F#min','G#Dim']

if i =="A minor":
	j= ['Amin','Bdim','Cmaj','Dmin','Emin','Fmaj','Gmaj']

if i =="Ab major":
	j= ['Abmaj','Bbmin','Cmin','Dbmaj','Ebmaj','Fmin','Gdim']

if i =="Ab minor":
	j= ['Abmin','Bbdim','Cbmaj','Dbmin','Ebmin','Fbmaj','GbDmaj']

if i =="A# major":
	j= ['A#maj','B#min','C##min','D#maj','E#maj','F##min','G##dim']

if i =="A# minor":
	j= ['A#min','B#dim','C#maj','D#min','E#min','F#maj','G#maj']

if i =="Bb major":
	j=['Bbmaj','Cmin','Dmin','Ebmaj','Fmaj','Gmin','Adim']

if i =="Bb minor":
	j= ['Bbmin','Cdim','Dbmaj','Ebmin','Fmin','Gbmaj','Abmaj']

if i =="B major":
	j= ['Bmaj','C#min','D#min','Emaj','F#maj','G#min','A#dim']

if i =="B minor":
	j= ['Bmin','C#dim','Dmaj','Emin','F#min','Gmaj','Amaj']

if i =="B# major":
	j= ['B#maj','C##min','D##min','E#maj','F##maj','G##min','A##dim']

if i =="B# minor":
	j= ['B#min','C##dim','D#maj','E#min','F##min','G#maj','A#maj']

if i =="Cb major":
	j= ['Cbmaj','Dbmin','Ebmin','Fbmaj','Gbmaj','Abmin','Bbdim']

if i =="Cb minor":
	j= ['Cbmin','Dbdim','Ebbmaj','Fbmin','Gbmin','Abbmaj','Bbbmaj']

if i =="C major":
	j= ['Cmaj','Dmin','Emin','Fmaj','Gmaj','Amin','Bdim']

if i =="C minor":
	j= ['Cmin','Ddim','Ebmaj','Fmin','Gmin','Abmaj','Bbmaj']

if i =="C# major":
	j= ['C#maj','D#min','E#min','F#maj','G#maj','A#min','B#dim']

if i =="C# minor":
	j= ['C#min','D#dim','Emaj','F#min','G#min','Amaj','Bmaj']

if i =="Db major":
	j= ['Dbmaj','Ebmin','Fmin','Gbmaj','Abmaj','Bbmin','Cdim']

if i =="Db minor":
	j= ['Dbmin','Ebdim','Fbmaj','Gbmin','Abmin','Bbbmaj','Cbmaj']

if i =="D major":
	j= ['Dmaj','Emin','F#min','Gmaj','Amaj','Bmin','C#dim']

if i =="D minor":
	j= ['Dmin','Edim','Fmaj','Gmin','Amin','Bbmaj','Cmaj']

if i =="D# major":
	j= ['D#maj','E#min','F##min','G#maj','A#maj','B#min','C##dim']

if i =="D# minor":
	j= ['D#min','E#dim','F#maj','G#min','A#min','Bmaj','C#maj']

if i =="Eb major":
	j= ['Ebmaj','Fmin','Gmin','Abmaj','Bbmaj','Cmin','Ddim']

if i =="Eb minor":
	j= ['Ebmin','Fdim','Gbmaj','Abmin','Bbmin','Cbmaj','Dbmaj']

if i =="E major":
	j= ['Emaj','F#min','G#min','Amaj','Bmaj','C#min','D#dim']

if i =="E minor":
	j= ['Emin','F#dim','Gmaj','Amin','Bmin','Cmaj','Dmaj']

if i =="E# major":
	j= ['E#maj','F##min','G##min','A#maj','B#maj','C##min','D##dim']

if i =="E# minor":
	j= ['E#min','F##dim','G#maj','A#min','B#min','C#maj','D#maj']

if i =="Fb major":
	j= ['Fbmaj','Gbmin','Abmin','Bbbmaj','Cbmaj','Dbmin','Ebdim']

if i =="Fb minor":
	j= ['Fbmin','Gbdim','Abbmaj','Bbbmin','Cbmin','Dbbmaj','Ebbmaj']

if i =="F major":
	j= ['Fmaj','Gmin','Amin','Bbmaj','Cmaj','Dmin','Edim']

if i =="F minor":
	j= ['Fmin','Gdim','Abmaj','Bbmin','Cmin','Dbmaj','Ebmaj']

if i =="F# major":
	j= ['F#maj','G#min','A#min','Bmaj','C#maj','D#min','E#dim']

if i =="F# minor":
	j= ['F#min','G#dim','Amaj','Bmin','C#min','Dmaj','Emaj']

if i =="Gb major":
	j= ['Gbmaj','Abmin','Bbmin','Cbmaj','Dbmaj','Ebmin','Fdim']

if i =="Gb minor":
	j= ['Gbmin','Abdim','Bbbmaj','Cbmin','Dbmin','Ebbmaj','Fbmaj']

if i =="G major":
	j= ['Gmaj','Amin','Bmin','Cmaj','Dmaj','Emin','F#dim']

if i =="G minor":
	j= ['Gmin','Adim','Bbmaj','Cmin','Dmin','Ebmaj','Fmaj']

if i =="G# major":
	j= ['G#maj','A#min','B#min','C#maj','D#maj','E#min','F##dim']

if i =="G# minor":
	j= ['G#min','A#dim','Bmaj','C#min','D#min','Emaj','F#maj']


print random.sample((j),n)

	