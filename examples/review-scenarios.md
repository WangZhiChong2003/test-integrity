# Review scenarios

These are illustrative prompts and expected reasoning patterns, not executable test suites.

## 1. Harmless refactor breaks a mock expectation

**Situation:** A refactor replaces an internal helper but preserves the public result. A test asserts the helper is invoked twice.

**Expected review:** Check whether the helper call count is a documented guarantee. If not, classify **T** (test defect) and use observable output assertions. Avoid modifying the product to restore obsolete helper calls.

## 2. Test expected value copies the implementation

**Situation:** An agent tests a checksum routine by copying the same checksum loop into the test.

**Expected review:** Treat the oracle as insufficiently independent. Use published known-answer vectors or an independently justified property, and include an input that distinguishes a plausible wrong implementation.

## 3. Real protocol regression

**Situation:** A network parser starts accepting an invalid packet that the protocol explicitly rejects. An existing test flags it.

**Expected review:** Classify **P** (product defect). Fix the parser; preserve the test. Do not rewrite the expected outcome merely because the parser changed.

## 4. CI runner lacks required resources

**Situation:** An integration test requires a GPU, but the CI runner has no GPU device.

**Expected review:** Classify **E** (environment/infrastructure) if hardware requirements are verified. Route the test to supported infrastructure or mark it explicitly unverified; do not pretend a mock validates real GPU execution.

## 5. Flaky timeout on shared hardware

**Situation:** An ordinary data-validation test fails if it takes more than 100 milliseconds, and only fails under heavily loaded CI.

**Expected review:** Determine whether the performance threshold is part of the product contract. If not, separate performance measurement from correctness and retain checks for valid output. Investigate whether a true deadlock or race also exists before blaming the runner.

## 6. Existing test changed alongside a feature

**Situation:** The agent changes both a public API and the expected result in its tests.

**Expected review:** Confirm the request or specification authorized the new behavior. Check that tests still catch the original class of regression where appropriate. Do not treat synchronized source-and-test edits as proof of correctness.

## 7. A test passes vacuously

**Situation:** A test iterates through returned entries to check their validity, but the implementation accidentally returns an empty list.

**Expected review:** Require an assertion about expected non-emptiness or item count if the contract guarantees it. Passing loop assertions alone do not prove correctness.
