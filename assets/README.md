# Next Codeck Asset System

Assets are treated as a searchable design library.

## Folders
- \`icons/\` — approved iconography
- \`photos/\` — approved photography

## Catalog
- \`asset-catalog.json\`
- \`asset-catalog.md\`

These files are generated from the actual repository assets.

## Selection principle
1. Semantic relevance to the slide message.
2. Compatibility with the selected slide function.
3. Composition and aspect-ratio suitability.
4. Visual consistency.
5. Avoid repeated use of the same asset.

If no approved asset is a good match, report the gap instead of inventing an approved asset.

## Automation
The catalog is rebuilt automatically by GitHub Actions whenever files inside \`assets/\` change.
