#!/usr/bin/env python3
"""
Генерация PDF лидмагнита с обложкой, иллюстрациями и CTA кнопками
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path
import base64

def image_to_base64(path):
    """Конвертирует изображение в base64 для встраивания в HTML"""
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode()

# Читаем изображения
cover_b64 = image_to_base64("cover.jpg")
coral_mine_b64 = image_to_base64("img_coral_mine.png")
h500_b64 = image_to_base64("img_h500.png")
assimilator_b64 = image_to_base64("img_assimilator.png")
lecithin_b64 = image_to_base64("img_lecithin.png")

# HTML контент
html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
@page {{
    size: A4;
    margin: 0;
}}
@page content {{
    margin: 1.5cm 2cm;
}}
body {{
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    font-size: 11pt;
}}

/* Cover page */
.cover {{
    page: cover;
    width: 100%;
    height: 100vh;
    background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    page-break-after: always;
}}
.cover img {{
    max-width: 80%;
    max-height: 70vh;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.3);
}}
.cover h1 {{
    color: #1B5E20;
    font-size: 36pt;
    margin-top: 30px;
    margin-bottom: 10px;
}}
.cover p {{
    color: #388E3C;
    font-size: 16pt;
}}

/* Content pages */
.content {{
    page: content;
}}
h1 {{
    color: #1B5E20;
    font-size: 24pt;
    text-align: center;
    margin-bottom: 20px;
    page-break-before: always;
}}
h1:first-of-type {{
    page-break-before: avoid;
}}
h2 {{
    color: #2E7D32;
    font-size: 16pt;
    border-bottom: 3px solid #81C784;
    padding-bottom: 8px;
    margin-top: 25px;
}}
h3 {{
    color: #388E3C;
    font-size: 13pt;
    margin-top: 15px;
}}

/* Alert boxes */
.alert {{
    background: #FFEBEE;
    border-left: 5px solid #E53935;
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 0 10px 10px 0;
}}
.alert-title {{
    color: #C62828;
    font-weight: bold;
    font-size: 14pt;
    margin-bottom: 10px;
}}

/* Symptom list */
.symptoms {{
    background: #FFF3E0;
    padding: 20px;
    border-radius: 10px;
    margin: 20px 0;
}}
.symptoms li {{
    margin: 10px 0;
    font-size: 12pt;
}}

/* Product cards */
.product {{
    background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%);
    border-radius: 15px;
    padding: 20px;
    margin: 25px 0;
    page-break-inside: avoid;
}}
.product-header {{
    display: flex;
    align-items: center;
    margin-bottom: 15px;
}}
.product-icon {{
    font-size: 36pt;
    margin-right: 15px;
}}
.product-title {{
    color: #1B5E20;
    font-size: 18pt;
    margin: 0;
}}
.product-subtitle {{
    color: #558B2F;
    font-size: 12pt;
    margin: 0;
}}
.product img {{
    width: 100%;
    max-width: 300px;
    border-radius: 10px;
    margin: 15px auto;
    display: block;
}}
.product ul {{
    margin: 10px 0;
}}
.product li {{
    margin: 5px 0;
}}
.science-fact {{
    background: #E3F2FD;
    border-left: 4px solid #1976D2;
    padding: 10px 15px;
    margin: 15px 0;
    font-style: italic;
    color: #0D47A1;
}}

/* CTA buttons */
.cta {{
    display: block;
    background: linear-gradient(135deg, #43A047 0%, #2E7D32 100%);
    color: white !important;
    text-decoration: none;
    padding: 15px 30px;
    border-radius: 50px;
    text-align: center;
    font-size: 14pt;
    font-weight: bold;
    margin: 20px auto;
    max-width: 400px;
    box-shadow: 0 4px 15px rgba(46, 125, 50, 0.4);
}}
.cta:hover {{
    background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);
}}
.cta-secondary {{
    background: linear-gradient(135deg, #1976D2 0%, #0D47A1 100%);
    box-shadow: 0 4px 15px rgba(25, 118, 210, 0.4);
}}

/* Results table */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}}
th {{
    background: #2E7D32;
    color: white;
    padding: 12px;
    text-align: left;
}}
td {{
    padding: 12px;
    border-bottom: 1px solid #C8E6C9;
}}
tr:nth-child(even) {{
    background: #F1F8E9;
}}

/* Price comparison */
.price-box {{
    background: #FFF8E1;
    border: 2px solid #FFC107;
    border-radius: 15px;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
}}
.price-old {{
    color: #999;
    text-decoration: line-through;
    font-size: 18pt;
}}
.price-new {{
    color: #2E7D32;
    font-size: 32pt;
    font-weight: bold;
}}
.price-save {{
    background: #E53935;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-weight: bold;
}}

/* Benefits list */
.benefits {{
    background: #E8F5E9;
    border-radius: 15px;
    padding: 20px;
    margin: 20px 0;
}}
.benefits li {{
    margin: 10px 0;
    padding-left: 30px;
    position: relative;
}}
.benefits li::before {{
    content: "✅";
    position: absolute;
    left: 0;
}}

/* Footer */
.footer {{
    text-align: center;
    color: #888;
    font-size: 9pt;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #ddd;
}}
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
    <img src="data:image/jpeg;base64,{cover_b64}" alt="Детокс без мучений">
    <h1>ДЕТОКС БЕЗ МУЧЕНИЙ</h1>
    <p>Научный подход к очищению организма</p>
</div>

<!-- CONTENT -->
<div class="content">

<h1>⚠️ ВНИМАНИЕ: Это касается ТЕБЯ</h1>

<div class="alert">
    <div class="alert-title">Прямо сейчас в твоём теле:</div>
    <p><strong>2-5 кг токсинов и шлаков</strong> — накопленных за годы жизни в городе</p>
    <p><strong>До 15 кг каловых камней</strong> — в кишечнике (да, это не шутка)</p>
    <p><strong>Тысячи микроорганизмов</strong> — которые отравляют тебя изнутри</p>
</div>

<h2>Узнаёшь себя?</h2>

<div class="symptoms">
    <ul>
        <li>😴 <strong>Просыпаешься уставшим</strong>, хотя спал 8 часов</li>
        <li>🍕 <strong>Вздутие после каждого приёма пищи</strong>, даже от "правильной еды"</li>
        <li>😤 <strong>Прыщи, тусклая кожа, отёки</strong> — косметологи разводят руками</li>
        <li>🧠 <strong>Туман в голове</strong>, сложно сосредоточиться</li>
        <li>⚖️ <strong>Лишние килограммы не уходят</strong>, хотя сидишь на диетах</li>
        <li>💊 <strong>Постоянно болеешь</strong> — иммунитет на нуле</li>
    </ul>
</div>

<p style="text-align: center; font-size: 14pt; color: #C62828;">
    <strong>Врачи говорят "всё нормально", но ты ЧУВСТВУЕШЬ что это не так.</strong>
</p>

<h1>Решение существует</h1>

<h2>CORAL DETOX — система очищения на клеточном уровне</h2>

<p style="text-align: center; font-size: 14pt;">
    <strong>4 продукта. 30 дней. Результат с первой недели.</strong>
</p>

<p>Разработано в Японии. 30+ лет исследований. Миллионы довольных клиентов в 40 странах.</p>

<!-- PRODUCT 1 -->
<div class="product">
    <div class="product-header">
        <span class="product-icon">💧</span>
        <div>
            <h3 class="product-title">CORAL-MINE</h3>
            <p class="product-subtitle">Живая вода из глубин океана</p>
        </div>
    </div>
    <img src="data:image/png;base64,{coral_mine_b64}" alt="Coral-Mine">
    <p>Измельчённый коралл Санго с острова Окинава (Япония) — места, где люди живут дольше всех на планете.</p>
    <ul>
        <li>✅ Ощелачивает воду до pH 8.5-9</li>
        <li>✅ Насыщает 70+ минералами в ионной форме</li>
        <li>✅ Улучшает гидратацию клеток на 40%</li>
    </ul>
    <div class="science-fact">
        <strong>Научный факт:</strong> Жители Окинавы пьют воду, проходящую через коралловые породы. Средняя продолжительность жизни — 87 лет.
    </div>
    <a href="https://coralclub.us/shop/coral-mine.html" class="cta">🛒 КУПИТЬ CORAL-MINE</a>
</div>

<!-- PRODUCT 2 -->
<div class="product">
    <div class="product-header">
        <span class="product-icon">⚡</span>
        <div>
            <h3 class="product-title">H-500</h3>
            <p class="product-subtitle">Самый мощный антиоксидант в мире</p>
        </div>
    </div>
    <img src="data:image/png;base64,{h500_b64}" alt="H-500">
    <p>Гидрид кремния — донор электронов, который нейтрализует свободные радикалы эффективнее витамина C в 100 раз.</p>
    <ul>
        <li>✅ Защищает клетки от окислительного стресса</li>
        <li>✅ Даёт чистую энергию без кофеина</li>
        <li>✅ Ускоряет восстановление после тренировок</li>
    </ul>
    <div class="science-fact">
        <strong>Научный факт:</strong> 1 капсула H-500 = антиоксидантная сила 10,000 стаканов апельсинового сока.
    </div>
    <a href="https://coralclub.us/shop/h-500.html" class="cta">🛒 КУПИТЬ H-500</a>
</div>

<!-- PRODUCT 3 -->
<div class="product">
    <div class="product-header">
        <span class="product-icon">🧪</span>
        <div>
            <h3 class="product-title">ASSIMILATOR</h3>
            <p class="product-subtitle">Ферменты для идеального пищеварения</p>
        </div>
    </div>
    <img src="data:image/png;base64,{assimilator_b64}" alt="Assimilator">
    <p>Комплекс растительных ферментов + витамины A и D. Расщепляет пищу полностью, не оставляя шансов гниению.</p>
    <ul>
        <li>✅ Расщепляет белки, жиры, углеводы</li>
        <li>✅ Предотвращает вздутие и тяжесть</li>
        <li>✅ Снимает нагрузку с поджелудочной</li>
    </ul>
    <div class="science-fact">
        <strong>Научный факт:</strong> После 25 лет выработка ферментов падает на 13% каждые 10 лет. К 50 годам у тебя вдвое меньше, чем нужно.
    </div>
    <a href="https://coralclub.us/shop/assimilator.html" class="cta">🛒 КУПИТЬ ASSIMILATOR</a>
</div>

<!-- PRODUCT 4 -->
<div class="product">
    <div class="product-header">
        <span class="product-icon">🛡️</span>
        <div>
            <h3 class="product-title">CORAL LECITHIN</h3>
            <p class="product-subtitle">Защита печени и мозга</p>
        </div>
    </div>
    <img src="data:image/png;base64,{lecithin_b64}" alt="Coral Lecithin">
    <p>Фосфолипиды из соевых бобов — строительный материал для клеточных мембран.</p>
    <ul>
        <li>✅ Защищает клетки печени от токсинов</li>
        <li>✅ Помогает выводить жирорастворимые яды</li>
        <li>✅ Улучшает память и концентрацию</li>
    </ul>
    <div class="science-fact">
        <strong>Научный факт:</strong> Печень на 65% состоит из лецитина. При дефиците развивается жировой гепатоз.
    </div>
    <a href="https://coralclub.us/shop/coral-lecithin.html" class="cta">🛒 КУПИТЬ CORAL LECITHIN</a>
</div>

<h1>Результаты по дням</h1>

<table>
    <tr>
        <th>Срок</th>
        <th>Что почувствуешь</th>
    </tr>
    <tr>
        <td><strong>День 3-5</strong></td>
        <td>Уходит вздутие, лёгкость после еды</td>
    </tr>
    <tr>
        <td><strong>День 7-10</strong></td>
        <td>Больше энергии, глубже сон</td>
    </tr>
    <tr>
        <td><strong>День 14-21</strong></td>
        <td>Кожа чище, отёки уходят</td>
    </tr>
    <tr>
        <td><strong>День 30</strong></td>
        <td>Минус 2-5 кг, ясная голова</td>
    </tr>
</table>

<h1>💰 Сколько это стоит?</h1>

<div class="price-box">
    <p>Coral Detox (набор 4 продукта)</p>
    <p><span class="price-old">$107 в розницу</span></p>
    <p><span class="price-new">$85</span> в клубе</p>
    <p><span class="price-save">ЭКОНОМИЯ $22</span></p>
    <p style="margin-top: 15px;"><strong>И эта скидка действует ПОЖИЗНЕННО</strong></p>
</div>

<h1>🎁 Как получить скидку 20%?</h1>

<h2>Вступи в Coral Club — это БЕСПЛАТНО</h2>

<div class="benefits">
    <ul>
        <li><strong>Регистрация занимает 2 минуты</strong></li>
        <li><strong>Никаких ежемесячных платежей</strong></li>
        <li><strong>Никаких обязательств покупать</strong></li>
        <li><strong>Скидка 20% активируется мгновенно</strong></li>
        <li><strong>Действует на ВСЕ 500+ продуктов навсегда</strong></li>
    </ul>
</div>

<h2>Что ещё даёт членство?</h2>

<ul>
    <li>💰 <strong>20% скидка</strong> на все продукты</li>
    <li>🎁 <strong>Бонусы за покупки</strong> — конвертируются в продукты</li>
    <li>📚 <strong>Обучающие вебинары</strong> от врачей</li>
    <li>🌍 <strong>Единый аккаунт</strong> работает в 40 странах</li>
    <li>👨‍👩‍👧‍👦 <strong>Семейная скидка</strong> для близких</li>
</ul>

<h1>⚡ ДЕЙСТВУЙ СЕЙЧАС</h1>

<p style="text-align: center; font-size: 14pt;">
    Каждый день без детокса — это ещё один день, когда токсины разрушают твоё тело.
</p>

<a href="https://coralclub.us/registration" class="cta" style="font-size: 16pt; padding: 20px 40px;">
    👉 ПОЛУЧИТЬ СКИДКУ 20% — РЕГИСТРАЦИЯ
</a>

<a href="https://coralclub.us/shop/coral-detox.html" class="cta cta-secondary" style="margin-top: 15px;">
    🛒 ЗАКАЗАТЬ CORAL DETOX
</a>

<div class="footer">
    <p>© 2025 | Продукция сертифицирована. Не является лекарственным средством.</p>
    <p>Биологически активная добавка. Перед применением проконсультируйтесь со специалистом.</p>
</div>

</div>
</body>
</html>
"""

# Генерируем PDF
HTML(string=html_content).write_pdf("detox-leadmagnet-v2.pdf")
print("✅ PDF created: detox-leadmagnet-v2.pdf")
