
with open('the-verdict.txt','r',encoding='utf-8') as f:
    raw_text = f.read()

print(f"Total number of characters : {len(raw_text)}")
print(f"Raw Text : {raw_text[:99]}")