import os
import sys
import re
import csv
import json
import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.aem_client import AEMClient

client = AEMClient()

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports", "aem_modifications_log.csv")

def log_modification(jcr_path, propiedad, anterior, nuevo, status_api):
    ts = datetime.datetime.now().isoformat()
    row = [ts, jcr_path, propiedad, anterior.replace("\n", " "), nuevo.replace("\n", " "), client.user, status_api]
    with open(LOG_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

def execute_remediation(dry_run=True):
    print(f"=== INICIANDO REMEDIACIÓN FASE 2.1 (DRY_RUN={dry_run}) ===", flush=True)
    
    # 1. CDNSAFBAPPS NODES
    res = client.query_builder({
        'path': '/content/enel-co',
        'fulltext': 'cdnsafbapps',
        'p.limit': '50'
    })
    
    hits = res.get('hits', [])
    print(f"\n[1] Nodos con cdnsafbapps a limpiar: {len(hits)}", flush=True)
    
    for hit in hits:
        path = hit.get('path')
        data = client.get_node_json(path, depth=1)
        old_text = data.get('text', '')
        
        # Remove img tag with cdnsafbapps (including optional wrapping <p> or <br>)
        new_text = re.sub(r'<p[^>]*>\s*<img[^>]+cdnsafbapps[^\'\">]+[\'\"][^>]*>\s*(?:<br\s*/?>)?\s*</p>', '', old_text, flags=re.IGNORECASE)
        new_text = re.sub(r'<img[^>]+cdnsafbapps[^\'\">]+[\'\"][^>]*>', '', new_text, flags=re.IGNORECASE)
        
        if old_text != new_text:
            print(f"  -> Nodo: {path}", flush=True)
            print(f"     Longitud anterior: {len(old_text)} | Nueva: {len(new_text)} (Reducción: {len(old_text) - len(new_text)} chars)", flush=True)
            if not dry_run:
                # Backup
                bf = client.backup_node(path)
                # Update
                status = client.post_node(path, {'text': new_text})
                # Replicate page
                rep_page = path.split('/jcr:content')[0]
                rep_status = client.replicate_page(rep_page)
                log_modification(path, 'text', '[HTML con img cdnsafbapps]', '[HTML sanitizado sin llamada externa]', status)
                print(f"     [POST {status}] [REPLICATE {rep_status}] Backup: {os.path.basename(bf)}", flush=True)
    
    # 2. ENGLISH FOOTER
    en_footer_path = '/content/enel-co/en/jcr:content/footer'
    en_footer = client.get_node_json(en_footer_path, depth=1)
    old_copy = en_footer.get('copyRightLabel', '')
    new_copy = 'Enel Colombia S.A. ESP 2026'
    print(f"\n[2] Footer en inglés: {en_footer_path}", flush=True)
    print(f"    copyRightLabel actual: '{old_copy}' -> nuevo: '{new_copy}'", flush=True)
    if not dry_run:
        bf = client.backup_node(en_footer_path)
        status = client.post_node(en_footer_path, {'copyRightLabel': new_copy})
        rep_status = client.replicate_page('/content/enel-co/en')
        log_modification(en_footer_path, 'copyRightLabel', old_copy, new_copy, status)
        print(f"    [POST {status}] [REPLICATE {rep_status}] Backup: {os.path.basename(bf)}", flush=True)
        
    # 3. BROKEN FORM LINK (leads-mr-no-regulado-2026 -> contacto-mr-no-regulado-2026)
    mr_node = '/content/enel-co/es/megamenu/empresas/enel-generacion/jcr:content/hub-content/group_copy_162707897/hubGroup-module/module_content_copy__1300614356/url'
    mr_data = client.get_node_json(mr_node, depth=1)
    old_mr_path = mr_data.get('path', '')
    new_mr_path = 'https://cloud.customer.enelx.com/contacto-mr-no-regulado-2026'
    print(f"\n[3] Enlace roto 404 en AEM: {mr_node}", flush=True)
    print(f"    path actual: '{old_mr_path}' -> nuevo: '{new_mr_path}'", flush=True)
    if not dry_run:
        bf = client.backup_node(mr_node)
        status = client.post_node(mr_node, {'path': new_mr_path})
        rep_page = mr_node.split('/jcr:content')[0]
        rep_status = client.replicate_page(rep_page)
        log_modification(mr_node, 'path', old_mr_path, new_mr_path, status)
        print(f"    [POST {status}] [REPLICATE {rep_status}] Backup: {os.path.basename(bf)}", flush=True)
        
    print(f"\n=== FIN DE REMEDIACIÓN (DRY_RUN={dry_run}) ===", flush=True)

if __name__ == '__main__':
    import sys
    dry = '--apply' not in sys.argv
    execute_remediation(dry_run=dry)
