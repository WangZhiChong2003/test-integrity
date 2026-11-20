---
name: test-integrity
description: Design and review software tests that catch regressions, and diagnose test-related failures. Use when adding, changing, or reviewing tests, or investigating failing or flaky tests in local runs or CI. Includes test work identified partway through implementing a feature, fixing a bug, or refactoring.
license: MIT
---

# Test Integrity

## Goal

Keep tests effective at detecting real regressions without turning valid implementation changes into unnecessary test-maintenance work.

Treat production code and test code as independently fallible. A failed test is evidence to investigate, not proof that production code is wrong. A passing test is not proof that its assertions are meaningful.

## Scope and priority

- Follow the repository's documented requirements, API contracts, and established test conventions.
- Apply this skill to test design, changes, review, or test-related failure investigation. Tie new tests and suite redesigns to a specific task need.
- Prefer the smallest useful investigation and validation scope. Increase scope when risk or evidence warrants it.
- Respect explicit user requirements and security/correctness constraints. Never preserve a faulty test merely because it is old.

## 1. Establish the behavior contract

Before adding or changing a significant test, identify:

1. **Behavior:** What observable outcome must hold?
2. **Authority:** Where does the expected result come from (specification, API contract, requirement, standard, independently verified fixture, or domain invariant)?
3. **Failure mode:** What realistic regression would this test catch?
4. **Level:** Is a unit, integration, or end-to-end test the least costly reliable level?
5. **Overlap:** Does an existing test already protect this behavior?

If the behavior or expected result is unclear, inspect surrounding contracts and usages first. State material uncertainty instead of inventing an assertion.

## 2. Write tests that survive valid changes

- Assert observable outputs, state transitions, errors, invariants, and externally promised side effects.
- Prefer public or stable interfaces over private helpers, internal call order, exact data structures, or incidental logs.
- Use small, representative fixtures, explicit setup and teardown, and independent test cases.
- Control randomness, time, ordering, network behavior, and mutable global state when they are not part of the behavior under test.
- Avoid arbitrary sleeps and tight wall-clock thresholds in ordinary correctness tests. Separate performance tests from functional correctness where appropriate.
- Mock external boundaries when necessary, but do not mock the behavior whose correctness is being tested.
- Derive the expected value independently; do not recreate the production algorithm in the test or generate expected outputs from the same implementation being checked.
- Test realistic boundary and failure cases supported by the actual API and runtime contract. Do not force production code to support imaginary states merely to satisfy a new test.
- Prefer meaningful assertions to test count, coverage percentage, or snapshot volume.

For examples and review heuristics, consult [test design reference](references/test-design.md) when needed.

## 3. Check that a new test is useful

Before accepting a test:

- For a regression fix, run the new test before and after the fix when practical. Confirm that it fails for the intended behavioral reason before the fix and passes afterward.
- For a straightforward test, identify a realistic regression its assertions would catch and run the relevant tests.
- Check that the intended assertions execute and that a behavior-preserving refactor should leave the test passing. Watch for empty loops or swallowed exceptions that can let a test pass without checking the behavior.
- Use a targeted, reversible fault injection or mutation check when the risk warrants stronger evidence and the check is safe and inexpensive. Restore the code after the check.
- Keep the test only if it adds a meaningful signal or guards a previously missed regression.

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
5. **Fix the verified cause:** Change the smallest appropriate component. Record the reason for changing test expectations.
6. **Validate:** Rerun the affected test, then the relevant surrounding suite when practical. Report any unrun checks.

A repeat run may help diagnose nondeterminism, but repeated passes must not erase a known failure. Do not treat a failing test as authoritative merely because an agent wrote it.

For detailed triage patterns, consult [failure diagnosis reference](references/failure-triage.md) when needed.

## 5. Protect existing regression coverage

When modifying existing tests:

- Distinguish intentional contract changes from refactoring that should preserve behavior.
- Preserve valid regression assertions when changing implementation details.
- Change the expected outcome only when the intended contract changed or the former expectation was demonstrably wrong.
- Explain any removed assertion, loosened threshold, deleted test, skipped case, or modified fixture that could reduce defect detection.
- Replace brittle assertions with stronger behavior-level checks rather than simply deleting them.
- Do not modify product code to conform to a disproven test assumption, and do not weaken a correct test to make CI green.

If both production code and tests change, review whether the test still independently detects the target regression.

## 6. Finish with a concise evidence report

For relevant test work, report:

- **Contract protected:** What observable behavior was checked.
- **Test changes:** What was added or changed, and why it is needed.
- **Failure diagnosis:** P / T / E / N / U, with a brief explanation when investigating a failure.
- **Validation:** Exact relevant checks run and whether they passed, failed, or were not run.
- **Residual risk:** Material unverified behavior, environment limits, or remaining flakiness.

Keep this report proportionate to the task. Do not claim CI or tests passed unless they actually ran.
