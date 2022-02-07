<?php

class AttachmentsController extends Controller
{
    public function store(Request $request)
    {
        $orig = $request->file->getClientOriginalName();
        if (strstr($orig, '..') !== FALSE) {
            return redirect()->route('error', [
                'reason' => 'File is not allowed'
            ]);
        }
        $filename = public_path() . '/uploads/' . mt_rand();
        move_uploaded_file($request->file->getRealPath(), $filename);
        return redirect('attachments')->with('status', "$filename added!");
    }
}


'''
# Link
https://twitter.com/SonarSource/status/1467161775951032325

# Issues
1) `$filename` disclose the file root for the uploaded files.
2) Apache does not attach a Content-Type header for the files that are uploaded w/o any file extensions, which modern browsers will interpret the files as HTML --> vulnerable to XSS attacks.

# Mitigations
1) If only files with extensions are allowed, then implement a validation for `.` or specific file extension chekc (e.g., doc, xls, etc.).
2) Add a code to force attach Content-Type header for any uploaded files. (Not 100% sure if it is feasible with PHP).
'''

?>

