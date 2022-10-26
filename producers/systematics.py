from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup
from code_generation.producer import ExtendedVectorProducer


SystPSWeights = Producer(
    name="SystPSWeights",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.PSWeight],
    output=[q.PSWeight],
    scopes=["lep_iso"],
)

SystLHEScaleWeights = Producer(
    name="SystLHEScaleWeights",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.LHEScaleWeight],
    output=[q.LHEScaleWeight],
    scopes=["lep_iso"],
)

SystLHEPdfWeights = Producer(
    name="SystLHEPdfWeights",
    call="basefunctions::rename<ROOT::RVec<Float_t>>({df}, {input}, {output})",
    input=[nanoAOD.LHEPdfWeight],
    output=[q.LHEPdfWeight],
    scopes=["lep_iso"],
)
