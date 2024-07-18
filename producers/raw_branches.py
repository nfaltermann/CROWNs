from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup


nano_mu_pt = Producer(
    name="nano_mu_pt",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_pt],
    output=[q.nano_mu_pt],
    scopes=['lep'],
)
nano_mu_eta = Producer(
    name="nano_mu_eta",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_eta],
    output=[q.nano_mu_eta],
    scopes=['lep'],
)
nano_mu_phi = Producer(
    name="nano_mu_phi",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_phi],
    output=[q.nano_mu_phi],
    scopes=['lep'],
)
nano_mu_mass = Producer(
    name="nano_mu_mass",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_mass],
    output=[q.nano_mu_mass],
    scopes=['lep'],
)
nano_mu_iso = Producer(
    name="nano_mu_iso",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_iso],
    output=[q.nano_mu_iso],
    scopes=['lep'],
)
nano_mu_miniiso = Producer(
    name="nano_mu_miniiso",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_miniiso],
    output=[q.nano_mu_miniiso],
    scopes=['lep'],
)
nano_mu_tightid = Producer(
    name="nano_mu_tightid",
    call="basefunctions::rename<ROOT::RVec<Bool_t>>({df}, {input}, {output})",
    input=[nanoAOD.Muon_id_tight],
    output=[q.nano_mu_tightid],
    scopes=['lep'],
)
nano_el_pt = Producer(
    name="nano_el_pt",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_pt],
    output=[q.nano_el_pt],
    scopes=['lep'],
)
nano_el_eta = Producer(
    name="nano_el_eta",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_eta],
    output=[q.nano_el_eta],
    scopes=['lep'],
)
nano_el_phi = Producer(
    name="nano_el_phi",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_phi],
    output=[q.nano_el_phi],
    scopes=['lep'],
)
nano_el_mass = Producer(
    name="nano_el_mass",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_mass],
    output=[q.nano_el_mass],
    scopes=['lep'],
)
nano_el_detasc = Producer(
    name="nano_el_detasc",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_deltaEtaSC],
    output=[q.nano_el_detasc],
    scopes=['lep'],
)
nano_el_dxy = Producer(
    name="nano_el_dxy",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_dxy],
    output=[q.nano_el_dxy],
    scopes=['lep'],
)
nano_el_dz = Producer(
    name="nano_el_dz",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_dz],
    output=[q.nano_el_dz],
    scopes=['lep'],
)
nano_el_iso = Producer(
    name="nano_el_iso",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_iso],
    output=[q.nano_el_iso],
    scopes=['lep'],
)
nano_el_cutbasedid = Producer(
    name="nano_el_cutbasedid",
    call="basefunctions::rename<ROOT::RVec<Int_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_IDcutbased],
    output=[q.nano_el_cutbasedid],
    scopes=['lep'],
)

nano_el_cutbasedidbitmap = Producer(
    name="nano_el_cutbasedidbitmap",
    call="basefunctions::rename<ROOT::RVec<Int_t>>({df}, {input}, {output})",
    input=[nanoAOD.Electron_IDcutbasedBitmap],
    output=[q.nano_el_cutbasedidbitmap],
    scopes=['lep'],
)

LeptonAllQuantities = ProducerGroup(
    name="LeptonAllQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[nano_mu_pt, nano_mu_eta, nano_mu_phi, nano_mu_mass, nano_mu_iso, nano_mu_miniiso, nano_mu_tightid,
                  nano_el_pt, nano_el_eta, nano_el_phi, nano_el_mass, nano_el_detasc, nano_el_dxy, nano_el_dz, nano_el_iso, nano_el_cutbasedid, nano_el_cutbasedidbitmap
              ],
)

LeptonIsoQuantities = ProducerGroup(
    name="LeptonIsoQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[nano_mu_iso,
                  nano_el_iso
              ],
)




nano_jet_pt = Producer(
    name="nano_jet_pt",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[q.Jet_pt_corrected],
    output=[q.nano_jet_pt],
    scopes=['lep'],
)
nano_jet_eta = Producer(
    name="nano_jet_eta",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_eta],
    output=[q.nano_jet_eta],
    scopes=['lep'],
)
nano_jet_phi = Producer(
    name="nano_jet_phi",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_phi],
    output=[q.nano_jet_phi],
    scopes=['lep'],
)
nano_jet_mass = Producer(
    name="nano_jet_mass",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[q.Jet_mass_corrected],
    output=[q.nano_jet_mass],
    scopes=['lep'],
)
nano_jet_btag = Producer(
    name="nano_jet_btag",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.BJet_discriminator],
    output=[q.nano_jet_btag],
    scopes=['lep'],
)
nano_jet_id = Producer(
    name="nano_jet_id",
    call="basefunctions::rename<ROOT::RVec<Int_t>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_ID],
    output=[q.nano_jet_id],
    scopes=['lep'],
)

nano_jet_hadflav = Producer(
    name="nano_jet_hadflav",
    call="basefunctions::rename<ROOT::RVec<Int_t>>({df}, {input}, {output})",
    input=[nanoAOD.Jet_flavor],
    output=[q.nano_jet_hadflav],
    scopes=['lep'],
)

nano_njet = Producer(
    name="nano_njet",
    call="basefunctions::rename<ROOT::RVec<Int_t>>({df}, {input}, {output})",
    input=[nanoAOD.nJet],
    output=[q.nano_njet],
    scopes=['lep'],
)

JetAllQuantities = ProducerGroup(
    name="JetAllQuantities",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[nano_jet_pt, nano_jet_eta, nano_jet_phi, nano_jet_mass, nano_jet_btag, nano_jet_id, nano_njet],
)

JetAllQuantities_w_flav = ProducerGroup(
    name="JetAllQuantities_w_flav",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[nano_jet_pt, nano_jet_eta, nano_jet_phi, nano_jet_mass, nano_jet_btag, nano_jet_id, nano_njet, nano_jet_hadflav],
)

