# -*- coding: utf-8 -*-
from pathlib import Path
import re

base = Path('.')

templates = {
    'root': {
        'nav': '''<nav class="navbar desktop-navbar">
        <div class="navbar-left">
            <a href="index.html" class="navbar-brand">
                <img src="slike/XIVlogoFinalno.png" alt="Logo" class="navbar-logo">
                <span class="navbar-title">XIV гимназија</span>
            </a>
        </div>
        <div class="navbar-center">
            <ul class="navbar-menu">
                <li><a href="index.html">Почетна</a></li>
                <li class="dropdown"><a href="#">О школи▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="skoli/erasmus.html">Erasmus</a>
                        <a class="hRed" href="skoli/etwinning.html">eTwinning</a>
                        <a class="hRed" href="skoli/istorijat.html">Историјат</a>
                        <a class="hRed" href="skoli/ucenici.html">Ученик</a>
                        <a class="hRed" href="skoli/upis.html">Упис</a>
                        <a class="hRed" href="skoli/zaposleni.html">Запослени</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Вести▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="vesti/Casopis.html">Школски часопис</a>
                        <a class="hRed" href="vesti/novosti.html">Новости</a>
                        <a class="hRed" href="https://xivgimnazija.wordpress.com/">Aрхив</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Настава▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="nastava/IzPred.html">Изборни предмети</a>
                        <a class="hRed" href="nastava/predmeti.html">Предмети</a>
                        <a class="hRed" href="nastava/udzbenici.html">Уџбеници</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Активонсти▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="aktivnosti/ekskurzije.html">Екскурзије и путовања</a>
                        <a class="hRed" href="aktivnosti/parlament.html">Ученички парламент</a>
                        <a class="hRed" href="aktivnosti/vannastavneak.html">Секције и ваннаставне активности</a>
                    </div>
                </li>

                <li class="dropdown"><a href="orgrada/organizacijaRada.html">Организација рада</a></li>
            </ul>
            
        </div>
        <div class="hamburger" id="hamburger">
            <span class="line"></span>
            <span class="line"></span>
            <span class="line"></span>
        </div>
    </nav>''',
        'offcanvas': '''    <div class="offcanvas" id="offcanvas">
            <div class="offcanvas-header">
            <button class="exit-btn" id="exit-btn">X</button>
            </div>
    <ul class="offcanvas-links">
            <li>
                <a href="index.html">Почетна</a>
            </li>
            <li>
                    <a href="#" class="dropdown-toggle">O школи</a>
                    <!-- Podmeni -->
                    <ul class="dropdown-menu1">
                        <li class="dropdown-content1"><a href="skoli/erasmus.html">Erasmus</a></li>
                        <li class="dropdown-content1"><a href="skoli/etwinning.html">eTwinning</a></li>
                        <li class="dropdown-content1"><a href="skoli/istorijat.html">Историјат</a></li>
                        <li class="dropdown-content1"><a href="skoli/ucenici.html">Ученик</a></li>
                        <li class="dropdown-content1"><a href="skoli/upis.html">Упис</a></li>
                        <li class="dropdown-content1"><a href="skoli/zaposleni.html">Запослени</a></li>
                    </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">Вестi</a>
                <!-- Podmeni -->
                <ul class="dropdown-menu1">
                    <li class="dropdown-content1"><a href="vesti/Casopis.html">Школски часопис</a></li>
                    <li class="dropdown-content1"><a href="vesti/novosti.html">Новости</a></li>
                    <li class="dropdown-content1"><a href="https://xivgimnazija.wordpress.com/">Aрхив</a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">Nastava</a>
                    <!-- Podmeni -->
                     <ul class="dropdown-menu1">
                         <li class="dropdown-content1"><a href="nastava/IzPred.html">Изборни предмети</a></li>
                         <li class="dropdown-content1"><a href="nastava/predmeti.html">Предмети</a></li>
                         <li class="dropdown-content1"><a href="nastava/udzbenici.html">Уџбеници</a></li>
                     </ul>
            </li>
            <li>
                <a href="#" class="dropdown-toggle">Активонсти</a>
                <!-- Podmeni -->
                <ul class="dropdown-menu1">
                <li class="dropdown-content1"><a href="aktivnosti/ekskurzije.html">Екскурзије и путовања</a></li>
                <li class="dropdown-content1"><a href="aktivnosti/parlament.html">Ученички парламент</a></li>
                <li class="dropdown-content1"><a href="aktivnosti/vannastavneak.html">Секције и ваннаставне активности</a></li>
                </ul>
            </li>
            <li>
                <a href="orgrada/organizacijaRada.html">Organizacija rada</a>

            </li>
        </ul>
    </div>'''
    },
    'vesti': {
        'nav': '''<nav class="navbar desktop-navbar">
        <div class="navbar-left">
            <a href="../index.html" class="navbar-brand">
                <img src="../slike/XIVlogoFinalno.png" alt="Logo" class="navbar-logo">
                <span class="navbar-title">XIV гимназија</span>
            </a>
        </div>
        <div class="navbar-center">
            <ul class="navbar-menu">
                <li><a href="../index.html">Почетна</a></li>
                <li class="dropdown"><a href="#">О школи▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="../skoli/erasmus.html">Erasmus</a>
                        <a class="hRed" href="../skoli/etwinning.html">eTwinning</a>
                        <a class="hRed" href="../skoli/istorijat.html">Историјат</a>
                        <a class="hRed" href="../skoli/ucenici.html">Ученик</a>
                        <a class="hRed" href="../skoli/upis.html">Упис</a>
                        <a class="hRed" href="../skoli/zaposleni.html">Запослени</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Вести▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="Casopis.html">Школски часопис</a>
                        <a class="hRed" href="novosti.html">Новости</a>
                        <a class="hRed" href="https://xivgimnazija.wordpress.com/">Aрхив</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Настава▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="../nastava/IzPred.html">Изборни предмети</a>
                        <a class="hRed" href="../nastava/predmeti.html">Предмети</a>
                        <a class="hRed" href="../nastava/udzbenici.html">Уџбеници</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Активонсти▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="../aktivnosti/ekskurzije.html">Екскурзије и путовања</a>
                        <a class="hRed" href="../aktivnosti/parlament.html">Ученички парламент</a>
                        <a class="hRed" href="../aktivnosti/vannastavneak.html">Секције и ваннаставне активности</a>
                    </div>
                </li>

                <li class="dropdown"><a href="../orgrada/organizacijaRada.html">Организација рада</a></li>
            </ul>
            
        </div>
        <div class="hamburger" id="hamburger">
            <span class="line"></span>
            <span class="line"></span>
            <span class="line"></span>
        </div>
    </nav>''',
        'offcanvas': '''    <div class="offcanvas" id="offcanvas">
            <div class="offcanvas-header">
            <button class="exit-btn" id="exit-btn">X</button>
            </div>
    <ul class="offcanvas-links">
            <li>
                <a href="../index.html">Почетна</a>
            </li>
            <li>
                    <a href="#" class="dropdown-toggle">O школи</a>
                    <!-- Podmeni -->
                    <ul class="dropdown-menu1">
                        <li class="dropdown-content1"><a href="../skoli/erasmus.html">Erasmus</a></li>
                        <li class="dropdown-content1"><a href="../skoli/etwinning.html">eTwinning</a></li>
                        <li class="dropdown-content1"><a href="../skoli/istorijat.html">Историјат</a></li>
                        <li class="dropdown-content1"><a href="../skoli/ucenici.html">Ученик</a></li>
                        <li class="dropdown-content1"><a href="../skoli/upis.html">Упис</a></li>
                        <li class="dropdown-content1"><a href="../skoli/zaposleni.html">Запослени</a></li>
                    </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">Вестi</a>
                <!-- Podmeni -->
                <ul class="dropdown-menu1">
                    <li class="dropdown-content1"><a href="Casopis.html">Школски часопис</a></li>
                    <li class="dropdown-content1"><a href="novosti.html">Новости</a></li>
                    <li class="dropdown-content1"><a href="https://xivgimnazija.wordpress.com/">Aрхив</a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">Nastava</a>
                    <!-- Podmeni -->
                     <ul class="dropdown-menu1">
                         <li class="dropdown-content1"><a href="../nastava/IzPred.html">Изборни предмети</a></li>
                         <li class="dropdown-content1"><a href="../nastava/predmeti.html">Предмети</a></li>
                         <li class="dropdown-content1"><a href="../nastava/udzbenici.html">Уџбеници</a></li>
                     </ul>
            </li>
            <li>
                <a href="#" class="dropdown-toggle">Активонсти</a>
                <!-- Podmeni -->
                <ul class="dropdown-menu1">
                <li class="dropdown-content1"><a href="../aktivnosti/ekskurzije.html">Екскурзије и путовања</a></li>
                <li class="dropdown-content1"><a href="../aktivnosti/parlament.html">Ученички парламент</a></li>
                <li class="dropdown-content1"><a href="../aktivnosti/vannastavneak.html">Секције и ваннаставне активности</a></li>
                </ul>
            </li>
            <li>
                <a href="../orgrada/organizacijaRada.html">Organizacija rada</a>

            </li>
        </ul>
    </div>'''
    },
    'skoli': {
        'nav': '''<nav class="navbar desktop-navbar">
        <div class="navbar-left">
            <a href="../index.html" class="navbar-brand">
                <img src="../slike/XIVlogoFinalno.png" alt="Logo" class="navbar-logo">
                <span class="navbar-title">XIV гимназија</span>
            </a>
        </div>
        <div class="navbar-center">
            <ul class="navbar-menu">
                <li><a href="../index.html">Почетна</a></li>
                <li class="dropdown"><a href="#">О школи▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="erasmus.html">Erasmus</a>
                        <a class="hRed" href="etwinning.html">eTwinning</a>
                        <a class="hRed" href="istorijat.html">Историјат</a>
                        <a class="hRed" href="ucenici.html">Ученик</a>
                        <a class="hRed" href="upis.html">Упис</a>
                        <a class="hRed" href="zaposleni.html">Запослени</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Вести▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="../vesti/Casopis.html">Школски часопис</a>
                        <a class="hRed" href="../vesti/novosti.html">Новости</a>
                        <a class="hRed" href="https://xivgimnazija.wordpress.com/">Aрхив</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Настава▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="../nastava/IzPred.html">Изборни предмети</a>
                        <a class="hRed" href="../nastava/predmeti.html">Предмети</a>
                        <a class="hRed" href="../nastava/udzbenici.html">Уџбеници</a>
                    </div>
                </li>

                <li class="dropdown"><a href="#">Активонсти▼</a>
                    <div class="dropdown-content">
                        <a class="hRed" href="../aktivnosti/ekskurzije.html">Екскурзије и путовања</a>
                        <a class="hRed" href="../aktivnosti/parlament.html">Ученички парламент</a>
                        <a class="hRed" href="../aktivnosti/vannastavneak.html">Секције и ваннаставне активности</a>
                    </div>
                </li>

                <li class="dropdown"><a href="../orgrada/organizacijaRada.html">Организација рада</a></li>
            </ul>
            
        </div>
        <div class="hamburger" id="hamburger">
            <span class="line"></span>
            <span class="line"></span>
            <span class="line"></span>
        </div>
    </nav>''',
        'offcanvas': '''    <div class="offcanvas" id="offcanvas">
            <div class="offcanvas-header">
            <button class="exit-btn" id="exit-btn">X</button>
            </div>
    <ul class="offcanvas-links">
            <li>
                <a href="../index.html">Почетна</a>
            </li>
            <li>
                    <a href="#" class="dropdown-toggle">O школи</a>
                    <!-- Podmeni -->
                    <ul class="dropdown-menu1">
                        <li class="dropdown-content1"><a href="erasmus.html">Erasmus</a></li>
                        <li class="dropdown-content1"><a href="etwinning.html">Erasmus</a></li>
                        <li class="dropdown-content1"><a href="istorijat.html">Историјат</a></li>
                        <li class="dropdown-content1"><a href="ucenici.html">Ученик</a></li>
                        <li class="dropdown-content1"><a href="upis.html">Упис</a></li>
                        <li class="dropdown-content1"><a href="zaposleni.html">Запослени</a></li>
                    </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">Вестi</a>
                <!-- Podmeni -->
                <ul class="dropdown-menu1">
                    <li class="dropdown-content1"><a href="../vesti/Casopis.html">Школски часопис</a></li>
                    <li class="dropdown-content1"><a href="../vesti/novosti.html">Новости</a></li>
                    <li class="dropdown-content1"><a href="https://xivgimnazija.wordpress.com/">Aрхив</a></li>
                </ul>
            </li>

            <li>
                <a href="#" class="dropdown-toggle">Nastava</a>
                    <!-- Podmeni -->
                     <ul class="dropdown-menu1">
                         <li class="dropdown-content1"><a href="../nastava/IzPred.html">Изборни предмети</a></li>
                         <li class="dropdown-content1"><a href="../nastava/predmeti.html">Предмети</a></li>
                         <li class="dropdown-content1"><a href="../nastava/udzbenici.html">Уџбеници</a></li>
                     </ul>
            </li>
            <li>
                <a href="#" class="dropdown-toggle">Активонсти</a>
                <!-- Podmeni -->
                <ul class="dropdown-menu1">
                <li class="dropdown-content1"><a href="../aktivnosti/ekskurzije.html">Екскурзије и путовања</a></li>
                <li class="dropdown-content1"><a href="../aktivnosti/parlament.html">Ученички парламент</a></li>
                <li class="dropdown-content1"><a href="../aktivnosti/vannastavneak.html">Секције и ваннаставне активности</a></li>
                </ul>
            </li>
            <li>
                <a href="../orgrada/organizacijaRada.html">Organizacija rada</a>

            </li>
        </ul>
    </div>'''
    }
}

