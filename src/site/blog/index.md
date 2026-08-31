---
layout: default
title: Blog
eleventyExcludeFromCollections: true
---

# Blog

There's also an [RSS feed](/blog/feed.xml) you can subscribe to.

<ul class="post-list">
{% for post in collections.posts %}
  <li class="post-item">
    <span class="post-date">{{ post.date | date_est: false }}</span>
    <span class="post-separator"> — </span>
    <a href="{{ post.url }}" class="post-link">✍️ {{ post.data.title }}</a>
    {% if post.data.description %}<span class="post-desc">{{ post.data.description }}</span>{% endif %}
  </li>
{% else %}
  <li>No posts found.</li>
{% endfor %}
</ul>
