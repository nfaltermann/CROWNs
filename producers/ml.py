from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup



TransformVar01 = Producer(
    name="TransformVar01",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 1, "f")',
    input=[
        q.pfmet,
    ],
    output=[q.transformed_pfmet],
    scopes=["lep"],
)

TransformVar02 = Producer(
    name="TransformVar02",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 2, "f")',
    input=[
        q.top_mass,
    ],
    output=[q.transformed_top_mass],
    scopes=["lep"],
)

TransformVar03 = Producer(
    name="TransformVar03",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 3, "d")',
    input=[
        q.dphi_top_b1,
    ],
    output=[q.transformed_dphi_top_b1],
    scopes=["lep"],
)

TransformVar04 = Producer(
    name="TransformVar04",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 4, "d")',
    input=[
        q.wolfram,
    ],
    output=[q.transformed_wolfram],
    scopes=["lep"],
)

TransformVar05 = Producer(
    name="TransformVar05",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 5, "d")',
    input=[
        q.deta_topb2_b1,
    ],
    output=[q.transformed_deta_topb2_b1],
    scopes=["lep"],
)

TransformVar06 = Producer(
    name="TransformVar06",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 6, "d")',
    input=[
        q.deta_top_sb,
    ],
    output=[q.transformed_deta_top_sb],
    scopes=["lep"],
)

TransformVar07 = Producer(
    name="TransformVar07",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 7, "d")',
    input=[
        q.dphi_b1_b2,
    ],
    output=[q.transformed_dphi_b1_b2],
    scopes=["lep"],
)

TransformVar08 = Producer(
    name="TransformVar08",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 8, "f")',
    input=[
        q.lep_pt,
    ],
    output=[q.transformed_lep_pt],
    scopes=["lep"],
)

TransformVar09 = Producer(
    name="TransformVar09",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 9, "d")',
    input=[
        q.deta_lep_b1,
    ],
    output=[q.transformed_deta_lep_b1],
    scopes=["lep"],
)

TransformVar10 = Producer(
    name="TransformVar10",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 10, "d")',
    input=[
        q.pt_b1_b2,
    ],
    output=[q.transformed_m_lep_b2],
    scopes=["lep"],
)

TransformVar11 = Producer(
    name="TransformVar11",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 11, "d")',
    input=[
        q.pt_b1_b2,
    ],
    output=[q.transformed_pt_b1_b2],
    scopes=["lep"],
)

TransformVar12 = Producer(
    name="TransformVar12",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 12, "d")',
    input=[
        q.costhetastar,
    ],
    output=[q.transformed_costhetastar],
    scopes=["lep"],
)

TransformVar13 = Producer(
    name="TransformVar13",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 13, "d")',
    input=[
        q.sumht,
    ],
    output=[q.transformed_sumht],
    scopes=["lep"],
)

TransformVar14 = Producer(
    name="TransformVar14",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 14, "i")',
    input=[
        q.lep_charge,
    ],
    output=[q.transformed_lep_charge],
    scopes=["lep"],
)

TransformVar15 = Producer(
    name="TransformVar15",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 15, "f")',
    input=[
        q.bjet_1_pt,
    ],
    output=[q.transformed_bjet_1_pt],
    scopes=["lep"],
)

TransformVar16 = Producer(
    name="TransformVar16",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 16, "f")',
    input=[
        q.bjet_1_eta,
    ],
    output=[q.transformed_bjet_1_eta],
    scopes=["lep"],
)

TransformVar17 = Producer(
    name="TransformVar17",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 17, "f")',
    input=[
        q.bjet_2_pt,
    ],
    output=[q.transformed_bjet_2_pt],
    scopes=["lep"],
)

TransformVar18 = Producer(
    name="TransformVar18",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile}", 18, "f")',
    input=[
        q.bjet_2_eta,
    ],
    output=[q.transformed_bjet_2_eta],
    scopes=["lep"],
)


TransformVars = ProducerGroup(
    name="TransformVars",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[
        TransformVar01,
        TransformVar02,
        TransformVar03,
        TransformVar04,
        TransformVar05,
        TransformVar06,
        TransformVar07,
        TransformVar08,
        TransformVar09,
        TransformVar10,
        TransformVar11,
        TransformVar12,
        TransformVar13,
        TransformVar14,
        TransformVar15,
        TransformVar16,
        TransformVar17,
        TransformVar18,
    ],
)



KerasEvaluate = Producer(
    name="KerasEvaluate",
    call='ml::sofie::KerasEvaluate({df}, {input_vec}, {output}, "{dnn_modelfile}")',
    input=[
        q.transformed_pfmet,
        q.transformed_top_mass,
        q.transformed_dphi_top_b1,
        q.transformed_wolfram,
        q.transformed_deta_topb2_b1,
        q.transformed_deta_top_sb,
        q.transformed_dphi_b1_b2,
        q.transformed_lep_pt,
        q.transformed_deta_lep_b1,
        q.transformed_m_lep_b2,
        q.transformed_pt_b1_b2,
        q.transformed_costhetastar,
        q.transformed_sumht,
        q.transformed_lep_charge,
        q.transformed_bjet_1_pt,
        q.transformed_bjet_1_eta,
        q.transformed_bjet_2_pt,
        q.transformed_bjet_2_eta,
    ],
    output=[q.dnn_output],
    scopes=["lep"],
)
