#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import markdown
import os
import sys

def main():
    # Check if README.md exists
    if not os.path.exists('README.md'):
        print('ERROR: README.md not found in current directory')
        sys.exit(1)
    
    print('README.md found')
    
    # Read README.md
    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            text = f.read()
        print('Successfully read README.md')
    except Exception as e:
        print(f'Error reading README.md: {e}')
        sys.exit(1)
    
    # Convert to HTML with enhanced styling
    try:
        html = markdown.markdown(text, extensions=['fenced_code', 'tables', 'toc'])
        print('Successfully converted Markdown to HTML')
    except Exception as e:
        print(f'Error converting Markdown: {e}')
        sys.exit(1)
    
    # Create HTML content with modern responsive design
    html_start = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ziyang-Bai Homepage</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #24292f;
            background: #ffffff;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: #ffffff;
            border: 1px solid #000000;
            position: relative;
        }
        
        .content {
            padding: 40px;
            position: relative;
            z-index: 2;
        }
        
        h1, h2, h3, h4, h5, h6 {
            margin-top: 32px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }
        
        h1:first-child, h2:first-child {
            margin-top: 0;
        }
        
        h1 { 
            font-size: 2.5em; 
            color: #004a7f;
            border-bottom: 2px solid #eaecf0; 
            padding-bottom: 16px; 
            text-align: center;
        }
        
        h2 { 
            font-size: 1.8em; 
            color: #004a7f;
            border-bottom: 2px solid #eaecf0; 
            padding-bottom: 12px;
            position: relative;
        }
        
        h2::before {
            content: '';
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 50px;
            height: 2px;
            background: #004a7f;
        }
        
        h3 {
            font-size: 1.4em;
            color: #586069;
        }
        
        p {
            margin-bottom: 16px;
            text-align: justify;
        }
        
        pre {
            padding: 20px;
            overflow-x: auto;
            font-size: 85%;
            line-height: 1.45;
            background: #f6f8fa;
            border: 1px solid #e1e4e8;
            margin: 16px 0;
        }
        
        code {
            padding: 0.2em 0.4em;
            font-size: 85%;
            background-color: rgba(175,184,193,0.2);
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
        }
        
        pre code {
            background-color: transparent;
            padding: 0;
        }
        
        blockquote {
            padding: 16px 24px;
            color: #656d76;
            border-left: 4px solid #004a7f;
            margin: 16px 0;
            background-color: #f6f8fa;
        }
        
        table {
            border-spacing: 0;
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            overflow: hidden;
            border: 1px solid #d0d7de;
        }
        
        table th, table td {
            padding: 12px 16px;
            border: 1px solid #d0d7de;
            text-align: left;
        }
        
        table th {
            font-weight: 600;
            background: #004a7f;
            color: white;
        }
        
        table tr:nth-child(even) {
            background-color: #f6f8fa;
        }
        
        table tr:hover {
            background-color: #e6f3ff;
        }
        
        a {
            color: #004a7f;
            text-decoration: none;
            transition: all 0.2s ease;
        }
        
        a:hover {
            color: #003a65;
            text-decoration: underline;
        }
        
        img {
            max-width: 100%;
            height: auto;
            margin: 8px 0;
        }
        
        /* Badge 样式优化 */
        img[src*="shields.io"], img[src*="badge"] {
            margin: 2px 4px;
            display: inline-block;
        }
        
        /* GitHub stats 图表样式 */
        img[src*="github-readme-stats"], img[src*="github-readme"], img[src*="readme-typing-svg"] {
            margin: 16px 0;
        }
        
        /* GitHub contributions 图表样式 */
        img[src*="github-contribution-grid-snake"], 
        img[src*="github-contributions"],
        img[src*="contrib.rocks"],
        img[src*="activity-graph"],
        img[src*="ghchart.rshah.org"] {
            margin: 20px 0;
            border-radius: 8px;
        }
        
        /* 居中对齐的 div */
        div[align="center"] {
            text-align: center;
            margin: 24px 0;
        }
        
        /* 响应式设计 */
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }
            
            .container {
                margin: 0 5px;
            }
            
            .content {
                padding: 20px;
            }
            
            h1 {
                font-size: 2em;
            }
            
            h2 {
                font-size: 1.5em;
            }
            
            h3 {
                font-size: 1.2em;
            }
            
            pre {
                padding: 12px;
                font-size: 80%;
            }
            
            table {
                font-size: 14px;
            }
            
            table th, table td {
                padding: 8px 10px;
            }
            
            img[src*="github-readme-stats"], img[src*="github-readme"] {
                width: 100%;
                height: auto;
            }
        }
        
        @media (max-width: 480px) {
            .content {
                padding: 15px;
            }
            
            h1 {
                font-size: 1.8em;
            }
            
            h2 {
                font-size: 1.3em;
            }
            
            table {
                font-size: 12px;
            }
            
            table th, table td {
                padding: 6px 8px;
            }
        }
        
        /* 滚动条美化 */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #004a7f;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #003a65;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
'''
    
    html_end = '''
        </div>
    </div>
</body>
</html>'''
    
    # Write to index.html by concatenating the parts
    try:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_start + html + html_end)
        print('Successfully created index.html')
        
        # Show file information
        file_size = os.path.getsize('index.html')
        print(f'Generated file size: {file_size} bytes')
        
    except Exception as e:
        print(f'Error writing index.html: {e}')
        sys.exit(1)
    
    print('Conversion completed successfully!')

if __name__ == '__main__':
    main()
