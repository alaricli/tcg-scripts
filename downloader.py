import os
import urllib.request

response = [
    # put json response here
]

output_dir = os.path.expanduser("~/Downloads/pokemon_cards")
os.makedirs(output_dir, exist_ok=True)

for c in response:
    try:
        image_url = c["cardImages"]["small"]
        image_name = f"{c['id']}_{c['name']}.png"
        image_path = os.path.join(output_dir, image_name)
        print(f"Downloading {image_url} to {image_path}")

        urllib.request.urlretrieve(image_url, image_path)
        print(f"Successfully downloaded: {image_name}")
    except KeyError as e:
        print(f"Missing key in response data: {e}")
    except Exception as e:
        print(f"Failed to download: {e}")

print("Download complete.")
