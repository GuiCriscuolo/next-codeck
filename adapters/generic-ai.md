# Next Codeck — Generic AI Adapter

Use this package with any AI system that can read Markdown, YAML and files.

## Required context

Load, in order:

1. `core/system-prompt.md`
2. `core/design-principles.md`
3. `core/storytelling.md`
4. `rules/slide-rules.yaml`
5. `rules/slide-library.md`
6. Approved assets as needed
7. `core/quality-check.md`

## Task protocol

When asked to create a presentation:

1. Analyze the source material.
2. Propose the narrative structure.
3. Assign a Codeck function to every slide.
4. Select the corresponding master layout.
5. Identify required approved assets.
6. Produce the presentation using the approved master.
7. Validate against the quality checklist.

If the AI cannot create or edit PowerPoint files directly, it should still produce a slide-by-slide build specification rather than inventing a new design system.

## Output contract

For each slide, record:

- Slide number
- Function
- Master layout
- Title
- Main message
- Supporting content
- Required assets
- Data/visualization type
- Notes for editable PowerPoint construction
