# Example AGENTS.md section

Merge this section into the target project's root `AGENTS.md`, adapting it to the project's test conventions.

## Testing and Validation

- Read and follow the `test-integrity` skill, when installed, before adding, changing, or reviewing tests or diagnosing a test failure locally or in CI. Apply this rule even when test work arises partway through another task.
- Before adding or changing a test, identify the observable behavior it protects, the independent basis for the expected result, and the realistic regression it would catch. Reuse existing tests that already protect the behavior.
- Write deterministic assertions against documented behavior. For a new regression test, check that it fails for the intended reason before the fix and passes afterward when practical.
- Before editing code or test expectations in response to a failure, locate the failing assertion or setup step. Check the intended behavior and use the evidence to identify whether the product, test, or environment needs a fix.
- Preserve valid regression coverage. Change expectations only when the contract changes intentionally or the prior expectation is demonstrably incorrect.
- For routine validation, run the most relevant existing tests for the changed behavior.
- Report which checks actually ran and any unresolved failures or limitations.
