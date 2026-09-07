"""Check public guidance and optional cross-repository documentation routes."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# These protect material safety/interpretation details formerly checked against
# duplicate application guides. They belong beside the public text now.
REQUIRED = {
    "getting-started/installation.md": (
        "SHA256SUMS-Windows-",
        "Unknown publisher",
        "Run anyway",
        "15 GiB",
        "5 GiB",
        "Advanced details",
    ),
    "getting-started/macos.md": (
        "SHA256SUMS-macOS-",
        "Privacy & Security",
        "Open Anyway",
        "~/Library/vipp",
        "~/Applications/VIPP.app",
    ),
    "how-to/choose-compute.md": (
        "Add conversion",
        "uint8",
        "uint16",
        "float32",
        "Preserve",
        "Prefer GPU",
        "Strict",
        "fallback",
        "scientific parity",
    ),
    "reference/colocalization-metrics.md": (
        "pearson_any_channel_below_threshold",
        "manders_tm1",
        "experimental_source_aligned_golden_parity_pending",
        "not the shuffled Costes P-value",
    ),
    "reference/racc-index.md": (
        "include_percentile",
        "theta",
        "at least two voxels",
        "RACC-like",
    ),
    "reference/association-metrics.md": (
        "intersection_over_union",
        "centroid_distance_physical",
        "smaller region ID",
        "region_label_id",
    ),
    "reference/skeleton-nodes.md": (
        "Tortuosity",
        "leading",
        "Physical units",
        "Zhang",
        "Lee",
    ),
    "reference/measurement-tables.md": (
        "t_index",
        "label_id",
        "NaN",
        "anisotropic",
        "mesh_status",
    ),
    "reference/intensity-thresholds.md": (
        "65,536",
        "2^53",
        "Explicit values",
        "ImageJ",
        "NaN",
    ),
    "reference/channel-axis-controls.md": (
        "Preserve numeric values",
        "lossy",
        "Thumbnail channel",
    ),
    "how-to/crop-images.md": (
        "QYX",
        "undoable",
        "level-0",
        "origin",
        "channel",
    ),
    "reference/display-settings.md": (
        "0.15.0a1",
        "0.15.0a2",
        "Display settings",
        "Current slice",
        "Entire stack",
        "90 × 55",
        "720 × 440",
    ),
}


def source_for_route(route: str) -> Path:
    route = unquote(route).strip("/")
    page = DOCS / f"{route}.md"
    return page if page.is_file() else DOCS / route / "index.md"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--application-repo", type=Path)
    args = parser.parse_args()
    errors = []
    nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    for relative, terms in REQUIRED.items():
        page = DOCS / relative
        if not page.is_file():
            errors.append(f"Missing public page: {relative}")
            continue
        text = " ".join(page.read_text(encoding="utf-8").split())
        for term in terms:
            if term.casefold() not in text.casefold():
                errors.append(f"{relative}: review missing contract term {term!r}")
        if relative not in nav:
            errors.append(f"Not in navigation: {relative}")

    # Public guidance must not send readers back to a retired local guide.
    retired = (
        "user-guide",
        "quick-start",
        "gpu-guide",
        "io-user-guide",
        "cache-and-memory",
        "operator-tips",
        "measurement-workflows",
        "skeleton-nodes",
        "colocalization-method-notes",
    )
    legacy = re.compile(
        r"https://github\.com/rensutheart/napari-vipp/blob/main/docs/(?:"
        + "|".join(retired)
        + r")\.md"
    )
    for page in DOCS.rglob("*.md"):
        if "releases" not in page.relative_to(DOCS).parts and legacy.search(
            page.read_text(encoding="utf-8")
        ):
            errors.append(f"Retired guide link: {page.relative_to(DOCS)}")

    checked_routes = 0
    if args.application_repo:
        app = args.application_repo.resolve()
        routes = json.loads(
            (app / "docs/public-guide-redirects.json").read_text(encoding="utf-8")
        )
        for name, entry in routes.items():
            for route in entry["pages"].values():
                checked_routes += 1
                if not source_for_route(route).is_file():
                    errors.append(f"{name}: missing manual route {route}")

        for relative in ("README.md", "SUPPORT.md", "CONTRIBUTING.md"):
            text = (app / relative).read_text(encoding="utf-8")
            for url in re.findall(
                r"https://rensutheart\.github\.io/vipp-mkdocs/[^\s)]+", text
            ):
                parsed = urlsplit(url)
                route = parsed.path.removeprefix("/vipp-mkdocs/").split("/", 1)
                if route[0] in {"stable", "nightly"} or re.fullmatch(
                    r"\d+\.\d+\.\d+(?:(?:a|b|rc)\d+)?", route[0]
                ):
                    route = route[1] if len(route) > 1 else ""
                else:
                    route = "/".join(route)
                page = source_for_route(route)
                checked_routes += 1
                if not page.is_file():
                    errors.append(f"{relative}: missing target {url}")
                elif parsed.fragment:
                    html = markdown.markdown(
                        page.read_text(encoding="utf-8"),
                        extensions=["toc", "attr_list"],
                    )
                    if f'id="{unquote(parsed.fragment)}"' not in html:
                        errors.append(f"{relative}: missing anchor {url}")

    if errors:
        print("Manual checks failed:\n" + "\n".join(errors))
        return 1
    print(
        f"Manual checks passed: {len(REQUIRED)} content contracts; "
        f"{checked_routes} application-to-manual routes."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
