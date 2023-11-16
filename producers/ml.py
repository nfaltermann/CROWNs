from ..quantities import output as q
from ..quantities import nanoAOD as nanoAOD
from code_generation.producer import Producer, ProducerGroup



TransformVarMu01 = Producer(
    name="TransformVarMu01",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 1, "f")',
    input=[
        q.pfmet,
    ],
    output=[q.transformed_mu_pfmet],
    scopes=["lep"],
)

TransformVarMu02 = Producer(
    name="TransformVarMu02",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 2, "f")',
    input=[
        q.top_mass,
    ],
    output=[q.transformed_mu_top_mass],
    scopes=["lep"],
)

TransformVarMu03 = Producer(
    name="TransformVarMu03",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 3, "d")',
    input=[
        q.dphi_top_b1,
    ],
    output=[q.transformed_mu_dphi_top_b1],
    scopes=["lep"],
)

TransformVarMu04 = Producer(
    name="TransformVarMu04",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 4, "d")',
    input=[
        q.wolfram,
    ],
    output=[q.transformed_mu_wolfram],
    scopes=["lep"],
)

TransformVarMu05 = Producer(
    name="TransformVarMu05",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 5, "d")',
    input=[
        q.deta_topb2_b1,
    ],
    output=[q.transformed_mu_deta_topb2_b1],
    scopes=["lep"],
)

TransformVarMu06 = Producer(
    name="TransformVarMu06",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 6, "d")',
    input=[
        q.deta_top_sb,
    ],
    output=[q.transformed_mu_deta_top_sb],
    scopes=["lep"],
)

TransformVarMu07 = Producer(
    name="TransformVarMu07",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 7, "d")',
    input=[
        q.dphi_b1_b2,
    ],
    output=[q.transformed_mu_dphi_b1_b2],
    scopes=["lep"],
)

TransformVarMu08 = Producer(
    name="TransformVarMu08",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 8, "f")',
    input=[
        q.lep_pt,
    ],
    output=[q.transformed_mu_lep_pt],
    scopes=["lep"],
)

TransformVarMu09 = Producer(
    name="TransformVarMu09",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 9, "d")',
    input=[
        q.deta_lep_b1,
    ],
    output=[q.transformed_mu_deta_lep_b1],
    scopes=["lep"],
)

TransformVarMu10 = Producer(
    name="TransformVarMu10",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 10, "d")',
    input=[
        q.pt_b1_b2,
    ],
    output=[q.transformed_mu_m_lep_b2],
    scopes=["lep"],
)

TransformVarMu11 = Producer(
    name="TransformVarMu11",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 11, "d")',
    input=[
        q.pt_b1_b2,
    ],
    output=[q.transformed_mu_pt_b1_b2],
    scopes=["lep"],
)

TransformVarMu12 = Producer(
    name="TransformVarMu12",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 12, "d")',
    input=[
        q.costhetastar,
    ],
    output=[q.transformed_mu_costhetastar],
    scopes=["lep"],
)

TransformVarMu13 = Producer(
    name="TransformVarMu13",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 13, "d")',
    input=[
        q.sumht,
    ],
    output=[q.transformed_mu_sumht],
    scopes=["lep"],
)

TransformVarMu14 = Producer(
    name="TransformVarMu14",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 14, "i")',
    input=[
        q.lep_charge,
    ],
    output=[q.transformed_mu_lep_charge],
    scopes=["lep"],
)

TransformVarMu15 = Producer(
    name="TransformVarMu15",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 15, "f")',
    input=[
        q.bjet_1_pt,
    ],
    output=[q.transformed_mu_bjet_1_pt],
    scopes=["lep"],
)

TransformVarMu16 = Producer(
    name="TransformVarMu16",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 16, "f")',
    input=[
        q.bjet_1_eta,
    ],
    output=[q.transformed_mu_bjet_1_eta],
    scopes=["lep"],
)

TransformVarMu17 = Producer(
    name="TransformVarMu17",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 17, "f")',
    input=[
        q.bjet_2_pt,
    ],
    output=[q.transformed_mu_bjet_2_pt],
    scopes=["lep"],
)

