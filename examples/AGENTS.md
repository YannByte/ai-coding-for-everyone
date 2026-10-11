# Example instructions

Follow [root instructions](../AGENTS.md). Each case README owns its purpose, first useful outcome, and acceptance criteria. Apply the [book-writing skill](../.agents/skills/book-writing/SKILL.md) to explanations, prompts, instructions, and exercises. Use the [terminology table](../docs/terminology.md).

- Keep design, runnable implementation, and tested result distinct. Do not mark a case ready merely because code runs or a UI exists.
- Runnable examples must include prerequisites, supported environments actually tested, a command or clear entry, teaching inputs, expected results, and recovery guidance for common failures. Keep these beside the example.
- Use labeled synthetic or explicitly cleared materials. Record non-code inputs and outputs in [materials.json](materials.json), following [publication policy](../docs/publication-scope.md). Do not import research downloads by default.
- Originals are read-only. Write outputs separately; preview destructive operations and make any overwrite deliberate. Missing values are not zero; unrecognized fields must not be guessed.
- Reuse mature libraries for common file operations. Record dependencies and their licenses when code is added. A reader need not learn library selection before trying the case.
- Validate the task's result: report figures and layout, screenshot text readability in the destination, or document order and print readability. Use a separate input batch for repeat-use checks. Compare against independently checked expectations, not only the tool's previous output.
- State what still needs human judgment and which formats or environments have not been tested. Keep raw development conversations and private work files out of commits.
