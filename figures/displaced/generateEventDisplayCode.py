# given a bunch of event displays from my Fireworks configuration, these commands crop them appropriately:
#
# for i in unnamed-*_RhoZ.png; do x=${i/unnamed/event}; convert $i -crop 600x934+0+460 $x; done
# for i in unnamed-*_RhoPhi.png; do x=${i/unnamed/event}; convert $i -crop 1000x960+0+900 $x; done
#

import glob, re

files = glob.glob('event-*.png')
files.sort()

text = r'''
\begin{{figure}}[htpb]
  \centering
  \includegraphics[width=0.6\textwidth]{{figures/displaced/event-{RUN}_{EVENT}_{LUMI}_RhoPhi.png}}
  \includegraphics[width=0.6\textwidth]{{figures/displaced/event-{RUN}_{EVENT}_{LUMI}_RhoZ.png}}
  \caption{{Display of $\rho$-$\phi$ and $\rho$-$z$ views of event {EVENT} in 2016 data, in run {RUN}, lumi section {LUMI}.}}
  \label{{fig:dd:event-{LUMI}}}
\end{{figure}}'''

LUMIVETO = (669, 36, 1211, 847, 67)

dump = '''
DataB 274969  944 1675672448 ::: 56.9093 ::: 0.0764 :::  10.250 :::   0.0892   0.0044   -3.2245   -3.2245
DataD 276501  115  192083163 ::: 16.6786 ::: 2.1073 :::  45.840 :::   0.0463   0.2954    1.1651    7.4872
DataE 276831  669 1162025779 ::: 18.5126 ::: 0.2575 :::  34.150 :::   0.0302   0.1581   26.7362   26.4851
DataE 276870   87   45169652 :::  6.0748 ::: 3.0100 :::  35.470 :::   0.2470   0.0528   49.2451   -0.4646
DataE 276935  522  801995838 :::  6.7612 ::: 0.1309 :::  24.010 :::   0.0267   0.0783   -0.1558    1.5924
DataE 276940   97   59821031 ::: 14.2250 ::: 0.1123 :::  14.820 :::   0.1127   0.0065    3.3952   -2.5707
DataE 276947    4    6168006 :::  6.7264 ::: 0.0020 :::  15.370 :::   0.0569   0.0806    0.2279    0.6729
DataE 277127  131  251897955 :::  9.5866 ::: 1.3679 ::: 183.300 :::   0.0500   0.0079   -0.0352    1.6490
DataE 277168  114  203474554 ::: 76.6759 ::: 0.0714 :::  24.620 :::   0.0746   0.0222    0.8900    0.4811
DataF 278017  169  188965749 :::  8.8979 ::: 0.3114 :::  64.400 ::: 999.0000   0.0516 -999.0000   -1.5565
DataF 278274   67  138267891 :::  8.9318 ::: 0.2053 :::  61.580 :::   0.2155   0.0144  -50.0945    0.0029
DataF 278308  390  635154343 :::  8.8142 ::: 0.3784 ::: 184.100 :::   0.0593   0.0062    1.5499    0.8275
DataF 278345  523  879392031 :::  8.0093 ::: 2.7680 :::  68.800 :::   0.2628   0.0063   25.8254   -1.6082
DataG 279716 1211 2119675441 ::: 10.0141 ::: 0.5990 :::  56.660 :::   0.1218   0.0268   22.4661   24.1090
DataG 280249  847 1563984578 :::  6.9548 ::: 0.6037 :::  99.330 :::   0.0604   0.0179   24.6830   23.6719
DataG 280364   36   71857100 ::: 14.2920 ::: 0.2676 :::  21.750 :::   0.0105   0.2036   25.1886   26.6429
DataH 281797  501  676135274 ::: 87.7030 ::: 0.0468 :::  15.610 :::   0.0669   0.0850   -1.1093    2.4810
DataH 281976  604 1068424953 ::: 12.8926 ::: 1.8940 :::  91.620 ::: 999.0000   0.0188 -999.0000   50.0227'''

data = {}
for line in dump.split('\n'):
    if line == '': continue
    cols = line.split()
    lumi, lxysig, deltaphi, mass = cols[2], cols[5], cols[7], cols[9]
    data[lumi] = {'LxySig':float(lxysig), 'DeltaPhi':float(deltaphi), 'Mass':float(mass)}

for f in files:
    match = re.match(r'event-(\d*?)_(\d*?)_(\d*?)_Rho(Phi|Z).png', f)
    RUN, EVENT, LUMI, Y = match.groups()
    if Y == 'Z': continue
    if int(LUMI) in LUMIVETO: continue

    if False:
        print text.format(**locals())

    if True:
        print '{:6s} & {:4s} & {:10s} & {:5.1f} & {:.4f} & {:5.2f} & \\Fig~\\ref{{fig:dd:event-{}}}{} \\\\'.format(
            RUN, LUMI, EVENT,
            data[LUMI]['Mass'],
            data[LUMI]['DeltaPhi'],
            data[LUMI]['LxySig'],
            LUMI,
            ''.join([' ']*(3-len(LUMI))))
