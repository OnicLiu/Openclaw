# OpenClaw CLI 指令指南

本文件匯總了 OpenClaw CLI 的指令行為、詳細說明、範例以及參數用法。

## 概覽

OpenClaw CLI 提供了豐富的命令集，用於管理代理、Gateway、通道、技能、記憶體、節點和瀏覽器等功能。

### 全局旗標 (Global Flags)

*   `--dev`: 在 `~/.openclaw-dev` 下隔離狀態，並調整預設端口。
*   `--profile <name>`: 在 `~/.openclaw-<name>` 下隔離狀態。
*   `--no-color`: 禁用 ANSI 顏色輸出。
*   `--update`: `openclaw update` 的簡寫 (僅限源碼安裝)。
*   `-V, --version, -v`: 顯示版本並退出。

### 輸出樣式 (Output Styling)

*   ANSI 顏色和進度指示器僅在 TTY 會話中渲染。
*   OSC-8 超連結在支援的終端中顯示為可點擊連結。
*   `--json` (和支援的 `--plain`) 禁用樣式，提供簡潔輸出。
*   `--no-color` 禁用 ANSI 樣式。
*   長時間運行的命令會顯示進度指示器。

### 顏色調色板 (Color Palette)

OpenClaw CLI 輸出使用龍蝦調色板，包含 `accent`, `accentBright`, `accentDim`, `info`, `success`, `warn`, `error`, `muted` 等顏色。

### 命令樹 (Command Tree)

`openclaw [--dev] [--profile <name>] <command>`

主要的命令包括：
*   `setup`
*   `onboard`
*   `configure`
*   `config`
*   `doctor`
*   `security`
*   `reset`
*   `uninstall`
*   `update`
*   `channels`
*   `skills`
*   `plugins`
*   `memory`
*   `message`
*   `agent`
*   `agents`
*   `acp`
*   `status`
*   `health`
*   `sessions`
*   `gateway`
*   `logs`
*   `system`
*   `models`
*   `sandbox`
*   `cron`
*   `nodes`
*   `devices`
*   `node`
*   `approvals`
*   `browser`
*   `hooks`
*   `webhooks`
*   `pairing`
*   `docs`
*   `dns`
*   `tui`

**(注意：插件可以添加額外的頂級命令，例如 `openclaw voicecall`)**

## 安全 (Security)

*   `openclaw security audit`: 審計配置和本地狀態，檢查常見的安全風險。
*   `openclaw security audit --deep`: 深度探測運行中的 Gateway。
*   `openclaw security audit --fix`: 強化安全預設值並調整狀態/配置的權限。

## 插件 (Plugins)

管理擴展和其配置：

*   `openclaw plugins list`: 列出插件 (`--json` 用於機器可讀輸出)。
*   `openclaw plugins info <id>`: 顯示插件詳情。
*   `openclaw plugins install <id>`: 安裝插件 (或添加插件路徑到 `plugins.load.paths`)。
*   `openclaw plugins enable / disable <id>`: 切換 `plugins.entries.<id>.enabled`。
*   `openclaw plugins doctor`: 報告插件載入錯誤。

(大多數插件更改需要重啟 Gateway。)

## 記憶體 (Memory)

在 `MEMORY.md` + `memory/*.md` 上進行向量搜尋：

*   `openclaw memory status`: 顯示索引狀態。
*   `openclaw memory index`: 重新索引記憶體文件。
*   `openclaw memory search "<query>"`: 對記憶體進行語義搜尋。

## 聊天斜線指令 (Chat Slash Commands)

聊天訊息支援 `/...` 命令 (文本和原生)。

*   `/status`: 快速診斷。
*   `/config`: 持久化配置更改。
*   `/debug`: 僅運行時配置覆蓋 (非磁盤；需要 `commands.debug: true`)。

## 設定 + 入門 (Setup + Onboarding)

### setup

