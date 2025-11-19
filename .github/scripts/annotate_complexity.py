import os
import ast
from google import genai


COMMENT_MARKER = "# Time complexity"
MODEL_NAME = "gemini-2.5-flash"

client = genai.Client()


def file_already_annotated(text: str) -> bool:
    """Return True if file already contains complexity comments."""
    return COMMENT_MARKER in text


def extract_python_functions(code: str):
    """Parse the file and return function definitions."""
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return None
    return [node for node in tree.body if isinstance(node, ast.FunctionDef)]


def ask_gemini_for_complexity(code: str) -> str:
    """Ask Gemini to compute time/space complexity."""
    prompt = f"""
Analyze the following Python code and produce ONLY valid Python comments.
The output MUST be 3 lines formatted exactly like this:

# Time Complexity: O(...)
# Space Complexity: O(...) (worst case)
# Space Complexity: O(...) (best case)

Code:
{code}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={"response_mime_type": "text/plain"},
    )

    return response.text.strip()


def annotate_file(path: str):
    """Add complexity comments to the bottom of the file."""
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    # Skip if already contains complexity block
    if file_already_annotated(original):
        print(f"Skipping (already annotated): {path}")
        return

    functions = extract_python_functions(original)
    if not functions:
        print(f"Skipping (no functions detected): {path}")
        return

    # Merge all functions for analysis
    code_to_analyze = original

    print(f"Annotating: {path}")

    complexity_comments = ask_gemini_for_complexity(code_to_analyze)

    # Ensure comments begin with "#"
    cleaned_comments = "\n".join(
        line if line.strip().startswith("#") else f"# {line}"
        for line in complexity_comments.splitlines()
    )

    updated = original.rstrip() + "\n\n" + cleaned_comments + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)


def main():
    for root, _, files in os.walk("."):
        # Ignore .github, venv folders
        if ".github" in root:
            continue
        if "venv" in root or "env" in root:
            continue

        for filename in files:
            if filename.endswith(".py"):
                annotate_file(os.path.join(root, filename))


if __name__ == "__main__":
    main()
