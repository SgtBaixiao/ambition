# 发布与远程安装凭证

核对日期：2026 年 11 月 24 日。Ambition 已发布到公开仓库 [SgtBaixiao/ambition](https://github.com/SgtBaixiao/ambition)，固定版本为 [v1.0.0](https://github.com/SgtBaixiao/ambition/releases/tag/v1.0.0)。发布提交为 `1939e0e996311924eedc421095ba3d60e845c26c`，标签保留该版本；后续文档凭证不改动所测 Skill。

| 核对项 | 实际结果 |
|---|---|
| GitHub 仓库 | 公开，默认分支为 main；维护规则、两遍快照、原案例输出和研究记录已上传。 |
| GitHub CI | [发布提交的检查](https://github.com/SgtBaixiao/ambition/actions/runs/45384491470)完成并成功；元数据、引用、ZIP 内容和文件清单检查通过。 |
| Release 附件 | 最终包、第一遍包、第二遍包、manifest.json、SHA256SUMS 共五项；从 GitHub 重新下载，五项 SHA-256 与本地发布附件一致。 |
| 远程固定版本安装 | skills CLI 1.9.0 从 v1.0.0 克隆仓库，只发现一个 Skill；在独立临时项目复制安装成功，十一份文件与维护源逐项一致。 |
| 技能目录 | [skills.sh 页面](https://www.skills.sh/sgtbaixiao/ambition/ambition)返回 200，显示当前入口、安装命令及首次收录日期。安装次数显示为“–”，未据此推断用户数量。 |

发布和安装的结构化记录见[发布核对](../evidence/publication-verification.json)及[附件核对](../evidence/release-verification.json)。本机活动 Skill 也已同步，原 depth 和 range 之前的 ambition 副本分别归档，避免覆盖不同的已有内容。

实际远程安装命令如下；核对采用项目目录，没有通过这条命令改写全局 Skill。

```bash
npx --yes skills@1.9.0 add SgtBaixiao/ambition@v1.0.0 --skill ambition -a codex --copy -y
```

skills.sh 的 [Snyk 自动审计](https://www.skills.sh/sgtbaixiao/ambition/ambition/security/snyk)显示 `Warn`、`MEDIUM` 和 `W011`，说明 depth 会按问题读取第三方网页与文献，存在外部内容及间接提示注入的暴露面。审计正文将该暴露描述为按需检索，并标注 `low risk: 0.10`。这里记录其实际标签与理由，不将目录收录或安装成功解释为安全认证，也不据该通用暴露提示改动研究目标。

这些结果确认仓库、发布附件、安装及收录可访问。实际使用收益、跨领域迁移效果与宿主自动选用仍按[验证记录](validation.md)所列范围判断。
