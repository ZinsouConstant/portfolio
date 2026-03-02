<?php
if ($_SERVER["REQUEST_METHOD"] == "post") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);
    $subject = "Nouveau message depuis le portfolio";

    $to = "zinsouconstanta@gmail.com"; // ton adresse Gmail
    $headers = "From: " . $email . "\r\n";
    $headers .= "Reply-To: " . $email . "\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    $body = "Nom : $name\n";
    $body .= "Email : $email\n\n";
    $body .= "Message :\n$message\n";

    if (mail($to, $subject, $body, $headers)) {
        echo "<h2 style='color:green;text-align:center;'>✅ Message envoyé avec succès !</h2>";
    } else {
        echo "<h2 style='color:red;text-align:center;'>❌ Échec de l'envoi du message.</h2>";
    }
}
?>
