import re
path = r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked\generate_extra_tools.py"
content = open(path, 'r', encoding='utf-8').read()
# Replace the problematic f-string lines
content = content.replace(
    '{{< cta "{slug}" "Try {name}" >}}',
    '< cta slug_only >'
)
content = content.replace(
    '{{< cta "{slug}" "试用 {name}" >}}',
    '< cta slug_only >'
)
open(path, 'w', encoding='utf-8').write(content)
print("Fixed")
