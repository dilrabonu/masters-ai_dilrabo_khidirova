
model :
 https://huggingface.co/runwayml/stable-diffusion-v1-5


original photo:

![image](https://github.com/user-attachments/assets/d72f2077-ea3a-44c5-8190-9d52515322a8)


link of model:
https://huggingface.co/aifoundry-org/FLUX.1-schnell-Quantized/tree/main

![image](https://github.com/user-attachments/assets/7634248c-b65a-4b3a-8aad-82eca5ce16e8)

# Art Capstone - AI-Generated Media Covers

## 1. CD Album – Rammstein: MUTTER

**Original Cover**  
![original](original_mutter.png)

**AI-Generated Cover**  
![ai-generated](ai_mutter.png)

### Workflow
- **Model**: FLUX.1-schnell-Quantized  
- **Link**: https://huggingface.co/aifoundry-org/FLUX.1-schnell-Quantized  
- **Tool**: ComfyUI (self-hosted, local)  
- **Hardware**: NVIDIA RTX 3060 12GB (or your GPU)  
- **Steps**: 35  
- **CFG**: 8  
- **Sampler**: DPM++ 2M  
- **Prompt**: *"A surreal album cover of a faceless woman holding a baby, dark oil painting, high detail, minimal text, dramatic shadows..."*  
- **Negative Prompt**: *"text, watermark, logo, disfigured, low quality"*  
- **Extensions/LoRA**: None  
- **Screenshot of Pipeline**:  
![workflow](comfyui_pipeline_cd.png)

model:
https://huggingface.co/aifoundry-org/FLUX.1-schnell-Quantized/resolve/main/flux1-schnell-fp8.safetensors

localhost:
http://127.0.0.1:8188
