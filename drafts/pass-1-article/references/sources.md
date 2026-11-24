# 方法来源与适用范围

depth 方法资料核查于 2026 年 11 月 19 日，整理于 11 月 20 日；altitude 补充核查于 11 月 24 日。以下为一手方法来源，支持相应要素。跨领域工作流程和补充要求属于用户所需的方法设计，并不表示这些机构对整套 Skill 作了评测或背书。

| 来源及定位 | 支持的要素 | 应保留的边界 |
|---|---|---|
| [NIST，Choosing an experimental design，5.3](https://www.itl.nist.gov/div898/handbook/pri/section3/pri3.htm)；[Randomized block designs，5.3.3.2](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm) | 先确定目标和变量，再选设计；辨认干扰因素，适用时采用区组与随机化。 | 指向工程与科学实验设计，不规定所有研究都随机实验。 |
| [COS，Preregistration](https://www.cos.io/initiatives/prereg)，探索与验证、计划变更、留出数据问答 | 区分探索与验证，透明记录变更；适用时留出数据做验证。 | 正式预注册按类型选用；既往接触结果须说明，计划记录不能自行证明结论正确。 |
| [SIGSIM PADS 2025，Reproducibility and Artifact Evaluation](https://sigsim.acm.org/conf/pads/2025/blog/artifact-evaluation/)，Criteria、Badges、Submission Guidelines | 区分产物可用、可执行和独立人员获得主要结果，保存必要执行说明。 | 来源是特定会议评审规则，不能把我自行重跑称为获得其复现认证。 |
| [NASA，Fundamentals of Systems Engineering，2.4](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/) | 区分符合规定要求与在预期环境实现用途的验证。 | 通过要求检查不足以自动覆盖所有目标环境；按实际验证范围报告。 |
| [Cochrane 第 4 章](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04)，4.3.2、4.4.5、4.4.6、4.4.11、4.5、4.6.1 | 关注未公开材料及检索限制、更正撤回、检索记录、研究与报告的区分，讨论搜寻何时收尾。 | 这是干预系统综述的方法。Skill 借用其记录与覆盖意识，不默认执行完整 Cochrane 综述，也不移植固定数据库要求。搜寻停止的证据存在局限。 |
| [Cochrane 第 5 章](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-05)，5.2.2、表 5.2.a、5.5.4 | 底层数据的收益与成本；多报告补充和冲突。 | 逐个参与者数据可能与汇总报告给出相同结果，已有临床研究报告时可能不需要取得；更原始仍需质量检查。 |
| [Cochrane 第 14 章](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14)，14.2、14.2.2 | 按结局评价整组证据，检查偏倚、不一致、间接性、不精确性和发表偏倚。 | GRADE 有实际适用与执行要求；借鉴这些考虑不等于完成 GRADE 评估。宽区间可能同时容许重要好处和坏处。 |

## altitude 的方法依据

| 来源及定位 | 支持的要素 | 应保留的边界 |
|---|---|---|
| [NASA，Stakeholder Expectations Definition](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/)，4.1.1.2.2 至 4.1.1.2.3、4.1.1.2.6 至 4.1.1.2.9 | 问题、目标、约束、假设与使用情景分开；目标追踪到需要；成功条件从利益相关者角度建立。 | NASA 的正式承诺与基线程序按其工程情境执行，本 Skill 不给所有任务增加审批步骤。用户明确目标和约束的决定权继续保留。 |
| [NASA，Decision Analysis](https://www.nasa.gov/reference/6-8-decision-analysis/)，6.8.1、6.8.1.2.1 至 6.8.1.2.5 | 先明确结果和标准再比较方案；必须标准筛选；围绕主要因素产生路径；检查生命周期成本、假设和排序稳健性；考虑减少不确定性的价值与延误。 | 并非每次需要决策矩阵或数值权重。主观偏好可以进入分析，但来源、取舍与不确定性需要说明；有数据不等于价值取舍唯一。 |
| [GOV.UK，Start by learning user needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)，Researching users、Validating user needs、Linking user needs to user stories | 通过现有记录、真实用户访谈和观察了解需要；需要表述围绕问题；具体任务追踪到用户需要。 | 服务设计指导不证明某项需求或方案已经成立，用户明说的目标也不能被行为推断擅自替换。 |
| [GOV.UK，Designing services for government users](https://www.gov.uk/service-manual/design/services-for-government-users)，Understand the problem、Who to research with | 检查现有流程是否必要，用有真实任务经验的用户和现实数据测试。 | 指向政府内部服务；不自动引入其政策、视觉或技术要求。 |
| [Keeney，1993，Creativity in MS/OR](https://www.academia.utp.ac.pa/sites/default/files/docente/51/io15.-creativity.pdf)，第 64–65 页，Articulating Values、Creating Alternatives、Decision Opportunities；[出版社书目](https://pubsonline.informs.org/doi/10.1287/inte.23.3.62) | 问目标为何重要，检查已有方案造成的锚定，从目标产生不同路径；单目标创意可能牺牲其他目标。 | 阅读的是大学托管原期刊扫描件，书目信息与出版社对应，未取得出版社全文逐字核对；未读到 1992 专著及 1996 论文全文，不把其摘要当全文。目标追问不授权改变用户价值取舍。 |
| [HM Treasury，The Green Book (2026)](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026)，第 4 章 Objectives、Business as usual，第 5 章 Selecting a shortlist，第 6 章 Time horizon、Scope、Sunk costs | 结果与产出分开，已锁定产出可比较交付方式；不达标基线仍作比较；最低达标路径检查过度设计；成本覆盖生命周期及受影响者，沉没成本与机会成本分开。 | 英国公共资源评估规范不自动成为其他领域义务；本 Skill 不强制其选项数量、货币化、审批或完整商业论证模板。 |
| [HM Treasury，Magenta Book](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-central-government-guidance-on-evaluation-html)，第 2 章影响评估方法、2.3.3；[Test and Learn](https://www.gov.uk/government/publications/the-magenta-book/test-and-learn-html)，6.5 TEST、6.6 GROW | 比较组、反事实及噪声决定因果结论；事前登记评估计划；先检验关键且证据弱的假设，预定继续／调整／停止条件；小试验与整体稳健评估分开。 | 同一机构体系的方法依据，不按页面数当作独立效果证据。按任务采用相称的计划记录；不强制所有任务外部预注册或随机试验。 |

## ambition 的起点

[Felix Rieseberg，How to be more ambitious](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/)，2026 年 10 月 13 日，Altitude、Depth 和 Range 三节，实际核查于 11 月 24 日。文章提出提高抽象层级、深入原始材料与专业方法、从其他领域借用工具和技巧；Range 明确区分寻找领域方法与角色扮演，建议将名词转为动词。

这是作者的实践建议和本 Skill 的概念起点，案例与鼓励语不构成所选方法的普遍效果证明。文章谈到 Speed，本 Skill 按用户当前要求维护 altitude、depth、range。用户要求保留目标与约束、查证材料、说明迁移成本及实际验证，构成本文的执行边界。文章对 Tom Kelley 与 Jonathan Littman 著作的归属按作者说法记录，本轮没有取得该书原文作独立依据。

## 设计要求与方法事实分开

本 Skill 要求每项新增研究动作对应关键判断、先回答用户指定的前置问题再改写请求、区分计划与执行，并按任务分支交付。这些是用户授权的方法约定。

学习迁移、作品分析、形式证明、工程观测、变化敏感主张和否定判断的分支是按主张类型提出的应用建议。执行具体领域研究时仍需选取并核查领域依据。通用框架未提供现成的领域实验、样本、阈值或审美标准。

## 更新依据

用于方法归属或当前规范决策时，核查当前拥有该方法的来源。改动记录与原要求保留，说明改变的规则和理由；真实使用中的失败只修补相应分支，避免把单个案例扩大为所有任务的硬规则。

本次 ACM 总政策页面返回 HTTP 403，关于独立复现的依据采用实际读取的 SIGSIM PADS 2025 页面。来源快照保留在形成 Skill 的研究工作区，通用 Skill 不依赖该工作区才能使用。
