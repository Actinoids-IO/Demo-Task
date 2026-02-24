### Demo App

App for Demo

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app demo_app
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/demo_app
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit

###  About Development

Module 1 — Agency Management
Overview
The Agency Management module is developed to manage agencies that supply items and to maintain procurement-related information such as supplied items and lead times.
This module demonstrates ERPNext v15 capabilities including custom DocTypes, client-side actions, server-side methods, and reporting structure.




Module 2 — Manufacturer–Item Mapping
Overview
The Manufacturer–Item Mapping module is designed to manage relationships between manufacturers and ERPNext items along with their manufacturer-specific identifiers.
This module demonstrates master data modeling, business validations, automated field handling, REST API exposure, and reporting within ERPNext v15.

**REST API**  — Manufacturer Mappings
A custom whitelisted API endpoint exposes manufacturer mappings for external systems.
Returns all manufacturer mappings for a provided item_code.
Example Usage
/api/method/demo_app.manufacturer.doctype.manufacturer_item_mapping.manufacturer_item_mapping.get_manufacturer_items?item_code=Heartmate




###  AI Usage
AI assistance was used only for preparing and refining project documentation, including README creation and formatting.
All functional design, implementation, and development logic were completed independently.

