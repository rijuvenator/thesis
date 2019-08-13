# Bob comments on Ch 4 -- Jun 10 2019

signal reweighting

MUO-17-001 for BibTeX for Pythia etc

Discuss volunteers after HLT-RECO matching  
Get rid of the word "only"

We begin with DSA muons to identify ...;  
associating DSA muons ...   
This thesis emphasizes the displaced muon events where the particle travels far enough before decaying that a track is not observed in the tracker  
In order to implement that requirement, we need to efficiently associate DSA muons to tracker

Global muons: 

  * main type of muons used in most CMS analyses; everything is in contrast
  * associating a tracker track with a standalone muon
  * collecting all the hits from both are put into one big Kalman fit called global muon fit

Tracker muons:

  * in order to deal with cases in which global muon reco is inefficient, tracker muons developed which do not require a standalone muon but instead extrapolate a tracker track to associate muon hits.
  * in cases where 2+ tracker tracks associated with same muon hits, algorithm called arbitration chooses which association to prefer, result called ATM

Proximity match between position and direction

"in the case that a proximity-match_ed_"  
"in principle there's this case. we were prepared to use blah blah in that case, but in practice it never happens."

"This has little practical effect" (no oversight)

As matches that are missed can lead to a high rate of background events, this association procedure is designed to be liberal.

N(DT hits) content free ? OK

"Only after a common vertex fit" ... "We use the results of the common vertex fit to define..."

"refitted" --> "vertex constrained tracks"

"However, in a few situations"

"For an arbitrary pair of DSA muons, the efficiency for the common vertex fit to converge in the relevant volume is high. Thus, considering all possible pairs of DSA muons results in many dimuons formed ..."

"correct reconstructed dimuons with high efficiency"

"Rephrase" for dimuon object selection: mixing two lists, rephrase, break up.

Same thing in signal selection

