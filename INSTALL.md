# 安装说明

## 目录

- 命令行安装：Codex
- Windows 与 C 盘
- 手动 ZIP 安装
- 检查、更新与移除
- 验证到哪里

## 命令行安装：Codex

需要 Node.js 22.20.0 或更新版本、配套 npm / npx，以及可用的 Git。
此处使用第三方 [Skills CLI](https://github.com/vercel-labs/skills)，不是 Codex 插件。
安装工具版本固定为已验证的 1.7.4，Skill 从本仓库 main 获取当前版本。

**安装到当前用户，供各项目使用：**

```bash
npx --yes skills@1.7.4 add cammy-shares/chinese-document-simplifier --skill chinese-document-simplifier --agent codex --global --copy --yes
```

`--copy` 会复制完整 Skill 文件夹，不依赖符号链接。
如果已经安装同名 Skill，请先备份旧目录；`--yes` 会跳过安装确认。

**只安装到当前项目：** 在项目目录执行，去掉 `--global`。

```bash
npx --yes skills@1.7.4 add cammy-shares/chinese-document-simplifier --skill chinese-document-simplifier --agent codex --copy --yes
```

用户级目录是 `~/.agents/skills/`，项目级目录是 `.agents/skills/`。
目录依据 [OpenAI Docs](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)；
自定义宿主位置以实际配置为准。

Skills CLI 自身有遥测和安全查询配置。需要关闭时，在安装前设置
`DISABLE_TELEMETRY=1`；详见[工具的遥测说明](https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md#telemetry)。
这是安装工具的行为；安装的 Skill 本体只有文本指令。

## Windows 与 C 盘

在 Windows PowerShell 中使用 `npx.cmd`，避免 `npx.ps1` 的执行策略问题：

```powershell
npx.cmd --yes skills@1.7.4 add cammy-shares/chinese-document-simplifier --skill chinese-document-simplifier --agent codex --global --copy --yes
```

用户主目录通常位于 C 盘。安装目的地是
`%USERPROFILE%\.agents\skills\chinese-document-simplifier\`。
如果用户主目录实际在其他盘，以 `%USERPROFILE%` 为准，无须强制改成 C 盘根目录。

手动查看目录：在资源管理器地址栏输入 `%USERPROFILE%\.agents\skills`。
目录不存在时可自己创建；不需要把文件放进 Program Files。

**PowerShell 检查：**

```powershell
Test-Path (Join-Path $env:USERPROFILE '.agents\skills\chinese-document-simplifier\SKILL.md')
```

输出 `True` 表示文件在预期位置，不代表模型已完成调用。

若使用 WSL 中的 Codex，应在 WSL 的终端安装到 WSL 用户目录，
不要把 Windows 用户目录当成 WSL 的 `~`。

本项目没有在真实 Windows 系统执行本版本安装；上述路径与命令按工具规范提供。
当前已执行的安装验证范围见文末。

## 手动 ZIP 安装

1. 到 [v0.3.0 Releases](https://github.com/cammy-shares/chinese-document-simplifier/releases/tag/v0.3.0)
   下载 `chinese-document-simplifier-v0.3.0.zip`。
2. 解压后，找到包含 `SKILL.md`、`references/`、`agents/`、`LICENSE`
   和 `THIRD_PARTY_NOTICES.md` 的整个 `chinese-document-simplifier` 文件夹。
3. 放入用户级 Skills 目录，或项目的 `.agents/skills/`。
   已有同名目录时先备份，再替换整个文件夹。
4. 检查层级是 `skills/chinese-document-simplifier/SKILL.md`，不要多嵌套一层。
   不要只复制入口文件，否则参考规则与来源通知会缺失。

不安装 Node.js 的用户可以直接选择这种方式。
也可以从本仓库 `skills/chinese-document-simplifier/` 取得完整文件夹。
只需替换本 Skill，不要替换整个用户 Skills 目录。

## 检查、更新与移除

查看 Skills CLI 记录的用户级安装：

```bash
npx --yes skills@1.7.4 list --global --agent codex
```

项目级安装应在原项目目录运行，去掉 `--global`。
手动复制的 Skill 不一定被安装工具记录，仍需检查实际目录和宿主选择器。

在 Codex 的技能选择器查找“中文文档精简”或 `chinese-document-simplifier`。
CLI / IDE 可用 `/skills` 或输入 `$` 查找；未出现时检查路径并重启。
看到条目后，再显式调用它处理一小段不含隐私的文字。

更新时先备份同名目录，再重新执行同一安装命令；或下载新版 ZIP 替换整个 Skill 文件夹。
移除命令如下，执行前确认范围；保留交互确认以免误删：

```bash
npx --yes skills@1.7.4 remove chinese-document-simplifier --agent codex --global
```

Windows 对上述命令使用 `npx.cmd`。不要使用 `--all`，也不删除其他 Skills。

如果启动工具提示 Node 版本或 `styleText` 错误，确认 Node / npm / npx 来自同一套新版本安装。
可用以下命令检查安装子进程实际使用的 Node 版本：

```bash
npx --yes --package=skills@1.7.4 --call "node --version"
```

版本须为 22.20.0 或更新。更新 Node 后重新打开终端再安装，不需要降低系统安全策略。

## 验证到哪里

在 macOS 的隔离项目目录验证 CLI 发现本仓库 Skill 并复制完整安装文件，
逐个对照入口、参考资料、UI 元数据、许可和第三方通知。
没有为了验证而覆盖用户现有的全局 Skills。

文件安装成功、宿主能否发现、模型实际能否正确改写，是不同的验证层次。
真实 Windows 运行、独立 Codex 新会话调用及模型效果对照仍需另外验证。
