# Test Integrity：面向编程智能体的测试可信度 Skill

**测试应该发现真实回归，而不是制造无效失败。**

`test-integrity` 是一个遵循 [Agent Skills](https://agentskills.io/specification) 规范的轻量级、跨语言、跨测试框架的 Skill，用于约束 Coding Agent 编写和修改测试的方式，并帮助 Agent 合理诊断测试与 CI 失败。

它重点解决三类问题：

1. 测试过度依赖内部实现，正常重构也会导致失败。
2. Agent 假设测试总是正确，遇到失败就直接修改业务代码。
3. Agent 为通过 CI 而删除断言、改写预期结果或跳过测试。

但这不意味着所有失败都来自测试：真正的功能回归仍然必须被严格捕获。

## 核心理念

- **行为契约优先**：验证对外承诺的行为，而不是偶然的实现细节。
- **预期结果独立**：尽量从规范、需求、数学性质或经独立验证的样本得出预期。
- **先归因再修改**：区分业务代码缺陷（P）、测试缺陷（T）、环境问题（E）、非确定性问题（N）和未明确/混合原因（U）。
- **维护回归检测能力**：不能只为让 CI 变绿就放宽或删除测试。
- **避免过度流程**：先运行有针对性的测试，必要时才扩大范围；不强制执行耗时的变异测试。

## 安装

将仓库里的 `skills/test-integrity/` 整个目录复制到：

- **项目级**：`<项目>/.agents/skills/test-integrity/`
- **用户级（Codex 与 Pi）**：`~/.agents/skills/test-integrity/`

在 Linux、macOS 或 WSL 中，进入此仓库根目录后执行：

```bash
mkdir -p ~/.agents/skills
cp -R skills/test-integrity ~/.agents/skills/
```

Windows PowerShell：

```powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
Copy-Item -Recurse -Force "./skills/test-integrity" "$HOME/.agents/skills/test-integrity"
```

如果 Agent 未发现新 Skill，请重启或重新加载会话。Codex 可显式使用 `$test-integrity`，Pi 可以通过 `/skill:test-integrity` 调用。其他 Agent 的加载路径和命令可能不同。

## 在日常开发中使用

安装后，建议将 `Testing and Validation` 一节合并到目标项目根目录的 `AGENTS.md`。项目已有测试规则时，把相关条目并入现有章节。项目还没有 `AGENTS.md` 时，可以在根目录创建。具体内容见 [推荐的 AGENTS.md 片段](examples/AGENTS.snippet.md)。

项目指令让核心测试规则适用于普通开发任务，并要求 Agent 在新增、修改、审查测试或排查测试失败之前读取已安装的 Skill。即使你只交代“修复这个 bug”，Agent 中途决定补回归测试时，也应按这套规则检查预期结果的依据和测试能捕捉的回归。日常只需运行现有测试时，运行相关用例并报告结果即可。

团队共用时，将 `.agents/skills/test-integrity/` 和根目录的 `AGENTS.md` 一起提交到目标项目。个人在多个项目间复用时，可以在用户级安装一份 Skill，再把推荐片段合并到各项目的 `AGENTS.md`。

## 使用示例

> 使用 test-integrity 审查此次提交新增的测试，指出测试预期依据、可能的误报风险以及真实回归检测能力。

> 测试和 CI 失败了。先用 test-integrity 归因，不要直接修改业务代码或放宽断言。

> 重构后某个旧测试失败。判断它保护的是功能契约还是内部实现细节，修复真正的原因。

更多场景见 [审查示例](examples/review-scenarios.md)。

## 仓库结构与验证

完整目录结构、英文说明和仓库管理建议见 [README.md](README.md)。

```bash
python3 scripts/check_skill.py
```

上面的脚本只进行轻量级结构检查，不是完整 YAML 校验器。可按需额外运行 Agent Skills 官方参考验证器：

```bash
skills-ref validate ./skills/test-integrity
```

## 适用边界

Skill 不是独立运行的测试框架，不会自动证明测试正确、修好 CI 或强制达到某个覆盖率。不同 Agent 可能不总是自动加载相应 Skill，重要任务建议显式调用。

项目以 [MIT License](LICENSE) 开源。
