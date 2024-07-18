from __future__ import annotations  # needed for type annotations in > python 3.7

from typing import List
from code_generation.configuration import Configuration
from code_generation.systematics import SystematicShift
from .producers import electrons as electrons
from .producers import muons as muons


def add_qcdisoVariations(
    configuration: Configuration, available_sample_types: List[str], era: str
):
    #########################
    # nonprompt lepton isolation
    # up: Irel > 0.25
    # down: Irel > 0.15
    # nom: Irel > 0.2 
    #########################
    configuration.add_shift(
        SystematicShift(
            name="QCDIsoMuUncUp",
            shift_config={
                "lep": {"mu_antiiso": 0.25},
            },
            producers={"lep": [muons.LooseMuons, muons.NumberOfLooseMuons, muons.TightMuons, muons.NumberOfTightMuons, muons.AntiTightMuons, muons.NumberOfAntiTightMuons]},
        ),
       #samples=["data"]
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="QCDIsoElUncUp",
            shift_config={
                "lep": {"el_antiiso": 0.25},
            },
            producers={"lep": [electrons.LooseElectrons, electrons.NumberOfLooseElectrons, electrons.TightElectrons, electrons.NumberOfTightElectrons, electrons.AntiTightElectrons, electrons.NumberOfAntiTightElectrons]},
        ),
        #samples=["data"]
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="QCDIsoMuUncDown",
            shift_config={
                "lep": {"mu_antiiso": 0.15, "loose_mu_iso": 0.15},
            },
            producers={"lep": [muons.LooseMuons, muons.NumberOfLooseMuons, muons.TightMuons, muons.NumberOfTightMuons, muons.AntiTightMuons, muons.NumberOfAntiTightMuons]},
        ),
        #samples=["data"]
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["embedding", "embedding_mc"]
        ],
    )
    configuration.add_shift(
        SystematicShift(
            name="QCDIsoElUncDown",
            shift_config={
                "lep": {"el_antiiso": 0.15},
            },
            producers={"lep": [electrons.LooseElectrons, electrons.NumberOfLooseElectrons, electrons.TightElectrons, electrons.NumberOfTightElectrons, electrons.AntiTightElectrons, electrons.NumberOfAntiTightElectrons]},
        ),
        #samples=["data"]
        samples=[
            sample
            for sample in available_sample_types
            if sample not in ["embedding", "embedding_mc"]
        ],
    )


    return configuration
