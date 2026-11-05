import os
import re
import shutil

# Template base for thank you page
def build_thank_you_html(title, form_name, slug):
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gracias por su interés | Enel Colombia</title>
    <meta name="ROBOTS" content="INDEX, FOLLOW">
    <link rel="shortcut icon" type="image/x-icon" href="https://assets.enelcol.com.co/2021/landings/20210506_LandingRoboDeEnergia/images/favicon.png">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">
    <!-- Google Tag Manager --> 
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-52FXRWD');</script>
    <!-- End Google Tag Manager -->
    <script> window.adobeDataLayer = window.adobeDataLayer || []; </script>
    <script src="https://assets.adobedtm.com/58373ae8f4f6/1b8196dc8ed3/launch-bf0b791f2a5e.min.js" async></script>
    <link rel="stylesheet" type="text/css" href="https://enelsud.info-enel.com/main.min">
    <link rel="stylesheet" type="text/css" href="https://enelsud.info-enel.com/estilos-cfc">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: #f7f9fa;
            color: #2b2b2b;
            margin: 0;
            padding: 0;
        }}
        .header-logo {{
            background: #ffffff;
            padding: 18px 24px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
            border-bottom: 2px solid #e2e8f0;
        }}
        .header-logo img {{
            height: 38px;
        }}
        .thank-you-box {{
            max-width: 680px;
            margin: 60px auto 80px auto;
            background: #ffffff;
            padding: 45px 35px;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
            text-align: center;
        }}
        .check-icon {{
            width: 72px;
            height: 72px;
            margin: 0 auto 20px auto;
            border-radius: 50%;
            background: #e6f7ec;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #10b981;
            font-size: 38px;
            font-weight: bold;
        }}
        .thank-you-box h1 {{
            font-size: 28px;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 14px;
        }}
        .thank-you-box p {{
            font-size: 16px;
            color: #64748b;
            line-height: 1.6;
            margin-bottom: 30px;
        }}
        .btn-enel {{
            background: #d9006c;
            color: #ffffff;
            padding: 12px 28px;
            border-radius: 30px;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            transition: all 0.2s ease;
        }}
        .btn-enel:hover {{
            background: #b50058;
            color: #ffffff;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(217,0,108,0.25);
        }}
        footer {{
            background: #ffffff;
            border-top: 1px solid #e2e8f0;
            padding: 30px 20px;
            font-size: 13px;
            color: #64748b;
        }}
        .footer-content {{
            max-width: 1140px;
            margin: 0 auto;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
        }}
        .footer-links a {{
            color: #64748b;
            margin-right: 18px;
            text-decoration: none;
        }}
        .footer-links a:hover {{
            color: #d9006c;
        }}
        .footer-super img {{
            height: 32px;
            margin-left: 12px;
        }}
    </style>
</head>
<body>
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-52FXRWD" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    
    <header class="header-logo">
        <div class="container d-flex justify-content-between align-items-center">
            <a href="https://www.enel.com.co/es.html">
                <img src="https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/logo-enel.png" alt="Enel Colombia">
            </a>
            <span class="badge badge-light p-2" style="font-size:12px; border:1px solid #cbd5e1;">Enel Colombia S.A. ESP</span>
        </div>
    </header>

    <main class="container">
        <div class="thank-you-box">
            <div class="check-icon">&#10003;</div>
            <h1>¡Gracias por contactarnos!</h1>
            <p>Hemos recibido exitosamente tu solicitud para <strong>{form_name}</strong>. Uno de nuestros asesores especializados se comunicará contigo a la mayor brevedad posible.</p>
            <a href="https://www.enel.com.co/es.html" class="btn-enel">Volver a Enel Colombia</a>
        </div>
    </main>

    <footer>
        <div class="footer-content">
            <div>
                <span>&copy; Enel Colombia S.A. ESP 2026. Todos los derechos reservados.</span>
            </div>
            <div class="footer-links my-2">
                <a target="_blank" href="https://www.enel.com.co/es/legales.html">Términos Legales</a>
                <a target="_blank" href="https://www.enel.com.co/content/dam/enel-co/espa%C3%B1ol/ayuda/politica-de-tratamiento-de-datos-personales-de-enel2.pdf">Política de Privacidad</a>
                <a target="_blank" href="https://www.enel.com.co/es/politica-de-cookies.html">Política de Cookies</a>
            </div>
            <div class="footer-super d-flex align-items-center">
                <span>Vigilado:</span>
                <img src="https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/logo_vigilado-3.png" alt="Vigilado Superintendencia Financiera de Colombia">
            </div>
        </div>
    </footer>
