# Test and CI failure triage

Use this guide when the failure origin is disputed or unclear. The labels are analytical categories, not a mandate to change particular files.

## Triage table

| Class | Evidence to seek | Typical corrective action |
| --- | --- | --- |
| P — Product defect | Valid requirement + observed behavior violates it | Fix production logic and keep regression coverage |
| T — Test defect | Wrong oracle, obsolete requirement, brittle assertion, faulty fixture/mock | Correct the test without losing legitimate coverage |
| E — Environment/infrastructure | Missing dependency, wrong configuration, runner resource limit, platform mismatch | Fix setup, dependency pin, CI configuration, or document unavailable validation |
| N — Nondeterministic | Same inputs produce inconsistent failures; races, scheduling, clock, external service | Make test or product deterministic; identify real race when present |
| U — Unresolved/mixed | More than one cause or insufficient evidence | Report what is established and what remains unknown |

## Procedure

1. Identify the first informative failure, not just the final summary line.
2. Determine whether the failure occurs during environment setup, build, test setup, assertion, or teardown.
3. Inspect the minimal relevant source and test diff, plus the requirement being asserted.
4. Execute a targeted reproduction with an explicit reasonable timeout; capture lengthy output to a log and read only high-signal diagnostics.
5. For a suspected flaky failure, vary only one relevant factor at a time. One or two repeats may be enough to expose nondeterminism, but a passing rerun does not resolve a previous unexplained failure.
6. When the source is identified, fix the cause and verify both the target test and relevant neighboring behavior.

If a surrounding suite turns up a seemingly unrelated failure, compare the same case and configuration against the unchanged baseline when practical. An identical baseline failure can be reported separately while completing the requested fix. If the baseline is unavailable, leave attribution open. A failure in a different file can still share the changed code path.

## Common traps

- **"CI failed, so change src":** A test may have an incorrect expectation or invalid fixture.
- **"CI is green, so the bug is fixed":** A deleted, skipped, or vacuous test may provide no signal.
- **"The test works on my machine":** Check environment differences before changing expected results.
- **"Increase timeout until it passes":** First establish whether timing is a functional guarantee or environmental variability.
- **"Just regenerate the snapshot":** Review the behavioral difference and confirm it is intended.
- **"Retry until green":** Intermittent failures are still defects or unresolved environmental risks.

## Example: refactor changes internal calls

A test fails because a mock expects an internal helper to be called three times. The documented API output remains correct and there is no contract on helper call count.

Classify as **T** after verification. Replace the call-count assertion with an observable behavior assertion; do not force the refactored product to call a helper unnecessarily.

## Example: actual regression

A writer is required to reject a truncated record, but the new implementation accepts one silently. A test fails on an independently defined truncated fixture.

Classify as **P**. Fix the writer, keep the valid rejection test, and rerun relevant I/O tests.

## Example: resource-dependent integration test

A CI runner lacks a required GPU device for a hardware integration test. The application behaves correctly on supported GPU hardware, but the runner cannot execute the test.

Classify as **E** if the test requires that hardware. Route the test to an appropriate runner or report it as not executed; do not fake a successful integration test.
