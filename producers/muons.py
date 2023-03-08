from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup

####################
# BASE MUONS
####################

BaseMuonPtCut = Producer(
    name="BaseMuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_base_mu_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=["global"],
)
BaseMuonEtaCut = Producer(
    name="BaseMuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_base_mu_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=["global"],
)
BaseMuons = ProducerGroup(
    name="BaseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[],
    output=[q.base_muons_mask],
    scopes=["global"],
    subproducers=[
        BaseMuonPtCut,
        BaseMuonEtaCut,
    ],
)

####################
# LOOSE MUONS
####################

LooseMuonPtCut = Producer(
    name="LooseMuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_loose_mu_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=['lep'],
)
LooseMuonEtaCut = Producer(
    name="LooseMuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_loose_mu_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=['lep'],
)
LooseMuonIDCut = Producer(
    name="MuonIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{loose_mu_id}")',
    input=[],
    output=[],
    scopes=['lep'],
)
LooseMuonIsoCut = Producer(
    name="LooseMuonIsoCut",
    call="physicsobject::muon::CutIsolation({df}, {output}, {input}, {loose_mu_iso})",
    input=[nanoAOD.Muon_iso],
    output=[],
    scopes=['lep'],
)
LooseMuons = ProducerGroup(
    name="LooseMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.loose_muons_mask],
    scopes=['lep'],
    subproducers=[
        LooseMuonPtCut,
        LooseMuonEtaCut,
        LooseMuonIDCut,
        LooseMuonIsoCut,
    ],
)

NumberOfLooseMuons = Producer(
    name="NumberOfLooseMuons",
    call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
    input=[q.loose_muons_mask],
    output=[q.n_loose_mu],
    scopes=['lep'],
)



####################
# TIGHT MUONS
####################

TightMuonPtCut = Producer(
    name="TightMuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_mu_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=['lep'],
)
TightMuonEtaCut = Producer(
    name="TightMuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_mu_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=['lep'],
)
TightMuonIDCut = Producer(
    name="MuonIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{mu_id}")',
    input=[],
    output=[],
    scopes=['lep'],
)
TightMuonIsoCut = Producer(
    name="TightMuonIsoCut",
    call="physicsobject::electron::CutIsolation({df}, {output}, {input}, {mu_iso})",
    input=[nanoAOD.Muon_iso],
    output=[],
    scopes=['lep'],
)
TightMuons = ProducerGroup(
    name="TightMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.loose_muons_mask],
    output=[q.tight_muons_mask],
    scopes=['lep'],
    subproducers=[
        TightMuonPtCut,
        TightMuonEtaCut,
        TightMuonIDCut,
        TightMuonIsoCut,
    ],
)

NumberOfTightMuons = Producer(
    name="NumberOfTightMuons",
    call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
    input=[q.tight_muons_mask],
    output=[q.n_tight_mu],
    scopes=['lep'],
)


####################
# ANTIISO MUONS
####################

# AntiLooseMuonIsoCut = Producer(
#     name="AntiLooseMuonIsoCut",
#     call="physicsobject::muon::AntiCutIsolation({df}, {output}, {input}, {loose_mu_antiiso})",
#     input=[nanoAOD.Muon_iso],
#     output=[],
#     scopes=['lep'],
# )

# AntiLooseMuons = ProducerGroup(
#     name="AntiLooseMuons",
#     call="physicsobject::CombineMasks({df}, {output}, {input})",
#     input=[q.base_muons_mask],
#     output=[q.antiloose_muons_mask],
#     scopes=['lep'],
#     subproducers=[
#         LooseMuonPtCut,
#         LooseMuonEtaCut,
#         AntiLooseMuonIsoCut,
#     ],
# )

# NumberOfAntiLooseMuons = Producer(
#     name="NumberOfAntiLooseMuons",
#     call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
#     input=[q.antiloose_muons_mask],
#     output=[q.n_loose_mu],
#     scopes=['lep'],
# )