TransformVarMu18 = Producer(
    name="TransformVarMu18",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_mu}", 18, "f")',
    input=[
        q.bjet_2_eta,
    ],
    output=[q.transformed_mu_bjet_2_eta],
    scopes=["lep"],
)


TransformVarsMu = ProducerGroup(
    name="TransformVarsMu",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[
        TransformVarMu01,
        TransformVarMu02,
        TransformVarMu03,
        TransformVarMu04,
        TransformVarMu05,
        TransformVarMu06,
        TransformVarMu07,
        TransformVarMu08,
        TransformVarMu09,
        TransformVarMu10,
        TransformVarMu11,
        TransformVarMu12,
        TransformVarMu13,
        TransformVarMu14,
        TransformVarMu15,
        TransformVarMu16,
        TransformVarMu17,
        TransformVarMu18,
    ],
)



TransformVarEl01 = Producer(
    name="TransformVarEl01",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 1, "f")',
    input=[
        q.pfmet,
    ],
    output=[q.transformed_el_pfmet],
    scopes=["lep"],
)

TransformVarEl02 = Producer(
    name="TransformVarEl02",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 2, "f")',
    input=[
        q.top_mass,
    ],
    output=[q.transformed_el_top_mass],
    scopes=["lep"],
)

TransformVarEl03 = Producer(
    name="TransformVarEl03",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 3, "d")',
    input=[
        q.dphi_top_b1,
    ],
    output=[q.transformed_el_dphi_top_b1],
    scopes=["lep"],
)

TransformVarEl04 = Producer(
    name="TransformVarEl04",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 4, "d")',
    input=[
        q.wolfram,
    ],
    output=[q.transformed_el_wolfram],
    scopes=["lep"],
)

TransformVarEl05 = Producer(
    name="TransformVarEl05",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 5, "d")',
    input=[
        q.deta_topb2_b1,
    ],
    output=[q.transformed_el_deta_topb2_b1],
    scopes=["lep"],
)

TransformVarEl06 = Producer(
    name="TransformVarEl06",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 6, "d")',
    input=[
        q.deta_top_sb,
    ],
    output=[q.transformed_el_deta_top_sb],
    scopes=["lep"],
)

TransformVarEl07 = Producer(
    name="TransformVarEl07",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 7, "d")',
    input=[
        q.dphi_b1_b2,
    ],
    output=[q.transformed_el_dphi_b1_b2],
    scopes=["lep"],
)

TransformVarEl08 = Producer(
    name="TransformVarEl08",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 8, "f")',
    input=[
        q.lep_pt,
    ],
    output=[q.transformed_el_lep_pt],
    scopes=["lep"],
)

TransformVarEl09 = Producer(
    name="TransformVarEl09",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 9, "d")',
    input=[
        q.deta_lep_b1,
    ],
    output=[q.transformed_el_deta_lep_b1],
    scopes=["lep"],
)

TransformVarEl10 = Producer(
    name="TransformVarEl10",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 10, "d")',
    input=[
        q.pt_b1_b2,
    ],
    output=[q.transformed_el_m_lep_b2],
    scopes=["lep"],
)

TransformVarEl11 = Producer(
    name="TransformVarEl11",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 11, "d")',
    input=[
        q.pt_b1_b2,
    ],
    output=[q.transformed_el_pt_b1_b2],
    scopes=["lep"],
)

TransformVarEl12 = Producer(
    name="TransformVarEl12",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 12, "d")',
    input=[
        q.costhetastar,
    ],
    output=[q.transformed_el_costhetastar],
    scopes=["lep"],
)

TransformVarEl13 = Producer(
    name="TransformVarEl13",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 13, "d")',
    input=[
        q.sumht,
    ],
    output=[q.transformed_el_sumht],
    scopes=["lep"],
)

TransformVarEl14 = Producer(
    name="TransformVarEl14",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 14, "i")',
    input=[
        q.lep_charge,
    ],
    output=[q.transformed_el_lep_charge],
    scopes=["lep"],
)

