---
layout: default
title: Blog
eleventyExcludeFromCollections: true
pagination:
  data: collections.posts
  size: 20
  alias: posts
permalink: "blog/{% if pagination.pageNumber > 0 %}{{ pagination.pageNumber | plus: 1 }}/{% endif %}index.html"
---

# About this Blog

I started this blog on August 31, 2026.

You are welcome to read them if you find it interesting, though it's more of a public personal-reference thing.

[Here's a detailed post on why this blog exists](./hello-world).

If it somehow ends up influencing your life in a positive way, that's intentional. If the influence is negative, that's unintentional. Please do feel free to [hit me up](/) either way.

There's also an [RSS feed](/blog/feed.xml) you can subscribe to.

<ul class="post-list">
{% for post in pagination.items %}
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

{% if pagination.hrefs.size > 1 %}

<nav class="pagination" aria-label="Blog pages">
  <ul class="pagination-list">
    {%- if pagination.href.previous %}
    <li class="pagination-item pagination-prev">
      <a href="{{ pagination.href.previous }}" class="pagination-link">← Newer</a>
    </li>
    {%- endif %}
    {%- for pageHref in pagination.hrefs %}
    <li class="pagination-item">
      {%- if page.url == pageHref %}
      <span class="pagination-link pagination-link--current" aria-current="page">{{ forloop.index }}</span>
      {%- else %}
      <a href="{{ pageHref }}" class="pagination-link">{{ forloop.index }}</a>
      {%- endif %}
    </li>
    {%- endfor %}
    {%- if pagination.href.next %}
    <li class="pagination-item pagination-next">
      <a href="{{ pagination.href.next }}" class="pagination-link">Older →</a>
    </li>
    {%- endif %}
  </ul>
</nav>
{% endif %}
