---
layout: archive
title: "Projects"
permalink: /research/
author_profile: true
---

{% for post in site.research reversed %}
  {% include item-with-desc.html %}
{% endfor %}