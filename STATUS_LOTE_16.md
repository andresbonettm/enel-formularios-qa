# Paquete de Entrega: Lote de 16 Formularios y Landings Saneadas
**Proyecto:** Normalización Legal y Auditoría Técnica SEO / DOM — Enel Colombia  
**Fecha:** 6 de Noviembre de 2026  
**Entorno de Pruebas en Vivo (Vercel):** [https://enel-formularios-qa.vercel.app/lote2](https://enel-formularios-qa.vercel.app/lote2)  
**Repositorio GitHub:** [github.com/andresbonettm/enel-formularios-qa](https://github.com/andresbonettm/enel-formularios-qa)

---

## 📁 1. Estructura del Paquete de Entrega

```
ENTREGABLE_LOTE2_16_FORMULARIOS_Y_LANDINGS/
├── README_ENTREGABLE.md                     # Este documento de especificaciones
├── STATUS_Y_MATRIZ_LOTE_16.csv             # Matriz en CSV para importar a Excel / Sheets
└── formularios_saneados/                   # 16 subcarpetas con el código listo
    ├── 01-asistencia-funeral/              # CloudPage: Footer saneado (eliminado CFC)
    ├── 02-leads-obras-org/                 # CloudPage: Footer saneado y 0 cloaking
    ├── 03-juicebox-enel/                   # AEM Landing: DOM auditado
    ├── 04-pago-medios-electronicos/        # AEM Landing: Verificada
    ├── 05-registro/                        # AEM Landing / Wizard de Registro
    ├── 06-hurto-energia-consecuencias-legales/ # AEM Landing: Botón huérfano DTM saneado
    ├── 07-eficiencia-energetica-pequenas-empresas/ # AEM Landing: Verificada
    ├── 08-fenomeno-de-el-nino/             # AEM Landing: Verificada
    ├── 09-consejos-fraudes-digitales/      # AEM Landing Editorial: Verificada
    ├── 10-personas-factura-virtual/        # AEM Landing Hub: Verificada
    ├── 11-formulario-cultura-legalidad/    # CloudPage: Footer inyectado (anónimo)
    ├── 12-leads-juicebox-2026/             # CloudPage: Footer saneado (eliminado CFC)
    ├── 13-integral-360/                    # CloudPage: Logo Enel inyectado + Footer saneado
    ├── 14-access-my-enel/                  # AEM Portal SSO: Verificado
    ├── 15-elena-esta-enel-whatsapp/        # AEM Landing: Verificada
    └── 16-facturavirtual-enel-web/         # CloudPage: Logo HD + Footer institucional
```

> **Cada subcarpeta contiene 2 archivos:**
> - `[nombre].html`: Código HTML visual listo para previsualización e integración directa.
> - `[nombre].txt`: Archivo en texto plano sin formato para copiar y pegar directamente en los bloques HTML de **Salesforce Marketing Cloud** o componentes de **Adobe Experience Manager (AEM)**.

---

## 🛡️ 2. Resumen de Saneamiento Legal Aplicado

1. **Footer Institucional Enel Colombia:**
   * **Legal:** `https://www.enel.com.co/es/aviso-privacidad.html` *(Ajustado a la ruta oficial del cliente)*
   * **Privacidad:** `https://www.enel.com.co/es/politica-de-tratamiento-de-datos.html`
   * **Política de cookies:** `https://www.enel.com.co/es/politica-de-cookies/politica-de-cookies.html`
   * **Sello y Razón Social:** `Enel Colombia S.A ESP | VIGILADO SUPERINTENDENCIA FINANCIERA DE COLOMBIA`
   * **Selector de Idioma:** `Colombia (Español)`
2. **Exclusión Justificada en Cultura de Legalidad (Ítem 11):**
   * Por tratarse de un canal de denuncias anónimas, no se incluye casilla obligatoria de política de privacidad, respetando estrictamente el requerimiento.
3. **Preservación del Componente de Aplicación Móvil:**
   * Se mantuvieron intactos los botones oficiales de descarga de **App Store** y **Google Play** ("Descarga nuestra app").
4. **Logos Bancarios (DAVIbank / Davivienda):**
   * Ninguno de estos 16 formularios contiene logos hacia Davivienda o DAVIbank. Toda la identidad gráfica corresponde 100% a Enel Colombia. (La transición de DAVIbank a Davivienda aplica exclusivamente al formulario de Crédito Fácil Codensa `leads-cfc-mayo-2022`).
