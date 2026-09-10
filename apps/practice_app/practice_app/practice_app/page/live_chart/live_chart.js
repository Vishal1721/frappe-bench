frappe.pages['live-chart'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Realtime Chart',
		single_column: true
	});
	$(wrapper).find(".layout-main-section").html(`
        <div id="chart"></div>
    `);

    const data = {
        datasets: [
            {
                name: "Live Value",
                values: [],
            },
        ],
    };

    const chart = new frappe.ui.RealtimeChart(
        "#chart",
        "test_event",
        8,
        {
            title: "My Realtime Chart",
            data: data,
            type: "line",
            height: 300,
        }
    );

    chart.start_updating();
};
