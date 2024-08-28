---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% if site.talkmap_link == true %}

<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of the places I've worked or presented my work!</a></p>

{% endif %}

{% for post in site.research reversed %}
  {% include gallery %}
{% endfor %}