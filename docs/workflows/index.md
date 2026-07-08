# Workflows

These pages describe common analysis patterns. They are not the only possible
graphs; they are starting points that make the main scientific decisions
visible.

| Workflow | Use when |
| --- | --- |
| [Segmentation And Label Cleanup](segmentation-label-cleanup.md) | You need masks, labels, and object IDs. |
| [Object Measurements And Tables](object-measurements-tables.md) | You need morphology, intensity, metadata columns, summaries, or CSV output. |
| [Skeleton And Network Analysis](skeleton-network-analysis.md) | You need curvilinear structure QC and network measurements. |
| [Colocalization And Association](colocalization-association.md) | You need pixel, ROI, object, or label association analysis. |
| [PSF And Deconvolution](psf-deconvolution.md) | You need PSF-aware restoration. |
| [Batch Processing](batch-processing.md) | You need to run a tuned graph over a folder of inputs. |

## Rule Of Thumb

Build and tune the workflow interactively first. Add `Batch Output` nodes only
after the intermediate images, masks, labels, and tables are scientifically
reasonable.

