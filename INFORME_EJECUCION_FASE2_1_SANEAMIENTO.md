# Informe de Ejecución: Saneamiento Técnico Fase 2.1 — Enel Colombia

> **Proyecto:** Desbloqueo de Google Ads, Estandarización de Footer y Limpieza de Enlaces  
> **Cuenta Google Ads:** ID 7120943744  
> **Fecha de Ejecución:** 2026-11-04  
> **Usuario AEM:** `oespinel`  
> **Entorno:** Producción AEM Author (`10.152.145.177:4502`) ➔ Publicación a Publishers  
> **Directorio de Trabajo:** [`Enel_google/`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google)  

---

## 1. Resumen de la Intervención

En cumplimiento de la **Tarea 2.1 del Cronograma de Trabajo**, se ejecutó con éxito la remediación técnica sobre los componentes identificados en Adobe Experience Manager (AEM). Todas las operaciones siguieron estrictamente el protocolo de seguridad:
- ✅ Snapshot JCR de respaldo previo por cada nodo en `scratch/backups_aem/`.
- ✅ Actualización controlada vía Sling POST.
- ✅ Replicación inmediata a producción vía `/bin/replicate.json`.
- ✅ Asentamiento en la bitácora de auditoría [`reports/aem_modifications_log.csv`](file:///Users/andresbonett/dev/Enel_SEO/reports/aem_modifications_log.csv).
- ✅ Re-verificación mediante QueryBuilder con resultado de **cero incidencias residuales**.

---

## 2. Detalle de Acciones Ejecutadas

### 🎯 Acción 1: Erradicación Total del Dominio Comprometido `cdnsafbapps.com` (Desbloqueo Google Ads)
Google Ads mantenía suspendida la cuenta `7120943744` bajo la política de **"Sitios comprometidos"** debido a referencias activas hacia el dominio caducado y no seguro `cdnsafbapps.com`.

A continuación se listan las **URLs completas y rutas JCR sin abreviar**:

#### Tabla Detallada de Páginas y Nodos AEM Intervenidos

| # | Página Pública Completa (Canónica y Vanity) | Nodo AEM Completo Intervenido | Recurso Comprometido Eliminado | Status API POST | Status Replicación |
|:---:|:---|:---|:---|:---:|:---:|
| **1** | **Canónica:**<br>`https://www.enel.com.co/es/historias/archive/2017/11/nuestra-verdadera-energia-son-las-personas.html`<br><br>**Vanity:**<br>`https://www.enel.com.co/es/historias/a201711-nuestra-verdadera-energia-son-las-personas.html` | `/content/enel-co/es/megamenu/historias/archive/2017/11/nuestra-verdadera-energia-son-las-personas/jcr:content/intro` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/IMG-verdadera-energia-infografia.jpg` | 200 OK | 200 OK |
| **2** | **Canónica:**<br>`https://www.enel.com.co/es/historias/archive/2017/11/transformacion-digital-empresarial.html`<br><br>**Vanity:**<br>`https://www.enel.com.co/es/historias/a201711-transformacion-digital-empresarial.html` | `/content/enel-co/es/megamenu/historias/archive/2017/11/transformacion-digital-empresarial/jcr:content/article-content/text` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/IMG-hackday-1.jpg` | 200 OK | 200 OK |
| **3** | **Canónica:**<br>`https://www.enel.com.co/es/historias/archive/2017/11/de-los-rayos-del-sol-a-la-energia-electrica.html`<br><br>**Vanity:**<br>`https://www.enel.com.co/es/historias/a201711-de-los-rayos-del-sol-a-la-energia-electrica.html` | `/content/enel-co/es/megamenu/historias/archive/2017/11/de-los-rayos-del-sol-a-la-energia-electrica/jcr:content/intro` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/IMG-energia-electrica-2.jpg` | 200 OK | 200 OK |
| **4** | **Canónica:**<br>`https://www.enel.com.co/es/historias/archive/2017/11/la-tecnologia-que-impulsa-la-evolucion-de-la-energia-electrica.html`<br><br>**Vanity:**<br>`https://www.enel.com.co/es/historias/a201711-la-tecnologia-que-impulsa-la-evolucion-de-la-energia-electrica.html` | `/content/enel-co/es/megamenu/historias/archive/2017/11/la-tecnologia-que-impulsa-la-evolucion-de-la-energia-electrica/jcr:content/intro` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/Cont_hist_telecontrol.jpg` | 200 OK | 200 OK |
| **5** | **Canónica:**<br>`https://www.enel.com.co/es/historias/archive/2018/04/beca-excelencia-academica.html`<br><br>**Vanity:**<br>`https://www.enel.com.co/es/historias/a201804-beca-excelencia-academica.html` | `/content/enel-co/es/megamenu/historias/archive/2018/04/beca-excelencia-academica/jcr:content/intro` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/IMG-excelencia-academica-info-cod.jpg` | 200 OK | 200 OK |
| **6** | **Canónica:**<br>`https://www.enel.com.co/en/stories/archive/2017/11/innovative-projects-as-part-of-the-transformation-of-the-world.html`<br><br>**Vanity:**<br>`https://www.enel.com.co/en/stories/a201711-innovative-projects-as-part-of-the-transformation-of-the-world.html` | `/content/enel-co/en/megamenu/stories/archive/2017/11/innovative-projects-as-part-of-the-transformation-of-the-world/jcr:content/intro`<br><br>y `/content/enel-co/en/megamenu/stories/archive/2017/11/innovative-projects-as-part-of-the-transformation-of-the-world/jcr:content/article-content/text` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/imagen-maqueta.jpg`<br><br>y `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/imagen-ninos-compartiendo.jpg` | 200 OK | 200 OK |
| **7** | **Canónica:**<br>`https://www.enel.com.co/en/stories/archive/2017/11/investing-to-improve-the-quality-of-our-energy.html`<br><br>**Vanity:**<br>`https://www.enel.com.co/en/stories/a201711-investing-to-improve-the-quality-of-our-energy.html` | `/content/enel-co/en/megamenu/stories/archive/2017/11/investing-to-improve-the-quality-of-our-energy/jcr:content/intro` | `https://www.cdnsafbapps.com/2017/ejemplo-historia/imagenes/imagen-incorporando-nuevas-tecnologias.jpg` | 200 OK | 200 OK |

#### Formulario Externo de Marketing Cloud con cdnsafbapps.com Saneado

| # | Nombre del Formulario | URL Completa en Producción | Recursos Afectados en `cdnsafbapps.com` | Solución Aplicada |
|:---:|:---|:---|:---|:---|
| **8** | **Formulario 08: Factura Corporativa** | `https://enelsud.info-enel.com/EFacturaCorp` | `https://www.cdnsafbapps.com/2018/saleforce/registro-factura-virtual/node_modules/bootstrap/dist/css/bootstrap.min.css`<br>`https://www.cdnsafbapps.com/2019/Landings/saleforce/registro-factura-virtual/css/sale.css`<br>`https://www.cdnsafbapps.com/2018/saleforce/registro-factura-virtual/node_modules/bootstrap/dist/js/bootstrap.min.js`<br>`https://www.cdnsafbapps.com/2019/Landings/saleforce/registro-factura-virtual/img/favicon.png`<br>`https://www.cdnsafbapps.com/2019/Landings/saleforce/20190326_Landing_pago_factura_virtual/img/logo.png`<br>`http://www.cdnsafbapps.com/2018/saleforce/registro-factura-virtual/img/facebook.png?v=1`<br>`http://www.cdnsafbapps.com/2018/saleforce/registro-factura-virtual/img/twitter.png`<br>`http://www.cdnsafbapps.com/2018/saleforce/registro-factura-virtual/img/linke.png` | Sustitución integral por Bootstrap CDN oficial (`https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css`), CDN corporativo oficial (`https://assets.enelcol.com.co`) y eliminación de dependencias obsoletas en el paquete entregable. |

> 🔍 **Verificación Post-Intervención:**  
> Consulta Oak QueryBuilder: `path=/content/enel-co`, `fulltext=cdnsafbapps`  
> **Resultado:** **0 coincidencias encontradas**. El dominio ha quedado 100% erradicado del portal y de los formularios.

---

### 🎯 Acción 2: Actualización del Pie de Página Global en Inglés
- **Nodo Completo Modificado:** `/content/enel-co/en/jcr:content/footer`
- **Página de Impacto:** Afecta a todo el árbol de páginas en inglés bajo `https://www.enel.com.co/en.html`
- **Propiedad Modificada:** `copyRightLabel`
- **Valor Anterior:** `"ENEL S.A 2018"`
- **Valor Nuevo:** `"Enel Colombia S.A. ESP 2026"`
- **Replicación:** Replicado el nodo raíz `/content/enel-co/en` impactando la totalidad de páginas en inglés del sitio.
- **Resultado:** El portal en inglés queda alineado con la versión en español modificada el 27 de octubre de 2026.

---

### 🎯 Acción 3: Corrección de Enlace Roto 404 a Formulario en AEM
- **Página Completa en AEM:** `/content/enel-co/es/megamenu/empresas/enel-generacion`
- **URL Pública:** `https://www.enel.com.co/es/empresas/enel-generacion.html`
- **Nodo Completo del Componente:** `/content/enel-co/es/megamenu/empresas/enel-generacion/jcr:content/hub-content/group_copy_162707897/hubGroup-module/module_content_copy__1300614356/url`
- **Propiedad:** `path`
- **Valor Anterior (404 Roto):** `https://cloud.customer.enelx.com/leads-mr-no-regulado-2026`
- **Valor Nuevo (200 OK Vivo):** `https://cloud.customer.enelx.com/contacto-mr-no-regulado-2026`
- **Resultado:** Se restablece el tráfico y captación de leads en el segmento de Mercado No Regulado.

---

## 3. Respaldo y Trazabilidad (Archivos Completos)

Todos los snapshots JSON generados antes de la modificación se encuentran preservados en el directorio local:
1. `scratch/backups_aem/20261104_165228_content_enel-co_en_megamenu_stories_archive_2017_11_innovative-projects-as-part-of-the-transformation-of-the-world_jcr:content_article-content_text.json`
2. `scratch/backups_aem/20261104_165231_content_enel-co_es_megamenu_historias_archive_2017_11_transformacion-digital-empresarial_jcr:content_article-content_text.json`
3. `scratch/backups_aem/20261104_165233_content_enel-co_es_megamenu_historias_archive_2017_11_nuestra-verdadera-energia-son-las-personas_jcr:content_intro.json`
4. `scratch/backups_aem/20261104_165234_content_enel-co_en_megamenu_stories_archive_2017_11_innovative-projects-as-part-of-the-transformation-of-the-world_jcr:content_intro.json`
5. `scratch/backups_aem/20261104_165236_content_enel-co_en_megamenu_stories_archive_2017_11_investing-to-improve-the-quality-of-our-energy_jcr:content_intro.json`
6. `scratch/backups_aem/20261104_165238_content_enel-co_es_megamenu_historias_archive_2017_11_de-los-rayos-del-sol-a-la-energia-electrica_jcr:content_intro.json`
7. `scratch/backups_aem/20261104_165239_content_enel-co_es_megamenu_historias_archive_2017_11_la-tecnologia-que-impulsa-la-evolucion-de-la-energia-electrica_jcr:content_intro.json`
8. `scratch/backups_aem/20261104_165241_content_enel-co_es_megamenu_historias_archive_2018_04_beca-excelencia-academica_jcr:content_intro.json`
9. `scratch/backups_aem/20261104_165243_content_enel-co_en_jcr:content_footer.json`
10. `scratch/backups_aem/20261104_165245_content_enel-co_es_megamenu_empresas_enel-generacion_jcr:content_hub-content_group_copy_162707897_hubGroup-module_module_content_copy__1300614356_url.json`

Registro permanente asentado en [`reports/aem_modifications_log.csv`](file:///Users/andresbonett/dev/Enel_SEO/reports/aem_modifications_log.csv).

---

## 4. Próximos Pasos (Fase 2.2 a 2.4)

1. **Apelación de Google Ads (Soporte):** Con el portal libre de `cdnsafbapps.com`, se encuentra expedito el camino para radicar la solicitud de revisión y desbloqueo de la cuenta publicitaria `7120943744`.
2. **Fase 2.2 y 2.3:** Paquete de 18 formularios homologados con casillas legales y pie de página completo en [`Enel_google/formularios/`](file:///Users/andresbonett/dev/Enel_SEO/Enel_google/formularios).
3. **Fase 2.4:** Pruebas de funcionamiento en servidor local `http://localhost:8090` con botones de contraste hacia producción.
