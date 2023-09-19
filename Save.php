<?php
// Receive data from the Python script via HTTP POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Data sent
    $data = $_POST;

    // Generate a unique filename based on the current timestamp
    $timestamp = time();
    $file_path = "data_$timestamp.txt";

    // Open the file for writing (create if it doesn't exist)
    $file = fopen($file_path, "w");

    if ($file) {
        // Convert data to a text string and store it in the file
        fwrite($file, json_encode($data, JSON_PRETTY_PRINT));

        // Close the file
        fclose($file);

        // Send a success response with the filename
        echo "[+] Sended";
    } else {
        // If unable to open the file for writing
        echo "Failed to open the file for writing.";
    }
} else {
    // If no POST requests found
    echo "No POST Requests Found.";
}
?>
