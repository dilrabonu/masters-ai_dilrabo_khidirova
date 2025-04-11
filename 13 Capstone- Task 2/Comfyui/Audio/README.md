# 🎵 Art Capstone – AI Reinterpretation of Michael Jackson’s *Dangerous*

## 🔸 Original Cover
![image](https://github.com/user-attachments/assets/50c07d73-d0a9-45cc-8971-7f3df336f21e)


---

## 🔸 AI-Generated Cover Variation
![image](https://github.com/user-attachments/assets/52f8ba76-1a59-48d4-97e8-e60c68059fba)
![Uploading image.png…]()



A surreal, symbolic reinterpretation of the iconic "Dangerous" album cover. This version was generated using a self-hosted ComfyUI pipeline, focusing on themes of royalty, fantasy, mystery, and ornate symbolism.

---

## ⚙️ Technical Workflow Summary

| Setting            | Value |
|--------------------|-------|
| **Model**          | `v1-5-pruned-emaonly-fp16.safetensors` |
| **Sampler**        | `euler` |
| **Steps**          | `20` |
| **CFG (Guidance)** | `8.0` |
| **Resolution**     | `512x512` |
| **Seed**           | `648713597659107` |
| **Denoise**        | `1.0` |
| **Prompt**         | `surreal royal carnival, golden ornate frame, mysterious masked face, eyes looking forward, baroque palace in background, animal statues, fantasy architecture, magical realism, intricate details, rich color palette, glowing elements, album art` |
| **Negative Prompt**| `text, watermark, blurry, low contrast, logo` |
| **LoRA / Extensions** | None |
| **Tool Used**      | ComfyUI (Self-hosted) |
| **Hardware**       | Local – NVIDIA RTX 3050 Laptop GPU (6 GB VRAM), 7.8 GB RAM |

---

## 🖼️ Screenshot of Generation Pipeline

![workflow](mj-dangerous-workflow.png)

---

## 🛠️ Resources Used

- **Image Generation Model**: [Stable Diffusion v1.5 (pruned-emaonly-fp16)](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- **Generation Platform**: [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- **Running Environment**: Self-hosted locally on Windows, GPU: RTX 3050 6GB, PyTorch 2.1.0
- **Prompt Engineering**: Custom written for surreal reinterpretation of MJ’s "Dangerous" cover.

---

## ✅ Notes

- No public image generation APIs were used.
- All processing was done locally using only self-hosted tools and open-source models.