初始化配置 + 工作區。
選項：
*   `--workspace <path>`: 代理工作區路徑 (預設 `~/.openclaw/workspace`)。
*   `--wizard`: 運行入門嚮導。
*   `--non-interactive`: 無提示運行嚮導。
*   `--mode <mode>`: 嚮導模式。
*   `--remote-url <url>`: 遠端 Gateway URL。
*   `--remote-token <token>`: 遠端 Gateway Token。

### onboard

交互式嚮導，用於設置 Gateway、工作區和技能。
選項：
*   `--workspace`
*   `--reset`: 重置配置 + 憑據 + 會話 + 工作區後運行嚮導。
*   `--non-interactive`
*   `--mode`
*   `--flow` (manual 是 advanced 的別名)
*   `--auth-choice`
*   `--token-provider` (非交互式；與 `--auth-choice token` 搭配使用)
*   `--token` (非交互式；與 `--auth-choice token` 搭配使用)
*   `--token-profile-id` (非交互式；預設 `:manual`)
*   `--token-expires-in` (非交互式；例如 `365d, 12h`)
*   `--anthropic-api-key`
*   `--openai-api-key`
*   `--openrouter-api-key`
*   `--ai-gateway-api-key`
*   `--moonshot-api-key`
*   `--kimi-code-api-key`
*   `--gemini-api-key`
*   `--zai-api-key`
*   `--minimax-api-key`
*   `--opencode-zen-api-key`
*   `--gateway-port`
*   `--gateway-bind`
*   `--gateway-auth`
*   `--gateway-token`
*   `--gateway-password`
*   `--remote-url`
*   `--remote-token`
*   `--tailscale`
*   `--tailscale-reset-on-exit`
*   `--install-daemon`
*   `--no-install-daemon` (別名: `--skip-daemon`)
*   `--daemon-runtime`
*   `--skip-channels`
*   `--skip-skills`
*   `--skip-health`
*   `--skip-ui`
*   `--node-manager` (推薦 pnpm；不推薦 bun 用於 Gateway 運行時)
*   `--json`

### configure

交互式配置嚮導 (模型、通道、技能、Gateway)。

### config

非交互式配置輔助工具 (get/set/unset)。不帶子命令運行 `openclaw config` 會啟動嚮導。
子命令：
*   `config get <path>`: 打印配置值 (點/括號路徑)。
*   `config set <path> <value>`: 設置值 (JSON5 或原始字符串)。
*   `config unset <path>`: 移除值。

### doctor

健康檢查 + 快速修復 (配置 + Gateway + 舊服務)。
選項：
*   `--no-workspace-suggestions`: 禁用工作區記憶提示。
*   `--yes`: 無提示接受預設值。
*   `--non-interactive`: 跳過提示；僅應用安全遷移。
*   `--deep`: 掃描系統服務以獲取額外的 Gateway 安裝。

## 通道輔助工具 (Channel Helpers)

### channels

管理聊天通道帳戶 (WhatsApp/Telegram/Discord/Google Chat/Slack/Mattermost (插件)/Signal/iMessage/MS Teams)。
子命令：
*   `channels list`: 顯示已配置的通道和認證配置文件。
*   `channels status`: 檢查 Gateway 可達性和通道健康狀況 (`--probe` 運行額外檢查)。
*   `channels logs`: 顯示 Gateway 日誌文件中的最近通道日誌。
*   `channels add`: 嚮導式設置 (無旗標時)；帶旗標切換到非交互模式。
*   `channels remove`: 預設禁用；傳遞 `--delete` 移除配置條目。
*   `channels login`: 交互式通道登錄 (僅限 WhatsApp Web)。
*   `channels logout`: 登出通道會話 (如果支援)。

通用選項：
*   `--channel <name>`: `whatsapp|telegram|discord|googlechat|slack|mattermost|signal|imessage|msteams`
*   `--account <id>`: 通道帳戶 ID (預設 `default`)。
*   `--name <name>`: 帳戶顯示名稱。

範例：
*   `openclaw channels add --channel telegram --account alerts --name "Alerts Bot" --token $TELEGRAM_BOT_TOKEN`
*   `openclaw channels status --probe`

### skills

