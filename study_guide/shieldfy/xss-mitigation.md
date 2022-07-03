# Mitigation for XSS
1. Sufficient (Server-side) input filtering
- HTML Escape
    - PHP
    ```php
    htmlspecialchars(USER_INPUT)
    ```

    - Python
    ```python
    import html
    
    html.escape(USER_INPUT)
    ```
- Attribute Escape
- JavaScript Escape
    - PHP
    ```php
    json_encode(USER_INPUT)
    ```

    - Python
    ```python
    import django.utils.html as html

    html.escapejs(USER_INPUT)
    ```

2. Client-side Defenses
- Activate Browser Defenses
    - `X-XSS-Protection: 1`
- CSP (Content Security Policy)
    - CSP is an added layer of security that helps to detect and mitigate certian types of attacks like XSS or data injection attacks. 