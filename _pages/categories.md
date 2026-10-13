---
layout: page
permalink: /categories/
title: Categories
description: Browse Code Dissolved posts by software development topic.
---

{% assign categories = site.categories | sort %}
{% for category in categories %}
<section class="archive-group" aria-labelledby="{{ category[0] | slugify }}">
  <h2 id="{{ category[0] | slugify }}">{{ category[0] | escape }}</h2>
  <ul>
    {% for post in category[1] %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
    {% endfor %}
  </ul>
</section>
{% endfor %}
