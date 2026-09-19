# Comfy-Premiere-Automator 🎬🤖

An open-source orchestration tool that bridges Adobe Premiere Pro directly with local AI diffusion models via ComfyUI.

While enterprise studios have custom pipelines, independent video editors and boutique creative agencies lack open-source orchestration tools that connect professional NLEs (Non-Linear Editors) with local generative AI. This project fills that gap by allowing editors to use timeline markers as text prompts, automatically generating B-roll footage or assets locally (e.g., using FLUX models) and preparing them for seamless timeline integration.

## Features (MVP)
* **Marker Extraction:** ExtendScript (JSX) that pulls prompt data, timestamps, and durations directly from Adobe Premiere Pro timeline markers.
* **ComfyUI Bridge:** A lightweight Python middleware that translates Premiere marker data into API calls for a local ComfyUI instance.
* **Apple Silicon Optimized:** Designed with local mac-based workflows in mind.

## Prerequisites
* Adobe Premiere Pro (2024 or newer)
* ComfyUI running locally on `http://127.0.0.1:8188`
* Python 3.10+

## How it works
1. **Mark in Premiere:** Add a marker on your timeline and write your image/video prompt in the marker's name (e.g., "futuristic cyberpunk city").
2. **Export:** Run `export_markers.jsx` in Premiere to dump the marker data into a JSON file.
3. **Generate:** Run `comfy_bridge.py`. The script reads the JSON, sends the prompts to your local ComfyUI queue, and saves the generated assets into a designated `Rendered` folder.

## Future Roadmap (Claude API Integration)
The next major milestone for this project is integrating the **Claude API** as a reasoning engine. Claude will parse raw, messy transcriptions from the Premiere sequence and automatically suggest ideal B-roll markers and elaborate prompts for ComfyUI, fully automating the ideation phase of video editing. This is why access to Claude Max is critical for the continued development of this pipeline.

## License
MIT License
