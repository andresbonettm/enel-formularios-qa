import os
import sys
import re
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from template_utils import build_thank_you_html, STANDARDIZED_CHECKBOXES, STANDARDIZED_FOOTER

# Define all 18 forms with metadata
FORMS = [
    {
        'id': 1,
        'slug': 'leads-cfc',
        'name': 'Crédito Fácil Codensa - Solicitud de Crédito',
        'raw_file': 'Enel_google/formularios_raw/01_leads-cfc.html',
        'url': 'https://enelsud.info-enel.com/leads-cfc-mayo-2022'
    },
    {
        'id': 2,
        'slug': 'factura-virtual',
        'name': 'Suscripción Factura Virtual Enel',
        'raw_file': 'Enel_google/formularios_raw/02_factura-virtual.html',
        'url': 'https://enelsud.info-enel.com/FacturaVirtual_Enel_Web'
    },
    {
        'id': 3,
        'slug': 'cultura-legalidad',
        'name': 'Cultura de Legalidad y Denuncia de Conexiones Irregulares',
        'raw_file': 'Enel_google/formularios_raw/03_cultura-legalidad.html',
        'url': 'https://enelsud.info-enel.com/formulario-cultura-legalidad'
    },
    {
        'id': 4,
        'slug': 'reporte-anonimo',
        'name': 'Reporte Anónimo y Denuncia Segura',
        'raw_file': 'Enel_google/formularios_raw/04_reporte-anonimo.html',
        'url': 'https://enelsud.info-enel.com/enel-reporte-anonimo'
    },
    {
        'id': 5,
        'slug': 'energy-management',
        'name': 'Energy Management y Eficiencia Energética Empresas',
        'raw_file': 'Enel_google/formularios_raw/05_energy-management.html',
        'url': 'https://enelsud.info-enel.com/Formulario-Energy-Management'
    },
    {
        'id': 6,
        'slug': 'pago-virtual-empresas',
        'name': 'Pago Virtual y Canales Digitales Empresas',
        'raw_file': 'Enel_google/formularios_raw/06_pago-virtual-empresas.html',
        'url': 'https://enelsud.info-enel.com/PagoVirtEmpresas'
    },
    {
        'id': 7,
        'slug': 'suscripcion-factura-digital',
        'name': 'Suscripción Digital a Factura Electrónica',
        'raw_file': 'Enel_google/formularios_raw/07_suscripcion-factura-digital.html',
        'url': 'https://enelsud.info-enel.com/SFacturaDigital'
    },
    {
        'id': 8,
        'slug': 'factura-corporativa',
        'name': 'Facturación Electrónica Corporativa Enel',
        'raw_file': 'Enel_google/formularios_raw/08_factura-corporativa.html',
        'url': 'https://enelsud.info-enel.com/EFacturaCorp'
    },
    {
        'id': 9,
        'slug': 'copropiedades',
        'name': 'Exoneración y Beneficio Tributario Copropiedades',
        'raw_file': None, # Was 404, will be generated using standard Enel template
        'url': 'https://enelsud.info-enel.com/Copropiedades'
    },
    {
        'id': 10,
        'slug': 'factura-digital',
        'name': 'Registro y Consulta de Factura Digital',
        'raw_file': 'Enel_google/formularios_raw/10_factura-digital.html',
        'url': 'https://enelsud.info-enel.com/FacturaDigital'
    },
    {
        'id': 11,
        'slug': 'retiro-factura-virtual',
        'name': 'Retiro o Modificación de Factura Virtual',
        'raw_file': 'Enel_google/formularios_raw/11_retiro-factura-virtual.html',
        'url': 'https://enelsud.info-enel.com/RetiroEfacturaV'
    },
    {
        'id': 12,
        'slug': 'adecuaciones-electricas',
        'name': 'Adecuaciones Eléctricas y Obras Enel X',
        'raw_file': 'docs/enel-formulario-adecuaciones-electricas/formulario-adecuaciones-electricas.html',
        'url': 'https://cloud.customer.enelx.com/leads-obras-org'
    },
    {
        'id': 13,
        'slug': 'contacto-empresas',
        'name': 'Contacto Soluciones Empresas Enel X',
        'raw_file': 'Enel_google/formularios_raw/13_contacto-empresas.html',
        'url': 'https://cloud.customer.enelx.com/contacto-empresas-2026'
    },
    {
        'id': 14,
        'slug': 'contacto-ciudades',
        'name': 'Contacto Ciudades Inteligentes e Iluminación Enel X',
        'raw_file': 'Enel_google/formularios_raw/14_contacto-ciudades.html',
        'url': 'https://cloud.customer.enelx.com/contacto-ciudades-2026'
    },
    {
        'id': 15,
        'slug': 'mercado-no-regulado',
        'name': 'Clientes Mercado No Regulado - Asesoría Energética',
        'raw_file': 'Enel_google/formularios_raw/15_mercado-no-regulado.html',
        'url': 'https://cloud.customer.enelx.com/contacto-mr-no-regulado-2026'
    },
    {
        'id': 16,
        'slug': 'cargadores-juicebox',
        'name': 'Movilidad Eléctrica y Cargadores JuiceBox',
        'raw_file': 'Enel_google/formularios_raw/16_cargadores-juicebox.html',
        'url': 'https://cloud.customer.enelx.com/leads-juicebox-2026'
    },
    {
        'id': 17,
        'slug': 'asistencias-portafolio',
        'name': 'Asistencias y Portafolio de Protección Integral',
        'raw_file': 'Enel_google/formularios_raw/17_asistencias-portafolio.html',
        'url': 'https://cloud.customer.enelx.com/leads-asistencias-organico-portafolio'
    },
    {
        'id': 18,
        'slug': 'leads-mr-no-regulado',
        'name': 'Mercado No Regulado Grandes Clientes',
        'raw_file': 'Enel_google/formularios_raw/18_leads-mr-no-regulado.html',
        'url': 'https://cloud.customer.enelx.com/contacto-mr-no-regulado-2026'
    }
]

