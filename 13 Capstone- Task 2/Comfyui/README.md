# 🎨 Generative AI Art Capstone – Reimagining Iconic Media Covers

## 👩‍🎓 Author: Dilrabo Khidirova  
**Program**: Generative AI Capstone  
**Specialization**: Data & AI, Visual Media Track  
**Tooling**: Self-hosted ComfyUI + Stable Diffusion + LoRA

---

## 🧠 Objective

The goal of this capstone project is to explore creative reinterpretation of iconic media artwork (album, film, book) using **Generative AI**, while maintaining originality, stylistic intent, and self-hosted ethical control. This work emphasizes **prompt engineering**, **self-hosted image generation**, and **narrative styling** through image composition.

---

## 🧩 Project Overview

| Media Type   | Title                    | Style Used            | LoRA Used         |
|--------------|--------------------------|------------------------|-------------------|
| 🎵 Album     | *Dangerous* – M. Jackson | Baroque Fantasy Cover | ✅ Yes            |
| 🎬 Film      | *Blade Runner 2049*      | Cyberpunk Poster      | ✅ Yes            |
| 📚 Book      | *The Little Prince*      | Watercolor Storybook  | ✅ Yes            |

Each piece was first created **without LoRA**, then enhanced using a **style-specific LoRA model** to enrich the result with more professional visual storytelling and texture.

---

## ⚙️ Technical Approach

All images were generated using:

- **Model**: `v1-5-pruned-emaonly-fp16.safetensors`
- **Platform**: Self-hosted ComfyUI
- **Prompts**: Custom-engineered for style, symbolism, and theme
- **LoRA**: Downloaded and integrated via Civitai; no cloud APIs used
- **Resolution**: 512x512 or 512x768 depending on layout
- **Sampler**: Euler (or Euler A)
- **CFG Scale**: 8.0
- **Steps**: 20–25

All work was done **offline using a local GPU** (NVIDIA RTX 3050), ensuring data privacy, reproducibility, and full control over generation pipelines.

---

## 🧠 Skills Demonstrated

- Prompt Design & Visual Language Control  
- Style Transfer using LoRA  
- Symbolic Visual Storytelling  
- Technical Workflow in ComfyUI  
- Self-hosted AI Implementation  
- Creative Direction & Aesthetic Framing

---

## ✅ Capstone Requirements Checklist

- [x] Three original works selected (album, film, book)  
- [x] AI-generated reinterpretations (at least one LoRA-enhanced per type)  
- [x] All content generated using self-hosted tools  
- [x] No API or third-party hosted generation platforms used  
- [x] Markdown documentation provided for each cover  
- [x] Screenshots of ComfyUI workflow saved and explained  
- [x] Clear creative direction and ethical AI usage  

---

## 📚 Deliverables

- `mj-dangerous.md` – Audio Album (LoRA)  
- `bladerunner2049.md` – Film Cover (LoRA)  
- `little-prince.md` – Book Cover (LoRA)  
- Associated images and pipeline screenshots  
- This general `README.md` file  

---

## 🙌 Reflection

This project allowed me to combine technical AI knowledge with artistic expression. Working fully self-hosted helped me understand how **fine-tuned visual results can be controlled**, enhanced, and aligned with storytelling goals. Each reinterpretation paid homage to the original while offering a **fresh perspective through generative imagination**.

---

## 🖋️ Created with vision, creativity, and care  
**– Dilrabo Khidirova**
