from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# Set of producers used for selection possible good jets
####################
JetPtCorrection = Producer(
    name="JetPtCorrection",
    call="physicsobject::jet::JetPtCorrection({df}, {output}, {input}, {jet_reapplyJES}, {jet_jes_sources}, {jet_jes_shift}, {jet_jer_shift}, {jet_jec_file}, {jet_jer_tag}, {jet_jes_tag}, {jet_jec_algo})",
    input=[
        nanoAOD.Jet_pt,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        nanoAOD.Jet_area,
        nanoAOD.Jet_rawFactor,
        nanoAOD.Jet_ID,
        nanoAOD.GenJet_pt,
        nanoAOD.GenJet_eta,
        nanoAOD.GenJet_phi,
        nanoAOD.rho,
    ],
    output=[q.Jet_pt_corrected],
    scopes=["global"],
)
JetPtCorrection_data = Producer(
    name="JetPtCorrection_data",
    call="physicsobject::jet::JetPtCorrection_data({df}, {output}, {input}, {jet_jec_file}, {jet_jes_tag_data}, {jet_jec_algo})",
    input=[
        nanoAOD.Jet_pt,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_area,
        nanoAOD.Jet_rawFactor,
        nanoAOD.rho,
    ],
    output=[q.Jet_pt_corrected],
    scopes=["global"],
)
JetMassCorrection = Producer(
    name="JetMassCorrection",
    call="physicsobject::ObjectMassCorrectionWithPt({df}, {output}, {input})",
    input=[
        nanoAOD.Jet_mass,
        nanoAOD.Jet_pt,
        q.Jet_pt_corrected,
    ],
    output=[q.Jet_mass_corrected],
    scopes=["global"],
)
# in data and embdedded sample, we simply rename the nanoAOD jets to the jet_pt_corrected column
RenameJetPt = Producer(
    name="RenameJetPt",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_pt],
    output=[q.Jet_pt_corrected],
    scopes=["global"],
)
RenameJetMass = Producer(
    name="RenameJetMass",
    call="basefunctions::rename<ROOT::RVec<float>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_mass],
    output=[q.Jet_mass_corrected],
    scopes=["global"],
)
RenameJetsData = ProducerGroup(
    name="RenameJetsData",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[RenameJetPt, RenameJetMass],
)
JetEnergyCorrection = ProducerGroup(
    name="JetEnergyCorrection",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[JetPtCorrection, JetMassCorrection],
)
JetEnergyCorrection_data = ProducerGroup(
    name="JetEnergyCorrection",
    call=None,
    input=None,
    output=None,
    scopes=["global"],
    subproducers=[JetPtCorrection_data, JetMassCorrection],
)
JetPtCut = Producer(
    name="JetPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_jet_pt})",
    input=[q.Jet_pt_corrected],
    output=[],
    scopes=["global"],
)
JetLowPtCut = Producer(
    name="JetLowPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_jet_lowpt})",
    input=[q.Jet_pt_corrected],
    output=[],
    scopes=["global"],
)
BJetPtCut = Producer(
    name="BJetPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_bjet_pt})",
    input=[q.Jet_pt_corrected],
    output=[],
    scopes=["global"],
)
NonBJetPtCut = Producer(
    name="BJetPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_bjet_pt})",
    input=[q.Jet_pt_corrected],
    output=[],
    scopes=["global"],
)
JetEtaCut = Producer(
    name="JetEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_jet_eta})",
    input=[nanoAOD.Jet_eta],
    output=[q.jet_eta_mask],
    scopes=["global"],
)
BJetEtaCut = Producer(
    name="BJetEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_bjet_eta})",
    input=[nanoAOD.Jet_eta],
    output=[],
    scopes=["global"],
)
NonBJetEtaCut = Producer(
    name="BJetEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_bjet_eta})",
    input=[nanoAOD.Jet_eta],
    output=[],
    scopes=["global"],
)
JetIDCut = Producer(
    name="JetIDCut",
    call="physicsobject::jet::CutID({df}, {output}, {input}, {jet_id})",
    input=[nanoAOD.Jet_ID],
    output=[q.jet_id_mask],
    scopes=["global"],
)
JetPUIDCut = Producer(
    name="JetPUIDCut",
    call="physicsobject::jet::CutPUID({df}, {output}, {input}, {jet_puid}, {jet_puid_max_pt})",
    input=[nanoAOD.Jet_PUID, q.Jet_pt_corrected],
    output=[q.jet_puid_mask],
    scopes=["global"],
)
BTagCut = Producer(
    name="BTagCut",
    call="physicsobject::jet::CutRawID({df}, {input}, {output}, {btag_cut})",
    input=[nanoAOD.BJet_discriminator],
    output=[],
    scopes=["global"],
)
BTagAntiCut = Producer(
    name="BTagAntiCut",
    call="physicsobject::jet::AntiCutRawID({df}, {input}, {output}, {btag_cut})",
    input=[nanoAOD.BJet_discriminator],
    output=[],
    scopes=["global"],
)