for folder in ['nastava', 'aktivnosti', 'orgrada']:
    templates[folder] = templates['skoli']

changed = []
for path in sorted(Path('.').rglob('*.html')):
    text = path.read_text(encoding='utf-8')
    original = text
    if path.name == 'index.html':
        folder = 'root'
    else:
        folder = path.parent.name
    if folder in templates:
        text = re.sub(r'<nav class="navbar desktop-navbar">.*?</nav>', templates[folder]['nav'], text, flags=re.S)
        text = re.sub(r'<div class="offcanvas" id="offcanvas">.*?(?=<div class *= *"prazan")', templates[folder]['offcanvas'] + '\n', text, flags=re.S)
    text = text.replace('skoli/ucenik.html', 'skoli/ucenici.html')
    text = text.replace('href="../skoli/ucenik.html"', 'href="../skoli/ucenici.html"')
    text = text.replace('href="ucenik.html"', 'href="ucenici.html"')
    text = text.replace('aktivnosti/ucenicki.html', 'aktivnosti/parlament.html')
    text = text.replace('../aktivnosti/ucenicki.html', '../aktivnosti/parlament.html')
    text = text.replace('aktivnosti/sekcije.html', 'aktivnosti/vannastavneak.html')
    text = text.replace('../aktivnosti/sekcije.html', '../aktivnosti/vannastavneak.html')
    if text != original:
        path.write_text(text, encoding='utf-8')
        changed.append(str(path))

print('Updated files:')
for f in changed:
    print(f)
