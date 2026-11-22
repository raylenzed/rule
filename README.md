# rule

自己维护的分流规则。按客户端分目录，同一套域名四种格式。

```
src/*.yaml            源，改这里
rule/Clash/           Mihomo / Clash Meta，yaml
rule/Stash/           Stash，.list
rule/Surge/           Surge，.list
rule/Shadowrocket/    小火箭，.list
```

漏了域名：改 `src/` 下对应的 `.yaml`，再跑 `python3 scripts/generate.py`。

## 现在有什么

6 份独立 AI 规则，只收这些软件自己的域名：

- **OpenAI**（`src/openai.yaml`）：OpenAI / ChatGPT / Sora
- **Claude**（`src/claude.yaml`）：Anthropic / Claude
- **Grok**（`src/grok.yaml`）：xAI / Grok
- **Cursor**（`src/cursor.yaml`）：Cursor
- **Copilot**（`src/copilot.yaml`）：GitHub / Microsoft Copilot
- **Gemini**（`src/gemini.yaml`）：Google AI / Gemini / AI Studio / NotebookLM

## 订阅

将 `<Name>` 替换为 `OpenAI`、`Claude`、`Grok`、`Cursor`、`Copilot` 或 `Gemini`。

Clash / Mihomo（`behavior: classical`）：

```
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Clash/<Name>.yaml
```

Stash / Surge / 小火箭：

```
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Stash/<Name>.list
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Surge/<Name>.list
https://cdn.jsdelivr.net/gh/raylenzed/rule@main/rule/Shadowrocket/<Name>.list
```

jsDelivr 不稳就换 `testingcf.jsdelivr.net`。
