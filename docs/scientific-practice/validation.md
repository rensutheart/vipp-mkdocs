# Validate a workflow

Validation asks whether a frozen workflow produces sufficiently accurate and
stable outputs for a defined use. Passing software tests shows that code
behaves as specified; it does not establish biological validity for your data.

## Match evidence to the claim

| Claim | Useful evidence |
| --- | --- |
| An operation matches its mathematical definition | Unit tests, analytical phantoms, numerical comparison to a documented reference |
| A file route preserves required information | Round-trip fixtures, metadata assertions, visual inspection of representative real files |
| A segmentation identifies the target | Blinded reference annotations, object/boundary metrics, error taxonomy across representative conditions |
| A measurement is quantitatively accurate | Calibrated phantoms or objects with known dimensions/intensities |
| A workflow is robust | Held-out data across acquisition days, operators, biological conditions, and known artifacts |
| Users can complete a task | Preregistered usability protocol and task evidence—not developer observation alone |

## Build a reference set

Define the unit of analysis and sampling frame. Include ordinary cases and
predefined hard cases. Reference annotations should have documented rules; for
subjective targets, measure agreement between annotators and resolve ambiguous
cases without using the workflow output as the authority.

## Report more than one score

For segmentation consider object detection, splits/merges, pixel overlap,
boundary error, and count/size bias. For measurements examine error across the
range, not only correlation. For spatial association use deterministic
geometries with known overlap/distance before interpreting biological samples.

Always show representative failure cases and uncertainty. Select examples by a
predefined rule or show a balanced range, not only the most attractive field.

## Keep validation independent

Do not use the held-out set to choose parameters. Freeze the workflow and
software environment first. Record any failed items, exclusions, retries, or
manual interventions.

## Read VIPP's own evidence conservatively

The [validation status](../reference/validation-status.md) lists evidence in the
application repository and important gaps. Those checks support software-level
claims; they do not validate a specific biological workflow for you.
