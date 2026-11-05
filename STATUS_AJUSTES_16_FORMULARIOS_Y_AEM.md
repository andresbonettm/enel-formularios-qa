# Matriz Integral de Ajustes Realizados, Estatus Local y Tareas Pendientes
**Proyecto:** Auditoría Técnica y Normalización Legal de Formularios y Landings — Enel Colombia  
**Fecha:** 5 de Noviembre de 2026  
**Servidor Local Activo:** `http://localhost:8090` (Lote 1: Prioridad 2) y `http://localhost:8090/lote2` (Lote 2: Prioridad 1)  
**Documento Base del Cliente:** [Google Spreadsheet — Prioridades y Legales](https://docs.google.com/spreadsheets/d/1iZRa9VVFm0GYJ6uUV1PuR6AkkiJKCNwrYnJQvRCw0xc/edit?gid=0#gid=0)

---

## 1. Resumen Ejecutivo: Qué se ha Realizado en Local (100% Completado)

### A. Prioridad 1 (Paquete Inmediato para Mañana — 16 Ítems, Filas 19 a 34 del Excel)
Se clonaron, auditaron, corrigieron y montaron en el servidor local (`Enel_google/formularios_nuevos/` accesible en `http://localhost:8090/lote2`):

1. **6 Formularios / CloudPages Externas (Marketing Cloud / Enel X):**
   * **01. Asistencia Funeral (`cloud.customer.enelx.com/asistencia-funeral`):** Saneado. Se removieron los enlaces de Crédito Fácil Codensa (`creditofacilcodensa.com/legales/reglamentos`, `politicas/generales`) y Scotiabank; se insertaron los enlaces oficiales del Home de Enel Colombia.
   * **02. Leads Obras Enel X (`cloud.customer.enelx.com/leads-obras-org`):** Saneado. Footer actualizado a Enel Home. Se verificó el DOM: 0 enlaces ocultos y 0 trampas SEO.
   * **11. Cultura de Legalidad (`enelsud.info-enel.com/formulario-cultura-legalidad`):** Inyección de footer institucional Enel Colombia con sello Superfinanciera. Se omitió la casilla de privacidad expresamente solicitada por ser un reporte 100% anónimo.
   * **12. Leads JuiceBox 2026 (`cloud.customer.enelx.com/leads-juicebox-2026`):** Saneado. Enlaces de CFC eliminados y sustituidos por los institucionales de Enel Home.
   * **13. Integral 360 (`cloud.customer.enelx.com/integral-360`):** Saneado. Se insertó el Logo SVG Oficial de Enel Colombia en la cabecera que estaba vacía y se sustituyó el footer de CFC por el de Enel Home.
   * **16. Inscripción Factura Virtual (`enelsud.info-enel.com/FacturaVirtual_Enel_Web`):** Saneado. Se actualizó el isotipo de Enel a SVG de alta definición y se insertó el pie de página institucional completo.

2. **10 Páginas de AEM (`enel.com.co`):**
   * Todas las 10 URLs fueron auditadas a nivel de DOM y árbol JCR en AEM Author (`10.152.145.177:4502`):
     * **Juicebox Enel** (`/es/personas/juicebox-enel.html`)
     * **Pago Medios Electrónicos** (`/es/pago-medios-electronicos.html`)
     * **Registro Clientes** (`/es/personas/registro.html`)
     * **Hurto Energía** (`/es/personas/hurto-energia-consecuencias-legales.html`)
     * **Eficiencia Energética Pequeñas Empresas** (`/es/fenomeno-de-el-nino/eficiencia-energetica-para-pequenas-empresas.html`)
     * **Fenómeno de El Niño** (`/es/fenomeno-de-el-nino.html`)
     * **Consejos Fraudes Digitales** (`/es/historias/a202308-consejos-para-evitar-fraudes-digitales.html`)
     * **Factura Virtual Hub** (`/es/personas/factura-virtual.html`)
     * **AccessMyEnel** (`/es/AccessMyEnel.html`)
     * **Elena WhatsApp** (`/es/personas/servicio-al-cliente/elena-esta-enel-whatsapp.html`)
   * **Dictamen Anti-Cloaking:** Ninguna página presenta cloaking o penalizaciones de Google. Los enlaces invisibles reportados por herramientas externas corresponden a menús interactivos desplegables nativos de AEM (Selector de países del Grupo Enel, modal de Login SSO de clientes y pasos del asistente de registro).
   * **Acciones Menores Identificadas para AEM:**
     * En `hurto-energia`: retirar el botón huérfano `<a style="display:none">PAGA TU FACTURA AQÍ</a>` (generado por regla Launch).
     * En `registro`: actualizar 3 links internos de `http://` a `https://`.

---

### B. Ajuste Transversal de Enlaces Legales (50 Archivos Actualizados)
Siguiendo la instrucción estricta del cliente y el pantallazo del footer de Enel Colombia:

1. **Footer Estándar de Enel Colombia (33 Formularios y Landings):**
   * **Legal:** `https://www.enel.com.co/es/aviso-privacidad.html` *(Ajustado: antes apuntaba a /cookies/politica-de-cookies o /legales)*.
   * **Privacidad:** `https://www.enel.com.co/es/politica-de-tratamiento-de-datos.html`
   * **Política de cookies:** `https://www.enel.com.co/es/politica-de-cookies/politica-de-cookies.html`
   * **Sello:** `Enel Colombia S.A ESP | VIGILADO SUPERINTENDENCIA FINANCIERA DE COLOMBIA`
   * **Selector:** `Colombia (Español)`

2. **Excepción Obligatoria — Formulario Crédito Fácil Codensa (CFC):**
   * URL: `https://enelsud.info-enel.com/leads-cfc-mayo-2022`
   * **Legal:** `https://www.creditofacilcodensa.com/legales/reglamentos`
   * **Privacidad:** `https://cdn.aglty.io/scotiabank-colombia/terminos_y_condiciones_cfc.pdf` *(Ajustado con la URL oficial de Agility/Scotiabank)*
   * **Política de cookies:** `https://www.creditofacilcodensa.com/politicas/generales`

3. **Componente "Descarga nuestra app":**
   * Se verificó y mantuvo intacto en todos los formularios donde viene nativo (los botones de **App Store** y **Google Play**), garantizando que no se elimine en ningún archivo.

---

## 2. Qué Queda Pendiente y Próximos Pasos

### A. En Formularios de Prioridad 2 (Filas 1 a 18 del Excel)
1. **Reemplazo en AEM de 2 Formularios Obsoletos:**
   * **Formulario 04 obsoleto:** `https://enelsud.info-enel.com/enel-reporte-anonimo`  
     *Pendiente:* Reemplazar por `https://enelsud.info-enel.com/formulario-cultura-legalidad` en las **14 páginas vivas de AEM** que lo referencian.
   * **Formulario 05 obsoleto:** `https://enelsud.info-enel.com/Formulario-Energy-Management`  
     *Pendiente:* Reemplazar por `https://cloud.customer.enelx.com/contacto-mr-no-regulado-2026` en las **9 páginas vivas de AEM** que lo referencian.
2. **Ajuste en Formulario 06 (`PagoVirtEmpresas`):**
   * Solicitar al equipo de Salesforce Marketing Cloud remover la frase restrictiva de correo empresarial (`"Ingresa correo empresarial..."`).

### B. Coordinaciones Externas y Validaciones en Curso
1. **Transición Davibank a Davivienda (CFC):**
   * Coordinación con **Ana María Valbuena (Omnicom)** y **Gerar** para actualizar las piezas gráficas de Davibank a Davivienda en el footer del formulario de CFC (`leads-cfc-mayo-2022`).
2. **Validación Legal sobre 3 Landings Comerciales:**
   * El área Legal de Enel se encuentra validando internamente si se deben actualizar con fines comerciales las siguientes 3 páginas (aún no incorporadas en el Excel):
     * `https://www.enel.com.co/es/consentimiento-para-actividades-de-marketing`
     * `https://www.enel.com.co/es/consentimiento-a-codensa-y-a-los-terceros-autorizados-por-ella-p`
     * `https://www.enel.com.co/es/elaboracion-de-perfiles`

---

## 3. Guía de Acceso Rápido al Servidor Local

* **Dashboard Lote 1 (18 Formularios - Prioridad 2):**  
  👉 `http://localhost:8090/`
* **Dashboard Lote 2 (16 Formularios y Landings Nuevas - Prioridad 1 para mañana):**  
  👉 `http://localhost:8090/lote2`
* **Directorio de Archivos Listos para Despliegue:**  
  * `Enel_google/formularios/` (Formularios 01 al 18)  
  * `Enel_google/formularios_nuevos/` (Ítems 01 al 16)
