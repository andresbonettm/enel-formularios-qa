# Informe Técnico: Auditoría de Pie de Página, Formularios Externos y Desbloqueo Google Ads

> **Cliente:** Enel Colombia  
> **Proyecto:** Saneamiento Técnico del Portal, Desbloqueo de Google Ads y Normalización de Formularios  
> **Cuenta Google Ads Impactada:** ID `7120943744`  
> **Motivo de Suspensión:** Política de "Sitios comprometidos" (Compromised Site)  
> **Fecha de Emisión:** Noviembre 2026  
> **Ubicación de Trabajo:** Carpeta centralizada [`Enel_google/`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google)  

---

## 1. Resumen Ejecutivo y Diagnóstico Global

El presente informe consolida el diagnóstico técnico, la auditoría quirúrgica de formularios y el plan de remediación integral para levantar la suspensión de la cuenta de Google Ads (`7120943744`) de Enel Colombia, estandarizar el pie de página institucional en AEM y adecuar legalmente los formularios de captación de leads en cumplimiento con la normativa de la Superintendencia Financiera y Habeas Data (SIC).

### Hallazgos Principales:
1. **Suspensión de Google Ads:** Originada por la detección automatizada de Google de enlaces/recursos hacia el dominio obsoleto y catalogado como sospechoso `cdnsafbapps.com` dentro de artículos históricos de 2017 y 2018 alojados en AEM.
2. **Pie de Página Global (AEM):** Se clarificó la arquitectura de plantillas. **No se requiere intervenir 100 páginas de forma manual**, ya que el footer se gestiona centralizadamente vía Experience Fragment / Template. La versión en español ya fue actualizada a *"© Enel Colombia S.A. ESP 2026"*; únicamente resta aplicar el cambio en la plantilla en inglés.
3. **Censo de Formularios Externos:** Se identificaron **166 páginas vivas en el portal de Enel** que contienen enlaces hacia **18 formularios externos** principales (más 2 formularios adicionales activos en campañas de Google Ads).
4. **Estado de Cumplimiento de Formularios:**
   - **4 formularios (22%)** en `cloud.customer.enelx.com` ya cumplen plenamente con footer corporativo, logo de Superfinanciera y casillas de privacidad y comerciales.
   - **12 formularios (67%)** requieren adecuaciones (inserción de footer corporativo, logo Superfinanciera, casillas de privacidad y/o casillas comerciales).
   - **2 formularios (11%)** presentan **error crítico HTTP 404** (`Copropiedades` y `leads-mr-no-regulado-2026`), lo que genera pérdida inmediata de conversiones y rebote directo para usuarios de pauta.

---

## 2. Diagnóstico de Google Ads: Causa de Suspensión y Remediación

Google Ads suspendió las campañas bajo la causal de **"Sitios comprometidos"**. Tras la inspección técnica profunda en la base de datos local y el repositorio JCR de AEM, se localizaron los llamados exactos al dominio externo no verificado `cdnsafbapps.com`:

### Rutas Identificadas con Infección/Llamados Obsoletos:

