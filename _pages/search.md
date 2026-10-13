---
layout: page
title: Search
permalink: /search/
description: Search Code Dissolved posts by title or topic.
sitemap: false
---

<div id="search-container">
  <label for="search-input">Search posts by title or topic</label>
  <input type="search" id="search-input" placeholder="For example, Rails or Flask" autocomplete="off" aria-controls="results-container">
  <p id="search-status" role="status"></p>
  <ul id="results-container" aria-label="Search results"></ul>
  <p>You can also browse the <a href="{{ '/archive/' | relative_url }}">post archive</a>.</p>
  <noscript>Search requires JavaScript.</noscript>
</div>

<script src="{{ '/assets/search.js' | relative_url }}" data-index="{{ '/search.json' | relative_url }}" defer></script>
