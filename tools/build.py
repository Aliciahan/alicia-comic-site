"""Alicia Comic 的小站：介绍、支持、隐私政策，中 / 英 / 日 / 法四种语言。
改文字只改这里，然后 `python3 tools/build.py` 重新生成各语言目录下的 HTML（生成结果也提交，GitHub Pages 直接用）。"""
import html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = "alicia.han007@gmail.com"
UPDATED = "2026-10-28"
LANGS = ["zh", "en", "ja", "fr"]
HTML_LANG = {"zh": "zh-Hans", "en": "en", "ja": "ja", "fr": "fr"}
LANG_NAME = {"zh": "中文", "en": "English", "ja": "日本語", "fr": "Français"}
FONT = {"zh": "'Noto Serif SC'", "ja": "'Noto Serif JP'", "en": "Newsreader", "fr": "Newsreader"}

T = {
"zh": dict(
    nav=("介绍", "支持", "隐私"),
    tagline="为折叠屏而生的漫画阅读器",
    lead="读你自己的书库：CBZ、EPUB、PDF、图片文件夹，或家里 NAS 上的 Komga / OPDS。低清老漫画也能看清网点和线条。",
    duo="iPhone Duo 展开横拿就是一本翻开的单行本，铰链落在书缝上；竖着拿一整页铺满；合上外屏也有专属排法。目前按模拟器调好，真机适配从 2026 年 11 月末开始。",
    status="1.0 正在 TestFlight 内测，上架后这里会放 App Store 链接。",
    features=[
        ("超清引擎", "自己训练的漫画超分，在 iPhone 上把低清黑白页的网点和线条重新画清楚，彩页用系统超分；全部在设备上完成，不上传任何一页。第一次像配眼镜一样在「印刷感」和「平滑」里挑一副，插电过夜时先把接下来要读的页做好。"),
        ("一格一格读", "自动认出分镜和对白，按阅读方向一格格看。"),
        ("翻译", "对白在设备上翻译，按住看原文。"),
        ("纸与墨", "素净的纸色、书脊排成的书架、跟着系统深色的夜读。"),
        ("阅读日记", "每天读了什么、读了多久，最佳一格做成会动的画面。"),
        ("隐私", "不收集任何数据。书库和阅读记录只在你的设备和你自己的 iCloud 里。"),
    ],
    credit="截图与内置示例：Pepper&Carrot，David Revoy，CC-BY 4.0。",
    support_title="支持",
    support_lead="遇到问题、想要的功能，都可以写信给我。",
    contact="联系邮箱",
    faq=[
        ("能读哪些格式？", "CBZ / ZIP、EPUB、PDF 和图片文件夹；也能连接你自己的 Komga 或 OPDS 服务器边读边取。"),
        ("怎么把书放进来？", "书架右上角「+」从「文件」导入；也可以在设置里打开 Wi‑Fi 传书，用电脑浏览器把书拖进来；或者添加你的服务器。"),
        ("书库会在设备之间同步吗？", "会。打开 iCloud 后，书库和阅读记录一起放在你自己的 iCloud 里同步，不经过任何第三方服务器。"),
        ("「超清」为什么有时候没开始？", "超清很费电，所以发热、开着低电量模式时会暂停；也可以在设置 › 画质里设成只在充电时做。插着电过夜时，App 会把接下来要读的页先做好。"),
        ("iPhone Duo 呢？", "外屏、展开读双页、半开立成帐篷各有一套排法。目前按模拟器调好，真机适配从 2026 年 11 月末开始。"),
        ("App 提供漫画吗？", "不提供。请导入你自己拥有的书，或连接你自己的服务器。"),
    ],
    privacy_title="隐私政策",
    privacy=[
        ("一句话", "Alicia Comic 不收集任何数据：没有账号、没有统计、没有广告、没有第三方 SDK。"),
        ("你的书库和阅读记录", "只存在你的设备上；打开 iCloud 时，存在你自己 iCloud 的私有数据库和 iCloud Drive 里。开发者看不到。"),
        ("服务器", "你添加的 Komga / OPDS 服务器地址和账号存在设备上，密码放在钥匙串里；App 只和你填的那台服务器通信。"),
        ("天气", "阅读日记的天气用苹果的 WeatherKit，只在你打开日记时取当天的大致天气，不保存位置。"),
        ("翻译", "用系统的翻译框架在设备上完成，对白不会发给开发者。"),
        ("诊断", "崩溃和性能报告只留在本机；只有你在设置 › 关于里自己导出、发给我，它才会离开设备。系统的「与开发者共享分析」由你在系统设置里决定。"),
        ("儿童", "App 不收集任何人的数据，包括儿童。"),
        ("变更", "这份政策有变化时会更新本页，并写明更新日期。"),
    ],
    updated="更新于",
    footer="© 2026 Alicia Han",
),
"en": dict(
    nav=("About", "Support", "Privacy"),
    tagline="The manga reader for foldables",
    lead="Read your own library: CBZ, EPUB, PDF, image folders, or a Komga / OPDS server on your NAS. Even old low-res scans keep their screentones and lines.",
    duo="Open iPhone Duo sideways and it becomes an open volume, with the hinge on the gutter; upright, one page fills the screen; closed, the outer screen has its own layout. Tuned in the simulator today; on-device tuning starts in late November 2026.",
    status="Version 1.0 is in TestFlight testing. The App Store link will appear here at launch.",
    features=[
        ("HD Engine", "Our own manga upscaling model redraws the screentones and lines of low-res black-and-white pages right on your iPhone; color pages use the system upscaler. Nothing is uploaded. Pick “Print-like” or “Smooth” like an eye test, and while charging overnight the pages you’ll read next are prepared in HD."),
        ("Panel by panel", "Panels and dialogue are detected automatically and shown one by one in reading order."),
        ("Translation", "Dialogue is translated on device; hold to see the original."),
        ("Paper & ink", "A calm paper tone, a shelf of real spines, and night reading that follows Dark Mode."),
        ("Reading diary", "What you read each day and for how long, with your best panel brought to life."),
        ("Privacy", "No data collected. Your library and reading history stay on your devices and in your own iCloud."),
    ],
    credit="Screenshots and built-in sample: Pepper&Carrot by David Revoy, CC-BY 4.0.",
    support_title="Support",
    support_lead="Questions, problems or wishes — write to me.",
    contact="Contact",
    faq=[
        ("Which formats can it read?", "CBZ / ZIP, EPUB, PDF and image folders. It can also stream from your own Komga or OPDS server."),
        ("How do I add books?", "Tap “+” at the top right of the shelf to import from Files; turn on Wi‑Fi transfer in Settings and drag books in from a computer’s browser; or add your server."),
        ("Does my library sync between devices?", "Yes. With iCloud on, your library and reading history sync together through your own iCloud — no third-party server involved."),
        ("Why doesn’t HD start sometimes?", "HD uses a lot of power, so it pauses when the phone is hot or in Low Power Mode; you can also limit it to charging in Settings › Quality. While charging overnight, the app prepares the pages you’ll read next."),
        ("What about iPhone Duo?", "The outer screen, the open spread and the half-open tent each have their own layout. They are tuned in the simulator today; on-device tuning starts in late November 2026."),
        ("Does the app provide comics?", "No. Import books you own or connect your own server."),
    ],
    privacy_title="Privacy Policy",
    privacy=[
        ("In short", "Alicia Comic collects no data: no account, no analytics, no ads, no third-party SDKs."),
        ("Your library and reading history", "Stored only on your device and, if you turn on iCloud, in your own iCloud private database and iCloud Drive. The developer cannot see them."),
        ("Servers", "Komga / OPDS addresses and accounts you add are stored on your device, passwords in the Keychain; the app talks only to the server you entered."),
        ("Weather", "The reading diary’s weather comes from Apple’s WeatherKit, fetched only when you open the diary; your location is not stored."),
        ("Translation", "Done on device by the system Translation framework; dialogue is never sent to the developer."),
        ("Diagnostics", "Crash and performance reports stay on your device unless you export them yourself from Settings › About and send them to me. Sharing analytics with developers is your choice in system Settings."),
        ("Children", "The app collects no data from anyone, including children."),
        ("Changes", "If this policy changes, this page will be updated with a new date."),
    ],
    updated="Updated",
    footer="© 2026 Alicia Han",
),
"ja": dict(
    nav=("紹介", "サポート", "プライバシー"),
    tagline="折りたたみ画面のための漫画リーダー",
    lead="あなた自身のライブラリを読むためのアプリ。CBZ、EPUB、PDF、画像フォルダ、NAS 上の Komga / OPDS に対応。解像度の低い古いスキャンでも、トーンと線がくっきり。",
    duo="iPhone Duo を横に開けば見開きの単行本、ヒンジがちょうどノドに。縦に持てば一ページが画面いっぱい、閉じても外側の画面専用のレイアウト。現在はシミュレータで調整しており、実機での調整は2026年11月末から始めます。",
    status="バージョン 1.0 は TestFlight でテスト中です。公開後、ここに App Store へのリンクを掲載します。",
    features=[
        ("高画質エンジン", "独自に学習させた漫画用超解像で、低画質の白黒ページのトーンと線を iPhone の中で描き直します。カラーはシステムの超解像。ページは外に送りません。眼鏡を選ぶように「印刷風」と「なめらか」を選べ、夜の充電中に次のページを先に高画質化します。"),
        ("コマ送り", "コマとセリフを自動で見つけ、読む順に一コマずつ表示します。"),
        ("翻訳", "セリフは端末内で翻訳。長押しで原文が見られます。"),
        ("紙とインク", "落ち着いた紙の色、背表紙が並ぶ本棚、ダークモードに合わせた夜の読書。"),
        ("読書日記", "毎日読んだものと時間を記録。いちばんのコマが動き出します。"),
        ("プライバシー", "データは一切収集しません。ライブラリと読書記録は、あなたのデバイスとあなた自身の iCloud の中だけに。"),
    ],
    credit="スクリーンショットと内蔵サンプル：Pepper&Carrot（David Revoy、CC-BY 4.0）。",
    support_title="サポート",
    support_lead="不具合やご要望は、メールでお気軽にどうぞ。",
    contact="お問い合わせ",
    faq=[
        ("どの形式が読めますか？", "CBZ / ZIP、EPUB、PDF、画像フォルダ。ご自身の Komga / OPDS サーバーから読みながら取得することもできます。"),
        ("本はどうやって入れますか？", "本棚右上の「+」から「ファイル」で読み込むか、設定で Wi‑Fi 転送をオンにしてパソコンのブラウザからドラッグ、またはサーバーを追加してください。"),
        ("デバイス間で同期されますか？", "はい。iCloud をオンにすると、ライブラリと読書記録がご自身の iCloud で一緒に同期されます。第三者のサーバーは使いません。"),
        ("高画質化が始まらないのはなぜ？", "高画質化は電力を多く使うため、本体が熱いときや低電力モードでは一時停止します。設定 › 画質で充電中のみにもできます。夜に充電しているあいだ、次に読むページを先に用意します。"),
        ("iPhone Duo は？", "外側の画面、見開き、テント型それぞれに専用のレイアウトがあります。現在はシミュレータで調整しており、実機での調整は2026年11月末から始めます。"),
        ("漫画は提供されますか？", "いいえ。お手持ちの本を読み込むか、ご自身のサーバーに接続してください。"),
    ],
    privacy_title="プライバシーポリシー",
    privacy=[
        ("概要", "Alicia Comic はデータを一切収集しません。アカウント、解析、広告、第三者 SDK はありません。"),
        ("ライブラリと読書記録", "お使いのデバイスと、iCloud をオンにした場合はご自身の iCloud のプライベートデータベースと iCloud Drive にのみ保存されます。開発者は見ることができません。"),
        ("サーバー", "追加した Komga / OPDS のアドレスとアカウントはデバイスに、パスワードはキーチェーンに保存されます。アプリは入力されたサーバーとのみ通信します。"),
        ("天気", "読書日記の天気は Apple の WeatherKit を使い、日記を開いたときだけ取得します。位置情報は保存しません。"),
        ("翻訳", "システムの翻訳機能により端末内で行われ、セリフが開発者に送られることはありません。"),
        ("診断", "クラッシュやパフォーマンスのレポートは端末内に残り、設定 › 情報からご自身で書き出して送らない限り外に出ません。開発者との解析データ共有はシステム設定でご自身が選べます。"),
        ("子ども", "子どもを含め、誰のデータも収集しません。"),
        ("変更", "本ポリシーを変更する場合は、このページを更新し日付を記載します。"),
    ],
    updated="更新日",
    footer="© 2026 Alicia Han",
),
"fr": dict(
    nav=("Présentation", "Assistance", "Confidentialité"),
    tagline="Le manga sur écran pliable",
    lead="Lisez votre propre bibliothèque : CBZ, EPUB, PDF, dossiers d’images, ou un serveur Komga / OPDS sur votre NAS. Même les vieux scans basse définition gardent leurs trames et leurs traits.",
    duo="Ouvert à l’horizontale, l’iPhone Duo devient un tome ouvert, la charnière dans la reliure ; à la verticale, une page occupe tout l’écran ; fermé, l’écran extérieur a sa mise en page. Réglé sur le simulateur pour l’instant ; réglages sur l’appareil réel dès fin novembre 2026.",
    status="La version 1.0 est en test sur TestFlight. Le lien App Store apparaîtra ici à la sortie.",
    features=[
        ("Moteur HD", "Notre super-résolution manga redessine trames et traits des pages noir et blanc basse définition, directement sur l’iPhone ; la couleur passe par le système. Rien n’est envoyé. Choisissez « Imprimé » ou « Lisse » comme chez l’opticien ; la nuit, en charge, les pages suivantes sont préparées en HD."),
        ("Case par case", "Cases et bulles sont détectées automatiquement et affichées une à une dans le sens de lecture."),
        ("Traduction", "Les dialogues sont traduits sur l’appareil ; maintenez le doigt pour voir l’original."),
        ("Papier et encre", "Un ton papier sobre, une étagère de vrais dos de livres, et une lecture de nuit qui suit le mode sombre."),
        ("Journal de lecture", "Ce que vous lisez chaque jour et combien de temps, avec votre meilleure case qui prend vie."),
        ("Confidentialité", "Aucune donnée collectée. Votre bibliothèque et votre historique restent sur vos appareils et dans votre propre iCloud."),
    ],
    credit="Captures et exemple intégré : Pepper&Carrot de David Revoy, CC-BY 4.0.",
    support_title="Assistance",
    support_lead="Une question, un problème, une envie ? Écrivez-moi.",
    contact="Contact",
    faq=[
        ("Quels formats sont pris en charge ?", "CBZ / ZIP, EPUB, PDF et dossiers d’images ; l’app peut aussi lire depuis votre propre serveur Komga ou OPDS."),
        ("Comment ajouter des livres ?", "Touchez « + » en haut à droite de l’étagère pour importer depuis Fichiers ; activez le transfert Wi‑Fi dans Réglages et glissez les livres depuis le navigateur d’un ordinateur ; ou ajoutez votre serveur."),
        ("Ma bibliothèque est-elle synchronisée ?", "Oui. Avec iCloud, bibliothèque et historique de lecture se synchronisent ensemble via votre propre iCloud, sans serveur tiers."),
        ("Pourquoi la HD ne démarre-t-elle pas toujours ?", "La HD consomme beaucoup : elle se met en pause quand l’iPhone chauffe ou en mode économie d’énergie, et peut être limitée à la recharge dans Réglages › Qualité. Pendant la recharge de nuit, l’app prépare les pages que vous lirez ensuite."),
        ("Et l’iPhone Duo ?", "L’écran extérieur, la double page ouverte et la position tente ont chacun leur mise en page. Elles sont réglées sur le simulateur pour l’instant ; les réglages sur l’appareil réel commencent fin novembre 2026."),
        ("L’app fournit-elle des BD ?", "Non. Importez les livres que vous possédez ou connectez votre propre serveur."),
    ],
    privacy_title="Politique de confidentialité",
    privacy=[
        ("En bref", "Alicia Comic ne collecte aucune donnée : ni compte, ni statistiques, ni publicité, ni SDK tiers."),
        ("Votre bibliothèque et votre historique", "Stockés uniquement sur votre appareil et, si vous activez iCloud, dans votre propre base privée iCloud et iCloud Drive. Le développeur n’y a pas accès."),
        ("Serveurs", "Les adresses et comptes Komga / OPDS que vous ajoutez restent sur l’appareil, les mots de passe dans le trousseau ; l’app ne communique qu’avec le serveur que vous avez saisi."),
        ("Météo", "La météo du journal vient de WeatherKit d’Apple, récupérée seulement quand vous ouvrez le journal ; votre position n’est pas conservée."),
        ("Traduction", "Effectuée sur l’appareil par le framework de traduction du système ; les dialogues ne sont jamais envoyés au développeur."),
        ("Diagnostics", "Les rapports de plantage et de performance restent sur l’appareil, sauf si vous les exportez vous-même depuis Réglages › À propos pour me les envoyer. Le partage d’analyses avec les développeurs se choisit dans les Réglages du système."),
        ("Enfants", "L’app ne collecte aucune donnée, y compris celles des enfants."),
        ("Modifications", "En cas de changement, cette page sera mise à jour avec une nouvelle date."),
    ],
    updated="Mis à jour le",
    footer="© 2026 Alicia Han",
),
}

