import frappe

def get_context(context):
    context.cache = 0
    
    context["logo"] = (
            frappe.db.get_single_value("Website Settings", "app_logo")
            or frappe.get_hooks("app_logo_url")[-1]
        )