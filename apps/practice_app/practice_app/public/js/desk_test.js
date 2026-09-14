const OriginalControlCurrency = frappe.ui.form.ControlCurrency;

frappe.ui.form.ControlCurrency = class ControlCurrency extends OriginalControlCurrency {
    format_for_input(value) {
        const formatted_value = super.format_for_input(value);

        if (formatted_value) {
            return "₹ " + formatted_value;
        }

        return formatted_value;
    }
};