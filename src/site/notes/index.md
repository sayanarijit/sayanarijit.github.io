---
layout: default
---

# About these Notes

I started dumping notes here since March 29, 2022 in an attempt to organise and share my personal knowledge.

Hence, some notes here are knowledge intended for myself, while some are knowledge I feel others might find useful.

Basically, this is my [[digital garden]], organized by tags.

There's also an [[RSS feed]] you can subscribe to.

> ⚠️ These notes may not always be correct, as they contain my personal interpretation of things.

# Tags

<ul>
{% for tag in collections.tagList %}
  <li><a href="/tags/{{ tag }}" class="post-tag">🏷️ {{ tag }}</a></li>
{% endfor %}
</ul>
