// export_markers.jsx
// Run this script in Adobe Premiere Pro to export timeline markers to a JSON file.

app.enableQE();
var project = app.project;
var sequence = project.activeSequence;

if (sequence) {
    var markers = sequence.markers;
    var numMarkers = markers.numMarkers;
    var exportedData = [];

    var currentMarker = markers.getFirstMarker();
    
    while (currentMarker) {
        var markerData = {
            "name": currentMarker.name,
            "comments": currentMarker.comments,
            "start": currentMarker.start.seconds,
            "end": currentMarker.end.seconds
        };
        exportedData.push(markerData);
        currentMarker = markers.getNextMarker(currentMarker);
    }

    // Save to file on Desktop
    var outputPath = Folder.desktop.fsName + "/premiere_markers.json";
    var file = new File(outputPath);
    file.open("w");
    // Simple JSON stringify fallback for ExtendScript
    file.write(JSON_stringify(exportedData));
    file.close();

    alert("Exported " + numMarkers + " markers to Desktop/premiere_markers.json");
} else {
    alert("Please open a sequence with markers first.");
}

function JSON_stringify(obj) {
    var arr = [];
    for (var i = 0; i < obj.length; i++) {
        arr.push('{"prompt": "' + obj[i].name + '", "time": ' + obj[i].start + '}');
    }
    return "[" + arr.join(",") + "]";
}