列出和檢查可用技能及其就緒信息。
子命令：
*   `skills list`: 列出技能 (無子命令時預設)。
*   `skills info <id>`: 顯示技能詳情。
*   `skills check`: 總結就緒與缺失要求。

選項：
*   `--eligible`: 僅顯示就緒技能。
*   `--json`: 輸出 JSON (無樣式)。
*   `-v, --verbose`: 包含缺失要求詳情。

### pairing

批准跨通道的 DM 配對請求。
子命令：
*   `pairing list [--json]`
*   `pairing approve [--notify]`

### webhooks gmail

Gmail Pub/Sub 鉤子設置 + 運行器。
子命令：
*   `webhooks gmail setup`: 設置 Gmail Pub/Sub 鉤子 (需要 `--account`，支援多種選項)。
*   `webhooks gmail run`: 運行時覆蓋相同旗標。

### dns setup

廣域發現 DNS 輔助工具 (CoreDNS + Tailscale)。
選項：
*   `--apply`: 安裝/更新 CoreDNS 配置 (需要 sudo；僅限 macOS)。

## 訊息 + 代理 (Messaging + Agent)

### message

統一的出站訊息 + 通道操作。
子命令：
*   `message send|poll|react|reactions|read|edit|delete|pin|unpin|pins|permissions|search|timeout|kick|ban`
*   `message thread`
*   `message emoji`
*   `message sticker`
*   `message role`
*   `message channel`
*   `message member info`
*   `message voice status`
*   `message event`

範例：
*   `openclaw message send --target +15555550123 --message "Hi"`
*   `openclaw message poll --channel discord --target channel:123 --poll-question "Snack?" --poll-option Pizza --poll-option Sushi`

### agent

通過 Gateway (或 `--local` 嵌入式) 運行一個代理回合。
必需：
*   `--message <text>`

選項：
*   `--to <session_key>` (用於會話鍵和可選的交付)
*   `--session-id <id>`
*   `--thinking <level>`
*   `--verbose`
*   `--channel <name>`
*   `--local`
*   `--deliver`
*   `--json`
*   `--timeout`

### agents

管理獨立代理 (工作區 + 認證 + 路由)。

#### agents list

列出已配置的代理。
選項：
*   `--json`
*   `--bindings`

#### agents add [name]

添加新的獨立代理。運行引導式嚮導，除非傳遞旗標 (或 `--non-interactive`)；在非交互模式下需要 `--workspace`。
選項：
*   `--workspace`
*   `--model`
*   `--agent-dir`
*   `--bind` (可重複)
*   `--non-interactive`
*   `--json`

#### agents delete

刪除代理並清理其工作區 + 狀態。
選項：
*   `--force`
*   `--json`

### acp

運行連接 IDE 到 Gateway 的 ACP 橋接。

### status

顯示鏈接的會話健康狀況和最近的接收者。
選項：
*   `--json`
*   `--all` (完整診斷；只讀，可粘貼)
*   `--deep` (探測通道)
*   `--usage` (顯示模型提供者使用/配額)
*   `--timeout`
*   `--verbose`
*   `--debug` (別名 `--verbose`)

### health

從運行中的 Gateway 獲取健康狀況。
選項：
*   `--json`
*   `--timeout`
*   `--verbose`

### sessions

列出存儲的會話。
選項：
*   `--json`
*   `--verbose`
*   `--store`
*   `--active`

## 重置 / 卸載 (Reset / Uninstall)

### reset

重置本地配置/狀態 (CLI 仍保持安裝)。
選項：
*   `--scope`
*   `--yes`
*   `--non-interactive`
*   `--dry-run`

### uninstall

卸載 Gateway 服務 + 本地數據 (CLI 仍保持)。
選項：
*   `--service`
*   `--state`
*   `--workspace`
*   `--app`
*   `--all`
*   `--yes`
*   `--non-interactive`
*   `--dry-run`

## Gateway

### gateway

