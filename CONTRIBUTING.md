# Contributing

Thanks for improving Test Integrity.

Please keep this repository **small, portable, and evidence-oriented**. A proposed instruction should reduce real failure modes in agent-written tests without adding substantial busywork.

## Propose a change

1. Describe the failure mode (a small, anonymized reproduction is ideal).
2. Explain why the existing workflow fails to handle it.
3. Propose the smallest rule or example that addresses it.
4. Check the rule does not encourage weakening valid regression tests or force unsupported behavior into production code.
5. Run `python3 scripts/check_skill.py` before submitting.

## Scope

Welcome: better test oracles, failure triage, realistic cross-language examples, and concise portability fixes.

Avoid: mandated coverage numbers, tool-specific assumptions in the core skill, heavyweight default workflows, and generic coding guidance unrelated to test trustworthiness.

Please do not include proprietary source code, private CI logs, secrets, or personal data in examples.

## Compatibility

The canonical skill is `skills/test-integrity/SKILL.md`, with `name: test-integrity`. Keep its required frontmatter compliant with [Agent Skills](https://agentskills.io/specification). Prefer optional reference files over a sprawling main skill.