GoodJetsLowPt = ProducerGroup(
    name="GoodJetsLowPt",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.good_jetslowpt_mask],
    scopes=["global"],
    subproducers=[JetLowPtCut, JetEtaCut, JetIDCut, JetPUIDCut],
)
GoodJets = ProducerGroup(
    name="GoodJets",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.jet_eta_mask, q.jet_id_mask, q.jet_puid_mask],
    output=[q.good_jets_mask],
    scopes=["global"],
    subproducers=[JetPtCut],
)
GoodBJets = ProducerGroup(
    name="GoodBJets",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.jet_id_mask, q.jet_puid_mask],
    output=[q.good_bjets_mask],
    scopes=["global"],
    subproducers=[BJetPtCut, BJetEtaCut, BTagCut],
)
GoodNonBJets= ProducerGroup(
    name="GoodNonBJets",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.jet_id_mask, q.jet_puid_mask],
    output=[q.good_nonbjets_mask],
    scopes=["global"],
    subproducers=[NonBJetPtCut, NonBJetEtaCut, BTagAntiCut],
)

####################
# Set of producers to apply a veto of jets overlapping with ditaupair candidates and ordering jets by their pt
# 1. check all jets vs the two lepton candidates, if they are not within deltaR = 0.5, keep them --> mask
# 2. Combine mask with good_jets_mask
# 3. Generate JetCollection, an RVec containing all indices of good Jets in pt order
# 4. generate jet quantity outputs
####################
VetoOverlappingJets = Producer(
    name="VetoOverlappingJets",
    call="jet::VetoOverlappingJets({df}, {output}, {input}, {deltaR_jet_lep_veto})",
    input=[nanoAOD.Jet_eta, nanoAOD.Jet_phi, q.lep_p4, q.lep_p4],
    output=[q.jet_overlap_veto_mask],
    scopes=['lep_iso', 'lep_antiiso']
)

GoodJetsLowPtWithVeto = ProducerGroup(
    name="GoodJetsLowPtWithVeto",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_jetslowpt_mask],
    output=[],
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[VetoOverlappingJets],
)
GoodJetsWithVeto = Producer(
    name="GoodJetsWithVeto",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_jets_mask, q.jet_overlap_veto_mask],
    output=[],
    scopes=['lep_iso', 'lep_antiiso'],
)
GoodBJetsWithVeto = Producer(
    name="GoodBJetsWithVeto",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_bjets_mask, q.jet_overlap_veto_mask],
    output=[],
    scopes=['lep_iso', 'lep_antiiso']
)
GoodNonBJetsWithVeto = Producer(
    name="GoodNonBJetsWithVeto",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.good_nonbjets_mask, q.jet_overlap_veto_mask],
    output=[],
    scopes=['lep_iso', 'lep_antiiso']
)