def e(s): return html.escape(s, quote=True)

def page(lang, kind, title, body):
    t = T[lang]
    nav = "".join(f'<a href="{href}"{" aria-current=page" if kind == k else ""}>{e(label)}</a>'
                  for k, href, label in zip(("index", "support", "privacy"), ("./", "support.html", "privacy.html"), t["nav"]))
    langs = "".join(f'<a href="../{l}/{"" if kind == "index" else kind + ".html"}" lang="{HTML_LANG[l]}"{" aria-current=true" if l == lang else ""}>{LANG_NAME[l]}</a>' for l in LANGS)
    return f"""<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(t['tagline'])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500&family=Noto+Serif+SC:wght@400;600&family=Noto+Serif+JP:wght@400;600&display=swap">
<link rel="stylesheet" href="../assets/site.css">
<link rel="icon" href="../assets/icon.png">
<style>:root{{--display:{FONT[lang]}}}</style>
</head>
<body>
<header class="bar"><a class="brand" href="./"><img src="../assets/icon.png" alt="" width="28" height="28">Alicia Comic</a><nav>{nav}</nav></header>
<main>
{body}
</main>
<footer><nav class="langs">{langs}</nav><p>{e(t['footer'])} · <a href="mailto:{EMAIL}">{EMAIL}</a></p></footer>
</body>
</html>
"""

