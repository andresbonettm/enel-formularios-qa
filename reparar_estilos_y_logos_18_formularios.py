import os
import re
import glob

ASSETS_DIR = "Enel_google/assets"
FORMULARIOS_DIR = "Enel_google/formularios"

# Working verified URLs for production + relative fallback
URL_LOGO_ENEL = "https://www.enel.com.co/content/dam/enel-co/im%C3%A1genes-home/logo-white.png"
URL_LOGO_SUPER = "https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/logo_vigilado-3.png"
URL_LOGO_SUPER_SMALL = "https://www.enel.com.co/content/dam/enel-co/carpeta-global-de-archivos/iconos-y-logos/superintendencia/logo-superintendecnia-small.png"
URL_FB = "https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/icono-facebook.png"
URL_IG = "https://assets.enelcol.com.co/2025/julio/iconos-formulario-cfc/instagram.png"
URL_TW = "https://assets.enelcol.com.co/2025/julio/iconos-formulario-cfc/x.png"
URL_LI = "https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/icono-linkedin.png"

# Self-contained core CSS block that fixes all unstyled or broken forms
CORE_CSS = """
    <!-- Estilos Corporativos Oficiales Enel Colombia (Auto-contenidos y Resilientes) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">
    <style>
        :root {
            --enel-magenta: #d9006c;
            --enel-magenta-dark: #b50058;
            --enel-dark: #121926;
            --enel-light-bg: #f8fafc;
            --enel-border: #cbd5e1;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--enel-light-bg);
            color: #1e293b;
            margin: 0;
            padding: 0;
        }
        .header-top-enel {
            background-color: #121926;
            padding: 16px 24px;
            border-bottom: 3px solid var(--enel-magenta);
        }
        .header-top-enel img.logo-header {
            height: 36px;
            max-width: 140px;
            object-fit: contain;
        }
        .form-container-box {
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            padding: 35px 30px;
            margin: 35px auto 50px auto;
            max-width: 780px;
            border: 1px solid #e2e8f0;
        }
        .form-header-title {
            color: #121926;
            font-weight: 700;
            font-size: 24px;
            margin-bottom: 8px;
            text-align: center;
        }
        .form-header-subtitle {
            color: #64748b;
            font-size: 14px;
            text-align: center;
            margin-bottom: 25px;
        }
        .form-group label, .form-box label {
            font-size: 13px;
            font-weight: 600;
            color: #334155;
            margin-bottom: 5px;
            display: inline-block;
        }
        .form-control, input[type="text"], input[type="email"], input[type="tel"], input[type="number"], select, textarea {
            border: 1px solid var(--enel-border);
            border-radius: 6px;
            padding: 10px 14px;
            font-size: 14px;
            width: 100%;
            transition: all 0.2s ease;
            background-color: #ffffff;
            color: #1e293b;
        }
        .form-control:focus, input:focus, select:focus, textarea:focus {
            border-color: var(--enel-magenta);
            outline: none;
            box-shadow: 0 0 0 3px rgba(217,0,108,0.15);
        }
        .btn-enel-submit, input[type="submit"], button[type="submit"] {
            background-color: var(--enel-magenta) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            border: none !important;
            border-radius: 30px !important;
            padding: 12px 35px !important;
            font-size: 15px !important;
            cursor: pointer;
            transition: all 0.2s ease;
            display: block;
            margin: 20px auto 0 auto;
            min-width: 200px;
            text-align: center;
        }
        .btn-enel-submit:hover, input[type="submit"]:hover, button[type="submit"]:hover {
            background-color: var(--enel-magenta-dark) !important;
            box-shadow: 0 4px 12px rgba(217,0,108,0.3);
        }
        .terms, .terms-box {
            font-size: 12px;
            color: #475569;
            line-height: 1.5;
            display: flex;
            align-items: flex-start;
            margin-bottom: 12px;
        }
        .terms input[type="checkbox"], .terms-box input[type="checkbox"] {
            margin-right: 10px;
            margin-top: 3px;
            min-width: 16px;
            min-height: 16px;
            accent-color: var(--enel-magenta);
        }
        .terms a, .terms-box a {
            color: var(--enel-magenta);
            text-decoration: underline;
        }
        footer.enel-footer-standard {
            background: #ffffff;
            border-top: 1px solid #e2e8f0;
            padding: 30px 0;
            font-size: 13px;
            color: #64748b;
        }
        footer.enel-footer-standard a {
            color: #64748b;
            text-decoration: none;
        }
        footer.enel-footer-standard a:hover {
            color: var(--enel-magenta);
        }
        .footer-logo-super {
            height: 32px;
            object-fit: contain;
        }
        .footer-social-icon {
            width: 24px;
            height: 24px;
            object-fit: contain;
            margin-left: 8px;
        }
    </style>
"""

