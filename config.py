from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List

from .producers import electrons as electrons
from .producers import event as event
from .producers import genparticles as genparticles
from .producers import jets as jets
from .producers import met as met
from .producers import muons as muons
#from .producers import pairquantities as pairquantities
#from .producers import pairselection as pairselection
from .producers import scalefactors as scalefactors
#from .producers import taus as taus
from .producers import triggers as triggers
from .producers import topreco as topreco
from .quantities import nanoAOD as nanoAOD
from .quantities import output as q
from .lep_variations import add_lepVariations
from .jet_variations import add_jetVariations
from .btag_variations import add_btagVariations
from .other_variations import add_PUVariations
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
                    "2016preVFP": "data/jsonpog-integration/POG/LUM/2016_preVFP_UL/puWeights.json.gz",
                    "2016postVFP": "data/jsonpog-integration/POG/LUM/2016_postVFP_UL/puWeights.json.gz",
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
                    "2016": "data/recoil_corrections/Type1_PuppiMET_2016.root",
                    "2017": "data/recoil_corrections/Type1_PuppiMET_2017.root",
                    "2018": "data/recoil_corrections/Type1_PuppiMET_2018.root",
                }
            ),
            "recoil_systematics_file": EraModifier(
                {
                    "2016": "data/recoil_corrections/PuppiMETSys_2016.root",
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
        ["lep_iso"],
        {
            "singlemoun_trigger": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_mu24",
                            "hlt_path": "HLT_IsoMu24",
                            "ptcut": 25,
                            "etacut": 2.5,
                            "filterbit": 3,
                            "trigger_particle_id": 13,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                }
            ),
        },
    )

    ## trigger single ele
    configuration.add_config_parameters(
        ["lep_iso"],
        {
            "singleelectron_trigger": EraModifier(
                {
                    "2018": [
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2017": [
                        {
                            "flagname": "trg_single_ele32",
                            "hlt_path": "HLT_Ele32_WPTight_Gsf_L1DoubleEG",
                            "ptcut": 33,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016preVFP": [
                        {
                            "flagname": "trg_single_ele27",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 28,
                            "etacut": 2.1,
                            "filterbit": 1,
                            "trigger_particle_id": 11,
                            "max_deltaR_triggermatch": 0.4,
                        },
                    ],
                    "2016postVFP": [
                        {
                            "flagname": "trg_single_ele27",
                            "hlt_path": "HLT_Ele27_WPTight_Gsf",
                            "ptcut": 28,
                            "etacut": 2.1,
                            "filterbit": 1,
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
    # # electron base selection:
    configuration.add_config_parameters(
        "global",
        {
            "min_base_el_pt": 10.0,
            "max_base_el_eta": 2.5,
        },
    )

    # loose lepton base selection:
    configuration.add_config_parameters(
        ['lep_iso', "lep_antiiso"],
        {
            "min_loose_el_pt": 10.0,
            "max_loose_el_eta": 2.4,
            "loose_el_id": "Electron_cutBased",
            "loose_el_id_wp": 1,
            "min_loose_mu_pt": 10.0,
            "max_loose_mu_eta": 2.4,
            "loose_mu_iso": 0.2,
        },
    )

    # good lepton selections
    configuration.add_config_parameters(
        ['lep_iso', "lep_antiiso"],
        {
            "min_el_pt": EraModifier(
                {
                    "2016preVFP": 20, # TODO
                    "2016postVFP": 20, # TODO
                    "2017": 20, # TODO
                    "2018": 20, # TODO
                }
            ),
            "max_el_eta": 2.4,
            "el_id": "Electron_cutBased",
            "el_id_wp": 4,

            "min_mu_pt": EraModifier(
                {
                    "2016preVFP": 20, # TODO
                    "2016postVFP": 20, # TODO
                    "2017": 20, # TODO
                    "2018": 20, # TODO
                }
            ),
            "max_mu_eta": 2.4,
            "mu_id": "Muon_tightId",
            "mu_iso": 0.06,
        },
    )

    # cuts for defining antiiso selection
    configuration.add_config_parameters(
        ['lep_antiiso'],
        {
            "loose_mu_antiiso": 0.2,
            "mu_antiiso": 0.2,
            "loose_el_antiid": "Electron_cutBased",
            "loose_el_antiid_wp": 1,
            "el_antiid": "Electron_cutBased",
            "el_antiid_wp": 0,
        },
    )

    # jet base selection:
    configuration.add_config_parameters(
        "global",
        {
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
                    "2017": 2.4,
                    "2018": 2.4,
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
            "btag_corr_algo": "deepJet_shape",
        },
    )

    ###### scope Specifics ######



    ######################################################################################
    ##############################     PRODUCERS     #####################################
    ######################################################################################

    configuration.add_producers(
        "global",
        [
            # event.RunLumiEventFilter,
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
                jets.JetEnergyCorrection,
            ],
        )


    configuration.add_producers(
        "global",
        [
            jets.GoodJets,
            jets.GoodBJets,
            jets.GoodNonBJets,
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

    # iso lep
    configuration.add_producers(
        ['lep_iso'],
        [
            muons.TightMuons,
            muons.NumberOfTightMuons,
            electrons.TightElectrons,
            electrons.NumberOfTightElectrons,

            topreco.LeptonSelection,
            topreco.LeptonQuantities,

            # met.PFMetCorrections,

            # scalefactors.btagging_SF,
            # met.MetCorrections,
            # met.PFMetCorrections,
            # pairquantities.DiTauPairMETQuantities,
            # genparticles.GenMatching,
        ],
    )


    # antiiso lep
    configuration.add_producers(
        ['lep_antiiso'],
        [
            muons.AntiTightMuons,
            muons.NumberOfAntiTightMuons,
            electrons.AntiTightElectrons,
            electrons.NumberOfAntiTightElectrons,

            topreco.AntiLeptonSelection,
            topreco.LeptonQuantities,

        ],
    )


    # jet and top related
    configuration.add_producers(
        ['lep_iso', "lep_antiiso"],
        [
            topreco.LeptonicW,
            topreco.LeptonicWQuantities,

            jets.JetCollection,
            jets.BasicJetQuantities,
            jets.BJetCollection,
            jets.BasicBJetQuantities,
            jets.NonBJetCollection,
            jets.BasicNonBJetQuantities,

            topreco.TopReco,
            topreco.TopRecoQuantities,
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

            q.is_single_s,
            q.is_single_t,
            q.is_single_tw,
            q.is_ttbar,
            q.is_diboson,
            q.is_dy,
            q.is_wjets,
            q.is_data,
            # q.npartons,
            # q.puweight,

        ],
    )

    configuration.add_outputs(
        ['lep_iso'],
        [
            q.n_loose_mu, q.n_loose_el,
            q.n_tight_mu, q.n_tight_el,
            q.n_loose_lep, q.n_tight_lep,
        ],
    )

    configuration.add_outputs(
        ["lep_antiiso"],
        [
            q.n_loose_mu, q.n_loose_el,
            q.n_antitight_mu, q.n_antitight_el,
            q.n_loose_lep, q.n_antitight_lep,
        ],
    )

    configuration.add_outputs(
        ['lep_iso', "lep_antiiso"],
        [
            q.lep_is_mu, q.lep_is_el,
            q.lep_pt, q.lep_eta, q.lep_phi, q.lep_mass, q.lep_is_iso,

            q.wlep_pt, q.wlep_eta, q.wlep_phi, q.wlep_mass, q.wlep_mt,

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
            q.is_jjb, q.is_jjbb, q.is_jjjb, q.is_jjjbb,

            q.top_pt, q.top_eta, q.top_phi, q.top_mass,
            q.tb_pt, q.tb_eta, q.tb_phi, q.tb_mass,
            q.sb_pt, q.sb_eta, q.sb_phi, q.sb_mass,


        ],
    )

    # add gen info for everything but data
    if sample != "data":
        configuration.add_outputs(
            ['lep_iso'],
            [
            nanoAOD.genWeight,
            # nanoAOD.nPSWeight,
            # nanoAOD.PSWeight,
            # nanoAOD.nLHEScaleWeight,
            # nanoAOD.LHEScaleWeight,
            # nanoAOD.nLHEPdfWeight,
            # nanoAOD.LHEPdfWeight,
            ],
        )

    ## add prefiring
    if era != "2018":
        configuration.add_outputs(
            ['lep_iso'],
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
    # Pileup Shifts
    #########################
    configuration.add_shift(
        SystematicShift(
            name="PileUpUp",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "up"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample for sample in available_sample_types if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )

    configuration.add_shift(
        SystematicShift(
            name="PileUpDown",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "down"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        ),
        samples=[
            sample for sample in available_sample_types if sample not in ["data", "embedding", "embedding_mc"]
        ],
    )



    #########################
    # Jet energy resolution and jet energy scale
    #########################
    add_jetVariations(configuration, available_sample_types, era)

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
