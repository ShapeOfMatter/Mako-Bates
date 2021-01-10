---
title: Posts
date: 2021-01-10 12:10:00 -05:00
layout: busy
---

{% for post in site.posts %}
 + [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