JetCollection = ProducerGroup(
    name="JetCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    input=[q.Jet_pt_corrected],
    output=[q.good_jet_collection],
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[GoodJetsWithVeto],
)
BJetCollection = ProducerGroup(
    name="BJetCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    input=[q.Jet_pt_corrected],
    output=[q.good_bjet_collection],
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[GoodBJetsWithVeto],
)
NonBJetCollection = ProducerGroup(
    name="NonBJetCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    input=[q.Jet_pt_corrected],
    output=[q.good_nonbjet_collection],
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[GoodNonBJetsWithVeto],
)
JetLowPtCollection = ProducerGroup(
    name="JetLowPtCollection",
    call="jet::OrderJetsByPt({df}, {output}, {input})",
    input=[q.Jet_pt_corrected],
    output=[q.good_jetlowpt_collection],
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[GoodJetsLowPtWithVeto],
)



##########################
# Basic Jet Quantities
# njets, pt, eta, phi, b-tag value
##########################

LVJet1 = Producer(
    name="LVJet1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_jet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.jet_1_p4],
    scopes=['lep_iso', 'lep_antiiso']
)
LVJet2 = Producer(
    name="LVJet2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.good_jet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.jet_2_p4],
    scopes=['lep_iso', 'lep_antiiso']
)
LVJet3 = Producer(
    name="LVJet3",
    call="lorentzvectors::build({df}, {input_vec}, 2, {output})",
    input=[
        q.good_jet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.jet_3_p4],
    scopes=['lep_iso', 'lep_antiiso']
)
NumberOfJets = Producer(
    name="NumberOfJets",
    call="quantities::jet::NumberOfJets({df}, {output}, {input})",
    input=[q.good_jet_collection],
    output=[q.n_jets],
    scopes=['lep_iso', 'lep_antiiso']
)
jpt_1 = Producer(
    name="jpt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.jet_1_p4],
    output=[q.jet_1_pt],
    scopes=['lep_iso', 'lep_antiiso']
)
jpt_2 = Producer(
    name="jpt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.jet_2_p4],
    output=[q.jet_2_pt],
    scopes=['lep_iso', 'lep_antiiso']
)
jpt_3 = Producer(
    name="jpt_3",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.jet_3_p4],
    output=[q.jet_3_pt],
    scopes=['lep_iso', 'lep_antiiso']
)
jeta_1 = Producer(
    name="jeta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.jet_1_p4],
    output=[q.jet_1_eta],
    scopes=['lep_iso', 'lep_antiiso']
)
jeta_2 = Producer(
    name="jeta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.jet_2_p4],
    output=[q.jet_2_eta],
    scopes=['lep_iso', 'lep_antiiso']
)
jeta_3 = Producer(
    name="jeta_3",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.jet_3_p4],
    output=[q.jet_3_eta],
    scopes=['lep_iso', 'lep_antiiso']
)
jphi_1 = Producer(
    name="jphi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.jet_1_p4],
    output=[q.jet_1_phi],
    scopes=['lep_iso', 'lep_antiiso']
)
jphi_2 = Producer(
    name="jphi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.jet_2_p4],
    output=[q.jet_2_phi],
    scopes=['lep_iso', 'lep_antiiso']
)
jphi_3 = Producer(
    name="jphi_3",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.jet_3_p4],
    output=[q.jet_3_phi],
    scopes=['lep_iso', 'lep_antiiso']
)
jmass_1 = Producer(
    name="jmass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.jet_1_p4],
    output=[q.jet_1_mass],
    scopes=['lep_iso', 'lep_antiiso']
)
jmass_2 = Producer(
    name="jmass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.jet_2_p4],
    output=[q.jet_2_mass],
    scopes=['lep_iso', 'lep_antiiso']
)
jmass_3 = Producer(
    name="jmass_3",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.jet_3_p4],
    output=[q.jet_3_mass],
    scopes=['lep_iso', 'lep_antiiso']
)
jtag_value_1 = Producer(
    name="jtag_value_1",
    call="quantities::jet::btagValue({df}, {output}, {input}, 0)",
    input=[nanoAOD.BJet_discriminator, q.good_jet_collection],
    output=[q.jet_1_btag],
    scopes=['lep_iso', 'lep_antiiso']
)
jtag_value_2 = Producer(
    name="jtag_value_2",
    call="quantities::jet::btagValue({df}, {output}, {input}, 1)",
    input=[nanoAOD.BJet_discriminator, q.good_jet_collection],
    output=[q.jet_2_btag],
    scopes=['lep_iso', 'lep_antiiso']
)
jtag_value_3 = Producer(
    name="jtag_value_3",
    call="quantities::jet::btagValue({df}, {output}, {input}, 2)",
    input=[nanoAOD.BJet_discriminator, q.good_jet_collection],
    output=[q.jet_3_btag],
    scopes=['lep_iso', 'lep_antiiso']
)
BasicJetQuantities = ProducerGroup(
    name="BasicJetQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[
        LVJet1,
        LVJet2,
        LVJet3,
        NumberOfJets,
        jpt_1,
        jeta_1,
        jphi_1,
        jmass_1,
        jtag_value_1,
        jpt_2,
        jeta_2,
        jphi_2,
        jmass_2,
        jtag_value_2,
        jpt_3,
        jeta_3,
        jphi_3,
        jmass_3,
        jtag_value_3,
    ],
)

