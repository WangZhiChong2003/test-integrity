# Test Integrity

**Tests should catch regressions—not manufacture them.**

`test-integrity` is a lightweight, framework-agnostic [Agent Skill](https://agentskills.io/specification) for coding agents. It improves the quality of tests written by agents and the way agents diagnose test and CI failures.

It is useful when an agent writes fragile tests that fail after harmless refactoring, assumes every failed test proves a product bug, or changes expected results merely to make CI green.

## Principles

- **Contract over implementation:** Test observable behavior and documented guarantees, not incidental internal details.
- **Independent expectations:** Derive expected results from requirements, standards, known-answer data, or invariants rather than from the code under test.
- **Diagnose before editing:** Distinguish product defects, test defects, environment problems, nondeterminism, and unresolved/mixed causes.
- **Preserve regression detection:** Never weaken an assertion simply to produce a passing build.
- **Use proportionate effort:** Small, deterministic tests and targeted validation; no mandatory heavyweight processes.

This skill does **not** mean treating failing tests as wrong. It aims to make true bugs more obvious and false failures less frequent.

## Repository layout

```text
test-integrity/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CONTRIBUTING.md
├── .github/workflows/verify.yml
├── scripts/check_skill.py
├── examples/
│   ├── AGENTS.snippet.md
│   └── review-scenarios.md
└── skills/test-integrity/
    ├── SKILL.md
    └── references/
        ├── test-design.md
        └── failure-triage.md
```

## Install

Clone the repository (replace `<owner>` with its actual GitHub owner):

```bash
git clone https://github.com/<owner>/test-integrity.git
cd test-integrity
```

### Codex and Pi (user-wide installation)

Both support the shared `.agents/skills` location. On Linux, macOS, or WSL:

```bash
mkdir -p ~/.agents/skills
cp -R skills/test-integrity ~/.agents/skills/
```

On native Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse -Force "./skills/test-integrity" "$HOME/.agents/skills/test-integrity"
```

Restart or reload the agent if it does not immediately discover the new skill.

### Per-project installation

Copy the `skills/test-integrity/` folder into the target repository at `.agents/skills/test-integrity/`.

For Codex, invoke the skill explicitly using `$test-integrity` when needed; Pi supports `/skill:test-integrity`. Automatic selection depends on the agent and its skill-discovery behavior.

Other Agent Skills-compatible tools may support the format but differ in discovery paths and invocation commands. Consult your agent's documentation.

## Apply it in everyday development

After installing the skill, we recommend adding the `Testing and Validation` section to the target repository's root `AGENTS.md`. Merge the bullets into any existing testing rules, or create a root `AGENTS.md` if needed. Use the [recommended AGENTS.md snippet](examples/AGENTS.snippet.md).

The project instructions put the core testing rules in scope for ordinary coding requests. They also tell the agent to read the installed skill before writing, changing, or reviewing tests or investigating a test failure. This covers work that comes up mid-task, such as adding a regression test while fixing a bug. For routine verification, the agent runs the relevant existing tests and reports the results.

For a shared project setup, commit the skill under `.agents/skills/test-integrity/` alongside the root `AGENTS.md`. To reuse one installation across several projects, install the skill at user scope and merge the snippet into each project's `AGENTS.md`.

## Usage examples

Ask your agent:

> Use test-integrity to review the tests introduced in this change. Identify brittle assertions and explain what regression each new test catches.

> Use test-integrity to diagnose this CI failure before changing production code. Distinguish a product regression from an incorrect test or runner issue.

> Use test-integrity to replace implementation-coupled assertions with behavior-level checks without losing coverage.

Additional [review scenarios](examples/review-scenarios.md) show how the skill should reason about common cases.

## Validation

The repository includes a small **dependency-free** structural check. It checks required metadata, paths, and simple frontmatter conventions; it is not a full YAML parser or a substitute for an agent skill evaluation.

```bash
python3 scripts/check_skill.py
```

For full specification validation, use the official reference validator if installed:

```bash
skills-ref validate ./skills/test-integrity
```

## What the skill does not do

- It does not execute tests by itself or guarantee that agent-generated tests are correct.
- It does not install a framework, enforce test counts, or impose a specific coverage threshold.
- It does not require expensive mutation testing, repeated CI reruns, or broad suite rewrites.
- It does not replace code review or project-specific correctness requirements.

## License

MIT. See [LICENSE](LICENSE).

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI Codex skills documentation](https://learn.chatgpt.com/docs/build-skills)
- [Pi coding agent skill documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md)
