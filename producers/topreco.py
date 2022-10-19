from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
from .electrons import TightElectrons
from .muons import TightMuons


##########################################
############## TIGHT LEPTON ##############
##########################################

LeptonSelection = Producer(
    name="LeptonSelection",
    call="LeptonSelection({df}, {input}, {output})",
    input=[
        q.n_loose_mu,
        q.n_loose_el,
        q.n_tight_mu,
        q.n_tight_el,
        q.tight_muons_mask,
        q.tight_electrons_mask,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
    ],
    output=[
        q.n_loose_lep,
        q.n_tight_lep,
        q.is_mu,
        q.is_el,
        q.lep_p4,
    ],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)


lep_pt = Producer(
    name="lep_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_pt],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)
lep_eta = Producer(
    name="lep_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_eta],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)
lep_phi = Producer(
    name="lep_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_phi],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)
lep_mass = Producer(
    name="lep_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_mass],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)

LeptonQuantities = ProducerGroup(
    name="LeptonQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
    subproducers=[lep_pt, lep_eta, lep_phi, lep_mass],
)


#####################################
############## W BOSON ##############
#####################################

LeptonicW = Producer(
    name="LeptonicW",
    call="ReconstructLeptonicW({df}, {input}, {output})",
    input=[
        q.lep_p4,
        q.pfmet_p4,
    ],
    output=[
        q.wlep_p4,
    ],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)

wlep_pt = Producer(
    name="wlep_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_pt],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)
wlep_eta = Producer(
    name="wlep_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_eta],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)
wlep_phi = Producer(
    name="wlep_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_phi],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)
wlep_mass = Producer(
    name="wlep_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_mass],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)
wlep_mt = Producer(
    name="wlep_mt",
    call="ReconstructLeptonicW_mt({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_mt],
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
)

LeptonicWQuantities = ProducerGroup(
    name="LeptonicWQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['jjb', 'jjbb', 'jjjb', 'jjjbb'],
    subproducers=[wlep_pt, wlep_eta, wlep_phi, wlep_mass, wlep_mt],
)


######################################
############## TOP RECO ##############
######################################

JetSelection_jjb = Producer(
    name="JetSelection_jjjbb",
    call="JetSelection({df}, 2, 1, {input})",
    input=[
        q.good_jets_mask,
        q.good_bjets_mask,
    ],
    output=None,
    scopes=['jjb'],
)

JetSelection_jjbb = Producer(
    name="JetSelection_jjjbb",
    call="JetSelection({df}, 2, 2, {input})",
    input=[
        q.good_jets_mask,
        q.good_bjets_mask,
    ],
    output=None,
    scopes=[ 'jjbb'],
)

JetSelection_jjjb = Producer(
    name="JetSelection_jjjbb",
    call="JetSelection({df}, 3, 1, {input})",
    input=[
        q.good_jets_mask,
        q.good_bjets_mask,
    ],
    output=None,
    scopes=['jjjb'],
)

JetSelection_jjjbb = Producer(
    name="JetSelection_jjjbb",
    call="JetSelection({df}, 3, 2, {input})",
    input=[
        q.good_jets_mask,
        q.good_bjets_mask,
    ],
    output=None,
    scopes=['jjjbb'],
)
