import subprocess
from huggingface_hub import hf_hub_download
ckpt_path = hf_hub_download(repo_id="CompVis/stable-diffusion-v-1-4-original", filename="sd-v1-4-full-ema.ckpt", use_auth_token=True)

BATCH_SIZE = 4
N_GPUS = 2
ACCUMULATE_BATCHES = 1


command = [
    "python",
    "main.py",
    "-t",
    "--base",
    "kanji.yaml",
    "--gpus",
    "0,1",
    "--scale_lr",
    "False",
    "--num_nodes",
    "1",
    "--check_val_every_n_epoch",
    "10",
    "--finetune_from",
    "/scratch/network/jmonas/.cache/huggingface/hub/models--CompVis--stable-diffusion-v-1-4-original/snapshots/f0bb45b49990512c454cf2c5670b0952ef2f9c71/sd-v1-4-full-ema.ckpt",
    "data.params.batch_size=4",
    "lightning.trainer.accumulate_grad_batches=1",
    "data.params.validation.params.n_gpus=2"
]

# Execute the command
subprocess.run(command, shell=True)