def index(lang):
    t = T[lang]
    feats = "".join(f"<li><h3>{e(h)}</h3><p>{e(p)}</p></li>" for h, p in t["features"])
    shots = "".join(f'<img src="../assets/shots/{lang}-{i}.jpg" alt="" loading="lazy" width="420" height="912">' for i in range(1, 9)) if os.path.exists(os.path.join(ROOT, "assets", "shots", f"{lang}-1.jpg")) else ""
    body = f"""<section class="hero"><h1>{e(t['tagline'])}</h1><p class="lead">{e(t['lead'])}</p><p class="status">{e(t['status'])}</p></section>
{f'<section class="shots">{shots}</section>' if shots else ''}
<section><ul class="features">{feats}</ul><p class="note">{e(t['duo'])}</p><p class="credit">{e(t['credit'])}</p></section>"""
    return page(lang, "index", f"Alicia Comic — {t['tagline']}", body)

def support(lang):
    t = T[lang]
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t["faq"])
    body = f"""<section class="doc"><h1>{e(t['support_title'])}</h1><p class="lead">{e(t['support_lead'])}</p>
<p class="contact">{e(t['contact'])}：<a href="mailto:{EMAIL}">{EMAIL}</a></p>{faq}</section>""".replace("：", ": " if lang in ("en", "fr") else "：")
    return page(lang, "support", f"{t['support_title']} · Alicia Comic", body)

