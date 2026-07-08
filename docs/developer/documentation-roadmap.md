# Documentation Roadmap

This roadmap tracks what the MkDocs site needs next.

## Phase 1: Searchable System Manual

Status: started.

Goals:

- clear navigation;
- install and launch pages;
- concept pages;
- workflow pages;
- node-family reference;
- sample and example workflow index;
- troubleshooting pages.

This phase is for expert users who already understand bioimage analysis and
need to get going quickly.

## Phase 2: Screenshot Coverage

Add screenshots for:

- full VIPP widget in napari;
- node palette and search;
- graph canvas with thumbnails;
- selected-node inspector;
- histogram and threshold marker;
- mask and label inspection;
- table preview;
- named tunnels;
- batch dialog;
- each major example workflow.

Screenshots should be generated from stable sample data and workflow JSON files.

## Phase 3: Parameter-Level Node Reference

For each node:

- purpose;
- inputs and outputs;
- parameters;
- 2D/3D behavior;
- metadata behavior;
- common pitfalls;
- example workflow link.

This can be generated partly from `NODE_LIBRARY`, but the warnings and
scientific interpretation should be written by hand.

## Phase 4: Documentation Examples

Add documentation-only examples where a concept needs a very small teaching
case:

- mask versus labels;
- split channel versus split axis;
- 2D versus 3D connected components;
- wrong pixel size and physical measurements;
- label filtering by table property;
- blind pipeline transfer demonstration.

Promote only stable, broadly useful examples into core system examples.

## Phase 5: Training Book

After the system manual is solid, create a separate Quarto training book:

```text
Inspectable Bioimage Analysis with napari-vipp
```

That book can teach concepts more slowly and may later become a formal
publication project.

