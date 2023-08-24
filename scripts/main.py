import sys
import time
import modules.scripts as scripts
import modules
import modules.shared as shared
import gradio as gr
from modules.ui_components import FormColumn, FormRow
from modules import script_callbacks


def on_ui_settings():
    section = ("sdxlHiresHack ", "SDXL Refinder Hack")
    shared.opts.add_option(
        key = "sdxl_base_model",
        info = shared.OptionInfo(
            "sd_xl_base_1.0.safetensors",
            "SDXL Base model",
            section=section)
    )

    shared.opts.add_option(
        key = "sdxl_refiner_model",
        info = shared.OptionInfo(
            "sd_xl_refiner_1.0.safetensors",
            "SDXL refiner model",
            section=section)
    )

script_callbacks.on_ui_settings(on_ui_settings)

class sdxlRefinderHack(scripts.Script):

    def __init__(self):
        self.info_base = None
        self.info_hr = None
        self.first_pass = True

    def title(self):
        return "SDXL Refinder Hack"
    
    def show(self, is_img2img):
        return scripts.AlwaysVisible
    
    def ui(self, is_img2img):
        with gr.Accordion(self.title(), open=False):
            gr.Markdown("will become unnecessary in the 1.6 release of A1111")
            if is_img2img:
                gr.Markdown("will not do anything in img2img")
            else:
            
                with FormRow():
                    is_enabled = gr.Checkbox(value=False, label="Enable")
                with FormColumn():
                    base_model = gr.inputs.Textbox(lines=1, label="SDXL base model name", default=getattr(shared.opts, "sdxl_base_model", ""))
                    refinder_model = gr.inputs.Textbox(lines=1, label="SDXL refinder model name", default=getattr(shared.opts, "sdxl_refiner_model", ""))
                return [base_model, refinder_model, is_enabled]
    
    
    def before_process_batch(self, p,*args, **kwargs):
        print(f"\nEnabled: {args[2]}\n\ncheckpoint: {args[0]}")
        if args[2]:
            if self.first_pass:
                self.first_pass = False
            else:
                modules.sd_models.unload_model_weights(shared.sd_model, self.info_hr)
            self.info_base = modules.sd_models.get_closet_checkpoint_match(args[0])
            modules.sd_models.reload_model_weights(shared.sd_model, self.info_base)
            p.override_settings['sd_model_checkpoint'] = self.info_base.name

    def before_hr(self, p, *args, **kwargs):
        if args[2]:
            modules.sd_models.unload_model_weights(shared.sd_model, self.info_base)
            self.info_hr = modules.sd_models.get_closet_checkpoint_match(args[1])
            modules.sd_models.reload_model_weights(shared.sd_model, self.info_hr)
            p.override_settings['sd_model_checkpoint'] = self.info_hr.name
            p.extra_generation_params['base model'] = self.info_base.name


