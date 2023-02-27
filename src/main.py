import arxiv
import requests
import json
import datetime

from settings import arxiv_keywords, arxiv_subject, DEEPL_API_KEY, DISCORD_WEBHOOK_URL


def send_discord(embed):
    webhook_url = DISCORD_WEBHOOK_URL
    main_content = {
        "content": embed["content"],
        "embeds": [{
            "description": embed["description"],
            "color": 3589078,
        }]
    }
    headers = {"Content-Type": "application/json"}
    requests.post(webhook_url, json.dumps(main_content), headers=headers)


def keyword_search(target_str: str, keywords: list) -> list:
    res = []
    for keyword in keywords:
        if keyword in target_str:
            res.append(keyword)
    return res


def translate(string: str) -> str:
    res = requests.get(
        "https://api-free.deepl.com/v2/translate",
        params={
            "auth_key": DEEPL_API_KEY,
            "text": string,
            "target_lang": "JA",
        },
    )
    return res.json()["translations"][0]["text"]


if __name__ == "__main__":
    date = (
        datetime.datetime.today() - datetime.timedelta(days=2)
    ).strftime("%Y%m%d")

    arxiv_query = \
        f"({arxiv_subject}) AND " \
        f"({' OR '.join(arxiv_keywords)}) AND " \
        f"submittedDate:" \
        f"[{date}000000 TO {date}235959]"

    search = arxiv.Search(
        query=arxiv_query,
        max_results=1000,
        sort_by=arxiv.SortCriterion.SubmittedDate,
    )

    send_discord(
        {
            "content": f"{date} の arxiv の更新通知",
            "description": f"検索条件: {arxiv_query}"
        }
    )

    for paper in search.results():
        paper_summary = paper.summary.replace("\n", " ")
        keywords = keyword_search(paper_summary, arxiv_keywords)
        if len(keywords) > 2:
            content = \
                f"title: {translate(paper.title)} \n " \
                f"url: {paper.entry_id} \n" \
                f"keywords: `{keywords}`"

            embed = {
                "content": content,
                "description": f"abstract: \n {translate(paper_summary)}",
            }

            send_discord(embed)

    send_discord(
        {
            "content": f"END: {date} の arxiv の更新通知",
            "description": "_"
        }
    )
