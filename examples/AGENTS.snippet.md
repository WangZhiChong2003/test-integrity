# Example AGENTS.md section

Merge this section into the target project's root `AGENTS.md`, adapting it to the project's test conventions.

## Testing and Validation

- Read and follow the `test-integrity` skill, when installed, before adding, changing, or reviewing tests or diagnosing a test failure locally or in CI. Apply this rule even when test work arises partway through another task.
- Reuse an existing test if it catches the target regression. For a new case, identify the gap, exercise the production behavior, and derive the expected result independently.
- Write deterministic assertions against documented behavior. For a new regression test, check that it fails for the intended reason before the fix and passes afterward when practical.
- Before editing code or test expectations in response to a failure, locate the failing assertion or setup step. Check the intended behavior and use the evidence to identify whether the product, test, or environment needs a fix.
- Before changing what the suite accepts, cite the authorized contract change or independent evidence of a faulty check. This applies to fixtures, snapshots, and test selection as well as assertions. Preserve an unexplained failure for diagnosis.
- Check product fixes through the normal caller's path with the original failing input. A test-only branch, shadow state, or swallowed error can leave the promised behavior broken even when the original test passes.
- For routine validation, run the most relevant existing tests for the changed behavior.
- Report which checks actually ran and any unresolved failures or limitations.
