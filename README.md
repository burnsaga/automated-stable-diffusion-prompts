# Automated Stable Diffusion Scripts

Scripts to fully automate Stable Diffusion text-to-image generation. Using current Google Trends or miscellaneous art styles, generate hundreds of images with just one command.

## Ways to Run

1. [x] manual: run each prompt in command line (or use GUI)
2. [x] semi-automated: enter prompts into `prompts.txt` > run python script that runs each prompt
3. [x] automated: prompts generated using pre-defined (string) lists
4. [x] automated: prompts generated using pre-defined lists + US Google Trends search queries
5. [x] automated: prompts generated using pre-defined lists + US Google Trends search queries + random words from dictionary (separated by adjective, noun, etc.?)
   1. [x] using `randomword` Python library
   2. [ ] using custom dictionary? - (e.g. urbandictionary, Websters, etc.) - <https://stackoverflow.com/questions/70208287/how-to-use-urbandictionary-api-built-in-api-function-random>
   3. [x] using current US Google Trends