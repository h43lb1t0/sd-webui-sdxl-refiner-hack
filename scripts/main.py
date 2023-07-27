import sys
import time
import modules.scripts as scripts
import modules
import modules.shared as shared
import gradio as gr

class sdxlRefinderHack(scripts.Script):

    info = None

    def title(self):
        return "SDXL Refinder Hack"
    
    def show(self, is_img2img):
        return scripts.AlwaysVisible
    
    def ui(self, is_img2img):
        gr.Markdown("## SDXL Refinder Hack")
        base_model = gr.inputs.Textbox(
                    lines=1, label="SDXL base model name", default="sdxl/sd_xl_base_1.0.safetensors")
        refinder_model = gr.inputs.Textbox(lines=1, label="SDXL refinder model name", default="sdxl/sd_xl_refiner_1.0")
        return [base_model, refinder_model]
    
    
    def process_batch(self, p,*args, **kwargs):
        self.info = modules.sd_models.get_closet_checkpoint_match(args[0])
        modules.sd_models.reload_model_weights(shared.sd_model, self.info)

    def before_hr(self, p, *args, **kwargs):
        #print(f"before_hr: {foo}")
        #modules.sd_models.unload_model_weights(shared.sd_model, self.info)
        time.sleep(1)
        info = modules.sd_models.get_closet_checkpoint_match(args[1])
        modules.sd_models.reload_model_weights(shared.sd_model, info)
        p.hr_prompt = "a lion"
        return p