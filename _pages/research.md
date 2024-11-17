---
layout: archive
title: "Projects"
permalink: /research/
author_profile: true
---

<!-- My research focuses on understanding the bacterial diversity and interaction between the bacteria and their environment, particularly within the gut microbiome of animals. My work is driven by the excitement of utilizing modern sequencing technologies and bioinformatic approaches to achieve in hours what once took months or was previously impossible. I enjoy actively engaging in discussions with peers with varied expertise and to intiate and maintain collaborations.

Starting as an underdraguate thesis student I set up a Nanopore sequencing system in India to study the human gut microbiome of clinical samples marking my first foray into cutting-edge sequencing approaches and bioinformatics. Since then, I then moved to Lausanne to pursue my PhD where I started with the the goal of comparing gut microbiome diversity across different animal species to understand their evolution and ecology. First though we needed to decide how to define a bacterial species from bioinformatics data (which when I started was still a point of contention). This question has since been answered and substantiated with unprecendented amounts of data to which I have been contributing. Applying this and other recent approaches in shotgun metagenomics, my work has shed light on the gut microbiome of honeybees and how it is shaped by evolution and host ecology.

I am also motivated to understand how microbiomes operate at the strain-level which is an important open question especially given that the definition of strain has been a point of contention. This is especially important to enable engineering microbiomes towards the development of microbial consortia for specific applications. I have been working using strain-level analysis approaches to understand the dynamics of bacterial communities in the gut microbiome of honeybees. I am also using synthetic gut microbial communities to address to understand how strains interact with each other in the context of a whole community of other similar strains and different species. -->

Selected talk featuring my most recent work on the gut microbiome of honeybees:

<iframe src="https://cassyni.com/embed/events/MiMvAGXxaxTMCvZ75uqhpy" title="Evolution and Functional Potential of Gut Microbiota in Honeybees: A Comparative Metagenomic Approach - presented by Aiswarya Prasad (Cassyni)" frameBorder="0" scrolling="no" style="width:100%;height:100%;aspect-ratio:16/9;max-width:100%" allow="fullscreen; accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"></iframe>

{% assign sorted_posts = site.research | sort: 'order' %}
{% for post in sorted_posts %}
  {% include item-with-desc.html %}
{% endfor %}
