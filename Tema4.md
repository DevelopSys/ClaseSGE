# Acciones - Actions

Actions define the behavior of the system in response to user actions: login, action button, selection of an invoice, …
Actions can be stored in the database or returned directly as dictionaries in e.g. button methods. All actions share two mandatory attributes:

- type
  the category of the current action, determines which fields may be used and how the action is interpreted
- name
  short user-readable description of the action, may be displayed in the client’s interface

# Tipos de acciones

## Windows actions

The most common action type, used to present visualisations of a model through views: a window action defines a set of view types (and possibly specific views) for a model (and possibly specific record of the model).

## URL actions

Allow opening a URL (website/web page) via an Odoo action. Can be customized via two fields:

## Server actions

Server actions model. Server action work on a base model and offer various type of actions that can be executed automatically, for example using base action rules, of manually, by adding the action in the ‘More’ contextual menu.

## Reports action

Triggers the printing of a report.
If you define your report through a <record> instead of a <report> tag and want the action to show up in the Print menu of the model’s views, you will also need to specify binding_model_id from Bindings. It’s not necessary to set binding_type to report, since ir.actions.report will implicitly default to that.

## Client action

Triggers an action implemented entirely in the client.

## Automated action

Actions triggered automatically on a predefined frequency.
