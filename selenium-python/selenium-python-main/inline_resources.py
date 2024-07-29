import os
from bs4 import BeautifulSoup
import base64

def inline_resources(html_path):
    with open(html_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Inline CSS
    for link_tag in soup.find_all('link', {'rel': 'stylesheet'}):
        href = link_tag['href']
        if not href.startswith('http'):  # Bỏ qua các URL bên ngoài
            file_path = os.path.join(os.path.dirname(html_path), href)
            with open(file_path, 'r', encoding='utf-8') as css_file:
                style_tag = soup.new_tag('style')
                style_tag.string = css_file.read()
                link_tag.replace_with(style_tag)

    # Inline JS
    for script_tag in soup.find_all('script', src=True):
        src = script_tag['src']
        if not src.startswith('http'):  # Bỏ qua các URL bên ngoài
            file_path = os.path.join(os.path.dirname(html_path), src)
            with open(file_path, 'r', encoding='utf-8') as js_file:
                script_tag.string = js_file.read()
                del script_tag['src']

    # Inline images
    for img_tag in soup.find_all('img', src=True):
        src = img_tag['src']
        if not src.startswith('http'):  # Bỏ qua các URL bên ngoài
            file_path = os.path.join(os.path.dirname(html_path), src)
            with open(file_path, 'rb') as img_file:
                img_data = base64.b64encode(img_file.read()).decode('utf-8')
                img_tag['src'] = f"data:image/{os.path.splitext(src)[1][1:]};base64,{img_data}"

    # Write to a single HTML file
    with open('single_report.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

# Inline resources in the Allure report
inline_resources('D:\\selenium_python\\selenium-python\\selenium-python-main\\allure-report\\index.html')