AntiTightMuonPtCut = Producer(
    name="AntiTightMuonPtCut",
    call="physicsobject::CutPt({df}, {input}, {output}, {min_mu_pt})",
    input=[nanoAOD.Muon_pt],
    output=[],
    scopes=['lep'],
)
AntiTightMuonEtaCut = Producer(
    name="AntiTightMuonEtaCut",
    call="physicsobject::CutEta({df}, {input}, {output}, {max_mu_eta})",
    input=[nanoAOD.Muon_eta],
    output=[],
    scopes=['lep'],
)
AntiTightMuonIDCut = Producer(
    name="AntiMuonIDCut",
    call='physicsobject::muon::CutID({df}, {output}, "{mu_id}")',
    input=[],
    output=[],
    scopes=['lep'],
)
AntiTightMuonIsoCut = Producer(
    name="AntiTightMuonIsoCut",
    call="physicsobject::muon::AntiCutIsolation({df}, {output}, {input}, {mu_antiiso})",
    input=[nanoAOD.Muon_iso],
    output=[],
    scopes=['lep'],
)
AntiTightMuons = ProducerGroup(
    name="AntiTightMuons",
    call="physicsobject::CombineMasks({df}, {output}, {input})",
    input=[q.base_muons_mask],
    output=[q.antitight_muons_mask],
    scopes=['lep'],
    subproducers=[
        AntiTightMuonPtCut,
        AntiTightMuonEtaCut,
        AntiTightMuonIDCut,
        AntiTightMuonIsoCut,
    ],
)

NumberOfAntiTightMuons = Producer(
    name="NumberOfAntiTightMuons",
    call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
    input=[q.antitight_muons_mask],
    output=[q.n_antitight_mu],
    scopes=['lep'],
)




# NumberOfGoodMuons = Producer(
#     name="NumberOfGoodMuons",
#     call="quantities::NumberOfGoodLeptons({df}, {output}, {input})",
#     input=[q.good_muons_mask],
#     output=[q.nmuons],
#     scopes=["mt", "em", "mm"],
# )
# VetoMuons = Producer(
#     name="VetoMuons",
#     call="physicsobject::VetoCandInMask({df}, {output}, {input}, {muon_index_in_pair})",
#     input=[q.base_muons_mask, q.dileptonpair],
#     output=[q.veto_muons_mask],
#     scopes=["em", "mt", "mm"],
# )
# VetoSecondMuon = Producer(
#     name="VetoSecondMuon",
#     call="physicsobject::VetoCandInMask({df}, {output}, {input}, {second_muon_index_in_pair})",
#     input=[q.veto_muons_mask, q.dileptonpair],
#     output=[q.veto_muons_mask_2],
#     scopes=["mm"],
# )

# ExtraMuonsVeto = Producer(
#     name="ExtraMuonsVeto",
#     call="physicsobject::LeptonVetoFlag({df}, {output}, {input})",
#     input={
#         "mm": [q.veto_muons_mask_2],
#         "em": [q.veto_muons_mask],
#         "et": [q.base_muons_mask],
#         "mt": [q.veto_muons_mask],
#         "tt": [q.base_muons_mask],
#     },
#     output=[q.muon_veto_flag],
#     scopes=["em", "et", "mt", "tt", "mm"],
# )

# ####################
# # Set of producers used for di-muon veto
# ####################

# DiMuonVetoPtCut = Producer(
#     name="DiMuonVetoPtCut",
#     call="physicsobject::CutPt({df}, {input}, {output}, {min_dimuonveto_pt})",
#     input=[nanoAOD.Muon_pt],
#     output=[],
#     scopes=["global"],
# )
# DiMuonVetoIDCut = Producer(
#     name="DiMuonVetoIDCut",
#     call='physicsobject::muon::CutID({df}, {output}, "{dimuonveto_id}")',
#     input=[],
#     output=[],
#     scopes=["global"],
# )
# DiMuonVetoMuons = ProducerGroup(
#     name="DiMuonVetoMuons",
#     call="physicsobject::CombineMasks({df}, {output}, {input})",
#     input=MuonEtaCut.output + MuonDxyCut.output + MuonDzCut.output + MuonIsoCut.output,
#     output=[],
#     scopes=["global"],
#     subproducers=[
#         DiMuonVetoPtCut,
#         DiMuonVetoIDCut,
#     ],
# )
# DiMuonVeto = ProducerGroup(
#     name="DiMuonVeto",
#     call="physicsobject::CheckForDiLeptonPairs({df}, {output}, {input}, {dileptonveto_dR})",
#     input=[
#         nanoAOD.Muon_pt,
#         nanoAOD.Muon_eta,
#         nanoAOD.Muon_phi,
#         nanoAOD.Muon_mass,
#         nanoAOD.Muon_charge,
#     ],
#     output=[q.dimuon_veto],
#     scopes=["global"],
#     subproducers=[DiMuonVetoMuons],
# )
