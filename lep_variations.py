from code_generation.systematics import SystematicShift
from .producers import scalefactors as scalefactors
#from .producers import pairselection as pairselection
from .producers import muons as muons
from .producers import electrons as electrons
#from .producers import taus as taus
from .producers import event as event


def add_lepVariations(configuration):
    configuration.add_shift(
        SystematicShift(
            name="MuonIDUp",
            scopes = ["global"],
            shift_config={
                ("global"): {"muon_sf_varation": "systup"},
            },
            producers={
                "global": [
                    scalefactors.Muon_1_ID_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonIDDown",
            scopes = ["global"],
            shift_config={
                ("global"): {"muon_sf_varation": "systdown"},
            },
            producers={
                "global": [
                    scalefactors.Muon_1_ID_SF,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonIsoUp",
            scopes = ["global"],
            shift_config={
                ("global"): {"muon_sf_varation": "systup"},
            },
            producers={
                "global": [
                    scalefactors.Muon_1_Iso_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="MuonIsoDown",
            scopes = ["global"],
            shift_config={
                ("global"): {"muon_sf_varation": "systdown"},
            },
            producers={
                "global": [
                    scalefactors.Muon_1_Iso_SF,
                ],
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="ElectronIDUp",
            scopes = ["global"],
            shift_config={
                ("global"): {"ele_sf_varation": "sfup"},
            },
            producers={
                "global": [
                    scalefactors.Ele_1_IDWPMedium_SF,
                ]
            },
        )
    )
    configuration.add_shift(
        SystematicShift(
            name="ElectronIDDown",
            scopes = ["global"],
            shift_config={
                ("global"): {"ele_sf_varation": "sfdown"},
            },
            producers={
                "global": [
                    scalefactors.Ele_1_IDWPMedium_SF,
                ],
            },
        )
    )


    return configuration
