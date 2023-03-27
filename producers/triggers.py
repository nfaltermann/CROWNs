from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ExtendedVectorProducer

####################
# Set of producers used for trigger flags
####################

GenerateSingleMuonTriggerFlags = ExtendedVectorProducer(
    name="GenerateSingleMuonTriggerFlags",
    call='trigger::GenerateSingleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch} )',
    input=[
        q.lep_p4,
        nanoAOD.TriggerObject_filterBits,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname",
    scope=["lep"],
    vec_config="singlemoun_trigger",
)

GenerateSingleElectronTriggerFlags = ExtendedVectorProducer(
    name="GenerateSingleElectronTriggerFlags",
    call='trigger::GenerateSingleTriggerFlag({df}, {output}, {input}, "{hlt_path}", {ptcut}, {etacut}, {trigger_particle_id}, {filterbit}, {max_deltaR_triggermatch} )',
    input=[
        q.lep_p4,
        nanoAOD.TriggerObject_filterBits,
        nanoAOD.TriggerObject_id,
        nanoAOD.TriggerObject_pt,
        nanoAOD.TriggerObject_eta,
        nanoAOD.TriggerObject_phi,
    ],
    output="flagname",
    scope=["lep"],
    vec_config="singleelectron_trigger",
)



TriggerObject_filterBits = Producer(
    name="TriggerObject_filterBits",
    call="basefunctions::rename<ROOT::RVec<Int_t>>({df}, {input}, {output})",
    input=[nanoAOD.TriggerObject_filterBits],
    output=[q.TriggerObject_filterBits_vector],
    scopes=["lep"],
)

TriggerObject_pt = Producer(
    name="TriggerObject_pt",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.TriggerObject_pt],
    output=[q.TriggerObject_pt_vector],
    scopes=["lep"],
)

TriggerObject_eta = Producer(
    name="TriggerObject_eta",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.TriggerObject_eta],
    output=[q.TriggerObject_eta_vector],
    scopes=["lep"],
)

TriggerObject_phi = Producer(
    name="TriggerObject_phi",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.TriggerObject_phi],
    output=[q.TriggerObject_phi_vector],
    scopes=["lep"],
)

TriggerObject_id = Producer(
    name="TriggerObject_id",
    call="basefunctions::rename<ROOT::RVec<Int_t>>({df}, {input}, {output})",
    input=[nanoAOD.TriggerObject_id],
    output=[q.TriggerObject_id_vector],
    scopes=["lep"],
)

PrescaleValues_HLT_Mu20 = Producer(
    name="PrescaleValues_HLT_Mu20",
    call='trigger::GetPrescaleValues({df}, {output}, {input}, "{HLT_Mu20_prescale_file}")',
    input=[
        nanoAOD.HLT_Mu20,
        nanoAOD.run,
        nanoAOD.luminosityBlock,
    ],
    output=[q.HLT_Mu20_prescale],
    scopes=["lep"],
)
