import json
with open('data.json', 'r', encoding='utf-8') as f:
    news = json.load(f)
html = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hacker News</title>
    <style>
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            border-radius: 10px;
            overflow: hidden;
        }
        th {
            background: #ff6600;
            color: white;
            padding: 15px;
            text-align: left;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }
        tr:hover {
            background: #f5f5f5;
        }
        a {
            color: #0066cc;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Новости с Hacker News</h1>
    
    <table>
        <tr>
            <th>№</th>
            <th>Заголовок</th>
            <th>Комментарии</th>
            <th>Ссылка</th>
        </tr>
'''
for item in news:
    html += f'''
        <tr>
            <td>{item['id']}</td>
            <td>{item['title']}</td>
            <td>{item['comments']}</td>
            <td><a href="{item['link']}" target="_blank">Открыть</a></td>
        </tr>
    '''
html += '''
    </table>
    
    <div class="footer">
        <p>Источник: <a href="https://news.ycombinator.com/" target="_blank">Hacker News</a></p>
    </div>
</body>
</html>
'''
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML страница создана: index.html")
