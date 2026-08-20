import pytest

import api_demo


def test_search_posts_returns_matching_items():
    posts = [
        {"id": 1, "title": "qui est esse", "body": "some body"},
        {"id": 2, "title": "dolor sit amet", "body": "another content"},
        {"id": 3, "title": "hello world", "body": "nothing matches"},
    ]

    result = api_demo.search_posts(posts, "qui")
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_search_posts_empty_keyword_returns_first_five():
    posts = [{"id": i, "title": f"title {i}", "body": "body"} for i in range(1, 10)]

    result = api_demo.search_posts(posts, "   ")
    assert len(result) == 5
    assert [p["id"] for p in result] == [1, 2, 3, 4, 5]


def test_write_report_creates_html_file(tmp_path):
    posts = [{"id": 1, "title": "Example title", "body": "sample content"}]
    out_file = tmp_path / "report.html"

    api_demo.REPORT_PATH = out_file
    api_demo.write_report("example", posts, posts)

    html = out_file.read_text(encoding="utf-8")
    assert "Example title" in html
    assert "sample content" in html
