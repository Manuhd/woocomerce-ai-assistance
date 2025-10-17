# WooCommerce API Local Integration

This project demonstrates fetching WooCommerce products from a **local WordPress environment** (`.local`) using Python. It is intended for **development and testing purposes**.

---

## Features

- Fetch products from a WooCommerce local site.
- Compatible with WooCommerce REST API v3.
- Supports **query string authentication** for local development.
- Temporary filter to allow API access on local `.local` sites without 401 errors.
- Safe for local testing; does **not bypass permissions in production**.

---

## Prerequisites

- WordPress installed locally (e.g., LocalWP, XAMPP, WAMP)
- WooCommerce plugin installed and active
- Python 3.x
- `requests` Python library

---

## Setup

1. Clone this repository or download the files.
2. Ensure your WordPress local site resolves correctly:

3. Install WooCommerce plugin and create an **API key**:
- Go to **WooCommerce → Settings → Advanced → REST API → Add Key**
- User: Administrator
- Permissions: Read/Write (or Read-only)
- Copy `Consumer Key` and `Consumer Secret`

4. Add the **temporary filter** for local API access in `functions.php` or a plugin:

```php
add_filter('woocommerce_rest_check_permissions', function($permission = false, $context = '', $object_id = 0, $post_type = '', $user_id = null, $cap = '') {
 if (strpos($_SERVER['HTTP_HOST'], '.local') !== false) {
     return true;
 }
 return $permission;
}, 10, 6);

