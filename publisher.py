#!/usr/bin/env python3
import os
import shutil
import glob
import re
import html
import json
from datetime import datetime

# === CONFIGURATION ===
SOURCE_BEACH = "WORLD/Ocean/Beach"
SOURCE_REPORTS = "WORLD/Bookshelf/Reports"

TARGET_ROOT = "WORLD/System/Gallery"
TARGET_BEACH = os.path.join(TARGET_ROOT, "Beach")
TARGET_REPORTS = os.path.join(TARGET_ROOT, "Reports")

# === STYLES (Soft Lavender / Warm Paper) ===
STYLES = """
<style>
    :root {
        --bg: #fdfcf8;           /* Warm Cream */
        --sidebar-bg: #f8f7f4;   /* Subtle separation */
        --text-main: #4a4a4a;    /* Soft Charcoal */
        --text-dim: #95a5a6;     /* Muted Grey */
        --accent: #8e84d4;       /* Periwinkle/Lavender */
        --accent-light: #e0dcfc; /* Pale Lavender Highlight */
        --border: #f0f0f0;
        --code-bg: #f4f4f4;
    }
    body {
        font-family: "Palatino", "Georgia", serif; /* Classic, soft serif */
        background-color: var(--bg);
        color: var(--text-main);
        margin: 0;
        display: flex;
        height: 100vh;
        overflow: hidden;
    }
    
    /* Sidebar */
    .sidebar {
        width: 300px;
        background: var(--sidebar-bg);
        border-right: 1px dashed var(--border); /* Softer border */
        display: flex;
        flex-direction: column;
        padding: 3rem 2rem;
        overflow-y: auto;
        flex-shrink: 0;
    }
    
    .main-content {
        flex-grow: 1;
        padding: 5rem 8rem; /* Airy padding */
        overflow-y: auto;
        max-width: 850px;
        margin: 0 auto;
    }

    /* Typography */
    .site-title {
        font-family: "Futura", "Helvetica Neue", sans-serif; /* Clean sans for contrast */
        font-weight: 500;
        font-size: 1.1rem;
        letter-spacing: 0.15em;
        margin-bottom: 3rem;
        color: var(--accent);
        text-transform: uppercase;
        text-align: center;
    }
    
    .nav-section { margin-bottom: 2.5rem; }
    .nav-header {
        font-family: "Futura", "Helvetica Neue", sans-serif;
        font-size: 0.7rem;
        text-transform: uppercase;
        color: var(--text-dim);
        margin-bottom: 1rem;
        letter-spacing: 0.15em;
        font-weight: 600;
        padding-left: 0.5rem;
    }
    .nav-item {
        display: block;
        padding: 0.5rem 0.8rem;
        margin-bottom: 0.2rem;
        border-radius: 6px;
        cursor: pointer;
        font-size: 0.95rem;
        color: var(--text-main);
        transition: all 0.3s ease;
        line-height: 1.4;
        opacity: 0.8;
    }
    .nav-item:hover { 
        background: white; 
        color: var(--accent); 
        opacity: 1; 
        transform: translateX(2px);
    }
    .nav-item.active { 
        background: white; 
        color: var(--accent); 
        font-weight: 500; 
        box-shadow: 0 4px 15px rgba(142, 132, 212, 0.1); 
        opacity: 1;
    }
    .nav-date { font-size: 0.7rem; color: #b2bec3; display: block; margin-top: 0.2rem; font-family: sans-serif; }

    /* Markdown Content */
    h1 { 
        font-family: "Palatino", serif; 
        font-size: 2.4rem; 
        font-weight: 400; 
        margin-bottom: 0.5rem; 
        color: var(--text-main);
        letter-spacing: -0.02em;
    }
    .meta-line { 
        font-family: "Futura", sans-serif; 
        font-size: 0.8rem; 
        color: var(--accent); 
        margin-bottom: 4rem; 
        text-transform: uppercase; 
        letter-spacing: 0.1em; 
    }
    
    h2 { 
        font-family: "Palatino", serif; 
        font-size: 1.6rem; 
        color: var(--text-main);
        border-bottom: 1px solid var(--accent-light); 
        padding-bottom: 0.5rem; 
        margin-top: 3.5rem; 
        font-weight: 400; 
    }
    h3 { font-size: 1.2rem; font-style: italic; color: var(--text-dim); margin-top: 2.5rem; font-weight: 400; }
    
    p { font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.8rem; color: #555; }
    li { font-size: 1.05rem; line-height: 1.7; margin-bottom: 0.8rem; color: #555; }
    
    blockquote { 
        border-left: 2px solid var(--accent); 
        padding-left: 1.5rem; 
        margin: 2.5rem 0; 
        font-style: italic; 
        color: var(--text-dim); 
        background: transparent;
    }
    
    code { background: var(--code-bg); padding: 0.2rem 0.4rem; border-radius: 4px; font-family: 'Menlo', monospace; font-size: 0.85em; color: var(--accent); }
    pre { background: #fafafa; border: 1px solid #eee; color: #555; padding: 1.5rem; border-radius: 8px; overflow-x: auto; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }
    
    a { color: var(--accent); text-decoration: none; border-bottom: 1px dotted var(--accent); transition: all 0.2s; }
    a:hover { background: var(--accent-light); border-bottom-style: solid; }
    
    hr { border: 0; border-top: 1px dashed var(--border); margin: 4rem 0; }

    /* Selection */
    ::selection { background: var(--accent-light); color: var(--text-main); }

    @media (max-width: 800px) {
        body { flex-direction: column; overflow: auto; }
        .sidebar { width: 100%; height: auto; border-right: none; border-bottom: 1px dashed var(--border); padding: 2rem; }
        .main-content { padding: 2rem 1.5rem; }
    }
</style>
"""

