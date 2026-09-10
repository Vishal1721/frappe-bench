print("🔥 REALTIME HANDLERS LOADED")
from frappe.realtime import Socket, realtime
import frappe
@realtime.on("project_subscribe")
def project_subscribe(socket: Socket, project: str):

    print("Socket ID:", socket.id)
    print("Before:", socket.rooms)

    if socket.has_permission("Project", project):
        socket.join(f"project:{project}")

    print("After:", socket.rooms)