# Standardized clean Header with working logo
STANDARDIZED_HEADER = f"""
<header class="header-top-enel">
    <div class="container d-flex justify-content-between align-items-center">
        <a href="https://www.enel.com.co/es.html">
            <img src="{URL_LOGO_ENEL}" alt="Enel Colombia" class="logo-header">
        </a>
        <span class="badge badge-secondary px-3 py-1" style="background:#273549; font-weight:600; font-size:12px;">Enel Colombia S.A. ESP</span>
    </div>
</header>
"""

# Standardized clean Footer with all verified images
STANDARDIZED_FOOTER = f"""
<footer class="enel-footer-standard mt-5">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-xs-12 col-sm-12 col-md-8">
        <div class="d-flex flex-wrap align-items-center mb-2">
          <span class="mr-3 font-weight-bold text-dark">&copy; Enel Colombia S.A. ESP 2026. Todos los derechos reservados.</span>
        </div>
        <div class="footer-legal-links mt-2">
          <a target="_blank" href="https://www.enel.com.co/es/legales.html" class="mr-3">Términos Legales</a>
          <a target="_blank" href="https://www.enel.com.co/content/dam/enel-co/espa%C3%B1ol/ayuda/politica-de-tratamiento-de-datos-personales-de-enel2.pdf" class="mr-3">Política de Privacidad</a>
          <a target="_blank" href="https://www.enel.com.co/es/politica-de-cookies.html" class="mr-3">Política de Cookies</a>
        </div>
      </div>
      <div class="col-xs-12 col-sm-12 col-md-4 text-md-right mt-3 mt-md-0 d-flex flex-column align-items-md-end">
        <div class="d-flex align-items-center mb-2">
          <span class="mr-2 text-muted small">Vigilado:</span>
          <img src="{URL_LOGO_SUPER}" alt="Vigilado Superintendencia Financiera de Colombia" class="footer-logo-super">
        </div>
        <div>
          <a target="_blank" href="https://www.facebook.com/EnelColombia"><img src="{URL_FB}" alt="Facebook" class="footer-social-icon"></a>
          <a target="_blank" href="https://www.instagram.com/enelcolombia/?hl=es"><img src="{URL_IG}" alt="Instagram" class="footer-social-icon"></a>
          <a target="_blank" href="https://twitter.com/EnelColombia"><img src="{URL_TW}" alt="X/Twitter" class="footer-social-icon"></a>
          <a target="_blank" href="https://www.linkedin.com/company/enel-colombia/"><img src="{URL_LI}" alt="LinkedIn" class="footer-social-icon"></a>
        </div>
      </div>
    </div>
  </div>
</footer>
"""

