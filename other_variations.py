from code_generation.systematics import SystematicShift
from .producers import scalefactors as scalefactors
#from .producers import pairselection as pairselection
from .producers import muons as muons
from .producers import electrons as electrons
#from .producers import taus as taus
from .producers import event as event

def add_PUVariations(configuration):
    configuration.add_shift(
        SystematicShift(
            name="PUUp",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "up"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        )
    )

    configuration.add_shift(
        SystematicShift(
            name="PUDown",
            scopes=["global"],
            shift_config={
                ("global"): {"PU_reweighting_variation": "down"},
            },
            producers={
                "global": [
                    event.PUweights,
                ],
            },
        )
    )


    return configuration
