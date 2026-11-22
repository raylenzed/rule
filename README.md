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

19 份独立 AI 规则，只收这些软件自己的域名：

- **OpenAI**（`src/openai.yaml`）：OpenAI / ChatGPT / Sora
- **Claude**（`src/claude.yaml`）：Anthropic / Claude
- **GoogleAI**（`src/google-ai.yaml`）：Google AI / Gemini / AI Studio / NotebookLM / Antigravity
- **Grok**（`src/grok.yaml`）：xAI / Grok
- **Cursor**（`src/cursor.yaml`）：Cursor
- **Copilot**（`src/copilot.yaml`）：GitHub / Microsoft Copilot
- **Perplexity**（`src/perplexity.yaml`）：Perplexity
- **Poe**（`src/poe.yaml`）：Poe
- **MetaAI**（`src/meta-ai.yaml`）：Meta AI / Llama
- **Groq**（`src/groq.yaml`）：Groq
- **OpenRouter**（`src/openrouter.yaml`）：OpenRouter
- **Windsurf**（`src/windsurf.yaml`）：Windsurf / Codeium
- **Zed**（`src/zed.yaml`）：Zed AI
- **JetBrainsAI**（`src/jetbrains-ai.yaml`）：JetBrains AI / Junie / Grazie
- **Dify**（`src/dify.yaml`）：Dify
- **Jasper**（`src/jasper.yaml`）：Jasper AI
- **OpenArt**（`src/openart.yaml`）：OpenArt
- **Clipdrop**（`src/clipdrop.yaml`）：Clipdrop
- **CloudflareAI**（`src/cloudflare-ai.yaml`）：Cloudflare AI Gateway / Workers AI

## 订阅

将 `<Name>` 替换为上面任意规则名（如 `OpenAI`、`Claude`、`GoogleAI`、`Grok` 等）。

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
