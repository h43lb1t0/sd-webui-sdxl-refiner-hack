# This extension becomes unnecessary with the Realse 1.6 of A11111 !

There will be native sdxl support and in the hires. fix the model can be changed. See:

[realse notes ](https://github.com/AUTOMATIC1111/stable-diffusion-webui/releases/tag/v1.6.0-RC)

<hr>



# ~~SD WebUI SDXL Refiner Hack~~

~~Use the SDXL Refiner Model for the high-res fix pass. Hopefully, we won't need this extension for a long time.~~

### ~~This is not the same as the Refiner used in Comfy UI!~~

<hr>

~~You need to enable high-res fix.~~

### ~~System Requirements~~

- ~~32GB RAM (Not VRAM)~~

~~SDXL requires a lot of RAM so the more the better. With 32GB, it will use **ALL** of your RAM. Close **everything** you don't need to have open. `<br>`
Also, use [this pull request](https://github.com/AUTOMATIC1111/stable-diffusion-webui/pull/11958) with 32GB RAM to reduce RAM usage.~~

### ~~recommendations~~

- ~~Use [this](https://huggingface.co/madebyollin/sdxl-vae-fp16-fix) VAE (fp16)~~
- ~~Set batch count to 1 (for 32GB RAM)~~
- ~~Other settings as you would normally~~

~~My settings:~~

- ~~Upscaler: Latent~~
- ~~Upscale by: 1.25~~
- ~~Denoising: 0.53~~

<hr>

~~The default values can be changed in the settings~~

~~Of course, this extension can be just used to use a different checkpoint for the high-res fix pass for non-SDXL models.~~
