import json
import urllib.request
import os

# Configuration for local ComfyUI
COMFY_URL = "http://127.0.0.1:8188/prompt"
MARKERS_FILE = os.path.expanduser("~/Desktop/premiere_markers.json")

def queue_prompt(prompt_workflow):
    data = json.dumps(prompt_workflow).encode('utf-8')
    req = urllib.request.Request(COMFY_URL, data=data)
    try:
        response = urllib.request.urlopen(req)
        return json.loads(response.read())
    except Exception as e:
        print(f"Error connecting to ComfyUI: {e}")
        return None

def main():
    if not os.path.exists(MARKERS_FILE):
        print(f"File not found: {MARKERS_FILE}. Please run the JSX script in Premiere first.")
        return

    with open(MARKERS_FILE, 'r') as f:
        markers = json.load(f)

    if not markers:
        print("No markers found in the JSON file.")
        return

    print(f"Found {len(markers)} markers. Sending to ComfyUI...")

    for i, marker in enumerate(markers):
        text_prompt = marker.get("prompt", "")
        if not text_prompt:
            continue
            
        print(f"Queueing job {i+1}: {text_prompt}")
        
        # This is a highly simplified ComfyUI API JSON structure.
        # In a real workflow, you would load your saved API format JSON here 
        # and dynamically replace the text prompt node value.
        workflow = {
            "prompt": {
                "3": {
                    "class_type": "KSampler",
                    "inputs": {
                        "seed": 12345,
                        "steps": 20,
                        "cfg": 8.0,
                        "sampler_name": "euler",
                        "scheduler": "normal",
                        "denoise": 1.0,
                        "model": ["4", 0],
                        "positive": ["6", 0],
                        "negative": ["7", 0],
                        "latent_image": ["5", 0]
                    }
                },
                # Placeholder for the actual prompt node
                "6": {
                    "class_type": "CLIPTextEncode",
                    "inputs": {
                        "text": text_prompt,
                        "clip": ["4", 1]
                    }
                }
            }
        }
        
        # Send to ComfyUI
        queue_prompt(workflow)

    print("All tasks queued in ComfyUI!")

if __name__ == "__main__":
    main()
