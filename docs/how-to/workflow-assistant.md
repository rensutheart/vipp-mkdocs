# Plan and revise a workflow

Use the **Workflow assistant** to describe an objective, review ordinary VIPP
nodes, and optionally investigate a few trial results or assess a completed
workflow before drafting a revision. You do not need to write or validate JSON.

!!! warning "Unreleased development prototype"
    This feature is for testing after 0.16.0a4; it is not in that release.
    A valid proposal is a starting recipe, not evidence that it identifies the
    correct biological objects or produces valid measurements.

## Choose where the assistant works

The embedded assistant and an external MCP agent can use the same investigation
tools. Only one agent should control an investigation at a time. Processing
stays in VIPP; a cloud model receives only the approved request and previews.

In **Settings**, choose:

- **ChatGPT / Codex** for VIPP's separate, supported Codex connection.
- **Local model** for a trusted Ollama or local OpenAI-compatible service.
  Investigations can send selected source/result previews. Choose an
  image-capable model for this; a text-only model is rejected rather than
  silently receiving fewer images. Ordinary local text/metadata planning is
  still available with investigation and input previews off. The visible
  **Context tokens (Ollama)** defaults to 16,384; larger allocations can use
  substantially more memory. VIPP does not download or start a model for you.
- **OpenAI API — separately billed** for an explicit model available to your
  API project. Set your API key in an environment variable before starting
  VIPP, then enter only that variable's **name** in settings, not its value.
  Requests use the official OpenAI HTTPS endpoint. API mode uses investigation;
  it is not charged to your included ChatGPT allowance. No API key is saved in
  a workflow or copied from another application.

Both **Include input image previews** and **Assess workflow outputs** start
off. The latter permits trial measurements and result previews and is required
for investigation. Nothing is sent by changing a checkbox or settings.

### Working allowance and continuation

Expand **Working allowance** in Goal to choose active time, tool actions,
model requests/external contexts and cumulative preview bytes. Choose trial
attempts beside **Investigate with trial runs**. Defaults are three trials,
64 actions, 80 requests/contexts, 30 working minutes and 10 MiB of previews.
These are upper limits, not a requirement to spend the whole allowance.

**Pause after this step** waits for the current request or calculation to
settle. **Continue** resumes the same investigation and keeps the original
goal, answers, candidates, evidence and consumed usage. If clarification is
needed, answer it in the paused investigation card. Human pause/review time is
excluded from working time. A time allowance is checked at safe step boundaries;
an in-flight calculation can finish slightly past it. Stop/Close still use
normal cooperative cancellation and do not make incomplete output a result.

At an allowance checkpoint, use **Adjust allowance…** (or **Adjust working
allowance…** during finish review) to approve higher total limits. This does
not reset used work and does not automatically resume. Hard ceilings remain
five trials, 64 actions, 80 requests/contexts, 30 active minutes and 20 MiB of
transmitted previews, with the existing probe, memory and cleanup limits.
Reaching a ceiling is not evidence of success. Stale inputs, changed sharing,
cancellation or unsafe cleanup cannot be repaired by granting allowance.

