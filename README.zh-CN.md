<div align="center">

# Applied AI Operator OS

把一线的不确定性压缩成可交付、可验收、可运营的 AI 闭环，再把现场学习回流成可复用的交付能力和产品资产。

[English](./README.md)

![FDE Operator OS Banner](./assets/readme/banner-en.svg)

</div>

## 这个仓库解决什么

`fde-operator-os` 面向 FDE、Applied AI 负责人、方案架构师和 AI 交付负责人。

它帮助团队完成六件事：

- 判断一个 AI 机会是否值得投入交付资源
- 通过真实案例和证据还原业务现场
- 定义业务对象、状态、动作、权限与状态变化证据
- 把宽泛需求压缩成一个可以验收的 operator loop
- 在进入真实生产前完成上线就绪审查
- 把现场信号沉淀成模板、评测、工具和产品输入

这里的 FDE 指一种操盘职责：连接客户任务、系统设计、生产运营与可复用能力。

## 60 秒开始

```text
Use $fde-operator-os。

只跑一个 bounded loop：
- 场景：仓储异常闭环
- operator：楼层主管
- trigger：异常告警到达
- output：带审计记录的确认闭环任务

先输出到 POC Acceptance Contract。
证据仍然薄弱时，停在 Delivery Architecture 之前。
```

第一次使用时，先选一个 operator、一个 trigger、一个 business object、一个 output。这个闭环具备证据和 owner 后，再向外扩展。

## 七阶段与五道 Gate

| 阶段 | 核心判断 | 主要工件 | Gate |
|---|---|---|---|
| 1. Mission Qualification | 这个机会是否值得投入？ | Mission Brief | G0 Mission Fit |
| 2. Operational Reality Capture | 团队是否理解真实闭环？ | Operational Reality Map、Case Replay Pack、Reality Capture Gate | G1 Evidence Sufficiency |
| 3. System Framing | 当前最重要的瓶颈和边界是什么？ | System Problem Frame | — |
| 4. State, Action & Evidence Model | 系统能读取、判断、改变和证明什么？ | State, Action & Evidence Model | — |
| 5. Intervention & Pilot Design | 一个小型 pilot 能否证明或证伪价值？ | Minimum Viable Loop、POC Acceptance Contract、Eval Pack | G2 Pilot Contract |
| 6. Delivery Architecture | 这个闭环能否在可控风险下进入真实工作？ | Day-2 Operations Plan、Production Readiness Review | G3 Production Readiness |
| 7. Expansion Logic | 当前闭环是否具备复制和扩展条件？ | Expansion Roadmap | G4 Replication And Asset Promotion |

项目交付完成后运行 Asset Distillation overlay，把案例经验转化成模板、评测、skill、治理规则、工具和产品路线输入。

## 四条贯穿全程的控制环

七阶段负责推进顺序，四条控制环负责持续校准：

1. **客户价值环**：任务适配 -> operator adoption -> 可量化的工作流影响。
2. **系统质量环**：真实案例 -> eval -> regression gate -> production trace。
3. **生产可靠性环**：readiness -> telemetry -> incident response -> postmortem。
4. **产品学习环**：field signal -> 可复用模式 -> 资产或 roadmap 决策。

完整的证据层级、约束分类、决策权、现场节奏和指标体系见 [`references/fde-practice-system.md`](./references/fde-practice-system.md)。

## Skill Suite

根 Skill 保存统一 doctrine 和路由。高频任务拆成更轻的执行 Skill：

- [`mission-qualifier`](./skills/mission-qualifier/)：早期机会判断
- [`reality-capture`](./skills/reality-capture/)：真实流程还原与证据充分性
- [`pilot-designer`](./skills/pilot-designer/)：最小 pilot、验收合同与 eval
- [`deployment-readiness`](./skills/deployment-readiness/)：生产上线审查与 live deployment rescue

## 工件契约与自动验证

仓库把阶段和工件质量写成可执行契约：

