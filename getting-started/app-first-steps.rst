.. _app-first-steps:

================================
First Steps with Applications
================================

The CloudBees Platform as a Service (PaaS) allows you to deploy your
application packages (ex: WAR files, ZIP'd directories, etc) and run them
in application containers so that can be accessed by end-users.

.. sidebar:: Basic Steps
    :subtitle: Follow these steps to deploy an app

    - Subscribe to the Application Service
    - Install the :ref:`sdk`
    - Create an application package
    - Deploy using *bees app:deploy*

Applications are identified by a unique ID (formed ACCOUNT/APPNAME) that lets
you associate settings, configuration parameters and resource bindings with
your application.

Once your app is deployed, the PaaS will setup the runtime container to host
your application, injecting configured parameters and resources, and sets up
routing rules for sending requests to your application instances.

Subscribe to the Application Service
------------------------------------

To get started with deploying applications you first need to subscribe to the
RUN\@cloud Application Service.  To do this, sign in to :ref:`grandcentral`, browse to
the Ecosystem, and subscribe to one of the Application Service plans.

`Subscribe now <https://grandcentral.cloudbees.com/services/plans/application>`_

Install the CloudBees SDK
-------------------------

Install the :ref:`sdk` to provide a command line interface for deploying
applications and managing resources on your CloudBees account.

A Trivial Deployment Example 
----------------------------

The most basic example of deploying an app to Cloudbees is to zip up a webapp
directory structure (with some static HTML files in it) and deploy it using
the following commands:

.. code-block:: bash

   $ zip /Home/myappdir myapp.zip

   $ bees app:deploy --appid myapp myapp.zip
   Deploying application: acme/myapp
   Uploading application deltas ...
   ........................uploaded 25%
   ........................uploaded 50%
   ........................uploaded 75%
   ........................upload completed
   deploying application to server(s)...
   Application acme/myapp deployed: http://myapp.acme.cloudbees.net

After the command completes, the files from /Home/myappdir will be avaialble
from the URL that was automatically created for your application.

Where to go from here
=====================

If you want to learn more you should continue to the
:ref:`Next Steps <app-next-steps>` tutorial, and after that you
can study the :ref:`app-guide`.
