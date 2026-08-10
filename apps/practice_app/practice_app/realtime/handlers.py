from frappe.realtime import Socket, realtime
import frappe
@realtime.on("hello")
def hello(socket: Socket, name: str):
    frappe.msgprint("Received from browser:", name)

    socket.emit(
        "hello_response",
        {
            "message": f"Hello {name}!"
        }
    )