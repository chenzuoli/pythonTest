import base64
import os

import requests

engine_id = "stable-diffusion-v1-5"
api_host = os.getenv("API_HOST", "https://api.stability.ai")
api_key = os.getenv("STABILITY_API_KEY")

if api_key is None:
    raise Exception("Missing Stability API key.")

response = requests.post(
    f"{api_host}/v1/generation/{engine_id}/image-to-image",
    headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },
    # image dimensions must be multiples of 64
    files={
        # "init_image": open("../init_image.png", "rb")
        "init_image": open("./base_img/summer_me.png", "rb")
    },
    data={
        "image_strength": 0.9,
        "init_image_mode": "IMAGE_STRENGTH",
        # "text_prompts[0][text]": "Galactic dog with a cape",
        # "text_prompts[0][text]": "toph from avatar as an office clerk, detailed perfect face, exquisite details, fire magic, mid view, design on a white background, by studio muti, greg rutkowski makoto shinkai takashi takeuchi studio ghibli",
        # "text_prompts[0][text]": "a painted avatar portrait of an awesome powerful humanoid kitsune fox mage themed around life and death, in the style of dnd beyond avatar portraits, beautiful, artistic, elegant, lens flare, magical, lens flare, nature, realism, stylized, art by jeff easley",
        "text_prompts[0][text]": "katara from avatar as an azctec warrior, detailed perfect face, handsome, exquisite details, fire magic, mid view, design on a white background, by studio muti, greg rutkowski makoto shinkai takashi takeuchi studio ghibli",
        # "text_prompts[0][text]": "fantasy magic man portrait, sci-fi, smile, face, black hair, fantasy, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha",
        # "text_prompts[0][text]": "portrait by mandy jurgens, cartoon, oil painting, visionary art, smile, symmetric, magic symbols, holy halo, dramatic ambient lighting, high detail, vibrant colors",
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "samples": 1,
        "steps": 30,
    }
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()

for i, image in enumerate(data["artifacts"]):
    with open(f"./out/v1_img2img_{i}.png", "wb") as f:
        f.write(base64.b64decode(image["base64"]))
