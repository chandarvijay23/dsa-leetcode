import os
from google import genai

MODEL_NAME = "gemini-2.5-flash"
client = genai.Client()


def rewrite_with_complexity(code: str) -> str:
    """
    Sends the full file content to Gemini.
    Gemini returns:
    - fully reformatted code (whitespace only)
    - NO code logic modifications
    - complexity annotations for every function:
        # Time Complexity (Best): O(...)
        # Time Complexity (Average): O(...)
        # Time Complexity (Worst): O(...)
        # Space Complexity (Best): O(...)
        # Space Complexity (Average): O(...)
        # Space Complexity (Worst): O(...)
    """

    prompt = f"""
You are a strict code formatter and complexity annotator.

Given the FULL Python file below, return ONLY the rewritten file contents.

### RULES:
1. Do NOT change ANY logic.
2. Do NOT rename variables, functions, classes.
3. You may ONLY:
   - reformat whitespace and indentation
   - improve spacing
   - add Python comments
4. For every function or method (top-level or inside classes), add EXACTLY these 6 comments at the top of the function:

# Time Complexity (Best): O(...)
# Time Complexity (Average): O(...)
# Time Complexity (Worst): O(...)
# Space Complexity (Best): O(...)
# Space Complexity (Average): O(...)
# Space Complexity (Worst): O(...)

5. Replace "..." with the correct complexity values.
6. Output ONLY valid Python code. No markdown, no explanations.

### FILE TO PROCESS:
{code}
"""

    resp = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={"response_mime_type": "text/plain"},
    )

    return resp.text.strip()


def process_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    print(f"Processing: {path}")

    new_code = rewrite_with_complexity(original)

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_code + "\n")


def main():
    for root, _, files in os.walk("."):
        if ".github" in root:
            continue
        if "venv" in root or "env" in root:
            continue

        for filename in files:
            if filename.endswith(".py"):
                process_file(os.path.join(root, filename))


if __name__ == "__main__":
    main()