def privacy(lang):
    t = T[lang]
    items = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h, p in t["privacy"])
    body = f"""<section class="doc"><h1>{e(t['privacy_title'])}</h1><p class="meta">{e(t['updated'])} {UPDATED}</p>{items}
<h2>{e(t['contact'])}</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></section>"""
    return page(lang, "privacy", f"{t['privacy_title']} · Alicia Comic", body)

def root():
    links = "".join(f'<a href="{l}/" lang="{HTML_LANG[l]}">{LANG_NAME[l]}</a>' for l in LANGS)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Alicia Comic</title><link rel="stylesheet" href="assets/site.css"><link rel="icon" href="assets/icon.png">
<script>(function(){{var l=(navigator.languages||[navigator.language||"en"]).join(",").toLowerCase();
var m=/(^|,)zh/.test(l)?"zh":/(^|,)ja/.test(l)?"ja":/(^|,)fr/.test(l)?"fr":"en";location.replace(m+"/");}})();</script>
</head><body><main class="pick"><img src="assets/icon.png" alt="" width="64" height="64"><h1>Alicia Comic</h1><nav class="langs">{links}</nav></main></body></html>
"""

if __name__ == "__main__":
    for lang in LANGS:
        os.makedirs(os.path.join(ROOT, lang), exist_ok=True)
        for name, fn in (("index.html", index), ("support.html", support), ("privacy.html", privacy)):
            open(os.path.join(ROOT, lang, name), "w").write(fn(lang))
    open(os.path.join(ROOT, "index.html"), "w").write(root())
    print("built", ", ".join(LANGS))
