---
title: Paper Reviews
---

These are casual summaries, notes about, and in some cases critiques of papers that I've read or used in different contexts.
They're not organized, they vary is structure and quality, and they're probably not of use to anyone.

{% assign posts = site.papers | sort: "date" | reverse %}
{% for post in posts %}
 + [{{ post.title }}]({{ post.url | absolute_url }})
{% endfor %}
