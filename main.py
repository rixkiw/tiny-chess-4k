# tiny-chess-01 entry: lzma-packed chess engine, Python 3.13 stdlib only.
# alpha-beta with quiescence, incremental evaluation, killer moves, late-move reductions, fixed node budget.
import base64,lzma
exec(lzma.decompress(base64.b85decode(
'{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;1Bx-{9OPvn@VT6Qap3u7A1{kq%B%nSvVN<h6|E8eS1piol8R37^;7zv`LYF;a77E5*?nA'
'HC)!kuQhcuxP|!CWKoGSE8h8Y(m^anGG;25Vbu}Yg}S95ZRZok0K_xEXa9eEKe_$Zs2&5Qr26;}*D$%6zdNS6b%$UOrDf%@gae4;'
'Nsz{9pl`YkaM^2Vc#Q|)&s1veE{^_0e>E!oz66v+Ed)}Zu9g&LTibOH)Q~FDj+Zy)obL7}jhGmVzHaAbpjxITamX=!$Al_7ZT|c&'
'S?h%YfK`EPp__#8BdQT$6!lsF<e%fOpiv-Peow?y<YA+hI;bUrkC8uSPnbY-!AVw3TMp7Ke>!8p$2Qn5%&B0A^Z9H5*U`o_o=J#y'
'((!3HRw*kgV-hISJ!1stGrmS1H+(5)k`zLaz)}weYu9w4<7#cZTndP5^hD_P3z{w)*NtcK%{Z`m5t5}68+`|`xoI~#vW79J>9o&%'
'G-Eg{RIX(-d(Xz=hSHO$X@9P{*@N@@lbEL}M)I{wkC}%8XKPD1vK;p*m2xeRrSxlerM1@TfA*!A6UWS%c2mBWMtnFkQUl#$)1q~j'
'Sa*4>5I5OMcRZxsj|dXxqmXQdO0K!-B4Rr!gFIy^lO@F;dn_ndWGqA}OYdOv^jSpXrmf>Wl*ry8rEuIBIC~(t(iOp}*EmL)r(@NQ'
'o%SA(u<xR!Xy3i1pep+D@-RcrS=jev6fjV7B&somq%p8M$_}sm0^#|>=fN_5#21G_OSh}0M%f$-Jg)bs(vK_5f1W#iZr3;9;kXLH'
'QGhF)D`MiXNheU~P$MKX#g}J|Si=wjEcJ#>^&r7*Nj#}ujnKg>bzTC~IhvT(f$2<~UU@v#j57=(_FuM|U#@JR0fNjNLqwUVfQJ-q'
'fH%rdc2J1FVrvaO^Qh0mKs(&WY{Nx)j6nh&fLtJ$Edl~durSmvPV1KonW!i|&G=laD!0N)hHgUSPaw@v)Vz+c9+WM=!4VwcDJfyB'
'I%QkZ%EoUOXKY||^fOR8Y>qNlDDWfH*qs11GI(Cv)Agg0V^)^6g$Gac@p312V#glf3`T>Pc!wW>t+l5J1YqxzW~57+0DF~WGuJr('
'DVkfG(%Yg4F0Cb4k{64La$(<Ls2f{3BKYU~#m%EQfG+XQ`>)Chwx)+Wh*n17|CBA)*F~Np(GPm;0cYchy#+%zx9EqFBxy^paj`g!'
'hypyQtdGH#$+;^R1wr&F;?akr$56hZLcIzdEAHh&5$96!cYH5GebhOT-8-Z@vyCGxq^!op?4zW1NXpX%(cVYPJE$hn!y`eN&Mefi'
'3TB~0i>hSHS0?@@j#7Y<-f8Er8a2-AX&2XS^M8U*f|dQ~GII8G+<wjgonYgQX{$i4ft3s)!vUZ-8WB9MQHPv}Ot>#y>(eN?M}@YV'
'R`*yL3);N{Q+u5}y1)5mswi9(On&;OdGwnbMnHY6c#{4kmQUj|BnT&@jPYNtO~-MBr7@FB$Ga+qnZ6=fYS7p4>zdAEkvK<8VZiT4'
'A2yItHb96?LtRQ+JAs?70$z=|*}tO~^FB8A&-aeGpO<hJiPitF0)h(%1};!Qnvk<K#KG=8!?9@+igiTALe<Dn)?(byL7UrQEg?^5'
'w+B$~w~$*4>>VL|){zYQm+KD~IvloSXrCL!x`DOza9RWha9@E;pCY!Xb8&q6!I3clRznW@*|80*+B4a7Q87j<sATHoIGN}1{~s)U'
'x-2G4%48pPfm&a)CG=bG&baVdMp_<p*FNQN-YZE}dHo#T%Z^%ST|%jA(sai6osUj#8KyseK*j#HePf4eu~jx{9Jy31up}>ZS=W5-'
'l1x*%bpF<Ob~ht=-}DU&hOJ3!VJsHe-reY}A&0w!BOv~ee(sXVwKN?c@JRE62&T}iKsDvT1?&@G3BFIMcW#u<7`OVtdXwRecl_Gx'
'(oa%E7V-c9xuV_1Z6BLQd0--u-H_gy2Xj*8zw^Xe<9*kjLvK)Pd<xd|2q(*u9l3yh_zOyOn#S47)gm^j-Y4~gF^syY(p@m|#7a5e'
'(Bc3V<8R^7<qNus7|mCqTtZmAOs8)wdm?3X#sKKcGPmZWrkNGn=;LfP;$(OzEn`fG-HUq0_QpX=oXtebI*<r)IF|B^uu7KHg+2^g'
'%`v1h>nAR{V6*mbglL)lV>6A<8^#wW^lZt3Dr7SCs9LgYwTSE2#t6CW!*)WsF*7cUH#wZpoPBs;zhDMZhvHkKeEuX}n!JmRYO;W1'
'ncm$O>w;%}*iXm`1Y|8t|1X@Nzww@g!(S^DI`S+}T5mvoac_=ILY8q<guXqbRvJP45VB<Ea){CZRrQB8zwM+S00Ec|{2u@Sz_XfG'
'vBYQl0ssI200dcD')))
# end of entry
