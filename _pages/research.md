---
layout: archive
title: "Research Interest"
permalink: /research/
author_profile: true
---

> My research focuses on understanding the bacterial diversity and ecology within the gut microbiome of animals. My work is driven by exciting, modern sequencing technologies and bioinformatic approaches that achieve in hours what once took months or was previously practically unachievable over a decade ago.

> Through my PhD I have been studying how microbiomes operate at the strain-level which is an important open question given that the definition of strain has been a point of contention. It is especially important to understand strain-level patterns and interactions to enable engineering microbiomes towards the development of microbial consortia for specific applications. I have been investigating the eco-evolutionary paterns and processes shaping bacterial communities in the gut microbiome of honeybees. I am also using synthetic gut microbial communities to address to understand how strains interact with each other in the context of a whole community of other microbes.


{% assign sorted_posts = site.research | sort: 'order' %}
{% for post in sorted_posts %}
  {% include item-with-desc.html %}
{% endfor %}
