# Chinese Document Simplifier

**Clear Chinese workplace documents, written for people.** [中文说明](README.md)

A text-only Agent Skill for Chinese workplace and technical writing.
Reduce AI-style filler, abstract wording, translationese, and sentences that nest
too many concepts, while preserving facts, technical terms, conditions, and judgment.

Core examples cover product descriptions, technical explanations, proposals, and
review feedback. The same editing rules also apply to work reports, process
instructions, and other explanatory documents; use is not limited to PRDs.

## Install

Requires Node.js 22.20.0+, npm / npx, and Git. Install the Skill for Codex:

```bash
npx --yes skills@1.7.4 add cammy-shares/chinese-document-simplifier --skill chinese-document-simplifier --agent codex --global --copy --yes
```

On Windows PowerShell, use `npx.cmd` instead of `npx`.
The user-level folder is `~/.agents/skills/`, or `%USERPROFILE%\.agents\skills\`
on Windows. Omit `--global` to install only in the current project.
Back up an existing same-name Skill before replacing it.

Alternatively, download the [v0.3.0 ZIP](https://github.com/cammy-shares/chinese-document-simplifier/releases/tag/v0.3.0)
and copy the complete extracted folder into the local Skills directory.
See [installation, updates, removal, and telemetry settings](INSTALL.md).
No plugin installation is required.

CLI file installation is tested in an isolated macOS project directory.
A real Windows run and an independent fresh-host model invocation are not verified.

## Use

- **Rewrite:** return clearer prose with the source's meaning intact.
- **Audit:** report the location, reader impact, and smallest useful fix without rewriting the whole text.
- **Files:** read only for review requests; write back only when the user asks to save changes.
  Preserve code, data, metadata, and link targets.

```text
Use $chinese-document-simplifier to simplify this Chinese workplace document.
Preserve facts, terms, conditions, uncertainty, and my judgment. Return the revised prose.
[paste source]
```

The [Chinese examples](examples.md) are manually authored, fictional expectations.
Automated checks cover package structure, relative links, and common privacy leak patterns.
No independent model comparison is complete; see [evaluation boundaries](EVALUATION.md).

The installed Skill has no scripts, telemetry, or network dependencies.
The third-party installation CLI has its own network and telemetry behavior.
Your chosen AI host still processes submitted text.

## Rights and feedback

Free personal use includes your own daily work documents, including employment.
Modifying the Skill, selling it, public redistribution, paid product integration,
paid editing services, and hosted multi-user deployment are not granted.
See [LICENSE](LICENSE) for the complete terms and contribution exception.
This is a restricted personal-use license, not a standard open-source license.
Third-party rights remain unchanged; see [notices](THIRD_PARTY_NOTICES.md).

Submit redacted or synthetic failures through Issues. Maintainers decide whether
to merge PRs and publish official versions.
