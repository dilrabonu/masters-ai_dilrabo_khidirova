


![image](https://github.com/user-attachments/assets/53ca18b8-45e4-48f7-928a-d18babcbe870)

![image](https://github.com/user-attachments/assets/aab59c8f-f064-4cc6-a651-5e790f73efb8)




Lora 
![image](https://github.com/user-attachments/assets/eaf0b7c4-a2b4-4ed9-8c18-66c54febb03c)



![image](https://github.com/user-attachments/assets/eaed1f91-74dc-474f-9213-2de6935d5d00)

# 🎬 Art Capstone Project – Blade Runner 2049 (AI Reimagined Cover)

## 🟡 Original Work
**Media Type**: DVD Film Box  
**Title**: *Blade Runner 2049*  
**Director**: Denis Villeneuve  
**Year**: 2017  

![Original Cover](film-org.jpg)

---

## 🔵 AI-Generated Reinterpretation

### Version 1 – No LoRA (Pure SD 1.5)
![No LoRA Result](bladerunner2049-no-lora.png)

A cyberpunk-style reinterpretation featuring a futuristic city, glowing lights, and a team of silhouettes walking into a dystopian world — inspired by *Blade Runner 2049*.

### Version 2 – With LoRA (Enhanced Detail & Style)
![LoRA Result](bladerunner2049-lora-version.png)

This variation uses the Album Cover Art Style LoRA to enhance structure, richness, cinematic tones, and neon-lit atmosphere while preserving the sci-fi narrative.

---

## ⚙️ Workflow

All generations were done using **ComfyUI (self-hosted)** with full control over model loading, prompts, conditioning, and output configuration.

| Element              | Value                                              |
|----------------------|----------------------------------------------------|
| Base Model           | `v1-5-pruned-emaonly-fp16.safetensors`             |
| Platform             | ComfyUI (Local Self-Hosted)                        |
| GPU Used             | NVIDIA RTX 3050 6GB (Laptop)                       |
| OS & Memory          | Windows, 7.8 GB RAM                                |
| Sampler              | Euler                                              |
| Steps                | 20                                                 |
| CFG Scale            | 8.0                                                |
| Resolution           | 512 x 768                                          |
| Denoise Strength     | 1.0                                                |
| Seed                 | Randomized / Fixed for LoRA                        |

---

## 🎯 Prompt Engineering

### Positive Prompt (LoRA + No-LoRA)
cinematic cyberpunk movie poster, three futuristic characters walking together through a neon-lit dystopian city, trench coats, glowing signs, rain reflections, orange and blue lighting, moody atmosphere, high-tech skyscrapers, fog, blade runner 2049 inspired, symmetrical composition, ultra-detailed, retro-futurism, dramatic contrast, backlight silhouettes




### Negative Prompt
text, watermark, logo, blurry, distorted, bad anatomy, lowres, cropped



---

## 🧩 LoRA Integration

| Field          | Value                                              |
|----------------|----------------------------------------------------|
| LoRA Name      | `album-cover-style.safetensors`                    |
| Source         | [Civitai – Album Cover Style LoRA](https://civitai.com/models/106303) |
| Strength Model | 0.65                                               |
| Strength CLIP  | 0.65                                               |

---

## 🖼️ Workflow Snapshots

### No-LoRA Pipeline Screenshot
![Workflow – No LoRA](bladerunner2049-no-lora-workflow.png)

### LoRA-Enhanced Pipeline Screenshot
![Workflow – With LoRA](bladerunner2049-lora-workflow.png)

---

## 📚 Resources Used

- [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [Album Cover Style LoRA on Civitai](https://civitai.com/models/106303)

---

## ✅ Capstone Compliance

- [x] Original media selected: DVD Film Cover  
- [x] Self-hosted ComfyUI used (no cloud API, no online platforms)  
- [x] Prompt-engineered and LoRA-enhanced variant created  
- [x] Screenshot of pipeline included  
- [x] Markdown file documents all technical and creative decisions

---

**Author**: Dilrabo Khidirova  
**Project**: Art Capstone – Generative AI Media Reimagination  
**Instructor**: [Your Instructor’s Name or Course Title]


