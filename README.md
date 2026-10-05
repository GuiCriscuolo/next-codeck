# Next Codeck

**AI Presentation Design System by Next Interativa**

Next Codeck is a portable presentation-design system designed to help AI systems create strategic, visually compelling and editable PowerPoint presentations while following a controlled master template, slide-function library and approved asset libraries.

## Source of truth

The repository contains:

- `template/codeck-template.pptx` — approved PowerPoint master
- `rules/funcoes-slides.xlsx` — official slide-function definitions
- `rules/slide-library.md` — normalized human-readable slide catalog
- `rules/slide-rules.yaml` — machine-readable slide mapping
- `assets/icons/` — approved icon library
- `assets/photos/` — approved photography library
- `core/` — system instructions, design principles, storytelling and quality control
- `adapters/` — instructions for using Next Codeck with different AI environments

## Architecture

```
next-codeck/
├── README.md
├── core/
│   ├── system-prompt.md
│   ├── design-principles.md
│   ├── storytelling.md
│   └── quality-check.md
├── template/
│   └── codeck-template.pptx
├── rules/
│   ├── funcoes-slides.xlsx
│   ├── slide-library.md
│   └── slide-rules.yaml
├── assets/
│   ├── icons/
│   └── photos/
├── examples/
└── adapters/
    ├── generic-ai.md
    ├── chatgpt.md
    ├── claude.md
    └── gemini.md
```

## How Next Codeck works

1. Understand the audience and objective.
2. Define the message of each slide.
3. Classify the communication purpose.
4. Select an approved Codeck slide function.
5. Map the function to the approved master layout.
6. Use only approved icons and photography.
7. Preserve the Codeck visual system.
8. Keep PowerPoint elements editable whenever possible.
9. Run the quality check.

## Important semantic rules

**Historical Timeline** is reserved for chronological history.

**Process Roadmap** is for processes, methodologies, journeys and operational sequences.

**Product Roadmap** is for future product releases, features and initiatives organized by period.

**Flexible Content** is the controlled escape hatch for complex compositions that do not fit another approved layout. It must still preserve the Codeck identity.

## Portability

The core of Next Codeck is platform-independent Markdown + YAML. AI-specific adapters are provided only to explain how each environment should load and apply the system.

The PowerPoint master remains the visual source of truth.