TransformVarEl15 = Producer(
    name="TransformVarEl15",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 15, "f")',
    input=[
        q.bjet_1_pt,
    ],
    output=[q.transformed_el_bjet_1_pt],
    scopes=["lep"],
)

TransformVarEl16 = Producer(
    name="TransformVarEl16",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 16, "f")',
    input=[
        q.bjet_1_eta,
    ],
    output=[q.transformed_el_bjet_1_eta],
    scopes=["lep"],
)

TransformVarEl17 = Producer(
    name="TransformVarEl17",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 17, "f")',
    input=[
        q.bjet_2_pt,
    ],
    output=[q.transformed_el_bjet_2_pt],
    scopes=["lep"],
)

TransformVarEl18 = Producer(
    name="TransformVarEl18",
    call='ml::GaussianTransform({df}, {input}, {output}, "{dnn_transformfile_el}", 18, "f")',
    input=[
        q.bjet_2_eta,
    ],
    output=[q.transformed_el_bjet_2_eta],
    scopes=["lep"],
)


TransformVarsEl = ProducerGroup(
    name="TransformVarsEl",
    call=None,
    input=None,
    output=None,
    scopes=['lep'],
    subproducers=[
        TransformVarEl01,
        TransformVarEl02,
        TransformVarEl03,
        TransformVarEl04,
        TransformVarEl05,
        TransformVarEl06,
        TransformVarEl07,
        TransformVarEl08,
        TransformVarEl09,
        TransformVarEl10,
        TransformVarEl11,
        TransformVarEl12,
        TransformVarEl13,
        TransformVarEl14,
        TransformVarEl15,
        TransformVarEl16,
        TransformVarEl17,
        TransformVarEl18,
    ],
)




KerasEvaluateMu = Producer(
    name="KerasEvaluateMu",
    call='ml::sofie::KerasEvaluate({df}, {input_vec}, {output}, "{dnn_modelfile_mu}")',
    input=[
        q.transformed_mu_pfmet,
        q.transformed_mu_top_mass,
        q.transformed_mu_dphi_top_b1,
        q.transformed_mu_wolfram,
        q.transformed_mu_deta_topb2_b1,
        q.transformed_mu_deta_top_sb,
        q.transformed_mu_dphi_b1_b2,
        q.transformed_mu_lep_pt,
        q.transformed_mu_deta_lep_b1,
        q.transformed_mu_m_lep_b2,
        q.transformed_mu_pt_b1_b2,
        q.transformed_mu_costhetastar,
        q.transformed_mu_sumht,
        q.transformed_mu_lep_charge,
        q.transformed_mu_bjet_1_pt,
        q.transformed_mu_bjet_1_eta,
        q.transformed_mu_bjet_2_pt,
        q.transformed_mu_bjet_2_eta,
    ],
    output=[q.dnn_output_mu],
    scopes=["lep"],
)


KerasEvaluateEl = Producer(
    name="KerasEvaluateEl",
    call='ml::sofie::KerasEvaluate({df}, {input_vec}, {output}, "{dnn_modelfile_el}")',
    input=[
        q.transformed_el_pfmet,
        q.transformed_el_top_mass,
        q.transformed_el_dphi_top_b1,
        q.transformed_el_wolfram,
        q.transformed_el_deta_topb2_b1,
        q.transformed_el_deta_top_sb,
        q.transformed_el_dphi_b1_b2,
        q.transformed_el_lep_pt,
        q.transformed_el_deta_lep_b1,
        q.transformed_el_m_lep_b2,
        q.transformed_el_pt_b1_b2,
        q.transformed_el_costhetastar,
        q.transformed_el_sumht,
        q.transformed_el_lep_charge,
        q.transformed_el_bjet_1_pt,
        q.transformed_el_bjet_1_eta,
        q.transformed_el_bjet_2_pt,
        q.transformed_el_bjet_2_eta,
    ],
    output=[q.dnn_output_el],
    scopes=["lep"],
)
