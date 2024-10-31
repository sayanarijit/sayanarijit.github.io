---
layout: note
tags:
  - tech
  - computer-science
  - learning
  - ai
---

# GraphRAG

Using GraphRAG approach, we can make LLMs capable of answering more accurately from
private data, along with references to the data points that support the answer.

This approach generally works better than simple semantic (vector) search by overcoming
its inability to retrive enough relevant context for the questions in most cases.

The approach involves using LLMs to analyse the given private data, generate metadata
about each data point, build graph of communities from the generated metadata, generate
metadata about each community, and build a graph of communities of communities and so on.

This helps LLMs to gather relevant context faster and more accurately, by searching the
metadata to find relevant data points faster, and sometimes even provide accurate answers
that are not directly present in the data, but was discovered during graph generation.

- https://microsoft.github.io/graphrag/
- https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/
- https://github.com/noworneverev/graphrag-visualizer
