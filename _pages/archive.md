---
layout: page
permalink: /archive/
title: Posts Archive
description: All posts from Code Dissolved, organized by year.
---

{% assign years = site.posts | group_by_exp: 'post', 'post.date | date: "%Y"' %}
{% for year in years %}
<section class="archive-group" aria-labelledby="year-{{ year.name }}">
  <h2 id="year-{{ year.name }}">{{ year.name }}</h2>
  <ul>
    {% for post in year.items %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
      — <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d" }}</time></li>
    {% endfor %}
  </ul>
</section>
{% endfor %}
