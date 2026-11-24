# Example AGENTS.md section

Merge this section into the target project's root `AGENTS.md`, adapting it to the project's test conventions.

## Testing and Validation

- By default, verify the requested change with existing checks or direct inspection. Unless the user or repository explicitly requires automated coverage, add a case or assertion only for a failure of a required capability or system invariant that existing cases would miss. Identify what would break for a user, caller, or the system. If the only consequence is a difference from this edit, finish after verification.
- Use the installed `test-integrity` skill when that need arises, when asked to design or review tests, when changing existing tests, or when investigating a local or CI test failure.
- For the input and conditions under test, accept every outcome the contract allows. Exercise production behavior with deterministic inputs and independently derived expectations. For a new regression test, verify that it fails for the intended reason before the fix and passes afterward when practical.
- Before editing code or test expectations in response to a failure, locate the failing assertion or setup step. Check the intended behavior and use the evidence to identify whether the product, test, or environment needs a fix.
- Before changing what the suite accepts, cite the authorized contract change or independent evidence of a faulty check. This applies to fixtures, snapshots, and test selection as well as assertions. If several tests pin the same incidental detail, remove those expectations once the promised behavior is covered. Preserve an unexplained failure for diagnosis.
- Check product fixes through the normal caller's path with the original failing input. A test-only branch, shadow state, or swallowed error can leave the promised behavior broken even when the original test passes.
- When relying on a test run, confirm the affected case executed. Report unresolved failures and any required behavior that was skipped or exercised only through a substitute.