| # | URL de Página en Enel Colombia | Recurso Externo Detectado (`cdnsafbapps.com`) | Acción de Remediación en AEM |
|:---:|:---|:---|:---|
| 1 | `https://www.enel.com.co/es/historias/a201711-valores-que-construyen-un-mejor-pais.html` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/IMG-construyendo-un-mejor-pais-1.jpg` | Descargar imagen, migrar al DAM interno (`/content/dam/enel-co/...`), reemplazar referencia y republicar página. |
| 2 | `https://www.enel.com.co/en/stories/a201711-investing-to-improve-the-quality-of-our-energy.html` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/imagen-incorporando-nuevas-tecnologias.jpg` | Migrar imagen al DAM interno de Enel, actualizar componente de imagen en AEM y republicar. |
| 3 | `https://www.enel.com.co/es/historias/a201804-beca-excelencia-academica.html` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/IMG-excelencia-academica-info-cod.jpg` | Migrar imagen al DAM interno, limpiar llamada externa y republicar en AEM. |

> 🛡️ **Procedimiento de Desbloqueo ante Google Ads:**  
> Una vez reemplazadas estas 3 llamadas y verificado con escaneo limpio (cero referencias a `cdnsafbapps.com`), se radicará formalmente la apelación en Google Ads Console adjuntando el registro de remediación técnica (*Ticket de Apelación UAT*).

---

## 3. Diagnóstico del Pie de Página Institucional (AEM)

### Contexto y Clarificación del Esfuerzo
En la propuesta inicial se contempló mapear y editar 100 páginas de forma individual para asegurar la presencia de *"Enel Colombia S.A. ESP"*.  
**Diagnóstico confirmado:**  
- El pie de página se rige por un **Experience Fragment global** compartido. No existe necesidad de tocar 100 páginas independientes.
- **Versión en Español (`/es`):** Fue actualizada satisfactoriamente el **27 de octubre de 2026** por el usuario `ctorres`. Todas las páginas en español ya despliegan *"© Enel Colombia S.A. ESP 2026"*.
- **Versión en Inglés (`/en`):** Permanece desactualizada mostrando *"ENEL S.A 2018"*.
- **Acción requerida (Fase 2.1):** Editar el nodo de pie de página en `/content/experience-fragments/enel-co/en/site/footer/master` o componente global correspondiente, cambiar a *"© Enel Colombia S.A. ESP 2026"* y replicar a producción.

---

## 4. Auditoría Quirúrgica de los 18 Formularios Externos

Los formularios se alojan en dos dominios externos independientes de AEM:
1. `enelsud.info-enel.com` (11 Formularios): Plataforma de marketing cloud legacy con carencias generalizadas de footer y casillas de consentimiento.
2. `cloud.customer.enelx.com` (7 Formularios): Plataforma más reciente de Enel X con mejor nivel de cumplimiento.

### Matriz Detallada de Diagnóstico Técnico:

| # | Dominio | URL del Formulario | Págs. AEM | Status | Footer Institucional | Logo Superfinanciera | Casillas Checkboxes | Diagnóstico y Acción Requerida |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | `info-enel.com` | `https://enelsud.info-enel.com/leads-cfc-mayo-2022` | 10 | 200 OK | ✅ Sí | ❌ No | 1 (Habeas Data) | **Requiere Ajuste:** Formulario comercial de Crédito Fácil Codensa. Requiere agregar logo Superfinanciera y las 3 casillas comerciales independientes (Marketing, Terceros, Perfiles). |
| **2** | `info-enel.com` | `https://enelsud.info-enel.com/FacturaVirtual_Enel_Web` | 11 | 200 OK | ❌ No | ❌ No | 2 (Datos + Términos) | **Requiere Ajuste:** Carece de footer corporativo. Agregar pie de página estandarizado con logo Superfinanciera y validar casilla de privacidad. |
| **3** | `info-enel.com` | `https://enelsud.info-enel.com/formulario-cultura-legalidad` | 11 | 200 OK | ❌ No | ❌ No | 0 | **Requiere Ajuste:** Carece de footer y casillas. Integrar footer institucional y casilla obligatoria de política de tratamiento de datos personales. |
| **4** | `info-enel.com` | `https://enelsud.info-enel.com/enel-reporte-anonimo` | 14 | 200 OK | ❌ No | ❌ No | 0 | **Requiere Ajuste:** Carece de footer y casillas. Agregar pie de página institucional y cláusula legal de confidencialidad / tratamiento de datos. |
| **5** | `info-enel.com` | `https://enelsud.info-enel.com/Formulario-Energy-Management` | 9 | 200 OK | ⚠️ Genérico | ❌ No | 0 | **Requiere Ajuste:** Actualizar footer con nombre legal "Enel Colombia S.A. ESP" y agregar casillas de aceptación comercial y privacidad. |
| **6** | `info-enel.com` | `https://enelsud.info-enel.com/PagoVirtEmpresas` | 3 | 200 OK | ⚠️ Genérico | ❌ No | 0 | **Requiere Ajuste:** Actualizar pie de página y agregar casilla obligatoria de política de privacidad. |
| **7** | `info-enel.com` | `https://enelsud.info-enel.com/SFacturaDigital` | 4 | 200 OK | ✅ Sí | ❌ No | 2 (Datos + Términos) | **Requiere Ajuste:** Cuenta con políticas de Ley 1581. Falta incorporar en el footer el logo obligatorio de Vigilado Superintendencia Financiera. |
| **8** | `info-enel.com` | `https://enelsud.info-enel.com/EFacturaCorp` | 1 | 200 OK | ⚠️ Genérico | ❌ No | 0 | **Requiere Ajuste:** Actualizar footer institucional y agregar casilla de consentimiento de datos personales. |
| **9** | `info-enel.com` | `http://enelsud.info-enel.com/Copropiedades` | 1 | 🚨 **404** | ❌ No | ❌ No | 0 | **Crítico:** La URL no existe en el servidor externo. Corregir enlace en la página de AEM (`/empresas/.../exoneracion-copropiedad.html`) o restaurar landing externa. |
| **10** | `info-enel.com` | `http://enelsud.info-enel.com/FacturaDigital` | 1 | 200 OK | ✅ Sí | ❌ No | 2 (Datos + Términos) | **Requiere Ajuste:** Migrar protocolo a HTTPS y actualizar footer agregando el logo de la Superfinanciera. |
| **11** | `info-enel.com` | `http://enelsud.info-enel.com/RetiroEfactura` | 1 | 200 OK | ✅ Sí | ❌ No | 0 | **Requiere Ajuste:** En AEM apunta a HTTP `RetiroEfactura` mientras la versión viva es `RetiroEfacturaV`. Migrar a HTTPS, agregar casilla de privacidad y logo Superfinanciera. |
| **12** | `customer.enelx.com` | `https://cloud.customer.enelx.com/leads-obras-org` | 13 | 200 OK | ✅ Sí | ✅ Sí | 4 (Priv + 3 Comerciales) | **Al Día (Cumple):** Cuenta con footer corporativo, logo Superfinanciera y las 4 casillas completas y separadas. |
| **13** | `customer.enelx.com` | `https://cloud.customer.enelx.com/contacto-empresas-2026` | 35 | 200 OK | ✅ Sí | ✅ Sí | 4 (Priv + 3 Comerciales) | **Al Día (Cumple):** Implementación modelo. Presente en 35 páginas del portal. |
| **14** | `customer.enelx.com` | `https://cloud.customer.enelx.com/contacto-ciudades-2026` | 48 | 200 OK | ✅ Sí | ✅ Sí | 4 (Priv + 3 Comerciales) | **Al Día (Cumple):** Implementación modelo. Presente en 48 páginas del portal. |
| **15** | `customer.enelx.com` | `https://cloud.customer.enelx.com/contacto-mr-no-regulado-2026` | 2 | 200 OK | ✅ Sí | ✅ Sí | 4 (Priv + 3 Comerciales) | **Al Día (Cumple):** Versión funcional de Mercado No Regulado. |
| **16** | `customer.enelx.com` | `https://cloud.customer.enelx.com/leads-juicebox-2026` | 4 | 200 OK | ✅ Sí | ✅ Sí | 4 (Priv + 3 Comerciales) | **Requiere Ajuste Menor:** Las 4 casillas existen, pero se debe revisar el texto visible de las casillas comerciales para alinearlas a la versión corporativa estándar. |
| **17** | `customer.enelx.com` | `https://cloud.customer.enelx.com/leads-asistencias-organico-portafolio` | 9 | 200 OK | ✅ Sí | ❌ No | 4 (Priv + 3 Comerciales) | **Requiere Ajuste:** Dispone de las 4 casillas, pero carece del logo de Vigilado Superintendencia Financiera en el pie de página. |
| **18** | `customer.enelx.com` | `https://cloud.customer.enelx.com/leads-mr-no-regulado-2026` | 1 | 🚨 **404** | ❌ No | ❌ No | 0 | **Crítico:** Enlace roto en AEM. Se debe actualizar en AEM para que apunte a `contacto-mr-no-regulado-2026` (Formulario #15). |

### Formularios Adicionales Identificados en Campañas de Google Ads:
- **`https://cloud.customer.enelx.com/asistencia-funeral`:** 200 OK. Cuenta con footer, logo Superfinanciera y las 4 casillas de cumplimiento.
- **`https://cloud.customer.enelx.com/integral-360`:** 200 OK. Cuenta con footer, logo Superfinanciera y las 4 casillas de cumplimiento.

---

## 5. Cruce de Páginas de AEM con Campañas de Google Ads

A partir del listado oficial de campañas publicitarias activas en Google Ads (`docs/Listado de campañas Google Ads - Impactadas.xlsx`), se relacionan las URLs destino con sus respectivos formularios:

| Campaña Google Ads | URL de Campaña (Landing / Anuncio) | Destino / Formulario Asociado | Estado Técnico |
|:---|:---|:---|:---:|
| **Asistencias** | `https://cloud.customer.enelx.com/asistencia-funeral` | Formulario directo Enel X | 🟢 Operativo y Cumple |
| **Adecuaciones eléctricas** | `https://cloud.customer.enelx.com/leads-obras-org` | Formulario directo Enel X (#12) | 🟢 Operativo y Cumple |
| **Cargadores eléctricos** | `https://www.enel.com.co/es/personas/juicebox-enel` | `https://cloud.customer.enelx.com/leads-juicebox-2026` (#16) | 🟡 Ajuste menor casillas |
| **Pagos digitales** | `https://www.enel.com.co/es/pago-medios-electronicos.html` | Pasarela de Pago PSE / Enel | 🟢 Operativo |
| **Canales digitales** | `https://www.enel.com.co/es/personas/registro.html` | Portal de Registro AEM | 🟢 Operativo |
| **Seguridad y legalidad** | `https://www.enel.com.co/es/personas/hurto-energia-consecuencias-legales.html` | `https://enelsud.info-enel.com/formulario-cultura-legalidad` (#3) | 🟡 Requiere footer y casilla |
| **Uso Eficiente** | `https://www.enel.com.co/es/fenomeno-de-el-nino/eficiencia-energetica-para-pequenas-empresas.html` | Enlaces informativos AEM | 🟢 Operativo |
| **Amplificación Energías** | `https://www.enel.com.co/es/fenomeno-de-el-nino.html` | Hub informativo AEM | 🟢 Operativo |
| **Fraudes Digitales** | `https://www.enel.com.co/es/historias/a202308-consejos-para-evitar-fraudes-digitales.html` | Enlace a reporte anónimo (#4) | 🟡 Requiere footer y casilla |
| **Factura Virtual** | `https://www.enel.com.co/es/personas/factura-virtual.html` | `https://enelsud.info-enel.com/FacturaVirtual_Enel_Web` (#2) | 🟡 Requiere footer y logo Super |
| **Asistencia Integral 360** | `https://cloud.customer.enelx.com/integral-360` | Formulario directo Enel X | 🟢 Operativo y Cumple |
| **Canales Digitales (WhatsApp)**| `https://www.enel.com.co/es/personas/servicio-al-cliente/elena-esta-enel-whatsapp.html` | Bot Elena WhatsApp | 🟢 Operativo |

---

## 6. Distribución de Horas y Cotización de Trabajo

El plan contempla **46 Horas de Trabajo**, estructuradas en 2 fases de ejecución técnica:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ FASE 1: IDENTIFICAR LOS ERRORES (20 Horas)                                  │
│ - 1.1 Barrido del portal con pausas de seguridad (Imperva CDP)      : 8 h   │
│ - 1.2 Cruce de páginas con formularios externos y campañas Ads      : 6 h   │
│ - 1.3 Revisión uno a uno de los 18 formularios (Campos / Legal)      : 6 h   │
├─────────────────────────────────────────────────────────────────────────────┤
│ FASE 2: IMPLEMENTAR LO IDENTIFICADO (26 Horas)                              │
│ - 2.1 Limpieza de llamados a cdnsafbapps.com y footer en inglés      : 6 h   │
│ - 2.2 Armado y estandarización del pie de página para formularios    : 6 h   │
│ - 2.3 Ajuste de casillas de privacidad y 3 casillas comerciales      : 8 h   │
│ - 2.4 Pruebas de funcionamiento, tracking UTM y soporte Google Ads   : 6 h   │
├─────────────────────────────────────────────────────────────────────────────┤
│ TOTAL ESTIMADO DEL PROYECTO: 46 HORAS                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Archivos de Trabajo Centralizados en `Enel_google/`

Todos los entregables, matrices de datos y scripts de soporte han quedado organizados en la carpeta centralizada:

1. 📄 **Informe Técnico:** [`Enel_google/INFORME_TECNICO_FOOTER_Y_FORMULARIOS_ENEL.md`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/INFORME_TECNICO_FOOTER_Y_FORMULARIOS_ENEL.md)
2. 📊 **Matriz de Diagnóstico en CSV:** [`Enel_google/MATRIZ_DIAGNOSTICO_18_FORMULARIOS.csv`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/MATRIZ_DIAGNOSTICO_18_FORMULARIOS.csv)
3. 📋 **Checklist Operativo de 6 Días:** [`Enel_google/CHECKLIST_CRONOGRAMA_FORMULARIOS.md`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/CHECKLIST_CRONOGRAMA_FORMULARIOS.md)
4. 🗂️ **Censo Completo de Páginas AEM:** [`Enel_google/censo_formularios_aem.json`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/censo_formularios_aem.json)
5. 🔍 **Auditoría Técnica de Campos y Checkboxes:** [`Enel_google/auditoria_18_formularios_completa.json`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/auditoria_18_formularios_completa.json)
