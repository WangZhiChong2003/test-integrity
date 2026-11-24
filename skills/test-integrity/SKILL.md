---
name: test-integrity
description: Design or review tests when the task calls for test work or a concrete regression risk to a product or system contract needs coverage. Diagnose failing or flaky tests in local runs or CI. Routine edits and verification with existing checks are outside this workflow.
license: MIT
---

# Test Integrity

## Goal

Keep tests effective at detecting real regressions without turning valid implementation changes into unnecessary test-maintenance work.

Treat production code and test code as independently fallible. A failed test is evidence to investigate, not proof that production code is wrong. A passing test is not proof that its assertions are meaningful.

## When permanent coverage is warranted

By default, verify the requested result with existing checks or direct inspection. Follow explicit user or repository requirements for automated coverage.

Before adding coverage on your own, identify a dependency beyond the request to make the edit. What required task would fail, what caller would receive an incorrect result, or what system invariant would be violated if this detail changed again? Ground the consequence in requirements, actual usage, or an observed defect. If the only consequence is that the result would differ from this edit, finish after verification.

Add a permanent case or assertion only when it detects a specific failure of that capability or guarantee that existing cases would miss. Assert the affected outcome and accept every result the contract allows for the same input and conditions.

## 1. Establish the behavior contract

Before adding or changing a significant test, identify:

1. **Behavior:** What observable outcome must hold?
2. **Authority:** Where does the expected result come from (specification, API contract, requirement, standard, independently verified fixture, or domain invariant)?
3. **Failure mode:** What realistic regression would this test catch?
4. **Level:** Is a unit, integration, or end-to-end test the least costly reliable level?
5. **Overlap:** Reuse an existing case that would fail for the same defect. When a different input exposes an uncovered failure, extend the relevant case. Cover another level when it exposes a distinct risk, such as wiring the wrong implementation into the public entry point.

If the behavior or expected result is unclear, inspect surrounding contracts and usages first. State material uncertainty instead of inventing an assertion.

## 2. Write tests that survive valid changes

- Assert observable outputs, state transitions, errors, invariants, and externally promised side effects.
- Prefer public or stable interfaces over private helpers, internal call order, exact data structures, or incidental logs.
- Use small, representative fixtures, explicit setup and teardown, and independent test cases.
- Control randomness, time, ordering, network behavior, and mutable global state when they are not part of the behavior under test.
- Avoid arbitrary sleeps and tight wall-clock thresholds in ordinary correctness tests. Separate performance tests from functional correctness where appropriate.
- Exercise the production entry point that owns the behavior. A mock or fake can supply an input or dependency failure. Trace the asserted result back to the production decision, especially when a test helper or fake could supply the whole answer.
- Derive the expected value independently from the contract. Use a hand-checked example, a known-answer fixture, or an invariant that a plausible defect would violate. Copying the algorithm or recording its current output can preserve the same defect on both sides of the assertion.
- Test realistic boundary and failure cases supported by the actual API and runtime contract. Do not force production code to support imaginary states merely to satisfy a new test.
- Prefer meaningful assertions to test count, coverage percentage, or snapshot volume.

For examples and review heuristics, consult [test design reference](references/test-design.md) when needed.

## 3. Check that a new test is useful

Before accepting a test:

- For a regression fix, run the new test before and after the fix when practical. Confirm that it fails for the intended behavioral reason before the fix and passes afterward.
- Check that the intended assertions execute and that a behavior-preserving refactor should leave the test passing. Watch for empty loops or swallowed exceptions that can let a test pass without checking the behavior.
- Use a targeted, reversible fault injection or mutation check when the risk warrants stronger evidence and the check is safe and inexpensive. Restore the code after the check.
- If work shifts to repairing setup for a proposed test, revisit the gap. Discard your redundant draft if an existing case catches the defect. If the gap is real, use the simplest setup that still exercises it. Follow up on any actual product failure the draft exposed.

## 4. Diagnose failures before editing

When a test or CI job fails:

1. **Locate:** Find the first relevant failure and the specific assertion or setup step. Inspect concise logs, not repetitive output.
2. **Reproduce:** Run the smallest relevant test under the same meaningful configuration, if feasible. Do not blindly rerun the full suite.
3. **Validate expectation:** Compare the expected behavior with its authoritative contract and the current change's intended scope.
4. **Classify using evidence:**
   - **P — Product defect:** implementation violates a valid contract.
   - **T — Test defect:** assertion, fixture, mock, or test assumption is invalid or overcoupled.
   - **E — Environment/infrastructure:** dependency, configuration, resource, platform, or CI setup issue.
   - **N — Nondeterministic:** race, uncontrolled ordering, timing, or external instability.
   - **U — Unresolved/mixed:** insufficient evidence or multiple contributing causes.
5. **Fix the verified cause:** Keep the original failing input, expectation, and observed result available for comparison. Fix the component implicated by the evidence. If further edits would only be guesses, preserve the failing signal and report the evidence still needed.
6. **Validate:** Rerun the affected test, then the relevant surrounding suite when practical. Check the runner's results for the affected case. A successful command can select zero tests, skip the case, or exercise a substitute backend.

A repeat run may help diagnose nondeterminism, but repeated passes must not erase a known failure. Do not treat a failing test as authoritative merely because an agent wrote it.

For detailed triage patterns, consult [failure diagnosis reference](references/failure-triage.md) when needed.

## 5. Protect existing regression coverage

- Distinguish intentional contract changes from refactoring that should preserve behavior.
- Preserve valid regression assertions when changing implementation details.
- Before changing what the suite accepts, identify the requirement that changed or the independent evidence that the original check was wrong. Apply this to indirect changes too, including fixtures, mocks, snapshots, tolerances, skips, and test selection. The latest output alone cannot justify the edit.
- When an allowed design change breaks several tests, find the common assumption before updating expectations. Once the promised behavior is covered, remove assertions that enforce a disproven assumption. One existing behavioral check may already be sufficient.
- Review product edits made in response to a failure even when the tests are untouched. Trace the original input through the normal caller's path to the promised result, side effect, or error. Reject a flag, shadow value, fixture-specific branch, or silent fallback that makes the assertion pass while the caller still experiences the defect.

When both sides change, check them separately against the contract. For a regression fix, use the same discriminating case on the old and fixed behavior when practical. For a test correction, identify a still-invalid result the revised check would catch. If the requirement was retired, cite the change that retired it.

## 6. Finish with a concise evidence report

For relevant test work, report:

- **Contract protected:** What observable behavior was checked.
- **Test changes:** What was added or changed and why. For a changed expectation, give the old and new outcomes and the independent basis for the change.
- **Failure diagnosis:** P / T / E / N / U, with a brief explanation when investigating a failure.
- **Validation:** Name the checks that ran and the behavior they exercised. Identify any required path left unverified by a filter, skip, or unavailable dependency.
- **Residual risk:** Material unverified behavior, environment limits, or remaining flakiness.

For routine verification a sentence naming the check and its result is enough. Include diagnosis and residual risk when they affect the outcome.
