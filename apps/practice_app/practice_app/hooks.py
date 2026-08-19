app_name = "practice_app"
app_title = "Practice App"
app_publisher = "vishal"
app_description = "mastering frappe"
app_email = "vishal@gmail.com"
app_license = "mit"
test_string = ["hello from practice_app"]
fixtures = [
    "Client Script"
]
scheduler_events = {
    "daily": [
        "practice_app.tasks.daily_maintenance"
    
    ]
}
app_include_js = "/assets/practice_app/js/desk_test.js"
web_include_js = "/assets/practice_app/js/web_test.js"

web_include_css = "/assets/practice_app/css/web_test.css"
webform_include_js = {
    "employee form": "public/js/employee_form.js"
}
webform_include_css = {
    "employee form": "public/css/employee_form.css"
}

# sounds = [
#     {
#         "name": "ping",
#         "src": "/assets/practice_app/sounds/ping.mp3",
#         "volume": 0.2
#     }
# ]
# after_build = "practice_app.build.after_build"
before_install = "practice_app.setup.install.before_install"
after_install = "practice_app.setup.install.after_install"
after_sync = "practice_app.setup.install.after_sync"

before_tests = "practice_app.tests.before_tests"
# hooks.py


after_uninstall = "practice_app.setup.uninstall.after_uninstall"


# before_write_file = "practice_app.overrides.file.before_write"
# write_file = "practice_app.overrides.file.write_file"
delete_file_data_content = "practice_app.overrides.file.delete_file"
get_sender_details = "practice_app.overrides.email.get_sender_details"
website_context = {
    "company_name": "Practice Company",
    "support_email": "support@practice.com"
}   
extend_website_page_controller_context = {
    "frappe.www.404": "practice_app.pages.context_404"
}
website_catch_all = "not_found"
home_page = "homepage"
role_home_page= {
    "Customer":"customer-home",
    "Employee":"Employee-home"
}
# app_include_css = "/assets/practice_app/css/desk_test.css"
# Apps
# ----

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "practice_app",
# 		"logo": "/assets/practice_app/logo.png",
# 		"title": "Practice App",
# 		"route": "/practice_app",
# 		"has_permission": "practice_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/practice_app/css/practice_app.css"
# app_include_js = "/assets/practice_app/js/practice_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/practice_app/css/practice_app.css"
# web_include_js = "/assets/practice_app/js/practice_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "practice_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "practice_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "practice_app.utils.jinja_methods",
# 	"filters": "practice_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "practice_app.install.before_install"
# after_install = "practice_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "practice_app.uninstall.before_uninstall"
# after_uninstall = "practice_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "practice_app.utils.before_app_install"
# after_app_install = "practice_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "practice_app.utils.before_app_uninstall"
# after_app_uninstall = "practice_app.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "practice_app.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "practice_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"practice_app.tasks.all"
# 	],
# 	"daily": [
# 		"practice_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"practice_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"practice_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"practice_app.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "practice_app.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "practice_app.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "practice_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "practice_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["practice_app.utils.before_request"]
# after_request = ["practice_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["practice_app.utils.before_job"]
# after_job = ["practice_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"practice_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

