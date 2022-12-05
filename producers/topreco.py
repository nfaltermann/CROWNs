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
    call="topreco::LeptonSelection({df}, {input}, {output})",
    input=[
        q.n_loose_mu,
        q.n_loose_el,
        q.n_tight_mu,
        q.n_tight_el,
        q.tight_muons_mask,
        q.tight_electrons_mask,
        q.n_antitight_mu,
        q.n_antitight_el,
        q.antitight_muons_mask,
        q.antitight_electrons_mask,
        nanoAOD.Muon_pt,
        nanoAOD.Muon_eta,
        nanoAOD.Muon_phi,
        nanoAOD.Muon_mass,
        nanoAOD.Muon_charge,
        nanoAOD.Electron_pt,
        nanoAOD.Electron_eta,
        nanoAOD.Electron_deltaEtaSC,
        nanoAOD.Electron_phi,
        nanoAOD.Electron_mass,
        nanoAOD.Electron_charge,
    ],
    output=[
        q.n_loose_lep,
        q.n_tight_lep,
        q.n_antitight_lep,
        q.lep_is_mu,
        q.lep_is_el,
        q.lep_is_iso,
        q.lep_p4,
        q.lep_sceta,
        q.lep_charge,
    ],
    scopes=['lep'],
)


lep_pt = Producer(
    name="lep_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_pt],
    scopes=['lep'],
)
lep_eta = Producer(
    name="lep_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_eta],
    scopes=['lep'],
)
lep_phi = Producer(
    name="lep_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_phi],
    scopes=['lep'],
)
lep_mass = Producer(
    name="lep_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.lep_p4],
    output=[q.lep_mass],
    scopes=['lep'],
)

LeptonQuantities = ProducerGroup(
    name="LeptonQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[lep_pt, lep_eta, lep_phi, lep_mass],
)




LeptonScaleFactors  = Producer(
    name="LeptonScaleFactors",
    call='topreco::LeptonScaleFactors({df}, {input}, {output}, "{muon_sf_era}", "{muon_trigger_sf_file}", "{muon_trigger_sf_file_syst}", "{muon_trigger_sf_name}", "{muon_trigger_sf_name_syst}", "{muon_iso_sf_file}", "{muon_iso_sf_file_syst}", "{muon_iso_sf_name}", "{muon_iso_sf_name_syst}", "{muon_sf_file}", "{muon_id_sf_name}", "{ele_sf_era}", "{ele_trigger_sf_file}", "{ele_trigger_sf_file_syst}", "{ele_trigger_sf_name}", "{ele_trigger_sf_name_syst}", "{ele_sf_file}", "{ele_id_sf_name}")',
    input=[
        q.lep_pt,
        q.lep_eta,
        q.lep_sceta,
        q.lep_is_mu,
        q.lep_is_el,
        q.lep_is_iso,
    ],
    output=[
        q.lep_sf_mu_trigger_nom,
        q.lep_sf_mu_trigger_up,
        q.lep_sf_mu_trigger_down,
        q.lep_sf_mu_iso_nom,
        q.lep_sf_mu_iso_up,
        q.lep_sf_mu_iso_down,
        q.lep_sf_mu_id_nom,
        q.lep_sf_mu_id_up,
        q.lep_sf_mu_id_down,
        q.lep_sf_el_trigger_nom,
        q.lep_sf_el_trigger_up,
        q.lep_sf_el_trigger_down,
        q.lep_sf_el_id_nom,
        q.lep_sf_el_id_up,
        q.lep_sf_el_id_down,
        q.lep_sf_el_reco_nom,
        q.lep_sf_el_reco_up,
        q.lep_sf_el_reco_down,
    ],
    scopes=['lep'],
)

#####################################
############## W BOSON ##############
#####################################

LeptonicW = Producer(
    name="LeptonicW",
    call="topreco::ReconstructLeptonicW({df}, {input}, {output})",
    input=[
        q.lep_p4,
        q.pfmet_p4_jetcorrected,
    ],
    output=[
        q.wlep_p4,
    ],
    scopes=['lep'],
)

wlep_pt = Producer(
    name="wlep_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_pt],
    scopes=['lep'],
)
wlep_eta = Producer(
    name="wlep_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_eta],
    scopes=['lep'],
)
wlep_phi = Producer(
    name="wlep_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_phi],
    scopes=['lep'],
)
wlep_mass = Producer(
    name="wlep_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.wlep_p4],
    output=[q.wlep_mass],
    scopes=['lep'],
)
wlep_mt = Producer(
    name="wlep_mt",
    call="quantities::mT({df}, {output}, {input})",
    input=[q.lep_p4,
           q.pfmet_p4],
    output=[q.wlep_mt],
    scopes=['lep'],
)

