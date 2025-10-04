import markdown
from pathlib import Path

readme_text = Path("README.md").read_text(encoding="utf-8")
html = markdown.markdown(readme_text)

Path("docs").mkdir(exist_ok=True)
Path("docs/index.html").write_text(html, encoding="utf-8")

print("Документацію згенеровано у docs/index.html")