</body>
</html>
"""

# Standard Checkbox Block in HTML
STANDARDIZED_CHECKBOXES = """
                <!-- Bloque de Casillas de Cumplimiento Legal (Habeas Data y Superfinanciera) -->
                <div class="terms col-xs-12 col-sm-12 col-md-12 col-lg-12 mb-3">
                    <input tabindex="3" type="checkbox" name="privacy" id="privacy"
                        ng-model="saleforce.privacy"
                        autocomplete="off"
                        required>
                    <label for="privacy" class="check">
                        He leído y acepto la <a href="https://www.enel.com.co/content/dam/enel-co/espa%C3%B1ol/ayuda/politica-de-tratamiento-de-datos-personales-de-enel2.pdf" target="_blank">Política de Privacidad*</a>
                    </label>
                </div>

                <div class="terms col-xs-12 col-sm-12 col-md-12 col-lg-12 mb-3">
                    <input tabindex="4" type="checkbox" name="marketing" id="marketing"
                        ng-model="saleforce.marketing"
                        autocomplete="off"
                        value="1">
                    <label for="marketing" class="check">
                        Doy mi consentimiento para el <a href="https://www.enel.com.co/es/consentimiento-para-actividades-de-marketing" target="_blank">tratamiento de datos con fines de marketing</a>
                    </label>
                </div>

                <div class="terms col-xs-12 col-sm-12 col-md-12 col-lg-12 mb-3">
                    <input tabindex="5" type="checkbox" name="terceros" id="terceros"
                        ng-model="saleforce.terceros"
                        autocomplete="off"
                        value="1">
                    <label for="terceros" class="check">
                        Doy mi consentimiento a Enel y <a href="https://www.enel.com.co/es/consentimiento-a-codensa-y-a-los-terceros-autorizados-por-ella-p" target="_blank">a los terceros autorizados por ellos</a>
                    </label>
                </div>

                <div class="terms col-xs-12 col-sm-12 col-md-12 col-lg-12 mb-3">
                    <input tabindex="6" type="checkbox" name="perfiles" id="perfiles"
                        ng-model="saleforce.perfiles"
                        autocomplete="off"
                        value="1">
                    <label for="perfiles" class="check">
                        Doy mi consentimiento para las operaciones de <a href="https://www.enel.com.co/es/elaboracion-de-perfiles" target="_blank">elaboración de perfiles</a>
                    </label>
                </div>
"""

# Standard Footer Block in HTML
STANDARDIZED_FOOTER = """
<!-- Pie de Página Institucional Estandarizado Enel Colombia -->
<footer class="enel-footer-standard mt-5 pt-4 pb-4 bg-white border-top">
  <div class="container">
    <div class="row align-items-center">
      <div class="col-xs-12 col-sm-12 col-md-8">
        <div class="d-flex flex-wrap align-items-center mb-2">
          <span class="mr-3 font-weight-bold text-dark">Enel Colombia S.A. ESP 2026</span>
          <img src="https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/logo_vigilado-3.png" width="160" alt="Vigilado Superintendencia Financiera de Colombia" class="mr-3">
        </div>
        <div class="footer-legal-links mt-2">
          <a target="_blank" href="https://www.enel.com.co/es/legales.html" class="text-secondary mr-3">Términos Legales</a>
          <a target="_blank" href="https://www.enel.com.co/content/dam/enel-co/espa%C3%B1ol/ayuda/politica-de-tratamiento-de-datos-personales-de-enel2.pdf" class="text-secondary mr-3">Política de Privacidad</a>
          <a target="_blank" href="https://www.enel.com.co/es/politica-de-cookies.html" class="text-secondary mr-3">Política de Cookies</a>
        </div>
      </div>
      <div class="col-xs-12 col-sm-12 col-md-4 text-md-right mt-3 mt-md-0">
        <span class="d-block text-muted small mb-2">Síguenos en nuestras redes oficiales:</span>
        <a target="_blank" href="https://www.facebook.com/EnelColombia" class="mr-2"><img src="https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/icono-facebook.png" width="24" alt="Facebook"></a>
        <a target="_blank" href="https://www.instagram.com/enelcolombia/?hl=es" class="mr-2"><img src="https://assets.enelcol.com.co/2025/julio/iconos-formulario-cfc/instagram.png" width="24" alt="Instagram"></a>
        <a target="_blank" href="https://twitter.com/EnelColombia" class="mr-2"><img src="https://assets.enelcol.com.co/2025/julio/iconos-formulario-cfc/x.png" width="24" alt="Twitter/X"></a>
        <a target="_blank" href="https://www.linkedin.com/company/enel-colombia/"><img src="https://assets.enelcol.com.co/2021/landings/20210211_Landing_cfc/images/icono-linkedin.png" width="24" alt="LinkedIn"></a>
      </div>
    </div>
  </div>
</footer>
"""