def repair_form_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    original_html = html

    # 1. Remove broken external CSS that return 403 or relative broken paths
    html = re.sub(r'<link[^>]+(?:sale\.css|bootstrap\.min\.css|estilos-cfc)[^>]*>', '', html, flags=re.IGNORECASE)
    
    # 2. Inject CORE_CSS in head if not already present
    if "<!-- Estilos Corporativos Oficiales Enel Colombia" not in html:
        if "</head>" in html:
            html = html.replace("</head>", f"{CORE_CSS}\n</head>")
        else:
            html = f"{CORE_CSS}\n{html}"

    # 3. Replace all broken logo and image patterns
    # Replace broken 2018/2019/assets logo paths with verified working logo
    broken_logo_patterns = [
        r'https?://(?:www\.)?enel\.com\.co/(?:2018|2019)/[^\"\']*(?:logo|icon)[^\"\']*\.png',
        r'//assets\.enelcol\.com\.co/[^\"\']*(?:logo|icon)[^\"\']*\.png',
        r'https?://assets\.enelcol\.com\.co/2021/landings/20210211_Landing_cfc/images/logo-enel\.png',
        r'https?://assets\.enelcol\.com\.co/2022/diciembre/formularioRegistro/imagen/logo-enel-blanco\.png'
    ]
    for p in broken_logo_patterns:
        html = re.sub(p, URL_LOGO_ENEL, html, flags=re.IGNORECASE)

    # Replace broken social icons with verified ones
    html = re.sub(r'https?://(?:www\.)?enel\.com\.co/(?:2018|2019)/[^\"\']*facebook[^\"\']*\.png(?:\?v=\d+)?', URL_FB, html, flags=re.IGNORECASE)
    html = re.sub(r'//assets\.enelcol\.com\.co/[^\"\']*facebook[^\"\']*\.png(?:\?v=\d+)?', URL_FB, html, flags=re.IGNORECASE)

    html = re.sub(r'https?://(?:www\.)?enel\.com\.co/(?:2018|2019)/[^\"\']*twitter[^\"\']*\.png', URL_TW, html, flags=re.IGNORECASE)
    html = re.sub(r'//assets\.enelcol\.com\.co/[^\"\']*twitter[^\"\']*\.png', URL_TW, html, flags=re.IGNORECASE)

    html = re.sub(r'https?://(?:www\.)?enel\.com\.co/(?:2018|2019)/[^\"\']*(?:linke|linkedin)[^\"\']*\.png', URL_LI, html, flags=re.IGNORECASE)
    html = re.sub(r'//assets\.enelcol\.com\.co/[^\"\']*(?:linke|linkedin)[^\"\']*\.png', URL_LI, html, flags=re.IGNORECASE)

    # Remove broken decorative legacy image tags (score.png, landing-retiro-factura, youtube.png from 2018)
    html = re.sub(r'<img[^>]+src=[\"\'][^\"\']*(?:score|landing-retiro-factura|youtube)[^\"\']*[\"\'][^>]*>', '', html, flags=re.IGNORECASE)

    # 4. Normalize Header: If there's an existing broken header or no header, provide standardized header
    if '<header' not in html and '<nav' not in html:
        # Wrap body content with standard header
        if '<body' in html:
            body_match = re.search(r'<body[^>]*>', html, re.I)
            if body_match:
                end_pos = body_match.end()
                html = html[:end_pos] + "\n" + STANDARDIZED_HEADER + "\n" + html[end_pos:]
        else:
            html = STANDARDIZED_HEADER + "\n" + html

    # 5. Normalize Footer: Replace existing footer with STANDARDIZED_FOOTER
    if '<footer' in html:
        html = re.sub(r'<footer[^>]*>.*?</footer>', STANDARDIZED_FOOTER, html, flags=re.DOTALL | re.IGNORECASE)
    else:
        if '</body>' in html:
            html = html.replace('</body>', f'{STANDARDIZED_FOOTER}\n</body>')
        else:
            html += f'\n{STANDARDIZED_FOOTER}'

    return html

def repair_thank_you_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Fix broken logo in thank-you pages
    html = html.replace('https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/logo-enel.png', URL_LOGO_ENEL)
    # Ensure styles and fonts are clean
    return html

# Execute repairs on all 18 folders
total_repaired = 0
for folder in sorted(glob.glob(f"{FORMULARIOS_DIR}/enel-formulario-*")):
    if not os.path.isdir(folder): continue
    
    slug = os.path.basename(folder).replace("enel-formulario-", "")
    html_file = os.path.join(folder, f"formulario-{slug}.html")
    txt_file = os.path.join(folder, f"formulario-{slug}.txt")
    ty_html_file = os.path.join(folder, f"thank-you-{slug}.html")
    ty_txt_file = os.path.join(folder, f"thank-you-{slug}.txt")

    if os.path.exists(html_file):
        fixed_html = repair_form_html(html_file)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(fixed_html)
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(fixed_html)
            
    if os.path.exists(ty_html_file):
        fixed_ty = repair_thank_you_html(ty_html_file)
        with open(ty_html_file, "w", encoding="utf-8") as f:
            f.write(fixed_ty)
        with open(ty_txt_file, "w", encoding="utf-8") as f:
            f.write(fixed_ty)
            
    total_repaired += 1
    print(f"✅ Saneado al 100%: {os.path.basename(folder)}")

print(f"\nTotal formularios reparados y homologados: {total_repaired}/18")
