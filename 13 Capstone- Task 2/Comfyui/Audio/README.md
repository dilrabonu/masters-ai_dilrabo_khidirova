# 🎵 Art Capstone – AI Reinterpretation of Michael Jackson’s *Dangerous*

## 🔸 Original Cover
![image](https://github.com/user-attachments/assets/50c07d73-d0a9-45cc-8971-7f3df336f21e)


---

## 🔸 AI-Generated Cover Variation
![image](https://github.com/user-attachments/assets/52f8ba76-1a59-48d4-97e8-e60c68059fba)

![image](https://github.com/user-attachments/assets/c059b8f1-3092-46c2-bbf5-9b13d10c85b5)



## 🔸 AI-Generated Cover Variation (LoRA Enhanced)
![image](https://github.com/user-attachments/assets/d2a16128-ab3b-4e54-ac88-d20ee577c320)

![image](https://github.com/user-attachments/assets/6fc9937b-7c2d-4441-ba10-5b2cc84967f2)


![image](https://github.com/user-attachments/assets/9d3dff97-047c-43c5-8dae-8921e58706fc)

alternative:
![image](https://github.com/user-attachments/assets/48f5e758-a302-4c46-82c8-83ef209514bf)




This image is a surreal reinterpretation of the iconic *Dangerous* album cover. It was created using a **self-hosted ComfyUI pipeline** with a fantasy-inspired **LoRA model** to enhance detail, symbolism, and artistic expression.

---


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

## 🧩 LoRA / Adapter Used

| Field         | Value |
|---------------|-------|
| **LoRA Name** | `album-covers-im_pony_style.safetensors` |
| **Strength (Model)** | `0.65` |
| **Strength (CLIP)**  | `0.65` |
| **LoRA Source** | [Civitai – Album Cover Art Style](https://civitai.com/models/106303/album-cover-art-style-lora) |

 **Prompt**         | `surreal royal carnival, album cover art, masked face, ornate gold frame, glowing elements, magical realism, fantasy palace, abstract symbolism` |
| **Negative Prompt**| `text, watermark, blurry, low contrast, logo` |

---

## 🖼️ Screenshot of Generation Pipeline

![Uploading image.png…]()


---

## 🛠️ Resources Used

- **Image Generation Model**: [Stable Diffusion v1.5 (pruned-emaonly-fp16)](https://huggingface.co/runwayml/stable-diffusion-v1-5)
- **Generation Platform**: (http://127.0.0.1:8188/)
- **Running Environment**: Self-hosted locally on Windows, GPU: RTX 3050 6GB, PyTorch 2.1.0
- **Prompt Engineering**: Custom written for surreal reinterpretation of MJ’s "Dangerous" cover.

---

## ✅ Notes

- No public image generation APIs were used.
- All processing was done locally using only self-hosted tools and open-source models.


