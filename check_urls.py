import os, re, json

# List all actual files in resources/
resource_files = set()
base = r'C:\Users\qinxiaolin\WorkBuddy\2026-06-24-09-42-33\edui-nav\resources'
for root, dirs, files in os.walk(base):
    for f in files:
        if f.endswith('.html'):
            rel = os.path.relpath(os.path.join(root, f), base)
            if f == 'index.html' and root != base:
                # It's a directory with index.html
                folder = os.path.relpath(root, base)
                resource_files.add(folder + '/index.html')
            else:
                resource_files.add(rel)

with open(r'C:\Users\qinxiaolin\WorkBuddy\2026-06-24-09-42-33\edui-nav\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'const SITE_DATA = ({.*?});', content, re.DOTALL)
data = json.loads(match.group(1))
tools = data['sections'][1]['tools']

# Extract tool URLs referencing resources/
tool_urls = set()
tool_url_map = {}
for t in tools:
    url = t.get('url', '')
    if url.startswith('resources/'):
        tool_urls.add(url)
        tool_url_map[url] = t.get('title', '')

print('=== Actual resource files ===')
for f in sorted(resource_files):
    print(f'  resources/{f}')
print(f'Total: {len(resource_files)}')
print()

print('=== Tool URLs in data ===')
for u in sorted(tool_urls)[:10]:
    print(f'  {u}  ({tool_url_map.get(u, "")})')
print(f'...and {len(tool_urls)-10} more. Total: {len(tool_urls)}')
print()

# Check mismatches
print('=== Mismatched URLs ===')
mismatched = []
for u in sorted(tool_urls):
    file_path = u.replace('resources/', '', 1)
    if file_path not in resource_files:
        mismatched.append((u, tool_url_map.get(u, '')))
print(f'Mismatched: {len(mismatched)}')
for u, title in mismatched:
    print(f'  {u}  ({title})')
print()
print(f'Matching: {len(tool_urls) - len(mismatched)}/{len(tool_urls)}')
