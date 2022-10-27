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
        q.lep_is_mu,
        q.lep_is_el,
        q.lep_is_iso,
        q.lep_p4,
    ],
    scopes=['lep_iso'],
)

AntiLeptonSelection = Producer(
    name="AntiLeptonSelection",
    call="AntiLeptonSelection({df}, {input}, {output})",
    input=[
        q.n_loose_mu,
        q.n_loose_el,
        q.n_antitight_mu,
        q.n_antitight_el,
        q.antitight_muons_mask,
        q.antitight_electrons_mask,
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
        q.n_antitight_lep,
        q.lep_is_mu,
        q.lep_is_el,
        q.lep_is_iso,
        q.lep_p4,
    ],
    scopes=['lep_antiiso'],
)



lep_pt = Producer(
    name="lep_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_pt],
    scopes=['lep_iso', "lep_antiiso"],
)
lep_eta = Producer(
    name="lep_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_eta],
    scopes=['lep_iso', "lep_antiiso"],
)
lep_phi = Producer(
    name="lep_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_phi],
    scopes=['lep_iso', "lep_antiiso"],
)
lep_mass = Producer(
    name="lep_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_mass],
    scopes=['lep_iso', "lep_antiiso"],
)

LeptonQuantities = ProducerGroup(
    name="LeptonQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep_iso', "lep_antiiso"],
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
    scopes=['lep_iso', "lep_antiiso"],
)

wlep_pt = Producer(
    name="wlep_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_pt],
    scopes=['lep_iso', "lep_antiiso"],
)
wlep_eta = Producer(
    name="wlep_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_eta],
    scopes=['lep_iso', "lep_antiiso"],
)
wlep_phi = Producer(
    name="wlep_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_phi],
    scopes=['lep_iso', "lep_antiiso"],
)
wlep_mass = Producer(
    name="wlep_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_mass],
    scopes=['lep_iso', "lep_antiiso"],
)
wlep_mt = Producer(
    name="wlep_mt",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.lep_p4,
           q.pfmet_p4],
    output=[q.wlep_mt],
    scopes=['lep_iso', "lep_antiiso"],
)

LeptonicWQuantities = ProducerGroup(
    name="LeptonicWQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep_iso', "lep_antiiso"],
    subproducers=[wlep_pt, wlep_eta, wlep_phi, wlep_mass, wlep_mt],
)


######################################
############## TOP RECO ##############
######################################

TopReco = Producer(
    name="TopReco",
    call="TopReco({df}, {input}, {output})",
    input=[
        q.wlep_p4,
        q.n_nonbjets,
        q.nonbjet_1_p4,
        q.nonbjet_1_btag,
        q.nonbjet_2_p4,
        q.nonbjet_2_btag,
        q.n_bjets,
        q.bjet_1_p4,
        q.bjet_1_btag,
        q.bjet_2_p4,
        q.bjet_2_btag,
    ],
    output=[
        q.is_reco,
        q.is_jjb,
        q.is_jjbb,
        q.is_jjjb,
        q.is_jjjbb,
        q.reco_p4s,
        q.top_p4,
        q.tb_p4,
        q.sb_p4,
    ],
    scopes=['lep_iso', "lep_antiiso"],
)

top_pt = Producer(
    name="top_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_pt],
    scopes=['lep_iso', "lep_antiiso"],
)
top_eta = Producer(
    name="top_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_eta],
    scopes=['lep_iso', "lep_antiiso"],
)
top_phi = Producer(
    name="top_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_phi],
    scopes=['lep_iso', "lep_antiiso"],
)
top_mass = Producer(
    name="top_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_mass],
    scopes=['lep_iso', "lep_antiiso"],
)

tb_pt = Producer(
    name="tb_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_pt],
    scopes=['lep_iso', "lep_antiiso"],
)
tb_eta = Producer(
    name="tb_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_eta],
    scopes=['lep_iso', "lep_antiiso"],
)
tb_phi = Producer(
    name="tb_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_phi],
    scopes=['lep_iso', "lep_antiiso"],
)
tb_mass = Producer(
    name="tb_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_mass],
    scopes=['lep_iso', "lep_antiiso"],
)

sb_pt = Producer(
    name="sb_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_pt],
    scopes=['lep_iso', "lep_antiiso"],
)
sb_eta = Producer(
    name="sb_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_eta],
    scopes=['lep_iso', "lep_antiiso"],
)
sb_phi = Producer(
    name="sb_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_phi],
    scopes=['lep_iso', "lep_antiiso"],
)
sb_mass = Producer(
    name="sb_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_mass],
    scopes=['lep_iso', "lep_antiiso"],
)

TopRecoQuantities = ProducerGroup(
    name="TopRecoQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep_iso', "lep_antiiso"],
    subproducers=[top_pt, top_eta, top_phi, top_mass,
                  tb_pt, tb_eta, tb_phi, tb_mass,
                  sb_pt, sb_eta, sb_phi, sb_mass],
)
