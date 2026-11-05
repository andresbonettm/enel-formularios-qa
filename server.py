#!/usr/bin/env python3
"""
Servidor Local de Pruebas de Formularios — Enel Colombia
Monta todos los 18 formularios en localhost con landing interactiva y simulación de backend.
"""

import http.server
import socketserver
import urllib.parse
import json
import os
import sys
import datetime

PORT = 8090
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FORMULARIOS_DIR = os.path.join(BASE_DIR, "formularios")

from batch2_metadata import BATCH2_METADATA

FORMULARIOS_NUEVOS_DIR = os.path.join(BASE_DIR, "formularios_nuevos")


# In-memory storage for test leads
TEST_LEADS = []

FORMS_METADATA = [
    {
        "id": 1,
        "slug": "leads-cfc",
        "name": "Crédito Fácil Codensa - Solicitud de Crédito",
        "category": "Personas / Hogar",
        "domain": "info-enel.com",
        "folder": "enel-formulario-leads-cfc",
        "file_html": "formulario-leads-cfc.html",
        "file_txt": "formulario-leads-cfc.txt",
        "thank_you": "thank-you-leads-cfc.html",
        "live_url": "https://enelsud.info-enel.com/leads-cfc-mayo-2022"
    },
    {
        "id": 2,
        "slug": "factura-virtual",
        "name": "Suscripción Factura Virtual Enel",
        "category": "Facturación y Pagos",
        "domain": "info-enel.com",
        "folder": "enel-formulario-factura-virtual",
        "file_html": "formulario-factura-virtual.html",
        "file_txt": "formulario-factura-virtual.txt",
        "thank_you": "thank-you-factura-virtual.html",
        "live_url": "https://enelsud.info-enel.com/FacturaVirtual_Enel_Web"
    },
    {
        "id": 3,
        "slug": "cultura-legalidad",
        "name": "Cultura de Legalidad y Denuncia Conexiones",
        "category": "Seguridad y Legal",
        "domain": "info-enel.com",
        "folder": "enel-formulario-cultura-legalidad",
        "file_html": "formulario-cultura-legalidad.html",
        "file_txt": "formulario-cultura-legalidad.txt",
        "thank_you": "thank-you-cultura-legalidad.html",
        "live_url": "https://enelsud.info-enel.com/formulario-cultura-legalidad"
    },
    {
        "id": 4,
        "slug": "reporte-anonimo",
        "name": "Reporte Anónimo y Denuncia Segura",
        "category": "Seguridad y Legal",
        "domain": "info-enel.com",
        "folder": "enel-formulario-reporte-anonimo",
        "file_html": "formulario-reporte-anonimo.html",
        "file_txt": "formulario-reporte-anonimo.txt",
        "thank_you": "thank-you-reporte-anonimo.html",
        "live_url": "https://enelsud.info-enel.com/enel-reporte-anonimo"
    },
    {
        "id": 5,
        "slug": "energy-management",
        "name": "Energy Management y Eficiencia Empresas",
        "category": "Empresas",
        "domain": "info-enel.com",
        "folder": "enel-formulario-energy-management",
        "file_html": "formulario-energy-management.html",
        "file_txt": "formulario-energy-management.txt",
        "thank_you": "thank-you-energy-management.html",
        "live_url": "https://enelsud.info-enel.com/Formulario-Energy-Management"
    },
    {
        "id": 6,
        "slug": "pago-virtual-empresas",
        "name": "Pago Virtual y Canales Empresas",
        "category": "Facturación y Pagos",
        "domain": "info-enel.com",
        "folder": "enel-formulario-pago-virtual-empresas",
        "file_html": "formulario-pago-virtual-empresas.html",
        "file_txt": "formulario-pago-virtual-empresas.txt",
        "thank_you": "thank-you-pago-virtual-empresas.html",
        "live_url": "https://enelsud.info-enel.com/PagoVirtEmpresas"
    },
    {
        "id": 7,
        "slug": "suscripcion-factura-digital",
        "name": "Suscripción a Factura Digital",
        "category": "Facturación y Pagos",
        "domain": "info-enel.com",
        "folder": "enel-formulario-suscripcion-factura-digital",
        "file_html": "formulario-suscripcion-factura-digital.html",
        "file_txt": "formulario-suscripcion-factura-digital.txt",
        "thank_you": "thank-you-suscripcion-factura-digital.html",
        "live_url": "https://enelsud.info-enel.com/SFacturaDigital"
    },
    {
        "id": 8,
        "slug": "factura-corporativa",
        "name": "Facturación Electrónica Corporativa",
        "category": "Empresas",
        "domain": "info-enel.com",
        "folder": "enel-formulario-factura-corporativa",
        "file_html": "formulario-factura-corporativa.html",
        "file_txt": "formulario-factura-corporativa.txt",
        "thank_you": "thank-you-factura-corporativa.html",
        "live_url": "https://enelsud.info-enel.com/EFacturaCorp"
    },
    {
        "id": 9,
        "slug": "copropiedades",
        "name": "Exoneración Tributaria Copropiedades",
        "category": "Legal y Regulatorio",
        "domain": "info-enel.com",
        "folder": "enel-formulario-copropiedades",
        "file_html": "formulario-copropiedades.html",
        "file_txt": "formulario-copropiedades.txt",
        "thank_you": "thank-you-copropiedades.html",
        "live_url": "http://enelsud.info-enel.com/Copropiedades"
    },
    {
        "id": 10,
        "slug": "factura-digital",
        "name": "Registro y Consulta Factura Digital",
        "category": "Facturación y Pagos",
        "domain": "info-enel.com",
        "folder": "enel-formulario-factura-digital",
        "file_html": "formulario-factura-digital.html",
        "file_txt": "formulario-factura-digital.txt",
        "thank_you": "thank-you-factura-digital.html",
        "live_url": "http://enelsud.info-enel.com/FacturaDigital"
    },
    {
        "id": 11,
        "slug": "retiro-factura-virtual",
        "name": "Retiro o Modificación Factura Virtual",
        "category": "Facturación y Pagos",
        "domain": "info-enel.com",
        "folder": "enel-formulario-retiro-factura-virtual",
        "file_html": "formulario-retiro-factura-virtual.html",
        "file_txt": "formulario-retiro-factura-virtual.txt",
        "thank_you": "thank-you-retiro-factura-virtual.html",
        "live_url": "http://enelsud.info-enel.com/RetiroEfactura"
    },
    {
        "id": 12,
        "slug": "adecuaciones-electricas",
        "name": "Adecuaciones Eléctricas y Obras Enel X",
        "category": "Enel X Soluciones",
        "domain": "customer.enelx.com",
        "folder": "enel-formulario-adecuaciones-electricas",
        "file_html": "formulario-adecuaciones-electricas.html",
        "file_txt": "formulario-adecuaciones-electricas.txt",
        "thank_you": "thank-you-adecuaciones-electricas.html",
        "live_url": "https://cloud.customer.enelx.com/leads-obras-org"
    },
    {
        "id": 13,
        "slug": "contacto-empresas",
        "name": "Contacto Soluciones Empresas Enel X",
        "category": "Enel X Soluciones",
        "domain": "customer.enelx.com",
        "folder": "enel-formulario-contacto-empresas",
        "file_html": "formulario-contacto-empresas.html",
        "file_txt": "formulario-contacto-empresas.txt",
        "thank_you": "thank-you-contacto-empresas.html",
        "live_url": "https://cloud.customer.enelx.com/contacto-empresas-2026"
    },
    {
        "id": 14,
        "slug": "contacto-ciudades",
        "name": "Ciudades Inteligentes e Iluminación",
        "category": "Enel X Soluciones",
        "domain": "customer.enelx.com",
        "folder": "enel-formulario-contacto-ciudades",
        "file_html": "formulario-contacto-ciudades.html",
        "file_txt": "formulario-contacto-ciudades.txt",
        "thank_you": "thank-you-contacto-ciudades.html",
        "live_url": "https://cloud.customer.enelx.com/contacto-ciudades-2026"
    },
    {
        "id": 15,
        "slug": "mercado-no-regulado",
        "name": "Asesoría Mercado No Regulado",
        "category": "Empresas",
        "domain": "customer.enelx.com",
        "folder": "enel-formulario-mercado-no-regulado",
        "file_html": "formulario-mercado-no-regulado.html",
        "file_txt": "formulario-mercado-no-regulado.txt",
        "thank_you": "thank-you-mercado-no-regulado.html",
        "live_url": "https://cloud.customer.enelx.com/contacto-mr-no-regulado-2026"
    },
    {
        "id": 16,
        "slug": "cargadores-juicebox",
        "name": "Movilidad Eléctrica y Cargadores JuiceBox",
        "category": "Enel X Soluciones",
        "domain": "customer.enelx.com",
        "folder": "enel-formulario-cargadores-juicebox",
        "file_html": "formulario-cargadores-juicebox.html",
        "file_txt": "formulario-cargadores-juicebox.txt",
        "thank_you": "thank-you-cargadores-juicebox.html",
        "live_url": "https://cloud.customer.enelx.com/leads-juicebox-2026"
    },
    {
        "id": 17,
        "slug": "asistencias-portafolio",
        "name": "Asistencias y Portafolio de Protección",
        "category": "Personas / Hogar",
        "domain": "customer.enelx.com",
        "folder": "enel-formulario-asistencias-portafolio",
        "file_html": "formulario-asistencias-portafolio.html",
        "file_txt": "formulario-asistencias-portafolio.txt",
        "thank_you": "thank-you-asistencias-portafolio.html",
        "live_url": "https://cloud.customer.enelx.com/leads-asistencias-organico-portafolio"
    },
    {
        "id": 18,
        "slug": "leads-mr-no-regulado",
        "name": "Mercado No Regulado Grandes Cuentas",
        "category": "Empresas",
        "domain": "customer.enelx.com",
        "folder": "enel-formulario-leads-mr-no-regulado",
        "file_html": "formulario-leads-mr-no-regulado.html",
        "file_txt": "formulario-leads-mr-no-regulado.txt",
        "thank_you": "thank-you-leads-mr-no-regulado.html",
        "live_url": "https://cloud.customer.enelx.com/leads-mr-no-regulado-2026"
    }
]