**Start from the current completed workflow** uses ready cached nodes
downstream of the selected source as the starting candidate, without rerunning
them. Uncalculated, unsupported, private-text or multi-source dependencies must
be resolved first; VIPP does not silently switch to a different starting point.
Trials stay detached. **Add** creates a separate branch. For a tested change to
eligible existing nodes, you can instead
[review in-place changes](#review-changes-to-existing-nodes); nothing replaces
your workflow automatically.

## Prepare the input

In an investigation, the assistant can now inspect small image regions and
test a few processing ideas before spending a complete workflow trial. It can
use up to six such probes, with at most eight processing nodes and four named
outputs per probe. A probe uses an explicit region of the original image (at
most 262,144 input voxels), not a silently resized volume. Its result is a
comparison to consider, not an automatically accepted workflow. The normal
time, action, sharing and resource limits still apply. Goal investigations and
accepted-result refinement use the same tools and continuing agent loop.

Load and calculate an **Image Source** with explicit spatial **Y/X** axes and
correctly identified **Z**, time or channel axes when present. **YX**, **ZYX**
and explicitly described time/channel stacks can be used when the proposed
nodes support them. This testing slice requires a cached, finite NumPy image of at most
**64 MiB**; this is an assistant limit, not VIPP's general image-size limit.
Real floating-point values, up-to-32-bit integer images/labels and Boolean masks
are supported. Complex/object data, wide integers, unresolved axes and lazy or
unavailable images are not. Check axes, colour meaning and calibration; the
assistant does not invent them. Each node's normal metadata checks can still
reject an unsuitable dimension, channel interpretation or physical grid.

Describe what should be identified and how you intend to use the result.
If you want complete 3D masks and differently coloured meshes, explain whether
real cavities should stay open and how the target structures can be identified.
A circle in a slice is not necessarily a sphere. A conservative starting
candidate should follow the observed signal and state its assumptions, not
silently fill holes, cap image-border objects or invent identities/calibration.
If no safe, honest starting draft is possible, clarification is still needed.

If you want a missing or obscured part reconstructed, say that explicitly.
For example: “Continue the wavy band through the centre hidden by the bright
object, rather than around its edge. Keep separate masks that may overlap
there, and identify the reconstructed part as an inference.” This describes
your intended result, not a processing recipe or proof of the hidden shape.

## Set Assistant initiative

In **Goal**, use **Assistant initiative** to choose how much the assistant
decides while drafting. **Use best judgment** is the default.
The compact slider keeps its endpoint labels close to the track. The chosen mode
appears in bold at the start of its explanation below the slider.

| Choice | Drafting approach | Maximum questions per response |
| --- | --- | --- |
| **Ask first** | Ask about consequential ambiguity before choosing object conventions or parameters. Clear, safe requests can proceed directly. | 3 |
| **Balanced** | Prefer a starting candidate with reviewable assumptions; ask when the answer materially changes a safe draft. | 2 |
| **Use best judgment** | Delegate routine choices as explicit assumptions; ask only for a genuine blocker to a safe, honest draft. | 1 |

These question caps are enforced. Use best judgment aims for **zero routine
questions**, not guaranteed zero questions. Review the chosen method,
parameters and assumptions: more initiative does not prove accuracy, complete
masks, biological identity or scientific success. Missing calibration and
unavailable operations cannot be invented. This is a planning preference, not
model reasoning or temperature, and does not send, add or run anything.

## Investigate before choosing a plan

!!! note "Unreleased opt-in investigation"
    **Investigate with trial runs** is separate from ordinary planning and from
    [refining an already added workflow](#try-a-bounded-refinement-series).
    It starts off. A selected candidate is an AI interpretation, not a validated
    segmentation or a guarantee that your goal has been met.

1. In **Goal**, select **Investigate with trial runs** and choose the maximum
   trial attempts, from **1 to 5** (default **3**). Enable **Include input image
   previews** if the assistant may see source pixels. **Assess workflow
   outputs** is required to start an investigation: it permits trial
   measurements and result previews. Source-preview permission remains a
   separate choice. **Review before finishing** starts on for ChatGPT: it pauses
   at a proposed final choice so you can accept it, ask for more work or stop.
   Changing an option or a limit starts nothing.
2. Choose **Start investigation**. This explicitly authorizes bounded node
   discovery, source/result inspection, trial calculations and comparison using
   ordinary existing VIPP nodes, using the selected Codex, local or API provider.
3. Follow the reported actions. Trials are detached from your accepted graph.
   The assistant can scan a compact index of eligible nodes and request several
   exact node contracts together. It records a testable idea and what evidence
   would count against it before a linked trial, then assesses that particular
   result against the evidence it actually received. These records are model
   judgments, not measured truth or independent validation.
   The assistant must name the roles of outputs it wants to compare and select
   a completed candidate explicitly; the last trial is not automatically the
   best. Failed or incomplete attempts are not completed result evidence.
4. If finish review is enabled, [review the proposed finish](#review-a-proposed-finish)
   before accepting its exact completed choice. When a checked final plan is
   ready in **Plans**, review its assumptions,
   result evidence and limitations. **Add to workflow** remains a separate,
   undoable edit without calculation. Choose **Run workflow** separately to
   calculate the accepted graph normally. Trial results do not remove that
   review or grant permission to save files.

The investigation has finite action, model-call, preview-byte and trial budgets
and a maximum of **30 active minutes**. Format repair stays inside these budgets;
it does not start a fresh allowance. The normal request timeout and ordinary
calculation/resource checks still apply. It can stop without a final plan when
evidence, a genuine question, a failure or a budget requires review. Questions
and adjustable allowance limits pause the native session for continuation. Use
**Cancel request** or **Close** to stop; an already sent request cannot be
recalled, and calculation cancellation follows normal safe checkpoints.
Source, workflow, goal, settings or sharing changes invalidate the old authority.

### Review a proposed finish

!!! note "Unreleased finish review"
    **Review before finishing** starts on for investigations and agent
    refinement. The assistant's proposed finish is a preference with evidence
    and limitations, not an automatic acceptance or proof that the goal is met.
    Local and API investigation use the same review boundary.

When the assistant proposes a completed result, review the comparison and its
remaining problems, then choose:

| Choice | What happens |
| --- | --- |
| **Keep improving** | Resume the same bounded investigation, optionally with up to 1,000 characters of feedback about the remaining result. Further tests may address known problems under your original goal, if time, actions, calls and trial attempts remain. |
| **Good enough — review plan** | Accept that exact completed choice as the checked draft for separate **Add to workflow** and **Run workflow**. The stated limitations remain; this is your decision to proceed, not a scientific-quality certificate. |
| **Stop — keep accepted workflow** | End the investigation without changing the accepted workflow. |

With finish review on and a trial limit of **two or more**, VIPP holds one of
those trials back for **Keep improving**, along with room to assess it. For
example, a three-trial limit allows up to two before the first review and one
after you continue. This is part of your selected total, not an extra trial.
A one-trial limit cannot reserve a further test. Time, image and other limits
can still make Keep improving unavailable; the review shows the reason.

Expand **Trial images** to inspect already available PNG views. Check each
candidate/role caption: views can belong to the latest trial, not an older
nominated result. Missing selected-result views are neither rendered here nor
assumed available.

If the proposed choice is the already accepted starting result, Good enough
keeps that workflow rather than adding a duplicate branch.

No model work runs while this review is waiting for your choice, and human
review time is excluded from the active-time allowance. Keep improving does
not reset work: the same notebook, protected starting result, used attempts, calls,
actions and image budget remain. Once a hard work limit is reached, no more
tests or requests can start. You can still accept an already completed,
unchanged result with **Good enough — review plan** after the work deadline;
the source, workflow and sharing authority must still be current.

Known issues need not be dismissed as permanent just because the assistant
proposed stopping. They can motivate further bounded tests, but there is no
promise that every problem is fixable. Nor must the assistant erase limitations
or claim success to finish. Stopping, accepting a partial result and continuing
with the remaining allowance are different choices. Clearing **Review before
finishing** retains the earlier direct-to-checked-draft finish behavior; it does
not raise any limit or enable automatic Add/Run.

### How it keeps evidence in view

In this unreleased ChatGPT continuation, each request has a **bounded working
view**, not the entire conversation and every old result. The complete public
action records, test plans and assessments remain in a session-local notebook.
The assistant can retrieve an earlier exact record or keep a few small records
in its working view. You do not need to manage those records or edit JSON.
This notebook is not a promise that every older note is in every request.
Use an explicit [saved assistant session](#save-and-reopen-an-assistant-session)
to keep supported evidence across a restart; ordinary workflow Save and crash
recovery do not preserve it.

An unreleased refinement gives the latest test measurements and comparison
priority, rather than repeatedly sending a large unchanged starting plan. It
keeps an exact reference to that starting plan, whose full original remains
retrievable, alongside the current plan, relevant node instructions and measured
results. Older starting-plan detail is included only when there is room after
current evidence. This avoids repeatedly looking up the same notes just to review a test.
Protected-region and mesh checks are tied to the actual result being discussed;
remembered claims are not new measurements. If the finite view cannot include
something,
the omission is stated and the original note remains retrievable. This does
not choose settings or a better result for the assistant, and it does not
increase the number of tests or requests allowed.

VIPP can also reuse exact previously generated image views of the source and
current results for comparison, within your sharing choices and the same limits.
Only the actual previews supplied with the current request let the assistant
see those pixels; a record title, old caption or remembered claim is not an image.
Keeping a view does not render or calculate it again. Re-sending it still
uses the same sharing allowance: **seven previews and 2 MiB per request**, plus
the existing overall image budget. Neither input nor output permission is
enabled automatically.

An unreleased matched-assessment update keeps an eligible cached **before/after
pair** in view while the assistant assesses a completed test, even after another
result inspection. Both views must match the named output role, source/grid,
region, slice/view and display policy. If the pair is missing or does not fit,
VIPP states **unavailable** or **omitted**; a pair description is not a substitute
for its two actual images. The same permissions and preview budgets still apply.

The current evidence can also include a measured **mesh topology review** with
before/after counts and explicit warnings. A mesh can have no open boundary
edges while its components or Euler count change, or non-manifold edges and
duplicate faces remain. These diagnostics do not repair the mesh, choose a
better result, certify a simple solid or establish genus, self-intersection
safety or anatomical correctness.

As the existing limits approach, VIPP stops offering new tests and reserves room
for assessing completed tests and an explicit final choice. It can keep the
accepted starting result, choose a tested alternative with honest limitations,
or stop without a final plan. It does not choose the last trial by default or
invent an assessment to finish. The **192 KiB request limit** and the existing
action, model-call, trial and total-time limits are unchanged.

Requested slices, crops and montages are presentation evidence, not resampled
analysis data or complete-volume validation. Numerical regional inspection uses
an explicitly bounded native-grid region and records its population; a view's
crop or projection does not silently choose that measurement region. Source
overlays require source permission as well as output permission. Missing wanted signal, unwanted
foreground, separation and uncertain trade-offs still need independent review;
fewer fragments, smoother meshes or two colours alone do not prove improvement.
An ordinary-node reconstruction can be tested as a hypothesis, but inferred
boundaries or filled values must not be presented as observed anatomy.

## Goal, Discussion and Plans

1. Open **Workflow assistant…** in the three-dot **Workflow actions** menu
   beside **Save**. It opens a separate native window without blocking the
   graph or napari viewer. In **Goal**, choose the **Input image** and describe
   **What would you like to achieve?**
   The compact, bounded goal editor grows modestly with available window space
   and respects your font size.
   Set [Assistant initiative](#set-assistant-initiative) for the drafting style.
   If your goal includes saving results, use **Save outputs** locally: choose
   **Same folder as input** or **Choose folder…**, or leave **Ask me when saving**
   until a Save step needs a destination. See [Save results](#save-results-locally).
2. Use **Settings** to choose Codex, your trusted local model or the no-AI
   example. **Apply** accepts your provider/model edits; **Cancel** discards those
   edits. An explicit browser sign-in is separate and is not undone by Cancel.
   See [Connect the assistant](#connect-the-assistant) below.
3. In Goal's image-understanding choices, **Include input image previews** and
   **Assess workflow outputs** both start off. They are independent: the first
   shares source-image views, while the second makes result assessment available
   after a completed Run. For image-based feedback with ChatGPT, select both.
   Selecting either option sends nothing. Input previews work with Codex and
   image-capable local/API models using investigation. Use
   **Preview what is shared** to inspect the selected slices and metadata.
   The framed preview stays compact for short goals; longer text and images
   scroll. In investigation this is explicitly an **input-only** preview: tool
   history, workflow node types and parameters, measurements and permitted output
   images are additional evidence. Starting from the current completed workflow
   can include eligible cached results; those output images are not displayed in
   this input preview. **Advanced shared-data details** shows the read-only input
   JSON in its own framed area. Opening the preview neither uploads data nor copies
   it to the clipboard.
   Preview generation currently requires a scalar YX/ZYX input. For other
   supported source axes, leave previews off; VIPP does not silently select a
   timepoint or channel for you.
4. Read the sharing notice, then choose **Send goal**. This click approves that
   request, including its bounded validation repair: there is no permission
   checkbox to re-tick. Goal text and metadata go to the stated provider;
   image previews go only when separately enabled. The no-AI choice instead
   offers **Show example plan**, which sends nothing to a model.
   An inline spinner replaces the paper-plane icon while the sending label
   shows planning is in progress. A live elapsed clock shows how long this
   request has been waiting locally, including a bounded repair. Neither the
   clock nor spinner proves the remote model is still working, producing tokens
   or making progress; they are not a completion percentage. **Cancel request**
   remains available. When a
   checked response arrives, the assistant opens
   **Discussion** if it needs clarification, otherwise **Plans**.
5. If **Discussion** opens, review the reply and answer any questions with
   **Send answers**, or explain a change with **Send message**. Discussion uses
   one main scrolling page with open current-question cards, readable answer
   rows and a bounded message box. **Original goal** and **Conversation history**
   start collapsed in compact rows; expand their chevrons to refer back.
   Expanded spacing and header click targets are unchanged. Current questions
   appear in their answer cards without a repeated appendix above them. Full chat and
   draft history is retained, including earlier questions and answers.
   In expanded history, neutral bordered assistant bubbles sit on the left and
   your messages on the right in blue-accent blocks matching the stage tabs.
   Sender labels stay inside their own block. **Assistant’s question** and its referenced text share
   a blue-tinted inset with a blue outline inside your reply; the separate bold
   **Your answer** heading marks your literal submitted answer.
   Free messages stay messages rather than appearing under generated question labels.
   With **Use best judgment**, you may leave clarification fields blank and
   explicitly choose **Send answers** to delegate those choices in a fresh
   draft. Blanks are not recorded as your answers and do not make the current
   question-bearing plan eligible for Add. Genuine blockers may still remain.
   A failed or cancelled request keeps your current answers. You do not need to
   edit JSON.
   These Send actions use the same paper-plane icon and inline sending spinner
   as **Send goal**.
   **Preview what is shared** also works here and includes your currently
   typed, unsent message. Viewing the preview does not send it.
6. In **Plans**, inspect the numbered steps. Expand **Assumptions to check**
   using its chevron to review the complete bullet list before accepting the
   draft. This section starts collapsed; every accepted assumption stays
   unchanged, also in **Advanced details**, draft history and the graph note
   after Add. Current questions and blocking warnings stay prominent, not hidden
   inside these sections.
   From Discussion,
   **View plan** lets you inspect the current draft without sending a request.
   Draft history lets you look back; earlier drafts are read-only. Only the
   latest suitable, checked draft can be added. Choose **Add to workflow** when
   you accept it.
7. Choose **Run workflow** separately after adding. It uses ordinary
   **Calculate all**, with the normal manual-node, compute and resource rules.
   Run does not send results to AI. If you enabled **Assess workflow outputs**,
   continue with [Assess the completed result](#assess-the-completed-result).

Expand **What to check after running** for separate, generic human-review guidance.
It has its own chevron and also starts collapsed:
compare the result with the original for wanted parts and unwanted background;
if making separate masks, look for joined or split structures; for a Z stack,
inspect every slice; if measuring size, check scale, units and partial objects at
the image edge. These prompts are conditional and non-exhaustive, not automatic
validation or new assumptions about your plan. They do not automatically
assess the result or change the saved plan
or its history. Future AI requests ask for everyday explanations of choices,
reasons and checks while preserving uncertainty and caveats; existing model
assumptions are not translated or shortened.

Each stage keeps its action strip visible below scrolling content. Goal pins
**Preview what is shared** and **Send goal**; Discussion pins the preview,
**Send message** and **Send answers** when questions exist. The message box
stays in Discussion's scrolling page and uses a bounded, font-aware height that
grows modestly with available space. Plans keeps **Add to workflow** and
**Run workflow** fixed while its heading, draft selector, review, **Advanced details**, caveat and
refinement controls scroll. Resizing or scrolling does not send, add or run.

The AI sparkle identifies the assistant in its title and workflow-toolbar action.
Full-width numbered tabs highlight your current stage in light and dark themes.
Framed areas separate the input and goal, message composer and plan summary.
Assistant buttons have roomier icon-to-label spacing, including active send
spinners; wording, shortcuts and actions are unchanged.
The navigation row keeps **Back** on the left and **Step … of 3** in the centre;
Discussion offers **View plan** when a draft exists. **Close** sits in the very
bottom strip beside **Planning only · Add and Run are separate actions**, apart
from navigation. Goal initially has no **Next** button: **Send goal** is the
clear next action. Once draft history exists, **Next: Discussion** returns to
your retained discussion without sending or signing in again. Discussion keeps
**View plan**; Plans has no Next. These shortcuts are disabled while planning;
an initial failed request with no draft does not reveal Next. All tabs stay
available for browsing, including empty
states and error details before the first draft.

The tabs, **Back**, **Next: Discussion** and **View plan** only navigate. They
preserve your input,
goal and unsent message; they do not send, add or run anything. Editing the goal or
changing the input/workflow makes earlier plans unusable until a fresh request
is accepted. A blank goal blocks new requests, but history remains readable.
Changing **Assistant initiative** keeps your text, current answers and history,
but cancels an old planning request and revokes stale Add/Run eligibility. Send
explicitly again; moving the slider does not transmit or reuse an old approval.
Source/workflow freshness checks still apply.
After a draft or in-flight request, changing initiative or **Include input image
previews** shows the exact new choice beside **Update plan**. This is a stale-plan
notice, not an AI failure. With no draft or in-flight request, the choice is
informational, without an out-of-date-plan warning.

The retained window alone keeps discussion and draft **text** for the current
application session. **Close** cancels pending requests and revokes Add/Run
permission; retained text is not a usable old input capture. Use
[Session → Save session…](#save-and-reopen-an-assistant-session) to keep a local
conversation and supported investigation evidence across a restart. Keep the
accepted analysis as an ordinary workflow too: these are different files.

The status is checked automatically: green means a valid plan is ready to add;
amber means information or permission is needed; red means it could not be
accepted. Invalid proposals cannot be applied. Validation-feedback automatically
gives the AI one opportunity to repair a rejected response, within the selected
attempt limit. Terminal transport/authentication failures stop instead of retrying
indefinitely. Codex can recover an interrupted connection within the same
request and its original time limit; this does not start another plan attempt.
You can still cancel. A green check is not an accuracy or scientific-success score.

If a request fails before a plan arrives, VIPP says that the objective has not
been assessed; plan checks and automatic repair have not run. Follow the stated
connection or provider action instead of rewriting your goal. **Advanced details**
offers **Copy error details** when a safe error record is available. That button
copies only the error category and codes, not your goal, images or AI response.

### Update or retry a plan

Use the action beside the status message:

| Action | Effect |
| --- | --- |
| **Update plan** | Explicitly request a fresh draft with the current choice, goal and answers. An unsent Discussion message is kept but excluded. |
| **Retry plan**, **Retry answers**, **Retry message** | Send a fresh request after a retryable failure, using the same attempt/repair limit. A message retry uses the currently visible message; after edits it says **Send edited message**. |
| **Answer questions** | Open Discussion without sending when the current mode requires unanswered fields. |
| **Review goal** | Open Goal without sending when the input/workflow needs review; stale assumptions are not reused. |
| **Check connection** | Open Settings for authorization or unsupported model/image choices; it does not send a plan. |
| **Show details** | Open Advanced details for request-format/capability/configuration/protocol problems, not a blind AI repair. |

Update and retry clicks approve a fresh request under the current sharing notice
and image-preview opt-in. Fresh capture follows an explicit Update, Preview or
normal Send action, not changing the option; previewing alone never
uploads it. With unchanged input, updates retain goal and answers, including
allowed blank choices under
Use best judgment. The no-AI choice offers **Refresh example**, not model
transmission. A separate retry never starts automatically, attempt limits are
not raised,
and old invalid-response feedback is not carried into a separate retry.
Busy/cancellation and source-freshness guards still apply. Success clears the
recovery action; updating/retrying does not replace or rerun already-added nodes.
**Add to workflow** and **Run workflow** remain separate, explicit actions on
the latest eligible, checked draft.

Applying adds ordinary nodes as one **Undo** step and does not calculate them.
Save and replay the accepted workflow normally without the model. Changed
sources, goals, provider settings or workflow state invalidate the old plan;
the assistant does not silently apply a late answer to another workflow.
**Cancel request** discards late responses and stops further repair attempts.

### Review changes to existing nodes

This unreleased option changes an eligible existing workflow rather than adding
another branch. It uses a completed alternative that the assistant actually
tested, not an untested suggestion or an older saved draft.

1. Start from **Start from the current completed workflow**, or refine a completed
   result, then review and accept the tested alternative normally.
2. In **Plans**, choose **Review in-place changes…**. Read the old and new settings
   in **Review changes to existing workflow**; **Technical details** is optional.
3. Choose **Apply changes** only if you want those edits. VIPP first saves a
   recovery checkpoint, rechecks the exact workflow/result, then applies the
   whole change as one **Undo** step. If protection or checking fails, no edit
   is applied.
4. Inspect the changed nodes, then calculate when ready. Apply does **not** run
   anything. Affected results need recalculation; unrelated nodes, layout and
   results stay in place. Use **Undo** to revert the whole edit.

This first slice permits parameter edits or a compatible processing-step
replacement with the same connections and output roles. Adding/removing nodes,
rewiring, source/writer edits or an incompatible replacement still require
**Add to workflow** as a separate branch. If the workflow changes after the
trial, request a fresh test rather than applying a stale result. An accepted AI
preference is not proof of scientific improvement.

## Assess the completed result

1. In **Goal**, enable **Assess workflow outputs**. Leave **Include input image
   previews** off if you do not want source pixels shared. For source/result
   visual comparisons with ChatGPT, enable both. With a local model, leave input
   previews off: that connector assesses measurements, not images.
2. Add the checked draft and choose **Run workflow**. Wait for that ordinary run
   to finish successfully. Failed, cancelled, active or changed results cannot
   be assessed as the earlier completed candidate.
3. In **Plans**, choose **Preview results shared**. Review the actual output
   diagnostics and permitted images. This preview sends nothing. It identifies
   the completed run and reports unsupported or omitted outputs rather than
   pretending the assistant saw everything.
4. Choose **Assess results** to send that evidence. The result card separates
   the goal checks, what went wrong, possible changes and what cannot be judged.
   For example, many tiny mask components may suggest noise; a very large
   foreground region may suggest background leakage. These are clues, not proof
   of what the correct structures should be.
5. If useful, choose **Revise using results**. This is a separate request for a
   new draft using your original goal, answers, measured feedback and assessment.
   Review it, then choose **Add to workflow** and **Run workflow** separately.
   The revision has not been calculated or shown to improve anything yet.

In **Manual** mode, you control each request, Add and Run. For a finite series,
use [bounded refinement](#try-a-bounded-refinement-series) below. The assistant
does not keep rerunning without a limit or silently replace your accepted
workflow. Changing the source, graph or cached outputs invalidates old result
evidence; rerun the candidate before assessing again. Cancel remains available.

### Try a bounded refinement series

!!! note "Unreleased shared-agent refinement"
    Codex, local and API modes use the investigation tools to improve a completed accepted
    result. It tests changes separately, rather than adding every trial to your
    workflow. The older fallback series described below is not the native
    application's shared-agent path.

Choose your assistant and trial limit, enable **Assess workflow outputs**
and optionally **Include input image previews**, then add and run a first plan
normally. In **Plans**, choose **Start refinement**. This explicit click allows
up to your selected trial attempts and the **Working allowance** in Goal.
Failed trials count. The accepted result is imported
without another calculation and does not cost a trial.

The assistant can inspect the existing recipe and outputs, test small parameter
changes or a compatible operation replacement, and compare the actual results.
Its starting result stays unchanged. It may keep that result if no tested
alternative is better. **Review before finishing** starts on: when it proposes
a finish, use [Keep improving, Good enough or Stop](#review-a-proposed-finish).
If you accept a different completed candidate, review the checked draft, then
choose **Add to workflow** and **Run workflow** separately.
Editing its expert JSON does not preserve the tested-selection approval.

Its [working notebook](#how-it-keeps-evidence-in-view) keeps complete session-local
records while sharing a bounded current view. The assistant can retrieve notes,
keep a few records or exact image views in view, and reserve its remaining
allowance for assessment and a final choice. Those notes and choices are still
AI interpretations, not measurements or scientific validation. No extra trial
or fresh time allowance follows from retrieving or keeping evidence.

Use **Stop refinement**, **Cancel request** or **Close** at any time. Changed
inputs, accepted results, settings or sharing choices also stop the work; late
replies cannot change the workflow. Model selection and smoother appearance are
not proof of scientific accuracy. Inspect the source, missing or unwanted
foreground, joins and mesh defects yourself.

This Plans entry starts from the assistant's completed normal Run. For an
eligible pre-existing workflow, use **Start from the current completed workflow**
in Goal. Neither entry silently replaces nodes: use separate **Add**, or
explicitly [review a compatible in-place change](#review-changes-to-existing-nodes).

For older integrations without the investigation tools, the legacy bounded
series works as follows (not the current native shared-agent path):

1. In **Goal → Refine using the results**, choose up to **5 additional rounds**.
   The default, **Manual (0)**, keeps every assessment and revision under your
   control. Moving the slider sends nothing and starts no calculations. This
   limit is separate from **Assistant initiative**, which controls questions.
   It limits new calculation **attempts**, not promised improvements or completed
   assessments. Once a new calculation is dispatched, it uses one attempt even
   if it fails. The progress display separates attempts from completed results.
2. Enable **Assess workflow outputs**, then add and run your first checked plan
   normally. For ChatGPT to see the source alongside the results, also enable
   **Include input image previews**. Both choices still start off.
3. After that first run finishes, open **Plans** and choose **Start refinement**.
   Read its notice: this action authorizes the selected assistant to assess,
   draft a revised candidate, add it and run it, within your chosen limit.
   Each successfully completed calculation can receive a new assessment; a
   failed calculation cannot. The loop may assess the first run before revising
   it. [Limited failure repair](#if-a-calculation-fails) is included only when
   eligible and when the same budgets still allow it.
4. Follow the current stage and expand **Result history** to compare reports.
   Up to six recent reports remain visible, including the starting run. Each
   assessment receives the last completed run's measurements and report,
   not its images, so it can explain **improved**, **mixed**, **worse**,
   **unchanged** or **cannot compare** separately from meeting your objective.
   These are AI interpretations, not measured accuracy scores. No automatic
   best-result selector chooses a scientific winner.
   A failed attempt does not replace that comparison: the next completed result
   is compared with the last completed result, not with unqualified partial data.
5. Use **Stop refinement**, **Cancel request** or **Close** to stop. It also
   stops at your round limit, after **30 minutes total**, on a repeated unchanged
   draft, questions, a non-repairable error, insufficient evidence, changed input/settings or
   withdrawn sharing. It may stop because the assistant thinks the goal is met;
   that is an **AI judgment, not scientific validation**. Review the final
   results against your objective and an independent target.

Each run uses ordinary calculation and resource checks. Revised candidates are
added as new branches; earlier successfully completed branches are preserved.
The whole workflow must be eligible: a Save/output-writing node (even disabled),
another source, an external/custom operation or an operation not reviewed for
automatic runs blocks the series. Nothing is silently removed to make it run.
Use manual Add/Run for such plans and [saving](#save-results-locally).

A series allows at most two model requests per selected additional attempt plus one
starting assessment. Each request keeps the selected one-or-two-attempt format
repair limit and its timeout, within the overall deadline. A request already
sent cannot be recalled, and calculation cancellation takes effect at the
executor's normal safe checkpoints. Changing a slider never starts a series.

#### Keep an accepted part during refinement

This unreleased option starts off. Use it after a completed run when a part of
the mask already represents an assumption you want to keep.

1. In **Plans → Improve, run and review**, enable **Keep an accepted part of a
   mask**. Choose the completed mask or labels under **Mask to preserve**.
2. Under **Only within this region**, optionally choose a second mask or labels.
   The protected part is the first mask's existing foreground inside the second
   mask's foreground. Without a second region, the whole existing foreground
   is protected. Positive label IDs mean foreground; individual label identity
   is not protected. Choosing these controls starts no request or calculation.
3. Review the selection, then choose **Start refinement**. The assistant must
   explicitly nominate its revised structure, and VIPP checks that every
   protected foreground voxel remains on the same source grid after calculation.
   Where the plan creates a mesh, the nominated structure must feed its mesh
   rather than exist only as an unused preserved copy.

Changes outside the protected part remain possible. If a revision removes
protected foreground, cannot identify its revised output, or changes the source
or grid, refinement stops rather than accepting it as an improvement. Earlier
completed branches and evidence remain available; an old report is not new Run
authority. VIPP does not silently insert missing pixels, resample a result or
repair a mesh to make this check pass.

The constraint and its permitted display preview share the existing output
permission and seven-image/2 MiB limit; omitted views are disclosed. Source
pixels still need their separate input-preview choice. Preserving an accepted
inference is **not anatomical validation**: it can preserve a mistaken part too,
and it does not prove correct thickness, separation or mesh solidity.

With this protection enabled, a calculation failure stops for review rather
than entering the automatic mesh-failure repair path below. A failed or rejected
candidate does not receive a new completed-result assessment.

### If a calculation fails

VIPP shows the operation that failed and the actual local reason, rather than
calling it a general workflow change. The failed attempt stays in draft/chat
history. **Failed calculations are not assessed**: unfinished or out-of-date data is
not presented as a completed output, and no failed-output previews are sent.

Within a started series, VIPP can request a replacement for a positively
identified problem with a mesh's connections (topology). There are at most **two
failure-repair transitions** per series, still inside the selected calculation
attempt limit, model-request limit and **30-minute total** limit. Repairs do not
reset or enlarge any budget. A failure can exhaust the remaining attempts, so a
repair is not guaranteed even for a recognized problem.

Before requesting the replacement, VIPP checks and undoes only the exact failed
Add that belongs to this series. This prevents that broken branch from being
calculated again alongside the replacement. Earlier completed branches stay
untouched. If ownership, source or workflow checks no longer match, or that
cleanup cannot finish safely, the series stops for you to review; unrelated edits
are not rolled back.

The repair request uses the safe error code, operation and failed recipe, not an
invented result assessment or a raw traceback. It may include input previews
only if **Include input image previews** is enabled. It does not share failed
outputs or reuse old output images as if they came from this failed attempt.
Unknown failures, resource limits, cancellation, changed/out-of-date results,
connection or security problems and file errors stop for manual review instead of triggering
this scientific repair. Strict mesh validity and ordinary resource guards are
not weakened; repair does not silently remove duplicate faces or patch geometry.

The last completed assessment stays available as **history**, not as the failed
run's current result or permission to run an old plan. Earlier completed workflow
branches also remain available for review. "Completed" means the calculation
finished, not that its structures are correct. VIPP does not automatically select
the latest or last completed result as the best one.

### What result evidence means

The first assessment slice supports cached scalar **YX/ZYX** images and selected
mask, label, mesh and numeric table results. It uses at most eight output ports,
including actual mask inputs to final mesh branches. Arrays are limited to
4,000,000 elements, with a 64 MiB detached result budget; mesh-edge summaries
support at most 200,000 triangles. Unsupported, unavailable or excess results
are disclosed, not secretly sampled into a complete-looking assessment. This
slice does not infer a timepoint or channel for you.

In this unreleased continuation, adding **Mesh Morphology** measurements no
longer hides the measured final mesh from feedback. Its actual geometry,
mesh-edge checks and exact input masks remain candidates for sharing alongside
the measurement table, within the same limits. A table is not a substitute for
seeing the mesh; check the sharing preview for any omitted results or views.

Mask occupancy, border contact and connected-component counts describe the full
supported array. Label IDs and mesh display groups mean different things:
one label may contain disconnected pieces, and one mesh group can hold many
separate surfaces. **Two colours do not prove two correctly separated
structures.** Display slices may miss important parts of a volume. Actual mesh
previews use two fixed opposing oblique views, with carried scale and origin
and the actual object colours. They draw the original triangles without
simplification; depth ordering, lighting and transparency are display
approximations. Hidden or tiny surfaces can be missed. These views do not prove
closed surfaces, correct topology, completeness or biological accuracy.

The assistant is asked to weigh the goal's relevant parts separately: wanted
signal that may be missing, unwanted foreground, broken or falsely joined parts,
whether the intended structures remain separate, and mesh quality. **Cleaner
does not necessarily mean closer to your goal**: deleting genuine thin parts can
reduce noise counts, joining objects can reduce the number of fragments, and
surface smoothing can hide features. Added review views do not themselves change
the segmentation. A mesh-only change cannot establish better mask coverage.
These instructions improve the assessment criteria, not the evidence available.
Without an independent target, the model cannot establish how many true parts
were lost or invent an accuracy/overlap score. A mixed trade-off or insufficient
evidence should remain visible rather than being called success.

The model's **Achieved**, **Partly achieved**, **Not achieved** or **Cannot assess**
verdict is an interpretation of that evidence, not independent validation,
biological ground truth or a measured confidence score. Continue to check against
an [independent target](../scientific-practice/validation.md).

## Connect the assistant

The header connection indicator is a status, not a send or sign-in button.
A green check beside **ChatGPT · Connected** reports confirmed sign-in, not
model entitlement, a checked plan or scientific success. Open the **Settings**
gear to change the assistant or model, then **Apply** the change.
These actions do not send a planning request. Changing provider/settings makes
the current draft need a fresh request; earlier text remains for reference.

For **Codex (ChatGPT sign-in)**:

1. Open **Settings** and choose **Sign in with ChatGPT…**, or **Sign in again…**
   to reconnect. This explicit action opens browser sign-in for a separate VIPP
   profile; it does not copy credentials, settings or history from your existing
   Codex chat.
2. Complete sign-in in the browser, then return to Settings. The connection card
   shows progress and updates after sign-in completes.
3. Use **Check connection** if you want to check the status again without
   opening sign-in. An existing VIPP sign-in is also checked when the assistant
   opens. A confirmed sign-in is not a test of model access or image accuracy.

The compact Settings window keeps connection controls separate from optional
technical choices. Expand **Advanced** only to override the model, change
thinking effort or adjust the existing request-attempt/time limits. Expanded
Advanced keeps a continuous card background, with distinct input fields; this
does not change settings or sign-in behavior. Opening
Settings, selecting a provider or expanding Advanced never sends your goal or
images. Signing in does not start planning. **Apply** accepts staged settings;
**Cancel** does not sign out or remove an already completed login. Closing
Settings cancels its pending connection interaction, not other VIPP sessions.

### Repair a connection after a runtime update

If the card says **Connection setup needs an update**, choose **Repair connection
setup** directly in the card. You do not need to edit JSON or configuration files.
VIPP checks that its protected setup is still intact, keeps a backup of its
managed setup files, updates only its compatibility feature settings for the
installed Codex version, then checks the connection again. Your saved sign-in
is left untouched. Repair does not open browser sign-in or send your goal,
images or a planning request. If the resulting status asks you to sign in,
use the separate sign-in button.

**Apply** still controls staged provider/model edits. Repair is an explicit
immediate setup action; **Cancel** does not undo a completed repair.
An interrupted or uncertain repair stays blocked rather than continuing
silently; report the connection details instead of deleting setup files.

If the card instead says **Connection setup needs attention**, VIPP could not
verify that narrow update safely. Sign-in stays paused; **Check connection**
only checks again. Arbitrarily changed, redirected or extra configuration is not
silently reset. **Advanced → Connection details** is for reporting the problem,
not a place where you must edit a fix. Do not delete credentials or change
security settings. No model request is sent while setup is blocked. Codex must
be installed and support the restricted connector.

## Choose the assistant

| Choice | What it does |
| --- | --- |
| **Codex (ChatGPT sign-in)** | Ordinary planning proposes a graph without calculation. Investigation uses the shared guarded tools to inspect and calculate detached trials, with the selected input/output sharing choices. |
| **Local model (Ollama / compatible server)** | Uses your selected running, trusted loopback service. Ordinary planning shares metadata, not image pixels or source file paths; investigation supports the same guarded tools and approved previews with an image-capable model. It does not start, download or install models. |
| **OpenAI API — separately billed** | Uses the shared investigation tools with an explicit available model and your API key environment-variable name. The separate ordinary planning/Assess results actions are not supported by this API adapter. |
| **Example pipeline — no AI** | Demonstrates a fixed bright-object recipe and the add/undo path. It is not a live AI response and does not interpret your goal or inspect image content. |

## What the assistant can draft

The assistant now has authoring contracts for **143 of VIPP's 146 registered
operations**, not just the earlier small selection. It uses the actual node
definitions, connections and parameter help. The three exclusions are **Image
Source**, **Table Source** and **Batch Output**: these need explicit source
selection or the separate batch setup. The assistant should explain such a
boundary rather than saying the operation is missing from VIPP.

It can combine ordinary operations into separate branches and reconnect
their results, rather than only making a short sequence:

- Prepare intensities with smoothing, rescaling, background subtraction or
  non-local-means filtering.
- Create masks with thresholds, combine masks with OR/XOR, and refine them with
  erosion/dilation, binary-outlier removal or small-object removal.
- Label connected objects, separate touching foreground with mask watershed,
  select labels and measure them.
- Combine scalar results into channels or inspect their intensity distributions.
- Select/reorder channels and axes, project images, construct PSFs and propose
  deconvolution, registration, detection or tracking when their inputs permit it.
- Make, combine, colour and measure meshes; analyse skeletons or colocalization;
  combine measurements and make plots.
- Compare arrays with **Review Images**, or add a **Save Image** step with your
  [locally approved destination](#save-results-locally).

A draft can contain up to **64 new nodes, 128 connections and 256 ports**. Dynamic
combinations require every selected input to be connected: mesh combination
permits up to 16 inputs; channel combination and mask OR/XOR permit up to 12.
Exact split-channel/axis and PSF output counts come from connected metadata, not
a guessed default. These limits do not remove the
[input restrictions](#prepare-the-input) or permit arbitrary new source files,
external programs or custom code. A node being available does not mean it suits
your image: normal type, axis, calibration and resource checks still apply.

**Review Images** handles images/masks/labels; mesh overlays use the main napari
viewer. Mesh extraction stays manual and full resolution. **Close at image
border** adds a flat cap where the image ends; it does not recover the missing
part of a real object. **Leave open** makes no such outside-image assumption.
Combining meshes collects them; it does not weld or union them.
Broader node access does not mean the assistant has assessed the calculated
result or achieved your objective. Add, Run, optional assessment and human review
remain separate.

## Save results locally

1. In **Goal**, choose a folder under **Save outputs** if you want the workflow to
   save results. **Same folder as input** requires exactly one verified physical
   input file or OME-Zarr store. You can also answer a saving question with the exact
   phrase **use the same folder as input**.
2. For a sample, live image or multi-file input, choose **Choose folder…**
   yourself. This applies even when all input files share one folder.
   VIPP does not turn a display name into a path or
   guess a folder. An unresolved saving destination blocks the plan until you
   choose one; it does not silently omit the Save step.
3. Review the proposed Save step and format. The actual folder stays on your
   computer; the model sees only that a destination was selected and the
   placeholder `USER_OUTPUT_DIRECTORY`. Avoid typing private paths into other
   goal/message text.
4. Choose **Add to workflow**, then **Run workflow** separately. Send, the sharing
   preview and Add do not save files. The approved writer uses an explicit
   format and cannot overwrite an existing file. Normal calculation, format,
   calibration and resource checks still apply.

Changing the output folder makes the old plan need a fresh check/request; it
does not grant a model filesystem access. Saved accepted workflows retain their
ordinary local saving settings, independently of the model conversation.

## Save and reopen an assistant session

This unreleased **Session…** menu keeps the conversation separately from the
workflow JSON. It does not start work again just because you reopen VIPP.

1. If an investigation is running, choose **Pause after this step** and wait for
   the current request/calculation to finish. Then choose **Session… → Save
   session…** and a local `.vipp-session` file.
2. Read the local-data notice before saving. The file keeps the goal, discussion,
   drafts and supported retained investigation evidence, which can include
   source/result arrays and image previews. Treat it as sensitively as the
   original images. It contains no sign-in credentials and is not uploaded.
3. After restarting, open the Workflow assistant and choose **Session… → Open
   session…**. This replaces the displayed conversation, not the workflow.
   Opening performs no calculation or AI request, leaves image/output sharing
   off, and shows saved drafts as history—not permission to Add or Run them.
4. To continue, select the original input/workflow, reconnect your assistant if
   needed, and explicitly choose the saved input/output sharing options again.
   Choose **Session… → Resume saved investigation…** and confirm. VIPP checks
   the source, calibration, original graph, compute choices, supported evidence
   and operation contracts before preparing a paused continuation.
5. Review its remaining allowance and any pending question or finish decision,
   then use the offered **Continue** or review action when ready. Used trials,
   requests, actions, preview bytes and active time are retained; reopening does
   not give a fresh budget.

If the saved session cannot be safely continued, its history remains available
with a reason. Changed inputs/goal/processing contracts, unsupported evidence,
stopped sessions or exhausted hard limits cannot be repaired by reopening.
Start a new investigation deliberately if you need different inputs or sharing
choices. A live external connection and earlier image/evidence transmission
permissions are never restored from the file.

Ordinary [workflow recovery](save-share-export.md#recover-interrupted-workflows)
only restores graph working copies; it does not automatically recover or resume
this assistant conversation. Save the session explicitly before closing VIPP.

## Know what is shared

The input-image option sends at most seven display-only PNG slice/orthogonal
previews, not the entire stack. Captions disclose slice selection, grayscale
range and any integer-stride display sampling. They do not represent every voxel
or establish that a proposed segmentation works. Scientific image buffers are
unchanged. Source file paths, source names, acquisition history and the existing
workflow are not automatically transmitted.

With **Assess workflow outputs**, a separate explicit **Assess results** request
shares the completed candidate's topology/parameters, source grid and numeric
summary, selected output diagnostics and, for Codex, bounded output images.
Result PNGs use a shared limit of seven previews and 2 MiB, not seven images per
output. Captions disclose their slices, palettes, range and display sampling.
Source pixels, including intensity backgrounds in mask overlays, require the
separate **Include input image previews** choice. Without it, output masks can
still be shown on a plain background. Meshes contribute geometry summaries and
their actual upstream masks, plus rendered views of the actual final geometry.
Two mesh views share the same seven-image budget with source and mask slices;
omitted views are disclosed. The render uses carried compatible scale and origin,
fixed cameras and unchanged triangles, not a screenshot of unrelated viewer
layers. Its depth ordering and transparency are approximate, not a topology test.

No raw image volume, source file paths/names, acquisition history, table-row
text or unrelated earlier candidate is included. The local connector sends
measurements only; it does not silently discard an enabled input-image choice
and pretend it performed visual review. **Revise using results** shares the
measured evidence, report and image manifests again with the fresh draft request.
For Codex, it also resends the same previously approved bounded result images,
under the current image choices and shared limit; local revision still sends
measurements only. It does not silently capture additional images. You can inspect the current
disclosure before sending; merely checking an option never uploads evidence.

Codex sends the approved request to OpenAI. ChatGPT-authenticated usage follows
its applicable ChatGPT data policies; it is not automatically covered by API
data settings. "Not used for training" is different from no upload or no
retention, and a prompt cannot set the provider's retention policy. See
[Codex authentication policies](https://learn.chatgpt.com/docs/auth) and
[OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data).

Local-service trust is separate: a loopback address does not prove that
independently configured software never forwards or logs requests. Avoid
private information in the goal or messages for either provider. **Cancel request**
revokes acceptance and further repair; an already transmitted request cannot
be recalled. Changing image-preview sharing preserves answers only while the
input and workflow are unchanged, cancels pending work and requires a fresh
explicit Send. It does not transmit merely because you check the option.

## Optional details and evaluation

**Advanced details** contains the technical JSON, complete metadata request
and attempt trace. **Proposal JSON**, **Request**, **Attempts** and the sharing
preview's **Advanced shared-data details** use a fixed-width font. JSON fields
have light/dark-aware syntax colour cues; Attempts is font-only, while **Plan
text**, Goal and chat remain normal prose. Colours are not validation or repair:
incomplete JSON can be coloured without being accepted. Literal text, editing,
read-only roles, copying and undo are unchanged.
**Settings → Advanced** holds optional model/thinking choices, attempt limits
and time limits. Both Codex and local providers default to **600 seconds
(10 minutes) per attempt**, also the maximum. With up to two attempts, including
one automatic validation repair, a request can use up to **20 minutes** of model
time. You can cancel while waiting; the elapsed clock is a local timer, not a
remote-model heartbeat. Expert edits are also checked
automatically; there is no **Validate JSON** action in the normal workflow.
Copied goal/response text can contain private information.

The original goal allows up to 4,000 characters. Answered clarification history
has a separate limit of 32 question/answer pairs, with 2,000 characters per
question or answer. Clarification text has a 64 KiB budget. These history/text
limits are separate from the per-response 3/2/1 initiative caps.
The complete serialized metadata request, including the library catalogue,
is separately limited to 192 KiB; a returned proposal remains limited to
128 KiB. If a limit is reached, the request stops before sending;
earlier answers are not silently shortened or discarded to make room.
The full catalogue uses lossless shared tables: node definitions, parameter
choices and help are retained, not trimmed to a guessed shortlist.

Full-library requests also need more model context. The Ollama connector still
requests 16,384 context tokens with truncation disabled; a local server may
reject a request it cannot fit. Being connected does not prove it can handle
that request. Metadata-only authoring checks do not qualify live local-model or
Codex answer quality, prove that an analysis works, or compare model accuracy.

This slice plans and validates graphs, offers an opt-in bounded investigation,
assesses explicitly shared results and offers a separately started, finite
refinement series. It does not tune without limits, create custom code or
establish scientific success by itself.
Evaluate the calculated result against an **independent target**, including
missed, merged/split objects and incorrect boundaries. Visual appearance and
object count alone are insufficient. A small authoring comparison **does not
establish parity** between local models, API models or this coding agent.

The implemented assessment is bound to an actual, identified run. Broader
review-frequency controls remain future work. ChatGPT post-run refinement can
explicitly nominate a tested candidate or keep the accepted result; that is a
model preference, not a scientific best-result certificate. Local-connector
refinement retains its earlier series behavior.
Only **Start refinement**, not the longer wait limit or slider alone, authorizes
the bounded work described above.

Continue with [linked image review](review-images.md),
[workflow validation](../scientific-practice/validation.md), and
[parameter tuning](../scientific-practice/parameter-tuning.md).

## Optional external MCP client

### Connect to the open VIPP window

1. In Goal, select the loaded source, goal and independent sharing choices.
   Select whether to start from its current completed workflow.
2. Choose **Enable live connection**. This authorises the selected goal and
   data to be available to one external client; it does not send a built-in
   model request or change either image checkbox. Output assessment must be on
   for investigation. External mode always requires local finish review.
3. Use **Copy connection command** and configure that stdio command in your
   MCP client. VIPP does not modify the client's configuration automatically.
   The command includes `--enable-mcp --live` and a private temporary descriptor
   path. Treat that descriptor as a secret capability; do not share its contents.
4. Prompt your external agent. Its inspections and trials appear in VIPP's
   investigation history. The external client owns its model, sign-in, usage
   limits and conversation; no second OpenAI login in VIPP is required.
5. Review a nominated finish in VIPP. **Good enough**, **Add** and **Run** remain
   separate local decisions. **Disconnect and pause** revokes the connection
   and preserves the session. Continue locally, then enable a fresh connection
   and update its command if you want to reconnect.

The bridge listens only on authenticated local loopback and creates an
owner-only temporary connection descriptor. It never exposes a public listener,
automatically registers a client, executes arbitrary code or grants filesystem
access. If you change the source, graph or permissions, stale delivery is
rejected. A completed trial can remain in local history after disconnect even
when its result can no longer be sent to the external client. External context
exchanges are conservatively counted; they are not a count of that client's
private model turns or proof that a model read the delivered evidence.

### Isolated headless investigation

The unreleased `vipp-agent-mcp` command exposes these same guarded tools to a
local MCP client. It is **off by default** and requires both `--enable-mcp` and
`--config` with a human-authored local JSON configuration. It does not register
itself with a client or start a network service.

The `--config` mode creates an **isolated CPU investigation**, not a connection
to an already open VIPP window. The configuration names one local numeric NPY
file, your goal, explicit ZYX axes/scale/unit/origin, independent input/output
preview choices, and finite limits. Tool arguments cannot choose another file,
run arbitrary code, save outputs or accept/add a workflow. The external client
is responsible for its own model connection and privacy policy. Sent context
and images use the same sharing guards; counted external exchanges are not a
measurement of that client's actual model turns. Use the native assistant for
the integrated review, Add and Run steps.
