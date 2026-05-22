import sys

# Read files
with open("new_content.html", "r", encoding="utf-8") as f:
    new_content = f.read()

with open("index.html", "r", encoding="utf-8") as f:
    old_content = f.read()

# Find markers
start_marker = '<style>\n/* ============================'
start_idx = old_content.find(start_marker)

if start_idx < 0:
    print("ERROR: Start marker not found", file=sys.stderr)
    sys.exit(1)

# Find end (after </footer> and whitespace)
footer_idx = old_content.find('</footer>', start_idx)
if footer_idx < 0:
    print("ERROR: </footer> not found", file=sys.stderr)
    sys.exit(1)

end_idx = footer_idx + 9  # len('</footer>')

# Skip whitespace
while end_idx < len(old_content) and old_content[end_idx] in ' \t\n\r':
    end_idx += 1

# Splice
result = old_content[:start_idx] + new_content + old_content[end_idx:]

# Write back
with open("index.html", "w", encoding="utf-8") as f:
    f.write(result)

print(f"✓ Success! Updated index.html")
print(f"  Old block: {end_idx - start_idx} bytes")
print(f"  New block: {len(new_content)} bytes")
print(f"  New file: {len(result)} bytes")
