.. _app-guide:

==================
 Application Guide
==================

This section provides a detailed overview of deploying applications
to the CloudBees Platform as a Service (RUN@cloud).

Your applications are identified by an ID (formatted ACCOUNT/APPNAME) that lets
you associate settings, configuration parameters and resource bindings with
your application.

Once your app is deployed, the PaaS takes responsibility for setting up a
runtime container based on settings you have defined and will inject
configuration parameters and resources (databases, monitors, etc) that will be
available to your application at runtime.


.. toctree::

    deploying-apps
    app-settings
    app-config-params
    app-resources
    production/index
