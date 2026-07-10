# Tune without fooling yourself

Interactive tuning can reveal failures quickly. It can also overfit a workflow
to attractive fields or leak information from the final analysis into method
development.

## Separate development from evaluation

Before tuning, divide representative data by biological unit—not merely by
image tile—into:

- a **development set** used to choose graph structure and parameters;
- a **held-out evaluation set** used only after the workflow is frozen;
- optionally, a **stress set** containing known difficult acquisition or
  artifact conditions.

If multiple images come from one animal, culture, patient, or acquisition,
keep related images in the same partition.

## Tune in causal order

Work from upstream to downstream:

1. Confirm source, axes, channel, and calibration.
2. Tune background/denoising without erasing target structures.
3. Tune threshold or model output against boundaries and missed objects.
4. Tune morphology and object splitting against known failure types.
5. Tune label filtering using biological and acquisition scale.
6. Configure measurements only after labels are acceptable.

Changing several stages together makes it difficult to know which decision
improved or damaged the result.

## Avoid count chasing

Do not tune until the object count matches an expectation unless that
expectation comes from independent ground truth. Inspect false positives,
false negatives, merges, splits, boundaries, and failures across conditions.

Use predefined parameter ranges and stop rules when possible. Save graph
checkpoints before major changes and record why the selected configuration was
preferred.

## Freeze before batch execution

Once the development set is satisfactory:

- save and checksum the workflow;
- record VIPP and dependency versions;
- lock input selection and exclusion rules;
- define outputs and batch naming;
- evaluate without further tuning on the held-out set.

If evaluation prompts a change, describe that change and repeat evaluation on
a genuinely independent set when claims depend on unbiased performance.
