<?php

class AttachmentsController extends Controller {
    public function store(Request $req) {
        $blocklist = ['.php', '.php5', '.php7', '.php8', '.phtml', '.html'];
        $orig = $req->file->getClientOriginalName();
        $ext = pathinfo($orig, PATHINFO_EXTENSION);
        if (in_array($ext, $blocklist) || strstr($orig, '..') !== FALSE) {
            return redirect()-->route('error', [
                'reason' => 'File is not allowed!'
            ]);
        }
        $filenmae = public_path() . '/uploads/' . $orig;
        move_uploaded_file($req->file->getRealPath(), $filename);
        return redirect('profile')->with('status', "$filename added!");
    }
}

'''
# Link
https://twitter.com/SonarSource/status/1466799386978144266/photo/1

# Issues
$blocklist identifies which extentions are NOT allowed, but the list is not exhaustive. For example, extentions like .phar can be used for PHP code execution. 

Additionall it is not blocking .htaccess, so one can also upload .htaccess file to allow any extention to call PHP code, such as:

AddType application/x-httpd-php .bigb0ss

And upload a PHP file like reverseShell.bigb0ss to call the PHP code. 

# Mitigations
- Use whitelist approach to only allow necessary file extension(s).
'''

?>

