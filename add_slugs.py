import os, re

tools_dir = r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked\content\tools"
zh_tools_dir = r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked\content\zh\tools"

count = 0
for directory in [tools_dir, zh_tools_dir]:
    for filename in os.listdir(directory):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(directory, filename)
        slug = os.path.splitext(filename)[0]

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if re.search(r'^slug:\s', content, re.MULTILINE):
            continue

        fm_end = content.find('---', 4)
        if fm_end == -1:
            print(f"SKIP no frontmatter: {filename}")
            continue

        insertion = f'slug: "{slug}"\n'
        new_content = content[:3] + '\n' + insertion + content[3:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        count += 1
        print(f"ADDED slug to: {filename}")

print(f"\nTotal: {count} files updated")