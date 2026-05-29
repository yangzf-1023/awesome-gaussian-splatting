"""Rule-based topic classifier for Gaussian Splatting papers.

Given title + abstract, return one of the predefined topic buckets.
The first matching bucket wins, so order = priority.
Keep this file dependency-free so it stays trivially testable.
"""
from __future__ import annotations

import re
from typing import Iterable

# Each bucket: (display_name, slug, keyword_regex_list)
# Use word-boundary regex to avoid partial matches like "editing" hitting "edit".
TOPICS: list[tuple[str, str, list[str]]] = [
    ("Survey & Benchmark", "survey", [
        r"\bsurvey\b", r"\breview\b", r"\bbenchmark\b", r"\bcomparative study\b",
    ]),
    ("Dynamic / 4D / Streaming", "dynamic-4d", [
        r"\b4d\b", r"\b4dgs\b", r"\bdynamic\b", r"\btemporal\b",
        r"\bdeformable\b", r"\bnon-rigid\b", r"\bstreaming\b", r"\bspacetime\b",
    ]),
    ("Avatar / Human / Face", "avatar-human", [
        r"\bavatar\b", r"\bhuman\b", r"\bbody\b", r"\bface\b", r"\bhead\b",
        r"\bhand\b", r"\bportrait\b", r"\bclothing\b", r"\bgarment\b",
    ]),
    ("Generation / Diffusion", "generation", [
        r"\btext[- ]to[- ]3d\b", r"\bimage[- ]to[- ]3d\b", r"\bgenerative\b",
        r"\bgeneration\b", r"\bdiffusion\b", r"\bscore distillation\b",
        r"\bsds\b", r"\bdreamfusion\b",
    ]),
    ("Editing / Stylization / Watermark", "editing", [
        r"\bediting\b", r"\bstylization\b", r"\bstyle transfer\b",
        r"\binpaint(ing)?\b", r"\bmanipulation\b", r"\bwatermark(ing)?\b",
        r"\bremoval\b",
    ]),
    ("Compression / Compact / Efficient Storage", "compression", [
        r"\bcompression\b", r"\bcompact\b", r"\bquantization\b",
        r"\bpruning\b", r"\bcodec\b", r"\bbitrate\b", r"\bstorage\b",
    ]),
    ("Rendering / Acceleration / Mobile", "rendering", [
        r"\breal[- ]time\b", r"\bmobile\b", r"\bon[- ]device\b",
        r"\blod\b", r"\blevel of detail\b", r"\bantialiasing\b",
        r"\brasteriz(er|ation)\b", r"\bray tracing\b",
    ]),
    ("SLAM / Localization / Mapping", "slam", [
        r"\bslam\b", r"\blocalization\b", r"\bmapping\b", r"\bodometry\b",
        r"\bpose estimation\b",
    ]),
    ("Autonomous Driving / Outdoor", "driving", [
        r"\bdriving\b", r"\bautonomous\b", r"\bstreet\b", r"\burban\b",
        r"\blidar\b", r"\bcity[- ]scale\b", r"\baerial\b",
    ]),
    ("Medical / Surgical", "medical", [
        r"\bmedical\b", r"\bsurgery\b", r"\bsurgical\b", r"\bendoscop(y|ic)\b",
        r"\b(ct|mri|x[- ]ray)\b", r"\banatom(y|ical)\b",
    ]),
    ("Relighting / Material / BRDF", "relighting", [
        r"\brelight(ing)?\b", r"\bbrdf\b", r"\bmaterial\b", r"\blighting\b",
        r"\breflectance\b", r"\binverse rendering\b",
    ]),
    ("Sparse-View / Few-shot / Generalizable", "sparse-view", [
        r"\bsparse[- ]view\b", r"\bfew[- ]shot\b", r"\bsingle[- ]image\b",
        r"\bgeneralizable\b", r"\bfeed[- ]?forward\b",
    ]),
    ("Semantic / Scene Understanding", "semantic", [
        r"\bsemantic\b", r"\bsegmentation\b", r"\bscene graph\b",
        r"\bopen[- ]vocabulary\b", r"\bgrounding\b", r"\blanguage\b",
    ]),
    ("Reconstruction / Geometry", "reconstruction", [
        r"\breconstruction\b", r"\bgeometry\b", r"\bmesh\b", r"\bsurface\b",
        r"\bdepth\b", r"\bphotogrammetr(y|ic)\b",
    ]),
]


def classify(text: str) -> tuple[str, str]:
    """Return (display_name, slug) for the first matching topic, else ('Others', 'others')."""
    t = text.lower()
    for name, slug, patterns in TOPICS:
        for p in patterns:
            if re.search(p, t):
                return name, slug
    return "Others", "others"


def topic_order() -> Iterable[tuple[str, str]]:
    """Ordered iterable of (name, slug) for stable section ordering, with Others last."""
    for name, slug, _ in TOPICS:
        yield name, slug
    yield "Others", "others"
