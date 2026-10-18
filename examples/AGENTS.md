# Example instructions

Follow [root instructions](../AGENTS.md). Each case README owns its purpose, first useful outcome, and acceptance criteria. Apply the [writing method](../docs/writing-method.md) and [Chinese writing rules](../docs/chinese-writing.md) to explanations, prompts, instructions, and exercises. Use the [terminology table](../docs/terminology.md).

- Keep design, runnable implementation, and tested result distinct. Do not mark a case ready merely because code runs or a UI exists.
- Runnable examples must include prerequisites, supported environments actually tested, a command or clear entry, teaching inputs, expected results, and recovery guidance for common failures. Keep these beside the example.
- Use labeled synthetic or explicitly cleared materials. Record non-code inputs and outputs in [materials.json](materials.json), following [publication policy](../docs/publication-scope.md). Do not import research downloads by default.
- Originals are read-only. Write outputs separately; preview destructive operations and make any overwrite deliberate. Missing values are not zero; unrecognized fields must not be guessed.
- Reuse mature libraries for common operations. Record dependencies and their licenses when code is added. Explain choices that affect the reader’s implementation or verification.
- Validate software changes independently of the coding agent’s claim. Preserve starting revisions, task requirements, code diffs, test results, failure evidence, and recovery checks. Record human effort, waiting, rework, and available usage data. Do not treat one successful run or fewer tokens as proof of better development outcomes.
- State what still needs human judgment and which formats or environments have not been tested. Keep raw development conversations and private work files out of commits.