##########################
# Basic b-Jet Quantities
# nbtag, pt, eta, phi, b-tag value
##########################

LVBJet1 = Producer(
    name="LVBJet1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_bjet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.bjet_1_p4],
    scopes=['lep_iso', 'lep_antiiso']
)
LVBJet2 = Producer(
    name="LVBJet2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.good_bjet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.bjet_2_p4],
    scopes=['lep_iso', 'lep_antiiso']
)
NumberOfBJets = Producer(
    name="NumberOfBJets",
    call="quantities::jet::NumberOfJets({df}, {output}, {input})",
    input=[q.good_bjet_collection],
    output=[q.n_bjets],
    scopes=['lep_iso', 'lep_antiiso']
)
bpt_1 = Producer(
    name="bpt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.bjet_1_p4],
    output=[q.bjet_1_pt],
    scopes=['lep_iso', 'lep_antiiso']
)
bpt_2 = Producer(
    name="bpt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.bjet_2_p4],
    output=[q.bjet_2_pt],
    scopes=['lep_iso', 'lep_antiiso']
)
beta_1 = Producer(
    name="beta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.bjet_1_p4],
    output=[q.bjet_1_eta],
    scopes=['lep_iso', 'lep_antiiso']
)
beta_2 = Producer(
    name="beta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.bjet_2_p4],
    output=[q.bjet_2_eta],
    scopes=['lep_iso', 'lep_antiiso']
)
bphi_1 = Producer(
    name="bphi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.bjet_1_p4],
    output=[q.bjet_1_phi],
    scopes=['lep_iso', 'lep_antiiso']
)
bphi_2 = Producer(
    name="bphi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.bjet_2_p4],
    output=[q.bjet_2_phi],
    scopes=['lep_iso', 'lep_antiiso']
)
bmass_1 = Producer(
    name="bmass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.bjet_1_p4],
    output=[q.bjet_1_mass],
    scopes=['lep_iso', 'lep_antiiso']
)
bmass_2 = Producer(
    name="bmass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.bjet_2_p4],
    output=[q.bjet_2_mass],
    scopes=['lep_iso', 'lep_antiiso']
)
btag_value_1 = Producer(
    name="btag_value_1",
    call="quantities::jet::btagValue({df}, {output}, {input}, 0)",
    input=[nanoAOD.BJet_discriminator, q.good_bjet_collection],
    output=[q.bjet_1_btag],
    scopes=['lep_iso', 'lep_antiiso']
)
btag_value_2 = Producer(
    name="btag_value_2",
    call="quantities::jet::btagValue({df}, {output}, {input}, 1)",
    input=[nanoAOD.BJet_discriminator, q.good_bjet_collection],
    output=[q.bjet_2_btag],
    scopes=['lep_iso', 'lep_antiiso']
)
BasicBJetQuantities = ProducerGroup(
    name="BasicBJetQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[
        LVBJet1,
        LVBJet2,
        NumberOfBJets,
        bpt_1,
        beta_1,
        bphi_1,
        bmass_1,
        btag_value_1,
        bpt_2,
        beta_2,
        bphi_2,
        bmass_2,
        btag_value_2,
    ],
)