運行 WebSocket Gateway。
選項：
*   `--port`
*   `--bind`
*   `--token`
*   `--auth`
*   `--password`
*   `--tailscale`
*   `--tailscale-reset-on-exit`
*   `--allow-unconfigured`
*   `--dev`
*   `--reset`
*   `--force`
*   `--verbose`
*   `--claude-cli-logs`
*   `--ws-log`
*   `--compact`
*   `--raw-stream`
*   `--raw-stream-path`

### gateway service

管理 Gateway 服務 (launchd/systemd/schtasks)。
子命令：
*   `gateway status`: (預設探測 Gateway RPC)
*   `gateway install`: (服務安裝)
*   `gateway uninstall`
*   `gateway start`
*   `gateway stop`
*   `gateway restart`

### logs

通過 RPC 追蹤 Gateway 文件日誌。
範例：
*   `openclaw logs --follow`
*   `openclaw logs --limit 200`

### gateway (RPC)

Gateway CLI 輔助工具 (使用 `--url`, `--token`, `--password`, `--timeout`, `--expect-final` 用於 RPC 子命令)。
子命令：
*   `gateway call [--params <json>]`
*   `gateway health`
*   `gateway status`
*   `gateway probe`
*   `gateway discover`
*   `gateway install|uninstall|start|stop|restart`
*   `gateway run`

常用 RPCs：
*   `config.apply` (驗證 + 寫入配置 + 重啟 + 喚醒)
*   `config.patch` (合併部分更新 + 重啟 + 喚醒)
*   `update.run` (運行更新 + 重啟 + 喚醒)

## 模型 (Models)

### models (根)

`openclaw models` 是 `models status` 的別名。
根選項：
*   `--status-json` (別名 `models status --json`)
*   `--status-plain` (別名 `models status --plain`)

### models list

選項：
*   `--all`
*   `--local`
*   `--provider`
*   `--json`
*   `--plain`

### models status

選項：
*   `--json`
*   `--plain`
*   `--check` (退出 1=過期/缺失，2=即將過期)
*   `--probe` (對已配置的認證配置文件進行實時探測)
*   `--probe-provider`
*   `--probe-profile`
*   `--probe-timeout`
*   `--probe-concurrency`
*   `--probe-max-tokens`

### models set

設置 `agents.defaults.model.primary`。

### models set-image

設置 `agents.defaults.imageModel.primary`。

### models aliases list|add|remove

### models fallbacks list|add|remove|clear

### models image-fallbacks list|add|remove|clear

### models scan

選項：
*   `--min-params`
*   `--max-age-days`
*   `--provider`
*   `--max-candidates`
*   `--timeout`
*   `--concurrency`
*   `--no-probe`
*   `--yes`
*   `--no-input`
*   `--set-default`
*   `--set-image`
*   `--json`

### models auth add|setup-token|paste-token

選項：
*   `add`: 交互式認證輔助工具。
*   `setup-token`: `--provider` (預設 `anthropic`), `--yes`
*   `paste-token`: `--provider <name>`, `--profile-id <id>`, `--expires-in <duration>`

### models auth order get|set|clear

選項：
*   `get`: `--provider <name>`, `--agent <id>`, `--json`
*   `set`: `--provider <name>`, `--agent <id>`, `<profile_id...>`
*   `clear`: `--provider <name>`, `--agent <id>`

## 系統 (System)

### system event

將系統事件排入隊列並可選地觸發心跳 (Gateway RPC)。
必需：
*   `--text <message>`

選項：
*   `--mode`
*   `--json`

### system heartbeat last|enable|disable

心跳控制 (Gateway RPC)。

### system presence

列出系統存在條目 (Gateway RPC)。

## Cron

管理排程任務 (Gateway RPC)。

子命令：
*   `cron status [--json]`
*   `cron list [--all] [--json]`
*   `cron add` (別名: `create`；需要 `--name` 和 `--at | --every | --cron` 中的一個，以及 `--system-event | --message` 中的一個 payload)
*   `cron edit` (修補字段)
*   `cron rm` (別名: `remove`, `delete`)
*   `cron enable`
*   `cron disable`
*   `cron runs --id <id> [--limit <num>]`
*   `cron run [--force]`