LeptonicWQuantities = ProducerGroup(
    name="LeptonicWQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[wlep_pt, wlep_eta, wlep_phi, wlep_mass, wlep_mt],
)


######################################
############## TOP RECO ##############
######################################

TopReco = Producer(
    name="TopReco",
    call="topreco::TopReco({df}, {input}, {output})",
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
    scopes=['lep'],
)

top_pt = Producer(
    name="top_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_pt],
    scopes=['lep'],
)
top_eta = Producer(
    name="top_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_eta],
    scopes=['lep'],
)
top_phi = Producer(
    name="top_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_phi],
    scopes=['lep'],
)
top_mass = Producer(
    name="top_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.top_p4],
    output=[q.top_mass],
    scopes=['lep'],
)

tb_pt = Producer(
    name="tb_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_pt],
    scopes=['lep'],
)
tb_eta = Producer(
    name="tb_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_eta],
    scopes=['lep'],
)
tb_phi = Producer(
    name="tb_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_phi],
    scopes=['lep'],
)
tb_mass = Producer(
    name="tb_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.tb_p4],
    output=[q.tb_mass],
    scopes=['lep'],
)

sb_pt = Producer(
    name="sb_pt",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_pt],
    scopes=['lep'],
)
sb_eta = Producer(
    name="sb_eta",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_eta],
    scopes=['lep'],
)
sb_phi = Producer(
    name="sb_phi",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_phi],
    scopes=['lep'],
)
sb_mass = Producer(
    name="sb_mass",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.sb_p4],
    output=[q.sb_mass],
    scopes=['lep'],
)

TopRecoQuantities = ProducerGroup(
    name="TopRecoQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[top_pt, top_eta, top_phi, top_mass,
                  tb_pt, tb_eta, tb_phi, tb_mass,
                  sb_pt, sb_eta, sb_phi, sb_mass],
)


DNNQuantities = Producer(
    name="DNNQuantities",
    call="topreco::DNNQuantities({df}, {input}, {output})",
    input=[
        q.is_reco,
        q.lep_p4,
        q.pfmet_p4_jetcorrected,
        q.wlep_p4,
        q.nonbjet_1_p4,
        q.nonbjet_1_btag,
        q.nonbjet_2_p4,
        q.nonbjet_2_btag,
        q.bjet_1_p4,
        q.bjet_1_btag,
        q.bjet_2_p4,
        q.bjet_2_btag,
        q.top_p4,
        q.tb_p4,
        q.sb_p4,
        q.good_jetslowpt_mask,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
   ],
    output=[
        q.dphi_top_b1,
        q.deta_top_sb,
        q.dphi_b1_b2,
        q.deta_lep_b1,
        q.m_lep_b2,
        q.pt_b1_b2,
        q.costhetastar,
        q.sumht,
        q.wolfram,
        q.deta_topb2_b1,
    ],
    scopes=['lep'],
)




BTagScaleFactors  = Producer(
    name="BTagScaleFactors",
    call='topreco::BTagScaleFactors({df}, {input}, {output}, "{btag_sf_file}", "{btag_corr_algo_HF}", "{btag_corr_algo_LF}", "{btag_eff_file}", "{btag_eff_type}", "{btag_wp}", {max_bjet_eta_sf})',
    input=[
        q.lep_is_iso,
        q.is_reco,
        q.is_jjb,
        q.is_jjbb,
        q.is_jjjb,
        q.is_jjjbb,
        q.nonbjet_1_pt,
        q.nonbjet_1_eta,
        q.nonbjet_1_btag,
        q.nonbjet_1_flavor,
        q.nonbjet_2_pt,
        q.nonbjet_2_eta,
        q.nonbjet_2_btag,
        q.nonbjet_2_flavor,
        q.bjet_1_pt,
        q.bjet_1_eta,
        q.bjet_1_btag,
        q.bjet_1_flavor,
        q.bjet_2_pt,
        q.bjet_2_eta,
        q.bjet_2_btag,
        q.bjet_2_flavor,
    ],
    output=[
        q.btag_sf_vec,
        q.btag_sf_nom,
        q.btag_sf_HFup_corr,
        q.btag_sf_HFup_uncorr,
        q.btag_sf_HFdown_corr,
        q.btag_sf_HFdown_uncorr,
        q.btag_sf_LFup_corr,
        q.btag_sf_LFup_uncorr,
        q.btag_sf_LFdown_corr,
        q.btag_sf_LFdown_uncorr,
    ],
    scopes=['lep'],
)