##########################
# Basic non-b-Jet Quantities
# nbtag, pt, eta, phi, b-tag value
##########################

LVNonBJet1 = Producer(
    name="LVNonBJet1",
    call="lorentzvectors::build({df}, {input_vec}, 0, {output})",
    input=[
        q.good_nonbjet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.nonbjet_1_p4],
    scopes=['lep_iso', 'lep_antiiso']
)
LVNonBJet2 = Producer(
    name="LVNonBJet2",
    call="lorentzvectors::build({df}, {input_vec}, 1, {output})",
    input=[
        q.good_nonbjet_collection,
        q.Jet_pt_corrected,
        nanoAOD.Jet_eta,
        nanoAOD.Jet_phi,
        q.Jet_mass_corrected,
    ],
    output=[q.nonbjet_2_p4],
    scopes=['lep_iso', 'lep_antiiso']
)
NumberOfNonBJets = Producer(
    name="NumberOfNonBJets",
    call="quantities::jet::NumberOfJets({df}, {output}, {input})",
    input=[q.good_nonbjet_collection],
    output=[q.n_nonbjets],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbpt_1 = Producer(
    name="nonbpt_1",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.nonbjet_1_p4],
    output=[q.nonbjet_1_pt],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbpt_2 = Producer(
    name="nonbpt_2",
    call="quantities::pt({df}, {output}, {input})",
    input=[q.nonbjet_2_p4],
    output=[q.nonbjet_2_pt],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbeta_1 = Producer(
    name="nonbeta_1",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.nonbjet_1_p4],
    output=[q.nonbjet_1_eta],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbeta_2 = Producer(
    name="nonbeta_2",
    call="quantities::eta({df}, {output}, {input})",
    input=[q.nonbjet_2_p4],
    output=[q.nonbjet_2_eta],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbphi_1 = Producer(
    name="nonbphi_1",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.nonbjet_1_p4],
    output=[q.nonbjet_1_phi],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbphi_2 = Producer(
    name="nonbphi_2",
    call="quantities::phi({df}, {output}, {input})",
    input=[q.nonbjet_2_p4],
    output=[q.nonbjet_2_phi],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbmass_1 = Producer(
    name="nonbmass_1",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.nonbjet_1_p4],
    output=[q.nonbjet_1_mass],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbmass_2 = Producer(
    name="nonbmass_2",
    call="quantities::mass({df}, {output}, {input})",
    input=[q.nonbjet_2_p4],
    output=[q.nonbjet_2_mass],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbbtag_value_1 = Producer(
    name="nonbtag_value_1",
    call="quantities::jet::btagValue({df}, {output}, {input}, 0)",
    input=[nanoAOD.BJet_discriminator, q.good_nonbjet_collection],
    output=[q.nonbjet_1_btag],
    scopes=['lep_iso', 'lep_antiiso']
)
nonbbtag_value_2 = Producer(
    name="nonbtag_value_2",
    call="quantities::jet::btagValue({df}, {output}, {input}, 1)",
    input=[nanoAOD.BJet_discriminator, q.good_nonbjet_collection],
    output=[q.nonbjet_2_btag],
    scopes=['lep_iso', 'lep_antiiso']
)
BasicNonBJetQuantities = ProducerGroup(
    name="BasicNonBJetQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep_iso', 'lep_antiiso'],
    subproducers=[
        LVNonBJet1,
        LVNonBJet2,
        NumberOfNonBJets,
        nonbpt_1,
        nonbeta_1,
        nonbphi_1,
        nonbmass_1,
        nonbbtag_value_1,
        nonbpt_2,
        nonbeta_2,
        nonbphi_2,
        nonbmass_2,
        nonbbtag_value_2,
    ],
)
