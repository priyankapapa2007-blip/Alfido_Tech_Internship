import sys
from html import escape
from pathlib import Path

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
REPORT_PATH = Path(__file__).with_name("api_report.html")


def fetch_posts():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout as exc:
        raise RuntimeError("The API request timed out.") from exc
    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(f"The API returned HTTP {exc.response.status_code}.") from exc
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"A request error occurred: {exc}") from exc

    try:
        data = response.json()
    except ValueError as exc:
        raise RuntimeError("The API returned invalid JSON.") from exc

    if not isinstance(data, list):
        raise RuntimeError("The API response format was unexpected.")

    return data


def search_posts(posts, keyword):
    keyword = keyword.strip().lower()
    if not keyword:
        return posts[:5]

    matches = []
    for post in posts:
        title = str(post.get("title", "")).lower()
        body = str(post.get("body", "")).lower()
        if keyword in title or keyword in body:
            matches.append(post)
    return matches


def write_report(query, posts, matches):
    rows = ""
    for post in matches[:10]:
        rows += (
            "<tr>"
            f"<td>{post['id']}</td>"
            f"<td>{escape(post['title'])}</td>"
            f"<td>{escape(post['body'][:120])}</td>"
            "</tr>"
        )

    html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>API Demo Report</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    h1 {{ color: #1f4e79; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
    th {{ background: #f2f2f2; }}
  </style>
</head>
<body>
  <h1>Python API Demo</h1>
  <p>Fetched {len(posts)} posts from the JSONPlaceholder API.</p>
  <p>Search query: <strong>{escape(query)}</strong></p>
  <p>Matching posts: <strong>{len(matches)}</strong></p>
  <table>
    <thead>
      <tr><th>ID</th><th>Title</th><th>Preview</th></tr>
    </thead>
    <tbody>{rows}</tbody>
  </table>
</body>
</html>
"""
    REPORT_PATH.write_text(html, encoding="utf-8")


def main():
    query = sys.argv[1] if len(sys.argv) > 1 else "qui"

    try:
        posts = fetch_posts()
    except RuntimeError as exc:
        print(f"Error: {exc}")
        REPORT_PATH.write_text(
            "<html><body><h1>API Error</h1><p>Unable to load data.</p></body></html>",
            encoding="utf-8",
        )
        return 1

    matches = search_posts(posts, query)

    print(f"Fetched {len(posts)} posts from the API.")
    print(f"Found {len(matches)} matching posts for '{query}'.")
    for post in matches[:5]:
        print(f"- {post['id']}: {post['title']}")

    write_report(query, posts, matches)
    print(f"Saved HTML report to {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
