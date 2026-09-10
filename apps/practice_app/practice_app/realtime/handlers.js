function practice_app_handlers(socket) {

    console.log("🔥 PRACTICE APP HANDLERS LOADED");

    socket.on("project_subscribe", (project) => {

        console.log("🔥 EVENT RECEIVED");
        console.log("Project:", project);
        console.log("Socket ID:", socket.id);

    });
}

module.exports = practice_app_handlers;