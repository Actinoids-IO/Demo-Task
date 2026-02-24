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


Module 1 — Agency Management
Overview
The Agency Management module is developed to manage agencies that supply items and to maintain procurement-related information such as supplied items and lead times.
This module demonstrates ERPNext v15 capabilities including custom DocTypes, client-side actions, server-side methods, and reporting structure.

Relationship
One Agency → Multiple Agency Items.

Functional Implementation
1. Agency Status Management
A custom button dynamically appears on the form:
Disable Agent → sets status to In Active
Enable Agent → sets status back to Active
This allows quick operational control without manual field editing.

2. Create Supplier Integration
A server-side whitelisted method enables creation of a Supplier directly from an Agency.
Behavior
Clicking Create Supplier creates a new ERPNext Supplier document.
Supplier details are auto-populated:
Supplier Name from Agency
Supplier Type set as Company
Country set as India
Agency status is updated after supplier creation.
Benefit
Reduces duplicate data entry and connects agency records with ERPNext purchasing workflows.

3. Client-Side Customization
Form behavior is extended using a client script:
Conditional button rendering based on agency status.
UI-driven actions for enabling/disabling agencies.
Supplier creation triggered through mapped document logic.


Module 2 — Manufacturer–Item Mapping
Overview
The Manufacturer–Item Mapping module is designed to manage relationships between manufacturers and ERPNext items along with their manufacturer-specific identifiers.
This module demonstrates master data modeling, business validations, automated field handling, REST API exposure, and reporting within ERPNext v15.

Functional Implementation
1. Blocked Manufacturer Validation
When a Manufacturer is marked as blocked, users are prevented from creating or saving Manufacturer Item records linked to it.
Logic
During validation, the system checks manufacturer status.
If blocked, document save is stopped with an error message.
Purpose
Ensures restricted manufacturers cannot be used operationally.

2. Unique Manufacturer–Item Mapping
The system enforces uniqueness for the combination:
(manufacturer, item_code)

Duplicate mappings are not allowed.
Benefit
Maintains data integrity and avoids conflicting manufacturer references.

3. Automatic Part Number Handling
If part_number is left empty during creation:
The system automatically assigns the ERPNext item_code as the part number.
Purpose
Reduces manual entry while ensuring required identification data exists.

4. REST API — Manufacturer Mappings
A custom whitelisted API endpoint exposes manufacturer mappings for external systems.
Functionality
Returns all manufacturer mappings for a provided item_code.

Example Usage
/api/method/demo_app.manufacturer.doctype.manufacturer_item_mapping.manufacturer_item_mapping.get_manufacturer_items?item_code=Heartmate





AI Usage
AI assistance was used only for preparing and refining project documentation, including README creation and formatting.
All functional design, implementation, and development logic were completed independently.


