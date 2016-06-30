<?php

/* Configuration */
$subject = 'Free Trial Registration'; // Set email subject line here
$mailto  = 'ramnorgrup@gmail.com'; // Email address to send form submission to
/* END Configuration */

$name      = $_POST['name'];
$email          = $_POST['email'];
$timestamp = date("F jS Y, h:iA.", time());

// HTML for email to send submission details
$body = "
<br>
<p>The following information was submitted through the contact form on your website:</p>
<p><b>Name</b>: $name<br>
<b>Email</b>: $email</p>
<p>This form was submitted on <b>$timestamp</b></p>
";

// Success Message
$success = "
<form class=\"registration-form\" action=\"registration.php\">
	<fieldset>
		<div class=\"form-group\">
			<input id=\"name\" name=\"name\" type=\"text\" class=\"optin-input\" placeholder=\" \">
		</div>
		<div class=\"form-group\">
			<input id=\"email\" name=\"email\" type=\"email\" class=\"optin-input\" placeholder=\" \">
		</div>
		<div class=\"form-group\">
			<button class=\"btn btn-top-white btn-lg\" type=\"submit\">Get Started</button>
		</div>											
	</fieldset>
</form>
<div class=\"alert alert-info\">
	<button type=\"button\" class=\"close\" data-dismiss=\"alert\">&times;</button>
	<strong>Registration Successful!</strong> You will receive your Free Trial in a short moment.
</div>
";

$headers = "From: $name <$email> \r\n";
$headers .= "Reply-To: $email \r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
$message = "<html><body>$body</body></html>";

if (mail($mailto, $subject, $message, $headers)) {
    echo "$success"; // success
} else {
    echo 'Form submission failed. Please try again...'; // failure
}

?>