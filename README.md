# arXiv to Discord

arXiv の新着論文を Discord に通知するスクリプト。

毎朝、指定したカテゴリ、日付の arXiv の新着論文のうち、指定したキーワードにヒットするもののタイトル, URL, Abstract の和訳を DeepL で翻訳したものを Discord に通知する。

## 環境変数

- `DEEPL_API_KEY`: DeepL の API Key
- `DISCORD_WEBHOOK_URL`: Discord の Webhook URL
