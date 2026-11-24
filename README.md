# Ambition

Ambition 是一套用于 AI Agent 的任务方法：重审目标与路径、查清关键未知，并从其他领域迁移具体方法。使用时保留用户明确目标和约束，按证据选择方案。

| 方法 | 什么时候用 | 要交付什么 |
|---|---|---|
| altitude | 当前任务可能只是既定实现方式 | 更接近目标的任务定义、路径比较和验证方案 |
| depth | 答案依赖尚未查清的关键未知 | 专业补充、原始材料、具体方法、外部验证和相称结论 |
| range | 当前领域的方法不足，需要借鉴其他领域 | 行为与结果描述、迁移条件、具体步骤和可验证尝试 |

三种方法按需要选用。目标需要重审时先用 altitude，寻找跨领域方法时用 range，影响判断的未知用 depth；无需每次执行全部流程。普通查询、纯润色及已确定方案的常规实现按原任务工作。

## 安装

用 skills CLI 安装固定发布版：

```bash
npx skills add SgtBaixiao/ambition@v1.0.0 --skill ambition -a codex -g
```

安装最新主分支：

```bash
npx skills add SgtBaixiao/ambition --skill ambition -a codex -g
```

也可以下载 [GitHub Release](https://github.com/SgtBaixiao/ambition/releases/tag/v1.0.0) 的 `ambition-v1.0.0.zip`，把其中的 `ambition` 文件夹放入 Agent 的技能目录。Codex 默认目录为 `~/.codex/skills/`。已有同名 Skill 时先保留旧副本，再根据自己的更新方式替换。

Skill 不依赖特定 MCP、额外 Python 包或多代理运行器。方法需要的工具和材料由实际任务决定；工具未取得时说明条件，不把计划写成已经执行。

## 使用

```text
请用 $ambition 的 range 处理这个任务：[具体任务]。
保留我的明确目标、约束和交付物。
先描述需要完成的行为和结果，识别关键障碍，
从其他领域选择具体方法，说明适用条件、收益依据和成本，
设计有基线、观察结果、通过／失败与停止条件的尝试。
本次只给方案。
```

只写 `$ambition` 时，Agent 根据请求选择分支。明确需要继续执行时，在任务中写明执行范围；重审任务和跨领域方法不会扩大原有权限。

## 方法依据与验证

概念起点来自 Felix Rieseberg 的 [How to be more ambitious](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)。本 Skill 在其 altitude、depth、range 建议上加入用户要求的目标保留、材料追踪、迁移条件、成本比较、可验证尝试及停止规则。

[方法来源](skills/ambition/references/sources.md)区分原文支持与本项目的组合设计。[研究与两遍修订](docs/research-and-refinement.md)说明如何从文章细化，再结合用户要求扩展；[验证记录](docs/validation.md)保留实际检查及边界。两遍完整包存放在 `drafts/`，发布包只含可安装的 Skill。

`drafts/` 中的入口保存为 `SKILL.md.snapshot`，防止安装器将历史版本识别为当前 Skill；Release 的两遍 ZIP 会还原为 `SKILL.md`，可以单独解压核对。

公开发布、CI、附件下载、远程固定版本安装和 skills.sh 收录已核对，见[发布凭证](docs/publication.md)。

行为检查使用构造请求和材料。格式、包一致性与所测行为通过，不能证明跨领域普遍效果、真实使用收益或宿主自动选择。后续真实任务中的发现决定方法更新。

## 许可证

本仓库原创规则、研究归纳与构造案例采用 [MIT License](LICENSE)。参考文章和研究仅作出处链接，原网页、论文及其他 Skill 正文没有包含在分发包中。