- [`contracts/stages.json`](./contracts/stages.json)：七阶段编号、ID、显示名称与退出 Gate 的统一注册表
- [`contracts/artifacts.json`](./contracts/artifacts.json)：工件名称、必填字段、工件阶段引用、Gate、兼容别名、严格示例和跨工件事实源
- [`contracts/case-manifest.schema.json`](./contracts/case-manifest.schema.json)：案例索引格式
- [`tools/validate_repo.py`](./tools/validate_repo.py)：检查模板漂移、示例缺字段、失效链接、别名重复、未知 Gate 引用和案例清单
- [`tests/test_stage_contract.py`](./tests/test_stage_contract.py)：阻止阶段注册表、根 Skill、README、工件引用和 Gate 引用发生漂移
- [`.github/workflows/validate.yml`](./.github/workflows/validate.yml)：在 push 与 pull request 中运行验证和单元测试

执行完整本地验收：

```bash
make check
```

等价的直接命令：

```bash
python tools/validate_repo.py
python -m unittest discover -s tests -v
python -m compileall -q tools tests
```

验证器只使用 Python 标准库。

## 工件体系

核心决策工件：

- Mission Brief
- Operational Reality Map
- System Problem Frame
- State, Action & Evidence Model
- AI Intervention Design
- Minimum Viable Loop
- POC Acceptance Contract
- Expansion Roadmap

执行与控制工件：

- Case Replay Pack
- Reality Capture Gate
- Eval Pack
- Governance And Risk Overlay
- Day-2 Operations Plan
- Production Readiness Review
- Field Signal Log
- Asset Distillation Log

模板位于 [`assets/templates/`](./assets/templates/)。

## 示例案例

[`examples/synthetic-exception-closure-ai/`](./examples/synthetic-exception-closure-ai/) 是一套 synthetic end-to-end case，包含：

- 机会判断、现场还原、系统 framing、pilot 和验收工件
- production readiness 与 field signal 工件
- 机器可读的 `case-manifest.json`
- 可复用模式、eval case、产品反馈与资产沉淀

其他紧凑示例：

- [`examples/first-run-minimal-loop/`](./examples/first-run-minimal-loop/)
- [`examples/synthetic-cross-border-commerce-ai/`](./examples/synthetic-cross-border-commerce-ai/)：虚构跨境电商复合案例，不对应真实客户
- [`examples/case-pack-template/`](./examples/case-pack-template/)

## 安装与调用

可以把整个仓库复制到兼容的 Skill 目录，也可以把 doctrine、references、contracts 和 templates 接入其他 agent runtime。

Codex 风格安装示例：

```powershell
Copy-Item -Recurse .\fde-operator-os "$HOME\.codex\skills\"
```

常用调用方式：

```text
Use $fde-operator-os to qualify this AI opportunity and select one operator loop.
Use reality-capture to reconstruct the real workflow and evidence gaps.
Use pilot-designer to define the bounded pilot, acceptance contract, and eval pack.
Use deployment-readiness to make a go, conditional-go, or no-go launch decision.
```

短名 wrapper 位于 [`aliases/`](./aliases/)，跨 runtime 说明见 [`references/runtime-portability.md`](./references/runtime-portability.md)。

## 仓库结构

```text
fde-operator-os/
├── SKILL.md                  # 统一 doctrine 与路由
├── Makefile                  # 本地验收入口
├── skills/                   # 轻量执行 Skill
├── references/               # 方法论、启发式、失败模式
├── assets/templates/         # operator 与控制工件
├── contracts/                # 阶段、工件、Gate 与案例契约
├── examples/                 # synthetic case 与回归示例
├── tools/                    # 仓库验证器
├── tests/                    # 验证器与契约测试
├── .github/workflows/        # CI
├── aliases/                  # runtime wrapper
└── agents/                   # 宿主元数据
```

## 设计标准

- 先判断机会，再进入设计
- 用真实工作和异常路径建模
- 同时定义动作、权限、证据、审计和 rollback
- 通过代表性 eval 与业务验收判断 pilot
- 把 production adoption 与 workflow impact 纳入交付结果
- 明确 launch、incident、containment、support 和 rollback
- 让 field signal 具备证据、分类、去向和 owner
- 每个可信交付都留下可复用资产

## 当前状态

核心 doctrine 已经稳定。仓库会继续吸收 Applied AI 与 FDE 实践，自动验证用于保证契约、模板、Skill、示例和文档在迭代中保持一致。

## License

MIT
