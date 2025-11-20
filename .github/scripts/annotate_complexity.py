import os
import subprocess
from google import genai
from pydantic import BaseModel, Field
from typing import Optional

MODEL_NAME = "gemini-2.5-flash"
client = genai.Client()

COMMENT_HEADER = "# Complexity Annotations"


class ComplexityResult(BaseModel):
    time_best: str = Field(description="Time complexity best case, format: O(...)")
    time_avg: str = Field(description="Time complexity average case, format: O(...)")
    time_worst: str = Field(description="Time complexity worst case, format: O(...)")
    space_best: str = Field(description="Space complexity best case, format: O(...)")
    space_avg: str = Field(description="Space complexity average case, format: O(...)")
    space_worst: str = Field(description="Space complexity worst case, format: O(...)")


def get_changed_python_files():
    before = os.getenv("GITHUB_EVENT_BEFORE")
    sha = os.getenv("GITHUB_SHA")

    if before and sha:
        cmd = ["git", "diff", "--name-only", before, sha]
    else:
        cmd = ["git", "diff", "--name-only", "HEAD~1", "HEAD"]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    return [f for f in result.stdout.splitlines() if f.endswith(".py")]


def ask_gemini_for_complexity(code: str) -> ComplexityResult:
    prompt = f"""
Analyze the following Python code.
Do NOT rewrite the code.
Do NOT return comments or plain text.

Return ONLY JSON with exactly 6 fields:
- time_best
- time_avg
- time_worst
- space_best
- space_avg
- space_worst

Each value MUST be formatted like "O(...)".

Code:
{code}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": ComplexityResult.model_json_schema(),
        },
    )

    return ComplexityResult.model_validate_json(response.text)


def format_complexity_comments(result: ComplexityResult) -> str:
    return (
        f"{COMMENT_HEADER}\n"
        f"# Time Complexity (best): {result.time_best}\n"
        f"# Time Complexity (average): {result.time_avg}\n"
        f"# Time Complexity (worst): {result.time_worst}\n"
        f"# Space Complexity (best): {result.space_best}\n"
        f"# Space Complexity (average): {result.space_avg}\n"
        f"# Space Complexity (worst): {result.space_worst}\n"
    )


def annotate_file(path: str):
    print(f"Annotating: {path}")

    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    result = ask_gemini_for_complexity(original)
    comments = format_complexity_comments(result)

    updated = original.rstrip() + "\n\n" + comments + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)


def main():
    changed = get_changed_python_files()
    if not changed:
        print("No changed Python files found.")
        return

    for path in changed:
        annotate_file(path)


if __name__ == "__main__":
    main()
