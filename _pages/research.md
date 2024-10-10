---
layout: archive
title: "Projects"
permalink: /research/
author_profile: true
---

{% assign sorted_posts = site.research | sort: 'order' %}
{% for post in sorted_posts %}
  {% include item-with-desc.html %}
{% endfor %}