LANDING_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enel Colombia — Suite de Pruebas de Formularios en Localhost</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">
    <style>
        :root {
            --enel-magenta: #d9006c;
            --enel-dark: #121926;
            --enel-card-bg: #ffffff;
            --enel-border: #e2e8f0;
            --enel-text: #1e293b;
            --enel-muted: #64748b;
        }
        body {
            background-color: #f8fafc;
            color: var(--enel-text);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            padding-bottom: 60px;
        }
        .header-hero {
            background: linear-gradient(135deg, #121926 0%, #1e293b 100%);
            color: #ffffff;
            padding: 35px 0 25px 0;
            border-bottom: 4px solid var(--enel-magenta);
            margin-bottom: 30px;
        }
        .brand-pill {
            background: rgba(217, 0, 108, 0.2);
            border: 1px solid var(--enel-magenta);
            color: #ff70b3;
            font-size: 12px;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: inline-block;
            margin-bottom: 10px;
        }
        .stat-card {
            background: #ffffff;
            border-radius: 10px;
            border: 1px solid var(--enel-border);
            padding: 18px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            text-align: center;
        }
        .stat-card .val {
            font-size: 28px;
            font-weight: 800;
            color: var(--enel-magenta);
        }
        .stat-card .lbl {
            font-size: 13px;
            font-weight: 600;
            color: var(--enel-muted);
            text-transform: uppercase;
        }
        .form-card {
            background: #ffffff;
            border: 1px solid var(--enel-border);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.2s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .form-card:hover {
            border-color: var(--enel-magenta);
            transform: translateY(-2px);
            box-shadow: 0 8px 18px rgba(217,0,108,0.08);
        }
        .badge-domain {
            background: #e2e8f0;
            color: #334155;
            font-size: 11px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: 4px;
        }
        .badge-cat {
            background: #fdf2f8;
            color: #be185d;
            border: 1px solid #fbcfe8;
            font-size: 11px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: 4px;
        }
        .btn-open-form {
            background: var(--enel-magenta);
            color: #ffffff;
            font-weight: 600;
            font-size: 13px;
            border-radius: 6px;
            border: none;
            padding: 8px 16px;
            transition: background 0.2s;
        }
        .btn-open-form:hover {
            background: #b50058;
            color: #ffffff;
            text-decoration: none;
        }
        .btn-secondary-link {
            font-size: 12px;
            font-weight: 600;
            color: var(--enel-muted);
            text-decoration: none;
            padding: 4px 8px;
            border: 1px solid var(--enel-border);
            border-radius: 4px;
            background: #ffffff;
        }
        .btn-secondary-link:hover {
            color: var(--enel-text);
            border-color: #94a3b8;
            text-decoration: none;
        }
        .search-input {
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            padding: 12px 18px;
            font-size: 14px;
            width: 100%;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        .search-input:focus {
            border-color: var(--enel-magenta);
            outline: none;
            box-shadow: 0 0 0 3px rgba(217,0,108,0.15);
        }
        .filter-btn {
            font-size: 12px;
            font-weight: 600;
            border-radius: 20px;
            padding: 6px 14px;
            margin-right: 6px;
            margin-bottom: 6px;
            border: 1px solid var(--enel-border);
            background: #ffffff;
            color: var(--enel-muted);
            cursor: pointer;
        }
        .filter-btn.active, .filter-btn:hover {
            background: var(--enel-magenta);
            color: #ffffff;
            border-color: var(--enel-magenta);
        }
        .lead-logger {
            background: #0f172a;
            color: #38bdf8;
            padding: 15px;
            border-radius: 8px;
            font-family: monospace;
            font-size: 12px;
            max-height: 180px;
            overflow-y: auto;
        }
    </style>
</head>
<body>

<header class="header-hero">
    <div class="container">
        <div class="d-flex justify-content-between align-items-center flex-wrap">
            <div>
                <span class="brand-pill">Servidor de Pruebas Local • Puerto 8090</span>
                <h1 class="h3 font-weight-bold mb-1">Enel Colombia — Suite de Formularios</h1>
                <p class="text-light mb-0" style="opacity: 0.85;">Ambiente local interactivo para prueba de 18 formularios, validación de casillas y confirmaciones.</p>
            </div>
            <div class="mt-3 mt-md-0">
                <a href="#leadsSection" class="btn btn-outline-light btn-sm font-weight-bold mr-2">Ver Envíos de Prueba</a>
                <span class="badge badge-success px-3 py-2" style="font-size: 13px;">● Servidor Activo</span>
            </div>
        </div>
    </div>
</header>

<main class="container">
    <!-- Métricas -->
    <div class="row mb-4">
        <div class="col-6 col-md-3 mb-3">
            <div class="stat-card">
                <div class="val">18</div>
                <div class="lbl">Formularios Listos</div>
            </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
            <div class="stat-card">
                <div class="val">4</div>
                <div class="lbl">Casillas Legales (SIC)</div>
            </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
            <div class="stat-card">
                <div class="val">100%</div>
                <div class="lbl">Sello Superfinanciera</div>
            </div>
        </div>
        <div class="col-6 col-md-3 mb-3">
            <div class="stat-card">
                <div class="val">72</div>
                <div class="lbl">Archivos (.html / .txt)</div>
            </div>
        </div>
    </div>

    <!-- Buscador y Filtros -->
    <div class="card p-3 mb-4 border-0 shadow-sm">
        <div class="row align-items-center">
            <div class="col-md-6 mb-2 mb-md-0">
                <input type="text" id="searchInput" class="search-input" placeholder="Buscar formulario por nombre, slug o categoría...">
            </div>
            <div class="col-md-6 text-md-right" id="filterContainer">
                <button class="filter-btn active" onclick="filterCategory('all')">Todos (18)</button>
                <button class="filter-btn" onclick="filterCategory('Personas / Hogar')">Hogar</button>
                <button class="filter-btn" onclick="filterCategory('Empresas')">Empresas</button>
                <button class="filter-btn" onclick="filterCategory('Enel X Soluciones')">Enel X</button>
                <button class="filter-btn" onclick="filterCategory('Facturación y Pagos')">Facturación</button>
            </div>
        </div>
    </div>

    <!-- Grid de Formularios -->
    <div class="row" id="formsGrid">
        <!-- Renderizado dinámico vía JS -->
    </div>

    <!-- Sección de Envíos de Prueba Recibidos -->
    <div class="card p-4 mt-4 shadow-sm border-0" id="leadsSection">
        <div class="d-flex justify-content-between align-items-center mb-3">
            <div>
                <h5 class="font-weight-bold mb-1">Terminal de Envíos de Prueba Locales (Simulador CRM)</h5>
                <p class="text-muted small mb-0">Cada vez que envías un formulario de prueba, el payload capturado se registra en este panel.</p>
            </div>
            <button class="btn btn-outline-secondary btn-sm" onclick="fetchLeads()">Actualizar Envíos</button>
        </div>
        <div class="lead-logger" id="leadsLog">
            [Servidor Listo] Esperando envíos de prueba desde cualquiera de los 18 formularios...
        </div>
    </div>
</main>

<script>
const FORMS_DATA = __FORMS_JSON__;

function renderForms(items) {
    const grid = document.getElementById('formsGrid');
    grid.innerHTML = '';
    
    if (items.length === 0) {
        grid.innerHTML = '<div class="col-12 text-center py-5 text-muted">No se encontraron formularios con ese criterio.</div>';
        return;
    }

    items.forEach(f => {
        const col = document.createElement('div');
        col.className = 'col-md-6 col-lg-4 mb-4';
        
        const formUrl = `/formularios/${f.folder}/${f.file_html}`;
        const txtUrl = `/formularios/${f.folder}/${f.file_txt}`;
        const tyUrl = `/formularios/${f.folder}/${f.thank_you}`;
        
        col.innerHTML = `
            <div class="form-card">
                <div>
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <span class="badge-cat">${f.category}</span>
                        <span class="badge-domain">${f.domain}</span>
                    </div>
                    <h5 class="h6 font-weight-bold text-dark mb-1" style="min-height: 40px;">
                        #${f.id < 10 ? '0' + f.id : f.id}. ${f.name}
                    </h5>
                    <p class="text-muted small mb-3">Slug: <code>${f.slug}</code></p>
                </div>
                <div>
                    <div class="mb-2">
                        <a href="${formUrl}" target="_blank" class="btn-open-form btn-block text-center font-weight-bold">
                            Probar Formulario Local &rarr;
                        </a>
                    </div>
                    <div class="mb-3">
                        <a href="${f.live_url}" target="_blank" class="btn btn-sm btn-block text-dark font-weight-bold" style="background:#fff3cd; border: 1px solid #ffeeba; border-radius: 8px; padding: 7px 10px; font-size: 13px;" title="Abrir versión original en producción para comparar">
                            🌐 Comparar con Formulario Real en Vivo ↗
                        </a>
                    </div>
                    <div class="d-flex justify-content-between pt-2 border-top">
                        <a href="${txtUrl}" target="_blank" class="btn-secondary-link" title="Ver código en formato TXT">
                            📄 Código .txt
                        </a>
                        <a href="${tyUrl}" target="_blank" class="btn-secondary-link text-info" title="Ver página de agradecimiento">
                            🎉 Thank You Page
                        </a>
                    </div>
                </div>
            </div>
        `;
        grid.appendChild(col);
    });
}

function filterCategory(cat) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');
    
    if (cat === 'all') {
        renderForms(FORMS_DATA);
    } else {
        const filtered = FORMS_DATA.filter(f => f.category === cat);
        renderForms(filtered);
    }
}

document.getElementById('searchInput').addEventListener('input', function(e) {
    const q = e.target.value.toLowerCase().trim();
    const filtered = FORMS_DATA.filter(f => 
        f.name.toLowerCase().includes(q) || 
        f.slug.toLowerCase().includes(q) || 
        f.category.toLowerCase().includes(q) ||
        f.domain.toLowerCase().includes(q)
    );
    renderForms(filtered);
});

function fetchLeads() {
    fetch('/api/leads')
        .then(r => r.json())
        .then(data => {
            const el = document.getElementById('leadsLog');
            if (!data || data.length === 0) {
                el.innerText = '[Servidor Listo] No se han registrado envíos de prueba aún. Completa cualquier formulario para ver los datos aquí.';
            } else {
                el.innerHTML = data.map((l, i) => `[${l.timestamp}] Form: ${l.form_slug} | Datos: ${JSON.stringify(l.data)}`).join('<br>');
            }
        })
        .catch(err => console.error(err));
}

// Initial render
renderForms(FORMS_DATA);
fetchLeads();
setInterval(fetchLeads, 3000);
</script>
</body>
</html>
"""

LANDING_LOTE2_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enel Colombia — Lote 2: 16 Formularios y Landings Nuevas</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">
    <style>
        :root {
            --enel-magenta: #d9006c;
            --enel-dark: #121926;
            --enel-card-bg: #ffffff;
            --enel-border: #e2e8f0;
            --enel-text: #334155;
            --enel-blue: #0284c7;
            --enel-teal: #0d9488;
        }

        body {
            background-color: #f8fafc;
            color: var(--enel-text);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            min-height: 100vh;
            padding-bottom: 60px;
        }

        .header-banner {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            color: #ffffff;
            padding: 40px 0 35px 0;
            border-bottom: 4px solid var(--enel-blue);
            margin-bottom: 30px;
        }

        .header-title {
            font-weight: 800;
            letter-spacing: -0.5px;
            font-size: 1.85rem;
        }

        .header-desc {
            color: #94a3b8;
            font-size: 0.95rem;
            margin-bottom: 0;
        }

        .stat-card {
            background: #ffffff;
            border: 1px solid var(--enel-border);
            border-radius: 8px;
            padding: 16px 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .stat-number {
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--enel-blue);
        }

        .stat-label {
            font-size: 0.78rem;
            color: #64748b;
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        .form-card {
            background: var(--enel-card-bg);
            border: 1px solid var(--enel-border);
            border-radius: 10px;
            padding: 22px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.03);
            transition: all 0.2s ease-in-out;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .form-card:hover {
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.08);
            border-color: #cbd5e1;
            transform: translateY(-2px);
        }

        .form-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 6px;
        }

        .badge-type {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 4px 8px;
            border-radius: 4px;
            background-color: #e0f2fe;
            color: #0369a1;
        }

        .badge-id {
            background-color: #f1f5f9;
            color: #475569;
            font-weight: 700;
            font-size: 0.75rem;
            padding: 3px 8px;
            border-radius: 4px;
        }

        .req-box {
            background-color: #fffbeb;
            border-left: 3px solid #f59e0b;
            padding: 8px 12px;
            border-radius: 0 4px 4px 0;
            font-size: 0.82rem;
            color: #92400e;
            margin-bottom: 12px;
        }

        .rem-box {
            background-color: #f0fdf4;
            border-left: 3px solid #10b981;
            padding: 8px 12px;
            border-radius: 0 4px 4px 0;
            font-size: 0.82rem;
            color: #065f46;
            margin-bottom: 16px;
        }

        .btn-open {
            background-color: var(--enel-blue);
            color: white;
            font-weight: 600;
            border-radius: 6px;
            border: none;
            padding: 8px 14px;
            font-size: 0.88rem;
            transition: background 0.15s;
        }

        .btn-open:hover {
            background-color: #0369a1;
            color: white;
            text-decoration: none;
        }

        .btn-txt {
            background-color: #f1f5f9;
            color: #334155;
            font-weight: 600;
            border-radius: 6px;
            border: 1px solid #cbd5e1;
            padding: 8px 14px;
            font-size: 0.88rem;
        }

        .btn-txt:hover {
            background-color: #e2e8f0;
            color: #0f172a;
            text-decoration: none;
        }

        .btn-compare {
            background-color: #ffffff;
            color: #0284c7;
            font-weight: 600;
            border-radius: 6px;
            border: 1px solid #bae6fd;
            padding: 6px 12px;
            font-size: 0.82rem;
            display: inline-block;
            transition: all 0.15s ease-in-out;
            text-align: center;
        }

        .btn-compare:hover {
            background-color: #e0f2fe;
            color: #0369a1;
            text-decoration: none;
            border-color: #0284c7;
        }

        .search-box {
            border: 1px solid var(--enel-border);
            border-radius: 8px;
            padding: 10px 16px;
            font-size: 0.95rem;
            width: 100%;
            background: #ffffff;
            box-shadow: 0 1px 2px rgba(0,0,0,0.03);
        }

        .search-box:focus {
            outline: none;
            border-color: var(--enel-blue);
            box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header class="header-banner">
        <div class="container">
            <div class="d-flex align-items-center justify-content-between">
                <div>
                    <h1 class="header-title">🚀 Lote 2: 16 Formularios y Landings Nuevas</h1>
                    <p class="header-desc">Formularios no enlazados en el rastreo inicial, CloudPages de Enel X / Salesforce y Páginas AEM saneadas</p>
                </div>
                <div>
                    <span class="badge badge-info p-2 font-weight-bold" style="font-size: 0.9rem;">ENTORNO AISLADO</span>
                </div>
            </div>
        </div>
    </header>

    <div class="container">

        <!-- Top Navigation Tabs (Lote 1 vs Lote 2) -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="p-2 bg-white rounded shadow-sm d-flex flex-wrap align-items-center justify-content-between" style="border: 1px solid var(--enel-border);">
                    <div class="d-flex align-items-center">
                        <span class="mr-3 font-weight-bold text-muted small text-uppercase">Vistas Disponibles:</span>
                        <a href="/" class="btn btn-sm btn-outline-secondary mr-2 font-weight-bold">
                            📁 Lote 1: 18 Formularios Auditados
                        </a>
                        <a href="/lote2" class="btn btn-sm btn-primary font-weight-bold" style="background: var(--enel-blue); border-color: var(--enel-blue);">
                            🚀 Lote 2: 16 Formularios y Landings Nuevas (ACTIVO)
                        </a>
                    </div>
                    <div class="text-muted small mt-2 mt-md-0">
                        Carpeta local: <code class="text-primary font-weight-bold">Enel_google/formularios_nuevos/</code>
                    </div>
                </div>
            </div>
        </div>

        <!-- Metric Summary Cards -->
        <div class="row mb-4">
            <div class="col-md-3 mb-3 mb-md-0">
                <div class="stat-card">
                    <div>
                        <div class="stat-number">16</div>
                        <div class="stat-label">Items Procesados</div>
                    </div>
                    <div style="font-size: 2rem;">📦</div>
                </div>
            </div>
            <div class="col-md-3 mb-3 mb-md-0">
                <div class="stat-card">
                    <div>
                        <div class="stat-number">6</div>
                        <div class="stat-label">CloudPages Enel X / Info</div>
                    </div>
                    <div style="font-size: 2rem;">⚡</div>
                </div>
            </div>
            <div class="col-md-3 mb-3 mb-md-0">
                <div class="stat-card">
                    <div>
                        <div class="stat-number">10</div>
                        <div class="stat-label">Páginas AEM Saneadas</div>
                    </div>
                    <div style="font-size: 2rem;">🏛️</div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="stat-card">
                    <div>
                        <div class="stat-number" style="color: #10b981;">100%</div>
                        <div class="stat-label">Requisitos Cumplidos</div>
                    </div>
                    <div style="font-size: 2rem;">✅</div>
                </div>
            </div>
        </div>

        <!-- Search Bar -->
        <div class="row mb-4">
            <div class="col-12">
                <input type="text" id="searchInput" class="search-box" placeholder="🔍 Buscar por nombre, requerimiento, slug o tipo...">
            </div>
        </div>

        <!-- Grid of Forms -->
        <div class="row" id="formsGrid">
            <!-- Injected via JavaScript -->
        </div>

    </div>

    <script>
        const BATCH2_DATA = __BATCH2_JSON__;

        function renderBatch2(items) {
            const grid = document.getElementById('formsGrid');
            grid.innerHTML = '';
            
            if (items.length === 0) {
                grid.innerHTML = '<div class="col-12 text-center py-5 text-muted">No se encontraron items con ese criterio de búsqueda.</div>';
                return;
            }

            items.forEach(item => {
                const col = document.createElement('div');
                col.className = 'col-md-6 col-lg-4 mb-4';
                
                col.innerHTML = `
                    <div class="form-card">
                        <div>
                            <div class="d-flex justify-content-between align-items-center mb-2">
                                <span class="badge-type">${item.type}</span>
                                <span class="badge-id">#${String(item.id).padStart(2, '0')}</span>
                            </div>
                            <h3 class="form-title">${item.name}</h3>
                            <div class="small text-muted mb-2 font-mono"><code>${item.slug}</code></div>
                            
                            <div class="req-box">
                                <strong>📌 Requerimiento:</strong><br>
                                ${item.requirement}
                            </div>

                            <div class="rem-box">
                                <strong>🛡️ Remediación Aplicada:</strong><br>
                                ${item.remediation}
                            </div>
                        </div>

                        <div>
                            <div class="d-flex justify-content-between mb-2">
                                <a href="${item.file_html}" target="_blank" class="btn btn-open flex-grow-1 mr-2 text-center">
                                    🚀 Probar Local
                                </a>
                                <a href="${item.file_txt}" target="_blank" class="btn btn-txt text-center" title="Ver código fuente limpio para autores o CloudPages">
                                    📋 .txt
                                </a>
                            </div>
                            <a href="${item.live_url}" target="_blank" rel="noopener noreferrer" class="btn-compare w-100">
                                🌐 Comparar con URL Real en Vivo ↗
                            </a>
                        </div>
                    </div>
                `;
                grid.appendChild(col);
            });
        }

        renderBatch2(BATCH2_DATA);

        document.getElementById('searchInput').addEventListener('input', (e) => {
            const val = e.target.value.toLowerCase().trim();
            const filtered = BATCH2_DATA.filter(item => 
                item.name.toLowerCase().includes(val) ||
                item.slug.toLowerCase().includes(val) ||
                item.requirement.toLowerCase().includes(val) ||
                item.type.toLowerCase().includes(val) ||
                item.remediation.toLowerCase().includes(val)
            );
            renderBatch2(filtered);
        });
    </script>
</body>
</html>
"""


class EnelFormsHandler(http.server.SimpleHTTPRequestHandler):
    """Manejador HTTP especializado para servir la landing, los formularios y capturar envíos POST."""

    def end_headers(self):
        # Allow CORS for local testing
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = LANDING_HTML.replace("__FORMS_JSON__", json.dumps(FORMS_METADATA))
            self.wfile.write(html.encode("utf-8"))
            return

        
        if path == "/lote2" or path == "/lote2/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = LANDING_LOTE2_HTML.replace("__BATCH2_JSON__", json.dumps(BATCH2_METADATA))
            self.wfile.write(html.encode("utf-8"))
            return

        # Serve static files from formularios_nuevos directory
        if path.startswith("/formularios_nuevos/"):
            rel_path = path[len("/formularios_nuevos/"):]
            file_path = os.path.join(FORMULARIOS_NUEVOS_DIR, rel_path)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                self.send_response(200)
                if file_path.endswith(".html"):
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                elif file_path.endswith(".txt"):
                    self.send_header("Content-Type", "text/plain; charset=utf-8")
                elif file_path.endswith(".css"):
                    self.send_header("Content-Type", "text/css")
                elif file_path.endswith(".js"):
                    self.send_header("Content-Type", "application/javascript")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
                return

        if path == "/api/leads":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(TEST_LEADS).encode("utf-8"))
            return

        # Serve static assets locally
        if path.startswith("/assets/"):
            asset_file = os.path.join(BASE_DIR, "assets", os.path.basename(path))
            if os.path.exists(asset_file):
                self.send_response(200)
                if asset_file.endswith(".png"): self.send_header("Content-Type", "image/png")
                elif asset_file.endswith(".jpg"): self.send_header("Content-Type", "image/jpeg")
                elif asset_file.endswith(".svg"): self.send_header("Content-Type", "image/svg+xml")
                self.end_headers()
                with open(asset_file, "rb") as f:
                    self.wfile.write(f.read())
                return

        # Serve static files from formularios directory
        if path.startswith("/formularios/"):
            rel_path = path[len("/formularios/"):]
            file_path = os.path.join(FORMULARIOS_DIR, rel_path)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                self.send_response(200)
                if file_path.endswith(".html"):
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                elif file_path.endswith(".txt"):
                    self.send_header("Content-Type", "text/plain; charset=utf-8")
                elif file_path.endswith(".css"):
                    self.send_header("Content-Type", "text/css")
                elif file_path.endswith(".js"):
                    self.send_header("Content-Type", "application/javascript")
                self.end_headers()
                with open(file_path, "rb") as f:
                    self.wfile.write(f.read())
                return

        # Fallback to default
        super().do_GET()

    def do_POST(self):
        """Captura envíos de formularios locales simulando recepción de CRM / Marketing Cloud."""
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8", errors="ignore")
        
        parsed_data = {}
        try:
            # Try form-urlencoded first
            query = urllib.parse.parse_qs(body)
            if query:
                parsed_data = {k: v[0] if len(v) == 1 else v for k, v in query.items()}
            else:
                parsed_data = json.loads(body)
        except Exception:
            parsed_data = {"raw_payload": body}

        slug = "desconocido"
        for form in FORMS_METADATA:
            if form["slug"] in self.path or form["folder"] in self.path:
                slug = form["slug"]
                break

        lead_entry = {
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
            "form_slug": slug,
            "path": self.path,
            "data": parsed_data
        }
        TEST_LEADS.insert(0, lead_entry)
        if len(TEST_LEADS) > 50:
            TEST_LEADS.pop()

        print(f"📥 [LEAD RECIBIDO] Form: {slug} | Campos: {list(parsed_data.keys())}", flush=True)

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        response = {
            "status": "success",
            "message": "Lead registrado exitosamente en el servidor de pruebas local",
            "received_at": lead_entry["timestamp"]
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))


def run_server(port=PORT):
    # Set directory to workspace root so root paths also resolve
    os.chdir(os.path.dirname(BASE_DIR))
    handler = EnelFormsHandler
    # Allow address reuse and handle requests concurrently
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", port), handler) as httpd:
        print("\n" + "=" * 70)
        print("⚡ SERVIDOR LOCAL DE FORMULARIOS — ENEL COLOMBIA (CONCURRENTE)")
        print("=" * 70)
        print(f" 🌐 Acceso a la Landing de Pruebas:  http://localhost:{port}")
        print(f" 📁 Directorio de Formularios:       {FORMULARIOS_DIR}")
        print(" 🎯 Total de Formularios Montados:   18 Formularios")
        print(" 🛡️ Casillas Legales Integradas:     4 (Habeas Data + 3 Comerciales)")
        print(" 🏛️ Pie de Página:                  Sello Superfinanciera + Enel Colombia ESP")
        print(" 📨 Simulación de Recepción Leads:  Activa en tiempo real")
        print("=" * 70)
        print("Presiona Ctrl + C para detener el servidor.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor de formularios detenido limpiamente.")


if __name__ == "__main__":
    p = PORT
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        p = int(sys.argv[1])
    run_server(port=p)