BASE_OUT_DIR = 'Enel_google/formularios'
os.makedirs(BASE_OUT_DIR, exist_ok=True)

# Read reference template from adecuaciones-electricas for clean base
with open('docs/enel-formulario-adecuaciones-electricas/formulario-adecuaciones-electricas.html', 'r', encoding='utf-8') as f:
    REF_HTML = f.read()

def process_and_save_form(form):
    slug = form['slug']
    name = form['name']
    form_id = form['id']
    raw_path = form['raw_file']
    
    folder_name = f"enel-formulario-{slug}"
    folder_path = os.path.join(BASE_OUT_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    html_file = os.path.join(folder_path, f"formulario-{slug}.html")
    txt_file = os.path.join(folder_path, f"formulario-{slug}.txt")
    thank_html_file = os.path.join(folder_path, f"thank-you-{slug}.html")
    thank_txt_file = os.path.join(folder_path, f"thank-you-{slug}.txt")
    
    # 1. Prepare Form HTML
    content = ""
    if raw_path and os.path.exists(raw_path):
        with open(raw_path, 'r', encoding='utf-8') as rf:
            content = rf.read()
    else:
        # Generate based on reference template
        content = REF_HTML
    
    # Ensure title is updated
    content = re.sub(r'<title>[^<]*</title>', f'<title>Contáctanos | {name} - Enel Colombia</title>', content, flags=re.IGNORECASE)
    
    # Normalize thank you redirection in JS
    content = re.sub(r'location\.href\s*=\s*["\'][^"\']*thank-you[^"\']*["\']', f'location.href = "thank-you-{slug}.html"', content, flags=re.IGNORECASE)
    
    # Ensure footer has Superfinanciera and Enel Colombia S.A ESP
    if 'logo_vigilado-3.png' not in content and 'superintendencia' not in content.lower():
        if '</form>' in content:
            # Append standard logo and footer if missing
            if 'enel-footer-standard' not in content:
                content = content.replace('</body>', f'{STANDARDIZED_FOOTER}\n</body>')
    elif 'Enel Colombia S.A ESP' not in content and 'Enel Colombia S.A. ESP' not in content:
        content = content.replace('ENEL S.A 2018', 'Enel Colombia S.A. ESP 2026')
        content = content.replace('Enel Colombia', 'Enel Colombia S.A. ESP 2026')
    
    # Ensure the 4 legal checkboxes exist
    if 'name="privacy"' not in content and 'id="privacy"' not in content:
        # Inject before submit button
        submit_match = re.search(r'(<input[^>]+type=[\'"]submit[\'"][^>]*>|<button[^>]+type=[\'"]submit[\'"][^>]*>)', content, re.I)
        if submit_match:
            pos = submit_match.start()
            content = content[:pos] + STANDARDIZED_CHECKBOXES + content[pos:]
    else:
        # Check if marketing, terceros, perfiles exist
        if 'name="marketing"' not in content or 'name="terceros"' not in content:
            # We add the missing commercial checkboxes
            extra_cb = """
                <!-- Casillas de Aceptación Comercial Independientes -->
                <div class="terms col-xs-12 col-sm-12 col-md-12 col-lg-12 mb-2">
                    <input tabindex="4" type="checkbox" name="marketing" id="marketing" ng-model="saleforce.marketing" value="1">
                    <label for="marketing" class="check">Doy mi consentimiento para el <a href="https://www.enel.com.co/es/consentimiento-para-actividades-de-marketing" target="_blank">tratamiento de datos con fines de marketing</a></label>
                </div>
                <div class="terms col-xs-12 col-sm-12 col-md-12 col-lg-12 mb-2">
                    <input tabindex="5" type="checkbox" name="terceros" id="terceros" ng-model="saleforce.terceros" value="1">
                    <label for="terceros" class="check">Doy mi consentimiento a Enel y <a href="https://www.enel.com.co/es/consentimiento-a-codensa-y-a-los-terceros-autorizados-por-ella-p" target="_blank">a terceros autorizados</a></label>
                </div>
                <div class="terms col-xs-12 col-sm-12 col-md-12 col-lg-12 mb-2">
                    <input tabindex="6" type="checkbox" name="perfiles" id="perfiles" ng-model="saleforce.perfiles" value="1">
                    <label for="perfiles" class="check">Doy mi consentimiento para <a href="https://www.enel.com.co/es/elaboracion-de-perfiles" target="_blank">elaboración de perfiles</a></label>
                </div>
            """
            submit_match = re.search(r'(<input[^>]+type=[\'"]submit[\'"][^>]*>|<button[^>]+type=[\'"]submit[\'"][^>]*>)', content, re.I)
            if submit_match:
                pos = submit_match.start()
                content = content[:pos] + extra_cb + content[pos:]
    
    # Replace cdnsafbapps or insecure http if any
    content = content.replace('http://enelsud.info-enel.com', 'https://enelsud.info-enel.com')
    content = content.replace('cdnsafbapps.com', 'enel.com.co')
    
    # Save Form HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Save Form TXT
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # 2. Build Thank You HTML
    thank_html = build_thank_you_html(f"Gracias | {name}", name, slug)
    with open(thank_html_file, 'w', encoding='utf-8') as f:
        f.write(thank_html)
        
    # Save Thank You TXT
    with open(thank_txt_file, 'w', encoding='utf-8') as f:
        f.write(thank_html)
        
    print(f"[{form_id:02d}] {slug} -> Creado paquete en: {folder_path} (4 archivos)", flush=True)

for form in FORMS:
    process_and_save_form(form)

# Create symlink or root copy of formularios
root_form_dir = 'formularios'
if os.path.exists(root_form_dir):
    if os.path.islink(root_form_dir):
        os.unlink(root_form_dir)
    else:
        shutil.rmtree(root_form_dir)

try:
    os.symlink('Enel_google/formularios', root_form_dir)
    print("Symlink 'formularios' creado exitosamente.", flush=True)
except Exception as e:
    shutil.copytree('Enel_google/formularios', root_form_dir)
    print("Copia 'formularios' creada exitosamente.", flush=True)
