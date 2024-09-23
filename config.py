from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import electrons as electrons
from .producers import event as event
from .producers import genparticles as genparticles
from .producers import jets as jets
from .producers import met as met
from .producers import ml as ml
from .producers import muons as muons
from .producers import systematics as systematics
#from .producers import taus as taus
from .producers import triggers as triggers
from .producers import topreco as topreco
from .producers import raw_branches as raw_branches
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
from .jet_variations import add_jetVariations
from .qcdiso_variations import add_qcdisoVariations
from .btag_variations import add_btagVariations
from .jec_data import add_jetCorrectionData
from code_generation.configuration import Configuration
from code_generation.modifiers import EraModifier, SampleModifier
from code_generation.rules import AppendProducer, RemoveProducer, ReplaceProducer
from code_generation.systematics import SystematicShift, SystematicShiftByQuantity


def build_config(
    era: str,
    sample: str,
    scopes: List[str],
    shifts: List[str],
    available_sample_types: List[str],
    available_eras: List[str],
    available_scopes: List[str],
):

    configuration = Configuration(
        era,
        sample,
        scopes,
        shifts,
        available_sample_types,
        available_eras,
        available_scopes,
    )

    ######################################################################################
    ##############################        CONFIG     #####################################
    ######################################################################################

    # first add default parameters necessary for all scopes
    configuration.add_config_parameters(
        "global",
        {
            "PU_reweighting_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/LUM/2016preVFP_UL/puWeights.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/LUM/2016postVFP_UL/puWeights.json.gz",
                    "2017": "data/jsonpog-integration/POG/LUM/2017_UL/puWeights.json.gz",
                    "2018": "data/jsonpog-integration/POG/LUM/2018_UL/puWeights.json.gz",
                }
            ),
            "PU_reweighting_era": EraModifier(
                {
                    "2016preVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2016postVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2017": "Collisions17_UltraLegacy_goldenJSON",
                    "2018": "Collisions18_UltraLegacy_goldenJSON",
                }
            ),
            "PU_reweighting_variation": "nominal",
            "golden_json_file": EraModifier(
                {
                    "2016preVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2016postVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2017": "data/golden_json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                    "2018": "data/golden_json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                }
            ),
            "PU_reweighting_file_HLTMu20": EraModifier(
                {
                    "2016preVFP": "payloads/PU_HLTMu20/2016preVFP_UL/puWeights.json.gz",
                    "2016postVFP": "payloads/PU_HLTMu20/2016postVFP_UL/puWeights.json.gz",
                    "2017": "payloads/PU_HLTMu20/2017_UL/puWeights.json.gz",
                    "2018": "payloads/PU_HLTMu20/2018_UL/puWeights.json.gz",
                }
            ),
            "PU_reweighting_era_HLTMu20": EraModifier(
                {
                    "2016preVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2016postVFP": "Collisions16_UltraLegacy_goldenJSON",
                    "2017": "Collisions17_UltraLegacy_goldenJSON",
                    "2018": "Collisions18_UltraLegacy_goldenJSON",
                }
            ),
            "PU_reweighting_variation_HLTMu20": "nominal",
            "golden_json_file": EraModifier(
                {
                    "2016preVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2016postVFP": "data/golden_json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt",
                    "2017": "data/golden_json/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt",
                    "2018": "data/golden_json/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt",
                }
            ),
            "met_filters": EraModifier(
                {
                    "2016preVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        # "Flag_hfNoisyHitsFilter",
                    ],
                    "2016postVFP": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        # "Flag_hfNoisyHitsFilter",
                    ],
                    "2017": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                        # "Flag_hfNoisyHitsFilter",
                    ],
                    "2018": [
                        "Flag_goodVertices",
                        "Flag_globalSuperTightHalo2016Filter",
                        "Flag_HBHENoiseFilter",
                        "Flag_HBHENoiseIsoFilter",
                        "Flag_EcalDeadCellTriggerPrimitiveFilter",
                        "Flag_BadPFMuonFilter",
                        # "Flag_BadPFMuonDzFilter", # only since nanoAODv9 available
                        "Flag_eeBadScFilter",
                        "Flag_ecalBadCalibFilter",
                        # "Flag_hfNoisyHitsFilter",
                    ],
                }
            ),
        },
    )

    configuration.add_config_parameters(
        scopes,
        {
            "deltaR_jet_lep_veto": 0.4,
        },
    )

    ## all scopes MET selection
    configuration.add_config_parameters(
        scopes,
        {
            "propagateLeptons": SampleModifier(
                {"data": False, "embedding": False},
                default=True,
            ),
            "propagateJets": SampleModifier(
                {"data": False, "embedding": False},
                default=True,
            ),
            "recoil_corrections_file": EraModifier(
                {
                    "2016preVFP": "data/recoil_corrections/Type1_PuppiMET_2016.root",
                    "2016postVFP": "data/recoil_corrections/Type1_PuppiMET_2016.root",
                    "2017": "data/recoil_corrections/Type1_PuppiMET_2017.root",
                    "2018": "data/recoil_corrections/Type1_PuppiMET_2018.root",
                }
            ),
            "recoil_systematics_file": EraModifier(
                {
                    "2016preVFP": "data/recoil_corrections/PuppiMETSys_2016.root",
                    "2016postVFP": "data/recoil_corrections/PuppiMETSys_2016.root",
                    "2017": "data/recoil_corrections/PuppiMETSys_2017.root",
                    "2018": "data/recoil_corrections/PuppiMETSys_2018.root",
                }
            ),
            "applyRecoilCorrections": SampleModifier({"wj": True}, default=False),
            "apply_recoil_resolution_systematic": False,
            "apply_recoil_response_systematic": False,
            "recoil_systematic_shift_up": False,
            "recoil_systematic_shift_down": False,
            "min_jetpt_met_propagation": 15,
        },
    )

    configuration.add_config_parameters(
        ["lep"],
        {
            "singlemoun_trigger": EraModifier(
                {
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_mu",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 24,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_mu",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 24,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_mu",
                            "hlt_path": "HLT_IsoMu27",
                            "ptcut": 27,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_single_mu",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 24,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),

        "HLT_Mu20_prescale_file": "payloads/prescale/HLT_Mu20.json"

        },
    )

    ## trigger single ele
    configuration.add_config_parameters(
        ["lep"],
        {
            "singleelectron_trigger": EraModifier(
                {
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_el",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 27,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_el",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 27,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_el",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf_L1DoubleEG",
                            "ptcut": 32,
                            "etacut": 2.5,
                            "filterbit": 10,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2018": [
                        {
                            "flagname": "trg_single_el",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 32,
                            "etacut": 2.5,
                            "filterbit": -1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )

    # muon base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_base_mu_pt": 10.0,
            "max_base_mu_eta": 2.4,
        },
    )

    # muon Rochester corrections
    configuration.add_config_parameters(
        "global",
        {
            "muon_roccor_corrections_file": EraModifier(
                {
                    "2016preVFP": "data/data/RoccoR_files/RoccoR2016aUL.txt",
                    "2016postVFP": "data/data/RoccoR_files/RoccoR2016bUL.txt",
                    "2017": "data/data/RoccoR_files/RoccoR2017UL.txt",
                    "2018": "data/data/RoccoR_files/RoccoR2018UL.txt",
                }
            ),
        },
    )

    # electron base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_base_el_pt": 10.0,
            "max_base_el_eta": 2.5,
            "eb_ee_gap_start": 1.444,
            "eb_ee_gap_end": 1.566,
            "abseta_eb_ee": 1.479,
            "max_dxy_eb": 0.05,
            "max_dz_eb": 0.1,
            "max_dxy_ee": 0.1,
            "max_dz_ee": 0.2,
        },
    )

    # loose lepton base selection:
    configuration.add_config_parameters(
        ['lep'],
        {
            "min_loose_el_pt": 10.0,
            "max_loose_el_eta": 2.5,
            "loose_el_id": "Electron_cutBased",
            "loose_el_id_wp": 2,
            "min_loose_mu_pt": 10.0,
            "max_loose_mu_eta": 2.4,
            "loose_mu_iso": 0.2,
            "loose_mu_id": "Muon_looseId",
        },
    )

    # good lepton selections
    configuration.add_config_parameters(
        ['lep'],
        {
            "min_el_pt": EraModifier(
                {
                    "2016preVFP": 30,
                    "2016postVFP": 30,
                    "2017": 35,
                    "2018": 35,
                }
            ),
            "max_el_eta": 2.5,
            "el_id": "Electron_cutBased",
            "el_id_wp": 4,

            "min_mu_pt": EraModifier(
                {
                    "2016preVFP": 26,
                    "2016postVFP": 26,
                    "2017": 30,
                    "2018": 26,
                }
            ),
            "max_mu_eta": 2.4,
            "mu_id": "Muon_tightId",
            "mu_iso": 0.06,
        },
    )

    # cuts for defining antiiso selection
    configuration.add_config_parameters(
        ['lep'],
        {
            "loose_mu_antiiso": 0.2,
            "mu_antiiso": 0.2,
            "mu_antiiso_max_iso": 1.0,
            "loose_el_antiid": "Electron_cutBased",
            "loose_el_antiid_wp": 2,
            "el_antiid": "Electron_cutBased",
            "el_antiid_wp": 4,
            "el_antiiso": 0.2,
            "el_antiiso_max_iso": 1.0,
            "el_bitmap": "Electron_vidNestedWPBitmap",
        },
    )

    # lepton scale factors configuration
    configuration.add_config_parameters(
        ["lep"],
        {
            "muon_sf_era": EraModifier(
                {
                    "2016preVFP": "2016preVFP_UL",
                    "2016postVFP": "2016postVFP_UL",
                    "2017": "2017_UL",
                    "2018": "2018_UL",
                }
            ),
            "muon_trigger_sf_file": EraModifier(
                {
                    "2016preVFP": "data/custom_top_sf/muon/2016preVFP_UL/trigger_iso_2016preVFP_UL.json.gz",
                    "2016postVFP": "data/custom_top_sf/muon/2016postVFP_UL/trigger_iso_2016postVFP_UL.json.gz",
                    "2017": "data/custom_top_sf/muon/2017_UL/trigger_iso_2017_UL.json.gz",
                    "2018": "data/custom_top_sf/muon/2018_UL/trigger_iso_2018_UL.json.gz",
                }
            ),
            "muon_trigger_sf_file_syst": EraModifier(
                {
                    "2016preVFP": "data/custom_top_sf/muon/2016preVFP_UL/trigger_iso_2016preVFP_UL_combined_syst.json.gz",
                    "2016postVFP": "data/custom_top_sf/muon/2016postVFP_UL/trigger_iso_2016postVFP_UL_combined_syst.json.gz",
                    "2017": "data/custom_top_sf/muon/2017_UL/trigger_iso_2017_UL_combined_syst.json.gz",
                    "2018": "data/custom_top_sf/muon/2018_UL/trigger_iso_2018_UL_combined_syst.json.gz",
                }
            ),
            "muon_trigger_sf_name": EraModifier(
                {
                    "2016preVFP": "NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt",
                    "2016postVFP": "NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt",
                    "2017": "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt",
                    "2018": "NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt",
                }
            ),
            "muon_trigger_sf_name_syst": EraModifier(
                {
                    "2016preVFP": "NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt_combined_syst",
                    "2016postVFP": "NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt_combined_syst",
                    "2017": "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt_combined_syst",
                    "2018": "NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoVeryTight_abseta_pt_combined_syst",
                }
            ),

            "muon_iso_sf_file": EraModifier(
                {
                    "2016preVFP": "data/custom_top_sf/muon/2016preVFP_UL/trigger_iso_2016preVFP_UL.json.gz",
                    "2016postVFP": "data/custom_top_sf/muon/2016postVFP_UL/trigger_iso_2016postVFP_UL.json.gz",
                    "2017": "data/custom_top_sf/muon/2017_UL/trigger_iso_2017_UL.json.gz",
                    "2018": "data/custom_top_sf/muon/2018_UL/trigger_iso_2018_UL.json.gz",
                }
            ),
            "muon_iso_sf_file_syst": EraModifier(
                {
                    "2016preVFP": "data/custom_top_sf/muon/2016preVFP_UL/trigger_iso_2016preVFP_UL_combined_syst.json.gz",
                    "2016postVFP": "data/custom_top_sf/muon/2016postVFP_UL/trigger_iso_2016postVFP_UL_combined_syst.json.gz",
                    "2017": "data/custom_top_sf/muon/2017_UL/trigger_iso_2017_UL_combined_syst.json.gz",
                    "2018": "data/custom_top_sf/muon/2018_UL/trigger_iso_2018_UL_combined_syst.json.gz",
                }
            ),
            "muon_iso_sf_name": "NUM_VeryTightRelIso_DEN_TightIDandIPCut_abseta_pt",
            "muon_iso_sf_name_syst": "NUM_VeryTightRelIso_DEN_TightIDandIPCut_abseta_pt_combined_syst",

            "muon_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/MUO/2016preVFP_UL/muon_Z.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/MUO/2016postVFP_UL/muon_Z.json.gz",
                    "2017": "data/jsonpog-integration/POG/MUO/2017_UL/muon_Z.json.gz",
                    "2018": "data/jsonpog-integration/POG/MUO/2018_UL/muon_Z.json.gz",
                }
            ),
            "muon_id_sf_name": "NUM_TightID_DEN_TrackerMuons",

            "ele_trigger_sf_file": EraModifier(
                {
                    "2016preVFP": "data/custom_top_sf/electron/2016preVFP_UL/trigger_2016preVFP.json.gz",
                    "2016postVFP": "data/custom_top_sf/electron/2016postVFP_UL/trigger_2016postVFP.json.gz",
                    "2017": "data/custom_top_sf/electron/2017_UL/trigger_2017.json.gz",
                    "2018": "data/custom_top_sf/electron/2018_UL/trigger_2018.json.gz",
                }
            ),
            "ele_trigger_sf_file_syst": EraModifier(
                {
                    "2016preVFP": "data/custom_top_sf/electron/2016preVFP_UL/trigger_2016preVFP_syststat.json.gz",
                    "2016postVFP": "data/custom_top_sf/electron/2016postVFP_UL/trigger_2016postVFP_syststat.json.gz",
                    "2017": "data/custom_top_sf/electron/2017_UL/trigger_2017_syststat.json.gz",
                    "2018": "data/custom_top_sf/electron/2018_UL/trigger_2018_syststat.json.gz",
                }
            ),
            "ele_trigger_sf_name": "h2_scaleFactorsEGamma",
            "ele_trigger_sf_name_syst": "h2_uncertaintiesEGamma",

            "ele_sf_era": EraModifier(
                {
                    "2016preVFP": "2016preVFP",
                    "2016postVFP": "2016postVFP",
                    "2017": "2017",
                    "2018": "2018",
                }
            ),
            "ele_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/EGM/2016preVFP_UL/electron.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/EGM/2016postVFP_UL/electron.json.gz",
                    "2017": "data/jsonpog-integration/POG/EGM/2017_UL/electron.json.gz",
                    "2018": "data/jsonpog-integration/POG/EGM/2018_UL/electron.json.gz",
                }
            ),
            "ele_id_sf_name": "UL-Electron-ID-SF",

        },
    )


    # jet base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_jet_lowpt": 30,
            "min_jet_pt": 40,
            "max_jet_eta": 4.7,
            "jet_id": 2,  # default: 2==pass tight ID and fail tightLepVeto
            "jet_puid": EraModifier(
                {
                    "2016preVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2016postVFP": 1,  # 0==fail, 1==pass(loose), 3==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2017": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                    "2018": 4,  # 0==fail, 4==pass(loose), 6==pass(loose,medium), 7==pass(loose,medium,tight)
                }
            ),
            "jet_puid_max_pt": 50,  # recommended to apply puID only for jets below 50 GeV
            "jet_reapplyJES": False,
            "jet_jes_sources": '{""}',
            "jet_jes_shift": 0,
            "jet_jer_shift": '"nom"',  # or '"up"', '"down"'
            "jet_jec_file": EraModifier(
                {
                    "2016preVFP": '"data/jsonpog-integration/POG/JME/2016preVFP_UL/jet_jerc.json.gz"',
                    "2016postVFP": '"data/jsonpog-integration/POG/JME/2016postVFP_UL/jet_jerc.json.gz"',
                    "2017": '"data/jsonpog-integration/POG/JME/2017_UL/jet_jerc.json.gz"',
                    "2018": '"data/jsonpog-integration/POG/JME/2018_UL/jet_jerc.json.gz"',
                }
            ),
            "jet_jer_tag": EraModifier(
                {
                    "2016preVFP": '"Summer20UL16APV_JRV3_MC"',
                    "2016postVFP": '"Summer20UL16_JRV3_MC"',
                    "2017": '"Summer19UL17_JRV2_MC"',
                    "2018": '"Summer19UL18_JRV2_MC"',
                }
            ),
            "jet_jes_tag_data": '""',
            "jet_jes_tag": EraModifier(
                {
                    "2016preVFP": '"Summer19UL16APV_V7_MC"',
                    "2016postVFP": '"Summer19UL16_V7_MC"',
                    "2017": '"Summer19UL17_V5_MC"',
                    "2018": '"Summer19UL18_V5_MC"',
                }
            ),
            "jet_jec_algo": '"AK4PFchs"',
        },
    )
    # bjet base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_bjet_pt": 40,
            "max_bjet_eta": EraModifier(
                {
                    "2016preVFP": 2.4,
                    "2016postVFP": 2.4,
                    "2017": 2.5,
                    "2018": 2.5,
                }
            ),
            "btag_cut": EraModifier(  # medium
                {
                    "2016preVFP":  0.2598,
                    "2016postVFP": 0.2489,
                    "2017": 0.3040,
                    "2018": 0.2783,
                }
            ),
        },
    )
    # bjet scale factors
    configuration.add_config_parameters(
        scopes,
        {
            "btag_sf_file": EraModifier(
                {
                    "2016preVFP": "data/jsonpog-integration/POG/BTV/2016preVFP_UL/btagging.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/BTV/2016postVFP_UL/btagging.json.gz",
                    "2017": "data/jsonpog-integration/POG/BTV/2017_UL/btagging.json.gz",
                    "2018": "data/jsonpog-integration/POG/BTV/2018_UL/btagging.json.gz",
                }
            ),
            "btag_sf_variation": "central",
            "btag_corr_algo_HF": "deepJet_mujets",
            "btag_corr_algo_LF": "deepJet_incl",

            "btag_eff_file" : EraModifier(
                {
                    "2016preVFP": "data/custom_top_sf/btag_eff/2016preVFP_UL/btag_eff_2016preVFP.json.gz",
                    "2016postVFP": "data/custom_top_sf/btag_eff/2016postVFP_UL/btag_eff_2016postVFP.json.gz",
                    "2017": "data/custom_top_sf/btag_eff/2017_UL/btag_eff_2017.json.gz",
                    "2018": "data/custom_top_sf/btag_eff/2018_UL/btag_eff_2018.json.gz",
                }
            ),
            "btag_wp" : "M",

            "btag_eff_type": SampleModifier(
                {
                    "diboson": "ewk",
                    "dy": "ewk",
                    "wjets": "ewk",
                },
                default = "top",
            ),

            "max_bjet_eta_sf": EraModifier(
                {
                    "2016preVFP": 2.4,
                    "2016postVFP": 2.4,
                    "2017": 2.5,
                    "2018": 2.5,
                }
            ),
            "btag_cut": EraModifier(  # medium
                {
                    "2016preVFP":  0.2598,
                    "2016postVFP": 0.2489,
                    "2017": 0.3040,
                    "2018": 0.2783,
                }
            ),
        },
    )


    configuration.add_config_parameters(
        ['lep'],
        {
            "dnn_modelfile_mu": EraModifier(
                {
                    "2016preVFP": "payloads/model/2016preVFP/complete_mu.h5",
                    "2016postVFP": "payloads/model/2016postVFP/complete_mu.h5",
                    "2017": "payloads/model/2017/complete_mu.h5",
                    "2018": "payloads/model/2018/complete_mu.h5",
                }
            ),
            "dnn_modelfile_el": EraModifier(
                {
                    "2016preVFP": "payloads/model/2016preVFP/complete_el.h5",
                    "2016postVFP": "payloads/model/2016postVFP/complete_el.h5",
                    "2017": "payloads/model/2017/complete_el.h5",
                    "2018": "payloads/model/2018/complete_el.h5",
                }
            ),
            "dnn_transformfile_mu": EraModifier(
                {
                    "2016preVFP": "payloads/model/2016preVFP/transformation_mu.csv",
                    "2016postVFP": "payloads/model/2016postVFP/transformation_mu.csv",
                    "2017": "payloads/model/2017/transformation_mu.csv",
                    "2018": "payloads/model/2018/transformation_mu.csv",
                }
            ),
            "dnn_transformfile_el": EraModifier(
                {
                    "2016preVFP": "payloads/model/2016preVFP/transformation_el.csv",
                    "2016postVFP": "payloads/model/2016postVFP/transformation_el.csv",
                    "2017": "payloads/model/2017/transformation_el.csv",
                    "2018": "payloads/model/2018/transformation_el.csv",
                }
            ),
        }
    )

    ###### scope Specifics ######





    ######################################################################################
    ##############################     PRODUCERS     #####################################
    ######################################################################################


    if sample == "data":
        configuration.add_producers(
            "global",
            [
                event.JSONFilter,
            ],
        )


    configuration.add_producers(
        "global",
        [
            event.SampleFlags,
            # event.Lumi,
            # event.npartons,
            event.MetFilter,
            muons.BaseMuons,
            electrons.BaseElectrons,
        ],
    )

    if sample == "data":
        configuration.add_producers(
            "global",
            [
                jets.JetEnergyCorrection_data,
            ],
        )
    else:
        configuration.add_producers(
            "global",
            [
                event.PUweights,
                event.PUweights_up,
                event.PUweights_down,
                event.PUweights_HLTMu20,
                event.PUweights_HLTMu20_up,
                event.PUweights_HLTMu20_down,
                jets.JetEnergyCorrection,
            ],
        )


    configuration.add_producers(
        "global",
        [
            jets.GoodJets,
            jets.GoodBJets,
            jets.GoodNonBJets,
            jets.GoodJetsLowPt,
            met.MetBasics,
        ],
    )


    # common
    configuration.add_producers(
        scopes,
        [
            muons.LooseMuons,
            muons.NumberOfLooseMuons,
            electrons.LooseElectrons,
            electrons.NumberOfLooseElectrons,
            # jets.JetCollection,
            # jets.BasicJetQuantities,
            # jets.BJetCollection,
            # jets.BasicBJetQuantities,
            # scalefactors.btagging_SF,
            # met.MetCorrections,
            # met.PFMetCorrections,
            # pairquantities.DiTauPairMETQuantities,
            # genparticles.GenMatching,
        ],
    )

    # iso and antiiso lep
    configuration.add_producers(
        ['lep'],
        [
            muons.TightMuons,
            muons.NumberOfTightMuons,
            electrons.TightElectrons,
            electrons.NumberOfTightElectrons,

            muons.AntiTightMuons,
            muons.NumberOfAntiTightMuons,
            electrons.AntiTightElectrons,
            electrons.NumberOfAntiTightElectrons,

            topreco.LeptonSelection,
            topreco.LeptonQuantities,

            raw_branches.LeptonAllQuantities,
            #raw_branches.LeptonIsoQuantities,

            triggers.GenerateSingleMuonTriggerFlags,
            triggers.GenerateSingleElectronTriggerFlags,

            # triggers.TriggerObject_filterBits,
            # triggers.TriggerObject_id,
            # triggers.TriggerObject_pt,
            # triggers.TriggerObject_eta,
            # triggers.TriggerObject_phi,

            # scalefactors.leptons,

            # met.PFMetCorrections,

            # scalefactors.btagging_SF,
            # met.MetCorrections,
            # met.PFMetCorrections,
            # pairquantities.DiTauPairMETQuantities,
            # genparticles.GenMatching,
        ],
    )


    # jet and top related
    configuration.add_producers(
        ['lep'],
        [
            jets.JetLowPtCollection,
            jets.JetCollection,
            jets.BJetCollection,
            jets.NonBJetCollection,
        ],
    )

    if sample == "data":
        configuration.add_producers(
            ['lep'],
            [
                # jets.BasicJetQuantitiesData,
                jets.BasicBJetQuantitiesData,
                jets.BasicNonBJetQuantitiesData,
                raw_branches.JetAllQuantities,
            ],
        )
    else:
        configuration.add_producers(
            ['lep'],
            [
                # jets.BasicJetQuantitiesMC,
                jets.BasicBJetQuantitiesMC,
                jets.BasicNonBJetQuantitiesMC,
                raw_branches.JetAllQuantities_w_flav,
            ],
        )



    configuration.add_producers(
        ['lep'],
        [
            met.PFMetCorrections,

            topreco.LeptonicW,
            topreco.LeptonicWQuantities,

            topreco.TopReco,
            topreco.TopRecoQuantities,
            topreco.DNNQuantities,

            #raw_branches.JetAllQuantities_w_flav,

            ml.TransformVarsMu,
            ml.TransformVarsEl,
            ml.KerasEvaluateMu,
            ml.KerasEvaluateEl,
            topreco.CombineDNNOutputs,
        ],
    )

    # prescale values
    if sample == "data":
        configuration.add_producers(
            "lep",
            [
                triggers.PrescaleValues_HLT_Mu20,
            ],
        )

    # top pT for ttbar
    if sample == "ttbar":
        configuration.add_producers(
            "lep",
            [
                topreco.TopPtReweighting,
            ],
        )

    # syst producers
    if sample not in ["data","qcd"]:
        configuration.add_producers(
            "lep",
            [
                systematics.SystPSWeights,
                systematics.SystLHEScaleWeights,
                systematics.SystLHEPdfWeights,
            ],
        )
    if sample != "data":
        configuration.add_producers(
            "lep",
            [
                topreco.LeptonScaleFactors,
                topreco.BTagScaleFactors,
            ],
        )


    ######################################################################################
    ##############################       OUTPUT      #####################################
    ######################################################################################

    configuration.add_outputs(
        scopes,
        [

            nanoAOD.run,
            nanoAOD.luminosityBlock,
            nanoAOD.event,

            q.is_singletop,
            # q.is_single_s,
            # q.is_single_t,
            # q.is_single_tw,
            q.is_ttbar,
            q.is_diboson,
            q.is_dyjets,
            q.is_wjets,
            q.is_qcd,
            q.is_data,
            # q.npartons,
        ],
    )


    ### HLTs
    if era == "2016preVFP" or era == "2016postVFP":
        configuration.add_outputs(
            ['lep'],
            [
                nanoAOD.HLT_IsoMu24,
                nanoAOD.HLT_IsoTkMu24,
                nanoAOD.HLT_Ele27_WPTight_Gsf,
                nanoAOD.HLT_Mu20,
                nanoAOD.HLT_Mu27,
            ],
        )

    if era == "2017":
        configuration.add_outputs(
            ['lep'],
            [
                nanoAOD.HLT_IsoMu24_eta2p1,
                nanoAOD.HLT_IsoMu27,
                nanoAOD.HLT_Ele32_WPTight_Gsf_L1DoubleEG,
                nanoAOD.HLT_Mu20,
                nanoAOD.HLT_Mu27,
            ],
        )

    if era == "2018":
        configuration.add_outputs(
            ['lep'],
            [
                nanoAOD.HLT_IsoMu24,
                nanoAOD.HLT_Ele32_WPTight_Gsf,
                nanoAOD.HLT_Mu20,
                nanoAOD.HLT_Mu27,
            ],
        )

    configuration.add_outputs(
        ['lep'],
        [
            q.n_loose_lep, q.n_loose_mu, q.n_loose_el,
            q.n_tight_lep, q.n_tight_mu, q.n_tight_el,
            q.n_antitight_lep, q.n_antitight_mu, q.n_antitight_el,

            q.lep_is_mu, q.lep_is_el,
            q.lep_pt, q.lep_eta, q.lep_phi, q.lep_mass, q.lep_is_iso, q.lep_charge, q.lep_mu_index, q.lep_el_index,

            triggers.GenerateSingleMuonTriggerFlags.output_group,
            triggers.GenerateSingleElectronTriggerFlags.output_group,
            # q.TriggerObject_filterBits_vector,
            # q.TriggerObject_id_vector,
            # q.TriggerObject_pt_vector,
            # q.TriggerObject_eta_vector,
            # q.TriggerObject_phi_vector,

            q.wlep_pt, q.wlep_eta, q.wlep_phi, q.wlep_mass, q.wlep_mt,

            q.pfmet, q.pfmetphi,

            # q.n_jets,
            # q.jet_1_pt, q.jet_1_eta, q.jet_1_phi, q.jet_1_mass, q.jet_1_btag,
            # q.jet_2_pt, q.jet_2_eta, q.jet_2_phi, q.jet_2_mass, q.jet_2_btag,
            # q.jet_3_pt, q.jet_3_eta, q.jet_3_phi, q.jet_3_mass, q.jet_3_btag,

            q.n_nonbjets,
            q.nonbjet_1_pt, q.nonbjet_1_eta, q.nonbjet_1_phi, q.nonbjet_1_mass, q.nonbjet_1_btag,
            q.nonbjet_2_pt, q.nonbjet_2_eta, q.nonbjet_2_phi, q.nonbjet_2_mass, q.nonbjet_2_btag,

            q.n_bjets,
            q.bjet_1_pt, q.bjet_1_eta, q.bjet_1_phi, q.bjet_1_mass, q.bjet_1_btag,
            q.bjet_2_pt, q.bjet_2_eta, q.bjet_2_phi, q.bjet_2_mass, q.bjet_2_btag,

            q.is_reco,
            q.is_jj, q.is_jjb, q.is_jjbb, q.is_jjjb, q.is_jjjbb,

            q.top_pt, q.top_eta, q.top_phi, q.top_mass,
            q.tb_pt, q.tb_eta, q.tb_phi, q.tb_mass,
            q.sb_pt, q.sb_eta, q.sb_phi, q.sb_mass,

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

            #q.nano_mu_pt, q.nano_mu_eta, q.nano_mu_phi, q.nano_mu_mass, q.nano_mu_iso, q.nano_mu_miniiso, q.nano_mu_tightid,
            #q.nano_mu_iso,
            #q.nano_el_pt, q.nano_el_eta, q.nano_el_phi, q.nano_el_mass, q.nano_el_detasc, q.nano_el_dxy, q.nano_el_dz, q.nano_el_iso, q.nano_el_cutbasedid, q.nano_el_cutbasedidbitmap,
            #q.nano_el_iso,
            #q.nano_jet_pt, q.nano_jet_eta, q.nano_jet_phi, q.nano_jet_mass, q.nano_jet_btag, q.nano_jet_id, q.nano_njet, #q.nano_jet_hadflav,

            nanoAOD.PV_npvs,

            # q.dnn_output_mu,
            # q.dnn_output_el,
            q.dnn_output,

        ],
    )

    # add gen info and weights for everything but data
    if sample != "data":
        configuration.add_outputs(
            ['lep'],
            [
                nanoAOD.genWeight,

                q.puweight,
                q.puweight_up,
                q.puweight_down,
                q.puweight_HLTMu20,
                q.puweight_HLTMu20_up,
                q.puweight_HLTMu20_down,

                q.lep_sf_mu_trigger_nom, q.lep_sf_mu_trigger_up, q.lep_sf_mu_trigger_down,
                q.lep_sf_mu_iso_nom, q.lep_sf_mu_iso_up, q.lep_sf_mu_iso_down,
                q.lep_sf_mu_id_nom, q.lep_sf_mu_id_up, q.lep_sf_mu_id_down,

                q.lep_sf_el_trigger_nom, q.lep_sf_el_trigger_up, q.lep_sf_el_trigger_down,
                q.lep_sf_el_id_nom, q.lep_sf_el_id_up, q.lep_sf_el_id_down,
                q.lep_sf_el_reco_nom, q.lep_sf_el_reco_up, q.lep_sf_el_reco_down,

                q.btag_sf_nom,
                q.btag_sf_HFup_corr, q.btag_sf_HFup_uncorr,
                q.btag_sf_HFdown_corr, q.btag_sf_HFdown_uncorr,
                q.btag_sf_LFup_corr, q.btag_sf_LFup_uncorr,
                q.btag_sf_LFdown_corr, q.btag_sf_LFdown_uncorr,
            
                #q.nano_jet_hadflav,
            ],
        )

    if sample == "ttbar":
        configuration.add_outputs(
            ['lep'],
            [
                q.toppt_weight
            ],
        )


    if sample not in ["data","qcd"]:
        configuration.add_outputs(
            ['lep'],
            [
                q.PSWeight,
                q.LHEScaleWeight,
                q.LHEPdfWeight,
            ],
        )

    if sample == "data":
        configuration.add_outputs(
            ['lep'],
            [
                q.HLT_Mu20_prescale,
            ],
        )


    ## add prefiring
    if era != "2018":
        configuration.add_outputs(
            ['lep'],
            [
                nanoAOD.L1PreFiringWeight_Nom,
                nanoAOD.L1PreFiringWeight_Dn,
                nanoAOD.L1PreFiringWeight_Up,
                nanoAOD.L1PreFiringWeight_ECAL_Nom,
                nanoAOD.L1PreFiringWeight_ECAL_Dn,
                nanoAOD.L1PreFiringWeight_ECAL_Up,
                nanoAOD.L1PreFiringWeight_Muon_Nom,
                nanoAOD.L1PreFiringWeight_Muon_StatDn,
                nanoAOD.L1PreFiringWeight_Muon_StatUp,
                nanoAOD.L1PreFiringWeight_Muon_SystDn,
                nanoAOD.L1PreFiringWeight_Muon_SystUp,

            ],
        )


    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################
    ###########################################################################



    #########################
    # Jet energy resolution and jet energy scale
    #########################
    add_jetVariations(configuration, available_sample_types, era)

    #########################
    # QCD shape variations
    #########################
    add_qcdisoVariations(configuration, available_sample_types, era)

    #########################
    # systs related to leptons
    #########################
    #add_lepVariations(configuration, available_sample_types, era)

    #########################
    # btagging scale factor shape variation
    #########################
    #add_btagVariations(configuration, available_sample_types)

    #########################
    # Jet energy correction for data
    #########################
    add_jetCorrectionData(configuration, era)

    #########################
    # Finalize and validate the configuration
    #########################
    configuration.optimize()
    configuration.validate()
    configuration.report()
    return configuration.expanded_configuration()
