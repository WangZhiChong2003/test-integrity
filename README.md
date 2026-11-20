# Test Integrity

**English** · [简体中文](README.zh-CN.md)

[![Verify skill structure](https://github.com/WangZhiChong2003/test-integrity/actions/workflows/verify.yml/badge.svg)](https://github.com/WangZhiChong2003/test-integrity/actions/workflows/verify.yml)

**Help coding agents write tests that catch real regressions and survive routine refactors.**

`test-integrity` is a framework-agnostic Agent Skill for Codex, Pi, and other compatible coding agents. It guides test design, review, and failure diagnosis with the test framework your project already uses. See the [Agent Skills specification](https://agentskills.io/specification).

## What it changes in practice

| Situation | What the agent checks |
| --- | --- |
| An internal refactor breaks a mock call-count assertion. | Check whether the call count is a documented guarantee. If the contract only promises an output, assert the output. |
| A bug fix needs a regression test. | Derive the expected result independently from the intended behavior. When practical, verify that the test fails for the intended reason before the fix and passes afterward. |
| CI reports a failing test. | Reproduce the smallest relevant failure and check the assertion against the intended behavior. Use the evidence to decide whether to fix the product, the test, or the environment. |
| A legitimate API change updates an assertion. | Trace the new expectation to the authorized behavior change and verify that the remaining assertions still protect against relevant regressions. |

## Quick start

### 1. Install the skill

Clone and open the repository.

```bash
git clone https://github.com/WangZhiChong2003/test-integrity.git
cd test-integrity
```

Copy the entire `skills/test-integrity/` folder, including `references/`. Codex and Pi support both locations below.

| Scope | Destination | Use it when |
| --- | --- | --- |
| User | `~/.agents/skills/test-integrity/` | You want one installation across your projects. |
| Project | `<project>/.agents/skills/test-integrity/` | You want the team to use the same instructions. |

For a user-wide installation, run the command for your environment from this repository's root.

**Linux, macOS, or WSL**

```bash
mkdir -p "$HOME/.agents/skills/test-integrity"
cp -R skills/test-integrity/. "$HOME/.agents/skills/test-integrity/"
```

**Windows PowerShell**

```powershell
$skillDir = Join-Path $HOME '.agents/skills/test-integrity'
New-Item -ItemType Directory -Force -Path $skillDir | Out-Null
Copy-Item -Path './skills/test-integrity/*' -Destination $skillDir -Recurse -Force
```

### 2. Try it on a test change

Open your target project in the agent, then explicitly select the skill. If it is missing, open a new session and verify that the installed folder contains `SKILL.md` directly.

| Agent | Explicit invocation |
| --- | --- |
| Codex | `$test-integrity` |
| Pi | `/skill:test-integrity` |

Pair the invocation with a task like this one.

> Review the tests in this diff. For each new test, identify the observable behavior it protects, where the expected result comes from, and a realistic regression it would catch. Flag assertions that could break during a behavior-preserving refactor.

For more prompts and expected reasoning, see [Review scenarios](examples/review-scenarios.md).

### 3. Apply it in everyday development

**Merge `Testing and Validation` into the target project's root `AGENTS.md`.** If the project already has testing rules, add the relevant bullets to that section. Start from the [recommended AGENTS.md snippet](examples/AGENTS.snippet.md).

The project instructions tell the agent to read the installed skill when adding, changing, or reviewing tests or investigating test failures. This applies even when the agent decides to add a regression test midway through a request like “fix this bug.” For routine verification, the agent runs the relevant existing tests and reports the results. Automatic skill selection depends on the client and model, so use the explicit invocation when you want the workflow for a specific task.

For a shared setup, check in both `.agents/skills/test-integrity/` and the root `AGENTS.md` in the target project. For a user-wide installation, add the snippet to each project where you want the rules to apply.

## Repository guide

| File | Purpose |
| --- | --- |
| [`SKILL.md`](skills/test-integrity/SKILL.md) | The workflow and the description agents use to decide when it applies. |
| [Test design reference](skills/test-integrity/references/test-design.md) | How to choose assertions, fixtures, and test scope. |
| [Failure diagnosis reference](skills/test-integrity/references/failure-triage.md) | How to investigate product, test, environment, and intermittent failures. |
| [AGENTS.md snippet](examples/AGENTS.snippet.md) | Project instructions for everyday development. |
| [Review scenarios](examples/review-scenarios.md) | Examples of brittle tests, real regressions, and CI failures. |

## Contributing and validation

When proposing a change, include a concrete scenario where the current guidance falls short. See the [contribution guide](CONTRIBUTING.md).

Run the same dependency-free check used in CI to verify the skill metadata and local reference paths.

```bash
python3 scripts/check_skill.py
```

If you have the Agent Skills reference validator installed, run its specification check as well.

```bash
skills-ref validate ./skills/test-integrity
```

For client-specific discovery and settings, see the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Pi skill documentation](https://docs.pi.dev/latest/skills).

## License

[MIT](LICENSE)
