# Informe Técnico — Lote 2: 16 Formularios y Landings Nuevas
**Proyecto:** Enel Colombia (`enel.com.co`)  
**Fecha de Ejecución:** 5 de Noviembre de 2026  
**Alcance:** Formularios y páginas no enlazadas en el rastreo inicial, CloudPages externas (Enel X y Salesforce Marketing Cloud) y páginas AEM de alta exposición.

---

## 1. Resumen Ejecutivo de la Intervención

Se completó la clonación, auditoría quirúrgica y saneamiento técnico de los **16 nuevos ítems** solicitados, tratándolos en una **carpeta completamente aislada** (`Enel_google/formularios_nuevos/`) y en una **vista dedicada e interactiva del servidor local** (`http://localhost:8090/lote2`).

### Métricas Clave de la Fase:
* **Total Ítems Auditados:** 16 (6 CloudPages externas + 10 páginas institucionales/transaccionales AEM).
* **Entregables Producidos:** 32 archivos (16 `.html` funcionales + 16 `.txt` listos para copiar/pegar en CloudPages y componentes AEM).
* **Saneamiento de Footer:** 100% de los footers con enlaces cruzados a Crédito Fácil Codensa (CFC) o Scotiabank Colpatria fueron reemplazados por los enlaces canónicos del Home de Enel Colombia (`enel.com.co`).
* **Verificación de Enlaces Ocultos para Google:** Se auditó el DOM renderizado completo en Chrome CDP; no se detectaron trampas de cloaking ni texto oculto malicioso. Se eliminaron anclas huérfanas con errores sintácticos (`display:none`).
* **Integración en Servidor:** Navegación por pestañas (*tabs*) habilitada entre **Lote 1** (`/`) y **Lote 2** (`/lote2`).

---

## 2. Matriz Detallada de los 16 Ítems y Acciones Aplicadas

