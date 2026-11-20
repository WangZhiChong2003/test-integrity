# Test Integrity

[English](README.md) · **简体中文**

[![技能结构检查](https://github.com/WangZhiChong2003/test-integrity/actions/workflows/verify.yml/badge.svg)](https://github.com/WangZhiChong2003/test-integrity/actions/workflows/verify.yml)

**帮助编程 Agent 写出能发现真实回归、经得起日常重构的测试。**

`test-integrity` 适用于 Codex、Pi 和其他兼容的编程 Agent。它指导 Agent 使用项目已有的测试框架设计和审查测试，并排查本地或持续集成（CI）中的测试失败。技能采用 [Agent Skills 规范](https://agentskills.io/specification)。

## 它会怎样改变测试工作

| 场景 | Agent 应该检查什么 |
| --- | --- |
| 内部重构后，模拟对象（mock）的调用次数断言失败。 | 核对调用次数是否属于接口承诺。如果契约只规定输出，就检查输出。 |
| 修复缺陷时需要补一个回归测试。 | 根据预期行为独立推导结果。条件允许时，确认用例在修复前因预期原因失败、修复后通过。 |
| CI 中有测试失败。 | 运行最小相关用例复现问题，再核对失败断言与预期行为，根据证据判断应修改业务代码、测试还是运行环境。 |
| 接口的预期行为有意变更，需要更新断言。 | 确认新预期有需求或规范依据，并检查修改后的断言仍能捕捉相关回归。 |
| 改了测试夹具，或在生产代码里加了内存标记后，保存测试通过了。 | 如果接口承诺持久化，就按调用方的正常用法重新打开存储再读取。只读回缓存里的值可能掩盖写入失败。 |

## 快速开始

### 1. 安装技能

克隆并进入仓库目录。

```bash
git clone https://github.com/WangZhiChong2003/test-integrity.git
cd test-integrity
```

将 `skills/test-integrity/` 整个目录连同 `references/` 一起复制。Codex 和 Pi 均支持以下两个位置。

| 安装范围 | 目标路径 | 适用场景 |
| --- | --- | --- |
| 用户级 | `~/.agents/skills/test-integrity/` | 自己在多个项目中复用同一份技能。 |
| 项目级 | `<项目>/.agents/skills/test-integrity/` | 团队成员使用同一版本的技能。 |

选择用户级安装时，在本仓库根目录执行对应的命令。

**Linux、macOS 或 WSL**

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

### 2. 用一个测试改动试用

用 Agent 打开目标项目，然后显式调用技能。如果找不到技能，新开一个会话，并确认 `SKILL.md` 直接位于安装目录下。

| Agent | 显式调用方式 |
| --- | --- |
| Codex | `$test-integrity` |
| Pi | `/skill:test-integrity` |

调用时可以使用下面的任务试用。

> 审查这次改动中的测试。说明每个新测试保护的可观察行为、预期结果的依据，以及它能捕捉的一种实际回归。指出哪些断言可能在行为保持不变的重构后失败。

更多提示词和预期分析见 [审查示例](examples/review-scenarios.md)。

### 3. 接入日常开发

**推荐配置**是将 `Testing and Validation` 一节合并到目标项目根目录的 `AGENTS.md`。如果项目已有测试规则，把相关条目合并到现有章节。参见 [推荐的 AGENTS.md 片段](examples/AGENTS.snippet.md)。

项目规则要求 Agent 在新增、修改、审查测试或排查测试失败时读取已安装的技能。即使你的请求只是“修复这个 bug”，Agent 中途决定补回归测试时，这条规则也适用。日常验证可以直接运行相关的现有测试并报告结果。技能是否会被自动选中取决于客户端和模型，需要在具体任务中使用完整流程时，可以显式调用。

团队共享时，将 `.agents/skills/test-integrity/` 和根目录的 `AGENTS.md` 一起提交到目标项目。个人使用用户级安装时，把推荐片段合并到需要应用规则的各个项目中。

## 仓库文件索引

| 文件 | 用途 |
| --- | --- |
| [`SKILL.md`](skills/test-integrity/SKILL.md) | 技能的触发描述和完整工作流程。 |
| [测试设计参考](skills/test-integrity/references/test-design.md) | 如何选择断言、测试数据和测试范围。 |
| [失败诊断参考](skills/test-integrity/references/failure-triage.md) | 如何排查业务代码、测试、运行环境和间歇性失败。 |
| [AGENTS.md 片段](examples/AGENTS.snippet.md) | 日常开发使用的项目规则。 |
| [审查示例](examples/review-scenarios.md) | 脆弱测试、真实回归和 CI 失败的分析示例。 |

## 贡献与验证

提出改动时，尽量附上一个现有规则处理不到位的具体场景。参见 [贡献指南](CONTRIBUTING.md)。

可以运行与 CI 相同的结构检查，验证技能元数据和本地引用路径。该脚本无需额外的 Python 依赖。

```bash
python3 scripts/check_skill.py
```

如果已安装 Agent Skills 参考验证器，也可以执行规范检查。

```bash
skills-ref validate ./skills/test-integrity
```

各客户端如何发现技能以及有哪些设置，参见 [Codex 技能文档](https://learn.chatgpt.com/docs/build-skills) 和 [Pi 技能文档](https://docs.pi.dev/latest/skills)。

## 许可证

[MIT](LICENSE)
