# Living-Pixels
**Seeing without Eyes — Distributed Vision!!**

Living Pixels is a bio-inspired simulation exploring how global visual patterns can emerge from purely local interactions. The project models a 2D grid of pixel-like agents that adapt their appearance based solely on local environmental sensing and neighbor communication—without any central controller, global image access, or explicit search.

Inspired by the remarkable camouflage abilities of cephalopods such as octopuses and cuttlefish, this simulation investigates how “seeing without eyes” can arise from decentralised biological systems. Cephalopods achieve rapid, high-resolution camouflage using specialized skin cells called chromatophores. Each chromatophore is locally controlled and responds to neural, chemical, and environmental signals, yet together they form coherent, environment-matching patterns across the entire body.

Emergent behavior is a hallmark of many biological systems. This project builds on ideas discussed in my OmniSci Magazine article, [Living Pixels](https://www.omniscimag.com/issue-9/living-pixels), which explores chromatophores as biological, color-changing pixels and their potential role in distributed sensing and bio-inspired computation!

## Project Overview
The current implementation:

1. Reads input from a camera or environment image.
2. Updates a synthetic skin array to locally match environmental colors.
3. Uses neighbor averaging, local difference, and noise to generate a camouflage effect.
4. Allows the skin to gradually converge to the same color distribution as the background, minimizing local visual differences.

## Future Improvements
Planned extensions include:

1. Dynamic pulsing with Perlin noise: Inspired by [this video](https://www.youtube.com/watch?v=DxUY42r_6Cg), using Perlin noise to drive pulsing would create more fluid, lifelike shimmering effects compared to a constant random parameter.

2. Edge-aware adaptive camouflage:  Integrate computer vision techniques such as edge detection to enable the skin to respond intelligently to patterns, not just colors, for more realistic and effective camouflage.
