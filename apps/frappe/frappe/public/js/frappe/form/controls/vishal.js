frappe.ui.form.ControlVishal = class ControlVishal extends frappe.ui.form.ControlData {
    make_input() {
        super.make_input();

        this.$input.on("input", () => {
            this.$input.val(this.$input.val().toUpperCase());
            
        });
    }
};
