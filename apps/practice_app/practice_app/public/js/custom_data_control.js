frappe.ui.form.ControlCustomCurrency =
    class ControlCustomCurrency extends frappe.ui.form.ControlCurrency {

        get_precision() {
            return 3;
        }

    };