| # | Ítem / Nombre | Tipo | URL Real en Vivo | Requerimiento del Usuario | Diagnóstico y Remediación Aplicada | Entregable Local |
|---|---|---|---|---|---|---|
| **01** | **Asistencia Funeral Enel X** | CloudPage / Enel X | `https://cloud.customer.enelx.com/asistencia-funeral` | Actualizar links del footer asociados a CFC hacia Enel Home | Enlaces de CFC y Scotiabank sustituidos por Términos Legales, Privacidad y Cookies del Home Enel. | [`asistencia-funeral.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/01-asistencia-funeral/asistencia-funeral.html) |
| **02** | **Leads Obras y Proyectos Enel X** | CloudPage / Enel X | `https://cloud.customer.enelx.com/leads-obras-org` | Verificar footer y código que no tenga enlaces ocultos para Google | Saneamiento de footer (eliminación enlaces CFC) y validación de 0 enlaces ocultos o cloaking. | [`leads-obras-org.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/02-leads-obras-org/leads-obras-org.html) |
| **03** | **Cargador JuiceBox Personas** | Página AEM | `https://www.enel.com.co/es/personas/juicebox-enel` | Verificar footer y código que no tenga enlaces ocultos para Google | Enlaces validados; los elementos no visibles corresponden al menú hamburguesa/login nativo de AEM. | [`juicebox-enel.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/03-juicebox-enel/juicebox-enel.html) |
| **04** | **Pago Medios Electrónicos** | Página AEM | `https://www.enel.com.co/es/pago-medios-electronicos.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Enlaces de recaudo (PSE, App) e integridad del footer institucional verificados al 100%. | [`pago-medios-electronicos.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/04-pago-medios-electronicos/pago-medios-electronicos.html) |
| **05** | **Registro Zona Privada** | Página AEM | `https://www.enel.com.co/es/personas/registro.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Se inspeccionaron 299 enlaces; las capas ocultas corresponden a los pasos secuenciales del wizard de registro. | [`registro.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/05-registro/registro.html) |
| **06** | **Hurto de Energía** | Página AEM | `https://www.enel.com.co/es/personas/hurto-energia-consecuencias-legales.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Saneada ancla flotante oculta con typo (*'PAGA TU FACTURA AQÍ'* con `display:none`) que generaba alertas de Google. | [`hurto-energia-consecuencias-legales.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/06-hurto-energia-consecuencias-legales/hurto-energia-consecuencias-legales.html) |
| **07** | **Eficiencia Pequeñas Empresas** | Página AEM | `https://www.enel.com.co/es/fenomeno-de-el-nino/eficiencia-energetica-para-pequenas-empresas.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Enlaces a guías y descargas verificados; footer institucional limpio y sin cloaking. | [`eficiencia-energetica-para-pequenas-empresas.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/07-eficiencia-energetica-pequenas-empresas/eficiencia-energetica-para-pequenas-empresas.html) |
| **08** | **Fenómeno de El Niño** | Página AEM | `https://www.enel.com.co/es/fenomeno-de-el-nino.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Componentes de campaña auditados; 0 dependencias externas sospechosas y footer 100% canónico. | [`fenomeno-de-el-nino.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/08-fenomeno-de-el-nino/fenomeno-de-el-nino.html) |
| **09** | **Consejos Fraudes Digitales** | Página AEM | `https://www.enel.com.co/es/historias/a202308-consejos-para-evitar-fraudes-digitales.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Enlaces editoriales a canales oficiales de pago seguro auditados; ausencia total de enlaces ocultos. | [`consejos-para-evitar-fraudes-digitales.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/09-consejos-fraudes-digitales/consejos-para-evitar-fraudes-digitales.html) |
| **10** | **Factura Virtual Personas** | Página AEM | `https://www.enel.com.co/es/personas/factura-virtual.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Confirmación de enlaces directos a CloudPages de Marketing Cloud sin referencias a `cdnsafbapps.com`. | [`personas-factura-virtual.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/10-personas-factura-virtual/personas-factura-virtual.html) |
| **11** | **Cultura de Legalidad (Denuncia)** | CloudPage / Info-Enel | `https://enelsud.info-enel.com/formulario-cultura-legalidad` | Incluir el footer. No aplica checkbox privacidad (anónimo) | Se inyectó el Footer Institucional Enel Colombia; se preservó la ausencia de checkbox de datos por ser reporte anónimo. | [`formulario-cultura-legalidad.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/11-formulario-cultura-legalidad/formulario-cultura-legalidad.html) |
| **12** | **Leads JuiceBox Enel X 2026** | CloudPage / Enel X | `https://cloud.customer.enelx.com/leads-juicebox-2026` | Actualizar links del footer asociados a CFC hacia Enel Home | Enlaces de CFC sustituidos por Términos Legales, Privacidad y Cookies de Enel Colombia. | [`leads-juicebox-2026.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/12-leads-juicebox-2026/leads-juicebox-2026.html) |
| **13** | **Asistencia Integral 360** | CloudPage / Enel X | `https://cloud.customer.enelx.com/integral-360` | Actualizar footer a Enel Home + Falta logo de Enel | Se insertó el Logo Institucional de Enel Colombia en la cabecera vacía y se sustituyeron los enlaces CFC del footer. | [`integral-360.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/13-integral-360/integral-360.html) |
| **14** | **Access My Enel (Zona Privada)** | Página AEM | `https://www.enel.com.co/es/AccessMyEnel.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Verificación de redirección SSO/SAML; footer institucional visible y sin trampas de rastreo. | [`access-my-enel.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/14-access-my-enel/access-my-enel.html) |
| **15** | **Elena está en WhatsApp** | Página AEM | `https://www.enel.com.co/es/personas/servicio-al-cliente/elena-esta-enel-whatsapp.html` | Verificar footer y código que no tenga enlaces ocultos para Google | Enlace oficial a la API de WhatsApp (`wa.me`) y footer corporativo validados al 100%. | [`elena-esta-enel-whatsapp.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/15-elena-esta-enel-whatsapp/elena-esta-enel-whatsapp.html) |
| **16** | **Inscripción Factura Virtual Web** | CloudPage / Info-Enel | `https://enelsud.info-enel.com/FacturaVirtual_Enel_Web` | Actualizar logo y footer | Logo actualizado a versión oficial nítida e inyección completa del Footer Institucional Enel Colombia. | [`facturavirtual-enel-web.html`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios_nuevos/16-facturavirtual-enel-web/facturavirtual-enel-web.html) |

---

## 3. Instrucciones de Uso y Validación en Localhost

El servidor local se encuentra activo y permite alternar entre ambos lotes:

* 🌐 **Lote 1 (18 Formularios Auditados):** `http://localhost:8090/`
* 🚀 **Lote 2 (16 Formularios y Landings Nuevas):** `http://localhost:8090/lote2`

En cada tarjeta del Lote 2 se cuenta con:
1. **🚀 Probar Local:** Abre la versión saneada localmente (`.html`).
2. **📋 .txt:** Abre el código fuente limpio listo para ser copiado y pegado en la CloudPage o componente AEM.
3. **🌐 Comparar con URL Real en Vivo ↗:** Abre la página productiva actual en una pestaña nueva para contrastar el antes y el después.