## 節點主機 (Node Host)

`node` 運行無頭節點主機或將其作為後台服務管理。
子命令：
*   `node run --host --port 18789`
*   `node status`
*   `node install`
*   `node uninstall`
*   `node stop`
*   `node restart`

## 節點 (Nodes)

`nodes` 與 Gateway 通信並目標配對的節點。
子命令：
*   `nodes status [--connected] [--last-connected <duration>]`
*   `nodes describe --node <id|name>`
*   `nodes list [--connected] [--last-connected <duration>]`
*   `nodes pending`
*   `nodes approve`
*   `nodes reject`
*   `nodes rename --node <id|name> --name <new_name>`
*   `nodes invoke --node <id|name> --command <command> [--params <json>]`
*   `nodes run --node <id|name> [--cwd <path>] [--env KEY=VAL] [--command-timeout <ms>] [--needs-screen-recording] [--invoke-timeout <ms>]`
*   `nodes notify --node <id|name> [--title <text>] [--body <text>] [--sound <sound_id>] [--priority <level>] [--delivery <mode>]`

相機：
*   `nodes camera list --node <id|name>`
*   `nodes camera snap --node <id|name> [--facing front|back|both]`
*   `nodes camera clip --node <id|name> [--facing front|back] [--duration <duration>]`

Canvas + 屏幕：
*   `nodes canvas snapshot --node <id|name> [--format png|jpg|jpeg]`
*   `nodes canvas present --node <id|name> [--target <url>] [--x <num>] [--y <num>] [--width <num>] [--height <num>]`
*   `nodes canvas hide --node <id|name>`
*   `nodes canvas navigate --node <id|name> [--url <url>]`
*   `nodes canvas eval [] --node <id|name> [--js <javascript>]`
*   `nodes canvas a2ui push --node <id|name> (--jsonl <jsonl_data> | --text <text>)`
*   `nodes canvas a2ui reset --node <id|name>`
*   `nodes screen record --node <id|name> [--screen <index>] [--duration <duration>]`

位置：
*   `nodes location get --node <id|name> [--max-age <ms>] [--accuracy coarse|balanced|precise]`

## 瀏覽器 (Browser)

瀏覽器控制 CLI (專用 Chrome/Brave/Edge/Chromium)。

管理：
*   `browser status`
*   `browser start`
*   `browser stop`
*   `browser reset-profile`
*   `browser tabs`
*   `browser open`
*   `browser focus`
*   `browser close [targetId]`
*   `browser profiles`
*   `browser create-profile --name <name>`
*   `browser delete-profile --name <name>`

檢查：
*   `browser screenshot [targetId] [--full-page] [--ref <ref>] [--element <ref>] [--type png|jpeg]`
*   `browser snapshot [--format aria|ai] [--target-id <id>] [--limit <num>]`

操作：
*   `browser navigate [--target-id <id>] [--url <url>]`
*   `browser resize [--target-id <id>] [--width <num>] [--height <num>]`
*   `browser click [--double] [--button left|middle|right] [--modifiers alt|control|meta|shift]`
*   `browser type [--submit] [--slowly] [--text <text>]`
*   `browser press [--key <key>]`
*   `browser hover`
*   `browser drag`
*   `browser select`
*   `browser upload`
*   `browser fill [--fields <json>]`
*   `browser dialog --accept|--dismiss`
*   `browser wait [--time <ms>] [--text <text>] [--text-gone <text>]`
*   `browser evaluate --fn <javascript_fn_name> [--ref <ref>]`
*   `browser console [--level trace|debug|info|warn|error] [--target-id <id>]`
*   `browser pdf [--target-id <id>]`

## 文檔搜尋 (Docs Search)

### docs [query...]

搜尋實時文檔索引。

## TUI (終端 UI)

### tui

打開連接到 Gateway 的終端 UI。
選項：
*   `--url`
*   `--token`
*   `--password`
*   `--session`
*   `--deliver`
*   `--thinking`
*   `--message`
*   `--timeout-ms`
*   `--history-limit`