# --- HELPERS ---
def needs_update(source, target):
    """Check if source is newer than target, or if target doesn't exist."""
    if not os.path.exists(target):
        return True
    return os.path.getmtime(source) > os.path.getmtime(target)

def render_markdown(text):
    html_out = ""
    in_list = False
    in_code_block = False
    
    lines = text.split('\n')
    for line in lines:
        clean_line = line.strip()

        # Skip Frontmatter
        if clean_line.startswith(('---', 'tags:', '**Tags:**', '**Date:**', '**Source:**')):
            continue

        # Code Blocks
        if clean_line.startswith('```'):
            if in_code_block:
                html_out += '</code></pre>'
                in_code_block = False
            else:
                html_out += '<pre><code>'
                in_code_block = True
            continue
        
        if in_code_block:
            html_out += html.escape(line) + "\n"
            continue

        # Lists
        is_list_item = clean_line.startswith('- ') or clean_line.startswith('* ')
        if is_list_item:
            if not in_list:
                html_out += '<ul>'
                in_list = True
            content = clean_line[2:]
            html_out += f'<li>{format_inline(content)}</li>'
            continue
        else:
            if in_list and clean_line:
                html_out += '</ul>'
                in_list = False
            elif in_list and not clean_line:
                continue

        # Headers
        if clean_line.startswith('# '):
            html_out += f'<h1>{format_inline(clean_line[2:])}</h1>'
        elif clean_line.startswith('## '):
            html_out += f'<h2>{format_inline(clean_line[3:])}</h2>'
        elif clean_line.startswith('### '):
            html_out += f'<h3>{format_inline(clean_line[4:])}</h3>'
        # Blockquotes
        elif clean_line.startswith('> '):
            html_out += f'<blockquote>{format_inline(clean_line[2:])}</blockquote>'
        # HR
        elif clean_line == '---' or clean_line == '***':
            html_out += '<hr>'
        # Empty
        elif clean_line == '':
            continue
        # Paragraphs
        else:
            html_out += f'<p>{format_inline(clean_line)}</p>'
            
    if in_list: html_out += '</ul>'
    if in_code_block: html_out += '</code></pre>'
    return html_out

def format_inline(text):
    text = html.escape(text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\[\[(.*?)\]\]', r'<span class="internal-link">\1</span>', text)
    return text

def parse_note(filepath, category):
    filename = os.path.basename(filepath)
    title = filename.replace(".md", "").replace("_", " ")
    
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', filename)
    date = date_match.group(0) if date_match else "Unknown"

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    html_content = render_markdown(content)
    
    return {
        "id": filename,
        "title": title,
        "date": date,
        "category": category,
        "content": html_content
    }

def process_directory(source_dir, target_dir, category_name):
    notes = []
    files = glob.glob(os.path.join(source_dir, "*.md"))
    
    for f in files:
        filename = os.path.basename(f)
        target_path = os.path.join(target_dir, filename)
        
        # Incremental Copy
        if needs_update(f, target_path):
            shutil.copy(f, target_path)
            # print(f"Updated: {filename}") # Verbose logging optional
        
        # Always parse (we need the content for the index)
        notes.append(parse_note(f, category_name))
        
    return notes

# --- MAIN ---
def main():
    os.makedirs(TARGET_BEACH, exist_ok=True)
    os.makedirs(TARGET_REPORTS, exist_ok=True)

    all_notes = []

    print("--- Scanning & Updating Gallery ---")
    
    # Process Directories
    all_notes.extend(process_directory(SOURCE_BEACH, TARGET_BEACH, "Beach Artifacts"))
    all_notes.extend(process_directory(SOURCE_REPORTS, TARGET_REPORTS, "Essays"))

    # Sort
    all_notes.sort(key=lambda x: x['date'], reverse=True)

    # JS Data - We output an Array, not a Dict, because index.html expects it
    js_content = f"const galleryData = {json.dumps(all_notes, indent=2)};"
    
    with open(os.path.join(TARGET_ROOT, "meta.js"), 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print("--- Gallery Updated: meta.js ---")
    print("--- Note: index.html was NOT modified (to preserve custom design) ---")

if __name__ == "__main__":
    main()
