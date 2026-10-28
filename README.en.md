# Chinese Document Simplifier

Turn wordy Chinese documents into clear prose while preserving facts, conditions,
uncertainty, and the writer's judgment. [中文说明](README.md)

This is a text-only Agent Skill for existing product descriptions, proposals,
review comments, and explanatory documents. It is designed for Chinese editing.

## Use

- **Rewrite:** return clearer prose with the source's meaning intact.
- **Audit:** report the location, reader impact, and smallest useful fix; do not rewrite the whole text.
- **Files:** read only for review requests. Write back only when the user asks to save changes.
  Preserve code, data, metadata, and link targets.

Download the Skill ZIP from [v0.2.0 Releases](https://github.com/cammy-shares/chinese-document-simplifier/releases/tag/v0.2.0),
then place the extracted `chinese-document-simplifier` folder in
`~/.agents/skills/` for local Codex use, following
[OpenAI Docs](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills).
Look for the Skill in the selector. If missing, check the folder layout and restart Codex.
Other hosts and this release's independent installation workflow have not been verified.

Example prompt:

```text
Use $chinese-document-simplifier to simplify the following Chinese document.
Preserve facts, conditions, uncertainty, and my judgment. Return the revised prose.
[paste source]
```

The [Chinese examples](examples.md) are manually authored, fictional expectations.
Automated checks cover package structure, relative links, and common privacy leak patterns.
No independent model comparison is complete; no superiority or success rate is claimed.
See [evaluation boundaries](EVALUATION.md).

The installed Skill has no scripts, telemetry, or network dependencies.
Your chosen AI host still processes submitted text.

## Rights and feedback

Free personal use includes your own daily work documents, including employment.
Selling, public redistribution, publishing adapted versions, integration into paid
products, paid editing services, and hosted multi-user deployment are not granted.
See [LICENSE](LICENSE) for the complete controlling terms and contribution exception.
This is a restricted personal-use license, not a standard open-source license.
Third-party rights remain unchanged; see [notices](THIRD_PARTY_NOTICES.md).

Submit redacted or synthetic failures through Issues. Maintainers decide whether
to merge PRs and publish official versions.
