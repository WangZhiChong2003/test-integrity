# Example AGENTS.md section

Merge this section into the target project's root `AGENTS.md`, adapting it to the project's test conventions.

## Testing and Validation

- Use the installed `test-integrity` skill when deciding whether to add a test, changing or reviewing tests, or diagnosing a local or CI test failure. This also applies when the decision arises partway through another task.
- Reuse an existing test if it catches the target regression. For a new case, identify the gap, exercise the production behavior, and derive the expected result independently.
- Write deterministic assertions against documented behavior. For a new regression test, check that it fails for the intended reason before the fix and passes afterward when practical.
- Before editing code or test expectations in response to a failure, locate the failing assertion or setup step. Check the intended behavior and use the evidence to identify whether the product, test, or environment needs a fix.
- Before changing what the suite accepts, cite the authorized contract change or independent evidence of a faulty check. This applies to fixtures, snapshots, and test selection as well as assertions. Preserve an unexplained failure for diagnosis.
- Check product fixes through the normal caller's path with the original failing input. A test-only branch, shadow state, or swallowed error can leave the promised behavior broken even when the original test passes.
- For routine validation, run the relevant existing checks and confirm the affected case executed. If that establishes the requested behavior, finish with the result. Keep a diagnostic probe as a permanent test only for a lasting gap or an explicit requirement.
- Report unresolved failures and any required behavior that was skipped or exercised only through a substitute.
